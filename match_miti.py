# -*- coding: utf-8 -*-
"""Match scraped mitibg.com products against UNMATCHED Microinvest rows and (optionally)
enqueue the confident matches as new pipeline tasks.

Strategies (confident ones gate on name-token overlap so a bare numeric collision can
never match):
  A "till_code" — till Код == miti SKU
  B "stoka_code" — leading code token of Стока == miti SKU
  C "name"      — name-similarity only (REPORT ONLY, never auto-enqueued)

  python match_miti.py             # report -> miti_matches.jsonl + summary
  python match_miti.py --enqueue   # append A/B matches as tasks (tasks.jsonl + DB)
"""
import json
import re
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
EXCEL = r"C:\Users\lora_\Desktop\Local Database - enriched(AutoRecovered).xlsx"
MITI = HERE / "miti_products.jsonl"
OUT = HERE / "miti_matches.jsonl"
TASKS = HERE / "tasks.jsonl"

UNIVERSAL_CAT = "(универсални — приложими към всяка категория)"
ENRICHED_COLS = ["Код", "Каталожен номер", "Наименование", "Синоними", "Описание",
                 "Мета наименование", "Мета описание", "Бранд", "Доставчик", "Категории",
                 "Мярка", "Цена", "Количество", "Снимки", "Тегло (кг)", "Активен",
                 "Предварителна поръчка", "Атрибути", "Варианти", "Серия", "Свързани"]
TRUNC = {"Scrape raw (JSON)": 3500, "Описание (скрейп)": 2500, "Описание": 3000}

STOP = {"със", "три", "два", "две", "броя", "комплект", "малка", "малък", "голяма",
        "голям", "среден", "средна"}


def toks(s):
    return {w for w in re.findall(r"[а-яa-z]{3,}", str(s or "").lower())} - STOP


def norm_code(s):
    d = re.sub(r"^0+", "", str(s or "").strip())
    return d


def clean(v, limit=None):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return None
    s = str(v).strip()
    if s.lower() in ("nan", "none", ""):
        return None
    return s[:limit] if limit else s


def load_miti():
    by_sku = {}
    dup = set()
    for line in MITI.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            d = json.loads(line)
        except Exception:
            continue
        sku = norm_code(d.get("sku"))
        if not sku or not d.get("name"):
            continue
        if sku in by_sku:
            dup.add(sku)
        by_sku[sku] = d
    for s in dup:
        by_sku.pop(s, None)
    return by_sku, dup


def match():
    by_sku, dup = load_miti()
    micro = pd.read_excel(EXCEL, sheet_name="Microinvest", dtype={"Код": str})
    micro["Код"] = micro["Код"].str.strip()
    unm = micro[micro["Съвпадение"] != "да"]
    print(f"miti products: {len(by_sku)} (dropped {len(dup)} duplicate skus) | "
          f"unmatched till rows: {len(unm)}")
    matches = []
    used_till = set()
    for _, r in unm.iterrows():
        till_code = str(r["Код"])
        stoka = str(r["Стока"] or "")
        grp = str(r["Група"] or "")
        is_miti_grp = "МИТИ" in grp.upper()
        st = toks(stoka)
        cands = []
        m = by_sku.get(norm_code(till_code))
        if m:
            cands.append(("till_code", m))
        lead = re.match(r"\s*([A-Za-z0-9][\w\-\./]{1,14})\s+", stoka)
        if lead:
            m2 = by_sku.get(norm_code(lead.group(1)))
            if m2:
                cands.append(("stoka_code", m2))
        hit = None
        for kind, mm in cands:
            ov = len(st & toks(mm["name"]))
            if ov >= 1 or is_miti_grp:
                hit = (kind, mm, ov)
                break
        if hit is None:
            best, bs = None, 0
            for sku, mm in by_sku.items():
                ov = len(st & toks(mm["name"]))
                if ov > bs:
                    best, bs = mm, ov
            small = min(len(st), len(toks(best["name"]))) if best else 0
            if best and bs >= 3 and small and bs / small >= 0.75:
                hit = ("name", best, bs)
        if hit:
            kind, mm, ov = hit
            matches.append({"till_code": till_code, "стока": stoka, "група": grp,
                            "sku": mm["sku"], "miti_name": mm["name"], "kind": kind,
                            "overlap": ov, "url": mm["url"],
                            "images": mm.get("images") or [], "price": mm.get("price"),
                            "description": mm.get("description") or ""})
            used_till.add(till_code)
    OUT.write_text("\n".join(json.dumps(m, ensure_ascii=False) for m in matches) + "\n",
                   encoding="utf-8")
    import collections
    kinds = collections.Counter(m["kind"] for m in matches)
    print(f"MATCHES: {len(matches)} -> {OUT.name} | by kind: {dict(kinds)}")
    for m in matches[:6]:
        print(f"  [{m['kind']}] {m['till_code']} {m['стока'][:45]!r} <-> "
              f"sku {m['sku']} {m['miti_name'][:45]!r}")
    return matches


