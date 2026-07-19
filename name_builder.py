# -*- coding: utf-8 -*-
"""NAME BUILDER — renders every product's Наименование from its structured attributes,
so the whole catalog follows ONE convention (owner spec, 2026-07-17):

    Бранд + Материал(прилагателно) + Форма(прилагателно) + ТИП(каноничен) + Вариант + Размер
    e.g.  "Alkan Züccaciye Акрилен правоъгълен капак 34,5×54,5 см"

Grammar: adjectives agree with the canonical noun's GENDER (акрилен капак / акрилна купа /
акрилно кошче) via the vocab's adjective tables; materials without an adjective form render
as "от <материал>" after the noun. Canonical types come from name_vocab.json (LLM-swept,
synonym-merged: дозатор/пурер/диспенсър -> Дозатор).

Apply policy:
  * clean construction (type mapped, no name collision) -> AUTO-APPLY as a new version
    (stage name_builder; visible as a diff on the review cards; append-only + DB);
  * unresolved name collision -> 1-click PROPOSAL in review_fixes.jsonl; unmapped
    types are only counted in the run stats (nothing useful to propose);
  * products the OWNER already edited (human_edit) are never touched.

  python name_builder.py            # dry-run stats + samples
  python name_builder.py --apply
"""
import json, re, sys, collections
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
VOCAB = HERE / "name_vocab.json"
OUT = HERE / "results.lanez_names.jsonl"
_G = {"м": 0, "ж": 1, "ср": 2}

_SIZE_RX = re.compile(
    r"(?:Ø|ø|⌀)?\s*\d+(?:[.,]\d+)?(?:\s*[x×х]\s*\d+(?:[.,]\d+)?)*\s*(?:см|мм|cm|mm|л|мл|l|ml|бр)?\.?",
    re.IGNORECASE)


def load_vocab():
    return json.loads(VOCAB.read_text(encoding="utf-8"))


def _attrs(fields):
    d = {}
    for part in str(fields.get("Атрибути") or "").split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            d.setdefault(k.strip().lower(), v.strip())
    return d


def _size_from(fields, attrs):
    for k in ("размер", "размери", "габарити (см)", "обем", "вместимост", "диаметър"):
        v = attrs.get(k)
        if v:
            m = _SIZE_RX.search(v)
            if m and any(ch.isdigit() for ch in m.group(0)):
                return m.group(0).strip()
    # fall back to the current name (sizes usually live there) — scan ALL numeric runs
    # and prefer real dimensions (with × or a unit) over lone counts like "на 3 нива"
    best, best_score = "", -1
    for m in _SIZE_RX.finditer(str(fields.get("Наименование") or "")):
        cand = m.group(0).strip()
        if not any(ch.isdigit() for ch in cand):
            continue
        score = (2 if re.search(r"[×xх]", cand, re.IGNORECASE) else 0) + \
                (1 if re.search(r"(см|мм|cm|mm|л|мл|l|ml)\.?$", cand, re.IGNORECASE) else 0)
        if score == 0 and len(re.sub(r"[^0-9]", "", cand)) < 2:
            continue                                     # lone small int (e.g. '4' parts)
        if score > best_score:
            best, best_score = cand, score
    return best


def _norm_size(s):
    if not s:
        return ""
    s = s.replace("x", "×").replace("х", "×").replace("cm", "см").replace("mm", "мм")
    s = re.sub(r"(\d)\s*ml\b", r"\1 мл", s, flags=re.IGNORECASE)
    s = re.sub(r"(\d)\s*l\b", r"\1 л", s, flags=re.IGNORECASE)
    s = re.sub(r"(\d)\s*kg\b", r"\1 кг", s, flags=re.IGNORECASE)
    s = re.sub(r"(\d)\s*gr?\b", r"\1 г", s, flags=re.IGNORECASE)
    s = re.sub(r"(\d)\.(\d)", r"\1,\2", s)              # BG decimal comma
    s = re.sub(r"\s*×\s*", "×", s).strip(" .")
    if re.search(r"\d$", s) and "×" in s:               # dims without unit -> см
        s += " см"
    elif re.search(r"\d(см|мм|л|мл)$", s.replace(" ", "")):
        s = re.sub(r"(\d)\s*(см|мм|л|мл)$", r"\1 \2", s)
    return s


