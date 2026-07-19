# -*- coding: utf-8 -*-
"""Deterministic-transform golden test — ZERO quota, run after ANY code change to the
tidy/guard/link layer. It pins the exact behaviours we established through testing (many
of them hard-won regression fixes), so a future refactor that silently breaks one is
caught in <1s instead of corrupting the catalogue.

  python det_golden.py            # check current behaviour vs the pinned snapshot
  python det_golden.py --update   # re-pin (only after an INTENTIONAL behaviour change)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).parent
SNAP = HERE / "det_golden_snapshot.json"

# Curated tricky inputs — each exercises a specific fix. If any output changes, we want
# to know and confirm it was intentional.
CASES = []


def _cases():
    import field_tidy as ft
    import related_linker as rl
    out = {}
    # --- unit normalization ---
    for s in ["Покривка 140x140 cm", "чайник 800 ml", "18 литра", "2.5mm нож",
              "кутия 500 gr", "маса 30x60x75 см"]:
        out[f"units::{s}"] = ft.normalize_units(s)[0]
    # --- decimal comma (BG locale); must NOT touch version/alloy numbers ---
    for s in ["обем 0.83 л", "нож 2.5 мм", "v3.5 модел", "18/10 стомана", "маса 30x60 см"]:
        out[f"dec::{s}"] = ft.normalize_decimal_comma(s)[0]
    # --- brand splitter (the corruption regressions must stay fixed) ---
    for b in ["HFM DEFNE", "HFM PARIS", "Bormioli Rocco", "Luigi Bormioli",
              "Ceramic House", "Home Line", "ECE Metal", "HORECANO KIDS", "HORECANO",
              "Bonna Collection", "Инокс Bonna", "Tefal Ingenio"]:
        out[f"brand::{b}"] = ft.split_brand(b)[0]
    # --- cross-family synonym cleanup (метал must stay on steel) ---
    out["syn::steel"] = ft.clean_synonyms("вилица, порцелан, метал, риба",
                                          "Материал: Неръждаема стомана")[0]
    out["syn::porcelain"] = ft.clean_synonyms("чиния, порцелан, стомана",
                                              "Материал: Порцелан")[0]
    # --- related base-name (variants must reduce to the same base) ---
    out["base::a"] = rl.base_name("Метална каничка за мляко 550 ml", "", "")
    out["base::b"] = rl.base_name("Метална каничка за мляко 1000мл.", "", "")
    # --- quality cleaners (Tier 1) ---
    import quality_clean as qcl
    out["qc_syn"] = qcl.clean_synonyms("вилица, tigan, kupa, HFM, неръждаема стомана")[0]
    out["qc_json"] = qcl.fix_json_attrs('{"Тип": "Чиния", "Материал": "Метал"}')[0]
    out["qc_keys"] = qcl.normalize_attr_keys("Марка: COK; Тип: Купа; Модел:; Цвят: Бял")[0]
    out["qc_catcode"] = qcl.strip_catcode_from_name("Ролтоп капак (17703)")[0]
    out["qc_dangle"] = qcl.fix_meta_dangle("Метален кош черен обем за")[0]
    out["qc_leak"] = qcl.strip_reasoning_leak(
        "<p>Изработена от метал. Материалът е потвърден от визуалната оценка на снимката. Устойчива.</p>")[0]
    # --- name builder grammar (stub vocab: stable regardless of the live vocabulary) ---
    import name_builder as nbd
    _stub = {"types": {"капак": ["Капак", "м"], "купа": ["Купа", "ж"], "кошче": ["Кошче", "ср"],
                       "пурер": ["Дозатор", "м"]},
             "canon": {},
             "materials": {"акрил": ["акрилен", "акрилна", "акрилно"],
                           "метал": ["метален", "метална", "метално"]},
             "shapes": {"правоъгълен": ["правоъгълен", "правоъгълна", "правоъгълно"],
                        "кръгла": ["кръгъл", "кръгла", "кръгло"]}}
    out["nb::m"] = nbd.build_name({"Бранд": "Alkan Züccaciye",
        "Наименование": "Капак правоъгълен акрил 27×33 см",
        "Атрибути": "Тип: Капак; Материал: Акрил; Форма: Правоъгълен; Размер: 27x33 см"}, _stub)[0]
    out["nb::f"] = nbd.build_name({"Бранд": "HORECANO", "Наименование": "Купа кръгла метал 24 см",
        "Атрибути": "Тип: Купа; Материал: Метал; Форма: Кръгла; Размер: 24 см"}, _stub)[0]
    out["nb::n"] = nbd.build_name({"Бранд": "", "Наименование": "Кошче акрил",
        "Атрибути": "Тип: Кошче; Материал: Акрил"}, _stub)[0]
    out["nb::syn"] = nbd.build_name({"Бранд": "EASY LIFE", "Наименование": "Пурер 350 мл",
        "Атрибути": "Тип: Пурер; Материал: Неръждаема стомана"}, _stub)[0]
    # --- rules renderer: Ø prefix, seasonal template, per-type recipe (all vs stub vocab) ---
    _stub2 = dict(_stub, types=dict(_stub["types"], **{"тиган": ["Тиган", "м"],
                                                       "тенджера": ["Тенджера", "ж"]}))
    _pan = {"Бранд": "Tefal", "Наименование": "Тиган",
            "Атрибути": "Тип: Тиган; Материал: Метал; Форма: Кръгла; Размер: 28 см"}
    _pot = {"Бранд": "HORECANO", "Наименование": "Тенджера",
            "Атрибути": "Тип: Тенджера; Материал: Метал; Цвят: Розов; Размер: 24 см"}
    out["nbr::diam"] = nbd.build_name(_pan, _stub2, {"default": nbd._DEFAULT_TEMPLATE,
        "overrides": [{"enabled": True, "when": {"Тип": "Тиган", "Форма": "кръгла"},
                       "size_prefix": "Ø"}]})[0]
    out["nbr::season"] = nbd.build_name(_pot, _stub2, {"default": nbd._DEFAULT_TEMPLATE,
        "overrides": [{"enabled": True, "when": {"Тип": "Тенджера", "Цвят": "розов"},
                       "template": ["lit:Свети Валентинска", "Тип", "Размер"]}]})[0]
    out["nbr::recipe"] = nbd.build_name(_pot, _stub2, {"default": nbd._DEFAULT_TEMPLATE,
        "types": {"Тенджера": ["Материал:adj", "Тип", "Цвят", "Бранд", "Размер"]}})[0]
    out["nbr::disabled"] = nbd.build_name(_pan, _stub2, {"default": nbd._DEFAULT_TEMPLATE,
        "overrides": [{"enabled": False, "when": {"Тип": "Тиган", "Форма": "кръгла"},
                       "size_prefix": "Ø"}]})[0]
    # --- catalogue guard: model-code detection vs dimensions ---
    import catalogue_guard as cg
    out["mcode::E2483"] = cg.source_model_codes("Купа E2483 26 см")
    out["mcode::h21"] = cg.source_model_codes("Купа h21 см")            # dimension, NOT a code
    out["mcode::YB12"] = cg.source_model_codes("Масат Zicco YB-12")
    return out


def check(update=False):
    cur = _cases()
    if update or not SNAP.exists():
        SNAP.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"pinned {len(cur)} deterministic cases -> {SNAP.name}")
        return 0
    old = json.loads(SNAP.read_text(encoding="utf-8"))
    drift = []
    for k, v in cur.items():
        if k not in old:
            drift.append((k, "NEW", v))
        elif json.dumps(old[k], ensure_ascii=False) != json.dumps(v, ensure_ascii=False):
            drift.append((k, old[k], v))
    for k in old:
        if k not in cur:
            drift.append((k, old[k], "REMOVED"))
    if not drift:
        print(f"✓ deterministic golden OK — {len(cur)} cases unchanged")
        return 0
    print(f"✗ DRIFT in {len(drift)} case(s):")
    for k, o, n in drift:
        print(f"  {k}\n     was: {o!r}\n     now: {n!r}")
    print("\nIf intentional, re-pin with: python det_golden.py --update")
    return 1


if __name__ == "__main__":
    sys.exit(check(update="--update" in sys.argv))
