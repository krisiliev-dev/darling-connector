# -*- coding: utf-8 -*-
"""Deterministic quality cleaners (Tier 1) — zero quota. Fix the high-volume defects the
output-quality audit found: romanized-junk synonyms, model-reasoning leakage in copy,
recoverable-but-empty brand, JSON-blob attributes, catalogue codes in names, Марка→Бранд
key drift, and meta cut mid-thought. Each is conservative and returns (value, changed).

NOTE: fabricated authority claims (WIPO/AISI/certificates) are NOT auto-edited here —
those only get FLAGGED for human review (quality_flags), because deleting a claim that
happens to be true would itself be wrong. Cleaning is for unambiguous junk only.
"""
import re, json
import quality_flags as qf

_LATIN_LOWER = re.compile(r"^[a-z][a-z0-9\s\-]*$")


def clean_synonyms(syn):
    """Drop all-lowercase-Latin (romanized BG junk) synonym entries; keep Cyrillic and
    brand-like tokens (any uppercase letter). 'вилица, tigan, HFM' -> 'вилица, HFM'."""
    s = str(syn or "")
    if not s.strip():
        return s, False
    # keep Cyrillic and brand-like tokens (any uppercase); drop pure-lowercase-Latin junk
    kept = [t.strip() for t in s.split(",") if t.strip() and not _LATIN_LOWER.match(t.strip())]
    out = ", ".join(kept)
    return out, (out != s.strip())


def strip_reasoning_leak(desc):
    """Remove whole sentences that contain model-reasoning leakage. Sentence-split (not a
    spanning regex → no backtracking); a sentence is dropped only if it carries a leak
    phrase, so surrounding product copy is preserved intact."""
    s = str(desc or "")
    if not s or not any(rx.search(s) for rx in qf.LEAK_PHRASES):
        return s, False
    sents = re.split(r"(?<=[.!?])\s+", s)
    kept = [sen for sen in sents if not any(rx.search(sen) for rx in qf.LEAK_PHRASES)]
    new = " ".join(kept)
    new = re.sub(r"<(p|li|ul|h2)>\s*</\1>", "", new)     # drop tags emptied by removal
    new = re.sub(r"\s{2,}", " ", new).strip()
    return new, (new != s)


def backfill_brand(fields):
    """If Бранд is empty but a plausible brand sits in the attributes, populate it.
    Runs AFTER the driver's brand guards, so it must apply them itself: reject supplier
    names and anything guard_brand would drop (prefix/material/collection)."""
    if str(fields.get("Бранд") or "").strip():
        return fields.get("Бранд"), False
    m = qf._BRAND_IN_ATTR.search(str(fields.get("Атрибути") or ""))
    cand = (m.group(1).strip() if m else "")
    if not cand or len(cand) < 3 or cand.lower() in ("н/а", "няма", "-") \
            or qf._is_prefix_or_material(cand):
        return fields.get("Бранд"), False
    try:
        import run_one as _ro
        if cand.lower() in {s.lower() for s in getattr(_ro, "SUPPLIER_NAMES", [])}:
            return fields.get("Бранд"), False           # supplier ≠ brand
    except Exception:
        pass
    try:
        import catalogue_guard as _cg
        kept, _note = _cg.guard_brand(cand, [])
        if not kept:
            return fields.get("Бранд"), False
        cand = kept
    except Exception:
        pass
    return cand, True


def fix_json_attrs(attrs):
    """'{"Тип":"Чиния","Материал":"Метал"}' -> 'Тип: Чиния; Материал: Метал'."""
    s = str(attrs or "").strip()
    if not s.startswith("{"):
        return attrs, False
    try:
        d = json.loads(s)
        if isinstance(d, dict):
            out = "; ".join(f"{k}: {v}" for k, v in d.items() if str(v).strip())
            return out, (out != s)
    except Exception:
        pass
    return attrs, False


def normalize_attr_keys(attrs):
    """'Марка: X' -> 'Бранд: X' so the same concept co-filters. Also drops empty 'Key:;'."""
    s = str(attrs or "")
    if not s.strip():
        return s, False
    new = re.sub(r"(^|;\s*)Марка(\s*:)", r"\1Бранд\2", s)
    new = re.sub(r"(^|;\s*)[^:;]+:\s*(?=;|$)", r"\1", new)   # drop 'Key:;' empties
    new = re.sub(r";\s*;", ";", new)
    new = re.sub(r"\s{2,}", " ", new).strip("; ").strip()
    return new, (new != s.strip())


def strip_catcode_from_name(name):
    """Remove a trailing catalogue code from a NAME: '(17703)' or a dangling 'AB-1234'."""
    s = str(name or "")
    if not s:
        return s, False
    new = re.sub(r"\s*\(\s*\d{3,}\s*\)\s*$", "", s)
    new = re.sub(r"\s+[A-Z]{1,4}-?\d{3,}\s*$", "", new)
    new = new.strip(" -–,")
    return new, (new != s)


def fix_meta_dangle(meta):
    """Trim a meta that ends on a dangling function word (or bare comma) back to the last
    content word. '...черен, обем за' -> '...черен, обем'. A trailing comma strips ONLY
    the comma (never the word before it), and the original is kept if trimming would
    empty the meta."""
    s = str(meta or "").strip()
    orig = s
    if not s:
        return s, False
    changed = False
    while s:
        if s.endswith(","):
            s = s.rstrip(" ,")
            changed = True
            continue
        last = s.split(" ")[-1].lower()
        if last in qf._DANGLE:
            s = re.sub(r"\s*\S+$", "", s).rstrip(" ,")
            changed = True
        else:
            break
    if not s:                                           # never write an emptied meta
        return orig, False
    return s, changed


_UNIT_LIKE = ("Наименование", "Описание", "Мета описание", "Мета наименование", "Синоними", "Атрибути")


def clean(fields):
    """Apply all safe cleaners to a COPY of fields. Returns (new_fields, changes)."""
    f = dict(fields)
    changes = []
    v, ch = clean_synonyms(f.get("Синоними"))
    if ch:
        f["Синоними"] = v; changes.append("synonyms")
    v, ch = strip_reasoning_leak(f.get("Описание"))
    if ch:
        f["Описание"] = v; changes.append("reasoning_leak")
    v, ch = fix_json_attrs(f.get("Атрибути"))
    if ch:
        f["Атрибути"] = v; changes.append("json_attrs")
    v, ch = normalize_attr_keys(f.get("Атрибути"))
    if ch:
        f["Атрибути"] = v; changes.append("attr_keys")
    v, ch = backfill_brand(f)
    if ch:
        f["Бранд"] = v; changes.append("brand_backfill")
    v, ch = strip_catcode_from_name(f.get("Наименование"))
    if ch:
        f["Наименование"] = v; changes.append("catcode_name")
    for mk in ("Мета описание", "Мета наименование"):
        v, ch = fix_meta_dangle(f.get(mk))
        if ch:
            f[mk] = v; changes.append("meta_dangle")
    return f, changes
