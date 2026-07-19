# -*- coding: utf-8 -*-
"""Deterministic, zero-quota field tidies — the mechanical fixes the QA reviewer
keeps flagging every cycle (unit inconsistency, brand contamination, name-order),
moved out of the LLM so we don't spend free quota re-fixing formatting.

SAFETY CONTRACT:
  * Touches ONLY customer-facing text (Наименование/Бранд/Атрибути/Синоними/Описание/
    Мета*). NEVER the empiric columns (Код/Цена/Количество/Мярка/Каталожен номер).
  * Every transform is conservative and REVERSIBLE in intent: when unsure, it leaves
    the value untouched rather than guessing. Each returns (value, changed/note) so a
    caller can log exactly what moved.
"""
import re
import brand_tools

# ---------------------------------------------------------------- units ----------
# Latin unit token right after a number -> canonical Cyrillic, with one space.
# Longer tokens first so 'cm' wins before 'm', 'ml' before 'l', etc.
_LAT_UNITS = [("cm", "см"), ("mm", "мм"), ("ml", "мл"), ("lt", "л"),
              ("kg", "кг"), ("gr", "г"), ("l", "л"), ("g", "г")]
_LAT_ALT = "|".join(u for u, _ in _LAT_UNITS)
_LAT_RX = re.compile(r"(?<![A-Za-zА-Яа-я])(\d+(?:[.,]\d+)?)\s?(" + _LAT_ALT + r")(?![A-Za-zА-Яа-я0-9])")
_LAT_TO_CYR = {u: c for u, c in _LAT_UNITS}

# Verbose Cyrillic spellings -> abbreviation (the reviewer's '18 л' vs '18 литра' flag).
_VERBOSE = [("милилитр", "мл"), ("милилитра", "мл"), ("сантиметр", "см"),
            ("сантиметра", "см"), ("милиметр", "мм"), ("милиметра", "мм"),
            ("килограм", "кг"), ("килограма", "кг"), ("литър", "л"), ("литра", "л"),
            ("литри", "л"), ("грамове", "г"), ("грама", "г"), ("грам", "г")]
_VERB_ALT = "|".join(re.escape(w) for w, _ in sorted(_VERBOSE, key=lambda x: -len(x[0])))
_VERB_RX = re.compile(r"(\d+(?:[.,]\d+)?)\s*(" + _VERB_ALT + r")(?![А-Яа-я])", re.IGNORECASE)
_VERB_MAP = {}
for _w, _a in _VERBOSE:
    _VERB_MAP[_w] = _a


# Bulgarian locale uses a decimal COMMA. Convert 'digit.digit' -> 'digit,digit' ONLY when
# it's immediately followed by a unit (so it's unambiguously a measurement, never a
# version/model number). Runs after unit normalization, so the unit is already Cyrillic.
_DEC_UNIT = re.compile(r"(\d+)\.(\d+)(\s*(?:л|мл|кг|г|см|мм|cm|mm|ml|l)\b)", re.IGNORECASE)


def normalize_decimal_comma(text):
    """'0.83 л'->'0,83 л', '2.5 мм'->'2,5 мм'. Only a decimal that is followed by a unit.
    Returns (text, changed)."""
    s = str(text or "")
    if not s:
        return s, False
    new = _DEC_UNIT.sub(lambda m: m.group(1) + "," + m.group(2) + m.group(3), s)
    return new, (new != s)


def normalize_units(text):
    """'2.5mm'->'2.5 мм', '40cm'->'40 см', '18 литра'->'18 л'. Only converts a unit
    token that DIRECTLY follows a number (so plain words are never touched).
    Returns (text, changed)."""
    s = str(text or "")
    if not s:
        return s, False

    def _lat(m):
        return m.group(1) + " " + _LAT_TO_CYR[m.group(2).lower()]

    def _verb(m):
        return m.group(1) + " " + _VERB_MAP[m.group(2).lower()]

    new = _LAT_RX.sub(_lat, s)
    new = _VERB_RX.sub(_verb, new)
    new = re.sub(r"\s{2,}", " ", new).strip()
    return new, (new != s.strip())


