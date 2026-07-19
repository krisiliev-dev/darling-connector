# -*- coding: utf-8 -*-
"""Build the canonical catalog: one JSON document per product.

Everything downstream (site export, review page, dashboards, golden set)
reads catalog.jsonl. The catalog itself is DERIVED — rebuilt any time from:

  Excel Enriched sheet      original content fields
  Excel Microinvest sheet   operational truth: Цена/Количество/Мярка (as-is,
                            owner directive), Доставна цена for margin flags
  results.jsonl             agent-verified content fields + provenance
  image-pipeline results    per-image processing status (when present)
  golden_codes.txt          quality reference set membership

Extras applied here (deterministic, no AI):
  - related-products symmetric closure (A↔B)
  - import validation -> "Импорт проблеми" per product
  - attribute-coverage report per category -> coverage_report.md

Outputs: catalog.jsonl, ../results/agent_verified_products.xlsx,
         ../results/coverage_report.md

Run with the pandas-capable python:
  "C:\\...\\WindowsApps\\python.exe" build_catalog.py
"""
import io
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = Path(__file__).parent
EXCEL_PATH = r"C:\Users\lora_\Desktop\Local Database - enriched(AutoRecovered).xlsx"
RESULTS_PATH = HERE / "results.jsonl"
CATEGORIES_PATH = HERE / "categories.json"
GOLDEN_PATH = HERE / "golden_codes.txt"
IMG_RESULTS = HERE.parent / "image-pipeline" / "process_results.jsonl"
CATALOG_PATH = HERE / "catalog.jsonl"
XLSX_OUT = HERE.parent / "results" / "agent_verified_products.xlsx"
COVERAGE_OUT = HERE.parent / "results" / "coverage_report.md"

ENRICHED_COLS = [
    "Код", "Каталожен номер", "Наименование", "Синоними", "Описание",
    "Мета наименование", "Мета описание", "Бранд", "Доставчик", "Категории",
    "Мярка", "Цена", "Количество", "Снимки", "Тегло (кг)", "Активен",
    "Предварителна поръчка", "Атрибути", "Варианти", "Серия", "Свързани",
]


def clean(v):
    # Agents occasionally emit arrays/objects for text fields.
    if isinstance(v, (list, tuple)):
        v = "; ".join(str(x) for x in v if x is not None)
    elif isinstance(v, dict):
        v = json.dumps(v, ensure_ascii=False)
    if v is None:
        return None
    try:
        if pd.isna(v):
            return None
    except (TypeError, ValueError):
        pass
    s = str(v).strip()
    return s if s else None


def load_jsonl(path, key="code"):
    out = {}
    if Path(path).exists():
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        r = json.loads(line)
                        out[r[key]] = r  # last write wins
                    except Exception:
                        pass
    return out


