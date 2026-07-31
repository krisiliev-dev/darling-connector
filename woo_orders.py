# -*- coding: utf-8 -*-
"""WooCommerce order → the connector's normalised order dict (Woo migration, Phase 4).

The connector's Barsy-side logic (shopify_order_to_barsy, finalise_order, refunds, invoices) is
platform-agnostic — it consumes a normalised dict. This module is the Woo half of the adapter that
produces that dict, replacing the Shopify webhook payload shape.

Deliberately ONLY the mapping + the intake guards: no HTTP, no Barsy calls, so it is testable without
a live store. `normalise(woo_order)` is a pure function.

Contract source: storefront handoff 2026-07-31 (see memory `woo-order-contract`). The `darling_*`
meta keys are FROZEN and shared with the Shopify build so the Barsy mapping does not move.
"""

# --- frozen meta keys (do NOT rename; a silent mismatch reads as "not requested") ---------------
M_DEST        = "darling_dest"           # office | door
M_CARRIER     = "darling_carrier"        # econt|speedy|boxnow|sameday|pigeon|evropat
M_CITY        = "darling_city"
M_OFFICE_ID   = "darling_office_id"
M_OFFICE_NAME = "darling_office_name"
M_VALIDATED   = "darling_validated"      # "true" only if the id was found in that city's office list

# shipping-LINE meta (not order meta)
S_CARRIER   = "darling_carrier"
S_MODE      = "darling_mode"             # office | door
S_FEE_SHIP  = "darling_fee_shipping"
S_FEE_COD   = "darling_fee_cod"
S_FALLBACK  = "darling_fallback"         # "yes" = panel was unreachable, an INVENTED rate was charged

# BOX NOW / Sameday are LOCKERS, not offices — booking logic that branches on "office" must include
# them. BOX NOW has no to-door product at all.
LOCKER_CARRIERS = {"boxnow", "sameday"}

# Carriers that resolve to a Barsy speditor_id. Anything else cannot carry one, so the waybill would
# be stamped with no courier attached — flagged, not silently dropped.
# Mirrors Barsy's Speditors_getlist; keep in step with it when a courier is registered.
#   econt=1  speedy=2  (Поща=3, От офис=4 unused)  BOX NOW=5  Sameday=6   [registered 2026-07-31]
# pigeon / evropat are deliberately absent: Barsy's speditor_provider_id is a CLOSED list of six
# integration classes, so they need a Pick Up row created before they can be booked.
BARSY_KNOWN_CARRIERS = {"econt", "speedy", "boxnow", "sameday"}


def _meta(order):
    """Woo exposes order meta as `meta_data: [{key, value}]`. Also accept an already-flattened dict."""
    md = order.get("meta_data")
    if isinstance(md, dict):
        return {str(k): v for k, v in md.items()}
    return {str(m.get("key")): m.get("value") for m in (md or []) if m.get("key")}


def _shipping_lines(order):
    return order.get("shipping_lines") or []


def _line_meta(line):
    md = line.get("meta_data")
    if isinstance(md, dict):
        return {str(k): v for k, v in md.items()}
    return {str(m.get("key")): m.get("value") for m in (md or []) if m.get("key")}


def _f(v):
    try:
        return float(v or 0)
    except (TypeError, ValueError):
        return 0.0


