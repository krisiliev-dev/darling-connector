# -*- coding: utf-8 -*-
"""Per-product difficulty scoring + model routing.

The worker chain is tiered cheap→capable with failover. Most products are EASY (clean
source name, a recognised brand, dimensions present) and finish on a fast flash model.
A minority are HARD (sparse data, no known brand) — those tend to fumble on the tiniest
flash models, burning a failed attempt before failing over to something capable.

score(task) is a deterministic 0..1 signal from the source data (zero quota). chain_for()
uses it CONSERVATIVELY: easy products keep the fast-first chain unchanged (already
optimal); hard products get one capable model tried FIRST, then the normal chain — cutting
the wasted small-flash attempts. The aggressive policy (skip tiers, vary step budget) is
deliberately deferred until the new telemetry gives real per-model cost/quality data —
routing harder than this now would be guessing.
"""
import re

_DIM = re.compile(r"\d+\s*(?:см|мм|мл|л|кг|г|cm|mm|ml|l|бр|x|х|×|Ø)", re.IGNORECASE)
# A capable mid model to lead HARD products with (present in WORKER_CHAIN).
_HARD_LEAD_MODEL = "qwen3.6-27b"


def score(task):
    """Return (score 0=easy..1=hard, reasons list). Uses only source data."""
    prod = (task or {}).get("product") or {}
    gt = (task or {}).get("ground_truth") or {}
    name = str(prod.get("Наименование") or "")
    stoka = str(gt.get("Стока") or name)
    reasons = []
    hard = 0.0
    # sparse name → little to work with
    if len(name.strip()) < 12:
        hard += 0.4; reasons.append("кратко име")
    # no dimensions/units anywhere → less structured data
    if not _DIM.search(stoka):
        hard += 0.25; reasons.append("без размери")
    # no recognised brand token in the source
    try:
        import brand_tools
        toks = re.findall(r"[A-Za-zА-Яа-я]{2,}", stoka)
        if not any(brand_tools.lookup(t) for t in toks[:8]):
            hard += 0.25; reasons.append("няма известна марка")
    except Exception:
        pass
    # missing image → can't use vision to resolve visual attrs
    if not str(prod.get("Снимки") or "").strip():
        hard += 0.2; reasons.append("няма снимка")
    return min(hard, 1.0), reasons


def chain_for(task, base_chain, threshold=0.6):
    """Return a per-product ordering of `base_chain`. Easy products: unchanged
    (fast-first). Hard products: a capable model tried first, then the normal chain."""
    s, _ = score(task)
    if s < threshold:
        return list(base_chain)
    lead = [a for a in base_chain if a[a.index("-m") + 1] == _HARD_LEAD_MODEL]
    if not lead:
        return list(base_chain)
    rest = [a for a in base_chain if a[a.index("-m") + 1] != _HARD_LEAD_MODEL]
    return lead + rest
