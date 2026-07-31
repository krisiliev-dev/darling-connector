# -*- coding: utf-8 -*-
"""Validate woo_orders.normalise() against REAL staging orders.

Fixtures: darling-woo `tests/fixtures-orders.json`, exported by the storefront agent 2026-07-31 from
staging orders 13 / 15 / 16. The VALUES are real — that is the whole point of using them instead of
fixtures I invent from a spec.

⚠ THE EXPORT IS RE-SHAPED, NOT THE WIRE FORMAT. The storefront flattened it for readability:

      export                         WooCommerce REST / webhook
      darling_meta {k: v}            meta_data [{key, value}]
      shipping_lines[].meta {k: v}   shipping_lines[].meta_data [{key, value}]
      shipping_lines[].name          shipping_lines[].method_title
      line_items[].qty               line_items[].quantity

`_wire()` below is MY translation back to the wire shape, and it is the one unverified link in this
test: it is an assumption about naming, not something the storefront confirmed. It is kept HERE and
not in the mapper on purpose — the mapper stays strict about the shape it will actually receive, so a
future wire-shape change fails loudly instead of being absorbed by leniency.
Semantics (the guards) are validated against real values; field NAMES are pending confirmation.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from woo_orders import normalise  # noqa: E402

FIXTURES = os.path.join(os.path.expanduser("~"), "darling-woo", "tests", "fixtures-orders.json")


def _wire(o):
    """Export shape -> WooCommerce REST shape. See the caveat in the module docstring."""
    return {
        "id": o.get("id"),
        "number": o.get("id"),
        "status": o.get("status"),
        "currency": o.get("currency"),
        "total": o.get("total"),
        "payment_method": o.get("payment_method"),
        "meta_data": [{"key": k, "value": v} for k, v in (o.get("darling_meta") or {}).items()],
        "shipping_lines": [
            {"method_title": ln.get("name"),
             "total": ln.get("total"),
             "meta_data": [{"key": k, "value": v} for k, v in (ln.get("meta") or {}).items()]}
            for ln in (o.get("shipping_lines") or [])
        ],
        "line_items": [
            {"sku": li.get("sku"), "quantity": li.get("qty"), "total": li.get("total")}
            for li in (o.get("line_items") or [])
        ],
    }


# what each real order MUST do. 13 is the negative fixture: the function_exists() bug wrote blank
# office meta while the UI looked healthy, so a correct mapper has to refuse it.
EXPECT = {
    "13": {"book": False, "reasons": {"missing_office_id", "office_not_validated"}},
    "15": {"book": True,  "reasons": set()},
    "16": {"book": True,  "reasons": set()},
}


def main():
    fixtures = json.load(open(FIXTURES, encoding="utf-8"))
    failures = []

    for oid, want in EXPECT.items():
        raw = fixtures.get(oid)
        if raw is None:
            failures.append(f"order {oid}: MISSING from fixtures")
            continue

        got = normalise(_wire(raw))
        reasons = {i["reason"] for i in got["issues"]}
        booked = not got["issues"]

        status = "OK " if booked == want["book"] and reasons == want["reasons"] else "FAIL"
        if status == "FAIL":
            failures.append(f"order {oid}: expected book={want['book']} reasons={sorted(want['reasons'])}, "
                            f"got book={booked} reasons={sorted(reasons)}")

        print(f"[{status}] order {oid}  {raw['payment_method']:<6} {raw['total']:>6} {got['currency']}  "
              f"-> {'BOOK' if booked else 'REFUSE'}")
        for i in got["issues"]:
            print(f"         ! {i['reason']}: {i['detail']}")

        # --- money invariant: what we would book must equal what the customer paid --------------
        items = sum(float(li["price"]) * float(li["quantity"]) for li in got["line_items"])
        ship = sum(float(s["price"]) for s in got["shipping_lines"])
        booked_total = round(items + ship, 2)
        paid = round(float(got["total_price"]), 2)
        if abs(booked_total - paid) > 0.01:
            failures.append(f"order {oid}: TOTAL MISMATCH booked {booked_total} vs paid {paid}")
            print(f"         ! TOTAL MISMATCH booked {booked_total} vs paid {paid}")
        else:
            print(f"         totals ok: items {items:.2f} + ship {ship:.2f} = {paid:.2f}")

        fee = got["shipping_fee"]
        print(f"         fees: shipping {fee['fee_shipping']:.2f} + cod {fee['fee_cod']:.2f} "
              f"= {fee['fee_shipping'] + fee['fee_cod']:.2f} (line total {fee['total']:.2f})"
              f"{'  [FALLBACK]' if fee['fallback'] else ''}")
        print(f"         financial_status={got['financial_status']}  "
              f"delivery={got['delivery']['dest']}/{got['delivery']['carrier']} "
              f"office={got['delivery']['office_id'] or '-'} validated={got['delivery']['validated']}")

        # the fee breakdown must add up to the shipping line total, or one of them is wrong
        if abs((fee["fee_shipping"] + fee["fee_cod"]) - fee["total"]) > 0.01:
            failures.append(f"order {oid}: FEE BREAKDOWN != line total")
            print("         ! fee breakdown does not equal the shipping line total")
        print()

    # --- END TO END: the issues must actually REACH the connector's refusal path ------------------
    # normalise() flagging an order is worthless if intake books it anyway. Until 2026-07-31 nothing
    # consumed `issues`, so these guards existed only inside this file's own assertions.
    print("--- end-to-end: intake must refuse what the adapter flagged ---")
    import barsy_shopify_connector as conn

    for oid, want in EXPECT.items():
        norm = normalise(_wire(fixtures[oid]))
        # Dry run (do_write=False) — nothing is booked. For a FLAGGED order the guard returns before
        # _catalog(), so no Barsy call happens at all; for a clean one the catalogue IS fetched (a live
        # read), which is why 15/16 get as far as SKU matching below.
        res = conn.shopify_order_to_barsy(dict(norm, id=f"wootest-{oid}"), mode="clientorder", do_write=False)
        refused = res.get("status") == "needs_review" and bool(res.get("needs_review"))
        if want["book"]:
            # These orders may still be refused for UNRELATED reasons — the fixtures carry the
            # storefront's TEST-WOO-001 SKU, which has no Barsy article, so `unmatched_skus` is the
            # correct outcome and proves the order got PAST the adapter guards. What must not happen
            # is a refusal blamed on an adapter guard.
            ok = res.get("reason") not in want["reasons"] and not (
                set(i["reason"] for i in res.get("detail", {}).get("issues", [])) & set(EXPECT["13"]["reasons"]))
            print(f"[{'OK ' if ok else 'FAIL'}] order {oid}: passed the adapter guards "
                  f"(intake then said {res.get('reason') or res.get('status')})")
            if not ok:
                failures.append(f"order {oid}: intake wrongly refused with {res.get('reason')}")
        else:
            ok = refused and res.get("reason") in want["reasons"]
            print(f"[{'OK ' if ok else 'FAIL'}] order {oid}: intake REFUSED -> {res.get('reason')}")
            if not ok:
                failures.append(f"order {oid}: intake failed to refuse a flagged order "
                                f"(status={res.get('status')}, reason={res.get('reason')})")
            else:
                # the refusal must name every fault, not just the first — whoever reads this has to
                # fix all of them, and a partial message sends them round the loop twice
                named = {i["reason"] for i in res.get("detail", {}).get("issues", [])}
                if named != want["reasons"]:
                    failures.append(f"order {oid}: refusal listed {sorted(named)}, expected "
                                    f"{sorted(want['reasons'])}")
                    print(f"         ! refusal listed only {sorted(named)}")
                else:
                    print(f"         names all faults: {sorted(named)}")
    print()

    print("=" * 70)
    if failures:
        print(f"{len(failures)} FAILURE(S):")
        for f in failures:
            print("  -", f)
        return 1
    print(f"all {len(EXPECT)} real staging orders behave as required")
    return 0


if __name__ == "__main__":
    sys.exit(main())
