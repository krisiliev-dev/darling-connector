# -*- coding: utf-8 -*-
"""Launch-readiness scorecard — the deterministic gate that answers 'how many products are
actually ready for Shopify, and what's blocking the rest?'. Runs over the DB canonical
records + image map + source prices, checks the hard requirements, and prints a dashboard.

A product is LAUNCH-READY when ALL critical checks pass:
  name · brand · usable image · category attributes · sane price · no fabrication flag ·
  not still-flagged-for-review.
"""
import json, collections
from pathlib import Path

HERE = Path(__file__).parent


def _image_status():
    p = HERE.parent / "image-pipeline" / "image_map.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def check(code, rec, task, img):
    """Return {check: ok_bool} for one product. Critical checks gate launch."""
    f = rec.get("fields") or {}
    src = (task or {}).get("product") or {}
    attrs = str(f.get("Атрибути") or "")
    qflags = [x[0] for x in ((rec.get("meta") or {}).get("quality_flags") or [])]
    im = img.get(str(code)) or {}
    price = src.get("Цена")
    return {
        "name": bool(str(f.get("Наименование") or "").strip()),
        "brand": bool(str(f.get("Бранд") or "").strip()),
        "image": im.get("usable") is True,
        "attributes": bool(attrs.strip()) and ("цвят" in attrs.lower() or "материал" in attrs.lower()),
        "price": price is not None and str(price).strip() not in ("", "0", "0.0"),
        "no_fabrication": "fabrication" not in qflags,
        "not_flagged": not rec.get("needs_human"),
    }


CRITICAL = ("name", "brand", "image", "attributes", "price", "no_fabrication", "not_flagged")


def main():
    import db
    canon = db.canonical_records()
    tasks = db.get_tasks(list(canon))
    img = _image_status()

    ready = 0
    blockers = collections.Counter()
    per_missing = collections.Counter()
    for code, rec in canon.items():
        res = check(code, rec, tasks.get(code), img)
        missing = [k for k in CRITICAL if not res[k]]
        if not missing:
            ready += 1
        else:
            per_missing[len(missing)] += 1
            for k in missing:
                blockers[k] += 1

    n = len(canon)
    print(f"=== LAUNCH READINESS (of {n} enriched; {14159 - n} not yet enriched) ===")
    print(f"READY for Shopify: {ready} ({100 * ready // max(n, 1)}%)")
    print(f"NOT ready: {n - ready}\n")
    print("Top blockers (products missing each requirement):")
    for k, c in blockers.most_common():
        print(f"  {k:16s} {c:5d} ({100 * c // max(n, 1)}%)")
    print("\nProducts by # of blockers:")
    for nm in sorted(per_missing):
        print(f"  missing {nm}: {per_missing[nm]}")
    # persist a small summary table
    try:
        con = db.connect()
        con.execute("CREATE TABLE IF NOT EXISTS launch_readiness(code TEXT PRIMARY KEY, ready INTEGER, blockers TEXT)")
        rows = []
        for code, rec in canon.items():
            res = check(code, rec, tasks.get(code), img)
            miss = [k for k in CRITICAL if not res[k]]
            rows.append((str(code), 0 if miss else 1, ",".join(miss)))
        con.executemany("INSERT OR REPLACE INTO launch_readiness(code,ready,blockers) VALUES(?,?,?)", rows)
        con.commit(); con.close()
        print(f"\npersisted readiness for {len(rows)} products -> DB table launch_readiness")
    except Exception as e:
        print("persist skipped:", str(e)[:60])


if __name__ == "__main__":
    main()
