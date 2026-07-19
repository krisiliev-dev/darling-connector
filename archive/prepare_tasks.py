# -*- coding: utf-8 -*-
"""One-time task preparation for the per-product agent pipeline.

Reads the master Excel once, joins Enriched + Microinvest on 'Код', keeps only
products matched to scraped data (Съвпадение == 'да'), and writes:

  tasks.jsonl   - one self-contained task per product (agent never touches Excel)
  (guide.md is seeded separately and maintained by the agents)

Run with a python that has pandas + openpyxl:
  "C:\\Users\\lora_\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" prepare_tasks.py
"""
import json
import re
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
EXCEL_PATH = r"C:\Users\lora_\Desktop\Local Database - enriched(AutoRecovered).xlsx"
TASKS_PATH = HERE / "tasks.jsonl"

ENRICHED_COLS = [
    "Код", "Каталожен номер", "Наименование", "Синоними", "Описание",
    "Мета наименование", "Мета описание", "Бранд", "Доставчик", "Категории",
    "Мярка", "Цена", "Количество", "Снимки", "Тегло (кг)", "Активен",
    "Предварителна поръчка", "Атрибути", "Варианти", "Серия", "Свързани",
]
GT_COLS = [
    "Стока", "Група", "Съвпадение", "Източник", "Match kind", "Снимка",
    "Английско име", "BG име (доставчик)", "Описание (скрейп)",
    "Бранд (скрейп)", "Материал (скрейп)", "Размери (скрейп)",
    "URL (доставчик)", "Scrape raw (JSON)",
]

# Scrape raw often hides brand/dimensions/weight deep in the JSON — keep more of it.
TRUNC = {"Scrape raw (JSON)": 3500, "Описание (скрейп)": 2500, "Описание": 3000}

UNIVERSAL_CAT = "(универсални — приложими към всяка категория)"


def load_filter_schema():
    """category -> [{group, values}], plus the universal groups."""
    filt = pd.read_excel(EXCEL_PATH, sheet_name="Филтри по категории")
    schema = {}
    for _, r in filt.iterrows():
        cat = str(r["Категория"]).strip()
        schema.setdefault(cat, []).append({
            "група": str(r["Филтрационна група"]).strip(),
            "стойности": str(r["Допустими стойности"]).strip(),
        })
    return schema


def filters_for(categories, schema):
    """Collect filter groups for a product's categories (exact + parent + universal)."""
    out, seen = [], set()

    def add(cat_key):
        # First add wins per group name: exact category is added before the
        # parent and universal fallbacks, so the most specific schema is kept.
        for g in schema.get(cat_key, []):
            if g["група"] not in seen:
                seen.add(g["група"])
                out.append(g)

    for cat in re.split(r"[;,]", categories or ""):
        cat = cat.strip()
        if not cat:
            continue
        add(cat)
        if "->" in cat:
            add(cat.split("->")[0].strip())
    add(UNIVERSAL_CAT)
    return out


def clean(v, limit=None):
    if pd.isna(v):
        return None
    s = str(v).strip()
    if limit and len(s) > limit:
        s = s[:limit] + " …[truncated]"
    return s if s != "" else None


def main():
    print("Loading Excel...")
    enr = pd.read_excel(EXCEL_PATH, sheet_name="Enriched", dtype={"Код": str})
    micro = pd.read_excel(EXCEL_PATH, sheet_name="Microinvest", dtype={"Код": str})
    enr["Код"] = enr["Код"].str.strip()
    micro["Код"] = micro["Код"].str.strip()
    print(f"Enriched: {enr.shape}, Microinvest: {micro.shape}")

    matched = micro[micro["Съвпадение"] == "да"].set_index("Код")
    print(f"Products matched to scraped data: {len(matched)}")

    schema = load_filter_schema()
    observed = set()
    for cats in enr["Категории"].dropna():
        for c in re.split(r"[;]", str(cats)):
            if c.strip():
                observed.add(c.strip())
    all_categories = sorted(
        (set(schema.keys()) | observed) - {UNIVERSAL_CAT}
    )

    # Related-product candidates: same first-4-character code prefix.
    enr["_prefix"] = enr["Код"].str[:4]
    by_prefix = {}
    for prefix, grp in enr.groupby("_prefix"):
        by_prefix[prefix] = [
            (r["Код"], clean(r["Наименование"]) or "")
            for _, r in grp.iterrows()
        ]

    n = 0
    seen = set()
    with open(TASKS_PATH, "w", encoding="utf-8") as f:
        for _, row in enr.iterrows():
            code = row["Код"]
            if code not in matched.index or code in seen:
                continue
            seen.add(code)
            gt_row = matched.loc[code]
            if isinstance(gt_row, pd.DataFrame):  # duplicate codes: take first
                gt_row = gt_row.iloc[0]

            product = {c: clean(row[c], TRUNC.get(c)) for c in ENRICHED_COLS}
            gt = {c: clean(gt_row[c], TRUNC.get(c)) for c in GT_COLS}
            candidates = [
                {"Код": c, "Наименование": name}
                for c, name in by_prefix.get(code[:4], [])
                if c != code
            ][:40]

            f.write(json.dumps({
                "code": code,
                "product": product,
                "ground_truth": gt,
                "related_candidates": candidates,
                "filter_schema": filters_for(product.get("Категории"), schema),
            }, ensure_ascii=False) + "\n")
            n += 1

    (HERE / "categories.json").write_text(
        json.dumps(all_categories, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"Wrote {n} tasks to {TASKS_PATH}")


if __name__ == "__main__":
    sys.exit(main())
