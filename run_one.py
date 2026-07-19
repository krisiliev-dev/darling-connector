# -*- coding: utf-8 -*-
"""Process the next pending product through ONE dedicated Hermes agent run.

All file I/O and bookkeeping happen here in plain Python (stdlib only).
The agent gets exactly one product, its ground truth, the shared guide, and
the web/vision toolsets — nothing else. Its final message must be one JSON
object, which this driver validates and records.

State model (append-only, resumable):
  tasks.jsonl    input queue (from prepare_tasks.py)
  results.jsonl  one line per successfully verified product
  failures.jsonl one line per failed attempt; codes with >= MAX_ATTEMPTS are skipped
  guide.md       shared reviewer guide; agent lessons are appended here

Exit codes: 0 = processed one product, 2 = queue empty, 1 = attempt failed.
"""
import base64
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import urllib.parse
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).parent
TASKS_PATH = HERE / "tasks.jsonl"
CATEGORIES_PATH = HERE / "categories.json"
# Env overrides let bake-off/test runs use a different model and results file
# without touching the production configuration.
RESULTS_PATH = Path(os.environ.get("PIPELINE_RESULTS_PATH") or (HERE / "results.jsonl"))
NO_LESSONS = os.environ.get("PIPELINE_NO_LESSONS") == "1"
# Parallel lanes: PIPELINE_SHARD="0/2" makes this process claim only codes with
# md5(code) % 2 == 0. Each lane appends to its own results file; the done-set
# always reads ALL results*.jsonl so lanes never duplicate work.
SHARD = os.environ.get("PIPELINE_SHARD", "")
FAILURES_PATH = HERE / "failures.jsonl"
GUIDE_PATH = HERE / "guide.md"
LOG_PATH = HERE / "runner.log"
DESC_HASHES_PATH = HERE / "desc_hashes.txt"

# The uv-tools install owns the ~/.hermes profile (free-first model chain,
# tavily web search, gemini vision, running gateway). The venv hermes.exe uses
# a different home (AppData\Local\hermes, zai-only) — do NOT use it here.
HERMES_EXE = r"C:\Users\lora_\AppData\Roaming\uv\tools\hermes-agent\Scripts\hermes.exe"
HERMES_HOME = r"C:\Users\lora_\.hermes"
TOOLSETS = "web,vision"
# Model chain (2026-07-13 rebuild). A 16-model Bulgarian benchmark (5 tasks incl.
# Russian-seeded, scored on RU-letter/garble/CJK/EN contamination) ranked Qwen
# far above the old Mistral worker, which leaked Russian in ~50% of production
# output (the root cause of the high review rate). Results (lower=better):
#   qwen-flash 1.8 (fast 2.5s), qwen3.5-397b 2.4, qwen3-max 2.4, qwen-plus 3.4,
#   Mistral-Large-3 ~unmeasurable/high (prod-evidenced). gpt-oss truncates; small
#   Qwen3 dumps <think>; Aya/Command leaked. See memory bg-model-benchmark.
# WORKER = qwen-flash on Alibaba's free Singapore quota (dashscope-intl); this
# also offloads NVIDIA, relieving the rate-limiting that starved the vision pass.
# Worker failover chain (2026-07-13, free-tier strategy). Alibaba grants each model
# its OWN ~1M free-token quota, so we chain across ALL the clean Qwen chat models —
# ~7 fresh ones × 1M ≈ millions of free tokens — before spilling to other providers.
# As each model's quota exhausts (403 AllocationQuota.FreeTierOnly), it is written to
# EXHAUSTED_PATH and skipped for all future products (no wasted 403 round-trip). All
# probed clean on Bulgarian (ru=0); ordered fastest-first for throughput.
# The WORKER runs via direct OpenAI-compatible API (run_worker_direct) — pure text
# generation, sidesteps the Hermes CLI's context-compression bug on our ~20k prompts.
# CRITICAL free-tier insight (verified 2026-07-13): on Alibaba, each model — INCLUDING
# every DATED snapshot of qwen-plus — carries its OWN ~1M free-token grant. So dated
# snapshots multiply capacity (qwen-plus is exhausted, but qwen-plus-2025-07-14 etc. are
# fresh). All entries below were probed OK + clean (ru=0), fastest-first. Add more dated
# snapshots here as quotas drain — the exhausted-cache skips drained ones automatically.
WORKER_CHAIN = [
    # OWNER POLICY (2026-07-17): DashScope first — fresh free grants (700k-capped each),
    # then the BILLED workhorses (under the DASHSCOPE_BILLED_OK spend cap). Only when
    # DashScope is done/capped does traffic flow to the other free tiers, ordered by
    # quality: Mistral (frontier, ~1B tok/mo) -> Cerebras -> Groq -> NVIDIA -> tail.
    # --- DashScope: drained-grant models (skipped while exhausted) ---
    ["-m", "qwen3.6-flash-2026-04-16", "--provider", "dashscope-intl"],
    ["-m", "qwen3.6-flash", "--provider", "dashscope-intl"],
    ["-m", "qwen3.5-flash-2026-02-23", "--provider", "dashscope-intl"],
    ["-m", "qwen3.5-flash", "--provider", "dashscope-intl"],
    ["-m", "qwen3.6-27b", "--provider", "dashscope-intl"],
    ["-m", "qwen3.5-122b-a10b", "--provider", "dashscope-intl"],
    ["-m", "qwen3.6-35b-a3b", "--provider", "dashscope-intl"],
    ["-m", "qwen3.5-35b-a3b", "--provider", "dashscope-intl"],
    ["-m", "qwen3.5-27b", "--provider", "dashscope-intl"],
    ["-m", "qwen-plus-2025-09-11", "--provider", "dashscope-intl"],
    # --- DashScope: fresh free grants (700k hard cap each) ---
    ["-m", "qwen-plus-character", "--provider", "dashscope-intl"],
    ["-m", "qwen-plus-latest", "--provider", "dashscope-intl"],
    ["-m", "qwen-plus-2025-01-25", "--provider", "dashscope-intl"],
    ["-m", "qwen3.6-plus-2026-04-02", "--provider", "dashscope-intl"],
    ["-m", "qwen3.6-plus", "--provider", "dashscope-intl"],
    ["-m", "qwen3.5-plus-2026-04-20", "--provider", "dashscope-intl"],
    ["-m", "qwen3.7-plus", "--provider", "dashscope-intl"],
    ["-m", "qwen3.5-plus-2026-02-15", "--provider", "dashscope-intl"],
    ["-m", "qwen3.5-plus", "--provider", "dashscope-intl"],
    ["-m", "qwen3-max-2026-01-23", "--provider", "dashscope-intl"],
    ["-m", "qwen3-max", "--provider", "dashscope-intl"],
    ["-m", "qwen3-max-2025-09-23", "--provider", "dashscope-intl"],
    ["-m", "qwen3-max-preview", "--provider", "dashscope-intl"],
    ["-m", "qwen3.7-max-preview", "--provider", "dashscope-intl"],
    ["-m", "qwen3.7-max-2026-05-17", "--provider", "dashscope-intl"],
    ["-m", "qwen3.6-max-preview", "--provider", "dashscope-intl"],
    ["-m", "qwen3.7-max", "--provider", "dashscope-intl"],
    ["-m", "qwen3.7-max-2026-06-08", "--provider", "dashscope-intl"],
    ["-m", "qwen3.7-max-2026-05-20", "--provider", "dashscope-intl"],
    # --- DashScope: BILLED workhorses (spend-capped; newest first) ---
    ["-m", "qwen3.7-plus-2026-05-26", "--provider", "dashscope-intl"],
    ["-m", "qwen-plus-2025-12-01", "--provider", "dashscope-intl"],
    # --- free tiers: BEST model per provider FIRST, then that provider's weaker models on
    # exhaustion, before moving to the next provider (owner 2026-07-18). DashScope OFF
    # (arrearage). Cross-provider order by quality+reliability: Mistral (frontier) → Groq
    # (fast, large) → zai → Cerebras → NVIDIA → Cohere. All model names probed live. ---
    ["-m", "mistral-medium-2508", "--provider", "mistral"],   # Medium-3: newer/faster, frontier-class
    ["-m", "mistral-large-latest", "--provider", "mistral"],  # bigger fallback if medium throttles
    ["-m", "mistral-small-latest", "--provider", "mistral"],
    ["-m", "openai/gpt-oss-120b", "--provider", "groq"],      # 120B best on Groq
    ["-m", "llama-3.3-70b-versatile", "--provider", "groq"],
    ["-m", "qwen/qwen3.6-27b", "--provider", "groq"],
    ["-m", "llama-3.1-8b-instant", "--provider", "groq"],     # 8B: highest free rpd, last resort
    ["-m", "glm-4.7", "--provider", "zai"],                   # full GLM before flash
    ["-m", "glm-4.7-flash", "--provider", "zai"],
    ["-m", "gpt-oss-120b", "--provider", "cerebras"],         # (paid-gated until billing active)
    ["-m", "gemma-4-31b", "--provider", "cerebras"],
    ["-m", "nvidia/llama-3.3-nemotron-super-49b-v1", "--provider", "nvidia"],  # strong+fast
    ["-m", "meta/llama-3.3-70b-instruct", "--provider", "nvidia"],
    ["-m", "qwen/qwen3.5-397b-a17b", "--provider", "nvidia"],  # 397B best-quality but ~2min: last
    ["-m", "command-a-03-2025", "--provider", "cohere"],
]
# Back-compat default (a few call sites reference MODEL_ARGS); polish uses a fresh model.
MODEL_ARGS = list(WORKER_CHAIN[0])
POLISH_MODEL_ARGS = ["-m", "qwen-turbo", "--provider", "dashscope-intl"]
EXHAUSTED_PATH = HERE / "exhausted_models.txt"

REVIEW_ENABLED = os.environ.get("PIPELINE_REVIEW", "1") == "1"
REVIEW_MODEL_ARGS = ["-m", "glm-4.7-flash", "--provider", "zai"]  # vestigial; reviewer uses REVIEW_CHAIN
REVIEW_TOOLSETS = "search"


# HARD BUDGET GUARD (2026-07-16 billing incident): DashScope free grants are 1M tokens
# per model, ONE-TIME. On a billable account, exceeding the grant does NOT 403 — it
# silently rolls to pay-as-you-go (this is how qwen-plus-2025-12-01 billed 188M+ tokens).
# So we enforce the grant OURSELVES: any dashscope model whose measured cumulative usage
# exceeds DASHSCOPE_BUDGET is treated as exhausted, permanently. Additionally, dashscope
# is DISABLED entirely unless env DASHSCOPE_OK=1 (owner must explicitly re-enable after
# settling the balance and accepting the per-model budget policy).
BILLED_WORKHORSES = {"qwen3.7-plus-2026-05-26", "qwen-plus-2025-12-01"}
DASHSCOPE_BUDGET = 700_000                      # 300k margin: 12 lanes have ~1 product in flight each before telemetry lands, so the cap must absorb concurrent drift
_BUDGET_SPENT = None


def _dashscope_allowed():
    # env var OR flag file (cron lanes don't inherit the shell env, so the file is the
    # reliable cross-process switch — delete DASHSCOPE_OK file to cut Alibaba off again).
    # DASHSCOPE_OFF=1 per-process override: the reviewer fleet runs with it so reviews go
    # to Mistral/Cerebras/Groq and the DashScope grants stay reserved for ENRICHMENT.
    if os.environ.get("DASHSCOPE_OFF") == "1":
        return False
    return os.environ.get("DASHSCOPE_OK") == "1" or (HERE / "DASHSCOPE_OK").exists()


def _dashscope_spend():
    """{model: measured dashscope tokens} — lean indexed read from model_spend (kept
    incrementally by db.record_version). The old full record_json re-parse per check was
    a measurable lane-throughput drag."""
    spent = {}
    try:
        import db as _db
        con = _db.connect()
        try:
            for m, t in con.execute("SELECT model, tokens FROM model_spend "
                                    "WHERE provider='dashscope-intl'").fetchall():
                spent[str(m)] = int(t or 0)
        finally:
            con.close()
    except Exception:
        pass
    return spent


def _billed_cap_millions():
    """Owner-controlled BILLED-overflow ceiling: the DASHSCOPE_BILLED_OK file contains a
    number = max NEW billed tokens in MILLIONS beyond the free grants (edit to raise;
    delete the file for free-grants-only). Missing/invalid file = 0 (no billed usage)."""
    try:
        return float((HERE / "DASHSCOPE_BILLED_OK").read_text(encoding="utf-8").strip().split()[0])
    except Exception:
        return 0.0


def billed_overflow_tokens(spent=None):
    """Measured tokens beyond each model's 1M free grant — the part that BILLS."""
    spent = spent if spent is not None else _dashscope_spend()
    return sum(max(0, t - 1_000_000) for t in spent.values())


def _budget_exhausted():
    """dashscope models to block, per the owner's spend policy:
      * free-grants-only (no billed cap): block any model beyond DASHSCOPE_BUDGET (700k).
      * billed allowed (cap set): allow overflow while cumulative billed tokens stay
        under the cap; when the cap is reached, fall back to free-grant policy."""
    global _BUDGET_SPENT
    if _BUDGET_SPENT is None:
        spent = _dashscope_spend()
        cap_m = _billed_cap_millions()
        over = {m for m, t in spent.items() if t > DASHSCOPE_BUDGET}
        if cap_m > 0 and billed_overflow_tokens(spent) < cap_m * 1_000_000:
            # billing authorized: fresh grants STAY protected at 700k (they must drain
            # for free, one by one); only the designated workhorses may bill.
            _BUDGET_SPENT = over - BILLED_WORKHORSES
        else:
            _BUDGET_SPENT = over
    return _BUDGET_SPENT


def _load_exhausted():
    try:
        ex = set(l.strip() for l in EXHAUSTED_PATH.read_text(encoding="utf-8").splitlines() if l.strip())
    except FileNotFoundError:
        ex = set()
    ex |= _budget_exhausted()
    return ex


def _mark_exhausted(model):
    with open(EXHAUSTED_PATH, "a", encoding="utf-8") as f:
        f.write(model + "\n")


def _is_quota_error(msg):
    m = str(msg).lower()
    return "freetieronly" in m or "free quota has been exhausted" in m or "allocationquota" in m


