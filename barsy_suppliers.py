# -*- coding: utf-8 -*-
"""Product -> supplier mapping + Barsy supplier links (owner 2026-07-19).

The Microinvest export's "Група" column encodes the supplier per product, e.g.
"6/АНИС- ПЛОВДИВ", "7/ЛЕВЕНА- ПЛОВДИВ", "ВЕРТЕКС". We:
  1. parse a clean supplier name per code (dropping the "N/" prefix + "- CITY" suffix),
     excluding non-supplier buckets ("Служебна група" = unassigned, "Преоценени", ...);
  2. ensure each supplier exists in Barsy (Suppliers_create for missing ones);
  3. push the article<->supplier links via Suppliers_save_articles, carrying the supplier's
     own name for the product (remote_article_name = "Стока - име за печат", the print name)
     and the delivery price (default_delivery_price) — Barsy's "SourcedFrom" relation.

Only products already present in Barsy (with an article_id) can be linked. Coverage is
partial by nature: ~2/3 of products sit in "Служебна група" (no named supplier).

  python barsy_suppliers.py --suppliers        # show parsed supplier list + coverage
  python barsy_suppliers.py --ensure           # create missing suppliers in Barsy
  python barsy_suppliers.py --link --confirm    # push links for in-Barsy articles
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import barsy_api as b

HERE = Path(__file__).parent
EXPORT = Path(r"C:\Users\lora_\Desktop\Full Data per product.xlsx")

# "Група" buckets that are NOT external suppliers (product/ops buckets, not vendors)
NOT_SUPPLIER = {"преоценени", "покривки", "ин хаус", "подаръци",
                "ваучери", "полилей", "мушама", "nan", ""}
# owner-supplied: the default "Служебна група" bucket is (mostly) the Mira-N supplier
GROUP_ALIAS = {"служебна група": "MIRA-N"}


def _clean_name(group):
    """'6/АНИС- ПЛОВДИВ' -> 'АНИС' ; 'ЛЕВЧЕ СОФИЯ' -> 'ЛЕВЧЕ' ; '' if not a supplier."""
    g = re.sub(r"\s+", " ", str(group or "").strip())
    if g.lower() in GROUP_ALIAS:
        return GROUP_ALIAS[g.lower()]
    if not g or g.lower() in NOT_SUPPLIER:
        return ""
    g = re.sub(r"^\s*\d+\s*[/\-]\s*", "", g)              # drop leading "6/" / "13-"
    g = re.split(r"\s*/\s*", g)[0]                        # 'ДИЗАНИК/МУШАМА' -> 'ДИЗАНИК'
    g = re.sub(r"[\s\-]+(ПЛОВДИВ|СОФИЯ)\b.*$", "", g, flags=re.I)  # drop trailing CITY
    g = re.sub(r"^ААТАНАСОВ", "АТАНАСОВ", g)              # fix source double-А typo
    g = g.strip(" -/").strip().upper()                   # canonical case (merges Левче/ЛЕВЧЕ)
    return "" if g.lower() in NOT_SUPPLIER else g


def _export_rows():
    """{code: {supplier, print_name, delivery_price}} from the export."""
    import pandas as pd
    raw = pd.read_excel(EXPORT, sheet_name=0, header=None, dtype=str, engine="calamine")
    hi = next(i for i in range(15)
              if any(str(v).strip() == "Код" for v in raw.iloc[i].tolist()))
    cols = [str(v).strip() for v in raw.iloc[hi].tolist()]
    idx = {c: i for i, c in enumerate(cols)}
    ci, gi = idx["Код"], idx.get("Група")
    pi = idx.get("Стока - име за печат")
    di = idx.get("Доставна цена")
    out = {}
    for r in range(hi + 1, len(raw)):
        code = str(raw.iloc[r, ci]).strip()
        if not code or code.lower() == "nan":
            continue
        sup = _clean_name(raw.iloc[r, gi]) if gi is not None else ""
        if not sup:
            continue
        rec = {"supplier": sup,
               "print_name": str(raw.iloc[r, pi]).strip() if pi is not None else "",
               "delivery_price": str(raw.iloc[r, di]).strip() if di is not None else ""}
        for part in re.split(r"\s*/\s*", code):
            part = part.strip()
            if part:
                out[part] = rec
    return out


def _barsy_suppliers():
    """{normalized_name: supplier_id} for suppliers already in Barsy."""
    m = {}
    for s in b.call("Suppliers_getlist"):
        nm = re.sub(r"\s+", " ", str(s.get("supplier_name") or "")).strip()
        if nm:
            m[nm.lower()] = s["supplier_id"]
    return m


def _match_id(name, barsy):
    """Match an export supplier name to a Barsy supplier_id (exact, then prefix/substring)."""
    n = name.lower()
    if n in barsy:
        return barsy[n]
    for bn, sid in barsy.items():
        if bn.startswith(n) or n.startswith(bn) or n in bn or bn in n:
            return sid
    return None


def suppliers_report():
    rows = _export_rows()
    counts = defaultdict(int)
    for r in rows.values():
        counts[r["supplier"]] += 1
    barsy = _barsy_suppliers()
    print(f"products with a named supplier: {len(rows)}")
    print(f"distinct suppliers: {len(counts)}\n")
    print(f"{'supplier':32} {'#prod':>6}  in-Barsy?")
    for name, n in sorted(counts.items(), key=lambda x: -x[1]):
        sid = _match_id(name, barsy)
        print(f"{name[:32]:32} {n:>6}  {'#'+str(sid) if sid else 'MISSING'}")


def ensure(do_write=False):
    rows = _export_rows()
    names = sorted({r["supplier"] for r in rows.values()})
    barsy = _barsy_suppliers()
    missing = [n for n in names if _match_id(n, barsy) is None]
    print(f"{len(names)} suppliers, {len(missing)} missing in Barsy: {missing}")
    if not do_write:
        print("(dry-run — pass --confirm to create them)")
        return
    for n in missing:
        try:
            out = b.call("Suppliers_create", {"supplier": {"supplier_name": n}})
            print(f"  created «{n}» -> {out}")
        except b.BarsyError as e:
            print(f"  FAIL «{n}»: {str(e)[:100]}")


def link(do_write=False):
    """Push article<->supplier links for products currently in Barsy."""
    rows = _export_rows()
    barsy = _barsy_suppliers()
    arts = {str(a["code"]): a["article_id"]
            for a in b.call("Articles_getlist", {"filters": {}}) if a.get("code")}
    per_supplier = defaultdict(list)
    skipped = 0
    for code, aid in arts.items():
        r = rows.get(code) or rows.get(code.lstrip("0") or "0")
        if not r:
            continue
        sid = _match_id(r["supplier"], barsy)
        if not sid:
            skipped += 1
            continue
        row = {"article_id": aid, "remote_article_name": r["print_name"]}
        try:
            dp = float(str(r["delivery_price"]).replace(",", "."))
            if dp:
                row["default_delivery_price"] = dp
        except (ValueError, TypeError):
            pass
        per_supplier[sid].append(row)
    total = sum(len(v) for v in per_supplier.values())
    print(f"in-Barsy products: {len(arts)} | linkable: {total} | "
          f"suppliers touched: {len(per_supplier)} | no supplier-id: {skipped}")
    if not do_write:
        print("(dry-run — pass --confirm to push links)")
        return
    for sid, rws in per_supplier.items():
        try:
            b.call("Suppliers_save_articles", {"id": sid, "rows": rws})
            print(f"  supplier #{sid}: linked {len(rws)} articles")
        except b.BarsyError as e:
            print(f"  supplier #{sid} FAIL: {str(e)[:100]}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--suppliers", action="store_true")
    ap.add_argument("--ensure", action="store_true")
    ap.add_argument("--link", action="store_true")
    ap.add_argument("--confirm", action="store_true")
    a = ap.parse_args()
    if a.ensure:
        ensure(do_write=a.confirm)
    elif a.link:
        link(do_write=a.confirm)
    else:
        suppliers_report()