RULES = HERE / "name_rules.json"
_DEFAULT_TEMPLATE = ["Бранд", "Материал:adj", "Форма:adj", "Тип", "Вариант", "Размер"]


def load_rules():
    """Owner-editable rendering rules (see name_rules.json):
      default   — token order used for every type without its own recipe
      types     — {"Лампа": [tokens...]} per-CANON-type recipes
      overrides — [{"when": {attr: value, ...}, "template": [...] | "size_prefix": "Ø",
                    "enabled": true, "id": "..."}] matched on the product's attributes
                   (Тип compares against the CANON type); first enabled match wins.
    Tokens: Бранд / Тип / Вариант / Размер / Цвят / <Attr> (verbatim value) /
            Материал:adj / Форма:adj (gender-agreed adjective) / lit:<text>.
    Names are DERIVED: change a rule, run `python name_builder.py --apply`, and every
    non-human-pinned product re-renders. Remove a seasonal override -> re-render reverts."""
    try:
        return json.loads(RULES.read_text(encoding="utf-8"))
    except Exception:
        return {"default": list(_DEFAULT_TEMPLATE), "types": {}, "overrides": []}


def _match(when, attrs, canon):
    for k, v in (when or {}).items():
        have = canon if k.strip().lower() == "тип" else attrs.get(k.strip().lower(), "")
        if str(have).strip().lower() != str(v).strip().lower():
            return False
    return bool(when)


def build_name(fields, vocab, rules=None):
    """Returns (name or None, reason). Renders the template resolved from the rules:
    conditional override > per-type recipe > default. Reason set when not clean."""
    attrs = _attrs(fields)
    raw_type = attrs.get("тип", "")
    hit = vocab["types"].get(raw_type.lower()) if raw_type else None
    if not hit:
        # fallback: head noun of the current name
        for w in re.findall(r"[А-Яа-я]{3,}", str(fields.get("Наименование") or "")):
            hit = vocab["types"].get(w.lower())
            if hit:
                break
    if not hit:
        return None, "unmapped_type"
    canon, gender = hit[0], _G.get(hit[1], 0)

    if rules is None:
        rules = load_rules()
    template = (rules.get("types") or {}).get(canon) or rules.get("default") or list(_DEFAULT_TEMPLATE)
    size_prefix = ""
    for ov in (rules.get("overrides") or []):
        if ov.get("enabled", True) and _match(ov.get("when"), attrs, canon):
            template = ov.get("template") or template
            size_prefix = ov.get("size_prefix") or size_prefix
            break

    tail = []                                           # "от <материал>" style suffixes
    def _token(tok):
        t = str(tok)
        if t.startswith("lit:"):
            return t[4:]
        key = t.split(":")[0].strip()
        kl = key.lower()
        if kl == "бранд":
            return str(fields.get("Бранд") or "").strip()
        if kl == "тип":
            return canon.lower()                        # sentence-cased at the end
        if kl == "размер":
            sz = _norm_size(_size_from(fields, attrs))
            if sz and size_prefix and "×" not in sz and not sz.startswith(size_prefix):
                sz = f"{size_prefix}{sz}"
            return sz
        if kl == "материал" and t.endswith(":adj"):
            mat = attrs.get("материал", "")
            if not mat:
                return ""
            mk = mat.lower().split("/")[0].split(";")[0].strip()
            row = vocab["materials"].get(mk) or vocab["materials"].get(mk.split()[0] if mk else "")
            if row:
                return row[gender]
            tail.append(f"от {mk}")
            return ""
        if kl == "форма" and t.endswith(":adj"):
            row = vocab["shapes"].get(str(attrs.get("форма", "")).lower().strip())
            return row[gender] if row else ""
        return str(attrs.get(kl, "")).strip()           # any attribute, verbatim (Цвят, Вариант…)

    rendered = [x for x in (_token(t) for t in template) if x]
    # "от <материал>" tails read best directly after the type noun, not at the very end
    if tail:
        try:
            at = rendered.index(canon.lower()) + 1
        except ValueError:
            at = len(rendered)
        rendered[at:at] = tail
        tail = []
    parts = rendered
    name = re.sub(r"\s{2,}", " ", " ".join(parts)).strip()
    if not name:
        return None, "empty_render"
    # capitalize the first letter after the brand (or the very first if no brand leads)
    brand = str(fields.get("Бранд") or "").strip()
    if brand and name.startswith(brand + " ") and len(name) > len(brand) + 1:
        i = len(brand) + 1
        name = name[:i] + name[i].upper() + name[i + 1:]
    else:
        name = name[:1].upper() + name[1:]
    return name, None


