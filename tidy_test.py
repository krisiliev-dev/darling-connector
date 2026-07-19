# -*- coding: utf-8 -*-
"""TEST HARNESS — does the deterministic tidy help or make it worse?

Reads all finished records (READ-ONLY), applies the tidies in memory, and reports:
  * BEFORE/AFTER counts of each defect class the tidies target,
  * how many records changed per field,
  * REGRESSION guards (brand never emptied, no digit changed by unit-norm, etc.),
  * a diff sample per change type for human inspection.

Nothing is written to the live results. A separate --apply step (with backup) does that,
and only after this report looks clean.
"""
import json, glob, re, sys, io
from pathlib import Path
import field_tidy as ft
import related_linker as rl

HERE = Path(__file__).parent


def load_records_with_src():
    recs, files = [], {}
    for fp in glob.glob(str(HERE / "results.lane*.jsonl")):
        for i, line in enumerate(open(fp, encoding="utf-8", errors="replace")):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if "agentic" in ((d.get("meta") or {}).get("notes") or []):
                recs.append(d)
    return recs


def _digits(s):
    return re.findall(r"\d+", str(s or ""))


def main(apply=False):
    recs = load_records_with_src()
    rel_idx = rl.related_index(recs)
    n = len(recs)

    before = {"latin_unit": 0, "verbose_unit": 0, "brand_multiword_splittable": 0,
              "cross_family_syn": 0, "empty_related": 0, "not_brand_first": 0}
    after = dict.fromkeys(before, 0)
    changed = {"Наименование": 0, "Бранд": 0, "Атрибути": 0, "Синоними": 0,
               "Мета наименование": 0, "Мета описание": 0, "Описание": 0, "Свързани": 0}
    reorder_changed = 0
    regress = {"brand_emptied": 0, "digit_changed_by_units": 0, "brand_single_token_changed": 0}
    samples = {"units": [], "brand": [], "synonyms": [], "related": [], "reorder": []}

    for d in recs:
        f = d.get("fields") or {}
        code = str(d.get("code"))
        # --- BEFORE defect counts ---
        blob = " ".join(str(f.get(k) or "") for k in ft._UNIT_FIELDS)
        if ft._LAT_RX.search(blob):
            before["latin_unit"] += 1
        if ft._VERB_RX.search(blob):
            before["verbose_unit"] += 1
        b0 = f.get("Бранд")
        b1, _ = ft.split_brand(b0)
        if b0 and b1 != b0:
            before["brand_multiword_splittable"] += 1
        syn2, rm = ft.clean_synonyms(f.get("Синоними"), f.get("Атрибути"))
        if rm:
            before["cross_family_syn"] += 1
        if not str(f.get("Свързани") or "").strip():
            before["empty_related"] += 1
        nm = str(f.get("Наименование") or "")
        if b0 and len(str(b0)) >= 2 and not nm.lower().startswith(str(b0).lower()) \
                and re.search(r"(?<![0-9A-Za-zА-Яа-я])" + re.escape(str(b0)) + r"(?![0-9A-Za-zА-Яа-я])", nm):
            before["not_brand_first"] += 1

        # --- APPLY tidy (safe set) + related union ---
        newf, changes = ft.tidy(f, do_reorder=False)
        variants = rel_idx.get(code, [])
        if variants:
            merged = rl.union_related(f.get("Свързани"), variants)
            if merged != f.get("Свързани"):
                newf["Свързани"] = merged
                changes.append("related")

        # --- REGRESSION guards ---
        if b0 and str(b0).strip() and not str(newf.get("Бранд") or "").strip():
            regress["brand_emptied"] += 1
        if b0 and " " not in str(b0).strip() and newf.get("Бранд") != b0 \
                and str(newf.get("Бранд") or "").strip():
            regress["brand_single_token_changed"] += 1
        for col in ft._UNIT_FIELDS:
            if _digits(f.get(col)) != _digits(newf.get(col)):
                regress["digit_changed_by_units"] += 1
                break

        # --- track what changed + collect samples ---
        for col in changed:
            if str(f.get(col) or "") != str(newf.get(col) or ""):
                changed[col] += 1
        for tag, bucket in (("units", "Наименование"),):
            pass
        if any(c.startswith("units") for c in changes) and len(samples["units"]) < 6:
            samples["units"].append((code, f.get("Наименование"), newf.get("Наименование")))
        if any(c.startswith(("brand", "name_brand")) for c in changes) and len(samples["brand"]) < 8:
            samples["brand"].append((code, b0, newf.get("Бранд"), newf.get("Наименование")))
        if any(c.startswith("syn_material") for c in changes) and len(samples["synonyms"]) < 6:
            samples["synonyms"].append((code, f.get("Синоними"), newf.get("Синоними")))
        if "related" in changes and len(samples["related"]) < 8:
            samples["related"].append((code, f.get("Наименование"), newf.get("Свързани")))

        # --- AFTER defect counts (on tidied copy) ---
        blob2 = " ".join(str(newf.get(k) or "") for k in ft._UNIT_FIELDS)
        if ft._LAT_RX.search(blob2):
            after["latin_unit"] += 1
        if ft._VERB_RX.search(blob2):
            after["verbose_unit"] += 1
        nb1, _ = ft.split_brand(newf.get("Бранд"))
        if newf.get("Бранд") and nb1 != newf.get("Бранд"):
            after["brand_multiword_splittable"] += 1
        _, rm2 = ft.clean_synonyms(newf.get("Синоними"), newf.get("Атрибути"))
        if rm2:
            after["cross_family_syn"] += 1
        if not str(newf.get("Свързани") or "").strip():
            after["empty_related"] += 1

        # reorder measured separately (risky transform)
        rn, rc = ft.reorder_name(f.get("Наименование"), b0, f.get("Атрибути"))
        if rc:
            reorder_changed += 1
            if len(samples["reorder"]) < 10:
                samples["reorder"].append((code, f.get("Наименование"), rn))

    out = io.StringIO()
    p = lambda *a: print(*a, file=out)
    p(f"=== TIDY TEST on {n} finished products (read-only) ===\n")
    p("DEFECT CLASS                     BEFORE   AFTER   fixed")
    for k in before:
        p(f"  {k:30s} {before[k]:6d}  {after[k]:6d}   {before[k]-after[k]:+d}")
    p("\nRECORDS CHANGED PER FIELD:")
    for k, v in changed.items():
        if v:
            p(f"  {k:22s} {v}")
    p(f"\nname-order reorder would change: {reorder_changed} (measured, NOT applied)")
    p("\nREGRESSION GUARDS (must all be 0):")
    for k, v in regress.items():
        p(f"  {k:30s} {v}")
    p("\n--- SAMPLE: unit normalization ---")
    for c, a, b in samples["units"]:
        p(f"  {c}: {a!r}\n       -> {b!r}")
    p("\n--- SAMPLE: brand split/sync ---")
    for c, a, b, nm in samples["brand"]:
        p(f"  {c}: brand {a!r} -> {b!r} | name -> {nm!r}")
    p("\n--- SAMPLE: synonym material cleanup ---")
    for c, a, b in samples["synonyms"]:
        p(f"  {c}: {a!r}\n       -> {b!r}")
    p("\n--- SAMPLE: related variant links added ---")
    for c, nm, rel in samples["related"]:
        p(f"  {c} ({nm!r}) -> Свързани: {rel!r}")
    p("\n--- SAMPLE: name reorder (RISKY — inspect before enabling) ---")
    for c, a, b in samples["reorder"]:
        p(f"  {c}: {a!r}\n       -> {b!r}")
    txt = out.getvalue()
    print(txt)
    (HERE / "tidy_test_report.txt").write_text(txt, encoding="utf-8")


if __name__ == "__main__":
    main(apply="--apply" in sys.argv)
