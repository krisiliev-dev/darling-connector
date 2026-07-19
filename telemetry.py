# -*- coding: utf-8 -*-
"""Per-product model/token telemetry — you can't optimise a quota you don't measure.

Every OpenAI-compatible response carries a `usage` block (prompt/completion tokens). We
were throwing it away; here we accumulate it per product so each record can carry which
models did the work and how many tokens it cost. That unlocks model routing, quota
forecasting and cost caps.

Each lane is a SEPARATE process handling one product at a time (run_batch → process_next
sequentially), so a plain module-level buffer is safe — no locking needed. reset() at the
start of a product, record() after each model call, summary() when writing the record.
"""
_buf = []


def reset():
    _buf.clear()


def record(model, provider, resp):
    """Append the usage from one chat.completions response. Best-effort: never raises."""
    try:
        u = getattr(resp, "usage", None)
        pt = int(getattr(u, "prompt_tokens", 0) or 0) if u else 0
        ct = int(getattr(u, "completion_tokens", 0) or 0) if u else 0
        _buf.append({"model": str(model), "provider": str(provider), "pt": pt, "ct": ct})
    except Exception:
        pass


def summary():
    """Aggregate the current product's usage: totals, per-model breakdown, primary model."""
    by = {}
    tp = tc = 0
    for e in _buf:
        m = e["model"]
        d = by.setdefault(m, {"calls": 0, "pt": 0, "ct": 0, "provider": e["provider"]})
        d["calls"] += 1
        d["pt"] += e["pt"]
        d["ct"] += e["ct"]
        tp += e["pt"]
        tc += e["ct"]
    primary = max(by, key=lambda m: by[m]["pt"] + by[m]["ct"]) if by else None
    return {
        "total_tokens": tp + tc,
        "prompt_tokens": tp,
        "completion_tokens": tc,
        "calls": len(_buf),
        "primary_model": primary,
        "by_model": by,
    }
