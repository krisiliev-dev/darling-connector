# -*- coding: utf-8 -*-
import json, glob, io, sys, collections
sys.path.insert(0, '.')
import review_agent as ra
# recent new-key codes (processed since 12:15 today)
recent=[]
for f in glob.glob('results.lane*.jsonl'):
    for line in open(f,encoding='utf-8',errors='replace'):
        if not line.strip(): continue
        try: d=json.loads(line)
        except: continue
        if (d.get('ts') or '')>'2026-07-15T12:15:00' and 'agentic' in ((d.get('meta') or {}).get('notes') or []):
            recent.append((d['ts'], d['code']))
recent.sort()
codes=[c for _,c in recent]
picks=codes[::max(1,len(codes)//8)][:8]
print(f'reviewing {len(picks)} of {len(codes)} new-key products...', flush=True)
ra.review_one._cache.update(records=ra.load_records(), sources=ra.load_sources(), manifest=ra.load_manifest())
results=[]
for i,c in enumerate(picks):
    print(f'[{i+1}/{len(picks)}] {c}', flush=True)
    try: results.append(ra.review_one(c))
    except Exception as e: results.append({'code':c,'error':str(e)[:100]})
ra._write_report(results)
ra.apply_fixes(results)
# concise summary
o=io.open('review_recent_summary.txt','w',encoding='utf-8')
ready=sum(1 for r in results if (r.get('verdict') or {}).get('готов_за_сайта') is True)
o.write(f'REVIEWED {len(results)} new-key products | ready-for-site: {ready}/{len(results)}\n\n')
for r in results:
    v=r.get('verdict') or {}
    if r.get('error'): o.write(f'  {r[\"code\"]}: ERROR {r[\"error\"]}\n'); continue
    o.write(f'  {r[\"code\"]} [{ \"OK\" if v.get(\"готов_за_сайта\") else \"issues\"}]: {v.get(\"оценка\",\"\")[:110]}\n')
    for p in (v.get('проблеми') or [])[:4]:
        o.write(f'      - [{p.get(\"тежест\")}] {p.get(\"поле\")}: {p.get(\"проблем\")}\n')
o.write('\nSYSTEMIC:\n')
for r in results:
    for s in ((r.get('verdict') or {}).get('системни_препоръки') or []):
        o.write(f'  - {s.get(\"наблюдение\")} => {s.get(\"препоръка\")}\n')
o.close()
print('done')
