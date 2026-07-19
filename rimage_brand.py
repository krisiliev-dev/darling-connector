# -*- coding: utf-8 -*-
"""REVERSE-IMAGE brand discovery (owner pilot 2026-07-18): Google Lens via SerpAPI on
BRANDLESS products — the same manufacturer studio photo on other shops reveals the brand
in their listing titles.

Discipline: responses are CACHED FOREVER (serp_cache.jsonl — a search is never paid
twice); candidates go through brand_tools.gather (gazetteer/corroboration/supplier
gates) — a lone unknown lands in the owner's /brands queue, never auto-applied.

  python rimage_brand.py [N]        # process up to N brandless products (default 15)
  python rimage_brand.py --report   # yield stats from the cache
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
CACHE = HERE / "serp_cache.jsonl"

STOP = {"за", "от", "със", "серия", "комплект", "броя", "инокс", "premium", "нов",
        "new", "set", "the", "and", "with", "for", "professional", "home", "kitchen"}


def _key():
    for line in open(Path.home() / ".hermes" / ".env", encoding="utf-8"):
        if line.startswith("SERPAPI_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("SERPAPI_KEY not in ~/.hermes/.env")


def _cache():
    out = {}
    if CACHE.exists():
        for line in CACHE.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                d = json.loads(line)
                out[d["code"]] = d
            except Exception:
                pass
    return out


def lens(img_url):
    q = urllib.parse.urlencode({"engine": "google_lens", "url": img_url,
                                "hl": "bg", "api_key": _key()})
    req = urllib.request.Request("https://serpapi.com/search.json?" + q)
    return json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))


def titles_from(resp):
    out = []
    for sec in ("exact_matches", "visual_matches"):
        for m in (resp.get(sec) or [])[:12]:
            t = str(m.get("title") or "").strip()
            src = str(m.get("source") or m.get("link") or "")[:60]
            if t:
                out.append((t, src))
    return out[:15]


LLM_PROMPT = """Продуктови обяви от различни онлайн магазини показват СЪЩАТА снимка
като наш продукт "{name}". Ето заглавията им (със сайта):
{titles}

Каква е МАРКАТА НА ПРОИЗВОДИТЕЛЯ на продукта, ако изобщо се разбира?
ВНИМАНИЕ: думи като Bathroom/Glass/Kitchen са описания, НЕ марки. Маркетплейс
псевдо-марки (случайни имена като "Jormftte" от Amazon обяви на генерични стоки)
НЕ са истинската марка на производителя — при такива върни null.
Марка приемай само ако се появява в 2+ обяви от РАЗЛИЧНИ сайтове или е известен
производител на домашни стоки.

Върни САМО валиден JSON: {{"марка": "..." или null, "увереност": "висока"|"ниска"}}"""


def brand_candidates(titles, name=""):
    """LLM judgment over the match titles; returns (brand_or_None, confidence)."""
    if not titles:
        return None, "ниска"
    import run_one
    tl = chr(10).join(f"  - {t}  [{src}]" for t, src in titles)
    try:
        out, _m = run_one.generate_with_chain(
            LLM_PROMPT.format(name=name, titles=tl),
            system="Отговаряй само с валиден JSON.")
        d = run_one.extract_json(out) or {}
    except Exception:
        return None, "ниска"
    b = d.get("марка")
    b = str(b).strip() if b else None
    if b and b.lower() in ("null", "none", "-"):
        b = None
    return b, str(d.get("увереност") or "ниска")


def main(limit=15):
    import db
    import brand_tools
    cache = _cache()
    con = db.connect()
    rows = con.execute(
        "SELECT p.code, p.fields_json, p.record_json FROM products p "
        "WHERE p.record_json IS NOT NULL").fetchall()
    con.close()
    todo = []
    for code, fj, rj in rows:
        code = str(code)
        f = json.loads(fj or "{}")
        if str(f.get("Бранд") or "").strip():
            continue
        rec = json.loads(rj)
        if "v2" not in [str(n) for n in ((rec.get("meta") or {}).get("notes") or [])]:
            continue
        img = str(f.get("Снимки") or "").split(",")[0].strip()
        if not img.startswith("http"):
            continue
        todo.append((code, img, str(f.get("Наименование") or "")))
    fresh = [t for t in todo if t[0] not in cache]
    print(f"{len(todo)} brandless v2 products with images; {len(cache)} cached; "
          f"processing {min(limit, len(fresh))} new", flush=True)
    n_known = n_cand = n_none = 0
    with CACHE.open("a", encoding="utf-8") as fh:
        for code, img, nm in fresh[:limit]:
            try:
                resp = lens(img)
            except Exception as e:
                print(f"  {code}: SERP FAIL {str(e)[:60]}", flush=True)
                continue
            titles = titles_from(resp)
            fh.write(json.dumps({"code": code, "img": img, "titles": titles,
                                 "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                                ensure_ascii=False) + "\n")
            fh.flush()
            b, conf = brand_candidates(titles, nm)
            if b:
                known = brand_tools.lookup(b)
                tag = "GAZETTEER" if known else ("strong" if conf == "висока" else "weak")
                print(f"  {code} {nm[:38]!r}: {tag} -> {known or b}", flush=True)
                if known or conf == "висока":
                    brand_tools.queue_candidate(code, known or b, ["rimage"], nm)
                    n_cand += 1
                else:
                    n_none += 1
            else:
                n_none += 1
                print(f"  {code} {nm[:38]!r}: no brand ({len(titles)} matches)", flush=True)
            time.sleep(1.2)
    print(f"PILOT: {n_known} gazetteer-confirmed, {n_cand} new candidates (queued), "
          f"{n_none} no signal")


if __name__ == "__main__":
    if "--report" in sys.argv:
        c = _cache()
        print(len(c), "cached lens responses")
    else:
        n = next((int(a) for a in sys.argv[1:] if a.isdigit()), 15)
        main(n)
