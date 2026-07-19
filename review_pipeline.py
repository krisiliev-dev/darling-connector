# -*- coding: utf-8 -*-
"""PIPELINE REVIEWER AGENT (owner 2026-07-18): an independent LLM look at freshly-processed
v2 products that reports SYSTEMIC problems (not per-product flags — that's needs_human).

Samples N recent v2 products, judges each holistically (is the LEAF right for what this
actually is? are attributes sensible & on-vocabulary? does the description assert anything
not in the record? is the name good?), then aggregates into PATTERNS the owner/Claude can
act on. Read-only: never writes product data. Output: printed + appended to
pipeline_review.jsonl.

  python review_pipeline.py [N]     # review N recent v2 products (default 15)
"""
import json
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent

JUDGE = """Ти си строг одитор на качеството на продуктови данни за онлайн магазин. Виж
ЕДИН обработен продукт и прецени дали има проблем. Данни:
  Каса (оригинал): {stoka}
  Присвоена категория-лист: {leaf}
  Тип: {typ}
  Бранд: {brand}
  Атрибути: {attrs}
  Име: {name}
  Описание: {desc}

Прецени:
1. КАТЕГОРИЯ: листът правилен ли е за този продукт? (най-важно)
2. АТРИБУТИ: стойностите логични ли са и съответстват ли на продукта?
3. ОПИСАНИЕ: съдържа ли твърдения (число, материал, цвят), които ги няма в атрибутите?
4. ИМЕ: ясно и точно ли е?

Върни САМО валиден JSON:
{{"категория_ок": true|false, "вярна_категория": "<ако не е ок, каква трябва, иначе null>",
 "атрибути_ок": true|false, "описание_ок": true|false,
 "халюцинация": "<конкретното измислено твърдение или null>",
 "тежест": "висока|средна|ниска", "бележка": "<едно изречение>"}}"""


def _recent(n):
    import db
    con = db.connect()
    rows = con.execute("SELECT code, record_json, ts FROM products "
                       "WHERE record_json IS NOT NULL ORDER BY ts DESC LIMIT 400").fetchall()
    con.close()
    out = []
    for code, rj, ts in rows:
        try:
            rec = json.loads(rj)
        except Exception:
            continue
        if "v2" in [str(x) for x in ((rec.get("meta") or {}).get("notes") or [])]:
            out.append((str(code), rec))
        if len(out) >= n:
            break
    return out


def review(n=15):
    import run_one as ro
    sample = _recent(n)
    if not sample:
        print("no v2 products yet")
        return
    findings = []
    cat_bad = attr_bad = desc_bad = halluc = 0
    wrong_leaf = Counter()
    for code, rec in sample:
        f = rec.get("fields") or {}
        m = rec.get("meta") or {}
        gt = {}  # stoka from the record's task isn't stored; use name context
        attrs = str(f.get("Атрибути") or "")
        typ = next((p.split(":", 1)[1].strip() for p in attrs.split(";")
                    if p.strip().lower().startswith("тип")), "")
        prompt = JUDGE.format(
            stoka=str(f.get("Наименование") or "")[:80], leaf=m.get("leaf_name") or "?",
            typ=typ, brand=f.get("Бранд") or "—", attrs=attrs[:300],
            name=f.get("Наименование") or "", desc=str(f.get("Описание") or "")[:500])
        try:
            out, _model = ro.run_reviewer_direct(prompt)
            d = ro.extract_json(out) or {}
        except Exception as e:
            continue
        issues = []
        if d.get("категория_ок") is False:
            cat_bad += 1
            issues.append("leaf→" + str(d.get("вярна_категория")))
            if d.get("вярна_категория"):
                wrong_leaf[str(m.get("leaf_name")) + " ⇒ " + str(d.get("вярна_категория"))] += 1
        if d.get("атрибути_ок") is False:
            attr_bad += 1
            issues.append("attrs")
        if d.get("описание_ок") is False:
            desc_bad += 1
        if d.get("халюцинация"):
            halluc += 1
            issues.append("HALLUC:" + str(d.get("халюцинация"))[:40])
        if issues:
            findings.append({"code": code, "leaf": m.get("leaf_name"),
                             "sev": d.get("тежест"), "issues": issues,
                             "note": d.get("бележка")})

    k = len(sample)
    print(f"===== PIPELINE REVIEW — {k} recent v2 products =====")
    print(f"  leaf wrong:     {cat_bad}/{k} ({round(100*cat_bad/k)}%)")
    print(f"  attrs wrong:    {attr_bad}/{k}")
    print(f"  desc issues:    {desc_bad}/{k}")
    print(f"  hallucinations: {halluc}/{k}")
    if wrong_leaf:
        print("  SYSTEMIC leaf corrections seen:")
        for pat, c in wrong_leaf.most_common(6):
            print(f"    {c}× {pat}")
    print("  sample issues:")
    for fi in findings[:8]:
        print(f"    {fi['code']} [{fi['sev']}] {fi['issues']} — {fi['note']}")
    snap = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "sampled": k,
            "leaf_wrong": cat_bad, "attr_wrong": attr_bad, "desc_issues": desc_bad,
            "hallucinations": halluc, "wrong_leaf_patterns": dict(wrong_leaf),
            "findings": findings}
    with (HERE / "pipeline_review.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(snap, ensure_ascii=False) + "\n")
    return snap


if __name__ == "__main__":
    review(next((int(a) for a in sys.argv[1:] if a.isdigit()), 15))