def _is_arrearage(msg):
    m = str(msg).lower()
    return "arrearage" in m or "overdue" in m or "account is in good standing" in m


def maybe_pause_on_arrearage(exc):
    """CIRCUIT BREAKER (owner's request): the instant a provider reports arrearage —
    i.e. ANY charge accrued on an account with no payment method — write the PAUSE
    sentinel so EVERY lane stops immediately. Returns True if it paused."""
    if _is_arrearage(exc):
        try:
            (HERE / "PAUSE").write_text(
                "AUTO-PAUSED (arrearage/charge detected) " +
                datetime.now().isoformat(timespec="seconds") +
                " — a charge accrued on the model provider. All lanes stopped; resolve billing to resume.",
                encoding="utf-8")
        except Exception:
            pass
        try:
            log("!!! ARREARAGE/charge detected -> AUTO-PAUSED (PAUSE sentinel written). !!!")
        except Exception:
            pass
        return True
    return False
# 7 min: GLM p95 is ~150s; anything past this is a provider hang, and two of
# these (worker + reviewer) must fit inside the cron shim's kill window.
AGENT_TIMEOUT_S = 420
MAX_ATTEMPTS = 3
MAX_PROMPT_CHARS = 24000

ENRICHED_COLS = [
    "Код", "Каталожен номер", "Наименование", "Синоними", "Описание",
    "Мета наименование", "Мета описание", "Бранд", "Доставчик", "Категории",
    "Мярка", "Цена", "Количество", "Снимки", "Тегло (кг)", "Активен",
    "Предварителна поръчка", "Атрибути", "Варианти", "Серия", "Свързани",
]
# Fields the agent is allowed to change. Everything else is copied from the original.
EDITABLE = [
    "Наименование", "Описание", "Мета наименование", "Мета описание", "Бранд",
    "Категории", "Тегло (кг)", "Атрибути", "Варианти", "Свързани", "Синоними",
]
# Empiric/operational columns are DRIVER-OWNED: taken verbatim from the source
# and Microinvest, never generated or even shown to the agent (owner directive
# 2026-07-11 — so the AI cannot leak a price/quantity/code into any text field).
OPERATIONAL_COLS = [
    "Код", "Каталожен номер", "Цена", "Количество", "Мярка", "Доставчик",
    "Активен", "Предварителна поръчка",
]

# Dedicated vision-verification pass (3rd agent, 2026-07-11): checks the FINAL
# product against its photo for shape/type/material/colour/count. Catches errors
# the text reviewer (no image) and the worker (may trust a misleading name like
# "Ø20 cm" on a rectangular pan) both miss. Direct NVIDIA call, not through
# hermes, so we control the model and payload size.
VISION_VERIFY_ENABLED = os.environ.get("PIPELINE_VISION_VERIFY", "1") == "1"
VISION_VERIFY_MODEL = os.environ.get("PIPELINE_VISION_MODEL",
                                     "meta/llama-3.2-90b-vision-instruct")
# Vision failover chain (2026-07-18): NVIDIA's vision endpoint was 504-ing, which silently
# killed the photo QC. mistral-medium is VL-capable and independent, so vision survives one
# provider outage. Each entry: (provider-key-in-DIRECT_PROVIDERS or "nvidia", model).
VL_CHAIN = [("nvidia", VISION_VERIFY_MODEL), ("mistral", "mistral-medium-2508")]

# Language-polish pass: rewrites wording (facts frozen) when garbled/foreign
# words survive review, so language issues become clean output not human work.
POLISH_ENABLED = os.environ.get("PIPELINE_POLISH", "0") == "1"

# Common Russian-isms models leak into Bulgarian text. Deterministic fix runs
# before spellcheck so these become clean instead of escalating to a human.
RU_FIX = {
    "подходит": "подходящ", "покрытие": "покритие", "покрытия": "покрития",
    "покрытието": "покритието", "обеспечава": "осигурява",
    "обеспечи": "осигури", "обеспечиващ": "осигуряващ", "современен": "съвременен",
    "современа": "съвременна", "можно": "може", "применение": "приложение",
    "цвет": "цвят", "изготовлен": "изработен", "изготовена": "изработена",
    "прочный": "здрав", "ёмкость": "вместимост", "неза": "не", "достаточно": "достатъчно",
    "остатки": "остатъци", "также": "също", "длина": "дължина", "объем": "обем",
    "нержавеема": "неръждаема", "нержавеюща": "неръждаема", "металлен": "метален",
    "стойкост": "устойчивост", "готовене": "готвене", "губка": "гъба",
    "чистящо": "почистващо", "чистящи": "почистващи", "детергент": "препарат",
    # Recurring leaks observed in live output (2026-07 audit). Only unambiguous
    # orthographic cognates — identical meaning, Russian spelling — are listed;
    # semantic substitutions are deliberately excluded to protect accuracy.
    "другие": "други", "результат": "резултат", "результати": "резултати",
    "результата": "резултата", "результате": "резултат", "результаты": "резултати",
    "интерьер": "интериор", "интерьера": "интериора", "интерьере": "интериора",
    "интерьеры": "интериори", "интерьери": "интериори", "интерьор": "интериор",
    "интерьора": "интериора", "интерьоре": "интериора",
    "обеспечива": "осигурява", "обеспечивает": "осигурява",
    "пятна": "петна", "пятно": "петно", "пятен": "петна",
    "напиток": "напитка", "напитки": "напитки",
    "создадете": "създадете", "создайте": "създайте", "создава": "създава",
    "создаде": "създаде", "создаване": "създаване",
    "избегавайте": "избягвайте", "избегайте": "избягвайте", "избегава": "избягва",
    "изпечване": "изпичане",
    "профессионал": "професионал", "профессионална": "професионална",
    "профессионален": "професионален", "профессионално": "професионално",
    "профессионални": "професионални", "профессионализъм": "професионализъм",
    # Russian-only words (no Bulgarian meaning) that leaked into live output —
    # direct 1:1 translations, not risky semantic guesses (2026-07-14 audit).
    "бренд": "бранд", "бренда": "бранда", "брендове": "брандове",
    # NOTE (owner 2026-07-19): «посуда» is acceptable Bulgarian usage — do NOT flag or
    # auto-replace it. Only genuinely-Russian forms below.
    "нержавеща": "неръждаема", "нержавещата": "неръждаемата",
    "нержавейка": "неръждаема стомана", "нержавей": "неръждаема",
    "герметичен": "херметичен", "герметичният": "херметичният",
    "герметична": "херметична", "герметично": "херметично",
    "загрязнение": "замърсяване", "загрязнения": "замърсявания",
    "загрязнений": "замърсявания", "загрязнявания": "замърсявания",
    "герметичен": "херметичен", "герметична": "херметична",
    "герметично": "херметично", "герметични": "херметични",
    "герметичност": "херметичност", "герметичността": "херметичността",
    "аутентичен": "автентичен", "аутентична": "автентична",
    "аутентично": "автентично", "аутентични": "автентични",
    "аутентичния": "автентичния", "аутентичният": "автентичният",
    "аутентичность": "автентичност",
    "латун": "месинг", "латунен": "месингов", "латунна": "месингова",
    "оцинкован": "поцинкован", "оцинкована": "поцинкована",
    "оцинковано": "поцинковано", "оцинковани": "поцинковани",
    # Inflections the exact-match map missed but the marker net caught (2026-07-14).
    "нержавееща": "неръждаема", "нержавеещи": "неръждаеми",
    "нержавеещ": "неръждаем", "нержавеещо": "неръждаемо",
    "нержавейка": "неръждаема стомана", "нержавейки": "неръждаема стомана",
    "профессионалната": "професионалната", "профессионалния": "професионалния",
    "профессионалният": "професионалният", "профессионалните": "професионалните",
    "профессионалната": "професионалната",
    "современно": "съвременно", "современни": "съвременни", "современ": "съвременен",
    "современые": "съвременни", "современых": "съвременни",
    "посудомийка": "съдомиялна", "посудомийна": "съдомиялна",
    "посудомия": "съдомиялна", "посудомоечная": "съдомиялна",
    "посудомийки": "съдомиялни", "посудомийните": "съдомиялните",
    "современа": "съвременна", "современите": "съвременните",
}

# Curated Russian-word markers — stems that are UNAMBIGUOUSLY Russian and have no
# valid Bulgarian word sharing them. Used as the genuine text-contamination signal
# in the agentic path (replacing a crude spellcheck word-count that false-positived
# on valid commerce vocabulary). RU_FIX already auto-corrects the known forms above;
# this net catches inflections/variants that slip past the exact-match map. Keep it
# HIGH-precision — only add a stem when no Bulgarian word legitimately contains it.
RU_MARKERS = re.compile(
    r"(?:загрязн|герметич|аутентич|профессио|нержаве|"
    r"обеспечи|обеспеча|покрыти|результат|интерьер|создад|создай|"
    r"избега|современ)",
    re.IGNORECASE,
)


def russian_survivors(text):
    """Words in `text` that match a curated Russian-only marker (post RU_FIX).
    These are genuine Cyrillic contamination — NOT phunspell dictionary misses."""
    if not text:
        return []
    return [w for w in re.findall(r"[а-яА-ЯёэыЁЭЫ]+", str(text))
            if RU_MARKERS.search(w)]

# Supplier / operator names are NOT product brands (an agent once branded a
# product "LEVENA" because the supplier company checked out on the web).
SUPPLIER_NAMES = [
    "levena", "левена", "mira-n", "mira n", "мира-н", "мира н", "egera", "егера",
    "inhouse", "in house", "ин хаус", "city lights", "city-lights", "сити лайтс",
    "vertex", "вертекс", "kalian", "калиан", "plamplast", "плампласт",
    "elbulgaria", "ел българия", "microinvest", "микроинвест",
]


def log(msg):
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    try:
        print(line)
    except UnicodeEncodeError:
        # cp1252 stdout under some launchers: Cyrillic log lines must never turn a
        # successfully written record into a spurious "failed"
        print(line.encode("ascii", "replace").decode())
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_jsonl_codes(path, key="code"):
    codes = []
    if path.exists():
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        codes.append(json.loads(line)[key])
                    except Exception:
                        pass
    return codes


def _in_shard(code):
    if not SHARD:
        return True
    try:
        idx, total = (int(x) for x in SHARD.split("/"))
    except ValueError:
        # A typo'd PIPELINE_SHARD used to silently claim EVERY code — 12 lanes then
        # duplicate each other's work. Fail loudly instead.
        raise ValueError(f"malformed PIPELINE_SHARD={SHARD!r} (expected 'i/N')")
    import hashlib
    return int(hashlib.md5(code.encode()).hexdigest(), 16) % total == idx


_DONE_CACHE = None
_TASKCODES_CACHE = None
_PRIORITY_CACHE = {"v": None, "loaded": False}


def _priority_set():
    """Optional processing allow-list. When V2_PRIORITY.txt exists, lanes serve ONLY the
    codes listed there (one per line) — used to process a high-confidence batch first
    (e.g. products whose brand is GS1-confirmed) and then idle until the file is extended.
    Returns a set, or None when the file is absent (serve everything). Re-read when the
    file's mtime changes so appending a new batch resumes the fleet without a restart."""
    p = HERE / "V2_PRIORITY.txt"
    try:
        mtime = p.stat().st_mtime
    except OSError:
        _PRIORITY_CACHE.update(v=None, loaded=True, mtime=None)
        return None
    if _PRIORITY_CACHE.get("mtime") != mtime:
        codes = {ln.strip() for ln in p.read_text(encoding="utf-8").splitlines()
                 if ln.strip()}
        _PRIORITY_CACHE.update(v=codes, loaded=True, mtime=mtime)
    return _PRIORITY_CACHE["v"]


def _done_set():
    """Codes already processed. DB-first (indexed, no ~26MB parse per lane process; the
    DB is authoritative and written first) UNION the small legacy results.jsonl (predates
    lane files); full JSONL scan only as fallback. Cached per-process + grown via
    mark_done()."""
    global _DONE_CACHE
    if _DONE_CACHE is None:
        s = None
        try:
            import db as _db
            if (HERE / "V2_MODE").exists():
                # v2 reprocessing: EVERYTHING is todo until it has a v2 version;
                # union the sidecar of records whose DB write failed (JSONL-only)
                s = _db.done_codes_v2()
                s.update(load_jsonl_codes(HERE / "v2_done_pending.jsonl"))
            elif _db.is_ready():
                s = _db.done_codes()
                s.update(load_jsonl_codes(HERE / "results.jsonl"))   # tiny legacy file
        except Exception:
            s = None
        if s is None:
            s = set()
            if (HERE / "V2_MODE").exists():
                # v2 fallback: only records carrying the v2 marker count as done
                for rp in HERE.glob("results.lane*.jsonl"):
                    try:
                        with open(rp, encoding="utf-8", errors="replace") as f:
                            for line in f:
                                if '"v2"' in line:
                                    try:
                                        s.add(str(json.loads(line).get("code") or ""))
                                    except Exception:
                                        pass
                    except OSError:
                        pass
                s.update(load_jsonl_codes(HERE / "v2_done_pending.jsonl"))
            else:
                for rp in [HERE / "results.jsonl", *HERE.glob("results.lane*.jsonl")]:
                    s.update(load_jsonl_codes(rp))
        _DONE_CACHE = s
    return _DONE_CACHE


def mark_done(code):
    if _DONE_CACHE is not None:
        _DONE_CACHE.add(str(code))


def _fail_counts():
    fc = {}
    v2 = (HERE / "V2_MODE").exists()
    try:
        with open(FAILURES_PATH, encoding="utf-8", errors="replace") as f:
            for line in f:
                if v2 and '"pipeline": "v2"' not in line:
                    continue            # v1-era failures must not starve the v2 queue
                try:
                    c = str(json.loads(line).get("code") or "")
                except Exception:
                    continue
                if c:
                    fc[c] = fc.get(c, 0) + 1
    except FileNotFoundError:
        pass
    return fc


