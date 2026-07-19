# -*- coding: utf-8 -*-
"""Propose missing site categories.

Two evidence sources:
  1. verified products whose agents flagged category problems (reverted or
     noted) — these had no correct category to move to;
  2. Microinvest 'Група' values whose products land in generic/parent-only
     site categories — clusters big enough to deserve their own category.

Output: ../results/category_proposals.md (for the owner to approve; approved
categories then get added to the site + categories.json, and affected products
are requeued via reprocess.py).
"""
import io
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = Path(__file__).parent
EXCEL_PATH = r"C:\Users\lora_\Desktop\Local Database - enriched(AutoRecovered).xlsx"
CATALOG = HERE / "catalog.jsonl"
OUT = HERE.parent / "results" / "category_proposals.md"

MIN_CLUSTER = 15  # a Група needs at least this many products to deserve a category


def main():
    docs = []
    with open(CATALOG, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            if "code" in d:
                docs.append(d)

    # 1. agent-flagged category problems
    flagged = []
    for d in docs:
        p = d["provenance"]
        notes = p.get("notes") or []
        prob = str(p.get("problems") or "").lower()
        if any("invalid_category" in n for n in notes) or "категори" in prob:
            flagged.append(d)

    # 2. till groups vs current site category (generic = top-level only)
    micro = pd.read_excel(EXCEL_PATH, sheet_name="Микроinvest".replace("Микроinvest", "Microinvest"),
                          dtype={"Код": str})
    micro["Код"] = micro["Код"].str.strip()
    group_of = dict(zip(micro["Код"], micro["Група"].astype(str)))

    generic = defaultdict(list)
    for d in docs:
        cat = str(d["content"].get("Категории") or "")
        if "->" not in cat:  # top-level or empty = no specific shelf
            g = group_of.get(d["code"])
            if g and g.lower() not in ("nan", "none"):
                # till groups look like "6/АНИС- ПЛОВДИВ" (supplier) or real types
                generic[g.split("/")[-1].strip()].append(d["code"])

    clusters = {g: codes for g, codes in generic.items() if len(codes) >= MIN_CLUSTER}

    lines = [f"# Предложения за нови категории — {datetime.now():%Y-%m-%d}", ""]
    lines.append(f"## А. Продукти без вярна категория (сигнал от агентите): {len(flagged)}")
    examples = Counter()
    for d in flagged:
        examples[str(d['content'].get('Категории'))] += 1
    for cat, n in examples.most_common(15):
        lines.append(f"- текуща категория „{cat}“: {n} продукта")
    sample = [f"  - {d['code']}: {d['content'].get('Наименование')} "
              f"(проблем: {str(d['provenance'].get('problems'))[:120]})" for d in flagged[:10]]
    lines.extend(["", "Примери:"] + sample + [""])

    lines.append(f"## Б. Складови групи с ≥{MIN_CLUSTER} продукта, заседнали в обща категория")
    for g, codes in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
        lines.append(f"- **{g}** — {len(codes)} продукта (примерни кодове: {', '.join(codes[:5])})")
    lines.append("")
    lines.append("След одобрение: добавете категориите в сайта и в 'Филтри по категории', "
                 "обновете categories.json (prepare_tasks.py) и пуснете reprocess.py за засегнатите кодове.")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"flagged-by-agents: {len(flagged)}; till-group clusters: {len(clusters)}")
    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
