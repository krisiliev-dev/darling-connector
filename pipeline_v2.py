# -*- coding: utf-8 -*-
"""PIPELINE V2 — leaf-first, schema-driven enrichment (owner-approved 2026-07-18;
consolidated after the full v1 audit — all hard-won v1 guards ported).

Per product: 1) CLASSIFY into a Shopify taxonomy leaf (confidence-gated, category-seeded
candidates); 2) FILL the leaf's required attribute schema (official bg vocabularies,
"друго:"/"няма" escapes) + Тегло estimate; 3) NAME composed from validated attributes;
4) TEXTS (+Синоними) generated strictly from the record; 5) VISION verify of the final
record vs the photo (flag-only); plus the complete v1 deterministic armor: agentic_guards
(homoglyphs, supplier brands, weight plausibility, name cap, placeholder attrs, dup-desc),
catalogue_guard full strip set, quality_clean, field_tidy, russian survivors, weak-match
forcing, monotonic quality gate, relate_tools-driven Свързани, gazetteer brand growth.

v1 output is UNTRUSTED HINTS. Writes v2 versions on top of history (notes: "v2").
Activation: V2_MODE sentinel — run_one routes here; done-set = has a v2 version.
"""
import json
import re
import time
from pathlib import Path

HERE = Path(__file__).parent

CLASSIFY_PROMPT = """Класифицирай продукта в НАЙ-ТОЧНАТА категория-лист от Shopify
таксономията. Продукт:
  Име (каса): {stoka}
  Категория в магазина: {category}   ← силен сигнал за какво СЛУЖИ продуктът
  Име (доставчик): {scrape_name}
  Описание (скрейп): {scrape_desc}
  v1 данни (НЕПРОВЕРЕНИ подсказки): Тип: {v1_type}; Атрибути: {v1_attrs}
ВНИМАНИЕ: името от касата може да е подвеждащо — ако категорията и описанието сочат друг
тип продукт, вярвай на тях (напр. „щипка“ в категория „Чинии и плата“ вероятно е плато).
Разграничавай СЕРВИРАНЕ от ГОТВЕНЕ (стойка за торта ≠ форма за печене на торта).{weak}

Кандидати:
{cands}

Върни САМО валиден JSON:
{{"лист": <номер>, "увереност": "висока"|"средна"|"ниска"}}"""

FILL_PROMPT = """Попълни ЗАДЪЛЖИТЕЛНИТЕ атрибути на продукта по схемата на категорията
"{leaf}". ПРАВИЛА:
- Стойност САМО от списъка, ако има списък. Ако вярната стойност липсва в списъка:
  "друго: <стойност>". Ако групата не е приложима за този продукт: "няма".
- НИЩО измислено: всяка стойност трябва да следва от данните по-долу. При липса на
  данни за група → "няма".
- v1 подсказките може да съдържат ГРЕШКИ от визуален модел (напр. "дърво" защото
  кутията е дървена). Ползвай стойност от v1 САМО ако се потвърждава от името,
  доставчика или страницата — иначе "няма".
- "Размер/Обем": размерите/обемът с мерна единица (напр. "40×60 см" или "1,5 л").
- Върни и "тегло_кг": разумна оценка на теглото в кг (число; за доставка).
- Ако продуктът явно НЕ е "{noun}", върни и "тип": <правилното кратко съществително>.{weak}

ДАННИ:
  Каса: {stoka}
  Доставчик: {scrape_name} | {scrape_dims} | {scrape_brand} | {scrape_mat}
  Описание (доставчик): {scrape_desc}
  v1 (НЕПРОВЕРЕНИ подсказки): {v1_attrs}
  Страница на доставчика (откъс): {page}

СХЕМА:
{schema}

Върни САМО валиден JSON: {{"група": "стойност", ...}} (всички групи от схемата)."""

TEXT_PROMPT = """Напиши текстовете за продуктова страница на български за този продукт.
ЗАПИС (единствен източник на истина — НЕ добавяй факти извън него):
  Наименование: {name}
  Атрибути: {attrs}
  Описание от доставчика (може да ползваш идеи, без нови факти): {scrape_desc}
{owner_rules}
ФОРМАТ на описанието (SEO-структура, 60–110 думи общо):
  <p>Уводно изречение с типа, бранда (ако има) и главното предимство — ключовите думи
  естествено вплетени.</p>
  <ul><li>3–5 точки: конкретните характеристики от атрибутите (материал, размер/обем,
  механизъм, приложение) — по една на ред</li></ul>
  <p>Кратко заключение с употребата/за кого е подходящ.</p>

Върни САМО валиден JSON:
{{"Описание": "<HTML точно по формата по-горе, без измислени факти>",
 "Мета наименование": "<до 60 знака, ключовите думи напред>",
 "Мета описание": "<150-160 знака, завършено изречение с тип+размер+полза>",
 "Синоними": "<4-6 български думи за търсене, разделени със запетая>"}}"""

