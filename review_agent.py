# -*- coding: utf-8 -*-
"""Final QA reviewer agent — takes the owner's job of looking over the finished
product before it goes live. For each product it runs deterministic pre-checks
(catalogue codes in name/description, meta SEO lengths, attribute completeness,
name/attr format, image liveness via the download manifest, brand/related sanity)
and THEN an autonomous agent that inspects the photo, verifies the brand is real
AND makes home goods, judges the related products and the website presentation,
and decides what is best. It reports TWO things:
  1. per-product verdict (ready-for-site? + concrete issues + fixes)
  2. SYSTEMIC recommendations — how to instruct the processing agents better, which
     edge cases are missed, what to fix in the pipeline.

Run:
  python review_agent.py <code> [--verbose]          # review one product
  python review_agent.py --sample N [--flagged]      # review N finished products -> review_report.md
"""
import io, json, os, re, ssl, sys, time, urllib.parse, urllib.request, glob, collections, shutil
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import run_one
import brand_tools
import relate_tools
import catalogue_guard as cg
import filter_schema_store as fss    # living per-category filter schema (reviewer-adjustable)
import agent_enrich as ae            # reuse chat / _fetch / _vision_ask / _web_search

_CTX = ssl.create_default_context(); _CTX.check_hostname = False; _CTX.verify_mode = ssl.CERT_NONE
_UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) review-agent/1.0"}
MANIFEST = HERE.parent / "image-pipeline" / "manifest.jsonl"
REPORT = HERE / "review_report.md"
REVIEW_FIXES = HERE / "review_fixes.jsonl"     # proposals + verdicts for the 1-click review site
MAX_STEPS = 12

# SEO length windows (Google): title ~50-60 chars, description ~120-160 chars.
SEO = {"title": (35, 60), "desc": (70, 160)}


# --------------------------------------------------------------- data loading
def load_records():
    by = {}
    for f in [HERE / "results.jsonl", *HERE.glob("results.lane*.jsonl")]:
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("code") and "agentic" in ((d.get("meta") or {}).get("notes") or []):
                by[d["code"]] = d
    return by


def load_sources():
    src = {}
    for line in open(HERE / "tasks.jsonl", encoding="utf-8", errors="replace"):
        if not line.strip():
            continue
        try:
            t = json.loads(line)
        except Exception:
            continue
        src[t.get("code")] = t
    return src


