# -*- coding: utf-8 -*-
"""Shared, growing brand gazetteer + verification — the 'smart brand' pipeline.

A vision agent reads a brand off a photo. Before it ever touches the Бранд field:
  1. LOOKUP against the shared gazetteer (fuzzy) — brands the suppliers already
     listed (seeded) + brands verified by earlier agents. A hit gives the CANONICAL
     spelling for free, no network/LLM call.
  2. If unknown, VERIFY with a capable model (real brand? canonical spelling?
     confidence). Only a confident, real brand is accepted.
  3. ADD the accepted brand (+ the raw variant seen) to the gazetteer so every
     later agent reuses it — the shared knowledge grows and self-corrects spelling.

Storage is an append-only JSONL (concurrency-safe across the 6 lanes); load()
reconstructs the canonical map. Seed once from the supplier scrape brands.
"""
import difflib
import json
import re
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
GAZ = HERE / "brand_gazetteer.jsonl"


def _norm(s):
    return re.sub(r"[^0-9a-zа-я]", "", str(s or "").lower())


def load():
    """Reconstruct {canonical_name: {'name', 'variants':set-as-list, 'source'}}."""
    g = {}
    if GAZ.exists():
        for line in GAZ.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.strip():
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            name = o.get("name")
            if not name:
                continue
            e = g.setdefault(name, {"name": name, "variants": [], "source": o.get("source")})
            v = o.get("variant")
            if v and _norm(v) != _norm(name) and v not in e["variants"]:
                e["variants"].append(v)
    return g


def add(canonical, variant=None, source="vision", gaz=None):
    with open(GAZ, "a", encoding="utf-8") as f:
        f.write(json.dumps({"name": canonical, "variant": variant, "source": source,
                            "ts": datetime.now().isoformat(timespec="seconds")},
                           ensure_ascii=False) + "\n")
    if gaz is not None:  # keep an in-memory copy in sync
        e = gaz.setdefault(canonical, {"name": canonical, "variants": [], "source": source})
        if variant and _norm(variant) != _norm(canonical) and variant not in e["variants"]:
            e["variants"].append(variant)
    return canonical


def lookup(candidate, gaz=None, threshold=0.88):
    """Return the canonical brand for a candidate if the gazetteer knows it
    (exact-normalised or fuzzy match against names + variants), else None."""
    if not candidate:
        return None
    gaz = load() if gaz is None else gaz
    nc = _norm(candidate)
    if not nc:
        return None
    for entry in gaz.values():
        names = [entry["name"], *entry.get("variants", [])]
        if any(_norm(n) == nc for n in names):
            return entry["name"]
    best, best_r = None, 0.0
    for entry in gaz.values():
        for n in [entry["name"], *entry.get("variants", [])]:
            r = difflib.SequenceMatcher(None, nc, _norm(n)).ratio()
            if r > best_r:
                best_r, best = r, entry["name"]
    return best if best_r >= threshold else None


def verify_llm(candidate, generate_fn, context=""):
    """Ask a capable model whether `candidate` is a real brand and its canonical
    spelling. `generate_fn(prompt)->text`. Returns {'real':bool,'canonical':str|None,
    'confidence':'висока|средна|ниска'} or None."""
    prompt = (
        f"Оцени от знанията си дали '{candidate}' е РЕАЛНА търговска марка за домакински, "
        f"кухненски или битови продукти. {('Контекст: ' + context) if context else ''}\n"
        "Ако е реална, дай правилното канонично изписване (напр. правилни главни букви, "
        "диакритика). Ако е измислена/нечетлив текст/име на магазин, върни реална=false.\n"
        'Върни САМО JSON: {"реална": true/false, "канонично": "изписване или null", '
        '"увереност": "висока/средна/ниска"}'
    )
    try:
        out = generate_fn(prompt)
        m = re.search(r"\{.*\}", out, re.DOTALL)
        v = json.loads(m.group(0)) if m else None
        if not v:
            return None
        return {"real": bool(v.get("реална")),
                "canonical": (v.get("канонично") or None),
                "confidence": str(v.get("увереност") or "").lower()}
    except Exception:
        return None


def resolve(candidate, generate_fn, context="", gaz=None):
    """Full smart pipeline for a raw vision brand candidate. Returns
    (canonical_brand_or_None, note). Never returns a supplier/store name (caller
    filters those). Grows the gazetteer on a confident new verification."""
    if not candidate:
        return None, None
    # HARD supplier gate at the single choke point (Levena leak 2026-07-17: a watermark
    # OCR grew the gazetteer before any caller-side filter could reject it)
    try:
        from run_one import SUPPLIER_NAMES as _sup
    except Exception:
        _sup = ["levena", "левена", "mira-n", "mira n", "мира-н", "мира н", "egera",
                "егера", "vertex", "вертекс", "inhouse", "in house", "ин хаус",
                "city lights", "city-lights", "сити лайтс", "kalian", "калиан",
                "plamplast", "плампласт", "elbulgaria", "ел българия",
                "microinvest", "микроинвест"]
    if any(x in candidate.lower() for x in _sup):
        return None, f"brand_supplier_blocked:{candidate}"
    gaz = load() if gaz is None else gaz
    known = lookup(candidate, gaz)
    if known:
        return known, ("brand_known" if _norm(known) == _norm(candidate)
                       else f"brand_spelling_fixed:{candidate}->{known}")
    v = verify_llm(candidate, generate_fn, context)
    if v and v["real"] and v["confidence"] in ("висока", "средна") and v["canonical"]:
        canon = v["canonical"].strip()
        add(canon, variant=candidate, source="vision+llm", gaz=gaz)
        return canon, (f"brand_verified:{canon}" if _norm(canon) == _norm(candidate)
                       else f"brand_verified_fixed:{candidate}->{canon}")
    return None, f"brand_unverified:{candidate}"