def plan():
    import db
    vocab = load_vocab()
    canon = db.canonical_records()
    auto, proposals, skipped = {}, {}, collections.Counter()
    built_names = collections.Counter()
    rows = []
    for code, rec in canon.items():
        f = rec.get("fields") or {}
        notes = [str(n) for n in ((rec.get("meta") or {}).get("notes") or [])]
        if any(n.startswith("human_edit") for n in notes):
            skipped["human_edited"] += 1
            continue
        name, reason = build_name(f, vocab)
        if not name:
            skipped[reason] += 1
            proposals[code] = None                      # flagged, no construction
            continue
        if name == str(f.get("Наименование") or "").strip():
            skipped["already_conformant"] += 1
            continue
        built_names[name] += 1
        rows.append((code, rec, name))
    # collision resolution: identical constructed names -> append Цвят; still equal ->
    # proposal. ALSO checked against names of products NOT being renamed (conformant or
    # human-pinned), so a "unique within the batch" name can't shadow an existing one.
    renaming = {code for code, _r, _n in rows}
    used = {str((r.get("fields") or {}).get("Наименование") or "").strip()
            for c, r in canon.items() if c not in renaming}
    used.discard("")
    final_auto, final_prop = {}, {}
    by_name = collections.defaultdict(list)
    for code, rec, name in rows:
        by_name[name].append((code, rec))
    for name, group in by_name.items():
        for code, rec in group:
            col = _attrs(rec.get("fields") or {}).get("цвят", "").lower()
            for cand in ([name] + ([f"{name} {col}"] if col else [])):
                if cand not in used:
                    used.add(cand)
                    final_auto[code] = (rec, cand)
                    break
            else:
                final_prop[code] = (rec, name)          # unresolved duplicate -> human call
    return final_auto, final_prop, skipped


def main(apply=False):
    final_auto, final_prop, skipped = plan()
    print(f"AUTO-APPLY: {len(final_auto)} | needs-human proposals: {len(final_prop)} | skipped: {dict(skipped)}")
    shown = 0
    for code, (rec, name) in list(final_auto.items()):
        old = str((rec.get("fields") or {}).get("Наименование"))[:52]
        print(f"  {code}: {old!r}\n      -> {name!r}")
        shown += 1
        if shown >= 8:
            break
    if not apply:
        print("\n(dry-run; --apply to write)")
        return
    import db
    n = 0
    with open(OUT, "a", encoding="utf-8") as fh:
        for code, (rec, name) in final_auto.items():
            nf = dict(rec.get("fields") or {})
            nf["Наименование"] = name
            nd = dict(rec); nd["fields"] = nf
            nd["ts"] = datetime.now().isoformat(timespec="seconds")
            meta = dict(nd.get("meta") or {})
            meta["notes"] = list(meta.get("notes") or []) + ["name_builder:convention"]
            nd["meta"] = meta
            fh.write(json.dumps(nd, ensure_ascii=False) + "\n")
            fh.flush()
            try:
                db.record_version(nd)
            except Exception:
                pass
            n += 1
    # collisions -> 1-click proposals for the review console
    with open(HERE / "review_fixes.jsonl", "a", encoding="utf-8") as fh:
        for code, (rec, name) in final_prop.items():
            fh.write(json.dumps({
                "code": str(code), "ts": datetime.now().isoformat(timespec="seconds"),
                "готов_за_сайта": None, "оценка": "именна конвенция: неразрешен дубликат",
                "автоприложени": {}, "проблеми": [],
                "предложения": [{"поле": "Наименование",
                                 "стар": (rec.get("fields") or {}).get("Наименование"),
                                 "нов": name, "причина": "конструирано име (дубликат — провери)"}],
            }, ensure_ascii=False) + "\n")
    print(f"applied {n} names; {len(final_prop)} proposals -> review console")
    print("REVERT: rm results.lanez_names.jsonl && python db.py --ingest")


if __name__ == "__main__":
    main(apply="--apply" in sys.argv)
