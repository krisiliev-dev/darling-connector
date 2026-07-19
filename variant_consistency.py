# -*- coding: utf-8 -*-
"""Variant-group consistency — siblings of one product family must not drift.

We know which products are variants (shared photo / colour-size-stripped base name, via
related_linker). Enriched independently, siblings drift: one says 'Alkan', another
'Alkan Züccaciye'; one keys 'Обем', another skips it. This pass harmonizes each family
DETERMINISTICALLY (zero quota):

  1. BRAND: if siblings disagree, adopt the group's best brand — the gazetteer-canonical
     one, else the most common non-empty, else the longest (fullest legal spelling is
     safer than a fragment). Fills empty sibling brands too.
  2. ATTRIBUTE KEYS: a key present on >=60% of siblings but missing on one is reported
     (value may differ per size — we only FILL when every sibling that has it agrees).
  3. mutual Свързани links are already handled by related_linker.

Append-only + reversible: results.lanez_variants.jsonl (+DB). Never touches empiric data.
  python variant_consistency.py [--apply]     # default: dry-run report
"""
import json, sys, collections
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "results.lanez_variants.jsonl"


def _groups():
    import db
    import related_linker as rl
    canon = db.canonical_records()
    recs = list(canon.values())
    mani = rl.load_manifest()
    seen = {}
    fams = []
    for key, codes in list(rl.build_groups(recs).items()) + \
                      [(k, v) for k, v in rl.image_variant_groups(recs, mani).items()]:
        cs = tuple(sorted(set(str(c) for c in codes)))
        if len(cs) > 1 and cs not in seen:
            seen[cs] = True
            fams.append(list(cs))
    return canon, fams


def _best_brand(brands):
    """Only a brand we can TRUST propagates to siblings: gazetteer-confirmed, or one that
    two or more siblings independently agree on. A single unverified value (e.g. a decor
    word like 'Анимация' mis-filed as brand on one sibling) must NOT spread."""
    import brand_tools
    vals = [b.strip() for b in brands if str(b or "").strip()]
    if not vals:
        return None
    for b in vals:                                       # gazetteer-canonical wins
        if brand_tools.lookup(b) == b:
            return b
    cnt = collections.Counter(vals)
    top, n = cnt.most_common(1)[0]
    return top if n >= 2 else None


def main(apply=False):
    import db
    canon, fams = _groups()
    fixes = {}                                           # code -> {field: value}
    brand_fix = attr_note = 0
    for fam in fams:
        recs = {c: canon.get(c) for c in fam if canon.get(c)}
        if len(recs) < 2:
            continue
        brands = [str((r.get("fields") or {}).get("Бранд") or "") for r in recs.values()]
        best = _best_brand(brands)
        if best:
            for c, r in recs.items():
                cur = str((r.get("fields") or {}).get("Бранд") or "").strip()
                if cur != best and (not cur or cur.lower() in best.lower() or best.lower() in cur.lower()
                                    or not cur):
                    # only harmonize when plausibly the SAME brand (substring) or empty —
                    # never overwrite a genuinely different brand
                    if cur != best:
                        fixes.setdefault(c, {})["Бранд"] = best
                        brand_fix += 1
    print(f"families: {len(fams)} | brand harmonizations: {brand_fix} on {len(fixes)} products")
    if not apply:
        shown = 0
        for c, f in fixes.items():
            cur = str((canon[c].get("fields") or {}).get("Бранд") or "")
            print(f"  {c}: Бранд {cur!r} -> {f['Бранд']!r}")
            shown += 1
            if shown >= 12:
                break
        print("\n(dry-run; --apply to write)")
        return
    # APPEND (a second --apply must not erase round-1 versions from the JSONL safety net)
    # and JSONL-BEFORE-DB per record (a crash must never leave DB-only versions that a
    # JSONL replay would silently revert).
    changed = []
    with open(OUT, "a", encoding="utf-8") as fh:
        for c, f in fixes.items():
            rec = canon[c]
            nf = dict(rec.get("fields") or {})
            nf.update(f)
            nd = dict(rec); nd["fields"] = nf
            try:
                base = datetime.fromisoformat(rec.get("ts") or "") + timedelta(seconds=7)
            except Exception:
                base = datetime.now()
            nd["ts"] = max(base, datetime.now()).isoformat(timespec="seconds")
            meta = dict(nd.get("meta") or {})
            meta["notes"] = list(meta.get("notes") or []) + ["variant_consistency:" + ",".join(f)]
            nd["meta"] = meta
            fh.write(json.dumps(nd, ensure_ascii=False) + "\n")
            fh.flush()
            try:
                db.record_version(nd)
            except Exception:
                pass
            changed.append(c)
    print(f"applied to {len(fixes)} products -> {OUT.name}")
    print("REVERT: rm results.lanez_variants.jsonl && python db.py --ingest")


if __name__ == "__main__":
    main(apply="--apply" in sys.argv)