def main():
    enr = pd.read_excel(EXCEL_PATH, sheet_name="Enriched", dtype={"Код": str})
    micro = pd.read_excel(EXCEL_PATH, sheet_name="Microinvest", dtype={"Код": str})
    enr["Код"] = enr["Код"].str.strip()
    micro["Код"] = micro["Код"].str.strip()
    m = micro.drop_duplicates("Код").set_index("Код")

    # Resolve duplicate versions of a code by MAX ts (not file order) so every append-
    # only version-file (z_tidy / z_review / z_restore) is picked up correctly regardless
    # of filename — matching how the review server already resolves records.
    results = {}
    _best_ts = {}
    for rp in [RESULTS_PATH, *HERE.glob("results.lane*.jsonl")]:
        if not Path(rp).exists():
            continue
        with open(rp, encoding="utf-8", errors="replace") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                c = r.get("code")
                if c is None:
                    continue
                ts = r.get("ts") or ""
                if c not in _best_ts or ts >= _best_ts[c]:
                    _best_ts[c] = ts
                    results[c] = r
    img_status = load_jsonl(IMG_RESULTS)
    golden = set()
    if GOLDEN_PATH.exists():
        golden = {c.strip() for c in GOLDEN_PATH.read_text(encoding="utf-8").splitlines() if c.strip()}
    known_cats = set(json.loads(CATEGORIES_PATH.read_text(encoding="utf-8"))) \
        if CATEGORIES_PATH.exists() else set()

    # Category crosswalk (our 74 categories -> Shopify + Google taxonomy). Built
    # once by category_shopify_map.json; applied here by deterministic lookup so
    # every product lands categorized on Shopify import + Google/Meta feeds.
    xwalk_path = HERE / "category_shopify_map.json"
    xwalk = {}          # keyed by full "bg" value as authored (leaf, or full path)
    xwalk_leaf = {}     # keyed by leaf only, for path->leaf fallback (skip ambiguous)
    if xwalk_path.exists():
        rows = json.loads(xwalk_path.read_text(encoding="utf-8"))
        for e in rows:
            xwalk[e["bg"].strip()] = e
        # build leaf index; a leaf shared by >1 entry is ambiguous -> drop it so
        # we never guess (e.g. "За банята" as a top-level vs kids subcategory)
        leaf_count = {}
        for e in rows:
            leaf = e["bg"].split("->")[-1].strip()
            leaf_count[leaf] = leaf_count.get(leaf, 0) + 1
        for e in rows:
            leaf = e["bg"].split("->")[-1].strip()
            if leaf_count[leaf] == 1:
                xwalk_leaf[leaf] = e

    def map_category(cat_field):
        """Pick the crosswalk entry for a product's (possibly multi) category.
        The crosswalk keys subcategories by their bare leaf name ('Вази') but
        product category fields carry full 'Parent -> Child' paths, so try the
        full path first, then the unambiguous leaf. Most specific path wins."""
        parts = [p.strip() for p in str(cat_field or "").split(";") if p.strip()]
        for p in sorted(parts, key=lambda x: -x.count("->")):
            if p in xwalk:            # exact match (top-level, or the 2 kids paths)
                return xwalk[p]
            leaf = p.split("->")[-1].strip()
            if leaf in xwalk_leaf:    # subcategory keyed by leaf
                return xwalk_leaf[leaf]
        return None

    # Human decisions from review_server.py (1-click approve/reject of vision edits).
    approvals = {}
    approvals_path = HERE / "approvals.jsonl"
    if approvals_path.exists():
        for line in approvals_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    o = json.loads(line)
                    approvals[str(o["code"])] = o  # last decision wins
                except Exception:
                    pass

    # ------------------------------------------------------------------ pass 1
    docs, seen = {}, set()
    for _, row in enr.iterrows():
        code = row["Код"]
        if code in seen:
            continue  # duplicate code rows: first wins (see duplicate_report.py)
        seen.add(code)
        original = {c: clean(row[c]) for c in ENRICHED_COLS}
        r = results.get(code)

        content = dict(original)
        if r:
            for k, v in r["fields"].items():
                if k in content and k not in ("Код", "Цена", "Количество", "Мярка"):
                    content[k] = clean(v)

        # Apply a human's 1-click decision on the vision-proposed correction.
        decision = approvals.get(str(code))
        approved_fields = None
        if decision and decision.get("action") == "approve" and decision.get("fields"):
            for k, v in decision["fields"].items():
                if k in content:
                    content[k] = clean(v)
            approved_fields = decision["fields"]

        # Operational truth (owner directive: till data as-is, never AI).
        gt = m.loc[code] if code in m.index else None
        price = None if gt is None else pd.to_numeric(pd.Series([gt["Продажна цена"]]), errors="coerce").round(2).iloc[0]
        cost = None if gt is None else pd.to_numeric(pd.Series([gt["Доставна цена"]]), errors="coerce").iloc[0]
        qty = None if gt is None else pd.to_numeric(pd.Series([gt["Количество"]]), errors="coerce").iloc[0]
        operational = {
            "Цена": float(price) if price is not None and pd.notna(price) else content.get("Цена"),
            "Цена източник": "Microinvest" if price is not None and pd.notna(price) else "Enriched (липсва в Microinvest)",
            "Количество": float(qty) if qty is not None and pd.notna(qty) else content.get("Количество"),
            "Количество източник": "Microinvest" if qty is not None and pd.notna(qty) else "Enriched",
            "Мярка": (clean(gt["Мярка"]) if gt is not None else None) or content.get("Мярка"),
            "Под доставна цена": bool(price is not None and cost is not None
                                      and pd.notna(price) and pd.notna(cost) and price < cost),
        }
        # Deactivation candidate: zero stock, marked active, no preorder.
        try:
            zero_stock = operational["Количество"] is not None and float(operational["Количество"]) <= 0
        except (TypeError, ValueError):
            zero_stock = False
        operational["Кандидат за деактивиране"] = bool(
            zero_stock and str(content.get("Активен")).lower() in ("true", "1", "да")
            and str(content.get("Предварителна поръчка")).lower() not in ("true", "1", "да"))

        # A human decision resolves the record: approve applies the fix, reject keeps
        # the original — either way it's no longer pending human review.
        human_resolved = bool(decision)
        provenance = {
            "status": ("одобрен от човек" if decision and decision.get("action") == "approve"
                       else "проверен от агент" if r else "непроверен"),
            "verified_at": r.get("ts") if r else None,
            "confidence": r.get("confidence") if r else None,
            "needs_human": (False if human_resolved else bool(r.get("needs_human"))) if r else None,
            "human_decision": decision.get("action") if decision else None,
            "problems": r.get("Проблеми") if r else None,
            "image_problems": r.get("Снимка проблеми") if r else None,
            "review": r.get("review") if r else None,
            "notes": (r.get("meta") or {}).get("notes") if r else None,
        }
        img = img_status.get(code)
        images = {"status": img.get("status"), "bg_original": img.get("bg_original"),
                  "actions": img.get("actions"), "needs_review": img.get("needs_review")} if img else None

        docs[code] = {"code": code, "content": content, "operational": operational,
                      "provenance": provenance, "quality": {"golden": code in golden},
                      "images": images, "shopify": map_category(content.get("Категории"))}

    # ------------------------------------------------- related symmetric closure
    sym_added = 0
    def rel_codes(doc):
        rel = doc["content"].get("Свързани") or ""
        return [p.split("|")[0].strip() for p in re.split(r"[;\n]+", rel) if p.strip()]

    for code, doc in docs.items():
        # Only verified products have curated links worth propagating —
        # symmetrizing the old AI links would amplify their errors.
        if doc["provenance"]["status"] == "непроверен":
            continue
        for other in rel_codes(doc):
            od = docs.get(other)
            if not od or code in rel_codes(od) or len(rel_codes(od)) >= 10:
                continue
            existing = od["content"].get("Свързани") or ""
            entry = f"{code}|{doc['content'].get('Наименование') or ''}"
            od["content"]["Свързани"] = (existing + "; " if existing else "") + entry
            notes = od["provenance"].get("notes")
            if not isinstance(notes, list):
                notes = od["provenance"]["notes"] = []
            notes.append(f"related_symmetry_added:{code}")
            sym_added += 1

    # ------------------------------------------------------- import validation
    for code, doc in docs.items():
        issues = []
        c = doc["content"]
        if c.get("Наименование") and len(c["Наименование"]) > 80:
            issues.append("име >80 знака")
        if c.get("Мета наименование") and len(c["Мета наименование"]) > 70:
            issues.append("мета заглавие >70")
        if known_cats and c.get("Категории"):
            for part in str(c["Категории"]).split(";"):
                if part.strip() and part.strip() not in known_cats:
                    issues.append(f"непозната категория: {part.strip()[:40]}")
        if c.get("Снимки") and not str(c["Снимки"]).lower().startswith("http"):
            issues.append("невалиден URL на снимка")
        if doc["operational"]["Цена"] in (None, ""):
            issues.append("липсва цена")
        doc["import_issues"] = issues or None

    # ---------------------------------------------------------------- exports
    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps({"_meta": {"built_at": datetime.now().isoformat(timespec="seconds"),
                                      "products": len(docs),
                                      "verified": sum(1 for d in docs.values()
                                                      if d["provenance"]["status"] != "непроверен")}},
                           ensure_ascii=False) + "\n")
        for doc in docs.values():
            f.write(json.dumps(doc, ensure_ascii=False) + "\n")

    rows = []
    for doc in docs.values():
        row = dict(doc["content"])
        row["Цена"] = doc["operational"]["Цена"]
        row["Количество"] = doc["operational"]["Количество"]
        row["Мярка"] = doc["operational"]["Мярка"]
        row["Цена източник"] = doc["operational"]["Цена източник"]
        row["Под доставна цена"] = doc["operational"]["Под доставна цена"]
        row["Кандидат за деактивиране"] = doc["operational"]["Кандидат за деактивиране"]
        row["Статус проверка"] = doc["provenance"]["status"]
        row["needs_human"] = doc["provenance"]["needs_human"]
        row["confidence"] = doc["provenance"]["confidence"]
        row["Проблеми"] = doc["provenance"]["problems"]
        row["Снимка проблеми"] = doc["provenance"]["image_problems"]
        row["Импорт проблеми"] = "; ".join(doc["import_issues"]) if doc["import_issues"] else None
        xw = doc.get("shopify")
        row["Shopify категория"] = xw.get("shopify_category") if xw else None
        row["Shopify ID"] = xw.get("shopify_id") if xw else None
        row["Google категория"] = xw.get("google_category") if xw else None
        row["Google ID"] = xw.get("google_id") if xw else None
        rows.append(row)
    XLSX_OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_excel(XLSX_OUT, index=False)

    # ------------------------------------------------- attribute coverage report
    from collections import defaultdict
    cov = defaultdict(lambda: defaultdict(int))
    totals = defaultdict(int)
    for doc in docs.values():
        if doc["provenance"]["status"] == "непроверен":
            continue
        cat = (doc["content"].get("Категории") or "без категория").split(";")[0].strip()
        totals[cat] += 1
        for part in str(doc["content"].get("Атрибути") or "").split(";"):
            if ":" in part:
                cov[cat][part.split(":")[0].strip()] += 1
    lines = ["# Покритие на атрибутите (проверени продукти)",
             f"Генерирано {datetime.now():%Y-%m-%d %H:%M} · {sum(totals.values())} проверени продукта", ""]
    for cat in sorted(totals, key=totals.get, reverse=True):
        lines.append(f"## {cat} ({totals[cat]} продукта)")
        for grp, n in sorted(cov[cat].items(), key=lambda kv: -kv[1]):
            lines.append(f"- {grp}: {n}/{totals[cat]} ({n/totals[cat]:.0%})")
        lines.append("")
    COVERAGE_OUT.write_text("\n".join(lines), encoding="utf-8")

    verified = sum(1 for d in docs.values() if d["provenance"]["status"] != "непроверен")
    flagged = sum(1 for d in docs.values() if d["provenance"]["needs_human"])
    imp = sum(1 for d in docs.values() if d["import_issues"])
    print(f"Catalog: {len(docs)} products ({verified} verified, {flagged} need human, "
          f"{sym_added} related links symmetrized, {imp} with import issues)")
    print(f"  -> {CATALOG_PATH}")
    print(f"  -> {XLSX_OUT}")
    print(f"  -> {COVERAGE_OUT}")


if __name__ == "__main__":
    main()
