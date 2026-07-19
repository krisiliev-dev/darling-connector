# -*- coding: utf-8 -*-
"""Tiny disk-backed cache for repeated external lookups (web_search, supplier-page
fetch). Many products share a brand / supplier, so the same query recurs across the run.
Caching the raw lookup skips the network round-trip AND the LLM tokens spent re-reasoning
over a page we've already seen — a direct throughput + quota win.

Append-only JSONL, last-wins, loaded once per process. Cross-process sharing happens via
the file on the next process start (cron lanes are short-lived), which is exactly when a
new lane benefits from what earlier lanes discovered. A stale in-memory view only costs a
cache miss, never correctness.
"""
import json
import hashlib
from pathlib import Path

HERE = Path(__file__).parent
CACHE = HERE / "lookup_cache.jsonl"
_mem = None


def _load():
    global _mem
    if _mem is not None:
        return _mem
    _mem = {}
    if CACHE.exists():
        for line in open(CACHE, encoding="utf-8", errors="replace"):
            if line.strip():
                try:
                    o = json.loads(line)
                    _mem[o["k"]] = o["v"]
                except Exception:
                    pass
        # compact when the append-only file has grown well past its distinct content
        # (duplicates from last-wins appends) or is simply huge — it's re-parsed by every
        # lane process, so unbounded growth taxes every batch start.
        try:
            if CACHE.stat().st_size > 20_000_000:
                tmp = str(CACHE) + ".tmp"
                with open(tmp, "w", encoding="utf-8") as f:
                    for k, v in _mem.items():
                        f.write(json.dumps({"k": k, "v": v}, ensure_ascii=False) + "\n")
                import os
                os.replace(tmp, CACHE)
        except Exception:
            pass
    return _mem


def _key(ns, key):
    return ns + ":" + hashlib.md5(str(key).encode("utf-8")).hexdigest()[:16]


def get(ns, key):
    return _load().get(_key(ns, key))


def put(ns, key, value):
    k = _key(ns, key)
    _load()[k] = value
    try:
        with open(CACHE, "a", encoding="utf-8") as f:
            f.write(json.dumps({"k": k, "v": value}, ensure_ascii=False) + "\n")
    except Exception:
        pass


def stats():
    m = _load()
    ns = {}
    for k in m:
        p = k.split(":", 1)[0]
        ns[p] = ns.get(p, 0) + 1
    return {"entries": len(m), "by_namespace": ns}
