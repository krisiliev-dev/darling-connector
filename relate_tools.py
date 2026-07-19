# -*- coding: utf-8 -*-
"""Catalogue-number relatedness — a deterministic smart-enrichment step.

Supplier catalogue numbers run in sequence within a product family (e.g. '10-002',
'10-003', '10-004' are a set of variants). So a product whose catalogue number shares
the same prefix and sits ±1 from another product is almost certainly related. This
module keeps a shared append-only index of every processed product's catalogue number
(concurrency-safe across the 6 lanes) and finds those neighbours to populate Свързани.

build_catalog.py already does a symmetric A<->B closure, so a link found from either
side propagates to both.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
IDX = HERE / "catnum_index.jsonl"


def _parse(cat):
    """'10-002' -> ('10-', 2). Returns (prefix, number) or None if no trailing number."""
    m = re.match(r"^(.*?)(\d+)\s*$", str(cat or "").strip())
    if not m:
        return None
    try:
        return (m.group(1), int(m.group(2)))
    except Exception:
        return None


def register(code, cat):
    """Append this product's catalogue number to the shared index."""
    if not cat or not str(cat).strip():
        return
    with open(IDX, "a", encoding="utf-8") as f:
        f.write(json.dumps({"code": str(code), "cat": str(cat)}, ensure_ascii=False) + "\n")


def load_index():
    """{(prefix, number): [codes]} reconstructed from the append-only log."""
    idx = {}
    if IDX.exists():
        for line in IDX.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.strip():
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            p = _parse(o.get("cat"))
            if p:
                idx.setdefault(p, []).append(str(o.get("code")))
    return idx


def find_related(code, cat, idx=None):
    """Codes sharing this catalogue number's prefix with number n-1, n or n+1
    (excluding self). Sequential catalogue numbers = variants of the same family."""
    p = _parse(cat)
    if not p:
        return []
    idx = load_index() if idx is None else idx
    prefix, num = p
    out = []
    for d in (-1, 0, 1):
        for c in idx.get((prefix, num + d), []):
            if str(c) != str(code) and c not in out:
                out.append(c)
    return out
