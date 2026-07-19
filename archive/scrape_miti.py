# -*- coding: utf-8 -*-
"""Scrape mitibg.com (supplier, WooCommerce) — code (SKU), name, images, description,
price — into miti_products.jsonl. Polite: 1 req/sec, resumable (skips already-scraped
URLs). robots.txt allows product pages.

  python scrape_miti.py            # full crawl via the product sitemaps
"""
import json
import re
import ssl
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "miti_products.jsonl"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) darling-catalog/1.0"}
CTX = ssl.create_default_context()


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout, context=CTX).read().decode(
        "utf-8", "replace")


def product_urls():
    idx = fetch("https://mitibg.com/sitemap_index.xml")
    maps = re.findall(r"<loc>(https://mitibg\.com/post-type-product-sitemap-\d+\.xml)</loc>", idx)
    urls = []
    for m in maps:
        urls += re.findall(r"<loc>([^<]+)</loc>", fetch(m))
        time.sleep(0.5)
    return [u for u in urls if "/produkt/" in u]


def parse(html):
    out = {}
    # JSON-LD product blocks (Yoast/Woo emit these)
    for m in re.finditer(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',
                         html, re.S):
        try:
            d = json.loads(m.group(1))
        except Exception:
            continue
        cands = d if isinstance(d, list) else [d]
        if isinstance(d, dict) and "@graph" in d:
            cands = d["@graph"]
        for c in cands:
            if isinstance(c, dict) and c.get("@type") in ("Product", ["Product"]):
                out["name"] = c.get("name")
                out["sku"] = str(c.get("sku") or "")
                img = c.get("image")
                if isinstance(img, dict):
                    img = img.get("url")
                out["images"] = img if isinstance(img, list) else ([img] if img else [])
                out["description"] = re.sub(r"\s+", " ", str(c.get("description") or ""))[:1500]
                offers = c.get("offers") or {}
                if isinstance(offers, list):
                    offers = offers[0] if offers else {}
                out["price"] = offers.get("price")
    if not out.get("name"):
        m = re.search(r"<h1[^>]*>([^<]+)</h1>", html)
        if m:
            out["name"] = m.group(1).strip()
    if not out.get("sku"):
        m = re.search(r'class="sku"[^>]*>([^<]+)', html)
        if m:
            out["sku"] = m.group(1).strip()
    if not out.get("images"):
        out["images"] = re.findall(r'property="og:image" content="([^"]+)"', html)[:1]
    # gallery images
    gal = re.findall(r'data-large_image="([^"]+)"', html)
    if gal:
        out["images"] = list(dict.fromkeys((out.get("images") or []) + gal))[:8]
    return out


def main():
    done = set()
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                done.add(json.loads(line)["url"])
            except Exception:
                pass
    urls = product_urls()
    todo = [u for u in urls if u not in done]
    print(f"{len(urls)} products on site, {len(todo)} to scrape", flush=True)
    n = 0
    with OUT.open("a", encoding="utf-8") as fh:
        for u in todo:
            try:
                d = parse(fetch(u))
                d["url"] = u
                d["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S")
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
                fh.flush()
                n += 1
                if n % 100 == 0:
                    print(f"  {n}/{len(todo)} scraped", flush=True)
            except Exception as e:
                print(f"  FAIL {u[:80]}: {str(e)[:60]}", flush=True)
            time.sleep(1.0)
    print(f"DONE: {n} scraped -> {OUT.name}", flush=True)


if __name__ == "__main__":
    main()
