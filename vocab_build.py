# -*- coding: utf-8 -*-
"""Build the COMPREHENSIVE product-type vocabulary for the naming system.

Input: raw_types.json (every distinct Тип value + name head-nouns, with counts).
Method: LLM canonicalization in batches through the pipeline's own free chain — each raw
type maps to a canonical noun (short, singular, what a shopper searches) + grammatical
gender; the growing canonical list is fed back each batch so synonyms converge onto ONE
name (дозатор/пурер/диспенсър -> Дозатор). Deterministic merge; nothing needs manual
review (owner request) — the review console still shows every rename as a diff later.

Output: name_vocab.json
  { "types": {raw_lower: ["Канон", "м|ж|ср"]},
    "canon": {"Канон": "м|ж|ср"},
    "materials": {material_lower: ["прил_м","прил_ж","прил_ср"]},
    "shapes": {...} }
"""
import json, re, sys, time
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "name_vocab.json"
PARTIAL = HERE / "name_vocab.partial.json"    # per-batch checkpoint — a crash resumes, not restarts

# Hand-written Bulgarian adjective tables (deterministic grammar — the LLM never touches
# these). Materials without a natural adjective render as "от <материал>" at build time.
MATERIALS = {
    "пластмаса": ["пластмасов", "пластмасова", "пластмасово"],
    "метал": ["метален", "метална", "метално"],
    "стъкло": ["стъклен", "стъклена", "стъклено"],
    "керамика": ["керамичен", "керамична", "керамично"],
    "порцелан": ["порцеланов", "порцеланова", "порцеланово"],
    "дърво": ["дървен", "дървена", "дървено"],
    "бамбук": ["бамбуков", "бамбукова", "бамбуково"],
    "текстил": ["текстилен", "текстилна", "текстилно"],
    "силикон": ["силиконов", "силиконова", "силиконово"],
    "меламин": ["меламинов", "меламинова", "меламиново"],
    "акрил": ["акрилен", "акрилна", "акрилно"],
    "алуминий": ["алуминиев", "алуминиева", "алуминиево"],
    "чугун": ["чугунен", "чугунена", "чугунено"],
    "мед": ["меден", "медна", "медно"],
    "месинг": ["месингов", "месингова", "месингово"],
    "камък": ["каменен", "каменна", "каменно"],
    "мрамор": ["мраморен", "мраморна", "мраморно"],
    "хартия": ["хартиен", "хартиена", "хартиено"],
    "картон": ["картонен", "картонена", "картонено"],
    "полиестер": ["полиестерен", "полиестерна", "полиестерно"],
    "памук": ["памучен", "памучна", "памучно"],
    "ратан": ["ратанов", "ратанова", "ратаново"],
    "стомана": ["стоманен", "стоманена", "стоманено"],
    "поликарбонат": ["поликарбонатен", "поликарбонатна", "поликарбонатно"],
    "кожа": ["кожен", "кожена", "кожено"],
    "вълна": ["вълнен", "вълнена", "вълнено"],
    "лен": ["ленен", "ленена", "ленено"],
    "желязо": ["железен", "желязна", "желязно"],
    "стиропор": ["стиропорен", "стиропорена", "стиропорено"],
    "гума": ["гумен", "гумена", "гумено"],
}
SHAPES = {
    "кръгла": ["кръгъл", "кръгла", "кръгло"], "кръгъл": ["кръгъл", "кръгла", "кръгло"],
    "кръгло": ["кръгъл", "кръгла", "кръгло"],
    "правоъгълна": ["правоъгълен", "правоъгълна", "правоъгълно"],
    "правоъгълен": ["правоъгълен", "правоъгълна", "правоъгълно"],
    "правоъгълно": ["правоъгълен", "правоъгълна", "правоъгълно"],
    "квадратна": ["квадратен", "квадратна", "квадратно"],
    "квадратен": ["квадратен", "квадратна", "квадратно"],
    "квадратно": ["квадратен", "квадратна", "квадратно"],
    "овална": ["овален", "овална", "овално"], "овален": ["овален", "овална", "овално"],
    "овално": ["овален", "овална", "овално"],
    "триъгълна": ["триъгълен", "триъгълна", "триъгълно"],
    "триъгълен": ["триъгълен", "триъгълна", "триъгълно"],
    "продълговата": ["продълговат", "продълговата", "продълговато"],
    "продълговат": ["продълговат", "продълговата", "продълговато"],
    "цилиндрична": ["цилиндричен", "цилиндрична", "цилиндрично"],
    "цилиндричен": ["цилиндричен", "цилиндрична", "цилиндрично"],
}

