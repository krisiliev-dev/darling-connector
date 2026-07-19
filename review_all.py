# -*- coding: utf-8 -*-
"""Full-coverage, CONVERGING reviewer (option B). Reviews EVERY product exactly once, then
locks it — re-reviewing only when the product's content OR the category's filter schema
changes. This gives 'review everything' without burning quota forever.

State lives in DB table review_state(code, sig, reviewed_ts, ready, verdict). A product is
LOCKED when its current signature (fields + category schema fingerprint) matches the stored
one. The reviewer still promotes/demotes piles: apply_fixes auto-applies safe fixes and the
verdict updates needs_human, so products flow both ways as they're reviewed.

  python review_all.py --report        # coverage only (free, no LLM)
  python review_all.py [N]             # review the next N un-reviewed/changed (default 15)
"""
import hashlib, json, sys, time
from pathlib import Path

HERE = Path(__file__).parent
_KEYS = ("Наименование", "Описание", "Бранд", "Категории", "Атрибути", "Синоними",
         "Свързани", "Мета наименование", "Мета описание", "Тегло (кг)")


def signature(rec, cats=None):
    """Content + schema fingerprint. Changes when the product OR its category's filter
    schema changes -> triggers a re-review; otherwise the product stays locked.
    `cats` lets callers load the schema ONCE (coverage() calls this 14k times — reloading
    the ~1MB store per call was minutes of pure parsing + a huge wipe-risk window)."""
    f = rec.get("fields") or {}
    blob = json.dumps({k: f.get(k) for k in _KEYS}, ensure_ascii=False, sort_keys=True)
    try:
        import filter_schema_store as fss
        if cats is None:
            cats = fss.load()
        cat_full = str(f.get("Категории") or "").strip()
        # schema keys can be COMPOUND ("A; B") — try the full string first, then the first
        # part; otherwise compound-key categories were never fingerprint-invalidated.
        key = cat_full if cat_full in cats else cat_full.split(";")[0].strip()
        sfp = fss.category_fingerprint(key, cats)
    except Exception:
        sfp = ""
    return hashlib.md5((blob + "|" + sfp).encode("utf-8")).hexdigest()[:12]


def _chunk_canon(db, codes):
    """Canonical FULL records for just these codes (avoids re-parsing all 14k per chunk)."""
    out = {}
    con = db.connect()
    try:
        q = "SELECT code, record_json FROM products WHERE code IN (%s)" % ",".join("?" * len(codes))
        for code, rj in con.execute(q, [str(c) for c in codes]).fetchall():
            if rj:
                try:
                    out[str(code)] = json.loads(rj)
                except Exception:
                    pass
    finally:
        con.close()
    return out


def _ensure(con):
    con.execute("""CREATE TABLE IF NOT EXISTS review_state(
        code TEXT PRIMARY KEY, sig TEXT, reviewed_ts TEXT, ready INTEGER, verdict TEXT)""")


def coverage():
    import db
    import filter_schema_store as fss
    con = db.connect(); _ensure(con)
    stamped = {r[0]: r[1] for r in con.execute("SELECT code, sig FROM review_state").fetchall()}
    human = {r[0] for r in con.execute("SELECT code FROM review_state WHERE verdict LIKE 'human_%'").fetchall()}
    con.close()
    canon = db.canonical_records()
    cats = fss.load()                                   # once, not 14k times
    todo = [c for c, r in canon.items()
            if c not in human and stamped.get(c) != signature(r, cats)]
    locked = len(canon) - len(todo)
    return canon, todo, locked, stamped


def report():
    canon, todo, locked, stamped = coverage()
    import db
    con = db.connect(); _ensure(con)
    ready = con.execute("SELECT COUNT(*) FROM review_state WHERE ready=1").fetchone()[0]
    con.close()
    print(f"=== REVIEW COVERAGE (option B) ===")
    print(f"enriched products: {len(canon)}")
    print(f"reviewed & locked (unchanged since review): {locked}")
    print(f"need review (new or changed): {len(todo)}")
    print(f"marked ready-for-site by reviewer so far: {ready}")


