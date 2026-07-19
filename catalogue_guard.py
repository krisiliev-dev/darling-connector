# -*- coding: utf-8 -*-
"""Deterministic guards against catalogue-number / prefix leaks.

Microinvest 'Стока' names follow the shape:  BR-[COLLECTION-]Name (CATALOGUE_NUMBER)
Agents leak three things from it into customer-facing fields:
  1. the universal 'BR-' line prefix,
  2. the catalogue number itself (e.g. 'JAG 1152-50', 'ZCP 570', 'K-2050'),
  3. a catalogue prefix or collection token as a bogus Бранд.

We fix these in the DRIVER (never trusting the prompt), using each product's OWN
source catalogue number — so we only ever strip a string the source itself marks
as a catalogue code (in parentheses, containing a digit). The gazetteer is always
consulted first, so a REAL brand (incl. short ones like HL = Hobby life) is never
dropped or altered.
"""
import re
from pathlib import Path
import brand_tools

HERE = Path(__file__).parent
PREFIX_FILE = HERE / "catalogue_prefixes.txt"
COLLECTION_FILE = HERE / "collection_tokens.txt"

# The universal mira-n line prefix: on ~every product's Стока and image folder
# (…/images/br/). Never a consumer brand.
UNIVERSAL_PREFIX = "BR"

_PAREN = re.compile(r"\(([^()]*\d[^()]*)\)")            # a (…digit…) group = catalogue no.
_PREFIX_OF = re.compile(r"([A-Za-zА-Яа-я]{1,6})[\s\-]?\d")
_HAS_LETTER = re.compile(r"[A-Za-zА-Яа-я]")

# Cyrillic<->Latin lookalikes: source codes are often Cyrillic ('Т30') while the
# agent transliterates them to Latin in the name ('T30'). Match tolerantly.
_HOMO = {"А": "A", "В": "B", "С": "C", "Е": "E", "Н": "H", "К": "K", "М": "M",
         "О": "O", "Р": "P", "Т": "T", "Х": "X", "У": "Y",
         "а": "a", "е": "e", "о": "o", "с": "c", "р": "p", "х": "x", "у": "y"}
# An embedded model/catalogue code: 1-4 letters, optional single dash, 2+ digits,
# optional short trailing letters (E2483, DH1142, B-17, Т30, SG-86205, K8229).
_MODEL_CODE = re.compile(r"[A-Za-zА-Яа-я]{1,4}-?\d{2,}[A-Za-z]{0,2}")
_DIM_UNIT = r"(?:cm|см|mm|мм|ml|мл|lt|l|л|g|гр|г|kg|кг|oz|бр|pcs|ца)"
# single-letter height/width/depth/diameter markers (Latin + Cyrillic) — 'h60', 'В30'
# are DIMENSIONS, not catalogue codes.
_DIM_LETTER = set("hHwWdDВвШшДдГгФф")

# Leading supplier prefix in the source name: 'CN-…', 'CNC-…', 'BR-…' — a warehouse
# code, never a brand or a descriptor. Stripped from the title; blocked as a brand.
_LEAD = re.compile(r"^([A-Z]{2,4})-")
# 'мод.170', 'модел 170', 'mod.170', 'model № 5' — a model-number reference.
_MOD = re.compile(r"\b(?:мод|модел|mod|model)\.?\s*№?\s*\d+[A-Za-z]?\b", re.IGNORECASE)
# Material / generic descriptors the agent sometimes mistakes for a brand.
MATERIAL_WORDS = {
    "инокс", "inox", "иноx", "стомана", "steel", "неръждаема", "неръждаема стомана",
    "пластмаса", "plastic", "метал", "metal", "силикон", "silicone", "керамика",
    "ceramic", "порцелан", "porcelain", "стъкло", "glass", "меламин", "melamine",
    "бамбук", "bamboo", "дърво", "wood", "алуминий", "aluminium", "aluminum",
    "чугун", "cast iron", "поликарбонат", "polycarbonate", "акрил", "acrylic",
}


def source_leading_prefix(stoka, gaz=None):
    """The leading 'XXX-' supplier prefix of a source name, unless it is a real
    (gazetteer) brand. 'CNC-Стойка…' -> 'CNC'; 'LAV-…' -> None (LAV is a brand)."""
    m = _LEAD.match(str(stoka or "").strip())
    if not m:
        return None
    tok = m.group(1)
    return None if brand_tools.lookup(tok, gaz) else tok