# ---------------------------------------------------------------- brand ----------
_MAT = None  # lazy import to avoid a cycle at module load


def _materials():
    global _MAT
    if _MAT is None:
        try:
            import catalogue_guard as cg
            _MAT = cg.MATERIAL_WORDS
        except Exception:
            _MAT = set()
    return _MAT


# Sub-brand / line suffixes that are unambiguously NOT the manufacturer name. Kept
# deliberately tight: 'HORECANO KIDS'->'HORECANO', but a real two-word brand
# (Bormioli Rocco, Luigi Bormioli, Ceramic House, Home Line) is never touched — the
# test proved multi-word brands are commonly real, so we only strip a KNOWN marker.
_LINE_MARKERS = {"kids", "junior", "baby", "collection", "колекция", "series", "серия"}


def split_brand(brand, gaz=None):
    """Strip a trailing/leading line-MARKER from a multi-word brand ('HORECANO KIDS'->
    'HORECANO', 'Bonna Collection'->'Bonna'). Deliberately conservative: it removes ONLY
    a word from the explicit marker set, never an arbitrary token, never a material, and
    never touches a single-token brand — so real multi-word brands survive untouched.
    Returns (brand_or_None, note). ('HFM DEFNE'-type line contamination is handled
    upstream by the enrichment prompt + the reviewer, not here — DEFNE is not safely
    distinguishable from a real second brand word by rule.)"""
    raw = str(brand or "").strip()
    if not raw or " " not in raw:
        return (raw or None), None
    toks = raw.split()
    kept = list(toks)
    while len(kept) > 1 and kept[-1].lower() in _LINE_MARKERS:
        kept.pop()
    while len(kept) > 1 and kept[0].lower() in _LINE_MARKERS:
        kept.pop(0)
    if kept != toks and kept:
        new = " ".join(kept)
        return new, f"brand_marker:{raw}->{new}"
    return raw, None


# --------------------------------------------------- synonyms x material ----------
def _attr_value(attrs, key):
    for part in str(attrs or "").split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            if k.strip().lower() == key.lower():
                return v.strip()
    return ""


# Material FAMILIES — a synonym is only wrong if it names a DIFFERENT family than the
# product's material. 'метал' and 'стомана' are the SAME family, so 'метал' must stay
# on a steel product; 'порцелан' (ceramic) on a steel product is a genuine contradiction.
_FAMILY = {}
for _fam, _words in {
    "metal": ["метал", "стомана", "неръждаема", "инокс", "inox", "алуминий",
              "aluminium", "aluminum", "чугун", "steel", "metal", "месинг", "мед"],
    "ceramic": ["керамика", "порцелан", "ceramic", "porcelain", "фаянс", "теракота"],
    "glass": ["стъкло", "glass", "кристал"],
    "plastic": ["пластмаса", "plastic", "поликарбонат", "polycarbonate", "акрил",
                "acrylic", "меламин", "melamine", "силикон", "silicone", "найлон"],
    "wood": ["дърво", "wood", "бамбук", "bamboo", "ратан", "mdf"],
    "textile": ["текстил", "плат", "памук", "cotton", "полиестер", "лен"],
    "paper": ["хартия", "картон", "paper"],
    "stone": ["камък", "мрамор", "гранит", "marble", "stone"],
}.items():
    for _w in _words:
        _FAMILY[_w] = _fam


def _family_of(word):
    return _FAMILY.get(str(word or "").strip().lower())


