# -*- coding: utf-8 -*-
"""Deterministic attribute fill — ZERO quota. Fills the filter groups the reviewer keeps
flagging (Размер/Обем/Габарити) for products where the value is ALREADY sitting in the
name/source (e.g. name '...550 мл' but no 'Обем' attribute). No model call, no vision —
just moves data that's already there into the filterable attribute.

Visual gaps (Цвят/Материал) are NOT touched here — those need the deferred vision pass.
Append-only + reversible: writes results.lanez_attrfill.jsonl (ts bumped) and dual-writes
the DB. Delete the file + re-ingest to revert.
"""
import json
from datetime import datetime, timedelta
from pathlib import Path
import attr_reconcile as ar

HERE = Path(__file__).parent
OUT = HERE / "results.lanez_attrfill.jsonl"


def load_canonical():
    try:
        import db
        if db.is_ready():
            return db.canonical_records()
    except Exception:
        pass
    import glob
    recs = []
    for fp in glob.glob(str(HERE / "results.lane*.jsonl")):
        for line in open(fp, encoding="utf-8", errors="replace"):
            if line.strip():
                try:
                    recs.append(json.loads(line))
                except Exception:
                    pass
    by = {}
    for r in sorted(recs, key=lambda r: r.get("ts") or ""):
        by[str(r.get("code"))] = r
    return by


def main():
    import filter_schema_store as fss
    cats = fss.load()
    canon = load_canonical()
    filled = 0
    group_counts = {}
    buf = []
    for code, rec in canon.items():
        new_attrs, groups = ar.fill_deterministic(rec, cats)
        if not new_attrs or not groups:
            continue
        f = dict(rec.get("fields") or {})
        f["Атрибути"] = new_attrs
        nd = dict(rec)
        nd["fields"] = f
        try:
            nd["ts"] = (datetime.fromisoformat(rec.get("ts") or "")
                        + timedelta(seconds=4)).isoformat(timespec="seconds")
        except Exception:
            nd["ts"] = datetime.now().isoformat(timespec="seconds")
        meta = dict(nd.get("meta") or {})
        meta["notes"] = list(meta.get("notes") or []) + ["attr_fill_deterministic:" + ",".join(groups)]
        nd["meta"] = meta
        buf.append(json.dumps(nd, ensure_ascii=False))
        try:
            import db as _db
            _db.record_version(nd)
        except Exception:
            pass
        filled += 1
        for g in groups:
            group_counts[g] = group_counts.get(g, 0) + 1
    OUT.write_text("\n".join(buf) + ("\n" if buf else ""), encoding="utf-8")
    print(f"filled {filled} products with in-name attributes -> {OUT.name}")
    print("by group:", dict(sorted(group_counts.items(), key=lambda x: -x[1])))
    print("REVERT: rm results.lanez_attrfill.jsonl && python db.py --ingest")


if __name__ == "__main__":
    main()
