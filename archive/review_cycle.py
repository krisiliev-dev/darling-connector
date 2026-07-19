# -*- coding: utf-8 -*-
"""Per-check reviewer: sample the MOST-RECENT finished products, run the QA reviewer
on them (auto-applies safe fixes, logs proposals + schema adjustments), and write a
concise summary. Launched once per supervision cycle."""
import json, glob, io, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import review_agent as ra

N = int(sys.argv[1]) if len(sys.argv) > 1 else 8

recs = []
for f in glob.glob("results.lane*.jsonl"):
    for line in open(f, encoding="utf-8", errors="replace"):
        if not line.strip():
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        notes = (d.get("meta") or {}).get("notes") or []
        if d.get("code") and "agentic" in notes and not (d.get("review") or {}).get("verdict"):
            recs.append((d.get("ts") or "", d["code"]))
recs.sort()
# de-dup keeping latest, then take the most-recent ~40 and spread N across them
seen, latest = set(), []
for ts, c in reversed(recs):
    if c in seen:
        continue
    seen.add(c); latest.append(c)
    if len(latest) >= 40:
        break
picks = latest[:: max(1, len(latest) // N)][:N]
print("reviewing %d of the most-recent %d products..." % (len(picks), len(latest)), flush=True)

ra.review_one._cache.update(records=ra.load_records(), sources=ra.load_sources(),
                            manifest=ra.load_manifest())
results = []
for i, c in enumerate(picks):
    print("[%d/%d] %s" % (i + 1, len(picks), c), flush=True)
    try:
        results.append(ra.review_one(c))
    except Exception as e:
        results.append({"code": c, "error": str(e)[:100]})
ra._write_report(results)
ra.apply_fixes(results)

o = io.open("review_cycle_summary.txt", "w", encoding="utf-8")
ready = sum(1 for r in results if (r.get("verdict") or {}).get("готов_за_сайта") is True)
o.write("REVIEWED %d recent products | ready-for-site: %d/%d\n\n" % (len(results), ready, len(results)))
kinds = {}
for r in results:
    v = r.get("verdict") or {}
    code = r.get("code")
    if r.get("error"):
        o.write("  %s: ERROR %s\n" % (code, r["error"])); continue
    tag = "OK" if v.get("готов_за_сайта") else "issues"
    o.write("  %s [%s]: %s\n" % (code, tag, str(v.get("оценка", ""))[:110]))
    for p in (v.get("проблеми") or [])[:4]:
        k = str(p.get("тип") or p.get("поле") or "?"); kinds[k] = kinds.get(k, 0) + 1
        o.write("      - [%s] %s: %s\n" % (p.get("тежест"), p.get("поле"), p.get("проблем")))
    for fx in (v.get("автопоправки") or {}):
        o.write("      auto-fix: %s\n" % fx)
o.write("\nMOST-COMMON ISSUE TYPES: %s\n" % (dict(sorted(kinds.items(), key=lambda x: -x[1]))))
o.write("\nSYSTEMIC RECOMMENDATIONS:\n")
for r in results:
    for s in ((r.get("verdict") or {}).get("системни_препоръки") or []):
        o.write("  - %s => %s\n" % (s.get("наблюдение"), s.get("препоръка")))
o.close()
print("done", flush=True)
