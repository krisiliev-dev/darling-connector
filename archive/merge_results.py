# -*- coding: utf-8 -*-
"""Merge agent verification results back into a full Excel deliverable.

Produces results/agent_verified_products.xlsx: all rows of the original
Enriched sheet, with verified fields applied for processed products and
status columns describing what happened.

Run with a python that has pandas + openpyxl:
  "C:\\Users\\lora_\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" merge_results.py
"""
import json
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
EXCEL_PATH = r"C:\Users\lora_\Desktop\Local Database - enriched(AutoRecovered).xlsx"
RESULTS_PATH = HERE / "results.jsonl"
OUT_PATH = HERE.parent / "results" / "agent_verified_products.xlsx"


def main():
    enr = pd.read_excel(EXCEL_PATH, sheet_name="Enriched", dtype={"Код": str})
    enr["Код"] = enr["Код"].str.strip()

    # Agent values arrive as strings; let every content column hold them.
    for col in enr.columns:
        if col != "Код":
            enr[col] = enr[col].astype(object)

    results = {}
    if RESULTS_PATH.exists():
        with open(RESULTS_PATH, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    r = json.loads(line)
                    results[r["code"]] = r  # last write wins

    enr["Статус проверка"] = "непроверен"
    enr["Проблеми"] = None
    enr["Снимка проблеми"] = None
    enr["needs_human"] = None
    enr["confidence"] = None

    applied = 0
    idx_by_code = {c: i for i, c in enumerate(enr["Код"])}
    for code, r in results.items():
        i = idx_by_code.get(code)
        if i is None:
            continue
        for col, val in r["fields"].items():
            # Цена is operational data — synced from Microinvest below, never
            # taken from an agent (owner directive 2026-07-09).
            if col in enr.columns and col not in ("Код", "Цена"):
                enr.at[i, col] = val
        enr.at[i, "Статус проверка"] = "проверен от агент"
        enr.at[i, "Проблеми"] = r.get("Проблеми")
        enr.at[i, "Снимка проблеми"] = r.get("Снимка проблеми")
        enr.at[i, "needs_human"] = r.get("needs_human")
        enr.at[i, "confidence"] = r.get("confidence")
        applied += 1

    # PRICE POLICY (owner directive 2026-07-09): the site price IS Microinvest's
    # 'Продажна цена', taken as-is — never AI-generated. Applied LAST so nothing
    # can override it.
    micro = pd.read_excel(EXCEL_PATH, sheet_name="Microinvest", dtype={"Код": str})
    micro["Код"] = micro["Код"].str.strip()
    m = micro.drop_duplicates("Код").set_index("Код")
    till_price = pd.to_numeric(enr["Код"].map(m["Продажна цена"]), errors="coerce").round(2)
    cost_price = pd.to_numeric(enr["Код"].map(m["Доставна цена"]), errors="coerce")
    synced = till_price.notna()
    enr.loc[synced, "Цена"] = till_price[synced]
    enr["Цена източник"] = synced.map(
        {True: "Microinvest", False: "без промяна (липсва в Microinvest)"})
    enr["Под доставна цена"] = (till_price < cost_price) & synced
    print(f"Prices synced from Microinvest: {synced.sum()} of {len(enr)} "
          f"({(~synced).sum()} kept as-is); below cost: {enr['Под доставна цена'].sum()}")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    enr.to_excel(OUT_PATH, index=False)
    print(f"Applied {applied} verified products out of {len(enr)} rows.")
    print(f"Saved {OUT_PATH}")


if __name__ == "__main__":
    main()
