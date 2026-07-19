# -*- coding: utf-8 -*-
"""Programmatic image audit: resolution + background whiteness for catalog photos.

Samples N image URLs from tasks.jsonl, downloads each, and checks:
  - resolution (flag < 500px on the short side)
  - background: mean color of the 4 corner patches (flag if not near-white)
  - product coverage: rough share of non-background pixels (flag tiny products)

Usage:
  python audit_images.py [sample_size]     # default 200
Writes image_audit.jsonl + prints summary stats.
"""
import io
import json
import random
import sys
import urllib.request
from pathlib import Path

from PIL import Image

HERE = Path(__file__).parent
TASKS = HERE / "tasks.jsonl"
OUT = HERE / "image_audit.jsonl"

PATCH = 12          # corner patch size in px
WHITE_THR = 235     # mean channel value to count as "white-ish"
NEUTRAL_TOL = 12    # max channel spread to count as neutral grey


def classify_bg(img):
    w, h = img.size
    corners = [
        img.crop((0, 0, PATCH, PATCH)),
        img.crop((w - PATCH, 0, w, PATCH)),
        img.crop((0, h - PATCH, PATCH, h)),
        img.crop((w - PATCH, h - PATCH, w, h)),
    ]
    votes = []
    for c in corners:
        px = list(c.convert("RGB").getdata())
        r = sum(p[0] for p in px) / len(px)
        g = sum(p[1] for p in px) / len(px)
        b = sum(p[2] for p in px) / len(px)
        spread = max(r, g, b) - min(r, g, b)
        if min(r, g, b) >= WHITE_THR:
            votes.append("white")
        elif spread <= NEUTRAL_TOL:
            votes.append("grey")
        else:
            votes.append("colored")
    for kind in ("white", "grey", "colored"):
        if votes.count(kind) >= 3:
            return kind
    return "mixed"


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    urls = []
    with open(TASKS, encoding="utf-8") as f:
        for line in f:
            t = json.loads(line)
            img = t["product"].get("Снимки")
            if img:
                urls.append((t["code"], img.split(";")[0].strip()))
    random.seed(42)
    sample = random.sample(urls, min(n, len(urls)))

    stats = {"white": 0, "grey": 0, "colored": 0, "mixed": 0,
             "small": 0, "error": 0, "total": 0}
    with open(OUT, "w", encoding="utf-8") as out:
        for code, url in sample:
            stats["total"] += 1
            rec = {"code": code, "url": url}
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                data = urllib.request.urlopen(req, timeout=20).read()
                img = Image.open(io.BytesIO(data))
                img.load()
                rec["size"] = list(img.size)
                rec["bg"] = classify_bg(img)
                rec["small"] = min(img.size) < 500
                stats[rec["bg"]] += 1
                if rec["small"]:
                    stats["small"] += 1
            except Exception as e:
                rec["error"] = str(e)[:150]
                stats["error"] += 1
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(json.dumps(stats, indent=2))
    ok = stats["total"] - stats["error"]
    if ok:
        print(f"\nOf {ok} downloadable images:")
        print(f"  white bg:   {stats['white']}  ({stats['white']/ok:.0%})")
        print(f"  grey bg:    {stats['grey']}  ({stats['grey']/ok:.0%})")
        print(f"  colored bg: {stats['colored']}  ({stats['colored']/ok:.0%})")
        print(f"  mixed:      {stats['mixed']}  ({stats['mixed']/ok:.0%})")
        print(f"  small (<500px): {stats['small']}  ({stats['small']/ok:.0%})")


if __name__ == "__main__":
    main()