WEAK_WARN = ("\nВНИМАНИЕ: съвпадението с данните от доставчика е СЛАБО (по име, не по код)"
             " — данните може да са за ДРУГ продукт; при съмнение предпочети касата.")

_nodes_cache = {"v": None}
_maps_cache = {"cmap": None, "leafmap": None}


def _refined_pin(code):
    """The node for a leaf_refine.py-chosen leaf (product_taxonomy.source='agent_refined'),
    or None. When present it is authoritative — reprocessing fills THIS leaf's schema."""
    import db
    con = db.connect()
    try:
        r = con.execute("SELECT gid FROM product_taxonomy WHERE code=? "
                        "AND source='agent_refined'", (str(code),)).fetchone()
    finally:
        con.close()
    if not r or not r[0]:
        return None
    return next((n for n in _nodes() if n["gid"] == r[0]), None)


def _nodes():
    if _nodes_cache["v"] is None:
        import taxonomy_leaf as tl
        nodes = tl.load_nodes()
        for n in nodes:                                  # precompute token sets once
            n["_tb"] = _toks(n["bg"])
            n["_tf"] = _toks(n["full"])
            n["_vert"] = n["gid"].rsplit("/", 1)[-1].split("-")[0]   # vertical prefix
        _nodes_cache["v"] = nodes
    return _nodes_cache["v"]


def _cmap():
    if _maps_cache["cmap"] is None:
        _maps_cache["cmap"] = json.loads(
            (HERE / "category_shopify_map.json").read_text(encoding="utf-8"))
    return _maps_cache["cmap"]


def _leafmap():
    if _maps_cache["leafmap"] is None:
        try:
            _maps_cache["leafmap"] = json.loads(
                (HERE / "canon_leaf_map.json").read_text(encoding="utf-8"))
        except Exception:
            _maps_cache["leafmap"] = {}
    return _maps_cache["leafmap"]


def _toks(s):
    return {w for w in re.findall(r"[а-яa-z]{3,}", str(s or "").lower())}


def _stem_match(a, b):
    """Prefix-tolerant: 'нож'~'ножове', 'чаша'~'чаши' (3-char stem for 4-letter words)."""
    ka = a[:4] if len(a) >= 5 else a[:3]
    kb = b[:4] if len(b) >= 5 else b[:3]
    return a.startswith(kb) or b.startswith(ka)


def _tokscore(ptoks, ntoks):
    sc = 0
    for lt in ntoks:
        if any(_stem_match(lt, pt) for pt in ptoks):
            sc += 1
    return sc


def _candidates(stoka, scrape_name, v1_type, code, category=""):
    """Ranked candidate leaves from every signal, incl. the till category's mapped node
    (its leaf descendants are always on offer even when the NAME is misleading)."""
    import db
    nodes = _nodes()
    byg = {n["gid"]: n for n in nodes}
    seed = []
    cat_leaf_words = ""
    try:
        bycat = {m["bg"]: m.get("shopify_category") or "" for m in _cmap()}
        for part in str(category or "").split(";"):
            p = part.strip()
            path = bycat.get(p.split("->")[-1].strip()) or bycat.get(p.split("->")[0].strip())
            if path:
                cat_leaf_words += " " + p.split("->")[-1]
                pnode = next((n for n in nodes if n["full"] == path), None)
                if pnode:
                    seed.append(pnode)
    except Exception:
        pass
    lm = _leafmap().get(str(v1_type or "").strip().capitalize())
    if lm and lm.get("gid") in byg:
        seed.append(byg[lm["gid"]])
    try:
        con = db.connect()
        r = con.execute("SELECT gid FROM product_taxonomy WHERE code=?", (str(code),)).fetchone()
        con.close()
        if r and r[0] and r[0] in byg:
            seed.append(byg[r[0]])
    except Exception:
        pass
    ct = _toks(stoka) | _toks(scrape_name) | _toks(v1_type) | _toks(cat_leaf_words)
    # SOFT vertical prior (full-taxonomy switch 2026-07-19): the product's own signals (till
    # category, v1-type, prior assignment) suggest one or more verticals. Boost leaves in
    # those verticals so cross-vertical token noise (e.g. "чиния"~"чино" chinos) doesn't crowd
    # the shortlist — but it's only a boost, so a genuinely off-vertical product (office/toys)
    # whose seed points there still surfaces its leaf.
    seed_verts = {n["_vert"] for n in seed}
    scored = []
    for n in nodes:
        if not n["leaf"]:
            continue
        sc = _tokscore(ct, n["_tb"]) * 2 + _tokscore(ct, n["_tf"])
        if sc > 0:
            if seed_verts and n["_vert"] in seed_verts:
                sc += 4                                   # same-vertical prior
            scored.append((sc, n))
    scored.sort(key=lambda x: -x[0])

    def _expand(parent):
        subs = [x for x in nodes if x["leaf"] and x["full"].startswith(parent["full"] + " > ")]
        subs.sort(key=lambda x: -(_tokscore(ct, x["_tb"]) * 2 + _tokscore(ct, x["_tf"])))
        return subs[:10]

    out, seen = [], set()
    for n in seed + [n for _s, n in scored[:14]]:
        for cand in ([n] if n["leaf"] else _expand(n)):
            if cand["gid"] not in seen:
                seen.add(cand["gid"])
                out.append(cand)
    if not out:
        subs = [x for x in nodes if x["leaf"]]
        subs.sort(key=lambda x: -(_tokscore(ct, x["_tb"]) * 2 + _tokscore(ct, x["_tf"])))
        out = subs[:15]
    return out[:15]


