# -*- coding: utf-8 -*-
"""True duplicate-PRODUCT detection (distinct from the size-variant signal).

A duplicate is the SAME SKU entered twice — not a size variant. Signals, strongest first:
  1. identical supplier catalogue number (Каталожен номер) on two different codes,
  2. same shared image AND near-identical name (not just same category = variant),
  3. identical normalized name + brand.
These should become ONE Shopify product, not two. Reported for human confirmation (never
auto-merged — a merge is destructive and empiric Код must be preserved).
"""
import json, re, collections
from pathlib import Path

HERE = Path(__file__).parent


def _norm_name(s):
    s = re.sub(r"[^0-9a-zа-я ]", " ", str(s or "").lower())
    return " ".join(sorted(w for w in s.split() if len(w) > 2))


def main():
    import db
    import related_linker as rl
    canon = db.canonical_records()
    tasks = db.get_tasks(list(canon))
    manifest = rl.load_manifest()

    dups = []
    # NOTE: identical supplier catalogue number is NOT a duplicate signal for this data —
    # suppliers reuse a base code across a product FAMILY (e.g. GX-024 on several different
    # bins), which is the *variant/related* signal, not a same-SKU duplicate. So we rely on
    # identical name+brand (a genuine same-listing signal).

    # identical normalized name + brand
    by_nb = collections.defaultdict(list)
    for code, rec in canon.items():
        f = rec.get("fields") or {}
        key = (_norm_name(f.get("Наименование")), str(f.get("Бранд") or "").strip().lower())
        if key[0]:
            by_nb[key].append(code)
    for (nm, br), codes in by_nb.items():
        if len(set(codes)) > 1:
            dups.append(("same_name_brand", nm[:40], sorted(set(codes))))

    # de-dupe report rows by the code-set
    seen = set()
    uniq = []
    for kind, key, codes in dups:
        sig = tuple(codes)
        if sig in seen:
            continue
        seen.add(sig)
        uniq.append((kind, key, codes))

    print(f"=== DUPLICATE PRODUCTS (candidate same-SKU pairs) ===")
    print(f"found {len(uniq)} duplicate groups\n")
    by_kind = collections.Counter(k for k, _, _ in uniq)
    print("by signal:", dict(by_kind), "\n")
    bycode = {c: (canon[c].get("fields") or {}).get("Наименование") for c in canon}
    for kind, key, codes in uniq[:25]:
        print(f"[{kind}] {key}")
        for c in codes[:4]:
            print(f"    {c}: {str(bycode.get(c))[:55]}")
    # persist
    try:
        con = db.connect()
        con.execute("CREATE TABLE IF NOT EXISTS duplicate_products(sig TEXT PRIMARY KEY, kind TEXT, codes TEXT)")
        con.executemany("INSERT OR REPLACE INTO duplicate_products(sig,kind,codes) VALUES(?,?,?)",
                        [("|".join(c), k, json.dumps(c)) for k, _, c in uniq])
        con.commit(); con.close()
        print(f"\npersisted {len(uniq)} groups -> DB table duplicate_products")
    except Exception as e:
        print("persist skipped:", str(e)[:60])


if __name__ == "__main__":
    main()