def seed_from_scrape(tasks_path):
    """One-time: load every distinct supplier scrape brand as a verified base."""
    seen = {_norm(e["name"]) for e in load().values()}
    added = 0
    for line in open(tasks_path, encoding="utf-8", errors="replace"):
        if not line.strip():
            continue
        try:
            t = json.loads(line)
        except Exception:
            continue
        b = ((t.get("ground_truth") or {}).get("Бранд (скрейп)") or "").strip()
        if b and _norm(b) and _norm(b) not in seen:
            add(b, source="scrape")
            seen.add(_norm(b))
            added += 1
    return added


# ---------------------------------------------------------------------------------
# MULTI-SOURCE RESOLVER (owner 2026-07-18: brand extraction must be robust).
# Evidence from independent sources is CORROBORATED instead of trusted singly:
#   >=2 sources agree (canonicalized)  -> accept
#   1 source, gazetteer-known          -> accept (established brand)
#   1 source, unknown                  -> PENDING: queued for owner review, field empty
# Supplier names are hard-blocked at every entrance.

import re as _re
from pathlib import Path as _Path

_CANDQ = _Path(__file__).parent / "brand_candidates.jsonl"


def _suppliers():
    try:
        from run_one import SUPPLIER_NAMES
        return [s.lower() for s in SUPPLIER_NAMES]
    except Exception:
        return ["levena", "левена", "mira-n", "мира-н", "egera", "егера",
                "vertex", "вертекс", "inhouse", "kalian", "plamplast"]


def slot_candidate(stoka):
    """The brand slot in supplier till names: 'BR-ALKAN-Series-Name...' -> 'ALKAN'.
    Returns None unless the token survives the material/collection/supplier gates."""
    m = _re.match(r"\s*[A-Za-z]{1,4}-([A-Za-zА-Я][\w&\.]{1,18})-", str(stoka or ""))
    if not m:
        return None
    tok = m.group(1).strip()
    tl = tok.lower()
    if any(x in tl for x in _suppliers()):
        return None
    try:
        import catalogue_guard as _cg
        if tl in {w.lower() for w in _cg.MATERIAL_WORDS}:
            return None
        colls = set()
        if _cg.COLLECTION_FILE.exists():
            colls = {c.strip().lower() for c in
                     _cg.COLLECTION_FILE.read_text(encoding="utf-8").splitlines() if c.strip()}
        if tl in colls:
            return None
    except Exception:
        pass
    return tok


def gather(code, sources):
    """sources: [(source_name, raw_candidate)]. Returns (brand, notes, pending).
    pending = an uncorroborated unknown candidate (queued for the owner, not applied)."""
    notes = []
    sup = _suppliers()
    canon_votes = {}
    unknown = []
    gaz = load()
    for src, raw in sources:
        raw = str(raw or "").strip()
        if not raw or raw.lower() in ("null", "none", "-", "n/a", "—"):
            continue
        if any(x in raw.lower() for x in sup):
            notes.append(f"brand_supplier_blocked:{src}")
            continue
        known = lookup(raw, gaz)
        if known:
            canon_votes.setdefault(known, set()).add(src)
        else:
            unknown.append((src, raw))
    if canon_votes:
        best, srcs = max(canon_votes.items(), key=lambda kv: len(kv[1]))
        if len(srcs) >= 2:
            notes.append("brand_confirmed:" + "+".join(sorted(srcs)))
        else:
            notes.append("brand_known:" + next(iter(srcs)))
        return best, notes, None
    # no gazetteer hit: corroboration across raw unknowns?
    if len(unknown) >= 2:
        vals = {u[1].lower() for u in unknown}
        if len(vals) == 1:                              # two sources, same unknown string
            return None, notes + ["brand_unknown_agreed"], unknown[0][1]
    if unknown:
        return None, notes + [f"brand_pending:{unknown[0][0]}"], unknown[0][1]
    return None, notes, None


def queue_candidate(code, candidate, sources, stoka=""):
    import json as _json
    from datetime import datetime as _dt
    try:
        with _CANDQ.open("a", encoding="utf-8") as f:
            f.write(_json.dumps({"code": str(code), "candidate": candidate,
                                 "sources": sources, "stoka": str(stoka)[:80],
                                 "ts": _dt.now().isoformat(timespec="seconds")},
                                ensure_ascii=False) + chr(10))
    except Exception:
        pass