def run(limit=15, shard=None):
    """shard='i/n' -> review only codes with md5(code)%n==i, so a FLEET of concurrent
    instances covers disjoint slices instead of re-reviewing the same head of the queue."""
    import db
    import review_agent as ra
    canon, todo, locked, stamped = coverage()
    if shard:
        import hashlib
        i, n = (int(x) for x in shard.split("/"))
        todo = [c for c in todo if int(hashlib.md5(str(c).encode()).hexdigest(), 16) % n == i]
    print(f"{len(canon)} products | {locked} locked | {len(todo)} need review"
          + (f" in shard {shard}" if shard else "") + f"; doing {min(limit, len(todo))}")
    batch = todo[:limit]
    if not batch:
        print("nothing to review — all caught up."); return
    ra.review_one._cache.update(records=ra.load_records(), sources=ra.load_sources(),
                                manifest=ra.load_manifest())
    # INCREMENTAL: apply fixes + stamp review_state per CHUNK, not once at the end of the
    # whole batch — a crash hours into a 400-batch must not lose the reviewed work.
    CHUNK = 10
    total_ready = done = 0
    for start in range(0, len(batch), CHUNK):
        chunk = batch[start:start + CHUNK]
        try:
            import run_one as _ro
            _ro._BUDGET_SPENT = None                   # refresh spend-cap view each chunk
        except Exception:
            pass
        results = []
        for i, code in enumerate(chunk):
            print(f"[{start + i + 1}/{len(batch)}] {code}", flush=True)
            try:
                results.append(ra.review_one(code))
            except Exception as e:
                results.append({"code": code, "error": str(e)[:80]})
        try:
            ra.apply_fixes(results)                     # auto-apply safe fixes + log proposals
        except Exception as e:
            print(f"  apply_fixes error: {str(e)[:80]}", flush=True)
        # Stamp ONLY genuine reviews (an errored review must be retried next run, not
        # locked), fetch just this chunk's canonicals (not a 14k re-parse per chunk), and
        # NEVER stamp content the reviewer didn't see: if a foreign writer (lane/curator)
        # produced the current canonical mid-review, leave the product unstamped so it
        # re-queues.
        import filter_schema_store as _fss
        cats = _fss.load()
        canon2 = _chunk_canon(db, chunk)
        con = db.connect(); _ensure(con)
        # HUMAN VERDICTS ARE SACRED: the LLM reviewer must never overwrite a human's
        # approve/reject stamp (a re-queued product previously let INSERT OR REPLACE
        # silently replace the human decision).
        human = {r[0] for r in con.execute(
            "SELECT code FROM review_state WHERE verdict LIKE 'human_%'").fetchall()}
        for code, v in zip(chunk, results):            # code from the batch, not the result
            if not v or v.get("error"):
                continue
            if str(code) in human:
                continue
            rec = canon2.get(code)
            if rec is None:
                continue
            notes = [str(n) for n in ((rec.get("meta") or {}).get("notes") or [])]
            reviewed_src = canon.get(code) or {}
            same = rec.get("ts") == reviewed_src.get("ts")
            fixed_by_us = any(n.startswith("reviewer_autofix") for n in notes)
            if not (same or fixed_by_us):
                continue                                # foreign write mid-review -> re-queue
            vr = (v or {}).get("verdict") or {}
            rd = 1 if vr.get("готов_за_сайта") is True else 0
            total_ready += rd
            con.execute("INSERT OR REPLACE INTO review_state(code,sig,reviewed_ts,ready,verdict) VALUES(?,?,?,?,?)",
                        (code, signature(rec, cats), time.strftime("%Y-%m-%dT%H:%M:%S"), rd, str(vr.get("оценка"))[:200]))
        con.commit(); con.close()
        done += len(chunk)
        print(f"  -- chunk saved: {done}/{len(batch)} reviewed, {total_ready} ready so far --", flush=True)
    print(f"reviewed {done} | ready-for-site this batch: {total_ready}")


if __name__ == "__main__":
    if "--report" in sys.argv:
        report()
    else:
        n = next((int(a) for a in sys.argv[1:] if a.isdigit()), 15)
        sh = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--shard=")), None)
        run(n, shard=sh)
