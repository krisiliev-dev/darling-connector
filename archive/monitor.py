# -*- coding: utf-8 -*-
"""Pipeline health monitor + alerting. Supervision was 100% manual ('Check processing');
if a lane died or quota exhausted between checks, nothing recorded it. This runs a
deterministic health check, PERSISTS any problem to alerts.jsonl (so it's never missed
between manual checks), prints a verdict, and exits non-zero on a CRITICAL condition (so a
cron wrapper can escalate).

  python monitor.py            # check + persist alerts, print verdict
Cron-friendly: schedule every ~15 min alongside the lanes.
"""
import json, glob, os, sys, time
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).parent
ALERTS = HERE / "alerts.jsonl"
STALL_MIN = 25          # all lanes silent this long = stalled
EXHAUST_WARN = 30       # distinct exhausted models


def _recent_completions(minutes=30):
    rows = []
    for f in glob.glob(str(HERE / "results.lane*.jsonl")):
        try:
            for line in open(f, encoding="utf-8", errors="replace"):
                if line.strip():
                    try:
                        rows.append(json.loads(line).get("ts") or "")
                    except Exception:
                        pass
        except Exception:
            pass
    if not rows:
        return 0, None
    newest = max(rows)
    try:
        cut = (datetime.fromisoformat(newest) - timedelta(minutes=minutes)).isoformat()
    except Exception:
        return len(rows), newest
    return sum(1 for t in rows if t >= cut), newest


def check():
    alerts = []
    # 1. stall: newest completion age (uses lane mtimes — robust to clock)
    lane_files = [Path(f) for f in glob.glob(str(HERE / "results.lane*.jsonl")) if "z_" not in f]
    if lane_files:
        age_min = (time.time() - max(f.stat().st_mtime for f in lane_files)) / 60
        if age_min > STALL_MIN:
            alerts.append(("critical", "stall", f"няма запис от {int(age_min)} мин — пайплайнът е спрял"))
    # 2. PAUSE sentinel (arrearage circuit breaker)
    if (HERE / "PAUSE").exists():
        alerts.append(("critical", "paused", "PAUSE сентинел е активен (възможна арририя/такса)"))
    # 3. arrearage / repeated failures in the last window
    if (HERE / "failures.jsonl").exists():
        cutt = (datetime.now() - timedelta(minutes=30)).isoformat()
        arr = 0
        for line in open(HERE / "failures.jsonl", encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                fe = json.loads(line)
            except Exception:
                continue
            if (fe.get("ts") or "") >= cutt and "rrearage" in str(fe.get("error", "")).lower():
                arr += 1
        if arr:
            alerts.append(("critical", "arrearage", f"{arr} арририя-грешки за 30 мин — плащане?"))
    # 4. quota exhaustion (warn)
    if (HERE / "exhausted_models.txt").exists():
        ex = len(set(l.strip() for l in open(HERE / "exhausted_models.txt", encoding="utf-8") if l.strip()))
        if ex >= EXHAUST_WARN:
            alerts.append(("warn", "quota", f"{ex} изчерпани модела — свободната квота намалява"))
    # 5. throughput sanity
    done30, newest = _recent_completions(30)
    if done30 == 0 and not alerts:
        alerts.append(("warn", "idle", "0 завършени за 30 мин"))
    return alerts, done30, newest


def main():
    alerts, done30, newest = check()
    # optional integrity pass: surface JSONL<->DB drift as a WARN alert
    if "--reconcile" in sys.argv:
        try:
            import reconcile as _rc
            if _rc.main(heal=False) != 0:
                alerts.append(("warn", "db_drift", "JSONL и БД се разминават — виж reconcile.py (--heal)"))
        except Exception as e:
            alerts.append(("warn", "reconcile_error", str(e)[:80]))
    stamp = datetime.now().isoformat(timespec="seconds")
    crit = [a for a in alerts if a[0] == "critical"]
    if alerts:
        with open(ALERTS, "a", encoding="utf-8") as f:
            for level, kind, msg in alerts:
                f.write(json.dumps({"ts": stamp, "level": level, "kind": kind, "msg": msg},
                                   ensure_ascii=False) + "\n")
    try:
        import run_one as _ro
        _bo = _ro.billed_overflow_tokens()
        _cap = _ro._billed_cap_millions()
        if _bo or _cap:
            print(f"DASHSCOPE BILLED: ~{_bo/1e6:.1f}M new tokens (~EUR {_bo/1e6*0.42:.0f}) of {_cap:.0f}M cap")
    except Exception:
        pass
    if not alerts:
        print(f"OK — {done30} done/30min, newest {newest}")
    else:
        for level, kind, msg in alerts:
            print(f"{'‼️ CRITICAL' if level == 'critical' else '⚠️ WARN'} [{kind}] {msg}")
    return 2 if crit else 0


if __name__ == "__main__":
    sys.exit(main())
