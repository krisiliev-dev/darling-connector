# -*- coding: utf-8 -*-
"""Autonomous per-product enrichment agent.

Instead of a fixed pipeline, EACH product gets a capable model that investigates it
case-by-case with real tools — reads the supplier page, inspects the photo, checks the
shared brand gazetteer / verifies a brand, finds catalogue-number neighbours, searches
the web — decides for itself what to trust, and writes back a reusable technique to the
shared skill when it finds one. Guardrails (empiric values untouched, pure Bulgarian, no
guessing) are constraints, not a script.

ReAct loop over the free model chain (tool-calling emulated via a strict text protocol,
so it works on every provider). Run:  python agent_enrich.py <code> [--verbose]
"""
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import run_one          # reuse providers, chain, vision, prompt-builder
import brand_tools
import relate_tools

LEARNINGS = HERE / "agent_learnings.md"
# 14 -> 10 (2026-07-16): telemetry shows ~12 calls/product at 96% prompt-replay, i.e.
# ~112k tokens each. The last steps are usually redundant re-checks; a 10-step budget +
# the wrap-up nudge (MAX_STEPS-2) cuts ~25-30% of calls. Watch confidence/needs_human in
# telemetry — revert if quality dips.
MAX_STEPS = 10
_CTX = ssl.create_default_context()
_CTX.check_hostname = False
_CTX.verify_mode = ssl.CERT_NONE
_UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) enrich-agent/1.0"}


# ----------------------------------------------------------------- model chat
# Per-product worker-chain ordering, set by enrich() from difficulty routing. None => the
# default fast-first WORKER_CHAIN. A module global is safe: one product at a time per lane.
_CHAIN_OVERRIDE = None


def chat(messages, max_tokens=1200):
    """Multi-turn call over the exhausted-aware worker chain (difficulty-routed per
    product when _CHAIN_OVERRIDE is set)."""
    exhausted = run_one._load_exhausted()
    base = _CHAIN_OVERRIDE or run_one.WORKER_CHAIN
    chain = [a for a in base if a[a.index("-m") + 1] not in exhausted]
    if not run_one._dashscope_allowed():               # billing incident: dashscope opt-in only
        chain = [a for a in chain if a[a.index("--provider") + 1] != "dashscope-intl"]
    chain = chain or [a for a in base if a[a.index("--provider") + 1] != "dashscope-intl"]
    # Bound the failover walk: 35 models × 70s timeouts could pin a lane for ~40 min on a
    # single ReAct step (long enough for cron to steal the lock and DUPLICATE the shard).
    import os as _os
    if _os.environ.get("REVIEW_FLEET") == "1":
        # partition free capacity: lanes walk Mistral-first, the reviewer fleet walks the
        # reverse (Cerebras/zai first) — same pool, opposite ends, minimal collisions
        ds = [a for a in chain if a[a.index("--provider") + 1] == "dashscope-intl"]
        free = [a for a in chain if a[a.index("--provider") + 1] != "dashscope-intl"]
        chain = ds + free[::-1]
    chain = chain[:8]
    # Sanitize: strict providers (Cohere, Groq) reject a message with empty content
    # (happens when a model returns an empty turn). Replace empties with a placeholder
    # so one blank turn can't poison the whole conversation with a 400.
    messages = [m if (isinstance(m.get("content"), list) or str(m.get("content") or "").strip())
                else {**m, "content": "(празен ход)"} for m in messages]
    last = None
    for args in chain:
        model = args[args.index("-m") + 1]
        provider = args[args.index("--provider") + 1]
        base, key_env = run_one.DIRECT_PROVIDERS[provider]
        try:
            client = run_one._direct_client(base, key_env)
            # Explicit short timeout: on the flaky free providers a call that takes
            # >70s is hanging/overloaded — fail over to the next model, don't block.
            r = client.chat.completions.create(model=model, messages=messages,
                                               temperature=0.2, max_tokens=max_tokens,
                                               timeout=25 if provider == "nvidia" else 70)
            try:
                import telemetry as _tel
                _tel.record(model, provider, r)
            except Exception:
                pass
            return r.choices[0].message.content or ""
        except Exception as e:
            last = e
            run_one.maybe_pause_on_arrearage(e)   # circuit breaker: any charge -> pause all
            if run_one._is_quota_error(e) and model not in exhausted:
                run_one._mark_exhausted(model)
                exhausted.add(model)
            if "429" in str(e):
                time.sleep(2.5)                   # let per-second limits breathe before failover
    raise last or RuntimeError("no model")


