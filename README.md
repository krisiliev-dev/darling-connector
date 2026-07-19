# Agent pipeline — one product per AI agent run

Verifies/corrects the AI-generated product fields for the online store, **one
product per dedicated Hermes agent invocation**, using Microinvest + scraped
supplier data as ground truth, `web_search` for brand checks, `vision_analyze`
for image checks, and a shared self-improving `guide.md`.

Scope: the 14,159 products with a scraped-data match (`Съвпадение == "да"`).

## How it works
```
prepare_tasks.py  (pandas, run once)   Excel -> tasks.jsonl (self-contained per-product tasks
                                       incl. ground truth + related-product candidates)
run_one.py        (stdlib)             next pending task -> builds prompt (task + guide.md)
                                       -> `hermes -z <prompt> --cli -t web,vision`
                                       -> validates the agent's JSON -> appends results.jsonl,
                                       appends new lessons to guide.md
run_batch.py      (stdlib)             bounded loop over run_one with a lock file
build_catalog.py  (pandas, on demand)  CANONICAL STORE: catalog.jsonl — one JSON doc per
                                       product {content, operational, provenance, quality,
                                       images, import_issues}. Applies: Microinvest price/
                                       stock/unit sync (as-is, owner directive), related
                                       symmetric closure (verified sources only), import
                                       validation, deactivation candidates. Also emits
                                       ../results/agent_verified_products.xlsx + coverage_report.md.
merge_results.py  (legacy)             superseded by build_catalog.py
```
All analysis/QA tools read catalog.jsonl, not Excel rows:
- golden.py           regression harness: `approve <codes>` snapshots perfect products;
                      `run` re-runs them through the current pipeline and diffs stable
                      fields (categories/brand/attrs/related/name-overlap/weight ±25%)
- duplicate_report.py -> ../results/duplicate_products.xlsx (dup source rows, same image,
                      same name, one till item -> many codes)
- category_proposals.py -> ../results/category_proposals.md (missing site categories)
- price_reconciliation.py, review_page.py, audit_sample.py + reprocess.py, backup_state.py

Design rules that fix the earlier failures:
- The agent NEVER touches Excel, pandas, file paths, or the terminal — everything it
  needs is inline in the prompt; only `web` and `vision` toolsets are enabled.
- All bookkeeping is append-only JSONL -> fully resumable, no pointer-file races.
- "Свързани" may only be chosen from a precomputed candidate list (no invented codes);
  the driver drops anything else.
- Non-editable columns (Цена, Количество, ...) are force-reverted by the driver if the
  agent changed them.
- A product failing 3 attempts is skipped (recorded in failures.jsonl) and never blocks
  the queue.

## Continuous operation
Hermes cron job `product_agent_pipeline` (id 95a42c817601, every 20 min) runs
`~/.hermes/scripts/product_batch_runner.py`, which executes
`run_batch.py --max-items 10 --max-minutes 18`. The lock file (`.runner.lock`)
makes overlapping runs exit cleanly. Requires the Hermes gateway (cron ticker)
to be running — check `~/.hermes/cron/ticker_heartbeat` mtime.

## Model & tool routing (IMPORTANT — two Hermes installs)
- Agent runs go through the **uv-tools** hermes.exe with `HERMES_HOME=C:\Users\lora_\.hermes`
  (set in run_one.py). The venv hermes.exe on PATH uses a DIFFERENT home
  (`AppData\Local\hermes`) whose cron ticker never runs — don't register jobs there.
- **Worker: zai / glm-4.7-flash** — stable ~2 min/product, cleanest Bulgarian.
  (gemini-3.5-flash won the bake-off on depth but free-tier throttling swings runs
  from 74s to 14min — unusable at volume; kept as env-override option.)
- **Reviewer: nvidia / mistral-large-3-675b** — independent second agent per product;
  checks language, attribute sourcing, formats; may correct TEXT-QUALITY fields only.
  Fact fields (category/brand/related/name-type) are driver-protected: disagreement
  escalates to needs_human instead of being applied (a text-only reviewer once
  "corrected" a vision-verified fix back to the wrong original — never again).
