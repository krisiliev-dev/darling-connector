# Barsy docs — authed Chrome dive (2026-07-27)

Grabbed via the owner's logged-in docs.lukanet.com session. The filled `sources/*/json.json` example
payloads are NOT separately servable (404 / login-gated); method-page JSON tabs + Postman collection ship
EMPTY skeletons (`{"rows":[[]]}`). The value is in the PHP `BarsyApiClient` examples + the Extended-examples
(`/barsy.api/examples/`) pages. Two findings worth acting on:

## 1. `bid` (търговски обект / trade-object) context — likely cause of the association-write 500s
Every client example calls `$bapi->setBarsyId(<id>)` before the request, and the JSON endpoint form is
`.../endpoints/json/?bid=<id>`. Docs (`examples/set_barsy_id.html`): *"Necessary when the user you
authorize with has access to MORE THAN ONE trade object and you want to specify the context the requests
execute in."*
→ HYPOTHESIS for the long-standing generic-500 on `Suppliers_save_articles` (row w/ article_id) and
`Groupsattr_save`: the `Claude` API user may see >1 trade object, and these association writes may require
the request to be scoped to the correct `bid`. Simple reads/creates worked because they defaulted; the
association writes may not. ACTION (Hermes, live): retry both with an explicit `?bid=<darling7 id>` (get the
id via `Barsys_getlist`/`Misc`/`getCurrent`). If that clears the 500, wire `bid` into `barsy_api.call`.

## 2. Efficient DELTA article sync (fixes the O(N²) full-catalog re-pull perf note)
`examples/articles.html` — the canonical "smart sync to an external store (Magento)" pattern:
- `Articles_GetList` filters: `last_update: ">"+<iso-ts>` OR `all_last_update: -1` (uses Barsy's internal
  per-article last-queried marker — returns only rows changed since our last processed mark),
  `depot_group_id: 1` (only count stock in REAL depots, skip service ones), `picture: true`, `cat_id: true`,
  `parent_id: false`, `article_details: {"Марка": "!KM", ...}` (filter by characteristic).
- `extra_properties: ['article_details','store_amount_all','store_amount_details','categories']` to fetch
  stock totals + per-depot stock + categories inline.
- After processing, write the service marker back with
  `ArticleDetails_setDetailValue {article_id:[...], key_id:-1, detail_value:<now>}` so the next
  `all_last_update:-1` pull returns only newly-changed rows.
→ ACTION (connector/reconcile): replace the whole-catalog `Articles_getlist({})` re-pull with a delta
  `last_update`/`all_last_update` filter + `depot_group_id` scoping. Directly addresses the O(N²) warning in
  [[barsy-api]] and makes the nightly reconcile cheap. `ArticleDetails_getTree/getList/getListValues` also
  give the attribute vocab for enum work.

## Confirmed (no change needed)
- `Suppliers_save_articles` request shape = `{id:<supplier_id>, rows:[{article_id, default_delivery_price,
  remote_ref_id, remote_article_name}]}` — matches what we send (so the 500 is NOT the row shape → see #1).
- Undocumented (no doc page at all): `Storeouts_save`, `Revisions_*` — reverse-engineer live (Hermes did).
- `_sources/*.rst.txt` ARE public (no auth); rendered `.html` + `sources/*.json` need login.
