# Enrichment Skill — smart, verified data enrichment

This skill defines HOW agents enrich product data so results are high quality. The rule
is simple: **never write an enriched value you have not verified, and remember every
verification in a shared store so no agent verifies the same thing twice.** Agents have
the Hermes harness (web search, command execution, a model chain) — use it, but cache
the result.

## Core principles
1. **Verify before write.** A raw signal (a brand read off a photo, a guessed material,
   a candidate related product) is a *hypothesis*, not a value. Confirm it first.
2. **Grounded confidence gates the action.** High confidence → apply automatically.
   Medium → propose for 1-click human approval (see `review_server.py`, `vision_correction`).
   Low / unverifiable → leave the field empty and note why; do not guess.
3. **Shared, growing knowledge stores.** Every verification is appended to a shared,
   concurrency-safe JSONL that all 6 lanes read. Knowledge compounds and self-corrects.
4. **Prefer cheap, grounded sources first.** Gazetteer / index lookup (free, instant) →
   model knowledge → web search. Only escalate when the cheaper step is inconclusive.
5. **Empiric values are never touched** (Код, Цена, Количество, Мярка) — owner directive.

## Implemented protocols

### Brand (`brand_tools.py`, store: `brand_gazetteer.jsonl`)
Pipeline for a brand candidate read off the photo (`видим_бранд` from the vision verifier):
1. **Ignore noise.** Supplier/store watermarks (EGERA, LEVENA, MIRA-N …) are NOT product
   brands — the vision prompt is told to skip them and `SUPPLIER_NAMES` filters them.
2. **Gazetteer lookup** (`brand_tools.lookup`, fuzzy). A hit returns the CANONICAL spelling
   for free — this is how "gurex" becomes "GUREX". The gazetteer is seeded from every real
   supplier scrape brand (`seed_from_scrape`) and grows from step 3.
3. **Verify unknowns** (`brand_tools.verify_llm`): a capable model judges real-brand? +
   canonical spelling + confidence. (Web grounding via Tavily/Wikipedia can be plugged into
   `verify_llm`; keep the model as the interpreter.) Gibberish / store names are rejected.
4. **Grow the store.** A confident, real brand is appended to the gazetteer with the raw
   variant, so the next agent that sees it gets an instant spelling-corrected hit.
5. **Write only if verified AND the field is empty.** A confirmed brand that conflicts with
   an existing one is noted (`brand_image_differs`), never silently overwritten.
`brand_tools.resolve(candidate, generate_fn, context)` runs the whole pipeline.

### Related products by catalogue number (`relate_tools.py`, store: `catnum_index.jsonl`)
Supplier catalogue numbers run in sequence within a family ('10-002','10-003' = variants).
1. **Register** every processed product's `Каталожен номер` in the shared index.
2. **Find neighbours**: same prefix, number n-1 / n / n+1 → almost certainly related.
3. Merge those codes into `Свързани`; `build_catalog.py` makes the link symmetric (A↔B).

## How to add a new smart-enrichment step
Follow the same shape:
1. A **knowledge store** — append-only JSONL, `load()` reconstructs, `add()` appends
   (append is atomic → safe across lanes). Seed it from existing trustworthy data if any.
2. A **resolve function** — lookup store → verify with model/tool → add to store → return
   the value + a note. Return `None` + a note when unverified (caller leaves field empty).
3. **Wire it into `run_one.process_next`** at the point the field is finalised, gate the
   write on confidence, and append a note so the review page and audits can see the source.
Candidate next steps: material/colour canonical vocabularies (same pattern as brand);
weight estimation via a material-density table with a regression cross-check; series/model
grouping; unit normalisation to one canonical metric unit.

## Tools available to agents (Hermes harness)
- **Model chain** `run_one.generate_with_chain(prompt)` — direct, exhausted-quota-aware,
  spans ~13 free Alibaba models + Groq/NVIDIA/Cohere spillover.
- **Vision** `run_one.verify_against_image` — 90B VLM: type/shape/material/colour/count,
  brand OCR, and photo-grounded corrections with a confidence.
- **Web search** — Tavily backend is configured (currently out of credits); Wikipedia and
  the Hermes `-t web` toolset are alternatives. Wrap any of these behind the resolve step.
- **Command execution** — the Hermes CLI can run tools; keep such calls in verify steps
  and cache their results in the knowledge store.

## Why this yields quality
The failure mode of naive enrichment is confident garbage (a hallucinated brand, a wrong
material). Verify-before-write + a growing shared store means: brands are spelled the way
the manufacturer spells them, relatedness is grounded in catalogue structure, and each
correct decision makes the next one cheaper and more consistent.
