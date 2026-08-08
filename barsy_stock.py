# -*- coding: utf-8 -*-
"""Initial stock load into Barsy (owner 2026-07-20).

Barsy has NO "set quantity = N" call — stock is DOCUMENT-DRIVEN and ADDITIVE. So we post one
`Storeloads_create` goods-in document per product against the loadable depot, `save_and_close`
to commit it to stock.

IDEMPOTENCY, and what it does and does not promise. Each code is loaded at most once, tracked in
stock_loaded.jsonl — but the ledger line is written BEFORE the Barsy call, not after. That is the
whole point: a goods-in Barsy committed and failed to acknowledge must not look identical to one
that never happened. So a code goes `pending` first and `confirmed` on success, and BOTH block a
re-post. An interrupted load therefore blocks its code until `--reconcile` asks Barsy whether the
document is actually there.

`doc_num` is deterministic (`INIT-{code}`) so the document can be FOUND again. It used to carry
`int(time.time())`, which made every retry a new document — unrejectable and unfindable.

DATA DEPENDENCY: needs real stock quantities. The current Microinvest NOMENCLATURE export has NO
stock column — qty is blank for all rows. The owner must provide a Microinvest наличности/inventory
export (код + количество). Feed it as {code: qty} to sync_all().

COST: Storeloads rows want current_price (delivery/cost). We don't have a cost column, so the
initial load uses 0 (stock counts are correct; avg-cost/profit reporting starts at 0 until real
deliveries post). Change DEFAULT_COST if a cost export becomes available.

  python barsy_stock.py --status
  python barsy_stock.py --load <code> <qty>     # load ONE (test / manual)
  python barsy_stock.py --reconcile             # resolve pending codes against Barsy (dry)
  python barsy_stock.py --reconcile --run       # …and write the verdicts to the ledger
"""
import json
import sys
import time
from pathlib import Path

import barsy_api as b
import barsy_push as bp

HERE = Path(__file__).parent
STATE = HERE / "stock_loaded.jsonl"
DEPOT_ID = 1            # 'Основен', can_load=1 (verified live)
DEFAULT_COST = "0"


def doc_num_for(code):
    """The document number for a code. DETERMINISTIC — the same code always produces the same
    number, so a repeat is findable in Barsy instead of becoming a second document."""
    return f"INIT-{code}"


def _ledger():
    """{code: last record} — append-only file, the LAST line for a code wins.

    A line with no `state` predates this change. The old code appended only after a successful
    call, so those are confirmed; reading them as anything else would strand real loads."""
    out = {}
    if STATE.exists():
        for ln in STATE.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(ln)
            except Exception:
                continue
            code = str(rec.get("code", ""))
            if not code:
                continue
            rec.setdefault("state", "confirmed")
            out[code] = rec
    return out


def _blocked(ledger=None):
    """Codes that must NOT be posted again — confirmed AND pending.

    Pending is the whole reason this exists: "we do not know whether Barsy booked it" is not
    "it did not happen", and only one of those two is safe to act on. Released rows are the
    ones a reconcile has proven absent, so they drop out and become loadable again."""
    led = _ledger() if ledger is None else ledger
    return {c for c, r in led.items() if r.get("state") in ("confirmed", "pending")}


def _loaded():
    """Codes with stock actually booked in Barsy. Reporting only — never gate a write on this;
    gate on _blocked(), which also counts the ones we are unsure about."""
    return {c for c, r in _ledger().items() if r.get("state") == "confirmed"}


def _record(code, article_id, qty, sid, state, doc_num):
    with STATE.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"code": str(code), "article_id": article_id, "qty": qty,
                            "storeload_id": sid, "state": state, "doc_num": doc_num,
                            "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                           ensure_ascii=False) + "\n")