def _next_task_scan(target_code, fail_counts):
    """Original fallback: stream tasks.jsonl. Used when the DB tasks table isn't ready."""
    done = _done_set()
    prio = _priority_set()
    with open(TASKS_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            task = json.loads(line)
            code = str(task["code"])
            if target_code is not None:
                if code == str(target_code):
                    return task, fail_counts.get(code, 0)
                continue
            if code in done or fail_counts.get(code, 0) >= MAX_ATTEMPTS \
                    or not _in_shard(code) \
                    or (prio is not None and code not in prio):
                continue
            return task, fail_counts.get(code, 0)
    return None, 0


def next_task(target_code=None):
    """Return (task, fail_count) for the next undone in-shard product, or (None, 0).
    Fast path: `done` cached from the authoritative JSONL + candidate codes/task fetched
    from the indexed DB (no 167MB scan). Falls back to the streaming scan if the DB tasks
    table isn't ready — identical semantics either way."""
    fail_counts = _fail_counts()
    try:
        import db
        if db.tasks_ready():
            if target_code is not None:
                t = db.get_tasks([target_code]).get(str(target_code))
                return (t, fail_counts.get(target_code, 0)) if t else (None, 0)
            global _TASKCODES_CACHE
            if _TASKCODES_CACHE is None:
                _TASKCODES_CACHE = db.all_task_codes()
            done = _done_set()
            prio = _priority_set()
            for code in _TASKCODES_CACHE:
                if code in done or fail_counts.get(code, 0) >= MAX_ATTEMPTS \
                        or not _in_shard(code) \
                        or (prio is not None and str(code) not in prio):
                    continue
                t = db.get_tasks([code]).get(code)
                if t:
                    return t, fail_counts.get(code, 0)
            return None, 0
    except Exception:
        pass
    return _next_task_scan(target_code, fail_counts)


def known_categories():
    if CATEGORIES_PATH.exists():
        return json.loads(CATEGORIES_PATH.read_text(encoding="utf-8"))
    return []


def guide_text():
    text = GUIDE_PATH.read_text(encoding="utf-8") if GUIDE_PATH.exists() else ""
    if len(text) > 9000:
        text = text[:6000] + "\n…[съкратено]…\n" + text[-2500:]
    return text


def build_prompt(task):
    # Hide empiric/operational fields from the agent entirely (owner directive):
    # code, price, quantity, unit, supplier — the AI never sees them, so it
    # cannot echo them into a name or description.
    product = {k: v for k, v in task["product"].items()
               if v is not None and k not in OPERATIONAL_COLS}
    gt = {k: v for k, v in task["ground_truth"].items() if v is not None}
    if gt.get("Scrape raw (JSON)"):  # scrub prices out of the raw scrape blob
        gt["Scrape raw (JSON)"] = re.sub(
            r'"scrape_price_[a-z]+"\s*:\s*"[^"]*"\s*,?', "", gt["Scrape raw (JSON)"])
    candidates = task["related_candidates"]
    filter_schema = task.get("filter_schema", [])

    match_kind = str(task["ground_truth"].get("Match kind") or "")
    weak_match_block = ""
    if match_kind.startswith(("name", "model")):
        weak_match_block = f"""
## ⚠ СЛАБО СЪВПАДЕНИЕ ({match_kind})
Скрейпнатите данни и снимката са намерени по ПРИБЛИЗИТЕЛНО име — може да описват ДРУГ,
подобен продукт (една обява често е съпоставена на няколко складови кода). Затова:
- НЕ пренасяй съдържание/цвят/брой части от снимката или скрейпа, освен ако складовото
  име ги потвърждава;
- НЕ преразказвай оригиналното описание (то е недоверено AI съдържание);
- направи МИНИМАЛНИ безопасни корекции (език, формат, каталожен номер), опиши
  несигурността в "Проблеми" и сложи "needs_human": true.
"""
    prompt = f"""Ти си прецизен проверител на продуктови данни за български онлайн магазин.
Обработваш ТОЧНО ЕДИН продукт. Никога не измисляй факти — работи само с данните по-долу и с инструментите web_search / vision_analyze.
{weak_match_block}

## РЪКОВОДСТВО (спазвай го стриктно)
{guide_text()}

## ПРОДУКТ — текущи стойности (AI-генерирани, може да съдържат грешки)
```json
{json.dumps(product, ensure_ascii=False, indent=1)}
```

## GROUND TRUTH — надеждни данни (складова база Microinvest + скрейпнати данни от доставчик)
```json
{json.dumps(gt, ensure_ascii=False, indent=1)}
```

## КАНДИДАТИ за "Свързани" (продукти със същия префикс на кода; избирай САМО от тях)
```json
{json.dumps(candidates, ensure_ascii=False)}
```

## ФИЛТЪРНА СХЕМА за категорията (ключове и ДОПУСТИМИ стойности за Атрибути)
```json
{json.dumps(filter_schema, ensure_ascii=False, indent=1)}
```

## ВАЛИДНИ КАТЕГОРИИ на сайта (Категории може да съдържа САМО такива, разделени с ";")
{"; ".join(known_categories())}

## ЗАДАЧА
Провери и коригирай AI-генерираните полета: Наименование, Описание, Мета наименование, Мета описание, Бранд, Категории, Тегло (кг), Атрибути, Синоними, Варианти, Свързани.
1. Сравни текущите стойности с ground truth. При противоречие ground truth печели.
2. Наименование: приложи формулата от ръководството (тип продукт първо, без каталожни номера, без съкращения, единици на латиница).
3. Бранд: ако липсва — вземи от "Бранд (скрейп)"; ако го няма там, но има вероятен бранд в името, провери с web_search дали брандът съществува. Ако не може да се потвърди — остави празно.
4. Описание: следвай SEO HTML формата от ръководството (h2 + увод + <ul> характеристики + употреба). Материалът трябва да е потвърден.
5. Атрибути: нормализирай по филтърната схема — това захранва филтрите на сайта. Попълни всички известни групи с допустими стойности.
6. Снимка: ако има URL (Снимки/Снимка), извикай vision_analyze ВЕДНЪЖ и провери едновременно: материал/цвят/форма/брой части за описанието и атрибутите + одит на снимката (воден знак? бял фон? няколко продукта? качество? съответствие с името?). Резултата от одита запиши в "Снимка проблеми". Брой части, изписан на опаковката (напр. "12" на кутията), е надежден източник.
   ЧЕСТНОСТ: ако vision_analyze върне грешка — опитай ВТОРИ път. Ако и той е неуспешен, запиши "визуална проверка": "неуспешна" и премини в ОГРАНИЧЕН РЕЖИМ:
   - единственият надежден източник е GROUND TRUTH (складово име, скрейпнати данни);
   - оригиналните Наименование/Описание/Атрибути са НЕДОВЕРЕНИ (те са AI-генерираните данни, които поправяме) — НЕ преразказвай съдържание/цветове/брой части от тях;
   - описанието остава кратко и общо (без списък на съдържанието, без цвят/материал), а липсите се отбелязват в "Проблеми". Излъгано "ок" разваля данните на магазина.
7. Свързани: само реални варианти на същия модел (различие само в размер/цвят), избрани от списъка с кандидати. Ако няма — празно.
8. Емпирични стойности (код, цена, количество, мярка) НЕ ти се дават и НЕ ги връщаш —
   те се управляват отделно от системата. Никога не споменавай цена/количество/код в текст.
9. Всеки открит, но нерешен проблем опиши кратко в "Проблеми".

## ФОРМАТ НА ОТГОВОРА (СТРИКТЕН)
Финалният ти отговор е САМО ЕДИН ```json блок — БЕЗ обяснения, разсъждения или резюме
преди или след него. Всякакъв текст извън JSON блока е ГРЕШКА и проваля обработката.
Ключове (САМО тези съдържателни полета): {", ".join(EDITABLE)}, плюс:
- "Проблеми": низ или null
- "Снимка проблеми": низ (напр. "воден знак; цветен фон") или null
- "визуална проверка": "ок" | "неуспешна" | "няма снимка". "неуспешна" е САМО когато
  инструментът върне ГРЕШКА. Успешен анализ, който ПРОТИВОРЕЧИ на текста, е "ок" —
  снимката печели, а противоречието се описва в "Проблеми".
- "confidence": "high" | "medium" | "low"
- "needs_human": true/false — САМО за НЕРЕШЕНИ проблеми: противоречие между източници,
  съмнение за грешна идентификация на продукта, невъзможност да се спази правило.
  Проблем, РЕШЕН по правилата (бранд оставен празен, защото е непотвърден; тегло,
  оценено и отбелязано; описание без непотвърден материал), НЕ изисква needs_human —
  отбелязва се само в "Проблеми".
- "lesson": ЕДНО кратко общовалидно правило за бъдещи продукти (ако научи нещо ново, което го няма в ръководството), иначе null
Започни отговора си директно с ```json
"""
    if len(prompt) > MAX_PROMPT_CHARS:
        prompt = prompt[:MAX_PROMPT_CHARS] + "\n…[входът е съкратен — работи с наличното]"
    return prompt


def extract_json(text):
    blocks = re.findall(r"```json\s*(.*?)```", text, re.DOTALL)
    for block in reversed(blocks):
        try:
            return json.loads(block)
        except Exception:
            pass
    # fallback: last balanced top-level object
    end = text.rfind("}")
    while end != -1:
        depth = 0
        for start in range(end, -1, -1):
            if text[start] == "}":
                depth += 1
            elif text[start] == "{":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:end + 1])
                    except Exception:
                        break
        end = text.rfind("}", 0, max(end - 1, 0)) if end > 0 else -1
    return None


# Russian-only Cyrillic letters that never appear in literary Bulgarian — a
# reliable contamination signal, safe to transliterate.
_RU_LETTERS = str.maketrans({"э": "е", "Э": "Е", "ы": "и", "Ы": "И",
                             "ё": "е", "Ё": "Е"})


def apply_ru_fix(text):
    """Deterministically replace common Russian-isms with Bulgarian, preserving
    case, and transliterate Russian-only letters. Runs before spellcheck so
    leaked words become clean, not human work."""
    if not text:
        return text, False

    def repl(m):
        w = m.group(0)
        fix = RU_FIX.get(w.lower())
        if not fix:
            return w
        return fix.capitalize() if w[:1].isupper() else fix

    pattern = re.compile(r"[а-яА-ЯёэыЁЭЫ]+")
    out = pattern.sub(repl, str(text)).translate(_RU_LETTERS)
    return out, out != str(text)


