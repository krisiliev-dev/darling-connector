# -*- coding: utf-8 -*-
"""Shopify import builder — DRY RUN. Transforms enriched products into Shopify
`productSet` (GraphQL Admin 2026-04) payloads and writes them for review. It does NOT
touch the store — actually creating products is a separate, explicitly-gated step.

Mapping (per the migration plan):
  title         <- enriched Наименование
  descriptionHtml<- enriched Описание (HTML)
  vendor        <- Бранд
  category      <- category_shopify_map.json (BG Категории -> Shopify taxonomy gid)
  productType   <- BG leaf category
  tags          <- collection tags (кухня/баня/…) + Синоними (BG search) + 'lady-d' hooks
  price         <- SOURCE 'Цена' (Microinvest Продажна цена, VERBATIM — never AI-touched)
  inventory     <- SOURCE 'Количество'
  seo           <- Мета наименование / Мета описание
  images        <- image manifest (downloaded files) — upload strategy noted in the plan
  metafields    <- darling.old_url (redirects), code

Usage:  python shopify_export.py [N]   (default: all; writes shopify_payloads.jsonl)
"""
import json, sys, re
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "shopify_payloads.jsonl"
CATMAP = json.loads((HERE / "category_shopify_map.json").read_text(encoding="utf-8"))
_CAT_BY_BG = {c.get("bg"): c for c in CATMAP if c.get("bg")}

# BG category keyword -> auto-collection tag (mirrors the 11 store collections).
_COLLECTION_KEYWORDS = [
    ("кухн", "кухня"), ("готв", "кухня"), ("прибор", "кухня"), ("тенджер", "кухня"),
    ("баня", "баня"), ("тоалет", "баня"),
    ("декор", "декорация"), ("ваз", "декорация"), ("свещ", "декорация"), ("рамк", "декорация"),
    ("текстил", "текстил"), ("покривк", "текстил"), ("възглав", "текстил"), ("хавлия", "текстил"),
    ("градин", "градина"), ("саксия", "градина"), ("цветар", "градина"),
    ("почист", "почистване"), ("кош", "почистване"), ("метл", "почистване"),
    ("парти", "парти"), ("празни", "парти"),
    ("дет", "деца"), ("бебе", "деца"),
    ("подар", "подаръци"),
]


def _collection_tags(bg_cat, name):
    blob = (str(bg_cat or "") + " " + str(name or "")).lower()
    tags = {tag for kw, tag in _COLLECTION_KEYWORDS if kw in blob}
    return sorted(tags)


def _tags(rec_fields, bg_leaf):
    name = rec_fields.get("Наименование") or ""
    tags = set(_collection_tags(bg_leaf, name))
    for syn in re.split(r"[,;]+", str(rec_fields.get("Синоними") or "")):
        s = syn.strip()
        if 2 < len(s) <= 40:
            tags.add(s)
    return sorted(tags)


def _category(bg_cat):
    # BG path 'A -> B' : use the leaf; map to Shopify taxonomy gid if known.
    leaf = str(bg_cat or "").split("->")[-1].strip()
    m = _CAT_BY_BG.get(leaf) or _CAT_BY_BG.get(str(bg_cat or "").strip())
    return leaf, (m or {}).get("shopify_id")


def build_payload(code, rec, task, manifest):
    f = rec.get("fields") or {}
    src = (task or {}).get("product") or {}
    leaf, cat_gid = _category(f.get("Категории"))
    price = src.get("Цена")                            # EMPIRIC — verbatim, never AI-touched
    qty = src.get("Количество")
    img = manifest.get(str(code))
    payload = {
        "code": code,
        "input": {
            "title": f.get("Наименование") or src.get("Наименование"),
            "descriptionHtml": f.get("Описание") or src.get("Описание") or "",
            "vendor": f.get("Бранд") or None,
            "productType": leaf,
            "category": cat_gid,
            "tags": _tags(f, f.get("Категории")),
            "status": "DRAFT",                         # import as DRAFT; owner publishes
            "seo": {"title": f.get("Мета наименование"), "description": f.get("Мета описание")},
            "metafields": [
                {"namespace": "darling", "key": "code", "type": "single_line_text_field",
                 "value": str(code)},
            ],
        },
        "price": None if price is None else str(price),
        "inventory": None if qty is None else int(float(qty)),
        "image_file": (img or {}).get("file"),
        "image_ok": (img or {}).get("status") == "ok",
    }
    return payload


def main():
    import db
    limit = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else None
    canon = db.canonical_records()
    # APPROVAL GATE (owner requirement: human reviews everything before launch).
    # Default: export ONLY products marked ready in review_state (reviewer-passed or
    # human-approved). '--all' overrides for dry-run inspection of the full catalog.
    if "--all" not in sys.argv:
        con = db.connect()
        try:
            ready = {r[0] for r in con.execute(
                "SELECT code FROM review_state WHERE ready=1 "
                "AND verdict='human_approve'").fetchall()}
            if not ready:
                raise SystemExit("review_state has NO human-approved products — "
                                 "nothing to export (use --all to override the gate)")
        except Exception:
            ready = set()
        finally:
            con.close()
        before = len(canon)
        canon = {c: r for c, r in canon.items() if c in ready}
        print(f"approval gate: {len(canon)}/{before} products are review-approved "
              f"(use --all to export everything for dry-run inspection)")
    codes = list(canon)[:limit] if limit else list(canon)
    tasks = db.get_tasks(codes)
    manifest = {}
    mp = HERE.parent / "image-pipeline" / "manifest.jsonl"
    if mp.exists():
        for line in open(mp, encoding="utf-8", errors="replace"):
            if line.strip():
                try:
                    d = json.loads(line)
                    manifest[str(d.get("code"))] = d
                except Exception:
                    pass
    n = 0
    stats = {"with_price": 0, "with_image": 0, "with_category_gid": 0, "with_vendor": 0}
    with open(OUT, "w", encoding="utf-8") as out:
        for code in codes:
            p = build_payload(code, canon[code], tasks.get(code), manifest)
            out.write(json.dumps(p, ensure_ascii=False) + "\n")
            n += 1
            stats["with_price"] += p["price"] is not None
            stats["with_image"] += bool(p["image_ok"])
            stats["with_category_gid"] += p["input"]["category"] is not None
            stats["with_vendor"] += p["input"]["vendor"] is not None
    print(f"built {n} Shopify payloads (DRY RUN) -> {OUT.name}")
    print("coverage:", {k: f"{v} ({100*v//max(n,1)}%)" for k, v in stats.items()})
    if n:
        sample = json.loads(open(OUT, encoding="utf-8").readline())
        print("\nsample payload:\n" + json.dumps(sample, ensure_ascii=False, indent=1)[:900])


if __name__ == "__main__":
    main()
