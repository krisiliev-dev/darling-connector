# -*- coding: utf-8 -*-
"""СВЪРЗАНИ rebuild — owner's definition (2026-07-18): connected products are THE SAME
product in another variant (colour / size / volume), nothing else.

Post-v2 this is decidable deterministically:
  group key = (taxonomy leaf, Бранд, base-name signature)
  where the signature is the composed Наименование minus colour words, dimensions,
  volumes and trailing codes — AND within a group two products link only if their
  ATTRIBUTES are identical except for AT MOST ONE group (owner 2026-07-18: a variant
  differs in exactly one thing — the colour OR the size — everything else matches).
  Large groups (>6) are first subdivided by catalogue-number letter-prefix.

Replaces both v1 mechanisms (catalogue ±1 adjacency — which linked neighbouring SKUs
like a леген next to a бидон — and TF-IDF similarity). Runs AFTER the v2 pass (it
needs composed names + leaf assignments); safe to re-run any time.

  python relate_rebuild.py            # dry-run: group stats + samples
  python relate_rebuild.py --apply    # write Свързани as new versions
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import db

HERE = Path(__file__).parent

COLORS = {"бял", "бяла", "бяло", "бели", "черен", "черна", "черно", "черни", "сив",
          "сива", "сиво", "сиви", "червен", "червена", "червено", "червени", "син",
          "синя", "синьо", "сини", "зелен", "зелена", "зелено", "зелени", "жълт",
          "жълта", "жълто", "жълти", "розов", "розова", "розово", "розови", "лилав",
          "лилава", "лилаво", "кафяв", "кафява", "кафяво", "бежов", "бежова", "бежово",
          "оранжев", "оранжева", "оранжево", "прозрачен", "прозрачна", "прозрачно",
          "сребрист", "сребриста", "сребристо", "златист", "златиста", "златисто",
          "тюркоазен", "тюркоазена", "тюркоазено", "многоцветен", "шарен", "шарена",
          "меден", "медна", "антрацит", "крем", "екрю", "мента", "бордо"}
_NUMUNIT = re.compile(r"(?:Ø|ø)?\s*\d+(?:[.,]\d+)?(?:\s*[x×х]\s*\d+(?:[.,]\d+)?)*"
                      r"\s*(?:см|мм|cm|mm|л|мл|l|ml|кг|г|бр)?\.?", re.I)


def signature(name):
    s = str(name or "").lower()
    s = re.sub(r"\([^)]*\)", " ", s)                     # trailing (codes)
    s = _NUMUNIT.sub(" ", s)                             # sizes / volumes / counts
    toks = [w for w in re.findall(r"[а-яa-z]+", s) if w not in COLORS and len(w) > 1]
    return " ".join(sorted(toks))


def _cat_prefix(catno):
    m = re.match(r"\s*([A-Za-zА-Яа-я]*)", str(catno or ""))
    return (m.group(1) or "_").lower()


def _attr_dict(fields):
    d = {}
    for part in str(fields.get("Атрибути") or "").split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            k = k.strip().lower()
            if k and k != "тип":                          # type is the group key already
                d[k] = re.sub(r"\s+", " ", v.strip().lower())
    return d


def _is_variant_pair(a, b):
    """True iff the attributes KNOWN ON BOTH SIDES are identical except for at most one
    group. A group missing on one side is UNKNOWN, not different (extraction gaps must
    not break true variants) — but at least two shared groups are required, so sparse
    records can't link on no evidence."""
    shared = set(a) & set(b)
    if len(shared) < 2:
        return False
    diffs = sum(1 for k in shared if a[k] != b[k])
    return diffs <= 1


def main(apply=False):
    con = db.connect()
    rows = con.execute(
        "SELECT p.code, p.record_json, pt.gid FROM products p "
        "LEFT JOIN product_taxonomy pt ON pt.code = p.code "
        "WHERE p.record_json IS NOT NULL").fetchall()
    groups = {}
    recs = {}
    known = set()
    for code, rj, gid in rows:
        code = str(code)
        known.add(code)
        rec = json.loads(rj)
        notes = [str(n) for n in ((rec.get("meta") or {}).get("notes") or [])]
        if "v2" not in notes:
            continue                                     # only composed-name records
        recs[code] = rec
        f = rec.get("fields") or {}
        key = (gid or "", str(f.get("Бранд") or "").strip().lower(),
               signature(f.get("Наименование")))
        groups.setdefault(key, []).append(code)
    linked = {}
    for key, codes in groups.items():
        if len(codes) < 2:
            continue
        if len(codes) > 6:                               # subdivide big same-name pools
            sub = {}
            for c in codes:
                cp = _cat_prefix((recs[c].get("fields") or {}).get("Каталожен номер"))
                sub.setdefault(cp, []).append(c)
            buckets = [v for v in sub.values() if len(v) >= 2]
        else:
            buckets = [codes]
        for b in buckets:
            attrs = {c: _attr_dict(recs[c].get("fields") or {}) for c in b}
            for c in b:
                rel = [x for x in b
                       if x != c and _is_variant_pair(attrs[c], attrs[x])]
                if rel:
                    linked[c] = rel[:10]
    n_groups = sum(1 for v in groups.values() if len(v) >= 2)
    print(f"{len(recs)} v2 products | {n_groups} variant groups | "
          f"{len(linked)} products get links")
    shown = 0
    for c, rel in list(linked.items()):
        f = recs[c]["fields"]
        if shown < 6:
            print(f"  {c} {str(f.get('Наименование'))[:46]!r} <-> {rel}")
            shown += 1
    changed = 0
    if apply:
        with open(HERE / "results.lanez_related.jsonl", "a", encoding="utf-8") as fh:
            for c, rec in recs.items():
                new_rel = ", ".join(linked.get(c, []))
                old_rel = str((rec.get("fields") or {}).get("Свързани") or "").strip()
                if new_rel == old_rel:
                    continue
                nd = dict(rec)
                nd["fields"] = dict(rec.get("fields") or {}, **{"Свързани": new_rel})
                nd["ts"] = datetime.now().isoformat(timespec="seconds")
                meta = dict(nd.get("meta") or {})
                meta["notes"] = list(dict.fromkeys(
                    list(meta.get("notes") or []) + ["v2", "related_rebuilt"]))
                nd["meta"] = meta
                fh.write(json.dumps(nd, ensure_ascii=False) + "\n")
                db.record_version(nd)
                changed += 1
        print(f"applied: Свързани rewritten on {changed} products "
              f"(incl. clearing stale links)")
    con.close()


if __name__ == "__main__":
    main(apply="--apply" in sys.argv)
