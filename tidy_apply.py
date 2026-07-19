# -*- coding: utf-8 -*-
"""Apply the tested deterministic tidies to ALREADY-finished products.

SAFE & REVERSIBLE by construction: it writes ONE new file, results.lanez_tidy.jsonl,
that no lane ever writes to (no write race with the live pipeline). Each corrected
record is a copy of the product's canonical record with tidied fields and ts = original
+ 1s, so it wins the 'last-wins' de-dup in BOTH consumers (review_server by ts,
build_catalog by file order — the 'z_tidy' name sorts last). To REVERT everything:
just delete results.lanez_tidy.jsonl.

Overwrites the tidy file fresh each run (idempotent — never accumulates duplicates).
Does NOT touch empiric columns. Name-reorder is intentionally excluded (test-rejected).
"""
import json, glob, io
from datetime import datetime, timedelta
from pathlib import Path
import field_tidy as ft
import related_linker as rl

HERE = Path(__file__).parent
OUT = HERE / "results.lanez_tidy.jsonl"


def load_canonical():
    """Latest-per-code agentic record, EXCLUDING the tidy file (so re-runs are clean)."""
    recs = []
    for fp in glob.glob(str(HERE / "results.lane*.jsonl")):
        if Path(fp).name == OUT.name:
            continue
        for line in open(fp, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if "agentic" in ((d.get("meta") or {}).get("notes") or []):
                recs.append(d)
    by_code = {}
    for r in sorted(recs, key=lambda r: r.get("ts") or ""):
        by_code[str(r.get("code"))] = r
    return by_code


def bump_ts(ts):
    try:
        return (datetime.fromisoformat(ts) + timedelta(seconds=1)).isoformat(timespec="seconds")
    except Exception:
        return datetime.now().isoformat(timespec="seconds")


def main():
    canon = load_canonical()
    rel_idx = rl.related_index(list(canon.values()), manifest=rl.load_manifest())
    changed = 0
    counts = {}
    buf = io.StringIO()
    for code, rec in canon.items():
        f = rec.get("fields") or {}
        newf, changes = ft.tidy(f, do_reorder=False)
        variants = rel_idx.get(str(code), [])
        if variants:
            merged = rl.union_related(f.get("Свързани"), variants)
            if merged != f.get("Свързани"):
                newf["Свързани"] = merged
                changes.append("related")
        if not changes:
            continue
        changed += 1
        for c in changes:
            k = c.split(":")[0]
            counts[k] = counts.get(k, 0) + 1
        out = dict(rec)
        out["fields"] = newf
        out["ts"] = bump_ts(rec.get("ts") or "")
        meta = dict(rec.get("meta") or {})
        notes = list(meta.get("notes") or [])
        notes.append("field_tidy_applied:" + ",".join(dict.fromkeys(k.split(":")[0] for k in changes)))
        meta["notes"] = notes
        out["meta"] = meta
        buf.write(json.dumps(out, ensure_ascii=False) + "\n")
        try:
            import db as _db
            _db.record_version(out)
        except Exception:
            pass
    OUT.write_text(buf.getvalue(), encoding="utf-8")
    print(f"tidied {changed}/{len(canon)} finished products -> {OUT.name}")
    print("by change type:", dict(sorted(counts.items(), key=lambda x: -x[1])))
    print("REVERT with: rm results.lanez_tidy.jsonl")


if __name__ == "__main__":
    main()
