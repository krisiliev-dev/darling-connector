# -*- coding: utf-8 -*-
"""Approved-product COLLECTOR (owner 2026-07-19): gather every human-approved product with
its complete, clean field set into a structured payload ready for the Barsy article push.

Sources, per the owner's rules:
  - "Approved" = the latest action for a code in approvals.jsonl is "approve".
  - Enriched content (name, description, metas, attributes, brand, category, synonyms,
    related) = the approval record's fields (the owner's final/edited version), falling
    back to the DB canonical record for anything absent.
  - Price + quantity = the RECENT Microinvest export (Продажна цена / Количество), joined
    by code, taken AS-IS (never AI-touched — price policy).
  - Unit (Мярка) = the ENRICHED record (owner-normalised), NOT the export (its Мярка is raw).
  - Barcode = the ingested GS1 barcode(s). Every product MUST have one; those without are
    held out and reported, never sent.

Output: barsy_export.jsonl — one clean payload per product, the exact input the Barsy
mapper/push will consume (field-name mapping to ArticleInputData is the next step).

  python barsy_collect.py            # write barsy_export.jsonl + summary
  python barsy_collect.py --report   # summary only
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
APPROVALS = HERE / "approvals.jsonl"
EXPORT = Path(r"C:\Users\lora_\Desktop\Full Data per product.xlsx")
OUT = HERE / "barsy_export.jsonl"


def _approved():
    """{code: approved_fields_or_None} for codes whose LATEST action is 'approve'."""
    last = {}
    if APPROVALS.exists():
        for ln in APPROVALS.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                d = json.loads(ln)
            except Exception:
                continue
            c = str(d.get("code") or "")
            if c and not c.startswith("__"):
                last[c] = d
    return {c: d.get("fields") for c, d in last.items() if d.get("action") == "approve"}


def _export_price_qty():
    """{code: {price, qty}} from the recent Microinvest export (calamine — its xlsx has a
    malformed stylesheet + a banner above the header, same as the barcode export)."""
    import pandas as pd
    raw = None
    for eng in ("calamine", None):
        try:
            raw = pd.read_excel(EXPORT, sheet_name=0, header=None, dtype=str,
                                **({"engine": eng} if eng else {}))
            break
        except Exception:
            continue
    if raw is None:
        return {}
    hi = next((i for i in range(min(15, len(raw)))
               if any(str(v).strip() == "Код" for v in raw.iloc[i].tolist())), 0)
    cols = [str(v).strip() for v in raw.iloc[hi].tolist()]
    ci = cols.index("Код")

    def _find(names):
        for n in names:
            if n in cols:
                return cols.index(n)
        return None
    # retail selling price — "Продажна цена" (older export) or "Цена на дребно"
    # (the "Справка номенклатури" export); both are the same as-is retail price.
    pi = _find(["Продажна цена", "Цена на дребно"])
    qi = _find(["Количество", "Наличност"])   # nomenclature export has no stock column
    # supplier-facing print name + Microinvest reorder thresholds
    spi = _find(["Стока - име за печат"])
    mini = _find(["Мин. количество", "Минимално количество"])
    nomi = _find(["Номинално количество"])

    def _cell(r, i):
        return str(raw.iloc[r, i]).strip() if i is not None else ""

    out = {}
    for r in range(hi + 1, len(raw)):
        code = str(raw.iloc[r, ci]).strip()
        if not code or code.lower() == "nan":
            continue
        rec = {"price": _cell(r, pi), "qty": _cell(r, qi),
               "supplier_print_name": _cell(r, spi),
               "min_qty": _cell(r, mini), "nominal_qty": _cell(r, nomi)}
        for part in re.split(r"\s*/\s*", code):           # slash-joined till pairs
            part = part.strip()
            if part:
                out[part] = rec
                out.setdefault(part.lstrip("0") or "0", rec)   # normalised fallback
    return out


def _barcodes_by_code():
    import ean_brand as eb
    from collections import defaultdict
    m = defaultdict(list)
    for d in eb._load(eb.BARCODES):
        if d.get("cls") == "gs1":
            m[str(d["code"])].append(d["ean"])
    return m


def _attrs_to_dict(attrs):
    out = {}
    for part in str(attrs or "").split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            k = k.strip()
            if k:
                out[k] = re.sub(r"\s+", " ", v.strip())
    return out


def collect(write=True):
    import db
    approved = _approved()
    px = _export_price_qty()
    bc = _barcodes_by_code()
    pq_norm = {c.lstrip("0") or "0": v for c, v in px.items()}

    payloads = []
    no_barcode = []
    no_price = []
    for code, appr_fields in approved.items():
        rec = db.get_record(code) or {}
        base = dict(rec.get("fields") or {})
        if appr_fields:                                   # owner's final/edited wins
            base.update({k: v for k, v in appr_fields.items() if v not in (None, "")})
        meta = rec.get("meta") or {}
        barcodes = bc.get(code) or []
        if not barcodes:
            no_barcode.append(code)
            continue                                      # never send a product w/o a barcode
        pq = px.get(code) or px.get(code.lstrip("0") or "0") or pq_norm.get(code) or {}
        if not pq.get("price"):
            no_price.append(code)
        payload = {
            "unique_code": code,
            "name": base.get("Наименование") or "",
            "brand": str(base.get("Бранд") or "").strip(),
            "category_leaf": meta.get("leaf_full") or base.get("Категории") or "",
            "barcode": barcodes[0],
            "barcodes": barcodes,
            "unit": base.get("Мярка") or "",             # normalised (enriched), NOT export
            "price_retail": pq.get("price") or "",       # from export, as-is
            "quantity": pq.get("qty") or "",             # from export
            # supplier-facing name (for the SourcedFrom link → clearer supplier orders)
            "supplier_print_name": pq.get("supplier_print_name") or "",
            "min_qty": pq.get("min_qty") or "",          # Microinvest reorder threshold
            "nominal_qty": pq.get("nominal_qty") or "",  # Microinvest nominal/package qty
            "attributes": _attrs_to_dict(base.get("Атрибути")),
            "description_html": base.get("Описание") or "",
            "meta_title": base.get("Мета наименование") or "",
            "meta_description": base.get("Мета описание") or "",
            "synonyms": base.get("Синоними") or "",
            "related": [x.strip() for x in str(base.get("Свързани") or "").split(",")
                        if x.strip()],
            "catalogue_number": base.get("Каталожен номер") or "",
            "weight_kg": base.get("Тегло (кг)") or "",
            "images": base.get("Снимки") or "",
            "lang": "bg",                                 # → Barsy MultiLanguageData
        }
        payloads.append(payload)

    if write:
        with OUT.open("w", encoding="utf-8") as f:
            for p in payloads:
                f.write(json.dumps(p, ensure_ascii=False) + "\n")

    print(f"approved products: {len(approved)}")
    print(f"  -> collected (with barcode): {len(payloads)}")
    print(f"  -> HELD OUT (no barcode): {len(no_barcode)}"
          + (f" e.g. {no_barcode[:5]}" if no_barcode else ""))
    print(f"  -> collected but MISSING price from export: {len(no_price)}"
          + (f" e.g. {no_price[:5]}" if no_price else ""))
    if write:
        print(f"wrote {OUT.name} ({len(payloads)} products)")
    return payloads


if __name__ == "__main__":
    collect(write="--report" not in sys.argv)