# ----------------------------------------------------------------- tools
def _fetch(url, limit=6000):
    try:
        import lookup_cache as _lc
        _hit = _lc.get("fetch", f"{url}|{limit}")
        if _hit is not None:
            return _hit
    except Exception:
        _lc = None
    try:
        u = run_one._encode_url(url)
        html = urllib.request.urlopen(urllib.request.Request(u, headers=_UA),
                                      timeout=20, context=_CTX).read().decode("utf-8", "replace")
        text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
        text = re.sub(r"(?s)<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        res = text[:limit] or "(празна страница)"
        if _lc and not res.startswith("(празна"):
            _lc.put("fetch", f"{url}|{limit}", res)
        return res
    except Exception as e:
        return f"(грешка при извличане: {str(e)[:80]})"


# Vision chain: Alibaba Qwen-VL first (own free quota, reliable), NVIDIA only as last
# resort — offloads NVIDIA (which was saturated → analyze_image timeouts capping
# confidence). Each Qwen-VL model has its own 1M grant; exhausted-cache skips drained.
VL_CHAIN = [
    # Qwen-VL first (restored 2026-07-15); Groq Llama-4-Scout (multimodal) and NVIDIA
    # 90B as backups if Alibaba is unavailable.
    ("dashscope-intl", "qwen3-vl-plus"),
    ("dashscope-intl", "qwen-vl-max"),
    ("dashscope-intl", "qwen3-vl-flash"),
    ("mistral", "mistral-medium-2508"),               # frontier-class, vision, free tier
    ("groq", "meta-llama/llama-4-scout-17b-16e-instruct"),
    ("nvidia", None),  # None -> run_one.VISION_VERIFY_MODEL via the NVIDIA client
]


def _vision_ask(image_url, question):
    if not image_url:
        return "(няма снимка)"
    try:
        req = urllib.request.Request(run_one._encode_url(image_url), headers=_UA)
        data = urllib.request.urlopen(req, timeout=30, context=_CTX).read()
        from PIL import Image
        import base64
        im = Image.open(io.BytesIO(data)).convert("RGB")
        im.thumbnail((1024, 1024))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=85)
        b64 = base64.b64encode(buf.getvalue()).decode()
    except Exception as e:
        return f"(грешка при зареждане на снимка: {str(e)[:80]})"
    content = [{"type": "text", "text": "Отговори кратко на български. " + question},
               {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}]
    exhausted = run_one._load_exhausted()
    last = None
    for provider, model in VL_CHAIN:
        try:
            if provider == "dashscope-intl" and not run_one._dashscope_allowed():
                continue                               # billing incident: dashscope opt-in only
            if provider == "nvidia":
                client, m = run_one._nvidia_client(), run_one.VISION_VERIFY_MODEL
            else:
                if model in exhausted:
                    continue
                base, key_env = run_one.DIRECT_PROVIDERS[provider]
                client, m = run_one._direct_client(base, key_env), model
            r = client.chat.completions.create(
                model=m, messages=[{"role": "user", "content": content}],
                max_tokens=250, temperature=0, timeout=80)
            try:
                import telemetry as _tel
                _tel.record(m, provider, r)
            except Exception:
                pass
            return r.choices[0].message.content
        except Exception as e:
            last = e
            run_one.maybe_pause_on_arrearage(e)   # circuit breaker
            if provider != "nvidia" and run_one._is_quota_error(e):
                run_one._mark_exhausted(model)
                exhausted.add(model)
    return f"(грешка при преглед на снимка: {str(last)[:70]})"