def clean_synonyms(synonyms, attrs):
    """Remove a synonym that is a LONE material word from a DIFFERENT material family
    than the product's Материал ('порцелан' on a стомана product). Same-family terms
    ('метал' on steel) are KEPT — steel is a metal. Never touches multi-word phrases.
    Returns (synonyms, removed_list)."""
    s = str(synonyms or "")
    if not s.strip():
        return s, []
    material = _attr_value(attrs, "Материал").lower()
    if not material:
        return s, []
    prod_fams = {f for f in (_family_of(w) for w in re.split(r"[ ,/]+", material)) if f}
    if not prod_fams:
        return s, []
    out, removed = [], []
    for syn in [x.strip() for x in s.split(",")]:
        fam = _family_of(syn)
        if fam and fam not in prod_fams and " " not in syn.strip():
            removed.append(syn)
            continue
        if syn:
            out.append(syn)
    return (", ".join(out), removed)


# ------------------------------------------------------------- name order --------
# Rebuild a name in the template order Марка · Тип · Материал · Размер · Цвят · Форма
# ONLY from parts we can identify with confidence (brand value + attribute values that
# literally occur in the name). Descriptive words we can't classify keep their relative
# order right after the type. This is the HIGHER-RISK transform — it is measured
# separately and only enabled if the test shows it helps.
_DIM_RX = re.compile(r"(?:Ø|ø|⌀)?\d+(?:[.,]\d+)?\s*[xх×*]?\s*[hHwWdDВвШшДдГг]?\d*(?:[.,]\d+)?\s*"
                     r"(?:см|мм|мл|л|кг|г|cm|mm)?", re.IGNORECASE)


def reorder_name(name, brand, attrs):
    """Return (name, changed). Conservative: only moves a recognised BRAND token to the
    front (template position 1) when it already appears in the name but not at the
    start. Full multi-slot reordering proved lossy on freeform Bulgarian names, so we
    keep just the safe, unambiguous brand-first move."""
    s = str(name or "").strip()
    b = str(brand or "").strip()
    if not s or not b or len(b) < 2:
        return s, False
    # already brand-first?
    if s.lower().startswith(b.lower()):
        return s, False
    # brand present as a whole token elsewhere -> move it to the front, once
    rx = re.compile(r"(?<![0-9A-Za-zА-Яа-я])" + re.escape(b) + r"(?![0-9A-Za-zА-Яа-я])")
    if not rx.search(s):
        return s, False
    moved = rx.sub("", s, count=1)
    moved = re.sub(r"\s{2,}", " ", moved).strip(" -–,;")
    out = (b + " " + moved).strip()
    return out, (out != s)


# ---------------------------------------------------------------- driver ---------
_UNIT_FIELDS = ("Наименование", "Мета наименование", "Мета описание", "Описание", "Атрибути")


def tidy(fields, gaz=None, do_reorder=False):
    """Apply the safe deterministic tidies to a COPY of an editable-fields dict.
    Returns (new_fields, changes) where changes is a list of note strings. Does not
    touch any key outside the customer-facing set. `do_reorder` gates the risky
    name-order move so the test harness can measure it in isolation."""
    f = dict(fields)
    changes = []
    for col in _UNIT_FIELDS:
        if f.get(col):
            v, ch = normalize_units(f[col])
            v, ch2 = normalize_decimal_comma(v)
            if ch or ch2:
                f[col] = v
                changes.append(f"units:{col}")
    b0 = f.get("Бранд")
    if b0:
        b1, bn = split_brand(b0, gaz)
        if b1 != b0:
            f["Бранд"] = b1
            changes.append(bn or f"brand:{b0}->{b1}")
            # if the name led with the OLD multiword brand, swap in the clean one
            nm = str(f.get("Наименование") or "")
            if b1 and nm.lower().startswith(str(b0).lower()):
                f["Наименование"] = (b1 + nm[len(str(b0)):]).strip()
                changes.append("name_brand_synced")
    if f.get("Синоними"):
        syn, rm = clean_synonyms(f["Синоними"], f.get("Атрибути"))
        if rm:
            f["Синоними"] = syn
            changes.append("syn_material:" + ",".join(rm)[:60])
    if do_reorder and f.get("Наименование"):
        nm, ch = reorder_name(f["Наименование"], f.get("Бранд"), f.get("Атрибути"))
        if ch:
            f["Наименование"] = nm
            changes.append("name_reorder")
    return f, changes