def _balance_parens(s):
    """Trim an unmatched trailing '(' + short leftover ('… кафяв (CN' -> '… кафяв')
    and any emptied '()'. Only removes obvious orphan fragments, never real content."""
    s = re.sub(r"\(\s*\)", "", s)
    if s.count("(") > s.count(")"):
        s = re.sub(r"\(\s*[^()]{0,6}$", "", s)
    return s.strip(" -–,;")


def _tidy(s):
    """Normalise whitespace and remove dashes orphaned by a token removal
    ('купа -CERAMICA' -> 'купа CERAMICA', 'форми - 4бр' unchanged). A dash BETWEEN
    two word chars ('SHENGYA-BLACK') is preserved."""
    s = re.sub(r"\s{2,}", " ", s)
    s = re.sub(r"\s+([,.;])", r"\1", s)
    s = re.sub(r"(?:^|(?<=\s))[-–](?=[0-9A-Za-zА-Яа-я])", "", s)   # orphan leading dash
    s = re.sub(r"(?<=[0-9A-Za-zА-Яа-я])[-–](?=\s|$)", "", s)       # orphan trailing dash
    s = re.sub(r"\s{2,}", " ", s)
    return _balance_parens(s.strip(" -–,;"))


def strip_leading_prefix(name, prefix):
    """Remove the supplier prefix token (whole token, anywhere) from a name."""
    if not name or not prefix:
        return name, False
    rx = r"(?<![0-9A-Za-zА-Яа-я])" + re.escape(prefix) + r"-?(?![0-9A-Za-zА-Яа-я])"
    new = re.sub(rx, " ", str(name))
    if new != name:
        return _tidy(new), True
    return name, False


def trim_meta(text, limit):
    """Trim a meta field to <= limit chars at a clean word/sentence boundary (Google
    truncates over-length meta anyway, so a tidy self-trim is strictly better).
    Returns (trimmed, changed)."""
    s = str(text or "").strip()
    if len(s) <= limit:
        return s, False
    cut = s[:limit]
    for sep in (". ", "! ", "? "):
        i = cut.rfind(sep)
        if i >= limit * 0.55:
            return cut[:i + 1].strip(), True
    i = cut.rfind(" ")
    out = (cut[:i] if i >= limit * 0.55 else cut).rstrip(" ,;:-–")
    return out, True


def source_model_codes(stoka):
    """Model/catalogue codes embedded in the source name, EXCLUDING dimensions.
    Returned verbatim as they appear in the source (may be Cyrillic)."""
    s = str(stoka or "")
    out = []
    for m in _MODEL_CODE.finditer(s):
        tok = m.group(0)
        a, b = m.span()
        prev = s[a-1] if a > 0 else " "
        nxt = s[b:b+6]
        prefix = re.match(r"[A-Za-zА-Яа-я]+", tok).group(0)
        if prev in "×xX*/.," or prev.isdigit():           # inside a WxHxD / decimal group
            continue
        if re.match(r"[.,]\d", nxt):                       # 'h21.5' -> a measurement, not a code
            continue
        if re.match(r"\s*" + _DIM_UNIT + r"\b", nxt, re.I):   # followed by a unit -> a size
            continue
        if re.match(r"\s*[×xX*]", nxt):                   # followed by a dimension separator
            continue
        if len(prefix) == 1 and prefix in _DIM_LETTER:    # 'h60', 'В30' = height/width/depth
            continue
        out.append(tok)
    return out


def strip_model_codes(name, codes):
    """Homoglyph-tolerant, whole-token removal of source model codes from `name`,
    plus 'мод.NNN' model references, then tidy orphaned parens. Returns
    (clean_name, removed)."""
    if not name:
        return name, []
    s = str(name)
    removed = []
    for cn in (codes or []):
        pat = "".join((f"[{ch}{_HOMO[ch]}]" if ch in _HOMO else re.escape(ch)) for ch in cn)
        rx = r"(?<![0-9A-Za-zА-Яа-я])" + pat + r"(?![0-9A-Za-zА-Яа-я])"
        new = re.sub(rx, " ", s)
        if new != s:
            removed.append(cn)
            s = new
    new = _MOD.sub(" ", s)                                # 'мод.170' etc.
    if new != s:
        removed.append("мод.№")
        s = new
    if removed:
        s = re.sub(r"\(\s*[-–/,]\s*", "(", s)             # '( -2023)' -> '(2023)'
        s = _tidy(s)
    return s, removed


