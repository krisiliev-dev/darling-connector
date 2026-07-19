# -*- coding: utf-8 -*-
"""Standalone pipeline supervision status -> prints to stdout (UTF-8).
Run with the venv python from the agent-pipeline dir. Safe to run anytime."""
import json, io, glob, os, time, collections, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)
import run_one
now = time.time()

recs = []
for f in (["results.jsonl"] if os.path.exists("results.jsonl") else []) + glob.glob("results.lane*.jsonl"):
    for line in open(f, encoding="utf-8", errors="replace"):
        if not line.strip():
            continue
        try:
            recs.append(json.loads(line))
        except Exception:
            pass
recs.sort(key=lambda d: d.get("ts") or "")
tot = sum(1 for _ in open(run_one.TASKS_PATH, encoding="utf-8") if _.strip())
n = len(recs)
nh = sum(1 for d in recs if d.get("needs_human"))
durs = [(d.get("meta") or {}).get("duration_s") for d in recs if isinstance((d.get("meta") or {}).get("duration_s"), (int, float))]
med = sorted(durs)[len(durs)//2] if durs else 0
pair = collections.Counter((d.get("meta") or {}).get("model_pair") for d in recs)

# throughput from last 60 min of records
cutoff = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(now - 3600))
last_hr = [d for d in recs if (d.get("ts") or "") > cutoff]
rate = len(last_hr)  # per hour
print(f"REPROCESSING: {n}/{tot} done, {tot-n} remaining")
print(f"  clean: {n-nh} ({100*(n-nh)/max(n,1):.0f}%)   for-review: {nh} ({100*nh/max(n,1):.0f}%)")
print(f"  median duration: {med:.0f}s   last-hour throughput: {rate} products")
if rate:
    print(f"  ETA at current rate: ~{(tot-n)/rate:.0f}h (~{(tot-n)/rate/24:.1f} days)")
print(f"  worker pair usage: {dict(pair)}  (0=primary; higher=failover)")

# quota / model health
qsig = collections.Counter()
for d in recs[-200:]:
    for note in (d.get("meta") or {}).get("notes") or []:
        s = str(note).lower()
        if any(k in s for k in ("quota", "insufficient", "exhaust", "429", "403", "balance", "rate limit")):
            qsig[str(note)[:70]] += 1
print(f"QUOTA/AUTH signals (last 200): {dict(qsig) or 'none'}")

# live probe each provider primary so we know what still has quota
print("PROVIDER PROBES:")
for name, args in [("groq-scout", ["-m", "meta-llama/llama-4-scout-17b-16e-instruct", "--provider", "groq"]),
                   ("dashscope-qwen-flash", ["-m", "qwen-flash", "--provider", "dashscope-intl"]),
                   ("nvidia-qwen3.5", ["-m", "qwen/qwen3.5-397b-a17b", "--provider", "nvidia"]),
                   ("cohere-command-a", ["-m", "command-a-03-2025", "--provider", "cohere"])]:
    try:
        t = time.time()
        run_one.run_direct("хей", args, max_tokens=10)
        print(f"  {name}: OK ({time.time()-t:.1f}s)")
    except Exception as e:
        print(f"  {name}: DOWN ({str(e)[:80]})")

# lane liveness
print("LANES:")
for f in sorted(glob.glob("results.lane*.jsonl")):
    print(f"  {os.path.basename(f)}: last write {(now-os.path.getmtime(f))/60:.0f} min ago")
print(f"  locks: {[os.path.basename(l) for l in glob.glob('.runner.lock*')] or 'none'}")

# language quality on recent
try:
    import bg_spell
    bg_spell._whitelist.cache_clear()
    ru = garb = 0
    for d in recs[-40:]:
        fl = d.get("fields", {})
        blob = " ".join(str(fl.get(k) or "") for k in ("Наименование", "Описание", "Атрибути"))
        ru += sum(c in "ыэёЫЭЁ" for c in blob)
        garb += len(bg_spell.unknown_words(blob, limit=8))
    print(f"LANGUAGE (last 40): russian-letters={ru}  garbled-words={garb}")
except Exception as e:
    print(f"LANGUAGE check failed: {e}")

# images
ipres = os.path.join(os.path.dirname(HERE), "image-pipeline", "process_results.jsonl")
if os.path.exists(ipres):
    ok = err = cut = 0
    for line in open(ipres, encoding="utf-8", errors="replace"):
        if not line.strip():
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        ok += d.get("status") == "ok"
        err += d.get("status") == "error"
        cut += any("cutout_ok" in a for a in (d.get("actions") or []))
    print(f"IMAGES: ok={ok} errors={err} transparent-cutouts={cut}")