def validate(task, parsed):
    """Returns (fields, meta_notes). Raises ValueError when unusable.

    The agent only returns EDITABLE content fields; operational columns
    (Код, Цена, Количество, Мярка, Доставчик, ...) and Снимки/Серия are taken
    verbatim from the source — the AI never touches or even sees them.
    """
    notes = []
    original = task["product"]

    fields = {}
    for col in ENRICHED_COLS:
        if col not in EDITABLE:
            # Driver-owned: code, empiric values, image URL, series — verbatim.
            fields[col] = original.get(col)
            continue
        if col in parsed:
            v = parsed[col]
            if col == "Атрибути":
                # Normalize the filter-feed format regardless of how the model
                # shaped it (dict, newlines, list) -> "Ключ: Стойност; ..."
                if isinstance(v, dict):
                    v = "; ".join(f"{k}: {val}" for k, val in v.items() if val)
                elif isinstance(v, (list, tuple)):
                    v = "; ".join(str(x) for x in v if x)
                elif v:
                    v = re.sub(r"\s*[\r\n]+\s*", "; ", str(v).strip())
            elif isinstance(v, (list, tuple)):  # e.g. Синоними as an array
                v = ", ".join(str(x) for x in v if x is not None)
            elif isinstance(v, dict):
                v = json.dumps(v, ensure_ascii=False)
            fields[col] = None if v in ("", "null") else v
        else:
            fields[col] = original.get(col)
            notes.append(f"missing_key:{col}")

    # Deterministic Russian-ism cleanup on all customer-facing text.
    for col in ("Наименование", "Описание", "Мета наименование",
                "Мета описание", "Синоними", "Атрибути"):
        if fields.get(col):
            fixed, changed = apply_ru_fix(fields[col])
            if changed:
                fields[col] = fixed
                notes.append(f"ru_fixed:{col}")

    # AI-filler clichés (research: hurt trust + read as AI). Flag so the polish
    # pass rewrites them; the flag itself is not escalated (advisory).
    desc_low = str(fields.get("Описание") or "").lower()
    for cliche in ("издигнете", "перфектен за всеки", "не търсете повече",
                   "в днешно време", "висококачествен продукт",
                   "elevate your", "look no further", "perfect for any"):
        if cliche in desc_low:
            notes.append(f"ai_cliche:{cliche}")
            break

    name = str(fields.get("Наименование") or "").strip()
    if not name:
        raise ValueError("empty Наименование")

    # Category must stay within the site's category tree.
    cats = known_categories()
    if cats and fields.get("Категории"):
        parts = [p.strip() for p in str(fields["Категории"]).split(";") if p.strip()]
        if any(p not in cats for p in parts):
            fields["Категории"] = original.get("Категории")
            notes.append("reverted_invalid_category")

    # Brand: never a supplier name.
    brand = str(fields.get("Бранд") or "").strip().lower()
    if brand and any(s in brand for s in SUPPLIER_NAMES):
        notes.append(f"dropped_supplier_brand:{fields['Бранд']}")
        fields["Бранд"] = None

    # Weight policy: never emptied — restore the original if the agent removed it.
    if not fields.get("Тегло (кг)") and original.get("Тегло (кг)"):
        fields["Тегло (кг)"] = original.get("Тегло (кг)")
        notes.append("restored_weight")

    # Fabrication firewall for Материал/Цвят: a visual claim needs visual proof.
    # Value is kept only when its stem appears in GROUND TRUTH text (the till +
    # scraped supplier data), or the worker reported a successful image check.
    # The original Enriched fields are NOT a source — they are the AI-generated
    # data under repair (a "black wallet set" survived that way while the photo
    # showed a green camping kit).
    vision_ok = str(parsed.get("визуална проверка") or "").strip().lower() in ("ок", "ok")
    source_text = json.dumps(task.get("ground_truth"), ensure_ascii=False).lower()

    def textually_sourced(value):
        # Trim inflection endings: "Меден" must match GT's "медно покритие".
        words = str(value).strip().lower().split()
        if not words:
            return False
        stem = words[0][:max(3, len(words[0]) - 2)]
        return stem in source_text

    # Attributes: drop placeholder/junk values agents sometimes emit.
    attrs = fields.get("Атрибути")
    if attrs:
        kept = []
        for part in str(attrs).split(";"):
            part = part.strip()
            if not part:
                continue
            key = part.split(":", 1)[0].strip() if ":" in part else ""
            value = part.split(":", 1)[1].strip() if ":" in part else part
            if value.lower() in {"needs_human", "unknown", "null", "none", "n/a", "?", "-", ""}:
                notes.append(f"dropped_attr:{part[:40]}")
                continue
            if key in ("Материал", "Цвят") and not vision_ok and not textually_sourced(value):
                notes.append(f"dropped_unsourced:{part[:40]}")
                continue
            kept.append(part)
        fields["Атрибути"] = "; ".join(kept) if kept else None

    # Related products must come from the candidate list; cap at 10.
    allowed = {c["Код"] for c in task["related_candidates"]}
    rel = fields.get("Свързани")
    if rel:
        kept = []
        for part in re.split(r"[;\n]+", str(rel)):
            part = part.strip()
            if not part:
                continue
            rcode = part.split("|")[0].strip()
            if rcode in allowed:
                kept.append(part)
            else:
                notes.append(f"dropped_related:{rcode}")
        if len(kept) > 10:
            notes.append(f"related_capped:{len(kept)}")
            kept = kept[:10]
        fields["Свързани"] = "; ".join(kept) if kept else None

    # --- Text-quality guardrails -------------------------------------------
    # Name: no leading catalog codes, no banned abbreviations, length cap.
    name = str(fields.get("Наименование") or "")
    stripped = re.sub(r"^\s*[\d/.\-]{4,}\s+", "", name).strip()
    if stripped and stripped != name:
        fields["Наименование"] = stripped
        notes.append("stripped_catalog_prefix")
        name = stripped
    if re.search(r"\bК-т\b|\d+\s?бр\b|\bс/у\b", name, re.IGNORECASE):
        notes.append("name_abbreviation")
    if len(name) > 80:
        # Trim at a word/comma boundary rather than escalate — an over-long
        # name has a safe deterministic fix.
        cut = name[:80]
        boundary = cut.rfind(",") if "," in cut[60:] else cut.rfind(" ")
        fields["Наименование"] = (cut[:boundary] if boundary > 40 else cut).strip().rstrip(",")
        notes.append("name_trimmed")

    # Description: structure, meta-commentary, Russian-isms, duplication risk.
    desc = str(fields.get("Описание") or "")
    if desc:
        cleaned = re.sub(
            r"\s*\((?:визуално потвърдено|ако материалът позволява|приблизително|"
            r"не може да се потвърди[^)]*)\)", "", desc, flags=re.IGNORECASE)
        if cleaned != desc:
            fields["Описание"] = cleaned
            notes.append("stripped_meta_comments")
            desc = cleaned
        # Placeholder bullets ("Материал: Непотвърден") are internal state, not
        # customer copy — drop the whole <li>.
        cleaned = re.sub(
            r"<li>(?:<strong>)?[^<:]{2,30}:?(?:</strong>)?\s*"
            r"(?:Непотвърден[оа]?|Неизвестен[оа]?|Липсва|N/?A|unknown|няма данни)\.?\s*</li>",
            "", desc, flags=re.IGNORECASE)
        if cleaned != desc:
            fields["Описание"] = cleaned
            notes.append("stripped_placeholder_bullets")
            desc = cleaned
        if "<h2>" not in desc or "<ul>" not in desc:
            notes.append("desc_structure")
        for bad_word in ("подходит", "применение", "изготовлен", "прочный", "ёмкость"):
            if bad_word in desc.lower():
                notes.append(f"russianism:{bad_word}")
        words = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", desc)))
        if not 50 <= words <= 450:
            notes.append(f"desc_length:{words}w")

    # Homoglyph repair: models sometimes emit Latin lookalikes inside Cyrillic
    # words ("тоaлетна" with Latin 'a') — invisible to readers, poison for site
    # search. Any mostly-Cyrillic word gets its Latin lookalikes transliterated.
    _HOMO = str.maketrans("aeopcxyABEKMHOPCTX", "аеорсхуАВЕКМНОРСТХ")

    def _fix_homoglyphs(text):
        def fix_word(m):
            w = m.group(0)
            cyr = sum(1 for ch in w if "а" <= ch.lower() <= "я")
            lat = sum(1 for ch in w if ch in "aeopcxyABEKMHOPCTX")
            return w.translate(_HOMO) if cyr > lat else w
        return re.sub(r"\w*[а-яА-Я]\w*", fix_word, str(text))

    for k in ("Наименование", "Описание", "Мета наименование", "Мета описание",
              "Синоними", "Атрибути"):
        v = fields.get(k)
        if v:
            fixed = _fix_homoglyphs(v)
            if fixed != v:
                fields[k] = fixed
                notes.append(f"homoglyphs_fixed:{k}")

    # Deterministic Bulgarian spellcheck (phunspell/bg_BG) over customer-facing
    # text — catches garbled words both models and the reviewer keep missing.
    try:
        from bg_spell import unknown_words
        text_blob = " ".join(str(fields.get(k) or "") for k in
                             ("Наименование", "Описание", "Мета наименование",
                              "Мета описание", "Атрибути"))
        known_blob = json.dumps(task.get("ground_truth"), ensure_ascii=False) + \
            " " + json.dumps(task.get("filter_schema", []), ensure_ascii=False)
        bad_words = unknown_words(text_blob, limit=8, known_text=known_blob)
        if bad_words:
            notes.append("misspelled:" + ",".join(bad_words))
    except Exception as spell_err:
        notes.append(f"spellcheck_unavailable:{str(spell_err)[:60]}")

    # Meta lengths (soft flags; the human queue picks up chronic offenders).
    if len(str(fields.get("Мета наименование") or "")) > 70:
        notes.append("meta_title_long")
    md_len = len(str(fields.get("Мета описание") or ""))
    if fields.get("Мета описание") and not 100 <= md_len <= 220:
        notes.append(f"meta_desc_len:{md_len}")

    # Synonyms: dedupe, cap at 15 terms.
    syn = fields.get("Синоними")
    if syn:
        seen_terms, terms = set(), []
        for term in str(syn).split(","):
            term = term.strip()
            if term and term.casefold() not in seen_terms:
                seen_terms.add(term.casefold())
                terms.append(term)
        if len(terms) > 15:
            notes.append(f"synonyms_capped:{len(terms)}")
            terms = terms[:15]
        fields["Синоними"] = ", ".join(terms)

    # Weight: numeric and physically plausible for household goods.
    w = fields.get("Тегло (кг)")
    if w is not None:
        try:
            wf = float(str(w).replace(",", "."))
            if not 0.005 <= wf <= 100:
                fields["Тегло (кг)"] = original.get("Тегло (кг)")
                notes.append(f"weight_implausible:{w}")
        except (TypeError, ValueError):
            fields["Тегло (кг)"] = original.get("Тегло (кг)")
            notes.append(f"weight_not_numeric:{w}")
    return fields, notes


def maybe_add_lesson(lesson):
    if NO_LESSONS:
        return False
    if not lesson or not isinstance(lesson, str):
        return False
    lesson = " ".join(lesson.split())
    # Agents sometimes echo the guide's bullet format — strip any "- [date]" prefixes.
    lesson = re.sub(r"^(?:-\s*)?(?:\[\d{4}-\d{2}-\d{2}\]\s*)+", "", lesson).strip()
    if not (10 <= len(lesson) <= 300):
        return False
    guide = GUIDE_PATH.read_text(encoding="utf-8")
    existing = [ln for ln in guide.splitlines() if ln.strip().startswith("- ")]
    if len(existing) >= 80:  # keep the guide bounded
        return False
    new_words = set(re.findall(r"\w+", lesson.lower()))
    for line in existing:
        words = set(re.findall(r"\w+", line.lower()))
        if new_words and len(new_words & words) / len(new_words) > 0.7:
            return False  # near-duplicate of an existing rule
    with open(GUIDE_PATH, "a", encoding="utf-8") as f:
        f.write(f"- [{date.today().isoformat()}] {lesson}\n")
    return True


def run_agent(prompt, toolsets=TOOLSETS, model_args=None):
    env = dict(os.environ, HERMES_HOME=HERMES_HOME)
    proc = subprocess.run(
        [HERMES_EXE, "-z", prompt, "--cli", "-t", toolsets,
         *(model_args if model_args is not None else MODEL_ARGS)],
        capture_output=True, timeout=AGENT_TIMEOUT_S, env=env,
    )
    out = proc.stdout.decode("utf-8", errors="replace")
    err = proc.stderr.decode("utf-8", errors="replace")
    return proc.returncode, out, err


# --- Direct-API worker ------------------------------------------------------
# The generation step is a plain chat completion (prompt -> JSON), so we call the
# provider's OpenAI-compatible endpoint directly instead of the Hermes agent CLI.
# Faster, and immune to the CLI's context-compression mis-budgeting. Providers
# are keyed by the --provider token used in MODEL_PAIRS worker_args.
DIRECT_PROVIDERS = {
    "dashscope-intl": ("https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
                       "DASHSCOPE_INTL_API_KEY"),
    "nvidia": ("https://integrate.api.nvidia.com/v1", "NVIDIA_API_KEY"),
    "groq": ("https://api.groq.com/openai/v1", "GROQ_API_KEY"),
    "zai": ("https://api.z.ai/api/paas/v4", "GLM_API_KEY"),
    "mistral": ("https://api.mistral.ai/v1", "MISTRAL_API_KEY"),
    "cerebras": ("https://api.cerebras.ai/v1", "CEREBRAS_API_KEY"),
    "cohere": ("https://api.cohere.com/compatibility/v1", "COHERE_API_KEY"),
}
WORKER_SYS = (
    "Ти си прецизен редактор на продуктови текстове за български онлайн магазин "
    "за домашни стоки. Пишеш ИЗКЛЮЧИТЕЛНО на чист, естествен български език. "
    "АБСОЛЮТНО ЗАБРАНЕНИ са руски и сръбски думи и буквите ы, э, ё. Без английски "
    "или китайски думи в текста. Спазвай точно исканата JSON структура и започни "
    "отговора си директно с ```json."
)
_DIRECT_CLIENTS = {}


def _direct_key(key_env):
    # Prefer the hermes .env (the managed store where keys are rotated) over a
    # possibly-stale process/User env var — a User env var is cached by the running
    # gateway and inherited by every cron child, so without this a rotated key would
    # not take effect until the whole gateway restarts (2026-07-15: exactly this bit
    # us when swapping the arrears Alibaba key for a fresh one).
    env_path = Path(HERMES_HOME) / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if line.startswith(key_env + "="):
                v = line.split("=", 1)[1].strip()
                if v:
                    return v
    return os.environ.get(key_env, "")


def _direct_client(base_url, key_env):
    if base_url not in _DIRECT_CLIENTS:
        from openai import OpenAI
        _DIRECT_CLIENTS[base_url] = OpenAI(api_key=_direct_key(key_env),
                                           base_url=base_url, timeout=AGENT_TIMEOUT_S,
                                           max_retries=0)  # chain handles failover
    return _DIRECT_CLIENTS[base_url]


REVIEW_SYS = (
    "Ти си строг независим контролен редактор за български онлайн магазин. "
    "Проверяваш чужда продуктова обработка спрямо подадените достоверни данни и "
    "връщаш САМО искания JSON. Пиши на чист български без руски/сръбски думи."
)


def run_direct(prompt, model_args, system=WORKER_SYS, max_tokens=2000):
    """Direct OpenAI-compatible chat completion. Returns (rc, out, err) so the
    call site stays identical to run_agent. Raises on provider error (caller
    fails over)."""
    model = model_args[model_args.index("-m") + 1]
    provider = model_args[model_args.index("--provider") + 1]
    base_url, key_env = DIRECT_PROVIDERS[provider]
    client = _direct_client(base_url, key_env)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": prompt}],
        temperature=0.3, max_tokens=max_tokens)
    try:
        import telemetry as _tel
        _tel.record(model, provider, resp)
    except Exception:
        pass
    return 0, (resp.choices[0].message.content or ""), ""


def run_worker_direct(prompt, model_args):
    return run_direct(prompt, model_args, system=WORKER_SYS)


def generate_with_chain(prompt, system=WORKER_SYS):
    """Generate through WORKER_CHAIN, skipping models already in exhausted_models.txt
    and marking any that newly report free-quota exhaustion. Returns (text, model)
    or raises if every model fails. Used by the worker AND the auxiliary passes
    (vision-correction, polish) so none of them dies on a single drained quota."""
    exhausted = _load_exhausted()
    chain = [a for a in WORKER_CHAIN if a[a.index("-m") + 1] not in exhausted]
    if not _dashscope_allowed():                       # billing incident: dashscope opt-in only
        chain = [a for a in chain if a[a.index("--provider") + 1] != "dashscope-intl"]
    chain = chain or [a for a in WORKER_CHAIN if a[a.index("--provider") + 1] != "dashscope-intl"]
    last = None
    for args in chain:
        model = args[args.index("-m") + 1]
        try:
            _, out, _ = run_direct(prompt, args, system=system)
            return out, model
        except Exception as e:
            last = e
            maybe_pause_on_arrearage(e)
            if _is_quota_error(e) and model not in exhausted:
                _mark_exhausted(model)
                exhausted.add(model)
    raise last if last else RuntimeError("no model available")


# Reviewer failover chain — direct API, spread across providers so no single
# free-tier rate limit (zai saturates fast under 6 lanes) stalls the queue.
# Llama on Groq leads: fast (~2s), different family from the Qwen worker, and a
# quota independent of the worker's Alibaba and the vision pass's NVIDIA.
REVIEW_CHAIN = [
    ["-m", "llama-3.3-70b-versatile", "--provider", "groq"],
    ["-m", "glm-4.7-flash", "--provider", "zai"],
    ["-m", "meta/llama-3.3-70b-instruct", "--provider", "nvidia"],
]