def _category_vertical(product):
    try:
        bycat = {m["bg"]: m.get("shopify_category") or "" for m in _cmap()}
        for part in str(product.get("Категории") or "").split(";"):
            p = part.strip()
            s = bycat.get(p.split("->")[-1].strip()) or bycat.get(p.split("->")[0].strip())
            if s:
                return s.split(" > ")[0]
    except Exception:
        pass
    return None


def _owner_rules_text():
    try:
        t = (HERE / "owner_style_rules.md").read_text(encoding="utf-8").strip()
        return ("ПРАВИЛА ОТ СОБСТВЕНИКА (спазвай ги):\n" + t + "\n") if t else ""
    except Exception:
        return ""


def _vision_pick(ro, img_url, options):
    """Show the photo to the vision model with the disputed leaf options; returns the
    chosen index or None (vision unavailable / unsure / bad answer)."""
    import io
    import base64
    import urllib.request
    try:
        req = urllib.request.Request(ro._encode_url(img_url), headers={
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"),
            "Referer": ro._origin(img_url)})
        data = urllib.request.urlopen(req, timeout=30).read()
        from PIL import Image
        im = Image.open(io.BytesIO(data)).convert("RGB")
        im.thumbnail((768, 768))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=85)
        b64 = base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return None
    opts = "\n".join(f"  {i}. {o['bg']}  [{o['full']}]" for i, o in enumerate(options))
    prompt = ("Погледни снимката. Кое от изброените НАЙ-ТОЧНО описва предмета на нея?\n"
              + opts + '\nВърни САМО JSON: {"избор": <номер>, '
              '"сигурност": "висока"|"средна"|"ниска"}')
    try:
        out = ro.vision_complete([
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}],
            max_tokens=100)
        d = json.loads(re.search(r"\{.*\}", out, re.DOTALL).group(0))
        i = int(d.get("избор"))
        if str(d.get("сигурност") or "").lower() == "ниска":
            return None
        return i if 0 <= i < len(options) else None
    except Exception:
        return None


def _consensus(ro, cprompt, cands, leaf, confidence, img_url, notes):
    """Second classifier vote through REVIEW_CHAIN (Llama family — independent of the
    Qwen worker). Same prompt, same candidates. Agreement confirms the leaf; a split
    decision is tie-broken by the photo; an unresolved split keeps the primary leaf
    but downgrades confidence (which routes the product to human review)."""
    try:
        _, out2, _ = ro.run_reviewer_direct(cprompt)
        d2 = ro.extract_json(out2) or {}
        _li2 = int(d2.get("лист"))
        if not 0 <= _li2 < len(cands):           # negative index must not wrap
            raise ValueError(_li2)
        leaf2 = cands[_li2]
    except Exception:
        notes.append("leaf_vote2_unavailable")
        return leaf, confidence
    if leaf2["gid"] == leaf["gid"]:
        notes.append("leaf_consensus")
        return leaf, confidence
    notes.append("leaf_disagree:" + leaf2["gid"].rsplit("/", 1)[-1])
    pick = _vision_pick(ro, img_url, [leaf, leaf2]) if img_url else None
    if pick is not None:
        chosen = [leaf, leaf2][pick]
        notes.append("leaf_tiebreak_vision:" + chosen["gid"].rsplit("/", 1)[-1])
        return chosen, ("средна" if confidence == "висока" else confidence)
    notes.append("leaf_disagree_unresolved")
    return leaf, ("средна" if confidence == "висока" else "ниска")


