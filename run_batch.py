# -*- coding: utf-8 -*-
"""Run the per-product agent loop for a bounded number of items / minutes.

Safe to fire from cron: a lock file prevents overlapping runs, and every item
is independently resumable (see run_one.py).

Usage:
  python run_batch.py [--max-items N] [--max-minutes M]
"""
import argparse
import os
import sys
import time
from pathlib import Path

# --shard must be exported BEFORE run_one is imported (it reads env at import).
_ap = argparse.ArgumentParser(add_help=False)
_ap.add_argument("--shard", default="")
_shard_args, _ = _ap.parse_known_args()
if _shard_args.shard:
    os.environ["PIPELINE_SHARD"] = _shard_args.shard
    lane = _shard_args.shard.split("/")[0]
    os.environ.setdefault("PIPELINE_RESULTS_PATH",
                          str(Path(__file__).parent / f"results.lane{lane}.jsonl"))

import run_one

_lock_suffix = _shard_args.shard.replace("/", "-") if _shard_args.shard else ""
LOCK_PATH = Path(__file__).parent / f".runner.lock{_lock_suffix}"
# Longest legitimate batch: 12-min budget + one in-flight item (2 x 7-min agent
# calls) ≈ 26 min. A lock older than 40 min is an orphan (e.g. the shim killed
# run_batch before `finally` ran on 2026-07-09) — steal it, don't stall 2h.
# 40 min was SHORTER than a worst-case single ReAct step (chain walk x 70s timeouts),
# letting cron steal a live lock and duplicate the shard. The chain walk is now capped
# at 8 models (~9 min worst case), so 90 min is beyond any legitimate batch.
LOCK_STALE_S = 90 * 60


def acquire_lock():
    if LOCK_PATH.exists():
        age = time.time() - LOCK_PATH.stat().st_mtime
        if age < LOCK_STALE_S:
            return False
        run_one.log(f"Stealing stale lock (age {int(age)}s)")
    LOCK_PATH.write_text(str(os.getpid()), encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-items", type=int, default=10)
    ap.add_argument("--max-minutes", type=float, default=12)
    ap.add_argument("--shard", default="")  # consumed at import time above
    args = ap.parse_args()

    if not acquire_lock():
        run_one.log("Another runner is active — exiting.")
        return 0

    deadline = time.time() + args.max_minutes * 60
    done = failed = streak = 0
    try:
        for _ in range(args.max_items):
            if time.time() >= deadline:
                run_one.log("Time budget reached.")
                break
            status = run_one.process_next()
            if status == "empty":
                break
            if status == "done":
                done += 1
                streak = 0
            else:
                failed += 1
                streak += 1
                if streak >= 3:
                    # Circuit breaker: likely provider quota/outage. Stop the
                    # batch instead of burning retry budget across the queue;
                    # cron tries again next cycle.
                    run_one.log("3 consecutive failures — stopping batch (provider issue?).")
                    break
            LOCK_PATH.touch()  # keep the lock fresh for long batches
        run_one.log(f"Batch finished: {done} done, {failed} failed.")
    finally:
        try:
            LOCK_PATH.unlink()
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