def run_reviewer_direct(prompt):
    last = None
    for i, args in enumerate(REVIEW_CHAIN):
        try:
            return run_direct(prompt, args, system=REVIEW_SYS)
        except Exception as e:
            last = e
    raise last if last else RuntimeError("no reviewer available")


_NV_CLIENT = None


def _nvidia_client():
    global _NV_CLIENT
    if _NV_CLIENT is None:
        from openai import OpenAI
        key = os.environ.get("NVIDIA_API_KEY", "")
        if not key:
            env_path = HERMES_HOME + r"\.env"
            for line in Path(env_path).read_text(encoding="utf-8").splitlines():
                if line.startswith("NVIDIA_API_KEY="):
                    key = line.split("=", 1)[1].strip()
                    break
        _NV_CLIENT = OpenAI(api_key=key,
                            base_url="https://integrate.api.nvidia.com/v1",
                            timeout=120)
    return _NV_CLIENT


def vision_complete(content, max_tokens=300):
    """Run a vision chat over VL_CHAIN (NVIDIA → Mistral), returning the text of the first
    provider that answers. Raises only if every VL provider fails. Used by the record-vs-
    photo verify and the classifier vision tie-break so both survive a vision outage."""
    last = None
    for prov, model in VL_CHAIN:
        try:
            if prov == "nvidia":
                client = _nvidia_client()
            else:
                base_url, key_env = DIRECT_PROVIDERS[prov]
                client = _direct_client(base_url, key_env)
            r = client.chat.completions.create(
                model=model, temperature=0, max_tokens=max_tokens,
                messages=[{"role": "user", "content": content}])
            txt = r.choices[0].message.content or ""
            if txt.strip():
                return txt
        except Exception as e:
            last = e
    if last:
        raise last
    return ""


def _encode_url(u):
    """Percent-encode a URL's path/query so raw supplier filenames with spaces or
    parens (e.g. mira-n '140 - Copy.jpg', '187 (2).png') fetch correctly instead
    of raising 'control characters' or 404. Idempotent (safe='%' keeps existing %)."""
    try:
        p = urllib.parse.urlsplit(u)
        path = urllib.parse.quote(p.path, safe="/%")
        query = urllib.parse.quote(p.query, safe="=&%")
        return urllib.parse.urlunsplit((p.scheme, p.netloc, path, query, p.fragment))
    except Exception:
        return u


def _origin(u):
    try:
        p = urllib.parse.urlsplit(u)
        return f"{p.scheme}://{p.netloc}/"
    except Exception:
        return u


def verify_against_image(image_url, fields):
    """Independent vision check of the FINAL product against its photo.

    Returns dict {ok, mismatch, corrections} or None if vision unavailable.
    Only judges what a photo can show: product type, shape, material, colour,
    piece count. A stronger model (llama-90b-vision) than the worker's inline
    check, with the single job of catching contradictions like a round name on
    a rectangular pan.
    """
    if not image_url:
        return None
    try:
        req = urllib.request.Request(_encode_url(image_url), headers={
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/120 Safari/537.36"),
            "Referer": _origin(image_url)})
        data = urllib.request.urlopen(req, timeout=30).read()
        from PIL import Image
        im = Image.open(io.BytesIO(data)).convert("RGB")
        im.thumbnail((1024, 1024))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=85)
        b64 = base64.b64encode(buf.getvalue()).decode()
    except Exception as e:
        return {"ok": None, "error": f"image_load:{str(e)[:80]}"}

    prompt = (
        "Ти си контрол на качеството. Разгледай СНИМКАТА и провери дали описанието "
        "на продукта ѝ съответства. За всяко несъответствие дай ВЯРНАТА стойност "
        "според снимката. Отговори САМО с JSON:\n"
        '{"тип_ок": true/false, "форма_ок": true/false, "материал_ок": true/false, '
        '"цвят_ок": true/false, "брой_ок": true/false, '
        '"вярна_форма": "правоъгълна/кръгла/овална/квадратна/друга или null", '
        '"вярен_тип": "какво е всъщност, или null", '
        '"вярен_материал": "материал от снимката или null", '
        '"вярен_цвят": "основен цвят от снимката или null", '
        '"верен_брой": "брой части ако се вижда, или null", '
        '"видим_бранд": "марката НА САМИЯ продукт/опаковка ако ясно се чете, иначе null", '
        '"сигурност": "висока/средна/ниска — колко си сигурен в оценката от снимката", '
        '"забележка": "кратко описание на разминаването или null"}\n\n'
        "ВАЖНО: сигурност=висока САМО ако снимката е ясна и разминаването е недвусмислено. "
        "За видим_бранд: чети САМО марка отпечатана върху продукта/опаковката. "
        "ИГНОРИРАЙ водни знаци и лога на магазини/доставчици (напр. EGERA, LEVENA, MIRA-N) — "
        "те НЕ са марка на продукта. Не отгатвай; ако не си сигурен върни null.\n"
        f"ЗАЯВЕНО:\nИме: {fields.get('Наименование')}\n"
        f"Атрибути: {fields.get('Атрибути')}\n"
        f"Описание (само за проверка): {str(fields.get('Описание'))[:400]}"
    )
    try:
        out = vision_complete([
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}],
            max_tokens=300)
        m = re.search(r"\{.*\}", out, re.DOTALL)
        v = json.loads(m.group(0)) if m else None
        if not v:
            return {"ok": None, "error": "no_json"}
        mismatches = [k for k in ("тип_ок", "форма_ок", "материал_ок", "цвят_ок", "брой_ок")
                      if v.get(k) is False]
        return {"ok": not mismatches, "mismatch": mismatches, "detail": v}
    except Exception as e:
        return {"ok": None, "error": f"vision_call:{str(e)[:80]}"}


def vision_guided_correct(fields, detail, model_args=None):
    """When the photo contradicts the text, regenerate the affected fields to match
    what the PHOTO shows. Returns {Наименование, Атрибути, Описание} or None. Only
    the vision-confirmed facts (type/shape/material/colour/count) change; sizes,
    code, price and everything else are frozen."""
    corr = {k: detail.get(k) for k in
            ("вярна_форма", "вярен_тип", "вярен_материал", "вярен_цвят", "верен_брой")
            if detail.get(k)}
    if not corr:
        return None
    facts = "; ".join(f"{k}: {v}" for k, v in corr.items())
    payload = {k: fields.get(k) for k in ("Наименование", "Атрибути", "Описание") if fields.get(k)}
    prompt = (
        "Визуална проверка на СНИМКАТА установи следните ВЕРНИ факти за продукта "
        f"(имат приоритет над текста): {facts}. Забележка: {detail.get('забележка') or ''}.\n"
        "Коригирай полетата по-долу да отговарят на тези факти — смени САМО засегнатите "
        "факти (тип, форма, материал, цвят, брой) в името, атрибутите и описанието. "
        "НЕ променяй размери/код/цена. Запази стила и HTML структурата. Пиши чист "
        "български без руски думи. Върни САМО ```json блок със същите ключове:\n"
        f"```json\n{json.dumps(payload, ensure_ascii=False, indent=1)}\n```"
    )
    try:
        out, _ = generate_with_chain(prompt)
        return extract_json(out)
    except Exception:
        return None


def run_polish(fields, bad_words, model_args):
    """One focused rewrite that fixes only wording, freezing every fact.
    Returns a dict of corrected text fields, or None."""
    payload = {k: fields.get(k) for k in
               ("Наименование", "Описание", "Мета наименование",
                "Мета описание", "Синоними", "Атрибути") if fields.get(k)}
    prompt = (
        "Пренапиши текста на БЕЗУПРЕЧЕН книжовен български. Поправи всички сгрешени, "
        "чужди (руски/английски) или несъществуващи думи — особено: "
        f"{', '.join(bad_words)}. НЕ променяй факти (материал, размери, цвят, брой, "
        "тип) — само езика и правописа. Запази HTML структурата на описанието и "
        "формата на атрибутите. Върни САМО един ```json блок със същите ключове:\n"
        f"```json\n{json.dumps(payload, ensure_ascii=False, indent=1)}\n```"
    )
    # Direct API through the resilient chain (skips exhausted models).
    out, _ = generate_with_chain(prompt)
    return extract_json(out)


def build_review_prompt(task, fields, worker_meta, bad_words=None):
    # NOTE deliberately NO task["product"] here: the reviewer once used the
    # original AI fields as "truth" and resurrected a wrong contents list the
    # vision-informed worker had just removed. The reviewer reviews language,
    # format and schema against GROUND TRUTH only.
    gt = {k: v for k, v in task["ground_truth"].items() if v is not None}
    return f"""Ти си независим контролен редактор за български онлайн магазин. Друг агент е обработил
продукт — провери работата му БЕЗКОМПРОМИСНО и я поправи, ако е нужно.

## ГРАНИЦИ НА ТВОИТЕ ПРАВОМОЩИЯ (КРИТИЧНО)
Работният агент е ГЛЕДАЛ СНИМКАТА на продукта — ти НЕ МОЖЕШ да я видиш.
Съдържание, цвят, брой части и материал в НЕГОВИЯ текст са по-надеждни от всичко,
което ти "знаеш" за продукта. Затова:
- НЕ обръщай фактически решения, основани на снимката: тип продукт, материал, цвят,
  категория, брой части. Ако работникът е преименувал продукта след визуална проверка,
  приеми го за вярно.
- Ако имаш СЪМНЕНИЕ за фактическо решение — сложи "needs_human": true и го опиши в
  issues, но НЕ го променяй.
- Твоята работа е: език (правопис, чужди думи), формати и дължини, съответствие на
  атрибутите с допустимите стойности, вътрешна съгласуваност, кодове на Свързани.

## GROUND TRUTH (надеждни данни — склад + доставчик)
```json
{json.dumps(gt, ensure_ascii=False, indent=1)}
```

## ФИЛТЪРНА СХЕМА (допустими ключове/стойности за Атрибути)
```json
{json.dumps(task.get("filter_schema", []), ensure_ascii=False)}
```

## КАНДИДАТИ за Свързани (единствено допустими кодове)
```json
{json.dumps([c["Код"] for c in task["related_candidates"]], ensure_ascii=False)}
```

## РЕЗУЛТАТ НА РАБОТНИЯ АГЕНТ (за проверка)
```json
{json.dumps(fields, ensure_ascii=False, indent=1)}
```
Отбелязани от него проблеми: {worker_meta.get("Проблеми") or "няма"}
{("АВТОМАТИЧНАТА ПРАВОПИСНА ПРОВЕРКА откри сгрешени/чужди думи, които СИ ДЛЪЖЕН да поправиш "
  "в корекцията (замени с книжовни български думи): " + ", ".join(bad_words)) if bad_words else ""}

## КОНТРОЛЕН СПИСЪК (провери ВСЯКО)
1. ЕЗИК: книжовен български — нула руски думи ("цвет", "подходит"), нула английски
   думи/фрази в текста, нула изкривени/несъществуващи думи. Провери дума по дума.
   ИЗКЛЮЧЕНИЕ: мерните единици са НА ЛАТИНИЦА по стандарт на магазина (ml, cm, l, W) —
   НЕ ги "поправяй" на кирилица. В атрибутите пиши само реални стойности — никакви
   "needs_human"/"unknown" плейсхолдъри (при съмнение пропусни атрибута и го опиши в issues).
2. Наименование: точен тип продукт (резерва ≠ моп), формат "[Тип] [Бранд] [характеристика]
   [размер] [цвят]", без каталожни номера, без съкращения, ≤80 знака.
3. Атрибути: всяка стойност ТОЧНО от допустимите във филтърната схема. НЕ ДОБАВЯЙ нови
   атрибути (включително Цвят/Материал), които работникът не е посочил — ти не виждаш
   снимката и всяка твоя добавка е предположение. Само поправяй/премахвай съществуващи.
4. Бранд: или потвърден и правилно изписан на латиница, или празен.
5. Описание: формат h2 + увод + <ul> + употреба; никакви твърдения без източник
   (материал/размери/съвместимост); 120–250 думи; без повторения. БЕЗ мета-коментари
   в клиентския текст — "(визуално потвърдено)", "(ако материалът позволява)" са забранени.
   Етикети на bullet-редовете: Материал, Цвят, Размери, Обем, Брой части, Предназначение, Поддръжка.
6. Мета наименование ≤60 знака; Мета описание 150–160 знака, чист текст.
7. Свързани: провери САМО за невалидни кодове (извън списъка с кандидати) или очевидно
   грешни двойки. ПРАЗНОТО поле е ВАЛИДНО решение на работника — НИКОГА не изисквай
   и не добавяй свързани продукти.
8. Тегло (кг): попълнено и правдоподобно за типа продукт. Никога не го изтривай.
9. Непроменими колони (Код, Каталожен номер, Цена, Количество, Снимки...) — непокътнати.

## ОТГОВОР (СТРИКТЕН ФОРМАТ)
Върни САМО ЕДИН ```json блок — без обяснения преди или след него. Започни директно с ```json
{{"verdict": "approve" или "revise",
 "issues": ["кратък списък на откритите проблеми"],
 "corrected": null или ПЪЛНИЯТ коригиран обект с всичките 21 колони (само при "revise"),
 "needs_human": true/false}}
"needs_human" е САМО за нерешени проблеми (противоречия, съмнителна идентификация) —
НЕ за коректно приложени правила (празен непотвърден бранд, оценено тегло) и НЕ за
козметика, която сам си коригирал.
"""


# Autonomous mode (owner directive 2026-07-14): each product is investigated by a
# tool-using agent (agent_enrich.py) instead of the fixed worker->reviewer->vision chain.
# Set PIPELINE_AGENTIC=0 to fall back to the (backed-up) direct pipeline below.
AGENTIC = os.environ.get("PIPELINE_AGENTIC", "1") == "1"


_CONF_RANK = {"high": 2, "medium": 1, "low": 0}
_PRIOR_Q = None