def load_stock(code, article_id, qty, cost=DEFAULT_COST, depot_id=DEPOT_ID):
    """Post a goods-in document for ONE article and commit it. Returns the storeload id.

    The intent is written to the ledger as `pending` BEFORE the call. If anything goes wrong
    after that — timeout, gateway error, killed process — the code stays blocked and
    `--reconcile` decides its fate by asking Barsy. Recording only on success is what made a
    committed-but-unacknowledged load invisible and therefore repeatable."""
    doc_num = doc_num_for(code)
    _record(code, article_id, qty, None, "pending", doc_num)
    sid = b.call("Storeloads_create", {
        "store_load": {"depot_id": depot_id, "doc_date": time.strftime("%Y-%m-%d"),
                       "doc_num": doc_num,
                       # prices are EUR + VAT-inclusive (matches deliveries.py / panel config). Without
                       # these Barsy assumes the ex-VAT system default → wrong booked cost. price_mode
                       # polarity per storeloads/getlist.rst: 0=без ДДС, 1=с ДДС.
                       "currency_id": 1, "price_mode": 1},
        "articles": [{"article_id": int(article_id), "amount": str(qty),
                      "current_price": str(cost)}],
        "action_type": "save_and_close"})
    _record(code, article_id, qty, sid, "confirmed", doc_num)
    return sid


# Storeloads_getlist does NOT carry a document number — measured on the live box 2026-08-08,
# 43/43 rows, with and without depot_id. It returns only barsy_id, depot_id, doc_type_id,
# doc_type_name, status and store_load_id. The number is on the DETAIL call. A list-only probe
# would find nothing and call every pending code `released`, which is the verdict that
# authorises a second goods-in; that exact bug was live in the panel's delivery reconcile.
RECONCILE_SCAN_CAP = 500


def _storeload_doc_num(row):
    """doc_num out of a storeload record, whatever Barsy called it this time."""
    for k in ("doc_num", "docNum", "document_number", "doc_number", "number"):
        v = row.get(k)
        if v not in (None, ""):
            return str(v).strip()
    return ""


def _storeload_id(row):
    for k in ("store_load_id", "storeload_id", "id"):
        v = row.get(k)
        if v not in (None, ""):
            return v
    return None


def _doc_num_index(depot_id=DEPOT_ID):
    """{doc_num: store_load_id} for every storeload, read in full.

    Built COMPLETELY or not at all. A partial index cannot tell "not in Barsy" apart from "in
    the part I could not read", and the first of those is what releases a code for a second
    post. So every failure here raises."""
    rows = b.call("Storeloads_getlist", {"depot_id": depot_id})
    if isinstance(rows, dict):
        rows = rows.get("Storeloads_getlist") or rows.get("data") or rows.get("storeloads") or []
    if not isinstance(rows, list):
        raise RuntimeError(f"Storeloads_getlist returned {type(rows).__name__}, not a list")
    rows = [r for r in rows if isinstance(r, dict)]
    if len(rows) > RECONCILE_SCAN_CAP:
        raise RuntimeError(f"{len(rows)} storeloads is more than the {RECONCILE_SCAN_CAP} this "
                           "can read — check the documents in Barsy by hand")
    index = {}
    unnumbered = 0
    for r in rows:
        num = _storeload_doc_num(r)                  # in case a future build puts it in the list
        sid = _storeload_id(r)
        if not num:
            if sid is None:
                raise RuntimeError("a storeload row has neither a doc_num nor an id")
            num = _storeload_doc_num(_storeload_detail(sid))
        if num:
            index[num] = sid
        else:
            # One of the 43 has no document number at all (measured 2026-08-08). Skipping it is
            # safe ONLY because every document we create is named INIT-<code>, so a blank one
            # cannot be ours — but say so out loud rather than letting the count go quiet.
            unnumbered += 1
    # ASCII only in printed output: this is run by hand on a Windows console, and a mojibake
    # dash mid-sentence is exactly the kind of thing that makes an operator distrust the tool.
    print(f"  read {len(rows)} storeloads, {len(index)} with a document number"
          + (f", {unnumbered} without (cannot be ours - ours are all INIT-*)" if unnumbered else ""))
    return index


def _storeload_detail(store_load_id):
    """One storeload, unwrapped. Barsy wraps some detail payloads in the method name and some in
    a `store_load` key; both shapes have been seen, so handle both rather than guess."""
    out = b.call("Storeloads_get", {"store_load_id": store_load_id})
    if isinstance(out, dict) and isinstance(out.get("Storeloads_get"), dict):
        out = out["Storeloads_get"]
    if isinstance(out, dict) and isinstance(out.get("store_load"), dict):
        out = out["store_load"]
    return out if isinstance(out, dict) else {}