def _web_search(query, n=5):
    """Real keyless web search via DuckDuckGo's HTML endpoint — titles + snippets +
    links, like googling. The agent can then fetch_url any promising result.
    Cached: the same brand/product query recurs across products."""
    try:
        import lookup_cache as _lc
        _hit = _lc.get("web", f"{query}|{n}")
        if _hit is not None:
            return _hit
    except Exception:
        _lc = None
    try:
        data = urllib.parse.urlencode({"q": query}).encode()
        html = urllib.request.urlopen(urllib.request.Request(
            "https://html.duckduckgo.com/html/", data=data, headers=_UA),
            timeout=20, context=_CTX).read().decode("utf-8", "replace")
        out = []
        for m in re.finditer(r'result__a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.S):
            url = re.sub(r"&amp;", "&", m.group(1))
            title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            # snippet
            sm = re.search(r'result__snippet[^>]*>(.*?)</a>', html[m.end():m.end() + 1500], re.S)
            snip = re.sub(r"<[^>]+>", "", sm.group(1)).strip()[:160] if sm else ""
            out.append(f"{title} — {snip} [{url}]")
            if len(out) >= n:
                break
        res = "\n".join(out) if out else "(няма резултати)"
        if _lc and out:                                # only cache real hits
            _lc.put("web", f"{query}|{n}", res)
        return res
    except Exception as e:
        # fallback: Wikipedia opensearch
        try:
            r = json.loads(urllib.request.urlopen(urllib.request.Request(
                "https://en.wikipedia.org/w/api.php?action=opensearch&limit=3&format=json&search="
                + urllib.parse.quote(query), headers=_UA), timeout=10, context=_CTX).read())
            return f"Wikipedia: {r[1]}" if len(r) > 1 and r[1] else f"(грешка: {str(e)[:50]})"
        except Exception:
            return f"(грешка при търсене: {str(e)[:60]})"


def run_tool(name, args, ctx):
    if name == "fetch_url":
        return _fetch(args.get("url", ""))
    if name == "analyze_image":
        return _vision_ask(ctx["image_url"], args.get("question", "Опиши продукта."))
    if name == "lookup_brand":
        return json.dumps({"canonical": brand_tools.lookup(args.get("name", ""))}, ensure_ascii=False)
    if name == "verify_brand":
        canon, note = brand_tools.resolve(args.get("name", ""), lambda p: chat(
            [{"role": "user", "content": p}], max_tokens=200), context=ctx.get("name", ""))
        return json.dumps({"canonical": canon, "note": note}, ensure_ascii=False)
    if name == "find_related":
        return json.dumps({"related": relate_tools.find_related(ctx["code"], args.get("cat", ""))},
                          ensure_ascii=False)
    if name == "web_search":
        return _web_search(args.get("query", ""))
    if name == "record_learning":
        txt = str(args.get("text", "")).strip()
        if txt:
            with open(LEARNINGS, "a", encoding="utf-8") as f:
                f.write(f"- ({ctx['code']}) {txt}\n")
        return "записано"
    return f"(непознат инструмент: {name})"


# ----------------------------------------------------------------- agent loop
SYSTEM = """Ти си експерт по продуктови данни за български онлайн магазин. Разследваш ЕДИН
продукт задълбочено, като истински човек-проверител: сверяваш данните със снимката, със
складовото име (Microinvest), със скрейпнатите данни на доставчика и при нужда със сайта
на доставчика и с интернет. Взимаш решения за всеки случай поотделно.

ПРАВИЛА (задължителни):
- Пиши само чист български. Никакви руски/сръбски думи, нито буквите ы, э, ё.
- НЕ променяй: Код, Цена, Количество, Мярка — те са дадени.
- БЕЗ КАТАЛОЖНИ КОДОВЕ никъде в клиентския текст (Наименование, Описание, Мета).
- ИМЕННА КОНВЕНЦИЯ (задължителна): Наименованието се КОНСТРУИРА от атрибутите по шаблона:
  Бранд + Материал(прилагателно, съгласувано по род) + Форма(прилагателно) + ТИП + Размер.
  Пример: 'Alkan Züccaciye Акрилен правоъгълен капак 34,5×54,5 см'. Системата нормализира
  името машинно СЛЕД теб — твоята ГЛАВНА задача са ТОЧНИТЕ атрибути: Тип (кратко
  съществително, каквото клиент търси — 'Дозатор', не 'пурер с дозиращ капак'), Материал,
  Форма, Размер/Обем. Грешен или липсващ Тип = грешно име. Складовото име
  (Microinvest) съдържа артефакти — МАХНИ ги: представки 'BR-','CN-','CNC-','COK-','AN-','HR-';
  кодове 'E2483','F8005','CT30','M-7711','K-2050','ZCP 570','(2192)','мод.170','T350'; вътрешни
  серийни кодове 'ZAR'.
- СЕРИИ/ПРОДУКТОВИ ЛИНИИ: ЗАПАЗИ в Наименованието име на серия/линия САМО ако е РЕАЛНА продуктова
  линия, която клиент би търсил (напр. 'Elite Multi', 'HORECANO Antique') — при съмнение провери.
  МАХНИ безсмислени вътрешни кодове/складови обозначения ('ZAR', 'OUTPERFORM' като складова
  папка). Ако не си сигурен дали е реална линия, по-добре я спомени в Описанието, а не в името.
- Марка ≠ материал и ≠ складова представка. 'ИНОКС', 'стомана', 'меламин', 'пластмаса' са
  материали, НЕ марки; 'BR', 'CN', 'COK' са складови представки, НЕ марки. Не ги слагай в Бранд.
- Не отгатвай. Пиши стойност само ако си я потвърдил (снимка/доставчик/известна марка).
- ЗАБРАНЕНИ ИЗМИСЛЕНИ „ДОКАЗАТЕЛСТВА“: НИКОГА не пиши регистрационни номера на марки
  (WIPO/EUIPO/№1188666), юридически лица („S.L.U.“, „ООД“), сертификати или изпитвания
  („потвърдено от сертификат“), нито конкретни сплави/стандарти на стоманата (AISI 304,
  18/10, 14/1), ОСВЕН ако точно това число присъства в достоверните данни. Такива твърдения
  звучат достоверно, но са измислица и носят правен риск. При липса — не споменавай изобщо.
- Марка: провери с lookup_brand/verify_brand/снимка/сайта на доставчика; използвай
  каноничния правопис; игнорирай водни знаци на магазини (EGERA, LEVENA...). Ако разчиташ
  само на името (без потвърждение), сложи увереност НЕ по-висока от средна и го отбележи.
- САМО ОСНОВНАТА ТЪРГОВСКА МАРКА в поле Бранд — едно име. НЕ слагай марка+линия/модел
  ('HFM DEFNE' -> Бранд='HFM', а 'DEFNE' е линия -> отива в Наименованието/Описанието, не в Бранд).
  НЕ слагай юридическото/пълното име на доставчика, ако то съдържа и производствена група + линия —
  извади само разпознаваемата потребителска марка (при съмнение провери с lookup_brand/web_search).
- СЪОТВЕТСТВИЕ МАРКА-КАТЕГОРИЯ: марката трябва правдоподобно да произвежда стоки от ТАЗИ категория.
  Ако web_search покаже, че марката е известна основно от ДРУГ бранш (напр. Hella = авточасти,
  DEFNE = подправки), НЕ я слагай наивно — потърси потвърждение, че прави и този тип стока; ако
  липсва потвърждение, остави Бранд празно (по-добре празно, отколкото грешна марка).
- Свързани: ЕДИНСТВЕНО чрез find_related по каталожния номер. НИКОГА не измисляй кодове
  или продукти. Ако find_related върне празно, остави Свързани празно.
- АТРИБУТИ — СХЕМАТА Е ЧЕКЛИСТ, мини по нея ГРУПА ПО ГРУПА (най-честият пропуск!). Продуктът
  трябва да е НАМИРАЕМ по всеки филтър на категорията си. За ВСЯКА група от 'ФИЛТРИ ЗА ТАЗИ
  КАТЕГОРИЯ' изпълни по ред и спри на първия успех:
    1) потърси стойността в ДОСТОВЕРНИТЕ ДАННИ и в името (размери, обем, волтаж, ват, фасонка,
       брой често са там дословно);
    2) ако групата е ВИЗУАЛНА (Цвят, Форма, Материал, Тип, Модел/шарка, Стил) и стъпка 1 не я
       даде — извикай analyze_image и я разчети от снимката;
    3) ако още липсва и е важна — провери страницата на доставчика (fetch_url);
    4) ЕДВА СЛЕД тези проверки я остави празна: само ако е НЕПРИЛОЖИМА за продукта (Волтаж за
       чиния) или наистина непотвърдима. Празна група БЕЗ да си минал стъпки 1-3 = недовършена
       работа; празна група СЛЕД тях = честен отговор.
  Ползвай стойностите от вокабуляра на групата, когато пасват. Пиши САМО потвърдени стойности —
  грешен филтър е по-лош от празен (вкарва продукта в грешен резултат). Формат:
  'Ключ: Стойност; Ключ: Стойност'. Същият принцип за ВСИЧКИ полета: празно поле е допустимо
  само след като си опитал да го попълниш от източник/снимка/интернет.
- МЕТА ПОЛЕТА (SEO дължини, за да не ги съкращава Google): Мета наименование ДО 60 знака
  (идеално 50-60); Мета описание ДО 160 знака (идеално 120-160). Пиши ги стегнато, с ключови
  думи в началото, и ЗАВЪРШЕНИ (не режи по средата на мисъл/дума).
- ОПИСАНИЕ = чист, ВАЛИДЕН HTML за клиента: <h2> заглавие, <p> абзаци, <ul><li> за характеристики.
  Пиши като ПРОДАВАЧ, не като проверител: НЕ описвай собствената си проверка ('от снимката се
  вижда', 'потвърдена серия', 'според сертификат'). Без каталожни кодове.
- СИНОНИМИ: 4-6 алтернативни търсещи думи, които клиент би написал (други имена, умалителни,
  разговорни; кош→кофа за боклук). САМО на кирилица — без транслитерация (не 'tigan', 'kupa').
- ТЕГЛО (кг): ако липсва в данните, дай разумна ОЦЕНКА по типа/размера/материала и отбележи в
  'промени', че е приблизителна.
- ЕДИНИЦИ/ЛОКАЛ: една мерна система на кирилица (см, мл, л, кг, г) навсякъде; българска десетична
  ЗАПЕТАЯ (0,5 л, не 0.5).
- ТОЧНОСТ СПРЯМО СНИМКАТА: описанието и атрибутите НЕ трябва да твърдят форма, материал,
  покритие или цвят, които противоречат на снимката. Провери с analyze_image при съмнение.
- Всяка стойност, която пишеш, трябва да е подкрепена от инструмент или дадените данни —
  никакви измислени факти, кодове или продукти.
- Ако откриеш техника, дала ОТЛИЧЕН резултат, запиши я с record_learning за другите агенти.

ФОРМАТ — на всяка стъпка върни ТОЧНО един ред:
  TOOL <име> <json-аргументи>        (за да ползваш инструмент)
или, когато си готов:
  FINAL <json с ключове: Наименование, Описание, Бранд, Категории, Атрибути, Мета наименование,
        Мета описание, Синоними, Свързани, Тегло (кг), както и "промени" (какво поправи) и
        "увереност" (висока/средна/ниска)>

Инструменти:
  fetch_url {"url":"..."}          извлича текста на уеб страница (напр. сайта на доставчика)
  analyze_image {"question":"..."} пита модел за зрение относно снимката на продукта
  lookup_brand {"name":"..."}      каноничен бранд от общия речник (или null)
  verify_brand {"name":"..."}      проверява/поправя правописа на марка и я добавя в речника
  find_related {"cat":"..."}       кодове на продукти с каталожен номер ±1
  web_search {"query":"..."}       търсене в интернет (ограничено)
  record_learning {"text":"..."}   записва добра техника в общия скил файл

УВЕРЕНОСТ — цели ВИСОКА, спечелена чрез проверка (не чрез налучкване):
- ВИСОКА = потвърдил си КЛЮЧОВИТЕ факти (тип, марка, материал, форма/цвят от снимката,
  съответствие с данните). Второстепенни оценки (тегло, нюанс) не свалят увереността.
- Непотвърдена марка (от ЛЮБ източник — снимка или само име) -> остави Бранд ПРАЗНО, по-добре
  празно, отколкото грешно. При спорен факт направи още една проверка (analyze_image/web_search).
- 'средна'/'ниска' САМО когато КЛЮЧОВ факт остава реално неясен след проучване.
- Първо виж натрупания опит по-долу и речника (lookup_brand) — не повтаряй работа.
Работи стъпка по стъпка. Не измисляй резултати от инструменти — изчакай ги."""


def _owner_rules():
    """Style rules the OWNER accepted from the edit-lessons page — highest-priority
    instructions, since they encode the human's actual editing behaviour."""
    try:
        t = (HERE / "owner_style_rules.md").read_text(encoding="utf-8").strip()
        header = "\n\nПРАВИЛА ОТ СОБСТВЕНИКА (задължителни, изведени от негови редакции):\n"
        return (header + t) if t else ""
    except Exception:
        return ""


def _load_learnings_tail(path, tail_bytes=8192):
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - tail_bytes))
            return f.read().decode("utf-8", "replace")
    except OSError:
        return ""


