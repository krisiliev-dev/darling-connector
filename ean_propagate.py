# -*- coding: utf-8 -*-
"""PREFIX-BASED BRAND PROPAGATION (owner 2026-07-18).

A GS1 company prefix is licensed to ONE manufacturer, so every product sharing a
prefix shares a maker. If ANY product in a prefix group has a trustworthy brand (from
vision OCR / supplier scrape / gazetteer / a GS1 lookup), that brand applies to the
whole group. The barcode gives the grouping for free; the cheaper sources give the
name — turning sparse brand hits into broad coverage without 435 manual GS1 lookups.

Trust discipline (unchanged doctrine): a propagated brand is EVIDENCE, recorded in the
prefix cache as src="propagated" and surfaced in the /brands queue for owner confirm;
the ~30/day GS1 manual pass independently verifies each prefix (set_prefix warns on a
disagreement). Prefixes flagged own/distributor (bg_own_or_distributor) never propagate.
A prefix whose members carry DIFFERENT confirmed brands is a shared/generic prefix →
skipped, not guessed.

  python ean_propagate.py            # dry-run: what would propagate, conflicts
  python ean_propagate.py --apply    # write prefix cache + queue member candidates
  python ean_propagate.py --apply --restamp   # also set Бранд + recompose names now
"""
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

import ean_brand as eb

HERE = Path(__file__).parent


def _member_brands():
    """{prefix: {code: brand}} for products that currently HAVE a brand, over GS1,
    non-flagged prefixes only."""
    cache = eb.prefix_cache()
    code_pfx = defaultdict(set)
    for d in eb._load(eb.BARCODES):
        if d.get("cls") == "gs1" and d.get("prefix"):
            p = d["prefix"]
            h = cache.get(p) or {}
            if not (h.get("bad") or h.get("distributor") or h.get("multi_brand")):
                code_pfx[str(d["code"])].add(p)   # skip own/distributor/multi-brand
    import db
    con = db.connect()
    rows = con.execute("SELECT code, fields_json FROM products "
                       "WHERE fields_json IS NOT NULL").fetchall()
    con.close()
    out = defaultdict(dict)
    for code, fj in rows:
        code = str(code)
        if code not in code_pfx:
            continue
        try:
            b = str(json.loads(fj or "{}").get("Бранд") or "").strip()
        except Exception:
            b = ""
        if b:
            for p in code_pfx[code]:
                out[p][code] = b
    return out, code_pfx


def _dominant(brands, gaz):
    """Given {code: brand} in a prefix group, return (brand, evidence_codes, conf) or
    (None, reason, None). A brand is a valid SEED only if it is gazetteer-confirmed OR
    independently carried by >=2 members — a lone raw brand (pre-run these are untrusted
    v1 hints) never propagates across a whole group. One surviving seed -> propagate; two
    surviving seeds -> real conflict, skip (likely a shared/house/generic prefix)."""
    canon = defaultdict(list)                              # canonical -> [codes]
    known_flag = {}
    for code, b in brands.items():
        known = eb_lookup(b, gaz)
        key = known or b.strip()
        canon[key].append(code)
        known_flag[key] = known_flag.get(key, False) or bool(known)
    # keep only trustworthy seeds
    seeds = {k: v for k, v in canon.items() if known_flag[k] or len(v) >= 2}
    if not seeds:
        return None, "weak_single_unknown", None
    if len(seeds) == 1:
        brand, codes = next(iter(seeds.items()))
        conf = "high" if (known_flag[brand] and len(codes) >= 2) else \
               "gazetteer" if known_flag[brand] else "repeat"
        return brand, codes, conf
    return None, "conflict:" + "/".join(sorted(seeds)), None


def eb_lookup(cand, gaz):
    import brand_tools
    return brand_tools.lookup(cand, gaz)


