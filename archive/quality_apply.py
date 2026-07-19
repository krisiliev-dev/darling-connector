# -*- coding: utf-8 -*-
"""Apply the Tier-1 quality cleaners to already-finished products. Append-only +
reversible: writes results.lanez_qclean.jsonl (ts bumped) + DB dual-write. Also recomputes
the deterministic needs_human so the triage on existing records reflects real risk.
Delete the file + re-ingest to revert."""
import json
from datetime import datetime, timedelta
from pathlib import Path
import quality_clean as qc
import quality_flags as qflags

HERE = Path(__file__).parent
OUT = HERE / "results.lanez_qclean.jsonl"


def main():
    import db
    canon = db.canonical_records()
    changed = 0
    counts = {}
    buf = []
    for code, rec in canon.items():
        f = rec.get("fields") or {}
        nf, ch = qc.clean(f)
        need, flags = qflags.needs_human({"fields": nf})
        reflag = need != bool(rec.get("needs_human"))
        if not ch and not reflag:
            continue
        nd = dict(rec)
        nd["fields"] = nf
        nd["needs_human"] = need
        try:
            nd["ts"] = (datetime.fromisoformat(rec.get("ts") or "")
                        + timedelta(seconds=6)).isoformat(timespec="seconds")
        except Exception:
            nd["ts"] = datetime.now().isoformat(timespec="seconds")
        meta = dict(nd.get("meta") or {})
        meta["quality_flags"] = flags
        notes = list(meta.get("notes") or [])
        if ch:
            notes.append("quality_clean:" + ",".join(dict.fromkeys(ch)))
        meta["notes"] = notes
        nd["meta"] = meta
        buf.append(json.dumps(nd, ensure_ascii=False))
        try:
            db.record_version(nd)
        except Exception:
            pass
        changed += 1
        for c in ch:
            counts[c] = counts.get(c, 0) + 1
    OUT.write_text("\n".join(buf) + ("\n" if buf else ""), encoding="utf-8")
    print(f"cleaned/reflagged {changed}/{len(canon)} products -> {OUT.name}")
    print("by change:", dict(sorted(counts.items(), key=lambda x: -x[1])))
    print("REVERT: rm results.lanez_qclean.jsonl && python db.py --ingest")


if __name__ == "__main__":
    main()