- Rejected in bake-off (bakeoff/*.jsonl): nemotron (Russian-isms), deepseek-v4 via
  nvidia (10-min timeout), mistral via direct API (12 min/product).
- `vision_analyze` pinned to **meta/llama-3.2-11b-vision via NVIDIA NIM** in
  `auxiliary.vision` (`~/.hermes/config.yaml`) — 3-5s/call, accurate, no daily
  caps. History: zai vision has no credits; Gemini free tier died mid-day with
  a payment/credit error. NOTE: `tools/vision_tools.py` in the uv install is
  patched (_EMBED_TARGET_BYTES 4MB->700KB, _EMBED_MAX_DIMENSION 7900->1280) —
  re-apply after `hermes update`.
- **Fabrication firewall** (run_one.py, added after a metal stand was sold as
  "transparent glass" while vision was down): workers must report
  "визуална проверка" (ок/неуспешна/няма снимка); Материал/Цвят attribute
  values survive only if textually sourced in original+GT data OR the image
  check succeeded; supplier names (LEVENA, MIRA-N, EGERA...) can never become
  the brand; weight can never be emptied; any drop/revert forces needs_human.
- run_batch has a circuit breaker: 3 consecutive failures stop the batch
  (provider quota/outage) instead of burning per-product retry budget.
- Env overrides: PIPELINE_MODEL/PIPELINE_PROVIDER, PIPELINE_REVIEW=0,
  PIPELINE_REVIEW_MODEL/PIPELINE_REVIEW_PROVIDER, PIPELINE_RESULTS_PATH,
  PIPELINE_NO_LESSONS=1 (used by bakeoff.ps1).

## Image findings (audit_images.py, 200-image sample)
- 91% already white background; ~9% grey/colored (levena11 mostly) — fixable
  locally with rembg (proof of concept validated, u2net model downloaded).
- 61% are small (<500px short side) — almost all from mira-n.net (76% of catalog).
- ~15% of sampled URLs failed to download — images are hotlinked to supplier
  domains, not locally hosted.
- egera.bg images (~1,838) carry an "EGERA" corner watermark.

## Monitoring & quality loop
- `runner.log` — one line per product (OK/FAIL, duration, confidence).
- progress: `(Get-Content results.jsonl | Measure-Object -Line).Lines` of 14,159.
- `failures.jsonl` — errors per attempt.
- Deliverable: run `merge_results.py` any time for a full Excel snapshot; rows carry
  `Статус проверка`, `Проблеми`, `needs_human`, `confidence`.
- `review_page.py` → ../results/review_page.html — visual queue of needs_human
  items (photo + fields + flags side by side).
- `audit_sample.py` — independent spot-audit with a THIRD model family
  (gemini-3.5-flash); runs weekly via cron `product_quality_audit`
  (Mondays 04:00, id 4f0565c65b46); reports to audit_reports/, queues critical
  products in reprocess_queue.txt; apply with `reprocess.py`.
- `price_reconciliation.py` → ../results/price_discrepancies.xlsx — Enriched
  'Цена' vs Microinvest 'Продажна цена' (first run 2026-07-09: 6,371 mismatches,
  17 items below cost).

## Driver guardrails (validate() in run_one.py)
- related ⊆ candidates, capped 10; categories ⊆ site tree; non-editables reverted
- fabrication firewall: Материал/Цвят need textual source or successful image check
- supplier names blocked as brand; weight never emptied, numeric, 0.005–100 kg
- name: catalog prefixes stripped, ≤80 chars, abbreviation flags
- description: h2+ul structure, meta-comments stripped, Russian-ism flags,
  50–450 words, cross-product duplicate detection (desc_hashes.txt)
- synonyms deduped, capped 15; meta length flags
- every blocked/suspicious case forces needs_human

## Free-model chain upkeep (hermes-portable)
Run with the venv python + HERMES_HOME=C:\Users\lora_\.hermes:
  scripts/discover_openrouter_free.py   # add new :free OpenRouter models
  scripts/health_check.py               # ping chain, drop dead, fastest first
Last run 2026-07-09: chain = nemotron, mistral-large(API), glm-4.7-flash,
tencent/hy3:free live + 14 throttled + 2 safety nets. hy3 bake-off: clean
Bulgarian but dismissed correct photo evidence in favor of flawed text — not
adopted as worker.

## Tuning
- Throughput ~1 product/2 min (free-model chain). Increase cron `--max-items`
  / frequency, or run extra `run_batch.py` terminals only after sharding tasks.jsonl
  (the lock intentionally prevents naive parallelism).
- Model: per-run override possible via `hermes -z ... -m <model> --provider <p>`
  (edit `run_one.py: run_agent`).
