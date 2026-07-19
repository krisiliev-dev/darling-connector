# -*- coding: utf-8 -*-
"""Duplicate-product detection over the catalog.

Signals, strongest first:
  1. same 'Код' on multiple Enriched rows (already collapsed in the catalog,
     reported here so the source sheet can be cleaned)
  2. same first image URL on different codes (near-certain same product)
  3. same normalized name on different codes
  4. Microinvest names like "10-073/10-072 Закачалка" — one till item mapped
     to several catalog numbers

Output: ../results/duplicate_products.xlsx (one sheet per signal).
"""
import io
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = Path(__file__).parent
EXCEL_PATH = r"C:\Users\lora_\Desktop\Local Database - enriched(AutoRecovered).xlsx"
CATALOG = HERE / "catalog.jsonl"
OUT = HERE.parent / "results" / "duplicate_products.xlsx"


def norm_name(s):
    s = str(s or "").lower()
    s = re.sub(r"^[\d/.\-]{3,}\s*", "", s)          # leading catalog codes
    s = re.sub(r"[^\wа-я ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    enr = pd.read_excel(EXCEL_PATH, sheet_name="Enriched", dtype={"Код": str})
    enr["Код"] = enr["Код"].str.strip()
    micro = pd.read_excel(EXCEL_PATH, sheet_name="Microinvest", dtype={"Код": str})

    # 1. duplicate codes in the source sheet
    dup_codes = enr[enr.duplicated("Код", keep=False)].sort_values("Код")

    docs = []
    with open(CATALOG, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            if "code" in d:
                docs.append(d)

    # 2. same first image URL
    by_img = defaultdict(list)
    for d in docs:
        img = (d["content"].get("Снимки") or "").split(";")[0].strip()
        if img:
            by_img[img].append(d)
    img_rows = []
    for img, group in by_img.items():
        if len(group) > 1:
            for d in group:
                img_rows.append({"Снимка": img, "Код": d["code"],
                                 "Наименование": d["content"].get("Наименование"),
                                 "Цена": d["operational"]["Цена"],
                                 "Категории": d["content"].get("Категории")})

    # 3. same normalized name
    by_name = defaultdict(list)
    for d in docs:
        n = norm_name(d["content"].get("Наименование"))
        if len(n) >= 10:
            by_name[n].append(d)
    name_rows = []
    for n, group in by_name.items():
        if len(group) > 1:
            for d in group:
                name_rows.append({"Нормализирано име": n, "Код": d["code"],
                                  "Наименование": d["content"].get("Наименование"),
                                  "Цена": d["operational"]["Цена"],
                                  "Категории": d["content"].get("Категории")})

    # 4. till items pointing at several catalog numbers ("10-073/10-072 ...")
    multi = micro[micro["Стока"].astype(str).str.match(r"^[\w.-]+/[\w.-]+\s")]
    multi_rows = multi[["Код", "Стока", "Продажна цена"]].copy()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(OUT) as xl:
        dup_codes.to_excel(xl, sheet_name="Дублирани кодове (източник)", index=False)
        pd.DataFrame(img_rows).to_excel(xl, sheet_name="Еднаква снимка", index=False)
        pd.DataFrame(name_rows).to_excel(xl, sheet_name="Еднакво име", index=False)
        multi_rows.to_excel(xl, sheet_name="Един артикул - няколко кода", index=False)

    print(f"duplicate source rows: {len(dup_codes)} "
          f"({dup_codes['Код'].nunique()} codes)")
    print(f"same-image groups: {sum(1 for g in by_img.values() if len(g) > 1)} "
          f"({len(img_rows)} products)")
    print(f"same-name groups: {sum(1 for g in by_name.values() if len(g) > 1)} "
          f"({len(name_rows)} products)")
    print(f"till items with multiple catalog numbers: {len(multi_rows)}")
    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