def process(task, prior_failures):
    import run_one as ro
    import db
    import leaf_schema as ls
    import telemetry
    code = str(task["code"])
    product = task.get("product") or {}
    gt = task.get("ground_truth") or {}
    ro.log(f"Processing {code} (v2, attempt {prior_failures + 1})")
    t0 = time.time()
    telemetry.reset()
    notes = ["agentic", "v2"]
    if __import__("os").environ.get("V2_REPROCESS") == "1":
        notes.append(__import__("os").environ.get("V2_REPROCESS_TAG") or "v2_reprocess")
    try:
        v1 = db.get_record(code) or {}
        v1f = v1.get("fields") or {}
        v1_attrs = str(v1f.get("Атрибути") or "")
        m = re.search(r"(?i)тип\s*:\s*([^;]+)", v1_attrs)
        v1_type = (m.group(1).strip() if m else "")
        stoka = str(gt.get("Стока") or "")
        scrape_name = str(gt.get("BG име (доставчик)") or gt.get("Английско име") or "")
        scrape_desc = str(gt.get("Описание (скрейп)") or "")[:600]
        weak = str(gt.get("Match kind") or "").lower() in ("name", "model", "fuzzy")
        if weak:
            notes.append("weak_match")
        weak_txt = WEAK_WARN if weak else ""

        # ---- 1) classify --------------------------------------------------------
        # Honor an agent-refined leaf PIN: leaf_refine.py may have moved this product to a
        # better sibling (product_taxonomy.source='agent_refined'). That choice is authoritative
        # — reprocessing must fill THAT leaf's schema, not re-classify away from it (otherwise
        # attributes stay filled for the wrong leaf). Skips the classify LLM call entirely.
        _pin = _refined_pin(code)
        if _pin is not None:
            leaf = _pin
            confidence = "висока"
            defaulted = False
            model1 = "pinned:agent_refined"
            notes.append("leaf_pinned_refined")
        else:
            cands = _candidates(stoka, scrape_name, v1_type, code,
                                category=str(product.get("Категории") or ""))
            if not cands:
                raise RuntimeError("no leaf candidates")
            clist = "\n".join(f"  {i}. {n['bg']}  [{n['full']}]" for i, n in enumerate(cands))
            cprompt = CLASSIFY_PROMPT.format(stoka=stoka, scrape_name=scrape_name,
                                             category=str(product.get("Категории") or "—"),
                                             scrape_desc=scrape_desc, v1_type=v1_type or "—",
                                             v1_attrs=v1_attrs[:300] or "—", cands=clist,
                                             weak=weak_txt)
            out, model1 = ro.generate_with_chain(cprompt,
                                                 system="Отговаряй само с валиден JSON.")
            d = ro.extract_json(out) or {}
            defaulted = False
            try:
                _li = int(d.get("лист"))
                if not 0 <= _li < len(cands):        # int("-1") would wrap to the tail
                    raise ValueError(_li)
                leaf = cands[_li]
            except Exception:
                leaf = cands[0]
                defaulted = True
                notes.append("leaf_default_first")
            raw_conf = str(d.get("увереност") or "").strip().lower()
            confidence = ("висока" if raw_conf in ("висока", "high")
                          else "средна" if raw_conf in ("средна", "medium")
                          else "ниска")
        if defaulted:
            confidence = "ниска"
        # ---- 1b) consensus: independent second vote (REVIEW_CHAIN = different model
        # family) confirms the leaf; disagreement goes to a vision tie-break on the
        # photo; unresolved disagreement downgrades confidence and flags for review.
        if _pin is None:            # a pinned refined leaf is authoritative — no 2nd vote
            leaf, confidence = _consensus(ro, cprompt, cands, leaf, confidence,
                                          str(gt.get("Снимка") or "").strip(), notes)
        notes.append(f"leaf:{leaf['gid'].rsplit('/', 1)[-1]}")
        notes.append(f"leaf_conf:{confidence}")
        cat_vert = _category_vertical(product)
        if cat_vert and not leaf["full"].startswith(cat_vert):
            notes.append("leaf_branch_mismatch")
        # full-taxonomy switch (2026-07-19): products may now land outside the 8 home-goods
        # verticals. Flag such picks for review — usually right (office/toys/bags) but the
        # occasional absurd-vertical miss (Electronics/Vehicles) should be caught.
        _HOME_VERTS = {"ae", "ap", "bt", "fr", "ha", "hb", "hg", "sg"}
        if leaf["gid"].rsplit("/", 1)[-1].split("-")[0] not in _HOME_VERTS:
            notes.append("leaf_outside_home_verticals:"
                         + leaf["full"].split(" > ")[0])

        # ---- 2) fill the schema -------------------------------------------------
        ls.ensure_nouns([leaf["gid"]])
        noun, gender = ls.noun_for(leaf["gid"])
        if not noun:
            noun, gender = leaf["bg"].split()[0], "м"
            notes.append("noun_missing")
        schema = ls.schema_for(leaf["gid"])
        schema_txt = "\n".join(
            "  " + g["група"] + (": [" + ", ".join(g["стойности"]) + "]"
                                 if g["стойности"] else ": (свободна стойност)")
            for g in schema)
        page = ""
        try:
            url = str(gt.get("URL (доставчик)") or "")
            if url:
                import agent_enrich as ae
                page = (ae._fetch(url, 6000) or "")[:1200]   # cache-backed live fetch
                if page.startswith("(грешка"):
                    page = ""
        except Exception:
            pass
        out2, model2 = ro.generate_with_chain(
            FILL_PROMPT.format(leaf=leaf["bg"], noun=noun, stoka=stoka,
                               scrape_name=scrape_name,
                               scrape_dims=str(gt.get("Размери (скрейп)") or "—"),
                               scrape_brand=str(gt.get("Бранд (скрейп)") or "—"),
                               scrape_mat=str(gt.get("Материал (скрейп)") or "—"),
                               scrape_desc=scrape_desc, v1_attrs=v1_attrs[:400] or "—",
                               page=page or "—", schema=schema_txt, weak=weak_txt),
            system="Отговаряй само с валиден JSON.")
        vals = ro.extract_json(out2) or {}
        typ = str(vals.pop("тип", "") or "").strip() or noun
        if typ != noun:
            notes.append(f"type_override:{typ}")
        weight = vals.pop("тегло_кг", None)
        attrs_parts = [f"Тип: {typ}"]
        allowed = {g["група"]: set(g["стойности"]) for g in schema}
        PLACEHOLDERS = {"няма", "null", "n/a", "-", "—", "unknown", "none",
                        "needs_human", "?", "не е посочено", "неизвестно"}
        n_other = 0
        for g in schema:
            k = g["група"]
            raw = vals.get(k)
            if isinstance(raw, list):
                raw = ", ".join(str(x) for x in raw)
            v = str(raw or "").strip()
            if not v or v.lower() in PLACEHOLDERS:
                continue
            if v.lower().startswith("друго:"):
                v = v.split(":", 1)[1].strip()
                n_other += 1
                notes.append(f"attr_other:{k}")
            elif allowed[k] and v not in allowed[k]:
                # MULTI-SELECT aware: the model often returns several allowed values
                # comma-joined (e.g. cleaning instructions, storage features). Validate
                # each part; a combination of on-list values is VALID, not off-list.
                parts = [p.strip() for p in re.split(r"\s*,\s*", v) if p.strip()]
                matched, unmatched = [], []
                for p in parts:
                    m = next((a for a in allowed[k] if a.lower() == p.lower()), None)
                    (matched if m else unmatched).append(m or p)
                if matched and not unmatched:
                    v = ", ".join(matched)            # all parts valid → on-list
                elif matched:
                    v = ", ".join(matched + unmatched)  # keep all, note the stray part
                    n_other += 1
                    notes.append(f"attr_partial:{k}")
                else:
                    # single/all values genuinely not in Shopify's (often incomplete)
                    # per-leaf list — keep the value, but it's a soft signal not an error
                    n_other += 1
                    notes.append(f"attr_offlist:{k}")
            if k == "Размер/Обем":
                vol = re.search(r"\d+(?:[.,]\d+)?\s*(?:л|мл|l|ml)\b", v, re.I)
                rest = v.replace(vol.group(0), " ") if vol else v
                dims = re.search(r"\d+(?:[.,]\d+)?(?:\s*[x×х]\s*\d+(?:[.,]\d+)?)+"
                                 r"(?:\s*(?:см|мм|cm|mm))?", rest, re.I)
                if dims:
                    attrs_parts.append("Размер: " + dims.group(0).strip())
                if vol:
                    attrs_parts.append("Обем: " + vol.group(0).strip())
                if not dims and not vol:
                    attrs_parts.append("Размер: " + v)
                continue
            attrs_parts.append(f"{k}: {v}")
        attrs_str = "; ".join(attrs_parts)
        if len(attrs_parts) <= 2:
            notes.append("attr_sparse")
        _corpus = (stoka + " " + scrape_name + " " + scrape_desc + " " + page).lower()
        for _chk in ("Материал", "Цвят"):
            _mv = next((p.split(":", 1)[1].strip().lower() for p in attrs_parts
                        if p.startswith(_chk + ":")), "")
            if _mv and _mv[:5] not in _corpus and _mv[:5] in v1_attrs.lower():
                notes.append(f"attr_v1only:{_chk}")

        # ---- 3) brand: multi-source corroboration (owner 2026-07-18: robust) -----
        # sources: v1 field, supplier scrape field, the till-name brand slot. The photo
        # OCR joins after the vision step. >=2 agreeing sources or a gazetteer-known
        # single source -> accepted; a lone unknown -> owner review queue, field empty.
        import brand_tools
        _ebrand = None
        try:
            import ean_brand
            _ebrand, _enote = ean_brand.brand_for_code(code)
            if _enote:
                notes.append(_enote)          # sticker-over-sticker conflict etc.
        except Exception:
            pass
        _bsources = [("v1", v1f.get("Бранд")),
                     ("scrape", gt.get("Бранд (скрейп)")),
                     ("slot", brand_tools.slot_candidate(stoka)),
                     ("ean", _ebrand)]
        brand, _bnotes, _bpending = brand_tools.gather(code, _bsources)
        notes += _bnotes
        brand = brand or ""

        # ---- 4) name from attributes -------------------------------------------
        import name_builder as nb
        vocab = nb.load_vocab()
        vocab["types"][typ.lower()] = [typ.capitalize(), gender]
        vocab["canon"].setdefault(typ.capitalize(), gender)
        fields = dict(v1f) if v1f else {k: product.get(k) for k in product}
        fields["Бранд"] = brand
        fields["Атрибути"] = attrs_str
        nm, _rs = nb.build_name(fields, vocab)
        if nm:
            fields["Наименование"] = nm
        else:
            fields["Наименование"] = f"{typ.capitalize()} {stoka}".strip()[:80]
            notes.append("name_fallback")

        # ---- 5) texts + synonyms from the validated record ----------------------
        # Retry on empty/malformed JSON: the smaller free models occasionally return
        # unparseable output, and a single failure used to drop the product to its v1
        # text (this caused the 639 texts_missing fallbacks). Try up to 3× for the core
        # fields before giving up.
        _txt_prompt = TEXT_PROMPT.format(name=fields["Наименование"], attrs=attrs_str,
                                         scrape_desc=scrape_desc or "—",
                                         owner_rules=_owner_rules_text())
        # attempt 0 = normal chain (fast when strong models are available); on junk/empty
        # JSON, ESCALATE to a known-capable model (weak fallbacks like llama-8b can't
        # reliably emit the complex SEO-text JSON — the cause of the texts_missing fallbacks).
        _txt_plan = [None,
                     ["-m", "nvidia/llama-3.3-nemotron-super-49b-v1", "--provider", "nvidia"],
                     ["-m", "openai/gpt-oss-120b", "--provider", "groq"]]
        texts, model3 = {}, None
        for _tattempt, _args in enumerate(_txt_plan):
            try:
                if _args is None:
                    out3, model3 = ro.generate_with_chain(
                        _txt_prompt, system="Отговаряй само с валиден JSON.")
                else:
                    _rc, out3, _e = ro.run_direct(
                        _txt_prompt, _args, system="Отговаряй само с валиден JSON.",
                        max_tokens=1500)
                    model3 = _args[_args.index("-m") + 1]
                _t = ro.extract_json(out3) or {}
            except Exception:
                _t = {}
            if str(_t.get("Описание") or "").strip() and \
                    str(_t.get("Мета описание") or "").strip():
                texts = _t
                break
            texts = _t or texts
        if _tattempt > 0 and texts.get("Описание"):
            notes.append(f"texts_escalated:{model3}")
        texts_missing = []
        for k in ("Описание", "Мета наименование", "Мета описание", "Синоними"):
            v = texts.get(k)
            if isinstance(v, list):
                v = " ".join(str(x) for x in v if not isinstance(x, bool))
            v = str(v or "").strip()
            if v:
                fixed, _chg = ro.apply_ru_fix(v)
                fields[k] = fixed
            elif k != "Синоними":
                texts_missing.append(k)
        if texts_missing:
            notes.append("texts_missing:" + ",".join(texts_missing))

        # ---- 6) related: DEFERRED to relate_rebuild.py (owner 2026-07-18: connected
        # = the SAME product in another variant; catalogue adjacency linked neighbouring
        # SKUs like легени next to бидони, so per-product linking is retired). We still
        # register the catalogue number (keeps the shared index warm for diagnostics).
        try:
            import relate_tools
            catno = str(product.get("Каталожен номер") or "").strip()
            if catno:
                relate_tools.register(code, catno)
        except Exception:
            pass
        fields_related_note = True
        notes.append("related_deferred")

        # ---- 7) deterministic armor (empirics, guards, strips, tidy) ------------
        for k in ("Код", "Цена", "Количество", "Мярка", "Каталожен номер", "Доставчик",
                  "Серия", "Активен", "Предварителна поръчка"):
            if product.get(k) is not None:
                fields[k] = product.get(k)
        fields["Свързани"] = ""
        fields["Категории"] = v1f.get("Категории") or product.get("Категории")
        fields["Снимки"] = v1f.get("Снимки") or product.get("Снимки") or gt.get("Снимка")
        if weight is not None and not str(fields.get("Тегло (кг)") or "").strip():
            fields["Тегло (кг)"] = weight
        # full v1 catalogue-number/prefix strip set across name + metas + description
        try:
            import catalogue_guard as _cg
            _catnums = _cg.source_catnums(stoka)
            _prefs = [p for _, p in _catnums]
            _lead = _cg.source_leading_prefix(stoka)
            if _lead:
                _prefs.append(_lead)
            _mcodes = _cg.source_model_codes(stoka)
            _removed = []
            for _col in ("Наименование", "Мета наименование", "Мета описание", "Описание"):
                if fields.get(_col):
                    _cl, _rm = _cg.strip_catnums_from_name(str(fields[_col]), _catnums)
                    _cl, _rm2 = _cg.strip_model_codes(_cl, _mcodes)
                    if _lead and _col in ("Наименование", "Мета наименование"):
                        _cl, _lc = _cg.strip_leading_prefix(_cl, _lead)
                        if _lc:
                            _rm2 = list(_rm2) + [_lead]
                    fields[_col] = _cl
                    _removed += list(_rm) + list(_rm2)
            if _removed:
                notes.append("catnum_stripped:" + ",".join(dict.fromkeys(_removed)))
            _b1, _bn = _cg.guard_brand(fields.get("Бранд"), _prefs)
            if _b1 != fields.get("Бранд"):
                fields["Бранд"] = _b1
                if _bn:
                    notes.append(_bn)
        except Exception as _cge:
            notes.append(f"catalogue_guard_error:{str(_cge)[:50]}")
        # v1's bundled guards: homoglyphs, supplier brand, weight plausibility,
        # name cap, placeholder attrs, synonyms cap, duplicate-description hash
        _desc_hash = None
        try:
            _desc_hash = ro.agentic_guards(fields, task, notes, code)
        except Exception as _age:
            notes.append(f"agentic_guards_error:{str(_age)[:50]}")
        try:
            import quality_clean as qcl
            fields, _qn = qcl.clean(fields)
            notes += [f"quality_clean:{x}" for x in (_qn or [])][:4]
        except Exception:
            pass
        try:
            import field_tidy as ft
            fields, tnotes = ft.tidy(fields)
            notes += [f"field_tidy:{t}" for t in (tnotes or [])][:4]
        except Exception:
            pass
        for mk, lim in (("Мета наименование", 60), ("Мета описание", 160)):
            v = str(fields.get(mk) or "")
            if len(v) > lim:
                fields[mk] = v[:lim].rsplit(" ", 1)[0].rstrip(" ,;-")

        # ---- 7b) claims audit: mechanical fabrication check; violations get a
        # reviewer-agent quick look (owner 2026-07-18) — only a confirmed fabrication
        # flags the product or swaps in a cleaned description.
        try:
            import claims_audit as ca
            _viols = ca.audit(fields, scrape_desc)
            if _viols:
                notes.append("claims:" + ",".join(_viols[:4]))
                _cv = ca.review(fields, _viols, scrape_desc)
                if _cv.get("реален_проблем"):
                    _fixed = str(_cv.get("коригирано_описание") or "").strip()
                    _nv = (ca.audit(dict(fields, **{"Описание": _fixed}), scrape_desc)
                           if _fixed else _viols)
                    if _fixed and set(_nv) < set(_viols):   # correction must improve
                        fields["Описание"] = _fixed
                        notes.append("claims_fixed")
                        if _nv:                             # e.g. meta-only leftovers
                            notes.append("claims_flagged")
                    else:
                        notes.append("claims_flagged")
                elif _cv:
                    notes.append("claims_reviewed_ok")
                else:
                    notes.append("claims_review_unavailable")
        except Exception as _cae:
            notes.append(f"claims_error:{str(_cae)[:40]}")

        # ---- 8) vision verification of the FINAL record (flag-only) -------------
        vision_ok = None
        vr = None
        img_url = str(gt.get("Снимка") or "").strip()
        try:
            if img_url:
                vr = ro.verify_against_image(img_url, fields)
                if vr and vr.get("mismatch"):
                    notes.append("vision_mismatch")
                    vision_ok = False
                elif vr and vr.get("ok"):
                    notes.append("vision_ok")
                    vision_ok = True
                else:
                    notes.append("image_unverified")
            else:
                notes.append("image_unverified")
        except Exception as _ve:
            notes.append(f"vision_error:{str(_ve)[:40]}")
        # photo-read brand joins the evidence pool
        _pending_sources = [s0 for s0, _v0 in _bsources if _v0]
        try:
            _vb = ((vr or {}).get("detail") or {}).get("видим_бранд") if img_url else None
            if _vb and not fields.get("Бранд"):
                _vsources = [("vision", _vb),
                             ("slot", brand_tools.slot_candidate(stoka)),
                             ("scrape", gt.get("Бранд (скрейп)"))]
                _b2, _bn2, _bp2 = brand_tools.gather(code, _vsources)
                notes += [n for n in _bn2 if n not in notes]
                if _b2:
                    fields["Бранд"] = _b2
                    notes.append("brand_from_vision_corroborated")
                elif _bp2:
                    _bpending = _bp2
                    _pending_sources = [s0 for s0, _v0 in _vsources if _v0]
        except Exception:
            pass
        if _bpending:
            brand_tools.queue_candidate(code, _bpending, _pending_sources, stoka)
            notes.append("brand_candidate_queued")

        # ---- 9) verdicts ---------------------------------------------------------
        ru_bad = ro.russian_survivors(" ".join(str(fields.get(k) or "") for k in
                                               ("Наименование", "Описание", "Атрибути")))
        if ru_bad:
            notes.append("russian_survivors:" + ",".join(list(ru_bad)[:3]))
        # off-list attribute VALUES are usually legitimate (Shopify's per-leaf lists are
        # incomplete) — they don't force review; only an extreme count is anomalous.
        # texts_missing forces review only if the description actually came out empty.
        _text_empty = not str(fields.get("Описание") or "").strip() or \
            not str(fields.get("Мета описание") or "").strip()
        needs_human = (("leaf_branch_mismatch" in notes and confidence != "висока")
                       or confidence == "ниска" or n_other >= 6 or weak
                       or vision_ok is False or bool(ru_bad)
                       or (bool(texts_missing) and _text_empty)
                       or "leaf_disagree_unresolved" in notes
                       or "claims_flagged" in notes)
        conf_out = ("high" if confidence == "висока" and vision_ok is not False
                    else "medium" if confidence in ("висока", "средна")
                    else "low")
        usage = telemetry.summary()
        try:
            import quality_flags as qf
        except Exception:
            qf = None
        rec = {"code": code, "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
               "fields": fields, "confidence": conf_out,
               "needs_human": bool(needs_human),
               "meta": {"pipeline": "v2", "leaf_gid": leaf["gid"],
                        "leaf_name": leaf["bg"], "leaf_full": leaf["full"],
                        "notes": notes, "primary_model": model2,
                        "duration_s": round(time.time() - t0, 1),
                        "usage": usage}}
        if qf:
            try:
                _qf_need, _qf_flags = qf.needs_human(rec)   # returns (bool, flags-list)!
                if _qf_need:
                    rec["needs_human"] = True
                    notes.append("quality_flags_forced:" +
                                 ",".join(sorted({c for c, _s, _d in _qf_flags})))
            except Exception:
                pass
        # monotonic quality gate: a worse rerun must not overwrite a better canonical.
        # BYPASSED in deliberate reprocess mode (V2_REPROCESS) — the whole point is to
        # replace a v1-text-fallback record with a fresh full-v2 one, which the gate would
        # otherwise block on a marginal confidence dip; consensus + guards still protect
        # each product within the run.
        if __import__("os").environ.get("V2_REPROCESS") != "1":
            try:
                rec2, _qg = ro._quality_gate(code, rec)
                if rec2 is None:
                    ro.log(f"SKIP {code}: {_qg} — kept better existing version")
                    ro.mark_done(code)
                    return "done"
                rec = rec2
            except Exception:
                pass
        with open(ro.RESULTS_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        for _try in range(3):
            try:
                db.record_version(rec)
                break
            except Exception as _dbe:
                if _try == 2:
                    ro.log(f"  WARN {code}: DB write failed ({str(_dbe)[:60]}) — "
                           f"JSONL written; reconcile will heal")
                    # keep the code visible to the v2 done-set (which is DB-driven)
                    # so other lanes don't re-run the product before reconcile heals
                    try:
                        with open(HERE / "v2_done_pending.jsonl", "a",
                                  encoding="utf-8") as _pf:
                            _pf.write(json.dumps({"code": code}) + "\n")
                    except Exception:
                        pass
                else:
                    time.sleep(1.5)
        if _desc_hash:
            try:
                with open(ro.DESC_HASHES_PATH, "a", encoding="utf-8") as f:
                    f.write(f"{_desc_hash} {code}\n")
            except Exception:
                pass
        try:
            con = db.connect()
            con.execute("INSERT OR REPLACE INTO product_taxonomy VALUES (?,?,?,?)",
                        (code, leaf["gid"], leaf["full"], "v2"))
            con.commit()
            con.close()
        except Exception:
            pass
        ro.mark_done(code)
        ro.log(f"OK {code} in {time.time()-t0:.1f}s (v2, leaf={leaf['bg']}, "
               f"conf={confidence}, needs_human={rec['needs_human']})")
        return "done"
    except Exception as e:
        ro.log(f"FAIL {code} (v2): {str(e)[:120]}")
        with open(ro.FAILURES_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps({"code": code, "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                "error": str(e)[:300], "pipeline": "v2"},
                               ensure_ascii=False) + "\n")
        return "failed"