def normalise(order):
    """Woo order → the dict the Barsy side already consumes, plus `issues` for intake guards.

    `issues` is a list of {reason, detail} — NON-EMPTY MEANS DO NOT BOOK. The connector's intake
    already refuses on `needs_review`; these are the Woo-specific reasons that must reach it.
    """
    meta = _meta(order)
    issues = []

    dest    = str(meta.get(M_DEST) or "").strip().lower()
    carrier = str(meta.get(M_CARRIER) or "").strip().lower()
    off_id  = str(meta.get(M_OFFICE_ID) or "").strip()
    validated = str(meta.get(M_VALIDATED) or "").strip().lower()

    # --- GUARD 1: an unvalidated office cannot produce a waybill. BLOCK, don't warn. -------------
    # (Lockers count as "office" — BOX NOW/Sameday deliver to a locker, not an address.)
    is_office_like = dest == "office" or carrier in LOCKER_CARRIERS
    if is_office_like:
        if not off_id:
            # Orders created before ~02:15 2026-07-31 have this EMPTY even for office deliveries:
            # the storefront read Woo's `_wc_other/…` meta via a WC function that doesn't exist in
            # WC 10.9, behind function_exists(), so it silently wrote blanks. Staging order 13 is a
            # real example. Historical orders are NOT trustworthy here.
            issues.append({"reason": "missing_office_id",
                           "detail": "dest=office but darling_office_id is empty — cannot book a waybill"})
        if validated != "true":
            issues.append({"reason": "office_not_validated",
                           "detail": f"darling_validated={validated!r}; the office id was not confirmed "
                                     f"against that city's office list"})

    # --- shipping line: fee breakdown + the fabricated-rate alarm -------------------------------
    ship = {"carrier": carrier, "mode": dest, "fee_shipping": 0.0, "fee_cod": 0.0,
            "fallback": False, "total": 0.0}
    for ln in _shipping_lines(order):
        lm = _line_meta(ln)
        ship["carrier"] = str(lm.get(S_CARRIER) or ship["carrier"]).lower() or ship["carrier"]
        ship["mode"] = str(lm.get(S_MODE) or ship["mode"]).lower() or ship["mode"]
        ship["fee_shipping"] += _f(lm.get(S_FEE_SHIP))
        ship["fee_cod"] += _f(lm.get(S_FEE_COD))
        if str(lm.get(S_FALLBACK) or "").strip().lower() == "yes":
            ship["fallback"] = True
        ship["total"] += _f(ln.get("total")) + _f(ln.get("total_tax"))

    # --- GUARD 2: a fabricated rate is INTERNALLY CONSISTENT, so the totals invariant cannot see
    # it. The customer was charged a price no courier quoted; the real courier bill will differ.
    # External truth needs its own guard. (see memory `integration-safety-rules`)
    if ship["fallback"]:
        issues.append({"reason": "fallback_shipping_rate",
                       "detail": f"darling_fallback=yes — {ship['total']:.2f} was charged without a "
                                 f"courier quote; the actual courier cost will differ"})

    # --- carrier ↔ Barsy speditor gap: surfaced, never silently dropped -------------------------
    if carrier and carrier not in BARSY_KNOWN_CARRIERS:
        issues.append({"reason": "carrier_not_in_barsy",
                       "detail": f"carrier {carrier!r} has no Barsy speditor (Barsy knows only "
                                 f"{sorted(BARSY_KNOWN_CARRIERS)}) — the waybill would be stamped "
                                 f"with no courier attached"})

    return {
        "id": str(order.get("id") or ""),
        "name": f"#{order.get('number') or order.get('id') or ''}",
        # Woo COD reaches `processing` at placement; card reaches it via the gateway webhook.
        "financial_status": "paid" if str(order.get("payment_method") or "") != "cod"
                            and str(order.get("status") or "") in ("processing", "completed")
                            else "pending",
        "payment_method": str(order.get("payment_method") or ""),
        "total_price": str(order.get("total") or "0"),
        "currency": str(order.get("currency") or "EUR"),
        "line_items": [
            {"sku": str(li.get("sku") or "").strip(),
             "quantity": li.get("quantity") or 0,
             # Woo gives line totals, not unit price: unit = (total - discount)/qty is already net of
             # discounts, so the Shopify-side discount arithmetic is NOT reapplied here.
             "price": _unit_price(li),
             "total_discount": 0}
            for li in (order.get("line_items") or [])
        ],
        "shipping_lines": [{"title": ln.get("method_title") or "Доставка",
                            "price": f"{_f(ln.get('total')) + _f(ln.get('total_tax')):.2f}"}
                           for ln in _shipping_lines(order)],
        "delivery": {"dest": dest, "carrier": carrier, "city": meta.get(M_CITY) or "",
                     "office_id": off_id, "office_name": meta.get(M_OFFICE_NAME) or "",
                     "validated": validated == "true", "is_locker": carrier in LOCKER_CARRIERS},
        "shipping_fee": ship,
        "note_attributes": [{"name": k, "value": v} for k, v in meta.items()
                            if k.startswith("darling_invoice")],
        "issues": issues,
    }


def _unit_price(li):
    """Woo line -> per-unit price ACTUALLY PAID (net of line discounts), as a string.

    Woo's `subtotal` is pre-discount and `total` is post-discount; the difference is the discount.
    Booking `subtotal` would over-declare exactly like the Shopify pre-discount bug did.
    """
    qty = _f(li.get("quantity")) or 1.0
    paid = _f(li.get("total")) + _f(li.get("total_tax"))
    return f"{paid / qty:.2f}"
