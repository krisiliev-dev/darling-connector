# -*- coding: utf-8 -*-
"""Deterministic 'Свързани' linker — variant grouping beyond catalogue-number ±1.

relate_tools links products whose supplier catalogue numbers sit ±1 apart. That misses
the common case the reviewer keeps flagging: the SAME product in different colours/sizes,
whose catalogue numbers are far apart. This module groups products by
(category, brand, colour/size-stripped base name) so those variants find each other.

Zero-quota, read-only over the finished records. UNIONs with the existing ±1 links, so
it only ever ADDS related products, never drops a catalogue-number link.
"""
import json, glob, re
from pathlib import Path

HERE = Path(__file__).parent

_COLOR = {
    "бял", "бяла", "бяло", "бели", "черен", "черна", "черно", "черни", "червен",
    "червена", "червено", "син", "синя", "синьо", "зелен", "зелена", "зелено",
    "жълт", "жълта", "жълто", "кафяв", "кафява", "кафяво", "сив", "сива", "сиво",
    "розов", "розова", "оранжев", "оранжева", "лилав", "лилава", "златен", "златист",
    "златиста", "сребрист", "сребриста", "сребърен", "бежов", "бежова", "кремав",
    "кремава", "тюркоаз", "многоцветен", "прозрачен", "прозрачна", "антрацит",
    "бордо", "теракота", "мента", "циклама", "виолетов", "маслинен",
}
_SIZE_RX = re.compile(r"(?:Ø|ø|⌀|№|no\.?)?\s*\d+(?:[.,]\d+)?\s*[xх×*/]?\s*"
                      r"[hHwWdDВвШшДдГг]?\s*\d*(?:[.,]\d+)?\s*"
                      r"(?:см|мм|мл|л|кг|г|cm|mm|ml|l|бр|части|ч)?", re.IGNORECASE)


def _attr_value(attrs, key):
    for part in str(attrs or "").split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            if k.strip().lower() == key.lower():
                return v.strip()
    return ""


def base_name(name, brand="", attrs=""):
    """Colour/size-stripped, lowercased core of a product name — the identity a set of
    variants shares. '...кръгъл кафяв Ø40x50 см' and '...кръгъл червен Ø30x40 см' both
    reduce to the same base."""
    s = " " + str(name or "").lower() + " "
    for tok in (str(brand or ""), _attr_value(attrs, "Цвят"), _attr_value(attrs, "Размер")):
        for w in re.split(r"[ ,/]+", tok.lower()):
            if len(w) >= 3:
                s = re.sub(r"(?<![0-9a-zа-я])" + re.escape(w) + r"(?![0-9a-zа-я])", " ", s)
    s = _SIZE_RX.sub(" ", s)
    words = [w for w in re.split(r"[^0-9a-zа-я]+", s)
             if w and w not in _COLOR and len(w) > 1]
    return " ".join(words).strip()


def build_groups(records):
    """{ (category, brand, base): [codes] } over finished records. Only groups with a
    base specific enough (>=2 words) and >1 member become links."""
    groups = {}
    for d in records:
        f = d.get("fields") or {}
        base = base_name(f.get("Наименование"), f.get("Бранд"), f.get("Атрибути"))
        if base.count(" ") < 1:                      # too generic (single word) -> skip
            continue
        cat = str(f.get("Категории") or "").split(";")[0].strip()
        brand = str(f.get("Бранд") or "").strip().lower()
        key = (cat, brand, base)
        groups.setdefault(key, []).append(str(d.get("code")))
    return {k: v for k, v in groups.items() if len(v) > 1}


def image_variant_groups(records, manifest, max_group=8):
    """Products that SHARE a source image URL are almost certainly the SAME product in a
    different size (suppliers reuse one photo across sizes — the size isn't visible). A
    strong 'related' signal. Guards against false links:
      * only within the SAME category (real variants share a category),
      * skip large shared-URL groups (a URL on many products is a generic placeholder,
        not a size range).
    `manifest` is {code: source_url}. Returns {(cat, url): [codes]}."""
    by_code = {str(d.get("code")): d for d in records}
    url_codes = {}
    for code, url in (manifest or {}).items():
        if str(code) in by_code and url:
            url_codes.setdefault(url, []).append(str(code))
    groups = {}
    for url, codes in url_codes.items():
        codes = list(dict.fromkeys(codes))
        if not (2 <= len(codes) <= max_group):
            continue                                     # singleton or placeholder-shared
        bycat = {}
        for c in codes:
            cat = str((by_code[c].get("fields") or {}).get("Категории") or "").split(";")[0].strip()
            bycat.setdefault(cat, []).append(c)
        for cat, cc in bycat.items():
            if len(cc) > 1:
                groups[(cat, url)] = cc
    return groups


def related_index(records, cap=8, manifest=None):
    """{ code: [related codes] } from colour/size-base-name grouping AND (when a manifest
    is given) shared-image size-variant grouping. Deduped, capped."""
    idx = {}

    def _link(cset):
        cset = list(dict.fromkeys(cset))
        for c in cset:
            for o in cset:
                if o != c:
                    idx.setdefault(c, [])
                    if o not in idx[c] and len(idx[c]) < cap:
                        idx[c].append(o)

    for codes in build_groups(records).values():
        _link(codes)
    if manifest:
        for codes in image_variant_groups(records, manifest).values():
            _link(codes)
    return idx


def load_records():
    recs = []
    for fp in glob.glob(str(HERE / "results.lane*.jsonl")):
        for line in open(fp, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if "agentic" in ((d.get("meta") or {}).get("notes") or []):
                recs.append(d)
    return recs


def load_manifest():
    """{code: source_url} from the image manifest (ok downloads) — for shared-image linking."""
    m = {}
    mp = HERE.parent / "image-pipeline" / "manifest.jsonl"
    if mp.exists():
        for line in open(mp, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("code") and d.get("url") and d.get("status") == "ok":
                m[str(d["code"])] = d["url"]
    return m


def union_related(existing, variants, cap=8):
    """Merge the ±1 catalogue links already in Свързани with variant links."""
    have = [x.strip() for x in re.split(r"[,;]+", str(existing or "")) if x.strip()]
    for v in variants:
        if v not in have:
            have.append(v)
    return ", ".join(have[:cap]) if have else None
