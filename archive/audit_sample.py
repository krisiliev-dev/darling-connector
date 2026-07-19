# -*- coding: utf-8 -*-
"""Weekly quality spot-audit: re-check a random sample of finished products
with a FRESH agent (different model family than worker and reviewer).

For each sampled product the auditor gets the produced fields, the ground
truth, and the image, and must hunt for factual errors (wrong material/color/
type, fake brand, wrong category, bad Bulgarian). Findings go to a dated
markdown report; products with critical errors are queued in
reprocess_queue.txt (run reprocess.py to send them back through the pipeline).

Usage:  python audit_sample.py [sample_size]     (default 12)
"""
import json
import os
import random
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).parent
RESULTS_PATH = HERE / "results.jsonl"
TASKS_PATH = HERE / "tasks.jsonl"
REPORT_DIR = HERE / "audit_reports"
QUEUE_PATH = HERE / "reprocess_queue.txt"

HERMES_EXE = r"C:\Users\lora_\AppData\Roaming\uv\tools\hermes-agent\Scripts\hermes.exe"
HERMES_HOME = r"C:\Users\lora_\.hermes"
AUDIT_MODEL = os.environ.get("PIPELINE_AUDIT_MODEL", "gemini-3.5-flash")
AUDIT_PROVIDER = os.environ.get("PIPELINE_AUDIT_PROVIDER", "gemini")
TIMEOUT_S = 600


def extract_json(text):
    blocks = re.findall(r"```json\s*(.*?)```", text, re.DOTALL)
    for block in reversed(blocks):
        try:
            return json.loads(block)
        except Exception:
            pass
    return None


def build_prompt(task, record):
    gt = {k: v for k, v in task["ground_truth"].items() if v is not None}
    return f"""Ти си независим одитор на качеството на продуктови данни за български онлайн магазин.
Продуктът по-долу вече е обработен от друга система. Намери ФАКТИЧЕСКИ грешки, ако има такива.

## НАДЕЖДНИ ДАННИ (склад + скрейпнати от доставчик)
```json
{json.dumps(gt, ensure_ascii=False, indent=1)}
```

## ОБРАБОТЕНИ ДАННИ (за одит)
```json
{json.dumps(record["fields"], ensure_ascii=False, indent=1)}
```

## КАК ДА ОДИТИРАШ
1. Ако има URL на снимка в "Снимки" — извикай vision_analyze и провери: съответства ли
   типът продукт, материалът, цветът и броят части на снимката?
2. Сравни всяко твърдение в Описание/Атрибути с надеждните данни и снимката.
3. Провери езика: руски/английски думи, изкривени думи, мета-коментари в клиентски текст.
4. Брандът: реален бранд ли е (не доставчик като LEVENA/MIRA-N/EGERA)? Правилно изписан?
5. Не наказвай за липсваща информация — само за ГРЕШНА информация.

## ПОЛИТИКИ НА СИСТЕМАТА (НЕ ги отчитай като грешки)
- ЦЕНА: синхронизира се автоматично от склада Microinvest на финалната стъпка и е вярна
  по дефиниция — НЕ одитирай цени и не ги сравнявай със скрейпнати цени.
- Разминаване на кодове между обработените данни и "scrape_code" е очаквано при
  приблизителни съвпадения — не е грешка на обработката.
- Ако продуктът е обозначен за човешки преглед с честно описани проблеми, това е
  СИСТЕМАТА, РАБОТЕЩА ПРАВИЛНО — оцени качеството на съдържанието, но отбележи
  "хванато от системата" вместо да го третираш като пропуск.

## ОТГОВОР — САМО ЕДИН ```json блок:
{{"ok": true/false,
 "score": 1-5 (5 = безупречно, 1 = сериозни фактически грешки),
 "critical": true/false (невярна фактическа информация, видима за клиент),
 "errors": ["кратко описание на всяка открита грешка"]}}
Започни директно с ```json"""


def run_audit(prompt):
    env = dict(os.environ, HERMES_HOME=HERMES_HOME)
    proc = subprocess.run(
        [HERMES_EXE, "-z", prompt, "--cli", "-t", "web,vision",
         "-m", AUDIT_MODEL, "--provider", AUDIT_PROVIDER],
        capture_output=True, timeout=TIMEOUT_S, env=env)
    return extract_json(proc.stdout.decode("utf-8", errors="replace"))


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    records = []
    for rp in [RESULTS_PATH, *HERE.glob("results.lane*.jsonl")]:
        if Path(rp).exists():
            records += [json.loads(l) for l in open(rp, encoding="utf-8") if l.strip()]
    if not records:
        print("No results to audit yet.")
        return
    random.seed(date.today().isoformat())
    sample = random.sample(records, min(n, len(records)))
    codes = {r["code"] for r in sample}

    tasks = {}
    with open(TASKS_PATH, encoding="utf-8") as f:
        for line in f:
            t = json.loads(line)
            if t["code"] in codes:
                tasks[t["code"]] = t

    REPORT_DIR.mkdir(exist_ok=True)
    report = REPORT_DIR / f"audit_{date.today().isoformat()}.md"
    lines = [f"# Одит на качеството — {date.today().isoformat()}",
             f"Модел-одитор: {AUDIT_MODEL}; извадка: {len(sample)} от {len(records)} обработени.", ""]
    critical_codes = []
    scores = []
    for r in sample:
        task = tasks.get(r["code"])
        if not task:
            continue
        try:
            verdict = run_audit(build_prompt(task, r))
        except Exception as e:
            verdict = None
            lines.append(f"## {r['code']} — ОДИТЪТ СЕ ПРОВАЛИ: {str(e)[:120]}")
            continue
        if not verdict:
            lines.append(f"## {r['code']} — одиторът не върна валиден JSON")
            continue
        score = verdict.get("score")
        scores.append(score if isinstance(score, (int, float)) else 0)
        status = "КРИТИЧНО" if verdict.get("critical") else ("ок" if verdict.get("ok") else "забележки")
        lines.append(f"## {r['code']} — {status} (оценка {score}/5)")
        for err in verdict.get("errors") or []:
            lines.append(f"- {err}")
        lines.append("")
        if verdict.get("critical"):
            critical_codes.append(r["code"])

    if scores:
        lines.insert(2, f"**Средна оценка: {sum(scores)/len(scores):.1f}/5 — "
                        f"критични: {len(critical_codes)}**\n")
    report.write_text("\n".join(lines), encoding="utf-8")

    if critical_codes:
        with open(QUEUE_PATH, "a", encoding="utf-8") as f:
            for c in critical_codes:
                f.write(c + "\n")
    print(f"[{datetime.now().isoformat(timespec='seconds')}] Audit done: "
          f"{len(scores)} audited, avg {sum(scores)/max(len(scores),1):.1f}/5, "
          f"{len(critical_codes)} critical -> {report}")


if __name__ == "__main__":
    main()
