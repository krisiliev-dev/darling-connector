# -*- coding: utf-8 -*-
"""Golden-set regression harness.

Workflow:
  1. You review products (review_page.html / the Excel) and approve perfect ones:
       python golden.py approve 200465 0191508 ...
     Their current verified fields snapshot into golden_set.jsonl and the codes
     into golden_codes.txt (marked in the catalog as quality.golden).
  2. After ANY pipeline change (model, prompt, guide, guardrail):
       python golden.py run [--limit N]
     Re-runs each golden product through the CURRENT pipeline into a throwaway
     results file and diffs the stable fields against the approved snapshot.
     Drift -> golden_reports/golden_<date>.md, exit code 1.

Field comparison is tolerant to LLM wording variance: exact match for
Категории/Бранд/Свързани codes/attribute pairs, token-overlap for the name,
±25% for weight. Descriptions are NOT compared (wording always varies).
"""
import io
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

# UTF-8 stdout for the CLI, but ONLY when run as a script — reassigning sys.stdout at
# import time hijacks stdout for any process that imports this module.
if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = Path(__file__).parent
GOLDEN_SET = HERE / "golden_set.jsonl"
GOLDEN_CODES = HERE / "golden_codes.txt"
RESULTS = HERE / "results.jsonl"
REPORT_DIR = HERE / "golden_reports"
PY = sys.executable
RUN_ONE = HERE / "run_one.py"


def load_results():
    out = {}
    for rp in [RESULTS, *HERE.glob("results.lane*.jsonl")]:
        if Path(rp).exists():
            with open(rp, encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        r = json.loads(line)
                        out[r["code"]] = r
    return out


def norm_attrs(s):
    return {p.strip().lower() for p in str(s or "").split(";") if p.strip()}


def norm_rel(s):
    return {p.split("|")[0].strip() for p in re.split(r"[;\n]+", str(s or "")) if p.strip()}


def name_overlap(a, b):
    ta = set(re.findall(r"\w+", str(a or "").lower()))
    tb = set(re.findall(r"\w+", str(b or "").lower()))
    return len(ta & tb) / max(len(ta | tb), 1)


def diff_fields(golden, fresh):
    problems = []
    g, f = golden["fields"], fresh["fields"]
    if str(g.get("Категории") or "") != str(f.get("Категории") or ""):
        problems.append(f"Категории: '{g.get('Категории')}' -> '{f.get('Категории')}'")
    if str(g.get("Бранд") or "").lower() != str(f.get("Бранд") or "").lower():
        problems.append(f"Бранд: '{g.get('Бранд')}' -> '{f.get('Бранд')}'")
    if norm_attrs(g.get("Атрибути")) != norm_attrs(f.get("Атрибути")):
        problems.append(f"Атрибути: '{g.get('Атрибути')}' -> '{f.get('Атрибути')}'")
    if norm_rel(g.get("Свързани")) != norm_rel(f.get("Свързани")):
        problems.append(f"Свързани: '{g.get('Свързани')}' -> '{f.get('Свързани')}'")
    ov = name_overlap(g.get("Наименование"), f.get("Наименование"))
    if ov < 0.6:
        problems.append(f"Наименование ({ov:.0%} сходство): "
                        f"'{g.get('Наименование')}' -> '{f.get('Наименование')}'")
    try:
        gw, fw = float(g.get("Тегло (кг)") or 0), float(f.get("Тегло (кг)") or 0)
        if gw > 0 and abs(fw - gw) / gw > 0.25:
            problems.append(f"Тегло: {gw} -> {fw}")
    except (TypeError, ValueError):
        pass
    return problems


def cmd_approve(codes):
    results = load_results()
    existing = {}
    if GOLDEN_SET.exists():
        with open(GOLDEN_SET, encoding="utf-8") as f:
            existing = {json.loads(l)["code"]: json.loads(l) for l in f if l.strip()}
    added = 0
    for code in codes:
        r = results.get(code)
        if not r:
            print(f"  {code}: not in results.jsonl — process it first")
            continue
        existing[code] = {"code": code, "approved_at": date.today().isoformat(),
                          "fields": r["fields"]}
        added += 1
    with open(GOLDEN_SET, "w", encoding="utf-8") as f:
        for rec in existing.values():
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    GOLDEN_CODES.write_text("\n".join(existing.keys()) + "\n", encoding="utf-8")
    print(f"Golden set: {len(existing)} products ({added} added/updated)")


def cmd_run(limit=None):
    if not GOLDEN_SET.exists():
        print("Golden set is empty — approve products first.")
        return 0
    golden = [json.loads(l) for l in open(GOLDEN_SET, encoding="utf-8") if l.strip()]
    if limit:
        golden = golden[:limit]
    tmp_results = HERE / "golden_check.jsonl"
    tmp_results.unlink(missing_ok=True)

    REPORT_DIR.mkdir(exist_ok=True)
    report = REPORT_DIR / f"golden_{date.today().isoformat()}.md"
    lines = [f"# Golden-set регресионен тест — {date.today().isoformat()}", ""]
    drift = 0
    env = dict(os.environ, PIPELINE_RESULTS_PATH=str(tmp_results), PIPELINE_NO_LESSONS="1")
    for g in golden:
        code = g["code"]
        proc = subprocess.run([PY, str(RUN_ONE), code], capture_output=True,
                              timeout=1800, env=env)
        fresh = None
        if tmp_results.exists():
            for line in open(tmp_results, encoding="utf-8"):
                r = json.loads(line)
                if r["code"] == code:
                    fresh = r
        if not fresh:
            drift += 1
            lines.append(f"## {code} — ПРОВАЛ: пайплайнът не върна резултат "
                         f"(rc={proc.returncode})")
            continue
        problems = diff_fields(g, fresh)
        if problems:
            drift += 1
            lines.append(f"## {code} — ОТКЛОНЕНИЕ")
            lines.extend(f"- {p}" for p in problems)
        else:
            lines.append(f"## {code} — ок")
        lines.append("")
    lines.insert(1, f"**{len(golden)} тествани, {drift} с отклонение**\n")
    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"Golden run: {len(golden)} tested, {drift} drifted -> {report}")
    return 1 if drift else 0


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "approve":
        cmd_approve(sys.argv[2:])
    elif len(sys.argv) >= 2 and sys.argv[1] == "run":
        limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
        sys.exit(cmd_run(limit))
    else:
        print(__doc__)