PROMPT = """Ти си лексикограф за български онлайн магазин за домакински стоки. За ВСЕКИ \
"суров тип" по-долу дай КАНОНИЧНОТО име на типа продукт: кратко съществително име \
(1-2 думи, единствено число, с главна буква), което български клиент реално би търсил, \
плюс граматичния му род (м/ж/ср).

ВАЖНО: синонимите се обединяват — 'дозатор', 'пурер', 'диспенсър', 'термодиспенсър' \
всички стават 'Дозатор'. ПОЛЗВАЙ ПОВТОРНО вече избраните канони от списъка ВЕЧЕ ИЗБРАНИ, \
когато суровият тип е техен синоним или подвид без търговска разлика. Ако суровият тип \
описва РАЗЛИЧЕН продукт, дай нов канон. Не измисляй типове, които не са в списъка.

ВЕЧЕ ИЗБРАНИ КАНОНИ: {known}

СУРОВИ ТИПОВЕ:
{items}

Върни САМО валиден JSON без коментари, формат:
{{"суров тип": ["Канон", "м"], ...}} (род: м, ж или ср)"""


def canonicalize(raw_items):
    """raw_items: [(raw, count)] -> {raw: [canon, gender]} via batched LLM calls."""
    import run_one
    mapping = {}
    canon_genders = {}
    if PARTIAL.exists():
        try:
            ck = json.loads(PARTIAL.read_text(encoding="utf-8"))
            mapping, canon_genders = ck.get("types", {}), ck.get("canon", {})
            print(f"  resumed checkpoint: {len(mapping)} mapped, {len(canon_genders)} canon", flush=True)
        except Exception:
            pass
    batch = 40
    items = [r for r, _c in raw_items if str(r).strip().lower() not in mapping]
    for i in range(0, len(items), batch):
        chunk = items[i:i + batch]
        known = ", ".join(sorted(canon_genders)[:180]) or "(няма още)"
        prompt = PROMPT.format(known=known, items="\n".join(f"- {x}" for x in chunk))
        try:
            out, model = run_one.generate_with_chain(prompt, system="Отговаряй само с валиден JSON.")
            data = run_one.extract_json(out) or {}
        except Exception as e:
            print(f"  batch {i//batch}: LLM failed ({str(e)[:60]}) — skipped")
            continue
        ok = 0
        for raw, val in (data.items() if isinstance(data, dict) else []):
            if not isinstance(val, (list, tuple)) or len(val) < 2:
                continue
            canon = str(val[0]).strip()
            g = str(val[1]).strip().lower()[:2]
            if not canon or g not in ("м", "ж", "ср", "с"):
                continue
            g = "ср" if g == "с" else g
            rl = str(raw).strip().lower()
            mapping[rl] = [canon, g]
            canon_genders.setdefault(canon, g)
            ok += 1
        print(f"  batch {i//batch + 1}/{-(-len(items)//batch)}: {ok}/{len(chunk)} mapped "
              f"({model if 'model' in dir() else '?'}) | canon so far: {len(canon_genders)}", flush=True)
        PARTIAL.write_text(json.dumps({"types": mapping, "canon": canon_genders},
                                      ensure_ascii=False), encoding="utf-8")
        time.sleep(1)
    return mapping, canon_genders


def main():
    raw = json.loads((HERE / "raw_types.json").read_text(encoding="utf-8"))
    # types first (highest quality signal), then head-nouns that aren't already covered
    types = raw["types"]
    print(f"canonicalizing {len(types)} raw Тип values...", flush=True)
    mapping, canon = canonicalize(types)
    covered = set(mapping)
    heads = [(h, c) for h, c in raw["heads"] if h not in covered and c >= 3]
    print(f"canonicalizing {len(heads)} name head-nouns (fallback signal)...", flush=True)
    m2, c2 = canonicalize(heads)
    mapping.update(m2)
    for k, v in c2.items():
        canon.setdefault(k, v)
    vocab = {"types": mapping, "canon": canon, "materials": MATERIALS, "shapes": SHAPES}
    OUT.write_text(json.dumps(vocab, ensure_ascii=False, indent=1), encoding="utf-8")
    PARTIAL.unlink(missing_ok=True)     # a finished build must not seed the NEXT rebuild
    print(f"\nVOCABULARY: {len(mapping)} raw -> {len(canon)} canonical types -> {OUT.name}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)
