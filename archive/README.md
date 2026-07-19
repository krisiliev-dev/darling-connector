# Archived (2026-07-16)

One-off / superseded scripts and old result snapshots, moved here to reduce footguns.
Nothing in the live pipeline imports these (verified). Safe to delete after a while.

- *.py — one-time fixups (reflag/requeue/find_affected/clean_catalogue/merge_results),
  superseded review tools (review_recent*, review_page), one-off audits, and the
  one-time task builder (prepare_tasks).
- results_v*_archive.jsonl / results_reprocessed_archive.jsonl — old pipeline-version
  output snapshots. NOT matched by the live `results.lane*.jsonl` glob.

Still-active tools kept in the parent dir: reprocess.py, backup_state.py,
supervise_status.py, price_reconciliation.py.
