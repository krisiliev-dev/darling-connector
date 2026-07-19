# -*- coding: utf-8 -*-
"""Re-flag existing v2 records with the CORRECTED needs_human logic (owner 2026-07-19).

The v2 run flagged 99% for review because pipeline_v2 tested `if qf.needs_human(rec):`
on a (bool, flags) TUPLE — always truthy. This pass recomputes needs_human deterministically
from each record's stored notes + the correctly-unpacked quality_flags, with NO LLM calls,
and writes corrected versions. Also relaxes the `n_other>=3` attribute trigger (owner: off-
list/„друго" attribute values are usually fine — flag only genuinely risky records).

  python reflag_v2.py            # dry-run: old vs new review rate + driver breakdown
  python reflag_v2.py --apply    # write corrected needs_human as new versions
"""
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent


def _recompute(rec):
    """Corrected needs_human + the list of ACTUAL drivers, from stored notes/fields."""
    import quality_flags as qf
    meta = rec.get("meta") or {}
    notes = [str(n) for n in (meta.get("notes") or [])]
    conf = next((n.split(":", 1)[1] for n in notes if n.startswith("leaf_conf:")),
                str(rec.get("confidence") or ""))
    n_other = sum(1 for n in notes
                  if n.startswith("attr_other:") or n.startswith("attr_offlist:"))
    drivers = []
    if conf in ("ниска", "low"):
        drivers.append("low_leaf_conf")
    if "leaf_disagree_unresolved" in notes:
        drivers.append("leaf_disagree")
    if "vision_mismatch" in notes:
        drivers.append("vision_mismatch")
    if any(n.startswith("russian_survivors") for n in notes):
        drivers.append("russian")
    # texts_missing only matters if the field is ACTUALLY empty. When the v2 text step
    # failed (mid-batch throttling) the product kept its usable v1 description — that is
    # NOT a human-review issue, just a candidate for a cheap v2/SEO text upgrade later.
    f = rec.get("fields") or {}
    if any(n.startswith("texts_missing") for n in notes):
        if not str(f.get("Описание") or "").strip() or \
                not str(f.get("Мета описание") or "").strip():
            drivers.append("texts_actually_empty")
    if "weak_match" in notes:
        drivers.append("weak_match")
    if "claims_flagged" in notes:
        drivers.append("claims")
    if "leaf_branch_mismatch" in notes and conf not in ("висока", "high"):
        drivers.append("leaf_branch_mismatch")
    # relaxed: off-list attrs alone no longer flag; only an extreme count is suspicious
    if n_other >= 6:
        drivers.append("attrs_mostly_offlist")
    # quality_flags — CORRECTLY unpacked this time
    try:
        need, fl = qf.needs_human(rec)
        if need:
            drivers.append("qflag:" + ",".join(sorted({c for c, _s, _d in fl})))
    except Exception:
        pass
    return bool(drivers), drivers


def run(apply=False):
    import db
    prio = {ln.strip() for ln in (HERE / "V2_PRIORITY.txt").read_text(
        encoding="utf-8").splitlines() if ln.strip()}
    con = db.connect()
    rows = con.execute("SELECT code, record_json FROM products "
                       "WHERE record_json IS NOT NULL").fetchall()
    con.close()
    recs = {}
    for code, rj in rows:
        code = str(code)
        if code not in prio:
            continue
        rec = json.loads(rj)
        if "v2" in [str(n) for n in ((rec.get("meta") or {}).get("notes") or [])]:
            recs[code] = rec

    old_nh = sum(1 for r in recs.values() if r.get("needs_human"))
    new_nh = 0
    driver_counts = Counter()
    changed = []
    for code, rec in recs.items():
        need, drivers = _recompute(rec)
        if need:
            new_nh += 1
            for d in drivers:
                driver_counts[d.split(":")[0]] += 1
        if need != bool(rec.get("needs_human")):
            changed.append((code, need, drivers))

    n = len(recs)
    print(f"{n} v2 priority records")
    print(f"OLD needs_human: {old_nh} ({round(100*old_nh/n)}%)")
    print(f"NEW needs_human: {new_nh} ({round(100*new_nh/n)}%)  -> "
          f"{n - new_nh} now CLEAN / launch-ready")
    print(f"changed verdict: {len(changed)}")
    print("remaining review drivers:")
    for d, c in driver_counts.most_common():
        print(f"  {d}: {c}")

    if not apply:
        print("\n(dry-run — rerun with --apply to write corrected records)")
        return
    con = db.connect()
    written = 0
    with open(HERE / "results.lanez_reflag.jsonl", "a", encoding="utf-8") as fh:
        for code, rec in recs.items():
            need, drivers = _recompute(rec)
            if need == bool(rec.get("needs_human")):
                continue
            nd = dict(rec)
            nd["needs_human"] = need
            nd["ts"] = datetime.now().isoformat(timespec="seconds")
            meta = dict(nd.get("meta") or {})
            notes = [n for n in (meta.get("notes") or [])
                     if not str(n).startswith("quality_flags_forced")]
            notes.append("reflagged_v2")
            meta["notes"] = notes
            meta["reflag_drivers"] = drivers
            nd["meta"] = meta
            fh.write(json.dumps(nd, ensure_ascii=False) + "\n")
            db.record_version(nd)
            written += 1
    con.close()
    print(f"applied: {written} records re-flagged")


if __name__ == "__main__":
    run(apply="--apply" in sys.argv)