def _load_list(path):
    out = set()
    if path.exists():
        for ln in path.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#"):
                out.add(ln.upper())
    return out


CATALOGUE_PREFIXES = _load_list(PREFIX_FILE)
COLLECTION_TOKENS = _load_list(COLLECTION_FILE)


def source_catnums(stoka):
    """[(catnum_string, prefix_or_None), ...] parsed from a source Стока string."""
    out = []
    for m in _PAREN.finditer(str(stoka or "")):
        cn = m.group(1).strip()
        pm = _PREFIX_OF.match(cn)
        out.append((cn, pm.group(1).upper() if pm else None))
    return out


def strip_catnums_from_name(name, catnums):
    """Remove from `name`: (a) any EXACT source catalogue number that CONTAINS A
    LETTER (so a bare numeric size like '26' is never touched), and (b) the
    standalone universal 'BR' prefix. Returns (clean_name, removed_list).

    Conservative by design — we only delete a string the *source* flags as a
    catalogue code, matched verbatim (with flexible internal whitespace)."""
    if not name:
        return name, []
    s = str(name)
    removed = []
    for cn, _pref in catnums:
        if not _HAS_LETTER.search(cn):
            continue                                   # pure-numeric catnum: skip (could be a size)
        pat = re.escape(cn).replace(r"\ ", r"\s*")
        new = re.sub(r"[\(\[]?\s*" + pat + r"\s*[\)\]]?", " ", s, flags=re.IGNORECASE)
        if new != s:
            removed.append(cn)
            s = new
    new = re.sub(r"(?<![0-9A-Za-zА-Яа-я])BR(?![0-9A-Za-zА-Яа-я])", " ", s)
    if new != s:
        removed.append("BR")
        s = new
    if removed:
        s = _tidy(s)
    return s, removed


def guard_brand(brand, catnum_prefixes, gaz=None):
    """Return (brand_or_None, note).

    Order matters and protects real brands:
      1. gazetteer match (raw or core) -> KEEP, canonicalised (real brands incl. HL
         and the newly-seeded LAV/Pirge/Vidivi... survive).
      2. known series/collection token, or an 'X Collection' phrase -> DROP (a
         pattern/series name, not a manufacturer). Note carries the CORE token so the
         caller can also strip it from the title.
      3. equals 'BR', this product's OWN catalogue prefix, or a known catalogue
         prefix -> DROP.
      4. otherwise -> keep as-is (unknown, but not a known prefix/collection)."""
    if not brand:
        return None, None
    raw = str(brand).strip()
    if not raw:
        return None, None
    canon = brand_tools.lookup(raw, gaz)               # gazetteer wins
    if canon:
        return canon, (None if canon == raw else f"brand_canon:{raw}->{canon}")
    if raw.lower() in MATERIAL_WORDS:                  # 'ИНОКС', 'стомана' — a material
        return None, f"brand_dropped_material:{raw}"
    core = re.sub(r"\b(collection|колекция)\b", "", raw, flags=re.IGNORECASE).strip()
    if core and core != raw:                           # 'Bonna Collection' -> re-check core
        ccanon = brand_tools.lookup(core, gaz)
        if ccanon:
            return ccanon, f"brand_canon:{raw}->{ccanon}"
    core_up = re.sub(r"[^0-9A-ZА-Я]", "", core.upper())
    if core_up in COLLECTION_TOKENS or core != raw:
        return None, f"brand_dropped_collection:{core or raw}"
    up = re.sub(r"[^0-9A-ZА-Я]", "", raw.upper())
    prefs = {p for p in (catnum_prefixes or []) if p} | {UNIVERSAL_PREFIX}
    if up in prefs or up in CATALOGUE_PREFIXES:
        return None, f"brand_dropped_prefix:{raw}"
    return raw, None


def title_strip_token(title, token):
    """Remove `token` from a TITLE only when it sits at the FRONT (a bogus brand/
    collection prefix the agent prepended). Never mid-sentence, never from the
    description. Returns (clean_title, changed)."""
    if not title or not token:
        return title, False
    core = re.sub(r"\b(collection|колекция)\b", "", str(token), flags=re.IGNORECASE).strip()
    if not core:
        return title, False
    new = re.sub(r"^\s*" + re.escape(core) + r"\b[\s\-–:,]*", "", str(title),
                 count=1, flags=re.IGNORECASE)
    if new != title and new.strip():
        return new.strip(" -–,:"), True
    return title, False