def load_filter_schema():
    filt = pd.read_excel(EXCEL, sheet_name="Филтри по категории")
    schema = {}
    for _, r in filt.iterrows():
        schema.setdefault(str(r["Категория"]).strip(), []).append(
            {"група": str(r["Филтрационна група"]).strip(),
             "стойности": str(r["Допустими стойности"]).strip()})
    return schema


def filters_for(categories, schema):
    out, seen = [], set()

    def add(cat_key):
        for g in schema.get(cat_key, []):
            k = g["група"]
            if k not in seen:
                seen.add(k)
                out.append(g)
    for c in re.split(r"[;]", str(categories or "")):
        c = c.strip()
        if c:
            add(c)
            add(c.split("->")[0].strip())
    add(UNIVERSAL_CAT)
    return out


def enqueue(matches):
    import db
    conf = [m for m in matches if m["kind"] in ("till_code", "stoka_code")]
    print(f"enqueueing {len(conf)} confident matches (name-only stays report-only)")
    enr = pd.read_excel(EXCEL, sheet_name="Enriched", dtype={"Код": str})
    enr["Код"] = enr["Код"].str.strip()
    enr = enr.set_index("Код", drop=False)
    micro = pd.read_excel(EXCEL, sheet_name="Microinvest", dtype={"Код": str})
    micro["Код"] = micro["Код"].str.strip()
    micro = micro.set_index("Код")
    schema = load_filter_schema()
    enr["_prefix"] = enr["Код"].str[:4]
    by_prefix = {p: [(r["Код"], clean(r["Наименование"]) or "") for _, r in g.iterrows()]
                 for p, g in enr.groupby("_prefix")}
    existing = set()
    for line in open(TASKS, encoding="utf-8", errors="replace"):
        try:
            existing.add(json.loads(line)["code"])
        except Exception:
            pass
    n = skip = 0
    with open(TASKS, "a", encoding="utf-8") as f:
        for m in conf:
            code = m["till_code"]
            if code in existing or code not in enr.index:
                skip += 1
                continue
            row = enr.loc[code]
            if isinstance(row, pd.DataFrame):
                row = row.iloc[0]
            mr = micro.loc[code]
            if isinstance(mr, pd.DataFrame):
                mr = mr.iloc[0]
            product = {c: clean(row.get(c), TRUNC.get(c)) for c in ENRICHED_COLS}
            gt = {"Стока": clean(mr.get("Стока")), "Група": clean(mr.get("Група")),
                  "Съвпадение": "да", "Източник": "miti", "Match kind": m["kind"],
                  "Снимка": (m["images"] or [None])[0],
                  "Английско име": None, "BG име (доставчик)": m["miti_name"],
                  "Описание (скрейп)": clean(m["description"], 2500),
                  "Бранд (скрейп)": None, "Материал (скрейп)": None,
                  "Размери (скрейп)": None, "URL (доставчик)": m["url"],
                  "Scrape raw (JSON)": json.dumps(
                      {"scrape_sku": m["sku"], "scrape_name": m["miti_name"],
                       "scrape_price_bgn": m["price"], "scrape_images": m["images"][:8],
                       "scrape_site": "mitibg.com"}, ensure_ascii=False)[:3500]}
            cands = [{"Код": c, "Наименование": nm}
                     for c, nm in by_prefix.get(code[:4], []) if c != code][:40]
            f.write(json.dumps({"code": code, "product": product, "ground_truth": gt,
                                "related_candidates": cands,
                                "filter_schema": filters_for(product.get("Категории"),
                                                             schema)},
                               ensure_ascii=False) + "\n")
            n += 1
    print(f"appended {n} tasks ({skip} skipped: already tasked / no Enriched row)")
    db.ingest_tasks()
    print("DB tasks table refreshed — lanes pick the new codes up automatically")


if __name__ == "__main__":
    ms = match()
    if "--enqueue" in sys.argv:
        enqueue(ms)
