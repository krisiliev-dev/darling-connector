# -*- coding: utf-8 -*-
"""Schema-reconciliation attribute pass — the cheap, targeted answer to 'no product
left without attributes' (the reviewer's #1 recurring flag).

Two parts:
  1. DETECT (free, deterministic): find products whose Атрибути are missing filter
     GROUPS that exist in their category's CURRENT schema — either because they were
     enriched before the schema grew (stale fingerprint) or the agent skipped a group.
  2. FILL (quota-costing, DEFERRED): a lean agent that, per stale product, fills ONLY
     the missing groups — deterministic for size/volume groups whose value is already
     in the name/source, one analyze_image call only when a VISUAL group is missing.

We run DETECT every cycle to size the eventual sweep; FILL is held until the schema
stabilises (running it against a still-moving schema would re-touch the same products).
"""
import json, glob, re
from pathlib import Path
import filter_schema_store as fss

HERE = Path(__file__).parent
VISUAL_GROUPS = {"цвят", "форма", "материал", "тип", "принт", "декор"}


def _attr_keys(attrs):
    keys = set()
    for part in str(attrs or "").split(";"):
        if ":" in part:
            keys.add(part.split(":", 1)[0].strip().lower())
    return keys


def missing_groups(record, cats=None):
    """Filter groups defined for this product's category that are absent from its
    Атрибути. Returns (missing_group_names, is_stale)."""
    f = record.get("fields") or {}
    cat = str(f.get("Категории") or "").split(";")[0].strip()
    groups = (cats or fss.load()).get(cat, [])
    if not groups:
        return [], False
    have = _attr_keys(f.get("Атрибути"))
    want = [str((g or {}).get("група") or "").strip() for g in groups if (g or {}).get("група")]
    missing = [g for g in want if g and g.lower() not in have]
    stamped = (record.get("meta") or {}).get("schema_fp")
    is_stale = stamped is not None and stamped != fss.category_fingerprint(cat, cats)
    return missing, is_stale


def load_records():
    recs = []
    for fp in glob.glob(str(HERE / "results.lane*.jsonl")):
        for line in open(fp, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if "agentic" in ((d.get("meta") or {}).get("notes") or []):
                recs.append(d)
    return recs


def detect(records=None):
    """Free report: how many finished products are missing >=1 category filter group,
    the worst offending groups, and how many are stale vs schema-grown. Sizes the sweep."""
    records = records or load_records()
    cats = fss.load()
    n_missing = n_stale = 0
    group_counts = {}
    per_product = []
    for d in records:
        miss, stale = missing_groups(d, cats)
        if stale:
            n_stale += 1
        if miss:
            n_missing += 1
            per_product.append((str(d.get("code")), miss))
            for g in miss:
                group_counts[g] = group_counts.get(g, 0) + 1
    return {
        "total": len(records),
        "with_missing_groups": n_missing,
        "stale_fingerprint": n_stale,
        "top_missing_groups": dict(sorted(group_counts.items(), key=lambda x: -x[1])[:15]),
        "sample": per_product[:10],
    }


# ---- FILL (deferred; deterministic part only wired, vision part guarded) ----------
_NUM_UNIT = re.compile(r"(\d+(?:[.,]\d+)?\s*(?:см|мм|мл|л|кг|г|бр|части))", re.IGNORECASE)

# Technical filter groups whose value appears verbatim in the product text. Extraction
# only — a value is written ONLY if the exact token exists in the name/description.
_TECH_RX = {
    "волтаж": re.compile(r"\b\d{2,3}\s*[-–]?\s*\d{0,3}\s*[VvВв]\b|\b\d{1,2}\s*[Vv]\b"),
    "напрежение": re.compile(r"\b\d{2,3}\s*[VvВв]\b"),
    "мощност": re.compile(r"\b\d{1,4}\s*(?:W|Вт|вата|kW|кВт)\b"),
    "лумени": re.compile(r"\b\d{2,5}\s*(?:lm|лм|лумена?)\b", re.IGNORECASE),
    "фасонка": re.compile(r"\b(?:E14|E27|E40|G4|G9|GU10|GU5\.3|GX53|MR16)\b", re.IGNORECASE),
    "тегло": re.compile(r"\b\d+(?:[.,]\d+)?\s*(?:кг|kg|г|гр)\b", re.IGNORECASE),
    "дължина": re.compile(r"\b\d+(?:[.,]\d+)?\s*(?:см|м|cm|m)\b", re.IGNORECASE),
    "диаметър": re.compile(r"(?:Ø|ø|⌀)\s*\d+(?:[.,]\d+)?\s*(?:см|мм|cm|mm)?", re.IGNORECASE),
    "брой в опаковка": re.compile(r"\b\d{1,3}\s*(?:бр|части|броя)\b", re.IGNORECASE),
}


def fill_deterministic(record, cats=None):
    """Fill ONLY the missing groups whose value is unambiguously present in the name/
    source, WITHOUT any model call (e.g. a 'Размер'/'Обем' group when the name already
    carries '40x50 см' / '18 л'). Visual groups are left for the deferred vision filler.
    Returns (new_attrs_or_None, filled_groups)."""
    miss, _ = missing_groups(record, cats)
    if not miss:
        return None, []
    f = record.get("fields") or {}
    name = str(f.get("Наименование") or "")
    attrs = str(f.get("Атрибути") or "").strip()
    filled = []
    additions = []
    for g in miss:
        gl = g.lower()
        if gl in VISUAL_GROUPS:
            continue                                   # needs the deferred vision pass
        if gl in ("размер", "размери", "габарит"):
            m = re.search(r"(?:Ø|ø|⌀)?\d+(?:[.,]\d+)?\s*[xх×]\s*\d+(?:[.,]\d+)?"
                          r"(?:\s*[xх×]\s*\d+(?:[.,]\d+)?)?\s*(?:см|мм|cm|mm)?", name)
            if m:
                additions.append(f"{g}: {m.group(0).strip()}"); filled.append(g)
        elif gl in ("обем", "вместимост"):
            m = re.search(r"\d+(?:[.,]\d+)?\s*(?:мл|л|ml|l)\b", name, re.IGNORECASE)
            if m:
                additions.append(f"{g}: {m.group(0).strip()}"); filled.append(g)
        else:
            # TECHNICAL groups: the value often sits verbatim in the name/description
            # (e.g. '220V', '40W', '400 lm', 'E27') — extract it, never guess it.
            hay = name + " " + str(f.get("Описание") or "")[:600]
            rx = _TECH_RX.get(gl)
            if rx:
                m = rx.search(hay)
                if m:
                    additions.append(f"{g}: {m.group(0).strip()}"); filled.append(g)
    if not additions:
        return None, []
    new = (attrs + ("; " if attrs else "") + "; ".join(additions)).strip("; ")
    return new, filled


if __name__ == "__main__":
    import sys
    rep = detect()
    print(json.dumps({k: v for k, v in rep.items() if k != "sample"},
                     ensure_ascii=False, indent=1))
    if "--sample" in sys.argv:
        for code, miss in rep["sample"]:
            print(" ", code, "->", miss)
