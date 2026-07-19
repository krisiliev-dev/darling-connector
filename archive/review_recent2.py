# -*- coding: utf-8 -*-
"""Review a sample of the most-recent (new-Alibaba-key) products and summarize."""
import json, glob, io, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import review_agent as ra

recent = []
for f in glob.glob("results.lane*.jsonl"):
    for line in open(f, encoding="utf-8", errors="replace"):
        if not line.strip():
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        notes = (d.get("meta") or {}).get("notes") or []
        if (d.get("ts") or "") > "2026-07-15T12:15:00" and "agentic" in notes:
            recent.append((d["ts"], d["code"]))
recent.sort()
codes = [c for _, c in recent]
picks = codes[:: max(1, len(codes) // 8)][:8]
print("reviewing %d of %d new-key products..." % (len(picks), len(codes)), flush=True)

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

o = io.open("review_recent_summary.txt", "w", encoding="utf-8")
ready = sum(1 for r in results if (r.get("verdict") or {}).get("готов_за_сайта") is True)
o.write("REVIEWED %d new-key products | ready-for-site: %d/%d\n\n" % (len(results), ready, len(results)))
for r in results:
    v = r.get("verdict") or {}
    code = r.get("code")
    if r.get("error"):
        o.write("  %s: ERROR %s\n" % (code, r["error"]))
        continue
    tag = "OK" if v.get("готов_за_сайта") else "issues"
    o.write("  %s [%s]: %s\n" % (code, tag, str(v.get("оценка", ""))[:120]))
    for p in (v.get("проблеми") or [])[:4]:
        o.write("      - [%s] %s: %s\n" % (p.get("тежест"), p.get("поле"), p.get("проблем")))
    for fx in (v.get("автопоправки") or {}):
        o.write("      auto-fix: %s\n" % fx)
o.write("\nSYSTEMIC RECOMMENDATIONS:\n")
for r in results:
    for s in ((r.get("verdict") or {}).get("системни_препоръки") or []):
        o.write("  - %s => %s\n" % (s.get("наблюдение"), s.get("препоръка")))
o.close()
print("done", flush=True)