def _load_learnings():
    """The shared, growing skill: techniques earlier agents recorded as working well."""
    try:
        txt = _load_learnings_tail(LEARNINGS).strip()   # tail-read: the file grows ~1MB+
        if txt:
            return ("\n\nНАТРУПАН ОПИТ (техники от други агенти, дали отличен резултат — "
                    "ползвай ги):\n" + txt[-1200:])
    except Exception:
        pass
    return ""


def _compact(messages, keep_recent=3, cap=300):
    """Trim the conversation SENT to the model without losing the loop's own record.
    ~96% of a product's tokens are prompt: the ReAct loop replays its whole growing
    history (esp. big fetch_url dumps) on every one of ~12 steps. We keep the system
    prompt, the task, and the last `keep_recent` turns FULL, and shorten only OLDER
    tool-result dumps (already used by the time they scroll off). Big prompt-token cut,
    minimal context loss. The full `log` is kept separately for the forced-final summary."""
    if len(messages) <= keep_recent + 2:
        return messages
    out = list(messages[:2])                           # system + task (always full)
    for m in messages[2:-keep_recent]:
        c = m.get("content")
        if isinstance(c, str) and c.startswith("Резултат от") and len(c) > cap:
            out.append({**m, "content": c[:cap] + " …[съкратено]"})
        else:
            out.append(m)
    out.extend(messages[-keep_recent:])                # recent turns full
    return out


