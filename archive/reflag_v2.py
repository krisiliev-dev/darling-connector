"""One-time backlog re-flag: recompute needs_human under the v2 logic (category
reverts are safe; contamination = Russian letters + curated Russian-word markers)
and apply the expanded RU_FIX to already-stored fields. No reprocessing — the
enrichment content is unchanged; only the wrong review flag is corrected.
Human-reviewed records (review.verdict set) are left untouched. Backs up each file."""
import json, glob, os, shutil, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import run_one

TEXT_FIELDS = ("Наименование", "Описание", "Мета наименование",
               "Мета описание", "Атрибути", "Синоними", "Варианти")
BLOB_FIELDS = ("Наименование", "Описание", "Мета описание", "Атрибути")

files = [f for f in (["results.jsonl"] + sorted(glob.glob("results.lane*.jsonl")))
         if os.path.exists(f)]
tot = changed = up = 0
for path in files:
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    out = []
    for line in lines:
        if not line.strip():
            continue
        d = json.loads(line)
        notes = (d.get("meta") or {}).get("notes") or []
        if "agentic" not in notes:
            out.append(json.dumps(d, ensure_ascii=False)); continue
        if (d.get("review") or {}).get("verdict"):   # human already ruled — leave it
            out.append(json.dumps(d, ensure_ascii=False)); continue
        tot += 1
        fields = d.get("fields") or {}
        for k in TEXT_FIELDS:
            if fields.get(k):
                fx, _ = run_one.apply_ru_fix(str(fields[k]))
                fields[k] = fx
        blob = " ".join(str(fields.get(k) or "") for k in BLOB_FIELDS)
        has_ru = any(c in "ыэёЫЭЁ" for c in blob)
        ru_words = list(dict.fromkeys(run_one.russian_survivors(blob)))
        vision_ok = any(l.get("tool") == "analyze_image" and "греш" not in str(l.get("result", ""))
                        for l in ((d.get("meta") or {}).get("agent_log") or []))
        clean = not has_ru and not ru_words
        old_conf = d.get("confidence")
        if old_conf == "low":
            conf = "low"                       # genuine low stays low
        elif clean:
            conf = "high"
        else:
            conf = old_conf or "medium"        # contaminated -> keep for a human
        nh = conf != "high" or has_ru or bool(ru_words)
        new_notes = [n for n in notes if not str(n).startswith("russian_words:")]
        if ru_words:
            new_notes.append("russian_words:" + ",".join(ru_words)[:120])
        if "reflagged_v2" not in new_notes:
            new_notes.append("reflagged_v2")
        if d.get("confidence") != conf or d.get("needs_human") != nh:
            changed += 1
            if not nh and (d.get("needs_human")):
                up += 1
        d["confidence"] = conf
        d["needs_human"] = nh
        d["fields"] = fields
        d.setdefault("meta", {})["notes"] = new_notes
        out.append(json.dumps(d, ensure_ascii=False))
    if "--apply" in sys.argv:
        if not os.path.exists(path + ".reflagbak"):   # keep the pristine original
            shutil.copyfile(path, path + ".reflagbak")
        open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")

print(f"agentic records considered: {tot}")
print(f"records changed: {changed}  (unflagged: {up})")
print("APPLIED (backups .reflagbak written)" if "--apply" in sys.argv else "DRY RUN (pass --apply to write)")