def _prior_quality_index():
    """{code: {conf, brand, fallback, nfields}} for the CURRENT canonical of every
    finished product. Built lazily once per process (a few MB parse), cached — so it
    costs nothing until the first write and nothing on first-time products. Used by the
    write quality-gate to stop a re-processing run from DOWNGRADING a good product."""
    global _PRIOR_Q
    if _PRIOR_Q is not None:
        return _PRIOR_Q
    try:                                               # DB-first: lean columns, no re-parse
        import db as _db
        if _db.is_ready():
            _PRIOR_Q = _db.pipeline_index()
            return _PRIOR_Q
    except Exception:
        pass
    import glob as _glob
    idx, recs = {}, []
    for fp in [str(HERE / "results.jsonl")] + _glob.glob(str(HERE / "results.lane*.jsonl")):
        try:
            for line in open(fp, encoding="utf-8", errors="replace"):
                if line.strip():
                    try:
                        recs.append(json.loads(line))
                    except Exception:
                        pass
        except Exception:
            pass
    for d in sorted(recs, key=lambda d: d.get("ts") or ""):        # last (latest ts) wins
        c = str(d.get("code") or "")
        if not c:
            continue
        f = d.get("fields") or {}
        notes = (d.get("meta") or {}).get("notes") or []
        idx[c] = {"conf": _CONF_RANK.get(str(d.get("confidence")), 1),
                  "brand": str(f.get("Бранд") or "").strip(),
                  "fallback": any("agent_fallback_direct" in str(n) for n in notes),
                  "nfields": sum(1 for v in f.values() if str(v or "").strip()),
                  "v2": any(str(n) == "v2" for n in notes)}
    _PRIOR_Q = idx
    return idx


def _quality_gate(code, record):
    """Monotonic-reprocessing guard. Returns (record_or_None, note):
      * None  -> skip the write; the existing canonical is BETTER (block a downgrade),
      * record -> write it (possibly with a lost brand merged back from the prior version).
    Only fires when a prior canonical exists (re-processing); first-time products pass
    straight through. Targets the exact regression we found: a fallback-direct re-run
    that dropped a verified brand / lost fields / lowered confidence."""
    prior = _prior_quality_index().get(str(code))
    if not prior:
        return record, None
    # v2 rebuild over a v1 canonical ALWAYS writes: v1's self-reported confidence is
    # not comparable to v2's stricter scale, and blocking here would loop the product
    # forever (a blocked v2 write never enters done_codes_v2, so every lane re-runs
    # it). The gate only compares like with like (v2 rerun vs v2 canonical).
    _rec_v2 = any(str(n) == "v2" for n in
                  ((record.get("meta") or {}).get("notes") or []))
    if _rec_v2 and not prior.get("v2"):
        return record, None
    f = record.get("fields") or {}
    notes = (record.get("meta") or {}).setdefault("notes", []) if record.get("meta") else []
    if not isinstance(record.get("meta"), dict):
        record["meta"] = {"notes": notes}
    new_conf = _CONF_RANK.get(str(record.get("confidence")), 1)
    new_fallback = any("agent_fallback_direct" in str(n) for n in notes)
    new_brand = str(f.get("Бранд") or "").strip()
    new_nfields = sum(1 for v in f.values() if str(v or "").strip())
    if new_conf < prior["conf"]:
        return None, f"quality_gate_block:lower_conf({prior['conf']}->{new_conf})"
    if new_fallback and not prior["fallback"] and new_nfields < prior["nfields"]:
        return None, "quality_gate_block:fallback_over_agentic"
    if prior["brand"] and not new_brand:                           # reprocess lost the brand
        f["Бранд"] = prior["brand"]
        record["fields"] = f
        notes.append(f"quality_gate_restore_brand:{prior['brand']}")
    return record, None


_HOMO_TR = str.maketrans("aeopcxyABEKMHOPCTX", "аеорсхуАВЕКМНОРСТХ")


def agentic_guards(fields, task, notes, code):
    """Legacy validate() guardrails restored for the agentic path (they were silently
    lost in the rewrite): homoglyph repair, supplier-brand rejection, weight restore +
    plausibility, name cap, attribute-placeholder drop, synonym/related caps, and the
    duplicate-description check. Deterministic, in-place on `fields`."""
    original = task.get("product") or {}

    # Homoglyph repair: Latin lookalikes inside Cyrillic words poison site search.
    def _fix_homoglyphs(text):
        def fix_word(m):
            w = m.group(0)
            cyr = sum(1 for ch in w if "а" <= ch.lower() <= "я")
            lat = sum(1 for ch in w if ch in "aeopcxyABEKMHOPCTX")
            return w.translate(_HOMO_TR) if cyr > lat else w
        return re.sub(r"\w*[а-яА-Я]\w*", fix_word, str(text))

    for k in ("Наименование", "Описание", "Мета наименование", "Мета описание",
              "Синоними", "Атрибути"):
        v = fields.get(k)
        if v:
            fixed = _fix_homoglyphs(v)
            if fixed != v:
                fields[k] = fixed
                notes.append(f"homoglyphs_fixed:{k}")

    # Brand: never a supplier name.
    brand = str(fields.get("Бранд") or "").strip().lower()
    if brand and any(s in brand for s in SUPPLIER_NAMES):
        notes.append(f"dropped_supplier_brand:{fields['Бранд']}")
        fields["Бранд"] = None

    # Weight: never emptied; numeric and physically plausible for household goods.
    if not fields.get("Тегло (кг)") and original.get("Тегло (кг)"):
        fields["Тегло (кг)"] = original.get("Тегло (кг)")
        notes.append("restored_weight")
    w = fields.get("Тегло (кг)")
    if w is not None:
        try:
            wf = float(str(w).replace(",", "."))
            if not 0.005 <= wf <= 100:
                fields["Тегло (кг)"] = original.get("Тегло (кг)")
                notes.append(f"weight_implausible:{w}")
        except (TypeError, ValueError):
            fields["Тегло (кг)"] = original.get("Тегло (кг)")
            notes.append(f"weight_not_numeric:{w}")

    # Name: strip a leading catalog-digit prefix; cap at 80 chars on a boundary.
    name = str(fields.get("Наименование") or "")
    stripped = re.sub(r"^\s*[\d/.\-]{4,}\s+", "", name).strip()
    if stripped and stripped != name:
        fields["Наименование"] = stripped
        notes.append("stripped_catalog_prefix")
        name = stripped
    if len(name) > 80:
        cut = name[:80]
        boundary = cut.rfind(",") if "," in cut[60:] else cut.rfind(" ")
        fields["Наименование"] = (cut[:boundary] if boundary > 40 else cut).strip().rstrip(",")
        notes.append("name_trimmed")

    # Attributes: drop placeholder values the model uses to dodge a group.
    attrs = fields.get("Атрибути")
    if attrs:
        kept = []
        for part in str(attrs).split(";"):
            part = part.strip()
            if not part:
                continue
            value = part.split(":", 1)[1].strip() if ":" in part else part
            if value.lower() in {"needs_human", "unknown", "null", "none", "n/a", "?", "-", ""}:
                notes.append(f"dropped_attr:{part[:40]}")
                continue
            kept.append(part)
        fields["Атрибути"] = "; ".join(kept) if kept else None

    # Synonyms/related caps (site fields, not essays).
    syn = [t.strip() for t in str(fields.get("Синоними") or "").split(",") if t.strip()]
    if len(syn) > 15:
        notes.append(f"synonyms_capped:{len(syn)}")
        fields["Синоними"] = ", ".join(syn[:15])

    # Duplicate-description check: a description reused across DIFFERENT products is a
    # real store-quality problem (and an SEO one).
    desc_norm = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", str(fields.get("Описание") or ""))).strip().lower()
    desc_hash = hashlib.md5(desc_norm.encode()).hexdigest() if len(desc_norm) > 80 else None
    if desc_hash and DESC_HASHES_PATH.exists():
        for line in DESC_HASHES_PATH.read_text(encoding="utf-8").splitlines():
            h, _, other = line.partition(" ")
            if h == desc_hash and other.strip() != str(code):
                notes.append(f"duplicate_desc_of:{other.strip()[:20]}")
                break
    return desc_hash


