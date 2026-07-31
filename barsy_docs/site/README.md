# Barsy docs — full local mirror (grep this instead of driving Chrome)

Complete offline copy of both doc sections. No login needed to refresh — rebuild with
`bash ../mirror_docs.sh` (enumerates each section's `searchindex.js`; api via public
`_sources/*.rst.txt`, help via public HTML→text).

- **`barsy.api/`** — 588 pages as `.rst` (the API reference: every method's description, parameter
  table, helper-object shapes, response shape). Layout mirrors the site: `methods/<group>/<method>.rst`,
  `objects/*.rst`, `examples/*.rst`, `sparams/`, `usage/`, `integrations/`, `faq/`.
- **`barsy.help/`** — 698 pages as `.txt` (dictionary + how-tos + narrative), stripped from the public
  HTML. 8 pages failed to fetch (see `../_tmp/misses.txt`) — negligible.

## Greppable answers to things we were unsure about (verified 2026-07-27)
- **Genuinely UNDOCUMENTED (exist live, NO doc page — confirmed not a mirror gap):**
  `Storeouts_save` (Изписване), `Revisions_create/_save/_close` (Ревизия), `Groupsattr_save` (variants).
  → these MUST be reverse-engineered live (Hermes); the docs will never describe their save shape.
- **Fully documented:** `Storemoves_*` (Прехвърляне: create/close/update/get/getlist),
  `Storeloads_*`, `Reservations_*`, `Suppliers_save_articles`, `Pricelists_*` (many save_* targets).
- **No supplier purchase-ORDER create API:** `orders`/`deals`/`documents` are getlist/index only.
- **Channel/location pricing:** `Pricelists_save_client_groups` + `Pricelists_save_barsys_poses`
  (per trade-object/POS) + `save_countries`/`save_clients` → model "physical store vs online store"
  price as a pricelist scoped to a POS or client group. (See methods/pricelists/.)
- **Webhook events:** `methods/webhooks/event_type_getlist.rst` + `subscribe.rst` (enumerate live).

Quick grep examples:
  grep -rl "Storemoves_create" barsy.api/methods/storemoves/
  grep -A3 "price_mode" barsy.api/methods/storeloads/*.rst
