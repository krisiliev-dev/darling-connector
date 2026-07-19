# -*- coding: utf-8 -*-
"""Google Cloud Vision logo/web detection — brand evidence source with a HARD free-quota
guard (owner 2026-07-18: "make sure we don't go over the free quota").

Free tier: 1,000 units per FEATURE per month. Guard: gcv_usage.json counts units per
feature per month; any call that would push a feature past CAP (900, margin under
1,000) raises QuotaStop BEFORE the request is sent. Responses cache forever in
gcv_cache.jsonl — a product is never billed twice.

  python gcv_brand.py URL          # one-off: logo detection on an image URL
  python gcv_brand.py --report     # usage + cache stats
"""
import json
import time
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
USAGE = HERE / "gcv_usage.json"
CACHE = HERE / "gcv_cache.jsonl"
CAP = 900


class QuotaStop(RuntimeError):
    pass


def _key():
    for line in open(Path.home() / ".hermes" / ".env", encoding="utf-8"):
        if line.startswith("GCV_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("GCV_KEY not in ~/.hermes/.env")


def _usage():
    """{month, units:{feature: n}} read from the DB (atomic source of truth)."""
    import db
    month = time.strftime("%Y-%m")
    con = db.connect()
    try:
        con.execute("CREATE TABLE IF NOT EXISTS gcv_usage("
                    "month TEXT, feature TEXT, units INTEGER, "
                    "PRIMARY KEY(month, feature))")
        rows = con.execute("SELECT feature, units FROM gcv_usage WHERE month=?",
                           (month,)).fetchall()
    finally:
        con.close()
    return {"month": month, "units": {f: u for f, u in rows}}


def _spend(features):
    """Atomically reserve quota units or refuse — BEGIN IMMEDIATE serializes the
    check+increment across all 12 lane processes, so the free-tier cap cannot be
    blown by a read-modify-write race (a JSON-file counter was not atomic)."""
    import db
    month = time.strftime("%Y-%m")
    con = db.connect()
    try:
        con.execute("CREATE TABLE IF NOT EXISTS gcv_usage("
                    "month TEXT, feature TEXT, units INTEGER, "
                    "PRIMARY KEY(month, feature))")
        con.commit()
        con.execute("BEGIN IMMEDIATE")
        for f in features:
            r = con.execute("SELECT units FROM gcv_usage WHERE month=? AND feature=?",
                            (month, f)).fetchone()
            if r and r[0] + 1 > CAP:
                con.rollback()
                raise QuotaStop(f"{f}: {r[0]}/{CAP} units used this month")
        for f in features:
            con.execute("INSERT INTO gcv_usage VALUES (?,?,1) "
                        "ON CONFLICT(month, feature) DO UPDATE SET units = units + 1",
                        (month, f))
        con.commit()
    finally:
        con.close()


def _cache():
    out = {}
    if CACHE.exists():
        for ln in CACHE.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                d = json.loads(ln)
                out[d["img"]] = d
            except Exception:
                pass
    return out


def annotate(img_url, features=("LOGO_DETECTION",)):
    """Cached Vision annotate. Returns {logos: [(desc, score)], web_entities: [...],
    best_guess: str}. Raises QuotaStop at the free-tier guard."""
    hit = _cache().get(img_url)
    if hit and set(hit.get("features") or []) >= set(features):
        return hit["result"]
    _spend(features)
    body = json.dumps({"requests": [{
        "image": {"source": {"imageUri": img_url}},
        "features": [{"type": f, "maxResults": 10} for f in features]}]}).encode()
    req = urllib.request.Request(
        "https://vision.googleapis.com/v1/images:annotate?key=" + _key(),
        data=body, headers={"Content-Type": "application/json"})
    resp = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))
    r = (resp.get("responses") or [{}])[0]
    if r.get("error"):
        raise RuntimeError(str(r["error"])[:200])
    out = {
        "logos": [(l.get("description"), round(l.get("score", 0), 3))
                  for l in r.get("logoAnnotations") or []],
        "web_entities": [(e.get("description"), round(e.get("score", 0), 2))
                         for e in (r.get("webDetection") or {}).get("webEntities") or []
                         if e.get("description")][:10],
        "best_guess": next((b.get("label") for b in
                            (r.get("webDetection") or {}).get("bestGuessLabels") or []), None),
    }
    with CACHE.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"img": img_url, "features": list(features), "result": out,
                             "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                            ensure_ascii=False) + "\n")
    return out


def logo_candidate(img_url):
    """Brand-evidence hook for brand_tools.gather: highest-score logo >= 0.5, else None."""
    try:
        r = annotate(img_url, ("LOGO_DETECTION",))
    except Exception:            # incl. QuotaStop: no evidence is just no evidence
        return None
    logos = [l for l in r.get("logos") or [] if l[1] >= 0.5]
    return logos[0][0] if logos else None


if __name__ == "__main__":
    if "--report" in sys.argv:
        u = _usage()
        print("month:", u["month"], "| units:", u["units"] or "none",
              "| cap:", CAP, "per feature | cached:", len(_cache()))
    else:
        url = sys.argv[1]
        print(json.dumps(annotate(url, ("LOGO_DETECTION", "WEB_DETECTION")),
                         ensure_ascii=False, indent=1))
