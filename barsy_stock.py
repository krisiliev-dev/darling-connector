# -*- coding: utf-8 -*-
"""Initial stock load into Barsy (owner 2026-07-20).

Barsy has NO "set quantity = N" call — stock is DOCUMENT-DRIVEN and ADDITIVE. So we post one
`Storeloads_create` goods-in document per product against the loadable depot, `save_and_close`
to commit it to stock. Idempotent: each code is loaded at most once (tracked in stock_loaded.jsonl)
so re-runs never double-count.

DATA DEPENDENCY: needs real stock quantities. The current Microinvest NOMENCLATURE export has NO
stock column — qty is blank for all rows. The owner must provide a Microinvest наличности/inventory
export (код + количество). Feed it as {code: qty} to sync_all().

COST: Storeloads rows want current_price (delivery/cost). We don't have a cost column, so the
initial load uses 0 (stock counts are correct; avg-cost/profit reporting starts at 0 until real
deliveries post). Change DEFAULT_COST if a cost export becomes available.

  python barsy_stock.py --status
  python barsy_stock.py --load <code> <qty>     # load ONE (test / manual)
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


def _loaded():
    s = set()
    if STATE.exists():
        for ln in STATE.read_text(encoding="utf-8").splitlines():
            try:
                s.add(str(json.loads(ln)["code"]))
            except Exception:
                pass
    return s


def _record(code, article_id, qty, sid):
    with STATE.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"code": str(code), "article_id": article_id, "qty": qty,
                            "storeload_id": sid, "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                           ensure_ascii=False) + "\n")


def load_stock(code, article_id, qty, cost=DEFAULT_COST, depot_id=DEPOT_ID):
    """Post a goods-in document for ONE article and commit it. Returns the storeload id.
    doc_num must be unique per trade object → we stamp it with code + epoch."""
    sid = b.call("Storeloads_create", {
        "store_load": {"depot_id": depot_id, "doc_date": time.strftime("%Y-%m-%d"),
                       "doc_num": f"INIT-{code}-{int(time.time())}",
                       # prices are EUR + VAT-inclusive (matches deliveries.py / panel config). Without
                       # these Barsy assumes the ex-VAT system default → wrong booked cost. price_mode
                       # polarity per storeloads/getlist.rst: 0=без ДДС, 1=с ДДС.
                       "currency_id": 1, "price_mode": 1},
        "articles": [{"article_id": int(article_id), "amount": str(qty),
                      "current_price": str(cost)}],
        "action_type": "save_and_close"})
    _record(code, article_id, qty, sid)
    return sid


def sync_all(stock_map, do_write=False):
    """stock_map = {code: qty}. Loads each code that IS in Barsy, not yet loaded, qty>0."""
    catalog = bp._catalog()                       # {code: article}
    loaded = _loaded()
    todo = []
    for c, q in stock_map.items():
        c = str(c)
        try:
            qn = float(str(q).replace(",", ".")) if str(q).strip() else 0
        except ValueError:
            qn = 0
        if c in catalog and c not in loaded and qn > 0:
            todo.append((c, q))
    print(f"{len(todo)} products to load (in Barsy, not yet loaded, qty>0)")
    if not do_write:
        for c, q in todo[:20]:
            print(f"  would load {c}: {q}")
        if len(todo) > 20:
            print(f"  … +{len(todo) - 20} more (pass --run to load)")
        return
    ok = 0
    for c, q in todo:
        aid = catalog[c]["article_id"]
        try:
            sid = load_stock(c, aid, q)
            ok += 1
            print(f"  loaded {c} (article {aid}) qty {q} -> storeload {sid}")
        except Exception as e:
            print(f"  FAIL {c}: {str(e)[:90]}")
        time.sleep(0.3)                           # be gentle with the lower-tier API
    print(f"done: loaded {ok}/{len(todo)}")


def main():
    if "--status" in sys.argv:
        print(f"depot: {DEPOT_ID} | already stock-loaded: {len(_loaded())} codes")
    elif "--load" in sys.argv:
        i = sys.argv.index("--load")
        code, qty = sys.argv[i + 1], sys.argv[i + 2]
        aid = bp._catalog().get(str(code), {}).get("article_id")
        if not aid:
            print(f"{code} not in Barsy — push it first")
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
