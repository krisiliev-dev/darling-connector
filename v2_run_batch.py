# -*- coding: utf-8 -*-
"""Supervised one-off v2 batch runner (smoke tests / targeted reruns).
NOT a lane driver: single instance only. Writes to its own results file, honours
PAUSE (override with --force for supervised tests) and skips already-done codes
(override with --redo).

  python v2_run_batch.py codes.txt [--force] [--redo]
"""
import sys
import os
import json
import io
from pathlib import Path

HERE = Path(__file__).parent
os.environ.setdefault("PIPELINE_RESULTS_PATH", str(HERE / "results.lanez_manual.jsonl"))

import db            # noqa: E402
import pipeline_v2   # noqa: E402

codes = [c.strip() for c in io.open(sys.argv[1], encoding="utf-8") if c.strip()]
force = "--force" in sys.argv
redo = "--redo" in sys.argv
done = set() if redo else db.done_codes_v2()
con = db.connect()
for c in codes:
    if (HERE / "PAUSE").exists() and not force:
        print("PAUSE sentinel present — stopping (use --force for a supervised run)",
              flush=True)
        break
    if c in done:
        print("skip (already v2-done):", c, flush=True)
        continue
    r = con.execute("SELECT task_json FROM tasks WHERE code=?", (c,)).fetchone()
    if not r:
        print("no task for", c, flush=True)
        continue
    try:
        pipeline_v2.process(json.loads(r[0]), 0)
    except Exception as e:
        print("ERR", c, str(e)[:80], flush=True)
con.close()
print("BATCH DONE", sys.argv[1], flush=True)
