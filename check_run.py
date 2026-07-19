# -*- coding: utf-8 -*-
"""Health + LEAF-QUALITY monitor for the running v2 priority batch (owner 2026-07-18:
leaf assignment is the most vulnerable failure point — watch it closely).

Prints a snapshot and appends one JSON line to check_run_status.jsonl each run. Schedule
every 30 min. Sections:
  FLEET     — priority progress, lanes alive, PAUSE/V2_MODE state, throughput
  PROVIDERS — recent failure types + which models are carrying the load
  LEAF      — for processed priority products: coverage (every product HAS a leaf?),
              confidence distribution, consensus vs disagreement, branch mismatches
  REVIEW    — needs_human split and the top reasons
"""
import glob
import json
import re
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent


def _priority():
    return {ln.strip() for ln in (HERE / "V2_PRIORITY.txt").read_text(
        encoding="utf-8").splitlines() if ln.strip()} if (HERE / "V2_PRIORITY.txt").exists() else set()


def _v2_records(codes):
    """Latest v2 record per code (from DB), for the given code set."""
    import db
    con = db.connect()
    out = {}
    try:
        rows = con.execute("SELECT code, record_json FROM products "
                           "WHERE record_json IS NOT NULL").fetchall()
    finally:
        con.close()
    for code, rj in rows:
        code = str(code)
        if code not in codes:
            continue
        try:
            rec = json.loads(rj)
        except Exception:
            continue
        notes = [str(n) for n in ((rec.get("meta") or {}).get("notes") or [])]
        if "v2" in notes:
            out[code] = rec
    return out


def _lanes_alive():
    import subprocess
    try:
        out = subprocess.run(["tasklist", "/fi", "imagename eq python.exe"],
                             capture_output=True, text=True, timeout=15).stdout
        return out.count("python.exe")
    except Exception:
        return -1


def run():
    prio = _priority()
    recs = _v2_records(prio)
    done = len(recs)
    total = len(prio)
    paused = (HERE / "PAUSE").exists()
    v2mode = (HERE / "V2_MODE").exists()
    lanes = _lanes_alive()

    # throughput: v2 records written in the last 30 min (by ts)
    now = datetime.now()
    recent = 0
    durs = []
    for rec in recs.values():
        m = rec.get("meta") or {}
        try:
            ts = datetime.fromisoformat(rec.get("ts"))
            if (now - ts).total_seconds() < 1800:
                recent += 1
                if m.get("duration_s"):
                    durs.append(m["duration_s"])
        except Exception:
            pass
    avg_dur = round(sum(durs) / len(durs), 1) if durs else None

    # LEAF quality over processed priority products
    leaf_present = leaf_missing = 0
    conf = Counter()
    consensus = Counter()
    branch_mismatch = 0
    needs_human = 0
    nh_reasons = Counter()
    brands = Counter()
    for rec in recs.values():
        m = rec.get("meta") or {}
        notes = [str(n) for n in (m.get("notes") or [])]
        if m.get("leaf_gid"):
            leaf_present += 1
        else:
            leaf_missing += 1
        lc = next((n.split(":", 1)[1] for n in notes if n.startswith("leaf_conf:")), "?")
        conf[lc] += 1
        if "leaf_consensus" in notes:
            consensus["agree"] += 1
        elif "leaf_tiebreak_vision" in " ".join(notes):
            consensus["vision_tiebreak"] += 1
        elif "leaf_disagree_unresolved" in notes:
            consensus["unresolved_disagree"] += 1
        elif any(n.startswith("leaf_disagree") for n in notes):
            consensus["disagree_other"] += 1
        else:
            consensus["single_vote"] += 1
        if "leaf_branch_mismatch" in notes:
            branch_mismatch += 1
        if rec.get("needs_human"):
            needs_human += 1
            for n in notes:
                if any(k in n for k in ("leaf", "claims", "vision_mismatch", "attr_",
                                        "weak", "russian", "quality_flags")):
                    nh_reasons[n] += 1
        b = str((rec.get("fields") or {}).get("Бранд") or "").strip()
        if b:
            brands[b] += 1

    # provider failures in the last stretch
    fail_types = Counter()
    try:
        for ln in (HERE / "failures.jsonl").read_text(
                encoding="utf-8", errors="replace").splitlines()[-40:]:
            try:
                d = json.loads(ln)
                if d.get("pipeline") == "v2":
                    fail_types[str(d.get("error"))[:40]] += 1
            except Exception:
                pass
    except FileNotFoundError:
        pass

    hi = conf.get("висока", 0)
    hi_pct = round(100 * hi / done) if done else 0
    leaf_cov = round(100 * leaf_present / done) if done else 0

    print(f"===== v2 PRIORITY BATCH — {now.strftime('%H:%M:%S')} =====")
    print(f"FLEET   : {done}/{total} done ({round(100*done/total) if total else 0}%) | "
          f"+{recent} in last 30min | avg {avg_dur}s | lanes(py)={lanes} | "
          f"{'PAUSED' if paused else 'running'} | V2_MODE={'on' if v2mode else 'OFF'}")
    print(f"LEAF    : coverage {leaf_cov}% ({leaf_missing} missing) | "
          f"conf {dict(conf)} | high={hi_pct}%")
    print(f"          consensus {dict(consensus)} | branch_mismatch={branch_mismatch}")
    print(f"REVIEW  : needs_human {needs_human}/{done} "
          f"({round(100*needs_human/done) if done else 0}%) | "
          f"top reasons {dict(nh_reasons.most_common(5))}")
    print(f"PROVIDER: recent v2 failures {dict(fail_types.most_common(4)) or 'none'}")
    print(f"BRANDS  : {dict(brands.most_common(6))}")

    # concise flags
    flags = []
    if leaf_missing:
        flags.append(f"{leaf_missing} products with NO leaf")
    if conf.get("ниска", 0) > done * 0.15 and done > 20:
        flags.append(f"low-leaf-conf {conf.get('ниска',0)} (>15%)")
    if consensus.get("unresolved_disagree", 0) > done * 0.1 and done > 20:
        flags.append(f"unresolved leaf disagreements {consensus.get('unresolved_disagree',0)}")
    if not paused and recent == 0 and done < total:
        flags.append("STALLED: no progress in 30min and not done")
    if paused and done < total:
        flags.append("PAUSED before batch complete — check arrearage/breaker")
    print("FLAGS   : " + ("; ".join(flags) if flags else "none — healthy"))

    snap = {"ts": now.isoformat(timespec="seconds"), "done": done, "total": total,
            "recent_30min": recent, "avg_dur_s": avg_dur, "lanes_py": lanes,
            "paused": paused, "leaf_coverage_pct": leaf_cov, "leaf_missing": leaf_missing,
            "leaf_conf": dict(conf), "consensus": dict(consensus),
            "branch_mismatch": branch_mismatch, "needs_human": needs_human,
            "fail_types": dict(fail_types), "flags": flags}
    with (HERE / "check_run_status.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(snap, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    run()
