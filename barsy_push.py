# -*- coding: utf-8 -*-
"""Push enriched Darling products into Barsy (owner 2026-07-19).

Barsy already holds Darling's catalog (migrated from Microinvest): each article carries
the Microinvest `code` as its business key. So we NEVER blindly create — we resolve by
`code`:

  * code already in Barsy  -> Articles_update (enrich-in-place: add barcode, brand +
    attributes as `details`, public name; PRICE/QTY left untouched — those are owned by
    Barsy/Microinvest per the price policy).
  * code not in Barsy      -> Articles_create (full payload from barsy_collect).

Source of enrichment = our SQLite system-of-record (db.get_record), preferring the owner-
approved/edited fields when an approval exists. Barcodes = the ingested GS1 barcodes.

SAFETY: dry-run by default — prints the exact JSON body per product and writes NOTHING.
A real write requires BOTH `--push` and `--confirm`. Scope with `--code C` / `--limit N`.

  python barsy_push.py plan --code 210038        # show the exact update body, no write
  python barsy_push.py plan --limit 20           # dry-run the next 20 enrich candidates
  python barsy_push.py push --code 210038 --push --confirm   # ONE real update
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import barsy_api as b

HERE = Path(__file__).parent

# our normalized unit (Мярка / amount_type_name_short) -> Barsy amount_type_id
UNIT_TO_ID = {
    "бр": 1, "бр.": 1, "брой": 1, "": 1,
    "л": 2, "литър": 2, "кг": 3, "килограм": 3,
    "ч": 4, "д": 5, "км": 6, "м": 7, "метър": 7,
    "мин": 8, "м2": 11, "кв.м": 11, "м3": 16,
}
LANG = "bg_BG"


def _catalog():
    """Live {code: article} map of everything currently in Barsy (by business code)."""
    arts = b.call("Articles_getlist", {"filters": {}})
    return {str(a["code"]): a for a in arts if a.get("code")}


def _barcodes():
    import ean_brand as eb
    m = defaultdict(list)
    for d in eb._load(eb.BARCODES):
        if d.get("cls") == "gs1":
            m[str(d["code"])].append(str(d["ean"]))
    return m


def _fields(code):
    """Enriched fields for a code — owner-approved/edited version wins over DB canonical."""
    import db
    rec = db.get_record(code) or {}
    f = dict(rec.get("fields") or {})
    meta = rec.get("meta") or {}
    # approvals overlay
    try:
        import barsy_collect as bcol
        appr = bcol._approved().get(code)
        if appr:
            f.update({k: v for k, v in appr.items() if v not in (None, "")})
    except Exception:
        pass
    return f, meta


def _details(fields):
    """Barsy article `details` (characteristics) from our attributes + brand.
    Attributes are stored as 'Key: Value; Key: Value'. Brand becomes a 'Марка' detail."""
    rows = []
    brand = str(fields.get("Бранд") or "").strip()
    if brand:
        rows.append({"detail_name": "Марка", "detail_value": brand})
    for part in str(fields.get("Атрибути") or "").split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            k, v = k.strip(), re.sub(r"\s+", " ", v.strip())
            if k and v:
                rows.append({"detail_name": k, "detail_value": v})
    return rows


def _unit_id(fields, existing):
    u = str(fields.get("Мярка") or "").strip().lower().rstrip(".")
    if u in UNIT_TO_ID:
        return UNIT_TO_ID[u]
    return existing.get("amount_type_id") or 1        # keep Barsy's, else piece


_CATMAP = None


def _cat_id_for(meta, ensure=False):
    """Barsy cat_id for a product's Shopify leaf gid. Read-only against the build checkpoint by
    default; with ensure=True (the write path) it CREATES the leaf + ancestors just-in-time so a
    product never waits on the full background taxonomy build."""
    gid = (meta or {}).get("leaf_gid")
    if not gid:
        return None
    if ensure:
        import barsy_taxonomy as bt
        try:
            return bt.ensure_path(gid)
        except Exception:
            pass                                # fall back to read-only lookup below
    global _CATMAP
    if _CATMAP is None:
        import json
        p = HERE / "barsy_cat_map.json"
        _CATMAP = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    return _CATMAP.get(gid)


def _num(v):
    """Parse a Microinvest numeric string ('2', '2,5', '') -> float or None."""
    s = str(v or "").strip().replace(",", ".")
    try:
        return float(s) if s and s.lower() != "nan" else None
    except ValueError:
        return None


def build(code, catalog, bc, ensure_cat=False):
    """Return (mode, body) for one code. mode is 'update' or 'create'. body is the API arg.
    Only GAP fields are set on update; price/qty are never written here."""
    fields, meta = _fields(code)
    existing = catalog.get(code)
    barcodes = bc.get(code) or []
    art = {}
    name = str(fields.get("Наименование") or "").strip()
    if name:
        art["article_name"] = name
        art["article_name_ml"] = {LANG: name}          # Barsy stores ml as a lang-keyed map
    if barcodes:
        art["barcode"] = barcodes                      # ArticleInputData accepts an array
    details = _details(fields)
    if details:
        art["details"] = details
    desc = str(fields.get("Описание") or "").strip()
    cat_id = _cat_id_for(meta, ensure=ensure_cat)       # Shopify leaf gid -> Barsy cat_id
    if cat_id:
        art["cat_id"] = cat_id
        art["master_cat_id"] = cat_id
    aliases = [s.strip() for s in str(fields.get("Синоними") or "").split(",") if s.strip()]
    if aliases:
        art["article_aliases"] = aliases

    try:
        import barsy_collect as bcol
        pq = bcol._export_price_qty().get(code) or {}
    except Exception:
        pq = {}
    min_amt = _num(pq.get("min_qty"))                   # Microinvest reorder threshold

    if existing:
        aid = existing["article_id"]
        art["amount_type_id"] = _unit_id(fields, existing)
        if min_amt:
            art["min_amount"] = min_amt
        # enrich-in-place: only fill Barsy gaps, never clobber a populated field
        if existing.get("barcode"):
            art.pop("barcode", None)
        if not existing.get("description") and desc:
            art["description_ml"] = {LANG: desc}
        # Articles_update wants article_id at TOP level (not inside `article`)
        return "update", {"article_id": aid, "article": art}
    # create (approved products not yet in Barsy)
    art["amount_type_id"] = _unit_id(fields, {})
    art["ref_num"] = str(fields.get("Каталожен номер") or "") or None
    art["code"] = code
    art["is_public"] = 1
    art["is_for_sale"] = 1
    if min_amt:
        art["min_amount"] = min_amt
    if desc:
        art["description_ml"] = {LANG: desc}
    if pq.get("price"):
        art["actual_price"] = pq["price"]
    return "create", {"article": art}


def push_one(code, catalog=None, bc=None, images=True):
    """Create/update ONE product in Barsy (+ its images). Returns (mode, article_id).
    Used by the approved→store automation. Idempotent (update if the code already exists)."""
    if catalog is None:
        catalog = _catalog()
    if bc is None:
        bc = _barcodes()
    mode, body = build(code, catalog, bc, ensure_cat=True)
    method = "Articles_update" if mode == "update" else "Articles_create"
    out = b.call(method, body)
    aid = body.get("article_id") or (out if isinstance(out, int)
                                     else (out.get("article_id") if isinstance(out, dict) else None))
    if images and aid:
        push_images(code, aid)
    return mode, aid


def push_images(code, article_id, max_images=6):
    """Download a product's images (the Снимки supplier URLs) and upload them to the Barsy
    article as PICTURE files (Barsy resizes + sets article.picture). Returns (uploaded, err).
    Idempotent-ish: skips names already present on the article."""
    import urllib.request
    import re as _re
    fields, _ = _fields(code)
    urls = [u.strip() for u in _re.split(r"[,\s]+", str(fields.get("Снимки") or ""))
            if u.strip().startswith("http")][:max_images]
    if not urls:
        return 0, None
    try:
        have = {f.get("name") for f in b.call("Files_getlist",
                {"obj_type": "articles", "obj_id": str(article_id)})}
    except Exception:
        have = set()
    up = 0
    err = None
    for i, url in enumerate(urls):
        fn = url.rsplit("/", 1)[-1].split("?")[0] or f"img{i}.jpg"
        if not _re.search(r"\.(jpe?g|png|webp|gif)$", fn, _re.I):
            fn += ".jpg"
        if fn in have:
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                img = r.read()
            b.upload_image(article_id, img, fn)
            up += 1
        except Exception as e:
            err = f"{fn}: {str(e)[:80]}"
    return up, err


def delete_test_products(keep_ids=(16,), do_write=False):
    """Remove the earlier pilot/test articles (owner-authorised cleanup 2026-07-19).
    HARD delete (Articles_delete removes the row) — a full backup is taken first so any
    of these can be re-created from it. Deletes children (parent_id set) before parents.
    Keeps `keep_ids` (Barsy system defaults, e.g. 16 'Авансово плащане')."""
    import json as _json
    import pathlib
    arts = b.call("Articles_getlist", {"filters": {}})
    victims = [a for a in arts if a["article_id"] not in keep_ids]
    # backup EVERYTHING we're about to delete (full record + details)
    bak = {"ts": "2026-07-19", "articles": []}
    for a in victims:
        rec = dict(a)
        try:
            rec["_details"] = b.call("Articledetails_get", {"article_id": a["article_id"]})
        except Exception:
            rec["_details"] = None
        bak["articles"].append(rec)
    p = pathlib.Path("barsy_delete_backup.json")
    p.write_text(_json.dumps(bak, ensure_ascii=False, indent=1), encoding="utf-8")
    # children first (those with a parent_id), then parents
    order = sorted(victims, key=lambda a: 0 if a.get("parent_id") else 1)
    print(f"backup: {p} ({len(victims)} articles). keeping ids {list(keep_ids)}.")
    if not do_write:
        print("DRY-RUN — pass --push --confirm to actually delete.")
        for a in order[:5]:
            print(f"  would delete {a['article_id']} code={a.get('code')} {a['article_name'][:40]}")
        print(f"  ... {len(order)} total")
        return
    ok = fail = 0
    for a in order:
        try:
            b.call("Articles_delete", {"article_id": a["article_id"]})
            ok += 1
        except b.BarsyError as e:
            fail += 1
            print(f"  FAIL {a['article_id']} ({a.get('code')}): {str(e)[:120]}")
    left = b.call("Articles_getlist", {"filters": {}})
    print(f"deleted {ok}, failed {fail}. remaining articles: {len(left)} "
          f"({[x['article_name'] for x in left][:5]})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["plan", "push", "delete-test"])
    ap.add_argument("--code", action="append", help="restrict to these codes")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--push", action="store_true", help="actually call the API (writes)")
    ap.add_argument("--confirm", action="store_true", help="required with --push")
    ap.add_argument("--images", action="store_true", help="also upload product images")
    a = ap.parse_args()

    if a.action == "delete-test":
        delete_test_products(do_write=(a.push and a.confirm))
        return

    catalog = _catalog()
    bc = _barcodes()
    if a.code:
        codes = a.code
    else:
        # default candidate set: in-Barsy products we can enrich (have barcode or attrs)
        codes = [c for c in catalog if bc.get(c) or _fields(c)[0].get("Атрибути")][:a.limit]

    writing = a.action == "push" and a.push and a.confirm
    if a.action == "push" and not writing:
        print("REFUSING to write: `push` needs both --push and --confirm. Showing dry-run.\n")

    for code in codes:
        mode, body = build(code, catalog, bc)
        art = body["article"]
        gaps = [k for k in ("barcode", "details", "article_name_ml", "description_ml")
                if k in art]
        print(f"[{mode}] code={code} article_id={body.get('article_id','-')} "
              f"setting={gaps}")
        if a.action == "plan":
            print(json.dumps(body, ensure_ascii=False, indent=1)[:1400])
            print("-" * 60)
            continue
        if not writing:
            continue
        method = "Articles_update" if mode == "update" else "Articles_create"
        try:
            out = b.call(method, body)
            print(f"   -> {method} OK: {json.dumps(out, ensure_ascii=False)[:300]}")
            aid = body.get("article_id") or (out if isinstance(out, int)
                                             else (out.get("article_id") if isinstance(out, dict) else None))
            if a.images and aid:
                up, err = push_images(code, aid)
                print(f"   -> images: uploaded {up}" + (f", err {err}" if err else ""))
        except b.BarsyError as e:
            print(f"   -> {method} FAIL: {e}")


if __name__ == "__main__":
    main()
