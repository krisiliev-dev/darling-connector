# -*- coding: utf-8 -*-
"""Deterministic quality risk detectors — the honest replacement for the model's
self-reported confidence (which was 'high' on 99.7% of records and flagged 0.5%, i.e.
carried no triage signal). These flags drive needs_human so human review can actually be
TARGETED at the risky records, and feed the cleanup passes.

Each detector is a pure function over a record's fields. flags() returns a list of
(code, severity, detail). needs_human() derives a boolean: any HIGH flag, or >=2 MEDIUM.
"""
import re

# --- fabrication of verifiable authority (legal/reputational risk) ------------
# We FLAG (never auto-delete) — a human/reviewer confirms. Generous by design.
_FAB = [
    (re.compile(r"\bWIPO\b|\bEUIPO\b|\bUSPTO\b", re.I), "trademark-office"),
    (re.compile(r"\bAISI\b|\bSUS\s*3\d\d\b", re.I), "steel-grade-code"),
    (re.compile(r"\b1[8347]/[0-9]\b"), "steel-alloy-ratio"),          # 18/10, 18/0, 13/0, 14/1
    (re.compile(r"регистриран[а-я]*\s+(търговск[а-я]+\s+)?марк", re.I), "registered-trademark"),
    (re.compile(r"международно\s+регистриран", re.I), "intl-registration"),
    (re.compile(r"сертификат", re.I), "certificate-claim"),
    (re.compile(r"№\s*\d{6,}"), "registration-number"),
]

# --- model reasoning leaking into customer copy (safe to strip) ---------------
# Simple presence patterns (no sentence-spanning quantifiers → no catastrophic
# backtracking). Sentence removal is done by splitting, not regex, in quality_clean.
LEAK_PHRASES = [
    re.compile(r"визуалн\w*\s+оценка", re.I),
    re.compile(r"снимка\w*\s+(?:показва|потвърж\w*|се вижда|личи)", re.I),
    re.compile(r"(?:от|според)\s+снимка\w*\s+(?:се\s+)?(?:вижда|личи)", re.I),
    re.compile(r"потвърден\w*\s+серия", re.I),
    re.compile(r"потвърден\w*\s+от\s+\w*\s*сертификат", re.I),
]
_LEAK = LEAK_PHRASES

_BRAND_IN_ATTR = re.compile(r"(?:Бранд|Марка)\s*:\s*([^;]+)", re.I)
_CATCODE_IN_NAME = re.compile(r"\(\s*\d{3,}\s*\)\s*$|\b[A-Z]{1,4}-?\d{3,}\b")
_LATIN_LOWER = re.compile(r"^[a-z][a-z\s]*$")           # romanized junk synonym (all lower Latin)
_HAS_RU = re.compile(r"[ыэёЫЭЁ]")


def _txt(f, *keys):
    return " ".join(str(f.get(k) or "") for k in keys)


def flags(record):
    """List of (code, severity, detail). severity in {'high','medium','low'}."""
    f = record.get("fields") or {}
    out = []
    name = str(f.get("Наименование") or "")
    desc = str(f.get("Описание") or "")
    attrs = str(f.get("Атрибути") or "")
    syn = str(f.get("Синоними") or "")
    brand = str(f.get("Бранд") or "").strip()

    blob = _txt(f, "Наименование", "Описание", "Мета описание", "Атрибути")
    for rx, tag in _FAB:
        m = rx.search(blob)
        if m:
            out.append(("fabrication", "high", f"{tag}:{m.group(0)[:24]}"))
            break                                       # one is enough to flag

    if _HAS_RU.search(blob):
        out.append(("russian", "high", "ру-букви"))

    # brand empty but clearly present in attributes — and it's a PLAUSIBLE brand, not a
    # catalogue prefix (BR/CN…) or a material.
    if not brand:
        m = _BRAND_IN_ATTR.search(attrs)
        cand = (m.group(1).strip() if m else "")
        if cand and len(cand) >= 3 and cand.lower() not in ("н/а", "няма", "-") \
                and not _is_prefix_or_material(cand):
            out.append(("brand_recoverable", "medium", f"в атрибути: {cand[:24]}"))

    if attrs.strip().startswith("{"):
        out.append(("json_attrs", "medium", "Атрибути като JSON блок"))

    if _CATCODE_IN_NAME.search(name):
        out.append(("catcode_in_name", "medium", "код в наименованието"))

    for rx in _LEAK:
        if rx.search(desc):
            out.append(("reasoning_leak", "low", "разсъждение в описанието"))
            break

    # romanized-junk synonyms (all-lowercase Latin tokens)
    junk = [s.strip() for s in syn.split(",") if s.strip() and _LATIN_LOWER.match(s.strip())]
    if junk:
        out.append(("romanized_synonyms", "low", ",".join(junk[:4])))

    # meta cut mid-thought: PRECISE signal — ends on a dangling function word or a comma
    # (a legitimately complete phrase ending in a content word is NOT flagged).
    for mk in ("Мета описание", "Мета наименование"):
        v = str(f.get(mk) or "").strip()
        if not v:
            continue
        last = re.split(r"\s+", v)[-1].strip(" ,").lower()
        if v.endswith(",") or last in _DANGLE:
            out.append(("meta_truncated", "low", f"{mk[:4]}…{last}"))

    return out


_DANGLE = {"и", "за", "с", "на", "от", "до", "при", "или", "към", "по", "във", "в",
           "със", "без", "под", "над", "чрез", "като", "е", "са", "на", "но", "а"}


def _is_prefix_or_material(tok):
    t = str(tok or "").strip()
    if not t:
        return True
    try:
        import catalogue_guard as cg
        up = re.sub(r"[^0-9A-ZА-Я]", "", t.upper())
        if up in cg.CATALOGUE_PREFIXES or up == cg.UNIVERSAL_PREFIX or t.lower() in cg.MATERIAL_WORDS:
            return True
    except Exception:
        pass
    return False


def needs_human(record):
    """Deterministic triage: any HIGH flag, or >= 2 MEDIUM flags -> review."""
    fl = flags(record)
    highs = [x for x in fl if x[1] == "high"]
    meds = [x for x in fl if x[1] == "medium"]
    return (bool(highs) or len(meds) >= 2), fl


if __name__ == "__main__":
    import db, json, collections, sys
    canon = db.canonical_records()
    counts = collections.Counter()
    nh = 0
    examples = collections.defaultdict(list)
    for code, rec in canon.items():
        need, fl = needs_human(rec)
        if need:
            nh += 1
        for c, sev, det in fl:
            counts[c] += 1
            if len(examples[c]) < 3:
                examples[c].append((code, det))
    print(f"scanned {len(canon)} products")
    print(f"deterministic needs_human: {nh} ({100*nh//max(len(canon),1)}%)  "
          f"[was 0.5% via self-rating]")
    print("flag counts:", dict(counts.most_common()))
    if "--examples" in sys.argv:
        for c, ex in examples.items():
            print(f"  {c}: {ex}")
