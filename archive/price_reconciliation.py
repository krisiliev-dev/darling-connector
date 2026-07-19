# -*- coding: utf-8 -*-
"""Price reconciliation: Enriched 'Цена' vs Microinvest 'Продажна цена'.

The store sheet (Enriched) is what the site imports; Microinvest is the till.
Any mismatch is either a deliberate promo or a data error — this report lets a
human decide which, product by product.

Run:
  "C:\\...\\WindowsApps\\python.exe" price_reconciliation.py
Writes ../results/price_discrepancies.xlsx + prints a summary.
"""
import io
import sys
from pathlib import Path

import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = Path(__file__).parent
EXCEL_PATH = r"C:\Users\lora_\Desktop\Local Database - enriched(AutoRecovered).xlsx"
OUT = HERE.parent / "results" / "price_discrepancies.xlsx"

TOLERANCE_LV = 0.01  # exact-match tolerance for float noise


def main():
    enr = pd.read_excel(EXCEL_PATH, sheet_name="Enriched", dtype={"Код": str})
    micro = pd.read_excel(EXCEL_PATH, sheet_name="Microinvest", dtype={"Код": str})
    enr["Код"] = enr["Код"].str.strip()
    micro["Код"] = micro["Код"].str.strip()

    m = micro.drop_duplicates("Код").set_index("Код")
    df = enr[["Код", "Наименование", "Цена", "Количество", "Активен"]].copy()
    df["Цена сайт"] = pd.to_numeric(df["Цена"], errors="coerce")
    df["Цена Microinvest"] = pd.to_numeric(
        df["Код"].map(m["Продажна цена"]), errors="coerce")
    df["Доставна цена"] = pd.to_numeric(
        df["Код"].map(m["Доставна цена"]), errors="coerce")

    both = df.dropna(subset=["Цена сайт", "Цена Microinvest"]).copy()
    both["Разлика (лв)"] = (both["Цена сайт"] - both["Цена Microinvest"]).round(2)
    pct = (both["Цена сайт"] / both["Цена Microinvest"] - 1) * 100
    both["Разлика (%)"] = pct.replace(
        [float("inf"), -float("inf")], float("nan")).round(1)

    bad = both[both["Разлика (лв)"].abs() > TOLERANCE_LV].copy()
    # Site price below cost is the most dangerous class. FAIL-CLOSED: a MISSING cost must
    # NOT read as "safe" — `price < NaN` is False, which silently hid below-cost items with
    # no known cost. Flag unknown-cost separately so nothing dangerous passes unnoticed.
    bad["Липсва доставна цена"] = bad["Доставна цена"].isna()
    bad["Под доставна цена"] = (bad["Цена сайт"] < bad["Доставна цена"]) & bad["Доставна цена"].notna()
    bad = bad.sort_values("Разлика (лв)")

    only_site = df[df["Цена Microinvest"].isna() & df["Цена сайт"].notna()]
    missing_price = df[df["Цена сайт"].isna()]

    cols = ["Код", "Наименование", "Цена сайт", "Цена Microinvest",
            "Разлика (лв)", "Разлика (%)", "Доставна цена", "Под доставна цена",
            "Липсва доставна цена", "Количество", "Активен"]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(OUT) as xl:
        bad[cols].to_excel(xl, sheet_name="Разминавания", index=False)
        only_site.to_excel(xl, sheet_name="Без цена в Microinvest", index=False)
        missing_price.to_excel(xl, sheet_name="Без цена на сайта", index=False)

    print(f"Products with both prices: {len(both)}")
    print(f"Mismatches (> {TOLERANCE_LV} лв): {len(bad)} "
          f"({len(bad)/max(len(both),1):.1%})")
    print(f"  site cheaper: {(bad['Разлика (лв)'] < 0).sum()}, "
          f"site more expensive: {(bad['Разлика (лв)'] > 0).sum()}")
    print(f"  BELOW COST on site: {bad['Под доставна цена'].sum()}"
          f"   (unknown cost, needs check: {bad['Липсва доставна цена'].sum()})")
    print(f"No Microinvest price: {len(only_site)}; no site price: {len(missing_price)}")
    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
