# -*- coding: utf-8 -*-
"""Semantic-search sync — builds the /upsert payloads for the Cloudflare 'darling-search'
worker (Vectorize index 'darling-products', model @cf/baai/bge-m3, 1024 dims) so on-site
search works at launch.

Per the migration plan, on every product create/update the pipeline POSTs to /upsert; the
embedding text = title + collections + tags + description[:300]. This module builds those
payloads from the enriched catalogue.

DRY-RUN by default (writes search_payloads.jsonl for review). The LIVE push is deferred to
launch — it needs the SYNC_KEY and should run only AFTER human review + Shopify import (so
ids/handles match Shopify). Push guarded, custom User-Agent (Cloudflare edge 403s the
default urllib UA), batched.

  python shopify_search_sync.py [N]            # dry-run: build payloads
  python shopify_search_sync.py --push KEY     # live upsert (post-launch only)
"""
import json, re, sys, urllib.request
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "search_payloads.jsonl"
WORKER = "https://darling-search.darling7.workers.dev"
UA = "darling-pipeline/1.0"                             # NOT default urllib UA (edge 403)
BATCH = 100

_TR = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ж": "zh", "з": "z",
       "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p",
       "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts", "ч": "ch",
       "ш": "sh", "щ": "sht", "ъ": "a", "ь": "y", "ю": "yu", "я": "ya"}


def slugify(text, code):
    s = "".join(_TR.get(c, c) for c in str(text or "").lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s[:60] or "product") + "-" + str(code)


def build_payloads(limit=None):
    import db
    import shopify_export as se
    canon = db.canonical_records()
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
    out = []
    for code in codes:
        rec = canon[code]
        f = rec.get("fields") or {}
        sp = se.build_payload(code, rec, tasks.get(code), manifest)
        tags = sp["input"]["tags"]
        collections = se._collection_tags(f.get("Категории"), f.get("Наименование"))
        desc_plain = re.sub(r"<[^>]+>", " ", str(f.get("Описание") or ""))
        desc_plain = re.sub(r"\s+", " ", desc_plain).strip()[:300]
        title = f.get("Наименование") or ""
        text = " · ".join(x for x in [title, ", ".join(collections), ", ".join(tags), desc_plain] if x)
        out.append({
            "id": str(code),
            "handle": slugify(title, code),            # provisional; finalized at Shopify import
            "title": title,
            "text": text,
            "price": sp["price"],
            "image": (manifest.get(str(code)) or {}).get("file"),
        })
    return out


def push(payloads, key):
    """Live upsert in batches. Post-launch only."""
    ok = 0
    for i in range(0, len(payloads), BATCH):
        batch = payloads[i:i + BATCH]
        body = json.dumps({"products": batch}).encode("utf-8")
        req = urllib.request.Request(WORKER + "/upsert", data=body, method="POST",
                                     headers={"Content-Type": "application/json",
                                              "User-Agent": UA, "X-Sync-Key": key})
        try:
            r = urllib.request.urlopen(req, timeout=30)
            ok += len(batch)
            print(f"  upserted {ok}/{len(payloads)} (HTTP {r.status})")
        except Exception as e:
            print(f"  batch {i} FAILED: {str(e)[:100]}")
    print("NOTE: Vectorize mutations are async (~1-3 min to become queryable).")


def main():
    if "--push" in sys.argv:
        idx = sys.argv.index("--push")
        key = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else ""
        if not key:
            print("push needs a SYNC_KEY: --push <KEY>"); return
        payloads = build_payloads()
        print(f"LIVE upsert of {len(payloads)} products to {WORKER}/upsert ...")
        push(payloads, key)
        return
    limit = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else None
    payloads = build_payloads(limit)
    with open(OUT, "w", encoding="utf-8") as f:
        for p in payloads:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f"built {len(payloads)} search payloads (DRY RUN) -> {OUT.name}")
    if payloads:
        s = payloads[0]
        print(f"\nsample:\n  id={s['id']} handle={s['handle']}\n  text={s['text'][:180]}...")


if __name__ == "__main__":
    main()
