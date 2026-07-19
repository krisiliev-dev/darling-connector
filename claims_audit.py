# -*- coding: utf-8 -*-
"""CLAIMS AUDIT (owner 2026-07-18): mechanical hallucination check on generated texts.

Every hard claim in Описание/Мета описание — numbers, material words, colour words —
must be traceable to the VALIDATED record (Наименование, Атрибути, Тегло). Anything
untraceable is a violation. Violations are NOT auto-verdicts: a reviewer agent takes
a quick look (owner: a glass product may legitimately mention a metal ring as detail)
and only a confirmed fabrication flags the product / gets a corrected description.

  python claims_audit.py --sweep [N]   # audit existing v2 records, report flag rate
"""
import json
import re
import sys

_MATERIALS = {"дърв": "дърво", "стъкл": "стъкло", "метал": "метал", "инокс": "инокс",
              "керамич": "керамика", "порцелан": "порцелан", "пластмас": "пластмаса",
              "бамбук": "бамбук", "силикон": "силикон", "стоман": "стомана",
              "алумини": "алуминий", "чугун": "чугун", "тефлон": "тефлон",
              "гранит": "гранит", "мрамор": "мрамор", "текстил": "текстил",
              "памуч": "памук", "памук": "памук", "ленен": "лен", "велур": "велур",
              "кожен": "кожа", "кадифе": "кадифе", "ратан": "ратан", "юта": "юта",
              "акрил": "акрил", "меламин": "меламин", "полиестер": "полиестер",
              "полипропилен": "полипропилен", "неръждаем": "инокс", "месинг": "месинг"}
_COLORS = {"бял": "бял", "бяла": "бял", "бяло": "бял", "черен": "черен", "черн": "черен",
           "сив": "сив", "червен": "червен", "син": "син", "синя": "син", "синьо": "син",
           "зелен": "зелен", "жълт": "жълт", "розов": "розов", "лилав": "лилав",
           "кафяв": "кафяв", "бежов": "бежов", "оранжев": "оранжев",
           "прозрачн": "прозрачен", "сребрист": "сребрист", "златист": "златист",
           "тюркоазен": "тюркоазен", "бордо": "бордо", "антрацит": "антрацит"}

_TAG = re.compile(r"<[^>]+>")
_NUM = re.compile(r"\d+(?:[.,]\d+)?")


def _plain(markup):
    import html as _html
    return _TAG.sub(" ", _html.unescape(str(markup or "")))


def _nums(text):
    out = set()
    for n in _NUM.findall(str(text or "")):
        v = n.replace(",", ".")
        try:
            out.add(("%g" % float(v)))
        except ValueError:
            pass
    return out


def _vocab_hits(text, vocab):
    t = str(text or "").lower()
    hits = set()
    for w in re.findall(r"[а-я]{3,}", t):
        for stem, canon in vocab.items():
            if w.startswith(stem):
                hits.add(canon)
                break
    return hits


def _record_text(fields):
    return " ".join(str(fields.get(k) or "") for k in
                    ("Наименование", "Атрибути", "Тегло (кг)", "Мярка"))


def audit(fields, extra_ok=""):
    """-> list of 'kind:value' violations found in the generated texts. extra_ok is
    additional trusted source text (the supplier description — TEXT_PROMPT explicitly
    allows drawing on it), so its facts don't count as fabrications."""
    gen = " ".join(_plain(fields.get(k)) for k in ("Описание", "Мета описание"))
    rec = _record_text(fields) + " " + _plain(extra_ok)
    viols = []
    extra_nums = _nums(gen) - _nums(rec)
    # a bare year/percent is still a claim; tolerate ONLY tiny list-counts 1-3 which
    # are usually phrasing ("2 в 1" etc. go to the reviewer via materials anyway)
    viols += [f"число:{n}" for n in sorted(extra_nums) if n not in ("1", "2", "3")]
    viols += [f"материал:{m}" for m in
              sorted(_vocab_hits(gen, _MATERIALS) - _vocab_hits(rec, _MATERIALS))]
    viols += [f"цвят:{c}" for c in
              sorted(_vocab_hits(gen, _COLORS) - _vocab_hits(rec, _COLORS))]
    return viols


REVIEW_PROMPT = """Механична проверка откри в генерираното описание на продукт твърдения,
които ЛИПСВАТ в потвърдения запис. Прецени бързо кое е реално измислен факт и кое е
безобиден израз (напр. „метален пръстен“ като детайл на стъклен продукт, число в
устойчиво словосъчетание).

ЗАПИС (единствената истина):
  Име: {name}
  Атрибути: {attrs}
  Тегло: {weight}
Описание от доставчика (контекст, НЕ е истина): {scrape}

ГЕНЕРИРАНО ОПИСАНИЕ: {desc}
МЕТА ОПИСАНИЕ: {meta}

Съмнителни твърдения: {viols}

Върни САМО валиден JSON:
{{"реален_проблем": true|false,
 "обяснение": "<едно изречение>",
 "коригирано_описание": "<същото HTML описание БЕЗ измислените факти>" или null}}
(коригирано_описание само при реален_проблем=true и само ако можеш да махнеш факта
без да съсипеш текста; иначе null.)"""


def review(fields, viols, scrape_desc=""):
    """Reviewer-agent quick look over mechanical violations. Returns the parsed JSON
    verdict dict (empty dict on failure — caller falls back to flagging)."""
    import run_one as ro
    try:
        _, out, _ = ro.run_reviewer_direct(REVIEW_PROMPT.format(
            name=fields.get("Наименование"), attrs=fields.get("Атрибути"),
            weight=fields.get("Тегло (кг)") or "—",
            scrape=str(scrape_desc or "—")[:400],
            desc=str(fields.get("Описание") or "")[:1200],
            meta=str(fields.get("Мета описание") or ""),
            viols=", ".join(viols[:8])))
        return ro.extract_json(out) or {}
    except Exception:
        return {}


def _sweep(limit=200):
    import db
    con = db.connect()
    rows = con.execute("SELECT code, record_json FROM products "
                       "WHERE record_json IS NOT NULL").fetchall()
    con.close()
    n = flagged = 0
    samples = []
    for code, rj in rows:
        rec = json.loads(rj)
        if "v2" not in [str(x) for x in ((rec.get("meta") or {}).get("notes") or [])]:
            continue
        n += 1
        if n > limit:
            n -= 1
            break
        v = audit(rec.get("fields") or {})
        if v:
            flagged += 1
            if len(samples) < 12:
                samples.append((str(code), v[:5]))
    print(f"{n} v2 records audited | {flagged} with violations "
          f"({100*flagged/max(n,1):.0f}%)")
    for c, v in samples:
        print(f"  {c}: {v}")


if __name__ == "__main__":
    lim = next((int(a) for a in sys.argv[1:] if a.isdigit()), 200)
    _sweep(lim)