def load_manifest():
    m = {}
    if MANIFEST.exists():
        for line in open(MANIFEST, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("code"):
                m[d["code"]] = d
    return m


# --------------------------------------------------------------- tools
def _check_url(url):
    """Is the image live? Returns 'ok N bytes', 'DEAD <status>', or an error."""
    if not url:
        return "(няма URL)"
    try:
        req = urllib.request.Request(run_one._encode_url(url), headers=_UA, method="GET")
        r = urllib.request.urlopen(req, timeout=20, context=_CTX)
        data = r.read(2048)
        return f"жива (HTTP {r.status}, тип {r.headers.get('Content-Type','?')})" if data else "празна"
    except urllib.error.HTTPError as e:
        return f"МЪРТВА (HTTP {e.code})"
    except Exception as e:
        return f"грешка ({str(e)[:60]})"


def run_tool(name, args, ctx):
    if name == "analyze_image":
        return ae._vision_ask(ctx["image_url"], args.get("question", "Опиши подробно продукта."))
    if name == "check_image":
        return _check_url(ctx["image_url"])
    if name == "fetch_url":
        return ae._fetch(args.get("url", ""))
    if name == "web_search":
        return ae._web_search(args.get("query", ""))
    if name == "lookup_brand":
        return json.dumps({"canonical": brand_tools.lookup(args.get("name", ""))}, ensure_ascii=False)
    if name == "adjust_filter_schema":
        # Evolve the LIVING category schema when the hard rules don't fit. Add or
        # remove filter groups, or replace the whole list. Always give a reason.
        cat = str(args.get("category") or ctx.get("category") or "").strip()
        reason = str(args.get("reason") or "").strip()
        if not cat or not reason:
            return "нужни: category и reason"
        cur = fss.get_filters(cat)
        if isinstance(args.get("groups"), list):
            newg = args["groups"]
        else:
            remove = {str(x).strip().lower() for x in (args.get("remove") or [])}
            newg = [g for g in cur if str(g.get("група", "")).strip().lower() not in remove]
            for g in (args.get("add") or []):
                if isinstance(g, dict) and g.get("група"):
                    newg = [x for x in newg if str(x.get("група")) != str(g["група"])] + [g]
        ok = fss.adjust(cat, newg, reason, by=f"reviewer:{ctx.get('code','?')}")
        return f"схемата за '{cat}' е обновена: {json.dumps(newg, ensure_ascii=False)}" if ok else "неуспех при запис"
    return f"(непознат инструмент: {name})"


# --------------------------------------------------------------- deterministic pre-check
_GENERIC_CODE = re.compile(r"(?<![0-9A-Za-zА-Яа-я])[A-Za-zА-Яа-я]{1,4}-?\d{2,}[A-Za-z]{0,2}(?![0-9A-Za-zА-Яа-я])")
_DIMCTX = re.compile(r"[×xX*]\s*$|^\s*[×xX*]|\d\s*(cm|см|mm|мм|ml|мл|l|л|g|г|kg|кг)", re.I)


def _parse_attrs(attrs):
    keys = {}
    for part in str(attrs or "").split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            keys[k.strip().lower()] = v.strip()
    return keys


def precheck(rec, task, manifest):
    f = rec.get("fields") or {}
    src_stoka = (task.get("ground_truth") or {}).get("Стока") if task else None
    name = str(f.get("Наименование") or "")
    desc = str(f.get("Описание") or "")
    mtitle = str(f.get("Мета наименование") or "")
    mdesc = str(f.get("Мета описание") or "")
    brand = str(f.get("Бранд") or "").strip()
    attrs = _parse_attrs(f.get("Атрибути"))
    related = str(f.get("Свързани") or "").strip()
    issues = []

    # 1. catalogue codes leaked into name / description
    src_codes = set(cg.source_model_codes(src_stoka)) if src_stoka else set()
    for text, where in ((name, "Наименование"), (re.sub(r"<[^>]+>", " ", desc), "Описание")):
        hits = []
        for c in src_codes:
            if re.search(r"(?<![0-9A-Za-zА-Яа-я])" + re.escape(c) + r"(?![0-9A-Za-zА-Яа-я])", text, re.I):
                hits.append(c)
        for m in _GENERIC_CODE.finditer(text):
            tok = m.group(0)
            a, b = m.span()
            prev = text[a - 1] if a > 0 else " "
            nxt = text[b:b + 6]
            prefix = re.match(r"[A-Za-zА-Яа-я]+", tok).group(0)
            # skip dimensions / measurements, not catalogue codes
            if prev in "×xX*/.," or prev.isdigit():
                continue
            if re.match(r"[.,]\d", nxt):                       # 'h21.5'
                continue
            if re.match(r"\s*(?:cm|см|mm|мм|ml|мл|lt|l|л|g|гр|г|kg|кг)\b", nxt, re.I):
                continue
            if re.match(r"\s*[×xX*]", nxt):
                continue
            if len(prefix) == 1 and prefix in cg._DIM_LETTER:  # 'h60', 'В30'
                continue
            if tok.upper() not in {h.upper() for h in hits}:
                hits.append(tok)
        if hits:
            issues.append({"поле": where, "проблем": f"възможни каталожни кодове: {', '.join(sorted(set(hits))[:6])}",
                           "тежест": "висока", "тип": "catnum"})

    # 2. meta SEO lengths
    for key, val, label in (("title", mtitle, "Мета наименование"), ("desc", mdesc, "Мета описание")):
        lo, hi = SEO[key]
        if not val:
            issues.append({"поле": label, "проблем": "празно", "тежест": "средна", "тип": "seo"})
        elif len(val) > hi:
            issues.append({"поле": label, "проблем": f"{len(val)} знака (>{hi}, Google съкращава)", "тежест": "средна", "тип": "seo"})
        elif len(val) < lo:
            issues.append({"поле": label, "проблем": f"само {len(val)} знака (<{lo}, твърде късо за SEO)", "тежест": "ниска", "тип": "seo"})

    # 3. attribute completeness — the product must be FILTERABLE by its CATEGORY's
    # filters (a lamp needs volts/lumens/fitting, a bowl needs material/colour/volume).
    _cat = str((task.get("product") or {}).get("Категории") or "").strip() if task else ""
    fs = fss.get_filters(_cat) or ((task.get("filter_schema") or []) if task else [])
    # NOTE: a missing group is only ADVISORY (ниска) — many groups are legitimately N/A
    # for a given product (Волтаж on a plate), and the enrichment prompt tells the agent to
    # skip inapplicable ones. Flagging every absent group at медиум produced systematic
    # false positives the reviewer had to burn tool calls dismissing.
    for grp in fs:
        gname = str(grp.get("група") or "").strip()
        if gname and not any(gname.lower() in k for k in attrs):
            issues.append({"поле": "Атрибути", "тип": "attr_missing", "тежест": "ниска",
                           "проблем": f"липсва филтър-атрибут '{gname}' (провери дали е приложим за този продукт)"})
    if not attrs:
        issues.append({"поле": "Атрибути", "тип": "attr_empty", "тежест": "висока",
                       "проблем": "НЯМА атрибути — продуктът е ненамираем по филтри"})

    # 4. brand sanity
    if not brand:
        issues.append({"поле": "Бранд", "проблем": "празно", "тежест": "ниска", "тип": "brand"})
    else:
        canon = brand_tools.lookup(brand)
        if not canon:
            issues.append({"поле": "Бранд", "проблем": f"'{brand}' не е в речника — потвърди че е реална марка за домакински стоки",
                           "тежест": "средна", "тип": "brand_unverified"})
        # A hyphen alone does NOT make a bad brand — many real brands are hyphenated
        # (Char-Broil). Only flag material-as-brand, or a hyphen on an UNconfirmed value.
        if brand.lower() in cg.MATERIAL_WORDS or ("-" in brand and not canon):
            issues.append({"поле": "Бранд", "проблем": f"'{brand}' изглежда като материал/съставна представка, не марка",
                           "тежест": "висока", "тип": "brand_bad"})

    # 5. name format — should not be empty, not start lowercase, no double spaces / stray punctuation
    if len(name) < 8:
        issues.append({"поле": "Наименование", "проблем": "твърде кратко/липсва", "тежест": "висока", "тип": "name"})
    if re.search(r"\s{2,}|\s[-–,]\s|\(\s|\s\)", name):
        issues.append({"поле": "Наименование", "проблем": "форматен дефект (двойни интервали/висящи тирета/скоби)", "тежест": "ниска", "тип": "name_format"})

    # 6. image liveness (from the download manifest; agent re-checks live)
    mi = manifest.get(rec.get("code"))
    if mi and str(mi.get("status")) == "error":
        issues.append({"поле": "Снимка", "проблем": f"свалянето се провали ({mi.get('url','')[:60]}) — вероятно 404",
                       "тежест": "висока", "тип": "image_dead"})
    elif not mi:
        issues.append({"поле": "Снимка", "проблем": "няма запис в manifest — изображението не е сваляно", "тежест": "средна", "тип": "image_missing"})

    # 7. related present?
    if not related:
        issues.append({"поле": "Свързани", "проблем": "празно (възможно ок, ако няма варианти)", "тежест": "ниска", "тип": "related"})
    return issues


SYSTEM = """Ти си ФИНАЛНИЯТ проверител (QA) на български онлайн магазин за домакински стоки —
последната инстанция преди продуктът да излезе на сайта, вместо собственика. Мислиш какво е
най-добре за КЛИЕНТА и за представянето на сайта. Имаш автономия и правиш собствени преценки,
дори за неща, които не са ти изрично казани — ако видиш нещо нередно, действай/докладвай.

Даден ти е ФИНАЛЕН продукт, достоверните данни, снимката, филтрите за категорията, списък
АВТОМАТИЧНИ НАХОДКИ (детерминистична предпроверка) и — когато има — ИСТОРИЯ НА ПРОДУКТА
(хронология какво и кога е променял всеки етап). Провери всичко с инструментите и прецени.

ИЗПОЛЗВАЙ ИСТОРИЯТА: тя показва как е стигнал продуктът до сегашния си вид. Ако виждаш стъпка,
маркирана ⚠️ПО-ЗЛЕ (регресия) — верен бранд/факт е бил ЗАГУБЕН, или каталожен код е бил ВЪРНАТ
на по-късен етап — това е сериозен сигнал: сравни сегашната стойност с по-ранната и ако
по-ранната е била по-добра, посочи го в 'проблеми', върни добрата стойност в 'автопоправки' и
опиши в 'системни_препоръки' кой етап е причинил регресията, за да се поправи процесът. Историята
ти казва и кои стойности вече са били ПОТВЪРДЕНИ (напр. бранд, проверен със снимка/web) — не ги
подлагай на съмнение без основание.


1. НАИМЕНОВАНИЕ: без каталожни/артикулни кодове; КОНВЕНЦИЯ: Бранд + Материал(прил.,
   съгласувано по род) + Форма(прил.) + каноничен ТИП + Размер (пример: 'Alkan Züccaciye
   Акрилен правоъгълен капак 34,5×54,5 см'); правилен български род ('акрилна купа', не
   'акрилен купа'); каноничен тип от речника (Дозатор, не пурер/диспенсър). Реалните
   продуктови линии (напр. 'Elite Multi') СЕ ЗАПАЗВАТ.
2. ОПИСАНИЕ: четимо, точно и НЕ противоречи на снимката (форма/материал/покритие/цвят/брой);
   без каталожни номера; без непотвърдени серии/твърдения (halлюцинации); валиден, четим HTML;
   не е генеричен пълнеж. Единиците — еднородни (ml навсякъде, не 'сс').
3. МАРКА: реална ли е И прави ли ДОМАКИНСКИ стоки (не дрехи/парфюми/друга индустрия)? Провери с
   web_search/lookup_brand. Ако полето съдържа продуктова линия, а истинската марка е друга —
   посочи истинската. Еднообразен регистър (COPPE, не Coppe). Никога материал/представка като марка.
4. АТРИБУТИ — ЦЕЛТА: клиентът да намира продукта чрез ФИЛТРИ. Продуктът трябва да покрива
   приложимите филтър-групи за КАТЕГОРИЯТА си (различни са: лампа→Волтаж/Лумени/Фасонка/Тип
   светлина; купа→Материал/Цвят/Обем/Форма). Всеки продукт — с подходящи филтруеми атрибути,
   не празно. Еднообразен формат 'Ключ: Стойност'. Стойности по вокабуляра на филтрите. Без
   отгатване (цвят/материал само при потвърждение).
   СХЕМАТА НА ФИЛТРИТЕ Е ЖИВА И Я КОРИГИРАШ ТИ. Ако видиш, че твърдо правило не пасва на
   категорията — филтър-група, която НЕ е приложима за тези продукти (напр. 'Форма' за лампи),
   или ЛИПСВАЩА група, която клиентите биха ползвали (напр. 'Лумени', 'Фасонка' за осветление) —
   използвай adjust_filter_schema, за да добавиш/премахнеш групи за категорията (с причина).
   Така схемата се подобрява с времето. Прави го внимателно и само при ясен случай.
5. СВЪРЗАНИ: трябва да са СЪЩИЯТ продукт в друг размер/цвят/форма — не случайни. Ако има явни
   варианти (аромати, цветове, размери) в асортимента, отбележи ги.
6. МЕТА (SEO): Мета наименование ≤60 знака; Мета описание ≤160 знака; добре написани, с ключови
   думи; уникални (не копие на описанието).
7. СНИМКА: жива ли е (check_image; мъртва/404 = висок приоритет); показва ли ясно продукта; бял
   фон; без воден знак на магазин; съответства ли на продукта.
8. СИНОНИМИ: полезни ли са за търсене (алтернативни имена, които клиент би написал).
9. КАТЕГОРИЯ: правилна ли е за този продукт.
10. ОБЩО: би ли се доверил клиент на тази обява? Изглежда ли професионално?

РАЗДЕЛИ поправките на ДВЕ:
- "автопоправки": БЕЗОПАСНИ, детерминистични корекции, които да се приложат АВТОМАТИЧНО
  (регистър на марка, единици→ml, съкращаване на мета до дължина, преформатиране на атрибути,
  граматичен род/число, махане на явен каталожен код). Дай {"поле": "нова цялостна стойност"}.
- "предложения": корекции, изискващи преценка (пренаписване на описание спрямо снимка, смяна на
  марка, добавяне на варианти) — за 1-клик одобрение на сайта. Дай стар→нов + причина.

СЛЕД това дай СИСТЕМНИ ПРЕПОРЪКИ: как да се инструктират по-добре обработващите агенти, кои
гранични случаи се пропускат, какво да се поправи в процеса. Пример: марка 'NEVE' за хладилна
чанта, а истинската е 'CN Continental', и откриваш че NEVE прави дрехи, не домакинско →
препоръчай инструкция агентите да проверяват дали марката прави ДОМАКИНСКИ стоки.

ФОРМАТ — на всяка стъпка ТОЧНО един ред:  TOOL <име> <json>   или   FINAL <json>
Инструменти: analyze_image {"question"}, check_image {}, fetch_url {"url"}, web_search {"query"},
  lookup_brand {"name"},
  adjust_filter_schema {"category":"...", "add":[{"група":"...","стойности":"..."}], "remove":["група"], "reason":"..."}.
FINAL json схема:
{"готов_за_сайта": true/false, "оценка": "кратка обща оценка",
 "проблеми": [{"поле","проблем","тежест":"висока/средна/ниска","поправка"}],
 "автопоправки": {"<поле>": "<нова стойност>"},
 "предложения": [{"поле","стар","нов","причина"}],
 "системни_препоръки": [{"наблюдение","препоръка"}]}
Работи стъпка по стъпка. Не измисляй резултати от инструменти.

КООРДИНИРАНИ ПРЕДЛОЖЕНИЯ: когато проблемът е грешен ТИП на продукта (напр. плато,
класифицирано като щипка), предложението ТРЯБВА да включва ЗАЕДНО: (1) Атрибути с
поправен "Тип: ...", (2) Наименование, пресъставено с верния тип, (3) ако е явно —
и правилната категория-лист. Никога само името: името се сглобява от атрибутите, така
че поправка само на името ще бъде презаписана.
"""


def review_one(code, verbose=False):
    records = review_one._cache.get("records") or load_records()
    sources = review_one._cache.get("sources") or load_sources()
    manifest = review_one._cache.get("manifest") or load_manifest()
    review_one._cache.update(records=records, sources=sources, manifest=manifest)
    rec = records.get(code)
    if not rec:
        # legacy-path records (no 'agentic' note) are absent from load_records but ARE in
        # the DB canonical — without this fallback they error forever and clog the queue.
        try:
            import db as _db
            rec = _db.canonical_records().get(str(code))
        except Exception:
            rec = None
    if not rec:
        return {"error": f"no finished record for {code}"}
    task = sources.get(code, {})
    f = rec.get("fields") or {}
    image_url = ((task.get("product") or {}).get("Снимки") or "").split(";")[0].strip()
    category = str((task.get("product") or {}).get("Категории") or "").strip()
    ctx = {"code": code, "image_url": image_url, "category": category}
    auto = precheck(rec, task, manifest)
    gt = {k: v for k, v in (task.get("ground_truth") or {}).items() if v is not None}
    fs = fss.get_filters(category) or task.get("filter_schema") or []
    try:
        import history as _hist
        hist = _hist.history_summary(code)
    except Exception:
        hist = ""
    hist_block = (f"{hist}\n\n" if hist else "")
    user = (f"ФИНАЛЕН ПРОДУКТ (код {code}).\nПолета:\n{json.dumps(f, ensure_ascii=False, indent=1)}\n\n"
            f"Снимка: {image_url or 'няма'}\n\nДОСТОВЕРНИ ДАННИ:\n{json.dumps(gt, ensure_ascii=False, indent=1)}\n\n"
            f"{hist_block}"
            f"ФИЛТРИ ЗА КАТЕГОРИЯТА (продуктът трябва да е намираем по всеки приложим):\n"
            f"{json.dumps(fs, ensure_ascii=False, indent=1)}\n\n"
            f"АВТОМАТИЧНИ НАХОДКИ (провери ги и добави преценка):\n{json.dumps(auto, ensure_ascii=False, indent=1)}\n\n"
            "Прегледай продукта като финален проверител. Започни.")
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": user}]
    log = []
    for step in range(MAX_STEPS):
        if step == MAX_STEPS - 2:
            messages.append({"role": "user", "content": "Остават малко стъпки — на следващата върни FINAL."})
        out = ae.chat(messages).strip()
        messages.append({"role": "assistant", "content": out})
        line = out.splitlines()[0].strip() if out else ""
        if verbose:
            print(f"[{step+1}] {out[:300]}")
        if "FINAL" in line.upper():
            raw = out[out.upper().index("FINAL") + 5:].strip()
            m = re.search(r"\{.*\}", raw, re.DOTALL)
            verdict = None
            if m:
                try:
                    verdict = json.loads(m.group(0))
                except Exception:
                    verdict = run_one.extract_json(raw)
            if verdict and (verdict.get("проблеми") or verdict.get("системни_препоръки") or verdict.get("оценка")):
                verdict["_auto"] = auto
                verdict["_log"] = log
                return {"code": code, "verdict": verdict}
            break   # empty/invalid FINAL -> forced focused final below
        m = re.match(r"TOOL\s+(\w+)\s*(\{.*\})?", line, re.IGNORECASE)
        if m:
            try:
                targs = json.loads(m.group(2)) if m.group(2) else {}
            except Exception:
                targs = {}
            result = run_tool(m.group(1), targs, ctx)
            log.append({"tool": m.group(1), "result": str(result)[:200]})
            if verbose:
                print(f"   -> {m.group(1)} = {str(result)[:150]}")
            messages.append({"role": "user", "content": f"Резултат от {m.group(1)}:\n{result}\n\nПродължи."})
        else:
            messages.append({"role": "user", "content": "Върни ТОЧНО един ред: TOOL <име> <json> или FINAL <json>."})
    # Forced final — fresh focused prompt seeded with the investigation (the long
    # ReAct convo degrades JSON on free models; a clean prompt is reliably parseable).
    summary = "; ".join(f"{l['tool']}={str(l['result'])[:120]}" for l in log)
    fp = [{"role": "system", "content": "Ти си финален QA проверител на домакински стоки. "
           "Пишеш чист български. Върни САМО валиден JSON."},
          {"role": "user", "content": user + f"\n\nОТКРИТО ПРИ ПРОВЕРКАТА (инструменти): {summary}\n\n"
           'Върни САМО JSON: {"готов_за_сайта": true/false, "оценка": "кратка оценка", '
           '"проблеми": [{"поле":"","проблем":"","тежест":"висока/средна/ниска","поправка":""}], '
           '"автопоправки": {}, "предложения": [{"поле":"","стар":"","нов":"","причина":""}], '
           '"системни_препоръки": [{"наблюдение":"","препоръка":""}]}'}]
    verdict = None
    try:
        raw = ae.chat(fp, max_tokens=1400).strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        verdict = json.loads(m.group(0)) if m else run_one.extract_json(raw)
    except Exception:
        verdict = None
    if not verdict:
        verdict = {"готов_за_сайта": None, "оценка": "reviewer не завърши", "проблеми": auto,
                   "системни_препоръки": []}
    verdict["_auto"] = auto
    verdict["_log"] = log
    return {"code": code, "verdict": verdict}


review_one._cache = {}


def run_sample(n, flagged_only=False):
    records = load_records()
    review_one._cache.update(records=records, sources=load_sources(), manifest=load_manifest())
    codes = list(records)
    if flagged_only:
        codes = [c for c in codes if records[c].get("needs_human")]
    # spread across the catalogue: take every k-th
    step = max(1, len(codes) // n)
    picks = codes[::step][:n]
    results = []
    for i, c in enumerate(picks):
        print(f"[{i+1}/{len(picks)}] reviewing {c} ...")
        try:
            results.append(review_one(c))
        except Exception as e:
            results.append({"code": c, "error": str(e)[:120]})
    _write_report(results)
    apply_fixes(results)
    return results


def apply_fixes(results):
    """Auto-apply the reviewer's SAFE fixes to the stored records (validated, to
    EDITABLE text fields only), and log every proposal + verdict to review_fixes.jsonl
    for the review site to surface as 1-click approvals."""
    editable = set(getattr(run_one, "EDITABLE", []))
    autos, props = {}, []
    for r in results:
        v = r.get("verdict") or {}
        code = r.get("code")
        af = v.get("автопоправки") or {}
        # keep only safe, non-empty replacements to editable text fields
        clean_af = {k: str(val).strip() for k, val in af.items()
                    if k in editable and isinstance(val, (str, int, float))
                    and str(val).strip() and k != "Свързани"}
        if clean_af:
            autos[code] = clean_af
        if v.get("предложения") or clean_af:
            props.append({"code": code, "ts": datetime.now().isoformat(timespec="seconds"),
                          "готов_за_сайта": v.get("готов_за_сайта"), "оценка": v.get("оценка"),
                          "автоприложени": clean_af, "предложения": v.get("предложения") or [],
                          "проблеми": v.get("проблеми") or []})
    with open(REVIEW_FIXES, "a", encoding="utf-8") as f:
        for p in props:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    if not autos:
        print("apply_fixes: no safe auto-fixes"); return
    # APPEND-ONLY application (was: in-place rewrite of the live lane files, which
    # destroyed the pre-fix version AND raced the lanes). We instead append a corrected
    # VERSION of each product's canonical record to a dedicated file no lane writes to:
    #   * the pre-fix version is preserved -> full history/timeline stays intact,
    #   * no write race with the running pipeline,
    #   * ts is bumped so the fix wins last-wins; 'z_review' sorts last for the
    #     file-order consumer. Reversible: delete results.lanez_review.jsonl.
    from datetime import timedelta
    REVIEW_OUT = HERE / "results.lanez_review.jsonl"
    # Base each fix on the TRUE canonical (including this lane's own earlier fixes —
    # excluding them made a round-2 autofix silently REVERT round-1's). ts is bumped past
    # BOTH the base ts and now, so no same-second collision drops the version row.
    recs = []
    for fp in glob.glob(str(HERE / "results.lane*.jsonl")):
        for line in open(fp, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                recs.append(json.loads(line))
            except Exception:
                pass
    canon = {}
    for d in sorted(recs, key=lambda d: d.get("ts") or ""):
        if d.get("code"):
            canon[str(d["code"])] = d
    changed = 0
    # per-process output file: concurrent fleet processes appending one file can tear
    # long JSON lines; the results.lane* glob picks this up like any other lane file.
    out_path = HERE / f"results.lanez_review{os.getpid()}.jsonl"
    with open(out_path, "a", encoding="utf-8") as out:
        for code, fix in autos.items():
            d = canon.get(str(code))
            if not d:
                continue
            fl = dict(d.get("fields") or {})
            applied = [k for k, val in fix.items() if str(fl.get(k)) != val]
            if not applied:
                continue
            for k in applied:
                fl[k] = fix[k]
            nd = dict(d)
            nd["fields"] = fl
            try:
                base = datetime.fromisoformat(d.get("ts") or "") + timedelta(seconds=2)
            except Exception:
                base = datetime.now()
            nd["ts"] = max(base, datetime.now()).isoformat(timespec="seconds")
            meta = dict(nd.get("meta") or {})
            meta["notes"] = list(meta.get("notes") or []) + ["reviewer_autofix:" + ",".join(applied)]
            nd["meta"] = meta
            out.write(json.dumps(nd, ensure_ascii=False) + "\n")
            out.flush()
            try:
                import db as _db
                _db.record_version(nd)
            except Exception:
                pass
            changed += 1
    print(f"apply_fixes: appended {changed} corrected versions -> {out_path.name} "
          f"(pre-fix version preserved); {len(props)} proposals -> review_fixes.jsonl")


def _write_report(results):
    issue_kinds = collections.Counter()
    systemic = []
    not_ready = 0
    lines = ["# Финален QA преглед — доклад\n",
             f"Прегледани продукти: {len(results)}\n"]
    per = []
    for r in results:
        v = r.get("verdict") or {}
        if r.get("error"):
            per.append(f"- **{r['code']}** — грешка: {r['error']}")
            continue
        ready = v.get("готов_за_сайта")
        if ready is False:
            not_ready += 1
        probs = v.get("проблеми") or []
        for p in probs:
            issue_kinds[str(p.get("тип") or p.get("поле") or "?")] += 1
        for s in (v.get("системни_препоръки") or []):
            systemic.append((r["code"], s))
        tag = "✅" if ready else ("❌" if ready is False else "…")
        summ = v.get("оценка", "")
        pl = "; ".join(f"[{p.get('тежест','?')}] {p.get('поле','')}: {p.get('проблем','')}" for p in probs[:6])
        per.append(f"- {tag} **{r['code']}** — {summ}\n    {pl}")
    lines.append(f"Не са готови за сайта: {not_ready}/{len(results)}\n")
    lines.append("\n## Най-чести проблеми\n")
    for k, n in issue_kinds.most_common():
        lines.append(f"- {k}: {n}")
    lines.append("\n## СИСТЕМНИ ПРЕПОРЪКИ (към процеса/инструкциите)\n")
    for code, s in systemic:
        obs = s.get("наблюдение", "") if isinstance(s, dict) else str(s)
        rec = s.get("препоръка", "") if isinstance(s, dict) else ""
        lines.append(f"- ({code}) **{obs}** → {rec}")
    lines.append("\n## Продукти\n")
    lines += per
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nreport -> {REPORT}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--sample" in args:
        n = int(args[args.index("--sample") + 1])
        run_sample(n, flagged_only="--flagged" in args)
    elif args and not args[0].startswith("--"):
        r = review_one(args[0], verbose="--verbose" in args)
        print(json.dumps(r.get("verdict", r), ensure_ascii=False, indent=2))
    else:
        print("usage: review_agent.py <code> [--verbose]  |  --sample N [--flagged]")
