# -*- coding: utf-8 -*-
"""Boot restarter — registered as Scheduled Task 'Darling_Pipeline' (at logon, 2-min
delay). Idempotently brings the pipeline back after a reboot: each service starts ONLY
if not already running. Lanes themselves are Hermes cron jobs (task 'Hermes_Gateway');
this covers everything the gateway doesn't."""
import subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).parent
PY = sys.executable
LOG = HERE / "pipeline_boot.log"


def log(msg):
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(f"[{time.strftime('%Y-%m-%dT%H:%M:%S')}] {msg}\n")


def running(marker):
    out = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process -Filter \"name='python.exe'\" | "
         "ForEach-Object { $_.CommandLine }"],
        capture_output=True, text=True).stdout or ""
    return marker in out


def start(args, marker, env=None, priority=None, cwd=None):
    if running(marker):
        log(f"skip (already running): {marker}")
        return
    import os
    e = dict(os.environ); e["PYTHONIOENCODING"] = "utf-8"
    if env:
        e.update(env)
    flags = subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP
    import re as _re
    safe = _re.sub(r"[^\w-]+", "_", marker.split(".")[0]).strip("_") or "svc"
    p = subprocess.Popen([PY] + args, cwd=str(cwd or HERE), env=e, creationflags=flags,
                         stdout=open(HERE / f"boot_{safe}.log", "a"),
                         stderr=subprocess.STDOUT)
    if priority:
        subprocess.run(["powershell", "-NoProfile", "-Command",
                        f"(Get-Process -Id {p.pid}).PriorityClass='{priority}'"],
                       capture_output=True)
    log(f"started {marker} pid={p.pid}")


def _safe_start(*a, **kw):
    try:
        start(*a, **kw)
    except Exception as e:
        log(f"start FAILED for {a[1]}: {e}")


def main():
    log("=== boot restarter run ===")
    _safe_start(["review_server.py", "8733"], "review_server.py")
    for i in range(2):
        _safe_start(["review_all.py", "400", f"--shard={i}/2"], f"--shard={i}/2",
                    env={"DASHSCOPE_OFF": "1", "REVIEW_FLEET": "1"})
    _safe_start(["process_images.py", "--reprocess"], "process_images.py",
                priority="BelowNormal", cwd=HERE.parent / "image-pipeline")
    ac = Path(r"C:\Users\lora_\Downloads\auto_check.py")
    if ac.exists():
        _safe_start([str(ac)], "auto_check.py")
    log("done")


if __name__ == "__main__":
    main()