def process_agentic(task, prior_failures):
    """Run the per-product enrichment agent, then wrap its output in the essential
    deterministic guardrails (Russian-fix, spellcheck, catalogue index, record)."""
    code = task["code"]
    log(f"Processing {code} (agentic, attempt {prior_failures + 1})")
    t0 = time.time()
    try:
        import telemetry as _tel
        _tel.reset()                                   # begin per-product token accounting
    except Exception:
        pass
    global _BUDGET_SPENT
    _BUDGET_SPENT = None                           # re-read budget usage per product (12 lanes drift)
    try:
        import agent_enrich
        result = agent_enrich.enrich(code)
        af = result.get("fields") or {}
        fallback_note = None
        if not af:
            # Agent couldn't finalize (loop / unparseable final). Don't LOSE the product —
            # fall back to a direct generation so it's still processed (can be re-run through
            # the full agent later). ~guarantees zero product loss.
            log(f"  {code}: agent no-final ({str(result.get('error'))[:50]}) — direct fallback")
            try:
                out, _ = generate_with_chain(build_prompt(task))
                af = extract_json(out) or {}
                fallback_note = "agent_fallback_direct"
            except Exception:
                af = {}
            if not af:
                raise ValueError(f"agent + fallback both failed: {result.get('error')}")
        # Map agent output to editable fields; fall back to the original where the
        # agent left a field empty. Empiric columns are never in EDITABLE, so the
        # driver/catalog keep them verbatim.
        fields = {}
        for col in EDITABLE:
            v = af.get(col)
            if isinstance(v, list):
                v = "; ".join(str(x) for x in v if x)
            elif isinstance(v, dict):
                v = json.dumps(v, ensure_ascii=False)
            fields[col] = v if v not in ("", None) else task["product"].get(col)
        notes = ["agentic", f"agent_steps:{result.get('steps')}"]
        if fallback_note:
            notes.append(fallback_note)
        # Deterministic Russian-ism safety net on the agent's text.
        for col in ("Наименование", "Описание", "Мета наименование", "Мета описание",
                    "Синоними", "Атрибути", "Бранд"):
            if fields.get(col):
                fx, _ = apply_ru_fix(str(fields[col]))
                fields[col] = fx
        # Категории is a FIXED 74-entry taxonomy — the driver enforces it so the agent
        # can't invent a category path (it produced 'Домашни потребности / ...' once).
        known_cats = set(known_categories())
        parts = [p.strip() for p in str(fields.get("Категории") or "").split(";") if p.strip()]
        if known_cats and parts and not all(p in known_cats for p in parts):
            fields["Категории"] = task["product"].get("Категории")
            notes.append("reverted_invalid_category")
        # Свързани is a STRUCTURAL fact, not a judgement call — the driver owns it so
        # the agent can never invent related products. Authoritative source: catalogue
        # number ±1 (build_catalog then makes it symmetric). Overrides the agent's field.
        try:
            import relate_tools
            cat_no = task["product"].get("Каталожен номер")
            relate_tools.register(code, cat_no)
            rel = relate_tools.find_related(code, cat_no)
            fields["Свързани"] = ", ".join(rel) if rel else None
        except Exception:
            fields["Свързани"] = task["product"].get("Свързани")

        # Brand capture: if the agent TOOL-verified a brand (gazetteer/web) but didn't
        # write it to the Бранд field, the driver recovers it from the tool log — a
        # verified fact must not be lost to the agent's formatting choices. Never a
        # supplier name.
        supl = [s.lower() for s in SUPPLIER_NAMES]
        if not str(fields.get("Бранд") or "").strip():
            for l in (result.get("log") or []):
                if l.get("tool") in ("verify_brand", "lookup_brand"):
                    try:
                        canon = json.loads(l.get("result") or "{}").get("canonical")
                    except Exception:
                        canon = None
                    if canon and str(canon).lower() not in supl:
                        fields["Бранд"] = canon
                        notes.append(f"brand_from_verification:{canon}")
        # Catalogue-number / prefix guard (deterministic, driver-owned). The source
        # Стока encodes 'BR-[COLLECTION-]Name (CATALOGUE_NUMBER)'; agents leak the 'BR'
        # prefix, the catalogue number, and prefix/collection tokens into the customer
        # name and Бранд. We strip ONLY what the SOURCE marks as a catalogue code (a
        # parenthetical containing a digit, matched verbatim, letter-bearing so a bare
        # size is never touched); the number itself stays in the Каталожен номер column.
        # The gazetteer is consulted first, so real brands (incl. HL = Hobby life) are
        # never dropped.
        try:
            import catalogue_guard as _cg
            _stoka = (task.get("ground_truth") or {}).get("Стока")
            _catnums = _cg.source_catnums(_stoka)
            _prefs = [p for _, p in _catnums]
            _lead = _cg.source_leading_prefix(_stoka)      # 'CN'/'CNC'/... (not a brand)
            if _lead:
                _prefs.append(_lead)
            _mcodes = _cg.source_model_codes(_stoka)
            _removed = []
            for _col in ("Наименование", "Мета наименование", "Мета описание", "Описание"):
                if fields.get(_col):
                    _clean, _rm = _cg.strip_catnums_from_name(str(fields[_col]), _catnums)
                    _clean, _rm2 = _cg.strip_model_codes(_clean, _mcodes)
                    if _lead and _col in ("Наименование", "Мета наименование"):
                        _clean, _lc = _cg.strip_leading_prefix(_clean, _lead)
                        if _lc:
                            _rm2 = _rm2 + [_lead]
                    fields[_col] = _clean
                    _removed += _rm + _rm2
            if _removed:
                notes.append("catnum_stripped:" + ",".join(dict.fromkeys(_removed)))
            _b0 = fields.get("Бранд")
            _b1, _bn = _cg.guard_brand(_b0, _prefs)
            if _b1 != _b0:
                fields["Бранд"] = _b1
                if _bn:
                    notes.append(_bn)
                # NOTE: we no longer programmatically strip a series/line token from the
                # TITLE — genuine product lines (owner: keep 'Elite Multi'-type lines) are
                # the AGENT's judgement. The guard still drops it from Бранд (a series is
                # not the manufacturer) but leaves the title to the agent.
        except Exception as _cge:
            notes.append(f"catalogue_guard_error:{str(_cge)[:60]}")
        # Deterministic SEO-length enforcement (Google truncates over-length meta):
        # title <= 60, description <= 160, trimmed at a word/sentence boundary.
        try:
            import catalogue_guard as _cgm
            _mtrim = []
            for _mk, _lim in (("Мета наименование", 60), ("Мета описание", 160)):
                if fields.get(_mk):
                    _tv, _ch = _cgm.trim_meta(str(fields[_mk]), _lim)
                    if _ch:
                        fields[_mk] = _tv
                        _mtrim.append(_mk)
            if _mtrim:
                notes.append("meta_trimmed:" + ",".join(_mtrim))
        except Exception:
            pass
        # Deterministic field tidy (zero-quota): unit normalisation (cm->см, 18 литра->
        # 18 л), line-marker brand strip (HORECANO KIDS->HORECANO), cross-family synonym
        # cleanup. Runs AFTER meta-trim so lengths only shrink. Tested: units/synonyms/
        # marker-brand are clean; name-reorder was rejected (corrupts model codes) and is
        # NOT enabled here. Empiric columns are untouched.
        try:
            import field_tidy as _ft
            fields, _tch = _ft.tidy(fields, do_reorder=False)
            if _tch:
                notes.append("field_tidy:" + ",".join(dict.fromkeys(
                    c.split(":")[0] for c in _tch)))
        except Exception as _fte:
            notes.append(f"field_tidy_error:{str(_fte)[:50]}")
        # Deterministic quality cleaners (zero-quota): romanized-synonym junk, reasoning
        # leakage, JSON-blob attrs, Марка→Бранд, empty-brand backfill, catalogue code in
        # name, meta cut mid-thought. Fabricated claims are only FLAGGED, never edited.
        try:
            import quality_clean as _qc
            fields, _qcch = _qc.clean(fields)
            if _qcch:
                notes.append("quality_clean:" + ",".join(dict.fromkeys(_qcch)))
        except Exception as _qce:
            notes.append(f"quality_clean_error:{str(_qce)[:50]}")
        # Legacy validate() guardrails (homoglyphs, supplier-brand, weight, name cap,
        # placeholder attrs, dup-description) — restored for the agentic path.
        _desc_hash = None
        try:
            _desc_hash = agentic_guards(fields, task, notes, code)
        except Exception as _age:
            notes.append(f"agentic_guards_error:{str(_age)[:50]}")
        # NAMING CONVENTION (owner spec): render Наименование from the attributes via the
        # canonical type vocabulary — every future product conforms automatically.
        try:
            import name_builder as _nbld
            _nm, _nrs = _nbld.build_name(fields, _nbld.load_vocab())
            if _nm and _nm != str(fields.get("Наименование") or "").strip():
                fields["Наименование"] = _nm
                notes.append("name_builder:enforced")
            elif _nrs:
                notes.append(f"name_builder_skip:{_nrs}")
        except Exception:
            pass
        # Re-enforce meta limits LAST: unit normalization ('40cm'->'40 см') can re-grow a
        # meta past 60/160 after the earlier trim.
        try:
            import catalogue_guard as _cgm2
            for _mk, _lim in (("Мета наименование", 60), ("Мета описание", 160)):
                if fields.get(_mk):
                    _tv, _ch = _cgm2.trim_meta(str(fields[_mk]), _lim)
                    if _ch:
                        fields[_mk] = _tv
        except Exception:
            pass
        # Final spellcheck on the customer-facing text.
        final_bad = []
        try:
            from bg_spell import unknown_words as _uw
            blob = " ".join(str(fields.get(k) or "") for k in
                            ("Наименование", "Описание", "Мета описание", "Атрибути"))
            final_bad = _uw(blob, limit=8,
                            known_text=json.dumps(task.get("ground_truth"), ensure_ascii=False))
        except Exception:
            pass
        # The direct-fallback prompt answers in ENGLISH keys — map them too, else a
        # fallback record always looked 'medium' and its issues note was lost.
        conf = str(af.get("увереност") or af.get("confidence") or "").lower()
        base_conf = {"висока": "high", "средна": "medium", "ниска": "low",
                     "high": "high", "medium": "medium", "low": "low"}.get(conf, "medium")
        tools_used = ",".join(sorted({l["tool"] for l in (result.get("log") or [])}))
        if tools_used:
            notes.append(f"tools:{tools_used}")
        if final_bad:
            notes.append("final_misspelled:" + ",".join(final_bad))
        # Confidence from OBJECTIVE evidence, not the agent's (over-conservative) self-
        # rating: a SUCCESSFUL photo check + clean, taxonomy-valid output means the
        # product was actually verified against its image -> high.
        # NOTE: the bg spellchecker false-positives massively on valid commerce/cooking
        # vocabulary (принт, интериорен, филетиране, срезове...) — it was 100% of the review
        # queue and almost all false. The RELIABLE contamination signal is Russian LETTERS
        # (ы/э/ё); RU_FIX already strips those. The phunspell bg_BG dictionary is
        # demonstrably incomplete for commerce/cooking vocabulary (куркума, гастронорм,
        # ХОРЕКА, дипове, гранола...) so a spellcheck word-COUNT floods the queue with
        # valid words. Instead the contamination signal is precise: Russian LETTERS
        # (ы/э/ё) plus curated Russian-WORD markers (посуда, загрязнения, герметичен...)
        # that survive RU_FIX. Both are genuine; phunspell stays advisory only.
        blob2 = " ".join(str(fields.get(k) or "") for k in
                         ("Наименование", "Описание", "Мета описание", "Атрибути"))
        has_russian = any(c in "ыэёЫЭЁ" for c in blob2)
        ru_words = list(dict.fromkeys(russian_survivors(blob2)))
        if ru_words:
            notes.append("russian_words:" + ",".join(ru_words)[:120])
        # '(няма снимка)' / '(грешка...)' are FAILED vision calls — only a real answer
        # counts as a photo check (was stamping photo-verified with no photo).
        vision_ok = any(l.get("tool") == "analyze_image"
                        and not str(l.get("result", "")).strip().startswith("(")
                        for l in (result.get("log") or []))
        # A category revert restores the trusted SOURCE category, which is always a
        # valid taxonomy entry (verified: reverted records are 100% valid) — that is a
        # RESOLVED correction, not a defect, so it must NOT force a human. The only
        # genuine text-contamination signals that block "clean" are Russian LETTERS and
        # surviving Russian WORDS.
        clean = not has_russian and not ru_words
        # Confidence resolution:
        #  - not clean (Russian contamination) OR agent flagged LOW -> keep for a human.
        #  - clean + vision confirmed the photo -> high.
        #  - clean + agent verified via other tools but vision COULDN'T run (broken/404
        #    image) -> the broken image is an IMAGE-pipeline issue, not a text-review one;
        #    mark high with an image_unverified note instead of forcing a human.
        if not clean or base_conf == "low":
            confidence = base_conf
        elif vision_ok:
            confidence = "high"
            if base_conf != "high":
                notes.append("confidence_upgraded:vision+clean")
        elif base_conf == "high":
            confidence = "high"                        # agent's own high, no photo check
            notes.append("image_unverified")
        else:
            # No photo check AND the agent itself said 'средна' (a KEY fact unclear) —
            # do NOT promote; this was silently shipping fallback/uncertain output as
            # high-confidence with zero review.
            confidence = "medium"
            notes.append("image_unverified")
        if fallback_note:
            confidence = "medium" if confidence == "high" else confidence
            # no-tools direct fallback invents from the prompt alone — always review it
        needs_human = confidence != "high" or has_russian or bool(ru_words)
        # Weak-match guard (restored from the legacy path; lost in the agentic rewrite):
        # a product matched to supplier data only by NAME/MODEL similarity has polluted
        # multiple codes before (2026-07-09) — always give it a human look.
        _mk = str((task.get("ground_truth") or {}).get("Match kind") or "").lower()
        if _mk.startswith(("name", "model")):
            needs_human = True
            notes.append(f"weak_match:{_mk[:20]}")
        # Deterministic quality triage (the model's self-rating is 'high' ~99.7% of the
        # time, so it can't route review). Real risk flags — fabricated authority claims,
        # recoverable-but-empty brand, catalogue code in name, JSON-blob attrs, romanized
        # synonyms — force review and are stored so the console can show WHY.
        _qflags = []
        try:
            import quality_flags as _qf
            _qneed, _qflags = _qf.needs_human({"fields": fields})
            if _qneed:
                needs_human = True
            if any(fl[0] == "fabrication" for fl in _qflags):
                notes.append("fabrication_flag")
        except Exception:
            pass
        # Stamp the category's live filter-schema fingerprint so the reconciliation pass
        # can later tell which products were enriched against an OLDER schema (and may be
        # missing filter groups the reviewer has since added). Zero-quota, deterministic.
        try:
            import filter_schema_store as _fss2
            _schema_fp = _fss2.category_fingerprint(fields.get("Категории"))
        except Exception:
            _schema_fp = None
        try:
            import telemetry as _tel
            _usage = _tel.summary()
        except Exception:
            _usage = None
        record = {
            "code": code, "ts": datetime.now().isoformat(timespec="seconds"),
            "fields": fields, "Проблеми": af.get("промени"), "Снимка проблеми": None,
            "confidence": confidence, "needs_human": needs_human,
            "review": {"verdict": None, "issues": None},
            "vision_verify": None, "vision_correction": None, "lesson": None,
            "meta": {"duration_s": round(time.time() - t0, 1), "notes": notes,
                     "model_pair": "agentic", "agent_log": result.get("log"),
                     "schema_fp": _schema_fp,
                     "usage": _usage,
                     "primary_model": (_usage or {}).get("primary_model"),
                     "quality_flags": _qflags},
        }
        # Monotonic-reprocessing guard: never let a worse re-run overwrite a better
        # canonical (blocks a downgrade; merges a lost brand back). No-op for first-time
        # products.
        try:
            record, _qg = _quality_gate(code, record)
            if record is None:
                log(f"SKIP {code}: {_qg} — kept better existing version")
                mark_done(code)
                return "done"
        except Exception as _qge:
            notes.append(f"quality_gate_error:{str(_qge)[:50]}")
        # DB is the AUTHORITATIVE store (owner directive): write it FIRST and LOUDLY —
        # a DB failure is flagged in the record's notes, never swallowed. The JSONL
        # append is the durable export / safety net (the DB is rebuildable from it).
        try:
            import db as _db
            _db.record_version(record)
        except Exception as _dbe:
            notes.append(f"db_write_failed:{str(_dbe)[:60]}")
            log(f"  WARN {code}: DB write failed ({str(_dbe)[:80]}) — JSONL still written")
        with open(RESULTS_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        if _desc_hash:
            with open(DESC_HASHES_PATH, "a", encoding="utf-8") as f:
                f.write(f"{_desc_hash} {code}\n")
        mark_done(code)                                # keep the cached done-set current
        log(f"OK {code} in {record['meta']['duration_s']}s (agentic, "
            f"conf={confidence}, needs_human={needs_human}, tools={tools_used})")
        return "done"
    except Exception as e:
        with open(FAILURES_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps({"code": code, "ts": datetime.now().isoformat(timespec="seconds"),
                                "error": f"agentic: {str(e)[:400]}"}, ensure_ascii=False) + "\n")
        log(f"FAIL {code} (agentic): {str(e)[:200]}")
        return "failed"


def process_next(target_code=None):
    """Returns 'done', 'empty', or 'failed'."""
    # Reversible pause switch: while (HERE/'PAUSE') exists, lanes do nothing. Used
    # during the Alibaba-arrearage outage to avoid burning the last free providers
    # and producing vision-less records. Delete the file to resume.
    if (HERE / "PAUSE").exists():
        log("PAUSED (PAUSE sentinel present) — skipping this batch.")
        return "empty"
    task, prior_failures = next_task(target_code)
    if task is None:
        log("Queue empty — nothing pending.")
        return "empty"
    if (HERE / "V2_MODE").exists():
        import pipeline_v2
        return pipeline_v2.process(task, prior_failures)
    if AGENTIC:
        return process_agentic(task, prior_failures)
    code = task["code"]
    log(f"Processing {code} (attempt {prior_failures + 1})")
    t0 = time.time()
    try:
        prompt = build_prompt(task)
        rc = out = err = None
        worker_used = None
        exhausted = _load_exhausted()
        chain = [a for a in WORKER_CHAIN if a[a.index("-m") + 1] not in exhausted] or WORKER_CHAIN
        for i, worker_args in enumerate(chain):
            model = worker_args[worker_args.index("-m") + 1]
            try:
                rc, out, err = run_worker_direct(prompt, model_args=worker_args)
                if not extract_json(out):
                    raise ValueError("worker returned no JSON")
                worker_used = model
                if i > 0:
                    log(f"  worker -> {model} for {code}")
                break
            except Exception as e:
                if _is_quota_error(e) and model not in exhausted:
                    _mark_exhausted(model)
                    exhausted.add(model)
                    log(f"  {model} free quota EXHAUSTED — marked, will skip henceforth")
                if i == len(chain) - 1:
                    raise
                log(f"  worker {model} failed for {code} ({str(e)[:70]}) — failover")
        parsed = extract_json(out)
        if parsed is None:
            raise ValueError(f"no JSON in agent output (rc={rc}); tail: {out[-400:]!r}")
        fields, notes = validate(task, parsed)
        # Vision honesty: if the product has an image but the worker could not
        # (or did not) inspect it, the record goes to the human queue.
        vision_status = str(parsed.get("визуална проверка") or "").strip().lower()
        vision_unverified = bool(task["product"].get("Снимки")) and vision_status not in ("ок", "ok")
        if vision_unverified:
            notes.append(f"vision_unverified:{vision_status or 'missing'}")
        # Fuzzy-matched ground truth may describe a different product — those
        # records always get a human look (2026-07-09: one scraped listing was
        # matched to four till codes and polluted them all).
        match_kind = str(task["ground_truth"].get("Match kind") or "")
        weak_match = match_kind.startswith(("name", "model"))
        if weak_match:
            notes.append(f"weak_match:{match_kind}")

        review_issues = None
        review_verdict = None
        review_forced = False
        # The reviewer receives the spellcheck findings as a mandatory fix
        # list — misspellings become corrections, not just flags.
        worker_bad_words = next((n.split(":", 1)[1].split(",")
                                 for n in notes if n.startswith("misspelled:")), [])
        if REVIEW_ENABLED:
            try:
                rc2, out2, _ = run_reviewer_direct(
                    build_review_prompt(task, fields,
                                        {"Проблеми": parsed.get("Проблеми")},
                                        bad_words=worker_bad_words))
                review = extract_json(out2)
                if review is None:
                    raise ValueError(f"no JSON from reviewer (rc={rc2})")
                review_verdict = review.get("verdict")
                review_issues = review.get("issues")
                review_forced = bool(review.get("needs_human", False))
                corrected = review.get("corrected")
                if review_verdict == "revise" and isinstance(corrected, dict):
                    # Carry the worker's vision status into re-validation —
                    # otherwise the fabrication firewall wrongly drops
                    # attributes the worker DID verify against the image.
                    # Force-set: reviewers echo the schema with their own null
                    # here, and setdefault would keep that null.
                    corrected["визуална проверка"] = parsed.get("визуална проверка")
                    # The reviewer never saw the image, so it may only touch
                    # text-quality fields. Fact fields (category, brand,
                    # related, and the product-type head of the name) stay
                    # with the vision-informed worker; disagreement there is
                    # escalated to a human instead of applied.
                    MAY_CHANGE = {"Описание", "Мета наименование", "Мета описание",
                                  "Синоними", "Атрибути", "Наименование", "Тегло (кг)"}
                    merged = dict(fields)
                    conflicts = []
                    for k in ("Категории", "Бранд", "Свързани"):
                        if k in corrected and str(corrected[k] or "") != str(fields.get(k) or ""):
                            conflicts.append(k)
                    new_name = str(corrected.get("Наименование") or "").strip()
                    old_name = str(fields.get("Наименование") or "").strip()
                    if new_name and old_name:
                        # Type conflict only when the name HEADS share no token
                        # at all — reordering ("Закачалка стенна" vs "Стенна
                        # закачалка") is a wording tweak, not an identity change.
                        head_new = {w.lower() for w in new_name.split()[:3]}
                        head_old = {w.lower() for w in old_name.split()[:3]}
                        if not head_new & head_old:
                            conflicts.append("Наименование(тип)")
                            corrected.pop("Наименование", None)
                    for k in MAY_CHANGE:
                        if k in corrected and corrected[k] not in (None, ""):
                            merged[k] = corrected[k]
                    merged["Код"] = code
                    # The fabrication firewall inside validate() reads this key
                    # from ITS argument — merged, not corrected. Without it the
                    # worker's vision-verified attributes get wrongly stripped.
                    merged["визуална проверка"] = parsed.get("визуална проверка")
                    try:
                        fields, notes2 = validate(task, merged)
                        notes.extend("review_" + n for n in notes2)
                        notes.append("review_applied_partial" if conflicts
                                     else "review_applied")
                    except ValueError as ve:
                        notes.append(f"review_correction_rejected:{str(ve)[:80]}")
                        review_forced = True
                    if conflicts:
                        notes.append("review_fact_conflict:" + ",".join(conflicts))
                        review_forced = True
                elif review_verdict == "revise":
                    # Reviewer found problems but returned no usable correction.
                    review_forced = True
            except Exception as re_err:
                # Reviewer RELIABILITY failure (no JSON / provider rate-limited). The
                # worker (clean Qwen), vision verifier and spellcheck already validated
                # this product, so a missing SECONDARY review does not force a human —
                # note it and move on. (Only reviewer content-verdicts of concern force.)
                notes.append(f"review_unavailable:{str(re_err)[:60]}")

        # Final-state spellcheck: what matters is the text AFTER the reviewer's
        # corrections. Stage-level misspelled notes become informational; only
        # words surviving in the final fields force a human look.
        def _spellcheck():
            try:
                from bg_spell import unknown_words as _uw
                blob = " ".join(str(fields.get(k) or "") for k in
                                ("Наименование", "Описание", "Мета наименование",
                                 "Мета описание", "Атрибути"))
                known = json.dumps(task.get("ground_truth"), ensure_ascii=False)
                return _uw(blob, limit=8, known_text=known)
            except Exception:
                return worker_bad_words  # spellcheck down: stay conservative

        # Deterministic de-russification on the FINAL fields (post-review). The
        # GLM reviewer can reintroduce Russian-isms the worker's RU-fix already
        # cleaned, so re-apply the rule-based map here — BEFORE spellcheck — so
        # known Russian words never reach the store or the human queue regardless
        # of which stage produced them.
        for _k in ("Наименование", "Описание", "Мета наименование",
                   "Мета описание", "Синоними", "Атрибути", "Категории"):
            if fields.get(_k):
                _fixed, _ch = apply_ru_fix(str(fields[_k]))
                if _ch:
                    fields[_k] = _fixed
        final_bad = _spellcheck()
        # Targeted language polish: if garbled/foreign words survived, ask GLM to
        # rewrite ONLY the wording (facts frozen) fixing exactly those words, then
        # re-check. Converts most language flags to clean instead of human work.
        if final_bad and POLISH_ENABLED:
            try:
                polished = run_polish(fields, final_bad, POLISH_MODEL_ARGS)
                if polished:
                    for k in ("Наименование", "Описание", "Мета наименование",
                              "Мета описание", "Синоними", "Атрибути"):
                        if polished.get(k):
                            fixed, _ = apply_ru_fix(str(polished[k]))
                            fields[k] = fixed
                    notes.append("language_polished")
                    final_bad = _spellcheck()
            except Exception as pe:
                notes.append(f"polish_failed:{str(pe)[:60]}")
        # Threshold: the bg dictionary misses so much valid commerce vocabulary
        # that a SINGLE unknown word is ~80% a false positive, while real model
        # garbage arrives in clusters. One unknown word in the body is
        # informational; two-plus, or any in the customer-visible name, forces.
        name_l = str(fields.get("Наименование") or "").lower()
        misspell_forces = len(final_bad) >= 2 or any(
            w.lower() in name_l for w in final_bad)
        tag = "final_misspelled" if misspell_forces else "final_misspelled_minor"
        notes = [n for n in notes
                 if not n.startswith(("misspelled:", "review_misspelled:"))] + \
                ([f"{tag}:{','.join(final_bad)}"] if final_bad else [])

        # Duplicate-description check on the FINAL text.
        import hashlib
        desc_norm = re.sub(r"\s+", " ", str(fields.get("Описание") or "")).strip().lower()
        desc_hash = hashlib.md5(desc_norm.encode()).hexdigest() if len(desc_norm) > 80 else None
        if desc_hash and DESC_HASHES_PATH.exists():
            for line in DESC_HASHES_PATH.read_text(encoding="utf-8").splitlines():
                h, _, other = line.partition(" ")
                if h == desc_hash and other != code:
                    notes.append(f"duplicate_desc_of:{other}")
                    break

        # --- Independent vision verification (3rd agent) --------------------
        # Catches facts a photo can judge but the text passes miss (a round
        # name on a rectangular pan). Runs on the FINAL fields. A confirmed
        # mismatch is the main thing that sends an otherwise-clean product to
        # a human, with the correct shape/type attached.
        vision_mismatch = False
        vision_result = None
        vision_correction = None
        image_url = (task["product"].get("Снимки") or "").split(";")[0].strip()
        if VISION_VERIFY_ENABLED and image_url:
            vision_result = verify_against_image(image_url, fields)
            if vision_result and vision_result.get("ok") is False:
                d = vision_result.get("detail", {})
                conf = str(d.get("сигурност") or "").lower()
                # Vision-guided correction: rewrite the affected fields to match the
                # photo. High confidence -> apply automatically (stays out of the human
                # queue). Otherwise -> attach a proposed edit for 1-click approval.
                corrected = vision_guided_correct(fields, d)
                changes = {k: corrected.get(k) for k in
                           ("Наименование", "Атрибути", "Описание")
                           if corrected and corrected.get(k)} if corrected else {}
                if changes and conf.startswith("висок"):
                    for k, val in changes.items():
                        fx, _ = apply_ru_fix(str(val))
                        fields[k] = fx
                    notes.append("vision_autocorrected:" + ",".join(vision_result["mismatch"]))
                    vision_correction = {"applied": True, "confidence": conf, "changes": changes}
                    # Vision confidently resolved the fact conflict — clear the worker's
                    # now-stale self-flag so the product isn't sent to a human for the very
                    # thing that was just auto-fixed. Independent forcing conditions
                    # (weak_match, duplicate, misspelled) still apply below.
                    parsed["needs_human"] = False
                else:
                    vision_mismatch = True  # force human look (1-click approve if proposal present)
                    notes.append("vision_mismatch:" + ",".join(vision_result["mismatch"]))
                    if changes:
                        vision_correction = {"applied": False, "confidence": conf,
                                             "proposed": changes, "note": d.get("забележка")}
                if d.get("забележка"):
                    prob = parsed.get("Проблеми") or ""
                    parsed["Проблеми"] = (prob + " | " if prob else "") + \
                        f"визуален контрол: {d['забележка']}"
            elif vision_result and vision_result.get("ok") is None:
                notes.append(f"vision_verify_skipped:{vision_result.get('error', '?')}")

            # SMART brand pipeline (see enrichment_skill.md): vision reads a brand off
            # the photo -> resolve it against the shared gazetteer (spelling-correct from
            # real supplier brands) -> verify unknowns with a model -> grow the gazetteer.
            # Only a KNOWN/VERIFIED brand is ever written, and only into an empty field.
            det = (vision_result or {}).get("detail") or {}
            vbrand = str(det.get("видим_бранд") or "").strip()
            supl = [s.lower() for s in SUPPLIER_NAMES]
            if vbrand and vbrand.lower() not in ("null", "none", "-", "n/a") and vbrand.lower() not in supl:
                cur_brand = str(fields.get("Бранд") or "").strip()
                try:
                    import brand_tools
                    canon, bnote = brand_tools.resolve(
                        vbrand, lambda p: generate_with_chain(p)[0],
                        context=str(fields.get("Наименование") or ""))
                except Exception as be:
                    canon, bnote = None, f"brand_tool_error:{str(be)[:40]}"
                if bnote:
                    notes.append(bnote)
                if canon and canon.lower() not in supl:
                    if not cur_brand:
                        fields["Бранд"] = canon
                    elif cur_brand.lower() != canon.lower():
                        notes.append(f"brand_image_differs:{cur_brand}->{canon}")

        # SMART relatedness (see enrichment_skill.md): register this product's catalogue
        # number in the shared index and link products whose catalogue number sits ±1 in
        # the same family — almost always variants. Merges into the worker's Свързани.
        try:
            import relate_tools
            cat_no = task["product"].get("Каталожен номер")
            relate_tools.register(code, cat_no)
            rel = relate_tools.find_related(code, cat_no)
            if rel:
                existing = [c.strip() for c in str(fields.get("Свързани") or "").split(",") if c.strip()]
                merged = existing + [c for c in rel if c not in existing]
                fields["Свързани"] = ", ".join(merged)
                notes.append(f"related_by_catnum:{','.join(rel[:6])}")
        except Exception as rce:
            notes.append(f"relate_error:{str(rce)[:40]}")

        # Human-queue decision, computed ONCE on the final state. Kept minimal
        # (owner wants <=5% review): only genuine UNRESOLVED problems escalate.
        # Resolved states — reverted/restored values, dropped unconfirmed
        # attributes, estimated weights, single stray words, auto-fixed
        # Russian-isms — are complete and stay out of the human queue.
        worker_saw = str(parsed.get("визуална проверка") or "").strip().lower() in ("ок", "ok")
        verifier_saw = bool(vision_result) and vision_result.get("ok") is not None
        # A product WITH a photo that neither the worker nor the verifier could
        # actually see has no visual confirmation — the one vision case, besides
        # a confirmed mismatch, that still needs a human.
        no_visual_confirmation = bool(image_url) and not worker_saw and not verifier_saw
        if no_visual_confirmation:
            # Vision could not RUN (dead/404 image URL, or a vision-provider error) —
            # an IMAGE problem, not a text-quality one. The reviewer already checked the
            # text against ground truth. So note it for the image pipeline / a separate
            # queue but do NOT force text-review (this alone was ~1/3 of the human queue).
            # A real vision MISMATCH still forces below — that safeguard is untouched.
            broken = any(("image_load" in n or "404" in n) for n in notes)
            notes.append("image_broken" if broken else "vision_pending")

        FORCING = ("duplicate_desc_of", "final_misspelled:", "vision_mismatch")
        needs_human = (bool(parsed.get("needs_human", False))
                       or weak_match
                       or vision_mismatch
                       or review_forced
                       or any(n[7:].startswith(FORCING) if n.startswith("review_")
                              else n.startswith(FORCING) for n in notes))

        lesson = parsed.get("lesson")
        lesson_added = maybe_add_lesson(lesson)
        record = {
            "code": code,
            "ts": datetime.now().isoformat(timespec="seconds"),
            "fields": fields,
            "Проблеми": parsed.get("Проблеми"),
            "Снимка проблеми": parsed.get("Снимка проблеми"),
            "confidence": parsed.get("confidence"),
            "needs_human": needs_human,
            "review": {"verdict": review_verdict, "issues": review_issues},
            "vision_verify": vision_result,
            "vision_correction": vision_correction,
            "lesson": lesson if lesson_added else None,
            "meta": {"duration_s": round(time.time() - t0, 1), "notes": notes,
                     "model_pair": worker_used},
        }
        with open(RESULTS_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        if desc_hash:
            with open(DESC_HASHES_PATH, "a", encoding="utf-8") as f:
                f.write(f"{desc_hash} {code}\n")
        log(f"OK {code} in {record['meta']['duration_s']}s"
            f" (confidence={record['confidence']}, needs_human={record['needs_human']})")
        return "done"
    except subprocess.TimeoutExpired:
        reason = f"agent timeout after {AGENT_TIMEOUT_S}s"
        with open(FAILURES_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps({"code": code, "ts": datetime.now().isoformat(timespec="seconds"),
                                "error": reason}, ensure_ascii=False) + "\n")
        log(f"FAIL {code}: {reason}")
        return "failed"
    except Exception as e:
        with open(FAILURES_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps({"code": code, "ts": datetime.now().isoformat(timespec="seconds"),
                                "error": str(e)[:500]}, ensure_ascii=False) + "\n")
        log(f"FAIL {code}: {str(e)[:200]}")
        return "failed"


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    status = process_next(target)
    sys.exit({"done": 0, "empty": 2, "failed": 1}[status])
