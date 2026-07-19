# -*- coding: utf-8 -*-
"""POST-RUN name dedupe (audit finding: v2 composes names per-product with no global
uniqueness — run this once after the full v2 pass, and after any mass re-render).

Groups identical canonical Наименование values; keeps the first product as-is and
disambiguates the rest by appending (in order of availability) Цвят, Обем, Модел, or
the product code. Writes disambiguations as new versions (visible as diffs).

  python dedupe_names.py            # dry-run report
  python dedupe_names.py --apply
"""
import json
import re
import sys
from datetime import datetime

import db

HERE = __file__


def main(apply=False):
    con = db.connect()
    rows = con.execute("SELECT code, record_json FROM products WHERE record_json IS NOT NULL").fetchall()
    by_name = {}
    recs = {}
    for code, rj in rows:
        rec = json.loads(rj)
        recs[str(code)] = rec
        nm = str((rec.get("fields") or {}).get("Наименование") or "").strip()
        if nm:
            by_name.setdefault(nm, []).append(str(code))
    dups = {n: cs for n, cs in by_name.items() if len(cs) > 1}
    print(f"{len(dups)} duplicate name groups covering "
          f"{sum(len(c) for c in dups.values())} products")
    n_fixed = 0
    out = open("results.lanez_dedupe.jsonl", "a", encoding="utf-8") if apply else None
    for nm, codes in sorted(dups.items()):
        for c in codes[1:]:                              # first keeps the clean name
            rec = recs[c]
            f = dict(rec.get("fields") or {})
            attrs = {k.strip().lower(): v.strip() for k, v in
                     (p.split(":", 1) for p in str(f.get("Атрибути") or "").split(";")
                      if ":" in p)}
            suffix = attrs.get("цвят") or attrs.get("обем") or attrs.get("модел") or c
            new_nm = f"{nm} {suffix.lower() if suffix != c else '(' + c + ')'}"
            if new_nm in by_name:
                new_nm = f"{nm} ({c})"
            by_name.setdefault(new_nm, []).append(c)
            if len(codes) <= 4 or apply:
                print(f"  {c}: {nm!r} -> {new_nm!r}")
            if apply:
                nd = dict(rec)
                nd["fields"] = dict(f, **{"Наименование": new_nm})
                nd["ts"] = datetime.now().isoformat(timespec="seconds")
                meta = dict(nd.get("meta") or {})
                meta["notes"] = list(meta.get("notes") or []) + ["v2", "name_dedupe"]
                nd["meta"] = meta
                out.write(json.dumps(nd, ensure_ascii=False) + "\n")
                db.record_version(nd)
                n_fixed += 1
    if out:
        out.close()
        print(f"applied {n_fixed} disambiguations")
    con.close()


if __name__ == "__main__":
    main(apply="--apply" in sys.argv)
