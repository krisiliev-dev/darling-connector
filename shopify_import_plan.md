# Shopify import — scoping & plan

## Status
- **Store is already built** (Horizon theme → Cherry & Honey, 11 tag-collections, pages,
  12 pilot products, shipping/discounts). Store: `r9et0w-1u.myshopify.com`.
- **Category map done** — `category_shopify_map.json` (74 BG categories → Shopify taxonomy gids).
- **Import builder done (dry-run)** — `shopify_export.py` → `shopify_payloads.jsonl`.
  Coverage on the 3,225 enriched products so far: price 100%, category 99%, image 90%, vendor 82%.

## The remaining piece: the product-import pipeline
Transform enriched products → Shopify products via GraphQL Admin API (2026-04).

**Mapping** (implemented in `shopify_export.py`):
| Shopify field | Source |
|---|---|
| title / descriptionHtml | enriched Наименование / Описание |
| vendor | Бранд |
| category / productType | category_shopify_map (gid) / BG leaf |
| tags | collection tags (кухня/баня/…) + Синоними (BG search) |
| price / inventory | **source Цена / Количество — VERBATIM, never AI-touched** |
| seo | Мета наименование / Мета описание |
| images | image-pipeline manifest (downloaded files) |
| metafields | darling.code (+ darling.old_url for 301 redirects) |
| status | **DRAFT** (owner reviews, then publishes) |

**Still to build for the actual push** (each gated on your go-ahead):
1. **Auth** — client-credentials token (24h), per the migration memory. `shopify_api.py` helper pattern already exists in a prior session's scratchpad.
2. **`productSet` mutation runner** — batched, idempotent (keyed on darling.code metafield so re-runs update, not duplicate), rate-limit aware.
3. **Image upload** — staged uploads of the manifest files (source hotlink URLs 403 for many domains, so upload the downloaded files, not the URLs).
4. **Cloudflare search sync** — on each create/update POST to `/upsert` (worker `darling-search`), per the semantic-search requirement.
5. **Redirects** — generate 301s from old-site product IDs via the old_url metafield.

## Open questions (need your call)
1. **Scope: 14,159 vs 4,590.** The enrichment covers 14,159 Microinvest products; the old
   darling7.com site had ~4,590. Import **all enriched**, or only the ~4,590 that were live?
2. **When.** Import now (as DRAFT) in parallel with enrichment, or wait until enrichment +
   the vision attribute sweep complete so products land fully-enriched?
3. **Publish gate.** Confirm import-as-DRAFT (owner publishes) vs import-as-ACTIVE.

## Safety
Creating/updating products on a live store is an external, side-effectful action — I will
**not push without your explicit go-ahead**. The dry-run builder lets you inspect exact
payloads first (`shopify_payloads.jsonl`). Import defaults to DRAFT so nothing goes public
until you publish. Price/quantity are copied verbatim from Microinvest.