def run(apply=False, restamp=False):
    import brand_tools
    gaz = brand_tools.load()
    member, code_pfx = _member_brands()
    cache = eb.prefix_cache()
    def _asserts(p):
        h = cache.get(p) or {}
        return not (h.get("bad") or h.get("distributor") or h.get("multi_brand"))
    all_pfx = {d["prefix"] for d in eb._load(eb.BARCODES)
               if d.get("cls") == "gs1" and d.get("prefix") and _asserts(d["prefix"])}
    group_size = defaultdict(int)
    for _c, ps in code_pfx.items():
        for p in ps:
            group_size[p] += 1

    propagate = {}          # prefix -> (brand, evidence_codes, conf)
    conflicts = []
    for p in all_pfx:
        brands = member.get(p) or {}
        if not brands:
            continue                                       # no seed brand yet
        brand, ev, conf = _dominant(brands, gaz)
        if brand is None:
            if str(ev).startswith("conflict"):
                conflicts.append((p, ev, group_size[p]))
            continue
        already = (cache.get(p) or {}).get("brand")
        if already and already == brand:
            continue                                       # nothing new
        propagate[p] = (brand, ev, conf)

    covered = sum(group_size[p] for p in propagate)
    print(f"{len(all_pfx)} live prefixes | {len(propagate)} get a propagated brand "
          f"(covering {covered} products in their groups) | {len(conflicts)} conflicts")
    for p, (brand, ev, conf) in sorted(propagate.items(),
                                       key=lambda kv: -group_size[kv[0]])[:20]:
        print(f"  {p}  -> {brand!r}  (seed {len(ev)}/{group_size[p]} products, {conf})")
    if conflicts:
        print("CONFLICTS (different confirmed brands share a prefix — likely generic/"
              "shared, skipped):")
        for p, reason, n in sorted(conflicts, key=lambda x: -x[2])[:10]:
            print(f"  {p} ({n} products): {reason}")

    if not apply:
        print("\n(dry-run — rerun with --apply to write)")
        return
    # 1) write propagated brands into the prefix cache (becomes the 'ean' source)
    with eb.PREFIX_CACHE.open("a", encoding="utf-8") as fh:
        for p, (brand, ev, conf) in propagate.items():
            fh.write(json.dumps({"prefix": p, "owner": None, "brand": brand,
                                 "src": "propagated", "conf": conf, "evidence": ev[:8],
                                 "needs_gs1_confirm": True,
                                 "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                                ensure_ascii=False) + "\n")
    eb._bycode_cache["v"] = None
    # 2) queue member products that lack the brand, so /brands shows the whole group
    queued = 0
    for p, (brand, ev, _m) in propagate.items():
        have = set(ev)
        for code in [c for c, ps in code_pfx.items() if p in ps and c not in have]:
            brand_tools.queue_candidate(code, brand, ["ean_propagate"], "")
            queued += 1
    print(f"applied: {len(propagate)} prefixes cached; {queued} products queued for "
          f"owner confirm; worklist marks them for GS1 verification")
    if restamp:
        _restamp(propagate, code_pfx)


def _restamp(propagate, code_pfx):
    """Directly set Бранд + recompose the name for every product gaining a propagated
    brand (mirrors the /brands accept flow). Only touches products currently brandless."""
    import db
    import json as _j
    from datetime import datetime as _dt
    import name_builder as nb
    vocab = nb.load_vocab()
    pfx_brand = {p: b for p, (b, _e, _m) in propagate.items()}
    con = db.connect()
    changed = 0
    with open(HERE / "results.lanez_brandfix.jsonl", "a", encoding="utf-8") as fh:
        for code, ps in code_pfx.items():
            brand = next((pfx_brand[p] for p in ps if p in pfx_brand), None)
            if not brand:
                continue
            r = con.execute("SELECT record_json FROM products WHERE code=?",
                            (code,)).fetchone()
            if not r:
                continue
            rec = _j.loads(r[0])
            fl = dict(rec.get("fields") or {})
            if str(fl.get("Бранд") or "").strip():
                continue                                   # never overwrite an existing brand
            fl["Бранд"] = brand
            nm, _rs = nb.build_name(fl, vocab)
            if nm:
                fl["Наименование"] = nm
            nd = dict(rec, fields=fl, ts=_dt.now().isoformat(timespec="seconds"))
            meta = dict(nd.get("meta") or {})
            meta["notes"] = list(dict.fromkeys(
                list(meta.get("notes") or []) + ["v2", "brand_ean_propagated"]))
            nd["meta"] = meta
            fh.write(_j.dumps(nd, ensure_ascii=False) + "\n")
            db.record_version(nd)
            changed += 1
    con.close()
    print(f"restamped: {changed} brandless products got a propagated brand + new name")


if __name__ == "__main__":
    run(apply="--apply" in sys.argv, restamp="--restamp" in sys.argv)
