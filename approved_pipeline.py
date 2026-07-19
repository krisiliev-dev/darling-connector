# -*- coding: utf-8 -*-
"""Approved → Barsy → Shopify automation (owner 2026-07-19).

The end of the pipeline: for every human-APPROVED product, create/update it in Barsy (the
system of record) and then sync it to Shopify (as DRAFT) + the Cloudflare search index. Both
steps are idempotent, so this is safe to run on a schedule; it only (re)processes a code when
it's newly approved or its enriched record changed since the last sync.

State: store_synced.jsonl — {code, sig, barsy_mode, shopify_id, ts}. `sig` = a hash of the
record so a re-enriched approved product re-syncs automatically.

  python approved_pipeline.py --status
  python approved_pipeline.py            # dry-run: list what WOULD sync
  python approved_pipeline.py --run       # do it (writes to Barsy + Shopify)
  python approved_pipeline.py --run --limit 20
"""
import hashlib
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
STATE = HERE / "store_synced.jsonl"


def _sig(rec):
    f = json.dumps((rec.get("fields") or {}), ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(f.encode("utf-8")).hexdigest()[:16]


def _synced():
    """{code: sig} of what's already been pushed (last-line-wins)."""
    out = {}
    if STATE.exists():
        for ln in STATE.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(ln)
                out[str(d["code"])] = d.get("sig")
            except Exception:
                continue
    return out


def _record_synced(code, sig, barsy_mode, shopify_id):
    with STATE.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"code": code, "sig": sig, "barsy_mode": barsy_mode,
                            "shopify_id": shopify_id,
                            "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}, ensure_ascii=False) + "\n")


def _pending():
    """Approved codes whose record changed (or never synced). Returns [(code, rec, sig)]."""
    import db
    import barsy_collect as bcol
    approved = bcol._approved()                 # {code: approved_fields} latest action=approve
    synced = _synced()
    out = []
    for code in approved:
        rec = db.get_record(code) or {}
        if not rec.get("fields"):
            continue
        sig = _sig(rec)
        if synced.get(code) != sig:
            out.append((code, rec, sig))
    return out


def run(do_write=False, limit=None):
    import barsy_push
    import barsy_shopify_sync as sync
    pending = _pending()
    if limit:
        pending = pending[:limit]
    print(f"approved & pending sync: {len(pending)}", flush=True)
    if not do_write:
        for code, rec, _sg in pending[:25]:
            nm = (rec.get("fields") or {}).get("Наименование") or ""
            print(f"  would sync {code}: {nm[:50]}")
        if not pending:
            print("  (nothing pending — all approved products are in sync)")
        else:
            print("  (dry-run — pass --run to push to Barsy + Shopify)")
        return

    catalog = barsy_push._catalog()
    bc = barsy_push._barcodes()
    ok = fail = 0
    for code, rec, sig in pending:
        try:
            mode, aid = barsy_push.push_one(code, catalog, bc)          # -> Barsy
            res = sync.sync_code(code, do_write=True)                    # -> Shopify (+ CF search)
            sid = res.get("product_id", "")
            _record_synced(code, sig, mode, sid)
            ok += 1
            print(f"  OK {code}: Barsy={mode} article={aid} | Shopify={sid.rsplit('/',1)[-1]}",
                  flush=True)
        except Exception as e:
            fail += 1
            print(f"  FAIL {code}: {str(e)[:150]}", flush=True)
    print(f"done: synced {ok}, failed {fail}", flush=True)


def status():
    synced = _synced()
    pending = _pending()
    print(f"already synced to store: {len(synced)} | approved & pending: {len(pending)}")


if __name__ == "__main__":
    if "--status" in sys.argv:
        status()
    else:
        lim = None
        if "--limit" in sys.argv:
            lim = int(sys.argv[sys.argv.index("--limit") + 1])
        run(do_write="--run" in sys.argv, limit=lim)
