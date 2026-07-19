# -*- coding: utf-8 -*-
"""Send audited-bad products back through the pipeline.

Reads reprocess_queue.txt, archives the affected result lines to
results_reprocessed_archive.jsonl, removes them from results.jsonl (so the
cron picks the codes up again), and clears the queue.
"""
from datetime import datetime
from pathlib import Path
import json

HERE = Path(__file__).parent
RESULTS = HERE / "results.jsonl"
QUEUE = HERE / "reprocess_queue.txt"
ARCHIVE = HERE / "results_reprocessed_archive.jsonl"


def main():
    if not QUEUE.exists() or not QUEUE.read_text(encoding="utf-8").strip():
        print("Reprocess queue is empty.")
        return
    codes = {c.strip().lstrip("﻿") for c in
             QUEUE.read_text(encoding="utf-8-sig").splitlines() if c.strip()}
    moved_total = kept_total = 0
    with open(ARCHIVE, "a", encoding="utf-8") as arch:
        arch.write(f'{{"_batch": "{datetime.now().isoformat(timespec="seconds")}"}}\n')
        for rp in [RESULTS, *HERE.glob("results.lane*.jsonl")]:
            if not Path(rp).exists():
                continue
            kept, moved = [], []
            with open(rp, encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    (moved if json.loads(line)["code"] in codes else kept).append(line)
            if moved:
                arch.writelines(moved)
                Path(rp).write_text("".join(kept), encoding="utf-8")
            moved_total += len(moved)
            kept_total += len(kept)
    QUEUE.write_text("", encoding="utf-8")
    print(f"Requeued {moved_total} products ({len(codes)} codes); "
          f"{kept_total} results kept. The cron will redo them.")


if __name__ == "__main__":
    main()
