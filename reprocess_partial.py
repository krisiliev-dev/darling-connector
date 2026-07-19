# -*- coding: utf-8 -*-
"""Fully reprocess a specific set of codes through the IMPROVED v2 pipeline (owner
2026-07-19): the 639 products whose original run fell back to v1 text (mid-batch
throttling). Now the pipeline is better — fixed over-flagging, SEO text rules, best-
models chain, NVIDIA vision restored — so a fresh pass gives consistent v2 records.
The monotonic quality gate still protects: a worse rerun can't overwrite a better one.

Shards the codes across N processes (each runs v2_run_batch --force --redo on its shard,
writing to its own results file), loops until all have a fresh reprocessed version or
two rounds make no progress.

  python reprocess_partial.py reprocess_codes.txt [N]
"""
import subprocess
import sys
import os
import json
from pathlib import Path

HERE = Path(__file__).parent
N = 12


def _codes(path):
    return [c.strip() for c in Path(path).read_text(encoding="utf-8").splitlines() if c.strip()]


def _reprocessed():
    """Codes that have a FRESH reprocess version tagged with the current round's marker."""
    import os
    import db
    tag = os.environ.get("V2_REPROCESS_TAG") or "v2_reprocess"
    con = db.connect()
    try:
        rows = con.execute("SELECT code FROM products WHERE notes_json LIKE ?",
                           ("%" + tag + "%",)).fetchall()
    finally:
        con.close()
    return {str(c) for c, in rows}


def main(path):
    codes = _codes(path)
    print(f"reprocessing {len(codes)} partial products through improved v2", flush=True)
    shard_dir = HERE / ".reprocess_shards"
    shard_dir.mkdir(exist_ok=True)
    stalls = 0
    rnd = 0
    while True:
        done = _reprocessed()
        todo = [c for c in codes if c not in done]
        print(f"[round {rnd}] {len(todo)}/{len(codes)} remaining", flush=True)
        if not todo:
            print("REPROCESS COMPLETE — all partial products have fresh v2 records.",
                  flush=True)
            return
        shards = [todo[i::N] for i in range(N)]
        procs = []
        for i, s in enumerate(shards):
            if not s:
                continue
            fp = shard_dir / f"shard_{i}.txt"
            fp.write_text("\n".join(s), encoding="utf-8")
            env = dict(os.environ)
            env["PYTHONIOENCODING"] = "utf-8"
            env["PIPELINE_RESULTS_PATH"] = str(HERE / f"results.reprocess{i}.jsonl")
            env["V2_REPROCESS"] = "1"          # pipeline tags records 'v2_reprocess'
            procs.append(subprocess.Popen(
                [sys.executable, "v2_run_batch.py", str(fp), "--force", "--redo"],
                cwd=str(HERE), env=env,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
        for p in procs:
            p.wait()
        after = len(codes) - len([c for c in codes if c not in _reprocessed()])
        progressed = len(codes) - len(todo) - (len(codes) - after)
        stalls = stalls + 1 if progressed <= 0 else 0
        if stalls >= 2:
            print("no progress for 2 rounds — stopping (check provider health).",
                  flush=True)
            return
        rnd += 1


def _acquire_lock():
    """Single-instance guard — the shared-hermes gateway can double-launch this driver,
    spawning two full sets of shard workers that race the same products."""
    import time
    lock = HERE / ".reprocess.lock"
    try:
        fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        return lock
    except FileExistsError:
        try:
            if (time.time() - lock.stat().st_mtime) / 3600.0 >= 6:
                lock.unlink()
                return _acquire_lock()
        except OSError:
            pass
        return None


if __name__ == "__main__":
    _lk = _acquire_lock()
    if _lk is None:
        print("another reprocess driver is already running — exiting.", flush=True)
        raise SystemExit(0)
    try:
        main(sys.argv[1] if len(sys.argv) > 1 else str(HERE / "reprocess_codes.txt"))
    finally:
        try:
            _lk.unlink()
        except OSError:
            pass
