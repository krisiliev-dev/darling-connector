# -*- coding: utf-8 -*-
"""One-time backfill: apply the catalogue_guard (strip leaked catalogue numbers /
'BR' prefix from customer-facing text, drop prefix/collection Бранд, canonicalise
real brands) to already-stored records. No reprocessing — the enrichment content
is unchanged; only leaked catalogue fragments are removed.

Safe against the live cron lanes: each lane appends one record under a briefly-held
handle (open('a') closes immediately), so the file is closed ~all the time. We read,
transform, write a temp, and os.replace with retry; a record appended in the tiny
read->replace window is simply reprocessed later (it won't be in the done-set).

Usage:  python clean_catalogue.py            # dry run
        python clean_catalogue.py --apply    # write (backups: *.catbak)
"""
import json, glob, os, sys, time
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import catalogue_guard as cg
import brand_tools

TEXT_FIELDS = ("Наименование", "Мета наименование", "Мета описание", "Описание")

# code -> source Стока
stoka = {}
for line in open("tasks.jsonl", encoding="utf-8", errors="replace"):
    if not line.strip():
        continue
    try:
        t = json.loads(line)
    except Exception:
        continue
    stoka[t.get("code")] = (t.get("ground_truth") or {}).get("Стока")

gaz = brand_tools.load()
apply = "--apply" in sys.argv
files = [f for f in (["results.jsonl"] + sorted(glob.glob("results.lane*.jsonl")))
         if os.path.exists(f)]

n_names = n_brands = n_records = 0
examples = []
for path in files:
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    out = []
    changed_file = False
    for line in lines:
        if not line.strip():
            continue
        d = json.loads(line)
        notes = (d.get("meta") or {}).get("notes") or []
        if "agentic" not in notes or (d.get("review") or {}).get("verdict"):
            out.append(json.dumps(d, ensure_ascii=False)); continue
        f = d.get("fields") or {}
        src = stoka.get(d.get("code"))
        catnums = cg.source_catnums(src)
        prefs = [p for _, p in catnums]
        lead = cg.source_leading_prefix(src, gaz)
        if lead:
            prefs.append(lead)
        mcodes = cg.source_model_codes(src)
        removed = []
        name_changed = False
        for col in TEXT_FIELDS:
            if f.get(col):
                clean, rm = cg.strip_catnums_from_name(str(f[col]), catnums)
                clean, rm2 = cg.strip_model_codes(clean, mcodes)
                if lead and col in ("Наименование", "Мета наименование"):
                    clean, lc = cg.strip_leading_prefix(clean, lead)
                    if lc:
                        rm2 = rm2 + [lead]
                if col in ("Наименование", "Мета наименование"):
                    clean = cg._tidy(clean)          # fix any pre-existing orphan dash
                if clean != f[col]:
                    f[col] = clean
                    removed += rm + rm2
                    name_changed = True
        b0 = f.get("Бранд")
        b1, bn = cg.guard_brand(b0, prefs, gaz)
        touched = False
        if name_changed:
            n_names += 1; touched = True
            if removed:
                notes = [n for n in notes if not str(n).startswith("catnum_stripped:")]
                notes.append("catnum_stripped:" + ",".join(dict.fromkeys(removed)))
        if b1 != b0:
            n_brands += 1; touched = True
            f["Бранд"] = b1
            if bn and not any(str(n) == bn for n in notes):
                notes.append(bn)
        # NOTE: series/line tokens are NOT stripped from the title here — genuine
        # product lines are the agent's call (owner: keep 'Elite Multi'-type lines).
        # SEO-length trim on meta fields (Google truncates over-length meta anyway).
        mtrim = []
        for mk, lim in (("Мета наименование", 60), ("Мета описание", 160)):
            if f.get(mk):
                tv, ch = cg.trim_meta(str(f[mk]), lim)
                if ch:
                    f[mk] = tv; touched = True; mtrim.append(mk)
        if mtrim and not any(str(n).startswith("meta_trimmed:") for n in notes):
            notes.append("meta_trimmed:" + ",".join(mtrim))
        if touched:
            n_records += 1
            changed_file = True
            d["fields"] = f
            d.setdefault("meta", {})["notes"] = notes
            if len(examples) < 15:
                examples.append((d.get("code"), removed, b0, b1))
        out.append(json.dumps(d, ensure_ascii=False))
    if apply and changed_file:
        if not os.path.exists(path + ".catbak"):
            import shutil
            shutil.copyfile(path, path + ".catbak")
        tmp = path + ".tmp"
        open(tmp, "w", encoding="utf-8").write("\n".join(out) + "\n")
        for attempt in range(6):
            try:
                os.replace(tmp, path)
                break
            except PermissionError:
                time.sleep(0.4)          # lane mid-write; retry
        else:
            os.remove(tmp)
            print(f"  WARN: could not replace {path} (locked) — skipped")

print(f"records changed: {n_records}  (names cleaned: {n_names}, brands changed: {n_brands})")
print("--- examples (code | removed-from-name | brand: before -> after) ---")
for c, rm, b0, b1 in examples:
    print(f"  {c}  removed={rm}  brand: {b0!r} -> {b1!r}")
print("APPLIED (backups *.catbak)" if apply else "DRY RUN (pass --apply to write)")
