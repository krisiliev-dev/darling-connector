# -*- coding: utf-8 -*-
"""Drive the 12-lane v2 fleet through the V2_PRIORITY.txt allow-list, then stop.

Runs rounds of `run_batch.py --shard i/12` concurrently until every priority code has a
v2 version (or two rounds pass with zero progress — a stall guard). Honours PAUSE (the
arrearage breaker) between rounds. This is a CONTROLLED foreground driver for the
brand-confident batch; the Hermes cron lanes also process the same queue when they fire
(the per-shard lock prevents overlap), so this just makes it run continuously now.

  python run_priority_fleet.py            # default 12 lanes, 10-min rounds
"""
import subprocess
import sys
import time
import os
from pathlib import Path

HERE = Path(__file__).parent
NLANES = 12
ROUND_MIN = 10


def _remaining():
    import db
    prio = {ln.strip() for ln in (HERE / "V2_PRIORITY.txt").read_text(
        encoding="utf-8").splitlines() if ln.strip()}
    done = db.done_codes_v2()
    return len(prio - done), len(prio)


def main():
    if not (HERE / "V2_MODE").exists():
        print("V2_MODE sentinel missing — refusing to run", flush=True)
        return
    round_no = 0
    stalls = 0
    while True:
        if (HERE / "PAUSE").exists():
            print("PAUSE present — stopping the priority driver", flush=True)
            return
        remaining, total = _remaining()
        print(f"[round {round_no}] {remaining}/{total} priority products remaining",
              flush=True)
        if remaining == 0:
            print("PRIORITY BATCH COMPLETE — all brand-confident products processed.",
                  flush=True)
            return
        procs = []
        for i in range(NLANES):
            env = dict(os.environ)
            env["PYTHONIOENCODING"] = "utf-8"
            procs.append(subprocess.Popen(
                [sys.executable, "run_batch.py", "--shard", f"{i}/{NLANES}",
                 "--max-minutes", str(ROUND_MIN)],
                cwd=str(HERE), env=env,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
        for p in procs:
            p.wait()
        after, _ = _remaining()
        progressed = remaining - after
        print(f"[round {round_no}] processed {progressed} this round", flush=True)
        stalls = stalls + 1 if progressed == 0 else 0
        if stalls >= 2:
            print("No progress for 2 rounds — stopping (check provider health / logs).",
                  flush=True)
            return
        round_no += 1


if __name__ == "__main__":
    main()
