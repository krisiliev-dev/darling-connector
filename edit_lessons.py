# -*- coding: utf-8 -*-
"""EDIT-LESSONS MINER — learns from the owner's manual edits (owner request 2026-07-17).

Every human edit on the review site is a training signal: the diff between what the
pipeline produced and what the owner changed it to. This module collects each NEW human
edit since the last run, diffs the fields, and asks an LLM to induce GENERAL rules
("маха 'обикновено' от описанията -> avoid filler adverbs") with a concrete suggestion
for improving the processing instructions.

IT CHANGES NOTHING BY ITSELF — output is a report (edit_lessons.md) reviewed by the
supervising agent at each check; only rules the owner/supervisor accept get wired into
the prompts.

  python edit_lessons.py            # analyze new edits, append to edit_lessons.md
  python edit_lessons.py --status   # how many edits processed/pending
"""
import difflib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
REPORT = HERE / "edit_lessons.md"
STATE = HERE / "edit_lessons_state.json"
FIELDS = ("Наименование", "Бранд", "Атрибути", "Описание",
          "Мета наименование", "Мета описание", "Свързани")

PROMPT = """Ти анализираш РЕДАКЦИИ, направени НА РЪКА от собственика на български онлайн \
магазин върху продуктови описания, генерирани от AI. За всяка редакция виждаш СТАРО -> \
НОВО по поле. Изведи ОБЩИ ПРАВИЛА, които обясняват редакциите — какво собственикът \
систематично не харесва или предпочита.

За всяко правило дай JSON обект:
  "правило": кратка формулировка (напр. "маха запълващи наречия като 'обикновено'"),
  "защо": вероятната причина,
  "доказателство": кои редакции го подкрепят (кодове),
  "предложение": КОНКРЕТНА промяна в инструкциите на обработващия агент (1-2 изречения),
  "увереност": "висока" само при 2+ независими примера, иначе "ниска"

Върни САМО валиден JSON: {{"правила": [...]}}. Ако редакциите са твърде малко или \
твърде разнородни за общо правило, върни {{"правила": []}}.

РЕДАКЦИИ:
{edits}"""


def _strip_html(s):
    return re.sub(r"<[^>]+>", " ", str(s or "")).strip()


def _word_diff(old, new, cap=400):
    """Compact removed/added word runs — enough signal without dumping full texts."""
    ow, nw = _strip_html(old).split(), _strip_html(new).split()
    sm = difflib.SequenceMatcher(a=ow, b=nw, autojunk=False)
    rem, add = [], []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ("delete", "replace"):
            rem.append(" ".join(ow[i1:i2]))
        if op in ("insert", "replace"):
            add.append(" ".join(nw[j1:j2]))
    return ("- " + " | ".join(rem)[:cap] if rem else "") + \
           ("\n  + " + " | ".join(add)[:cap] if add else "")


def collect_new():
    """[(key, code, ts, {field: (old, new)})] for human edits not yet analyzed.
    A version is a NEW human edit only if its notes contain MORE 'human_edit' markers
    than the previous version's (notes are copied forward, so mere presence would match
    every later machine write too). Keys are (code, ts) — stable across db --ingest."""
    import db
    seen = set()
    if STATE.exists():
        try:
            seen = set(json.loads(STATE.read_text(encoding="utf-8")).get("seen", []))
        except Exception:
            pass
    con = db.connect()
    out = []

    def _he_count(nj):
        try:
            return sum(1 for n in json.loads(nj or "[]") if str(n) == "human_edit")
        except Exception:
            return 0

    try:
        rows = con.execute(
            "SELECT id, code, ts, fields_json, notes_json FROM versions "
            "WHERE notes_json LIKE '%human_edit%' ORDER BY ts, id").fetchall()
        for vid, code, ts, fj, nj in rows:
            key = f"{code}|{ts}"
            if key in seen:
                continue
            prev = con.execute(
                "SELECT fields_json, notes_json FROM versions WHERE code=? "
                "AND (ts < ? OR (ts = ? AND id < ?)) ORDER BY ts DESC, id DESC LIMIT 1",
                (code, ts, ts, vid)).fetchone()
            if prev and _he_count(nj) <= _he_count(prev[1]):
                continue                    # marker only carried forward — not a new edit
            new_f = json.loads(fj or "{}")
            old_f = json.loads(prev[0]) if prev and prev[0] else {}
            changed = {k: (old_f.get(k), new_f.get(k)) for k in FIELDS
                       if str(old_f.get(k) or "").strip() != str(new_f.get(k) or "").strip()}
            if changed:
                out.append((key, str(code), ts, changed))
    finally:
        con.close()
    return out, seen


def analyze(edits):
    import run_one
    blocks = []
    for _vid, code, _ts, changed in edits:
        lines = [f"## Продукт {code}"]
        for k, (old, new) in changed.items():
            d = _word_diff(old, new)
            if d.strip():
                lines.append(f"[{k}]\n  {d}")
        blocks.append("\n".join(lines))
    out, model = run_one.generate_with_chain(
        PROMPT.format(edits="\n\n".join(blocks)[:14000]),
        system="Отговаряй само с валиден JSON.")
    data = run_one.extract_json(out) or {}
    return (data.get("правила") or []), model


def main():
    edits, seen = collect_new()
    if "--status" in sys.argv:
        print(f"analyzed edits: {len(seen)} | pending: {len(edits)}")
        return
    if not edits:
        print("no new human edits to learn from.")
        return
    rules, model = analyze(edits)
    ts = datetime.now().isoformat(timespec="seconds")
    with open(REPORT, "a", encoding="utf-8") as fh:
        fh.write(f"\n## {ts} — {len(edits)} нови редакции ({model})\n\n")
        fh.write(f"Продукти: {', '.join(sorted({c for _, c, _, _ in edits}))}\n\n")
        if not rules:
            fh.write("_(няма достатъчно сигнал за общо правило)_\n")
        for r in rules:
            fh.write(f"- **{r.get('правило')}** [{r.get('увереност')}]\n"
                     f"  - защо: {r.get('защо')}\n"
                     f"  - доказателство: {r.get('доказателство')}\n"
                     f"  - предложение: {r.get('предложение')}\n")
    STATE.write_text(json.dumps(
        {"seen": sorted(seen | {v for v, _, _, _ in edits}), "updated": ts}),
        encoding="utf-8")
    print(f"analyzed {len(edits)} edits -> {len(rules)} rule(s) -> {REPORT.name}")
    for r in rules:
        print(f"  • {r.get('правило')} [{r.get('увереност')}]")


if __name__ == "__main__":
    main()
