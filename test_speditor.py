# -*- coding: utf-8 -*-
"""Regression tests for courier-name → Barsy speditor_id resolution.

Why this file exists: the matcher was SILENTLY broken until 2026-07-31. The storefront sends machine
keys ("boxnow"), Barsy stores display names ("BOX NOW"), and an exact lowercase compare missed on the
space alone. Nothing raised — `_speditor_id()` returned None, the caller omitted the field as designed,
and the waybill was stamped with no courier attached. A courier mismatch must never be a quiet None.

Run offline (normaliser + cache semantics) or with --live to also assert the real Barsy mapping.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import barsy_shopify_connector as c  # noqa: E402

fails = []


def check(label, got, want):
    ok = got == want
    print(f"[{'OK ' if ok else 'FAIL'}] {label}: {got!r}" + ("" if ok else f" (want {want!r})"))
    if not ok:
        fails.append(f"{label}: got {got!r} want {want!r}")


print("--- _speditor_key: everything below must collapse to the same key ---")
# the exact variants that broke it, plus the ones that would break a literal alias table
for variant in ("boxnow", "BOX NOW", "Box  Now", "box-now", "BoxNow", " boxnow ", "BOX_NOW"):
    check(f"key({variant!r})", c._speditor_key(variant), "boxnow")

print("\n--- _speditor_key: Cyrillic survives (isalnum() is unicode-aware) ---")
check("key('Спиди')", c._speditor_key("Спиди"), "спиди")
check("key('Еконт')", c._speditor_key("Еконт"), "еконт")
check("key('От офис')", c._speditor_key("От офис"), "отофис")

print("\n--- _speditor_key: degenerate input must not explode ---")
check("key(None)", c._speditor_key(None), "")
check("key('')", c._speditor_key(""), "")
check("key('  ')", c._speditor_key("  "), "")

print("\n--- distinct couriers must NOT collide after normalisation ---")
keys = {n: c._speditor_key(n) for n in ("Еконт", "Speedy", "Поща", "От офис", "BOX NOW", "Sameday")}
check("6 couriers -> 6 distinct keys", len(set(keys.values())), 6)

print("\n--- a failed/empty fetch must NOT be cached (would poison every later lookup) ---")
_real_call, _real_map = c.b.call, c._SPEDITORS["map"]
try:
    c._SPEDITORS["map"] = None

    def _boom(*a, **k):
        raise RuntimeError("simulated Barsy outage")

    c.b.call = _boom
    check("during outage -> None", c._speditor_id("econt"), None)
    check("map NOT poisoned by outage", c._SPEDITORS["map"], None)

    # recovery: the very next call must succeed, not return a cached empty map
    c.b.call = lambda *a, **k: [{"speditor_name": "Еконт", "speditor_id": 1},
                                {"speditor_name": "BOX NOW", "speditor_id": 5}]
    check("recovers after outage", c._speditor_id("econt"), 1)
    check("space-insensitive on recovery", c._speditor_id("boxnow"), 5)
    check("latin alias -> cyrillic entry", c._speditor_id("Еконт"), 1)
    check("unknown courier is still None", c._speditor_id("pigeon"), None)

    # an empty list is not a usable map either, and must not freeze
    c._SPEDITORS["map"] = None
    c.b.call = lambda *a, **k: []
    check("empty list -> None", c._speditor_id("econt"), None)
    check("map NOT poisoned by empty list", c._SPEDITORS["map"], None)
finally:
    c.b.call, c._SPEDITORS["map"] = _real_call, _real_map

if "--live" in sys.argv:
    print("\n--- live Barsy mapping ---")
    c._SPEDITORS["map"] = None
    for name, want in (("econt", 1), ("speedy", 2), ("boxnow", 5), ("sameday", 6),
                       ("BOX NOW", 5), ("Спиди", 2), ("Еконт", 1),
                       ("pigeon", None), ("evropat", None)):
        check(f"live {name!r}", c._speditor_id(name), want)

print("\n" + "=" * 60)
if fails:
    print(f"{len(fails)} FAILURE(S):")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("all speditor resolution checks pass")
