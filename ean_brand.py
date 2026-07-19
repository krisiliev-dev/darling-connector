# -*- coding: utf-8 -*-
"""EAN/barcode -> brand-owner resolution (owner greenlight 2026-07-18).

The GS1 company prefix inside an EAN-13 is LICENSED to one legal entity — a registry
fact, not an AI guess. Lookups happen per UNIQUE PREFIX (thousands of products
collapse to a few hundred prefixes) and are cached forever in ean_prefix_cache.jsonl.

Verified by GS1 (gs1.org) allows ~30 manual searches/day; the --worklist report
orders unknown prefixes by product count so the owner (or an agent session) burns
those searches on the biggest wins first. Resolved owners feed brand_tools.gather
as an 'ean' source; legal-suffix stripping turns "Leifheit AG" into "Leifheit";
supplier/importer names are gated exactly like every other source — nothing skips
the /brands queue.

  python ean_brand.py --ingest FILE.xlsx   # read barcode columns, validate, classify
  python ean_brand.py --worklist           # unknown prefixes by product count
  python ean_brand.py --set PREFIX "Company Name"   # record a GS1 lookup result
  python ean_brand.py --report             # coverage stats
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
BARCODES = HERE / "barcodes.jsonl"            # {code, ean, cls, prefix}
PREFIX_CACHE = HERE / "ean_prefix_cache.jsonl"  # {prefix, owner, brand, src, ts}

# GS1 country prefixes we expect to see; used only for provenance context, the
# licensee lookup is what names the company.
_COUNTRY = {
    "380": "България", "868": "Турция", "869": "Турция", "690": "Китай",
    "691": "Китай", "692": "Китай", "693": "Китай", "694": "Китай", "695": "Китай",
    "400": "Германия", "401": "Германия", "402": "Германия", "403": "Германия",
    "404": "Германия", "440": "Германия", "800": "Италия", "801": "Италия",
    "802": "Италия", "803": "Италия", "804": "Италия", "805": "Италия",
    "806": "Италия", "807": "Италия", "808": "Италия", "809": "Италия",
    "859": "Чехия", "590": "Полша", "460": "Русия", "462": "Русия",
    "489": "Хонконг", "471": "Тайван", "885": "Тайланд", "893": "Виетнам",
    "540": "Белг./Люкс.", "870": "Нидерландия", "871": "Нидерландия",
    "560": "Португалия", "840": "Испания", "841": "Испания", "300": "Франция",
    "500": "Великобритания", "501": "Великобритания",
}

_LEGAL = re.compile(
    r"\s+(AG|GmbH|KG|&\s*Co\.?|S\.?p\.?A\.?|S\.?r\.?l\.?|S\.?r\.?o\.?|S\.?A\.?|S\.?L\.?"
    r"|B\.?V\.?|Ltd\.?|LLC|Inc\.?|Co\.?|Sp\.?\s*z\s*o\.?o\.?|d\.?o\.?o\.?"
    r"|ЕООД|ООД|АД|ЕАД|A\.?Ş\.?|San\.?|Tic\.?|Ştı\.?|Şti\.?|Ltd\.?\s*Şti\.?)\.?\s*$",
    re.I)


# Turkish/generic corporate & product-category words that follow the brand token(s) in a
# GS1 legal name: "TİTİZ PLASTİK DIŞ TİCARET..." -> brand is everything BEFORE the first
# of these. Two-word brands ("YEŞİL YAYLA KESİCİ...") survive because the cut happens at
# the first category word, not the first space.
# compared after _fold() (Turkish letters -> Latin), so ASCII forms only
_CATEGORY_STOP = {
    "plastik", "zuccaciye", "seramik", "sanayi", "sanayii", "san", "ticaret", "tic",
    "dis", "limited", "ltd", "sirketi", "sti", "anonim", "as", "pazarlama", "paz",
    "mutfak", "esya", "esyalari", "kesici", "aletler", "madeni", "maden", "servis",
    "ekipmanlari", "turizm", "kalip", "ve", "scop", "sa", "gida", "ith", "ihr", "grup",
    "metal", "cam", "ambalaj", "kimya", "tekstil", "ev",
}


_TR_FOLD = str.maketrans({"İ": "I", "ı": "i", "Ş": "S", "ş": "s", "Ğ": "G", "ğ": "g",
                          "Ü": "U", "ü": "u", "Ö": "O", "ö": "o", "Ç": "C", "ç": "c",
                          "Â": "A", "â": "a"})


def _fold(s):
    """ASCII-ish fold for Turkish letters (İ/ş/ğ/ü/ö/ç) — Bulgarian shoppers search the
    Latin form, and it aligns with existing gazetteer entries (Dunya, not Dünya)."""
    import unicodedata
    s = str(s).translate(_TR_FOLD)
    return "".join(c for c in unicodedata.normalize("NFKD", s)
                   if not unicodedata.combining(c))


def clean_owner_to_brand(owner):
    """GS1 legal name -> display brand. Strips western legal suffixes (Leifheit AG ->
    Leifheit), then for Turkish-style names keeps the leading token(s) up to the first
    corporate/category word (TİTİZ PLASTİK DIŞ TİC... -> Titiz; YEŞİL YAYLA KESİCİ
    ALETLER... -> Yesil Yayla). Turkish letters are folded to Latin. NOTE: returns the
    LEGAL/manufacturer brand — a distinct consumer TRADE brand (Renga for Mercanlar,
    Pirge for Yeşil Yayla) must be set explicitly; those are surfaced, not guessed."""
    b = str(owner or "").strip()
    for _ in range(4):
        b2 = _LEGAL.sub("", b).strip(" ,.-")
        if b2 == b:
            break
        b = b2
    kept = []
    for t in re.split(r"[\s.]+", b):
        tok = t.strip(".,")
        if not tok:
            continue
        if _fold(tok).lower() in _CATEGORY_STOP:
            break
        kept.append(tok)
    brand = _fold(" ".join(kept) if kept else b)
    if brand.isupper() or brand.islower():
        brand = " ".join(w.capitalize() for w in brand.split())
    return brand.strip(" ,.-")


def checksum_ok(ean):
    if not re.fullmatch(r"\d{13}", ean):
        return False
    digs = [int(c) for c in ean]
    return (10 - sum(d * (3 if i % 2 else 1) for i, d in enumerate(digs[:12])) % 10) % 10 == digs[12]


def classify(raw):
    """-> (cls, ean13_or_None). cls: gs1 | internal | invalid | empty."""
    e = re.sub(r"\D", "", str(raw or ""))
    if not e:
        return "empty", None
    if len(e) == 12:                       # UPC-A -> EAN-13
        e = "0" + e
    if len(e) == 8:                        # EAN-8: too short to carry a company prefix
        return "internal", e
    if len(e) != 13 or not checksum_ok(e):
        return "invalid", None
    if e[0] == "2" or e[:2] in ("02", "04"):   # in-store / variable-weight ranges
        return "internal", e
    return "gs1", e


def prefix_of(ean13):
    """We can't know the licensed prefix length (6-10) without the registry, so bucket
    by 9 digits: fine-grained enough to split companies, coarse enough to dedupe."""
    return ean13[:9]


def _load(path):
    out = []
    if path.exists():
        for ln in path.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                out.append(json.loads(ln))
            except Exception:
                pass
    return out


def prefix_cache():
    return {d["prefix"]: d for d in _load(PREFIX_CACHE) if d.get("prefix")}


# Only these prefix sources are AUTHORITATIVE enough to auto-assert a brand on a
# product. A merely "propagated" guess is NOT — it can be wrong for private-label /
# licensed-character goods or a prefix-bucket collision, so it only ever suggests
# (queued for owner/GS1 confirmation), never labels silently.
CONFIRMED_SRCS = {"gs1_verified", "owner_confirmed"}


def brand_for(ean_raw):
    """Confirmed brand for a raw barcode, or None. Propagated-only prefixes return None
    (they are suggestions, surfaced via the queue, not asserted)."""
    cls, e = classify(ean_raw)
    if cls != "gs1":
        return None
    hit = prefix_cache().get(prefix_of(e))
    if not hit or hit.get("bad") or hit.get("distributor") or hit.get("multi_brand"):
        return None
    if hit.get("src") not in CONFIRMED_SRCS:
        return None
    return hit.get("brand") or None


_bycode_cache = {"v": None}


def brand_for_code(code):
    """The 'ean' source for brand_tools.gather. Resolves ALL of a product's GS1 barcodes.
    Only CONFIRMED prefixes (GS1-verified / owner-confirmed) auto-assert a brand; a lone
    propagated guess is returned as a *pending* note (queued, never labelled). Disagreeing
    confirmed brands (sticker-over-sticker) -> conflict, nothing asserted.
    Returns (brand_or_None, note_or_None)."""
    if _bycode_cache["v"] is None:
        from collections import defaultdict
        m = defaultdict(list)
        for d in _load(BARCODES):
            if d.get("cls") == "gs1":
                m[str(d["code"])].append(d["ean"])
        _bycode_cache["v"] = dict(m)
    eans = _bycode_cache["v"].get(str(code)) or []
    cache = prefix_cache()
    confirmed, pending, info = {}, {}, []
    for e in eans:
        hit = cache.get(prefix_of(e))
        if not hit or hit.get("bad"):
            continue
        if hit.get("distributor"):
            info.append("distributor")             # known importer — brand is per-product
            continue
        if hit.get("multi_brand"):
            info.append("multibrand")              # known maker, several sub-brands
            continue
        if not hit.get("brand"):
            continue
        (confirmed if hit.get("src") in CONFIRMED_SRCS else pending)[hit["brand"]] = 1
    if len(confirmed) == 1:
        return next(iter(confirmed)), None
    if len(confirmed) > 1:
        return None, "ean_conflict:" + "/".join(sorted(confirmed))
    if pending:                                    # propagation guess only — do NOT assert
        return None, "ean_propagated_pending:" + "/".join(sorted(pending))
    if info:                                       # manufacturer known but brand is per-product
        return None, "ean_" + info[0]
    return None, None


def _read_grid(xlsx):
    """Robust reader for Microinvest exports: their XLSX has a malformed styles.xml that
    breaks openpyxl (calamine ignores it), a title/logo banner above the real header, and
    a header row found by locating 'Код'. Returns a list of dict rows."""
    import pandas as pd
    raw = None
    for eng in ("calamine", "openpyxl", None):
        try:
            raw = pd.read_excel(xlsx, sheet_name=0, header=None, dtype=str,
                                **({"engine": eng} if eng else {}))
            break
        except Exception:
            continue
    if raw is None:
        raise RuntimeError("could not read workbook with any engine")
    hdr_i = next((i for i in range(min(15, len(raw)))
                  if any(str(v).strip() == "Код" for v in raw.iloc[i].tolist())), 0)
    cols = [str(v).strip() for v in raw.iloc[hdr_i].tolist()]
    out = []
    for _, r in raw.iloc[hdr_i + 1:].iterrows():
        out.append({cols[j]: r.iloc[j] for j in range(len(cols))})
    return out, cols


def _split_barcodes(cell):
    """A single Microinvest barcode cell can pack several comma/space-separated codes
    (and trailing empty commas). Yield each raw token."""
    for tok in re.split(r"[,\s;]+", str(cell or "")):
        tok = tok.strip()
        if tok and tok.lower() != "nan":
            yield tok


def ingest(xlsx):
    """Keep ALL barcodes per product (owner 2026-07-18: importers/suppliers sticker
    extra barcodes over the manufacturer's — one 'best' barcode would silently pick
    the wrong one). Trust is decided at resolution time, per prefix, from evidence."""
    rows, cols = _read_grid(xlsx)
    bc_cols = [c for c in cols if re.search(r"баркод|barcode|ean|gtin", str(c), re.I)]
    code_col = next((c for c in cols if str(c).strip() == "Код"), cols[0])
    if not bc_cols:
        print(f"NO barcode column found; columns = {cols}")
        return
    print(f"rows: {len(rows)} | code col '{code_col}' | barcode cols {bc_cols}")
    stats = {"gs1": 0, "internal": 0, "invalid": 0, "empty": 0}
    n_multi = 0
    n_products = 0
    with BARCODES.open("w", encoding="utf-8") as fh:
        for row in rows:
            raw_code = str(row.get(code_col) or "").strip()
            if not raw_code or raw_code.lower() == "nan":
                continue
            codes = [c.strip() for c in raw_code.split("/") if c.strip()]  # merged pairs
            found = []
            for c in bc_cols:
                for tok in _split_barcodes(row.get(c)):
                    cls, e = classify(tok)
                    if cls != "empty":
                        stats[cls] += 1
                    if e and (cls, e) not in [(f["cls"], f["ean"]) for f in found]:
                        found.append({"cls": cls, "ean": e})
            n_products += 1
            if not found:
                stats["empty"] += 1
            if len([f for f in found if f["cls"] == "gs1"]) > 1:
                n_multi += 1
            for code in codes:
                for f in found:
                    fh.write(json.dumps({
                        "code": code, "ean": f["ean"], "cls": f["cls"],
                        "prefix": prefix_of(f["ean"]) if f["cls"] == "gs1" else None},
                        ensure_ascii=False) + "\n")
    n_pfx = len({d["prefix"] for d in _load(BARCODES) if d.get("prefix")})
    print(f"products: {n_products} | barcode tokens: {stats} | products with MULTIPLE "
          f"GS1 barcodes (sticker-over-sticker): {n_multi} | unique GS1 prefixes: {n_pfx}")
    conflicts()


def conflicts():
    """Trust screening: (a) one EAN on SEVERAL different till products = reused/
    misassigned label — distrust that EAN; (b) prefixes spanning implausibly many
    unrelated products are importer/distributor prefixes, not manufacturers."""
    from collections import Counter, defaultdict
    rows = [d for d in _load(BARCODES) if d.get("cls") == "gs1"]
    by_ean = defaultdict(set)
    for d in rows:
        by_ean[d["ean"]].add(d["code"])
    reused = {e: sorted(cs) for e, cs in by_ean.items() if len(cs) > 1}
    pfx_products = Counter(d["prefix"] for d in rows)
    big = [(p, n) for p, n in pfx_products.most_common(8) if n >= 50]
    if reused:
        print(f"  ⚠ {len(reused)} EAN(s) shared by MULTIPLE products (reused labels "
              f"OR duplicate till entries — human triage):")
        for e, cs in list(reused.items())[:10]:
            print(f"    {e}: {', '.join(cs[:6])}")
    if big:
        print(f"  ⚠ high-spread prefixes (importer/distributor pattern, NOT brand "
              f"evidence): {', '.join(f'{p}…({n})' for p, n in big)}")
    return reused, dict(big)


def autoflag_distributors(country="380", min_products=100):
    """Bulgarian (380…) prefixes carried by MANY unrelated products are the retailer's
    own / a wholesaler's labels, not a manufacturer — flag them so they neither waste
    GS1 lookups nor block a real manufacturer barcode on the same product. Reversible:
    entries live in ean_prefix_cache.jsonl; remove a line to un-flag. Foreign prefixes
    are NEVER auto-flagged (a Turkish maker with 200 SKUs really is the brand)."""
    from collections import Counter
    import time
    cache = prefix_cache()
    cnt = Counter(d["prefix"] for d in _load(BARCODES) if d.get("cls") == "gs1")
    flagged = []
    with PREFIX_CACHE.open("a", encoding="utf-8") as fh:
        for p, n in cnt.items():
            if p.startswith(country) and n >= min_products and p not in cache:
                fh.write(json.dumps({"prefix": p, "owner": None, "brand": None,
                                     "bad": "bg_own_or_distributor", "spread": n,
                                     "src": "autoflag",
                                     "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                                    ensure_ascii=False) + "\n")
                flagged.append((p, n))
    flagged.sort(key=lambda x: -x[1])
    print(f"auto-flagged {len(flagged)} Bulgarian high-spread prefixes as own/"
          f"distributor ({sum(n for _p, n in flagged)} product-links):")
    for p, n in flagged[:20]:
        print(f"   {p}  {n} products")
    return flagged


def mark_bad(prefix, reason="unregistered"):
    """Owner/GS1 verdict: prefix is fake/unregistered/deceptive — never a brand."""
    import time
    with PREFIX_CACHE.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"prefix": prefix, "owner": None, "brand": None,
                             "bad": reason, "src": "flagged",
                             "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                            ensure_ascii=False) + "\n")
    print(f"{prefix} marked BAD ({reason})")


def worklist():
    from collections import Counter
    cache = prefix_cache()
    rows = _load(BARCODES)
    cnt = Counter(d["prefix"] for d in rows if d.get("prefix"))
    unknown = [(p, n) for p, n in cnt.most_common() if p not in cache]
    print(f"{len(cnt)} prefixes, {len(unknown)} unresolved. Top of worklist "
          f"(one example EAN each — paste into gs1.org Verified by GS1, ~30/day free):")
    ex = {}
    for d in rows:
        if d.get("prefix") and d["prefix"] not in ex:
            ex[d["prefix"]] = d["ean"]
    for p, n in unknown[:30]:
        c = _COUNTRY.get(p[:3], "?")
        print(f"  {p}…  {n:4d} продукта  [{c}]  пример: {ex.get(p)}")


def set_prefix(prefix, owner, brand=None, inactive=False, distributor=False,
               multi_brand=None):
    """Record an authoritative GS1 lookup. brand defaults to the cleaned owner name; pass
    it explicitly for a TRADE brand that differs from the legal name (Renga for Mercanlar).
    distributor=True (a "Pazarlama"/importer prefix) or multi_brand=[...] (a manufacturer
    selling several sub-brands, e.g. İrak Plastik: Plastart/Home Design/…) mark the prefix
    as NON-ASSERTING: the manufacturer is known but no single brand is auto-applied to its
    products — product-level sources (vision/scrape) decide, exactly like the owner warned.
    gs1_verified OUTRANKS a propagated guess; we WARN on a cross-check disagreement."""
    import time
    derived = clean_owner_to_brand(owner)
    entry = {"prefix": prefix, "owner": owner, "src": "gs1_verified",
             "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
    if distributor:
        entry.update(brand=None, distributor=True, legal_brand=derived)
        print(f"{prefix} -> DISTRIBUTOR ({derived}) — no single brand asserted")
    elif multi_brand:
        entry.update(brand=None, multi_brand=list(multi_brand), legal_brand=derived)
        print(f"{prefix} -> MULTI-BRAND ({derived}: {', '.join(multi_brand)}) — "
              f"product-level branding")
    else:
        brand = brand or derived
        prev = prefix_cache().get(prefix)
        if prev and prev.get("src") == "propagated" and prev.get("brand") and \
                str(prev["brand"]).lower() != str(brand).lower():
            print(f"  ⚠ cross-check: propagation guessed {prev['brand']!r}, resolved "
                  f"to {brand!r} for {prefix}.")
        entry["brand"] = brand
        if brand != derived:
            entry["legal_brand"] = derived
        print(f"{prefix} -> {brand!r}" + (f"  (mfr: {derived})" if brand != derived else ""))
    if inactive:
        entry["gs1_inactive"] = True
    with PREFIX_CACHE.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def report():
    rows = _load(BARCODES)
    cache = prefix_cache()
    with_pfx = [d for d in rows if d.get("prefix")]
    resolved = [d for d in with_pfx if d["prefix"] in cache]
    print(f"{len(rows)} barcoded products | {len(with_pfx)} GS1 | "
          f"{len(resolved)} resolvable to an owner via {len(cache)} cached prefixes")


if __name__ == "__main__":
    if "--ingest" in sys.argv:
        ingest(sys.argv[sys.argv.index("--ingest") + 1])
    elif "--worklist" in sys.argv:
        worklist()
    elif "--conflicts" in sys.argv:
        conflicts()
    elif "--autoflag" in sys.argv:
        autoflag_distributors()
    elif "--set" in sys.argv:
        i = sys.argv.index("--set")
        set_prefix(sys.argv[i + 1], sys.argv[i + 2])
    elif "--bad" in sys.argv:
        i = sys.argv.index("--bad")
        mark_bad(sys.argv[i + 1],
                 sys.argv[i + 2] if len(sys.argv) > i + 2 else "unregistered")
    else:
        report()
