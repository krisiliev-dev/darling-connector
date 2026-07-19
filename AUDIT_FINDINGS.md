# Project Audit — Findings & Cleanup Manifest (2026-07-19)

Read-only inventory across code, data/DB, and runtime (three parallel audits), reconciled.
Safety net: `pipeline.db` backed up (`pipeline.db.audit-bak-20260719`); code committed to a
fresh git baseline. Everything below is reversible via git except raw data deletes.

## Architecture verdict (now unambiguous)
- **Processing path is v2-only.** Cron/fleet → `run_batch.py --shard i/N` → `run_one.process_next()`
  → (because the `V2_MODE` sentinel exists) → `pipeline_v2.process()`. The v1 `process_agentic`
  / direct-worker chain still physically lives inside `run_one.py` but is a **dead branch**.
- **`run_one.py` stays** — it is the shared harness (providers, prompts, validate, dispatch)
  imported by 21 modules. Only its v1 *branches* are dead, not the file.
- **The DB (`pipeline.db`) is authoritative.** All readers read the DB; `results*.jsonl` is a
  rebuildable append-only export/recovery source. `db.py`'s docstring says the opposite — it is
  **stale** (fix it). Corrected by `run_one.py:1931`.
- 94 `.py`: **~60 keep, ~32 archive, 2 delete.** 13 archives already sit in `archive/`.

## MANIFEST

### DELETE (pure cruft; git covers code, no runtime refs)
- `_requeue_stuck.py` (2-line dead hack, imported by nothing)
- Source `.bak` blobs: `run_one.py.prefree_bak`, `pipeline_v2.py.pre_audit_bak`,
  `exhausted_models.txt.bak`, `exhausted_models.txt.oldacct`
- Data migration backups: `*.reflagbak` `*.catbak` `*.reqbak` `*.revbak` (~43 MB),
  `results.jsonl.reflagbak`
- Launch-day scratch: `v2_batch_aa` `v2_batch_ab` `v2_*_check*.txt` `v2_redo*` `pick.txt`
  `v2_straggler.txt` `results.smoke.jsonl` `results.smoke.log` `barsy_export.jsonl` (0-byte)

### ARCHIVE (move to `archive/` — one-off/superseded scripts, no live import)
attr_fill, attr_vision_fill, attr_reconcile (dead cluster) · quality_apply, tidy_apply,
tidy_test · variant_consistency, dup_products, related_fallback, restore_regressions ·
quota_forecast, price_reconciliation · build_catalog, golden, reprocess (v1, superseded) ·
scrape_miti, match_miti (one-shot, done) · supervise_status, review_cycle, monitor (superseded
by check_run/review_all) · name_vocab.raw.json, return_reasons.json (unreferenced data)

### ARCHIVE (large stale DATA — move out of working set, keep for DB rebuild safety)
- `catalog.jsonl` (103 MB, v1 derived; nothing reads it)
- `results.lanez_*.jsonl` (~69 MB, one-off stage passes; folded into DB `versions`)
- `archive_pre_agentic_*/`, `archive_pre_qwen_*/` (data snapshots), `image-samples/`, `bakeoff/`
- stale `*.log` / `fleet*.log`

### KEEP (corrections to agent output)
- **`v2_run_batch.py`** — actively spawned by the running `reprocess_partial.py`. KEEP.
- Barsy group (all `barsy_*`), pipeline_v2, run_one, run_batch, db, taxonomy_*, leaf_*,
  ean_*, review_server + schema_* pages, check_run, det_golden, and all shared libs.

### DB cleanup (after reprocess pauses + backup confirmed)
- Prune `versions` (230 MB, append-only): drop `record_json` on non-latest versions per code
  (keep `fields_json`/notes for the timeline) → ~150 MB reclaimed. `VACUUM` after.
- Delete `pipeline.db.audit-bak-20260719` **only after** cleanup verified.

## RUNTIME BUGS TO FIX (found in audit)
1. `pipeline_boot.py` references Scheduled Task `Darling_Pipeline` that **does not exist** →
   review_server / image pipeline / auto_check won't survive a reboot. Install task or drop boot.
2. `Hermes Rate Limit Monitor` scheduled task failing (LastResult=1) — underpins DashScope guard.
3. `db.py` docstring drift (says JSONL authoritative — it's not).
4. Provider chains duplicated in code: v1 `WORKER_CHAIN` (run_one) vs v2 chains (pipeline_v2) —
   consolidate to one config, or delete v1 chain with the v1 branch excision.
5. Three dead lane generations in `~/.hermes/scripts/` (3-lane `product_batch_runner*`, 6-lane
   `_bak_6lane/`) + two abandoned cron jobs (`product_processor`, `process_one.py`).

## DECISIONS NEEDED FROM OWNER
- **Shopify export path** (`shopify_export.py`, `shopify_search_sync.py`, `shopify_schema_align.py`):
  still a target, or fully replaced by the Barsy → Shopify route? Determines keep vs archive.
- **v1 excision depth**: leave the dormant v1 branch in `run_one.py` (safe, just dead weight),
  or excise it now (large dead-code reduction, needs careful testing since 21 modules import the file)?
- **DB `versions` prune**: ok to cap history / drop non-latest `record_json`?

---
## EXECUTED (2026-07-19)
- **Tranches 1-3 (cleanup):** deleted cruft + 43MB .bak sidecars; archived 22 one-off scripts → archive/,
  stale data (catalog.jsonl, results.lanez_*) → archive_data/. Kept shopify_schema_align (live v2 dep).
- **v1 excision:** removed process_agentic + inline direct-worker path + 4 dead helpers from run_one.py
  (2319→1475 lines). v2-only dispatch. Shared WORKER_SYS/DIRECT_PROVIDERS/_DIRECT_CLIENTS preserved.
- **DB:** NOT pruned — 0 free pages (VACUUM=0); all data live. 56MB record_json prune skipped (lossy).
  Removed 582MB redundant pipeline.db.audit-bak. Integrity: ok.
- **db.py docstring** corrected (DB authoritative). **barsy_api** hardened (retry timeouts/busy).
- **Cron lanes:** paused for audit → RESUMED. Catalog auto-processing back on.
- Verified after every step: imports + det_golden(44) + live product smoke. All git-committed.

## STILL OWNER ACTIONS (need admin / UI)
- Install Darling_Pipeline logon task (schtasks needs elevation) — command in commit msg / memory.
- Barsy UI: remove old Microinvest category roots + any dead cron gens (product_batch_runner*, _bak_6lane).
- Investigate failing "Hermes Rate Limit Monitor" scheduled task.
