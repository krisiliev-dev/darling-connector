# -*- coding: utf-8 -*-
"""JSONL <-> DB reconciliation — makes silent divergence between the authoritative DB and
the append-only JSONL safety net VISIBLE instead of accumulating.

Compares, per code: presence and newest ts. Classes:
  * missing_in_db  — JSONL has it, DB doesn't (a failed record_version write)
  * db_stale       — DB's canonical ts is OLDER than the JSONL's newest (missed upsert)
  * missing_in_jsonl — DB-only versions (should be impossible now that every writer
    appends JSONL first; nonzero => a writer bypasses the safety net)

  python reconcile.py            # report
  python reconcile.py --heal     # re-insert missing/stale rows into the DB from JSONL
Exit code 1 when divergence is found (cron-friendly). Called by monitor.py --reconcile.
"""
import json, glob, sys
from pathlib import Path

HERE = Path(__file__).parent


def jsonl_newest():
    """{code: (ts, record)} newest-per-code across the JSONL ground truth."""
    best = {}
    for fp in [str(HERE / "results.jsonl")] + glob.glob(str(HERE / "results.lane*.jsonl")):
        if not Path(fp).exists():
            continue
        for line in open(fp, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            c = str(d.get("code") or "")
            if not c:
                continue
            ts = d.get("ts") or ""
            if c not in best or ts >= best[c][0]:
                best[c] = (ts, d)
    return best


def main(heal=False):
    import db
    jl = jsonl_newest()
    con = db.connect()
    dbmap = dict(con.execute("SELECT code, ts FROM products").fetchall())
    con.close()

    missing_in_db = [c for c in jl if c not in dbmap]
    db_stale = [c for c, (ts, _) in jl.items() if c in dbmap and (dbmap[c] or "") < ts]
    missing_in_jsonl = [c for c in dbmap if c not in jl]

    print(f"JSONL codes: {len(jl)} | DB codes: {len(dbmap)}")
    print(f"missing_in_db: {len(missing_in_db)} {missing_in_db[:5]}")
    print(f"db_stale:      {len(db_stale)} {db_stale[:5]}")
    print(f"missing_in_jsonl (writer bypassing safety net!): {len(missing_in_jsonl)} {missing_in_jsonl[:5]}")

    diverged = len(missing_in_db) + len(db_stale) + len(missing_in_jsonl)
    if heal and (missing_in_db or db_stale):
        healed = 0
        for c in missing_in_db + db_stale:
            try:
                db.record_version(jl[c][1])
                healed += 1
            except Exception as e:
                print(f"  heal {c} failed: {str(e)[:60]}")
        print(f"healed {healed} records into the DB from JSONL")
        return 0
    return 1 if diverged else 0


if __name__ == "__main__":
    sys.exit(main(heal="--heal" in sys.argv))
