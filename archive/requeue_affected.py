# -*- coding: utf-8 -*-
"""Re-queue the catalogue-residual records (reprocess_affected.txt): delete their
result rows so next_task no longer sees them as done and the running cron lanes
reprocess them with the improved agent instruction. Safe vs live appends: read ->
write temp -> os.replace with retry (lanes hold each file only per-record-write)."""
import glob, os, json, time, sys, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

codes = {c.strip() for c in open("reprocess_affected.txt", encoding="utf-8") if c.strip()}
apply = "--apply" in sys.argv
removed_total = 0
for path in sorted(glob.glob("results.lane*.jsonl")):
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    kept, removed = [], 0
    for line in lines:
        if not line.strip():
            continue
        try:
            d = json.loads(line)
        except Exception:
            kept.append(line); continue
        # remove ONLY affected agentic rows; keep human-reviewed ones untouched
        if (d.get("code") in codes
                and "agentic" in ((d.get("meta") or {}).get("notes") or [])
                and not (d.get("review") or {}).get("verdict")):
            removed += 1
            continue
        kept.append(line)
    removed_total += removed
    if apply and removed:
        if not os.path.exists(path + ".reqbak"):
            shutil.copyfile(path, path + ".reqbak")
        tmp = path + ".tmp"
        open(tmp, "w", encoding="utf-8").write("\n".join(kept) + "\n")
        for _ in range(6):
            try:
                os.replace(tmp, path); break
            except PermissionError:
                time.sleep(0.4)
        else:
            os.remove(tmp); print(f"  WARN could not replace {os.path.basename(path)}")
    print(f"{os.path.basename(path)}: remove {removed}")

print(f"total re-queued: {removed_total}  ({'APPLIED' if apply else 'DRY RUN — pass --apply'})")