def reconcile(do_write=False, depot_id=DEPOT_ID):
    """Resolve every `pending` code by asking Barsy whether it holds that doc_num.

    Two verdicts, the same two the panel's Доставки page uses:
      confirmed — the document is there; adopt its storeload id and stop blocking
      released  — it is not there; the load never landed, so the code becomes loadable again

    A pending row is never guessed at. If the index cannot be built completely this raises and
    changes nothing, because a failed probe is not evidence of absence."""
    pending = {c: r for c, r in _ledger().items() if r.get("state") == "pending"}
    if not pending:
        print("nothing pending")
        return {}
    print(f"{len(pending)} pending - reading every storeload to find their documents")
    index = _doc_num_index(depot_id)
    verdicts = {}
    for code, rec in sorted(pending.items()):
        num = rec.get("doc_num") or doc_num_for(code)
        if num in index:
            verdicts[code] = ("confirmed", index[num])
        else:
            verdicts[code] = ("released", None)
    for code, (state, sid) in sorted(verdicts.items()):
        print(f"  {code}: {state}" + (f" (storeload {sid})" if sid else ""))
        if do_write:
            rec = pending[code]
            _record(code, rec.get("article_id"), rec.get("qty"), sid, state,
                    rec.get("doc_num") or doc_num_for(code))
    if not do_write:
        print(f"dry run - pass --run to write these {len(verdicts)} verdicts to the ledger")
    return verdicts


def sync_all(stock_map, do_write=False):
    """stock_map = {code: qty}. Loads each code that IS in Barsy, not yet loaded, qty>0."""
    catalog = bp._catalog()                       # {code: article}
    # _blocked, not _loaded: a code whose outcome we never learned must not be posted again.
    blocked = _blocked()
    todo = []
    for c, q in stock_map.items():
        c = str(c)
        try:
            qn = float(str(q).replace(",", ".")) if str(q).strip() else 0
        except ValueError:
            qn = 0
        if c in catalog and c not in blocked and qn > 0:
            todo.append((c, q))
    print(f"{len(todo)} products to load (in Barsy, not yet loaded, qty>0)")
    if not do_write:
        for c, q in todo[:20]:
            print(f"  would load {c}: {q}")
        if len(todo) > 20:
            print(f"  ... +{len(todo) - 20} more (pass --run to load)")
        return
    ok = 0
    for c, q in todo:
        aid = catalog[c]["article_id"]
        try:
            sid = load_stock(c, aid, q)
            ok += 1
            print(f"  loaded {c} (article {aid}) qty {q} -> storeload {sid}")
        except Exception as e:
            # The ledger already holds a `pending` line for this code, so it will NOT be
            # re-posted on the next run. It stays blocked until --reconcile asks Barsy.
            print(f"  FAIL {c}: {str(e)[:90]}")
            print(f"       -> left PENDING (doc {doc_num_for(c)}); run --reconcile, do not re-run blind")
        time.sleep(0.3)                           # be gentle with the lower-tier API
    print(f"done: loaded {ok}/{len(todo)}")


def main():
    if "--status" in sys.argv:
        led = _ledger()
        pend = sorted(c for c, r in led.items() if r.get("state") == "pending")
        print(f"depot: {DEPOT_ID} | stock-loaded: {len(_loaded())} codes | pending: {len(pend)}")
        if pend:
            print("  PENDING (outcome unknown, blocked from re-posting): " + ", ".join(pend[:20]))
            print("  run --reconcile to resolve them against Barsy")
    elif "--reconcile" in sys.argv:
        reconcile(do_write="--run" in sys.argv)
    elif "--load" in sys.argv:
        i = sys.argv.index("--load")
        code, qty = sys.argv[i + 1], sys.argv[i + 2]
        aid = bp._catalog().get(str(code), {}).get("article_id")
        if not aid:
            print(f"{code} not in Barsy - push it first")
            return
        print(f"loaded storeload id: {load_stock(code, aid, qty)}")
    else:
        print(__doc__)


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