def enrich(code, verbose=False):
    global _CHAIN_OVERRIDE
    task, _ = run_one.next_task(code)
    if not task:
        return {"error": f"no task for {code}"}
    # Difficulty routing: hard products lead with a capable model; easy ones stay
    # fast-first. Conservative until telemetry data can tune the policy.
    try:
        import difficulty as _diff
        _CHAIN_OVERRIDE = _diff.chain_for(task, run_one.WORKER_CHAIN)
    except Exception:
        _CHAIN_OVERRIDE = None
    prod = task.get("product", {})
    gt = {k: v for k, v in (task.get("ground_truth") or {}).items() if v is not None}
    # Weak supplier match (matched only by name/model similarity) — warn the agent so it
    # treats the scraped data as a HYPOTHESIS to verify, not ground truth.
    _mk = str(gt.get("Match kind") or "").lower()
    weak_warn = ""
    if _mk.startswith(("name", "model")):
        weak_warn = ("\n\n⚠️ ВНИМАНИЕ: съвпадението с данните на доставчика е СЛАБО (по име/модел, "
                     "не по код). Скрейпнатите данни може да са за ДРУГ продукт — проверявай всяко "
                     "твърдение срещу снимката и складовото име, и не пренасяй нищо непотвърдено.")
    image_url = (prod.get("Снимки") or "").split(";")[0].strip()
    ctx = {"code": code, "image_url": image_url, "name": prod.get("Наименование") or "",
           "cat": prod.get("Каталожен номер")}
    editable = {k: prod.get(k) for k in run_one.EDITABLE}
    import filter_schema_store as _fss
    _cat = str(prod.get("Категории") or "").strip()
    fs = _fss.get_filters(_cat) or task.get("filter_schema") or []
    fs_txt = ("\n\nФИЛТРИ ЗА ТАЗИ КАТЕГОРИЯ (попълни Атрибути така, че продуктът да е НАМИРАЕМ по "
              "ВСЕКИ приложим филтър тук; използвай точните имена на групите и стойности от списъка "
              "със стойности, където е приложимо):\n"
              + json.dumps(fs, ensure_ascii=False, indent=1)) if fs else ""
    user = (f"ПРОДУКТ (код {code}). Текущи редактируеми полета:\n"
            f"{json.dumps(editable, ensure_ascii=False, indent=1)}\n\n"
            f"Каталожен номер: {prod.get('Каталожен номер')}\nСнимка: {image_url or 'няма'}\n\n"
            f"ДОСТОВЕРНИ ДАННИ (Microinvest + скрейп доставчик):\n"
            f"{json.dumps(gt, ensure_ascii=False, indent=1)}"
            f"{fs_txt}\n\n"
            f"{weak_warn}\n\nРазследвай и подобри този продукт. Започни.")
    messages = [{"role": "system", "content": SYSTEM + _load_learnings() + _owner_rules()},
                {"role": "user", "content": user}]
    log = []

    def parse_final(text):
        raw = text[text.upper().index("FINAL") + 5:].strip() if "FINAL" in text.upper() else text
        try:
            m = re.search(r"\{.*\}", raw, re.DOTALL)
            if m:
                return json.loads(m.group(0))
        except Exception:
            pass
        return run_one.extract_json(raw)  # robust: ```json blocks + balanced braces

    for step in range(MAX_STEPS):
        if step == MAX_STEPS - 2:  # near the limit — wrap up, don't start new checks
            messages.append({"role": "user", "content":
                             "Остават малко стъпки. Приключи: на следващата стъпка върни FINAL "
                             "с наличното, без да започваш нови проверки."})
        out = chat(_compact(messages)).strip()
        messages.append({"role": "assistant", "content": out})
        line = out.splitlines()[0].strip() if out else ""
        if verbose:
            print(f"\n[stap {step+1}] {out[:400]}")
        if "FINAL" in line.upper():
            final = parse_final(out)
            if final:
                return {"code": code, "fields": final, "steps": step + 1, "log": log}
            messages.append({"role": "user", "content":
                             "FINAL JSON-ът беше невалиден. Върни отново: FINAL <валиден json>."})
            continue
        m = re.match(r'TOOL\s+(\w+)\s*(\{.*\})?', line, re.IGNORECASE)
        if m:
            tname = m.group(1)
            try:
                targs = json.loads(m.group(2)) if m.group(2) else {}
            except Exception:
                targs = {}
            result = run_tool(tname, targs, ctx)
            log.append({"tool": tname, "args": targs, "result": str(result)[:200]})
            if verbose:
                print(f"   -> {tname}({targs}) = {str(result)[:160]}")
            messages.append({"role": "user", "content": f"Резултат от {tname}:\n{result}\n\nПродължи."})
        else:
            messages.append({"role": "user", "content":
                             "Върни ТОЧНО един ред: 'TOOL <име> <json>' или 'FINAL <json>'."})
    # Forced final — FRESH focused prompt (not the bloated 14-round convo, which degrades
    # the JSON), seeded with what the investigation found. Reliably parseable.
    summary = "; ".join(f"{l['tool']}={str(l['result'])[:90]}" for l in log[-7:])
    fp = [{"role": "system", "content": "Ти си прецизен редактор на продукти за български "
           "магазин. Пишеш чист български без руски думи. Върни САМО валиден JSON."},
          {"role": "user", "content": user + f"\n\nОткрито при проверката: {summary}\n\n"
           "Върни САМО JSON с ключове: Наименование, Описание, Бранд, Категории, Атрибути, "
           "Мета наименование, Мета описание, Синоними, Тегло (кг), промени, увереност."}]
    try:
        final = parse_final(chat(fp, max_tokens=1500).strip())
    except Exception:
        final = None
    if final:
        return {"code": code, "fields": final, "steps": MAX_STEPS + 1, "log": log, "forced": True}
    return {"code": code, "error": "max steps reached", "log": log}


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verbose = "--verbose" in sys.argv
    res = enrich(args[0], verbose=verbose)
    print("\n=== RESULT ===\n" + json.dumps(res, ensure_ascii=False, indent=1))
