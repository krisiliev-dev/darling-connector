# -*- coding: utf-8 -*-
"""PER-LEAF ATTRIBUTE SCHEMA for pipeline v2 (owner-approved redesign 2026-07-18).

The taxonomy leaf defines the product's contract:
  * schema_for(gid)  -> required attribute groups with ALLOWED VALUES (Shopify's official
    bg-BG attribute + value vocabularies for that leaf) plus a universal core
    (Материал/Цвят/Размер-Обем) — every group REQUIRED, with the escape hatch
    "друго: <стойност>" so agents are never forced into a wrong enum.
  * noun_for(gid)    -> (singular Bulgarian type noun, gender) for the naming system —
    "Тигани за пържене" -> ("Тиган", "м"). LLM-built once per leaf, cached.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
NOUNS = HERE / "leaf_nouns.json"

_cache = {"tax": None, "nouns": None}

CORE = [("Материал", "material"), ("Цвят", "color")]      # + Размер/Обем added free-form

NOUN_PROMPT = """За всяко българско име на категория по-долу дай ЕДИНСТВЕНОТО число на
главното съществително (типа продукт, който клиент търси) и рода му (м/ж/ср).
Пример: "Тигани за пържене" -> ["Тиган","м"]; "Буркани за бисквитки" -> ["Буркан","м"];
"Изтривалки за врати" -> ["Изтривалка","ж"].

{items}

Върни САМО валиден JSON: {{"име на категория": ["Съществително","род"], ...}}"""


def _tax():
    if _cache["tax"] is None:
        import shopify_schema_align as ssa
        by_gid, attr_def, bg_name_for, bg_value_for = ssa.load_taxonomy()
        import yaml
        bgc = yaml.safe_load(open(HERE / "shopify_taxonomy" / "categories_bg.yml",
                                  encoding="utf-8"))["bg-BG"]["categories"]
        cats = json.load(open(HERE / "shopify_taxonomy" / "categories.json", encoding="utf-8"))
        node = {}
        for v in cats["verticals"]:
            for c in v["categories"]:
                node[c["id"]] = c
        _cache["tax"] = (by_gid, attr_def, bg_name_for, bg_value_for, bgc, node)
    return _cache["tax"]


def bg_leaf_name(gid):
    *_, bgc, node = _tax()
    c = node.get(gid)
    if not c:
        return None
    return (bgc.get(gid.rsplit("/", 1)[-1]) or {}).get("name") or c.get("name")


def full_name(gid):
    *_, node = _tax()
    c = node.get(gid)
    return c.get("full_name") if c else None


def schema_for(gid, max_values=30):
    # DB-cached (taxonomy_precompute.py) — avoids the ~27s taxonomy parse per process
    try:
        import db as _db
        con = _db.connect()
        r = con.execute("SELECT schema_json FROM leaf_schemas WHERE gid=?", (gid,)).fetchone()
        con.close()
        if r:
            return json.loads(r[0])
    except Exception:
        pass
    return _schema_for_slow(gid, max_values)


def _schema_for_slow(gid, max_values=30):
    """[{група, стойности:[...], източник}] — Shopify attrs for the leaf + universal core.
    Every group is REQUIRED; agents may answer "друго: X" or "няма" (not applicable,
    must be justified)."""
    by_gid, attr_def, bg_name_for, bg_value_for, _bgc, node = _tax()
    out, seen = [], set()

    def norm(s):
        return re.sub(r"[^0-9a-zа-я]", "", str(s or "").lower())

    for ta in (by_gid.get(gid) or []):
        h = ta.get("handle") or ""
        bgn = bg_name_for(h, ta.get("name") or h)
        if not bgn or norm(bgn) in seen:
            continue
        seen.add(norm(bgn))
        adef = attr_def.get(h) or {}
        vals = [bg_value_for(v.get("handle"), v.get("name"))
                for v in (adef.get("values") or [])[:max_values]]
        out.append({"група": bgn, "стойности": [x for x in dict.fromkeys(vals) if x],
                    "източник": "shopify", "shopify_attr": h})
    for bgn, h in CORE:
        if norm(bgn) in seen:
            continue
        seen.add(norm(bgn))
        adef = attr_def.get(h) or {}
        vals = [bg_value_for(v.get("handle"), v.get("name"))
                for v in (adef.get("values") or [])[:max_values]]
        out.append({"група": bgn, "стойности": [x for x in dict.fromkeys(vals) if x],
                    "източник": "core", "shopify_attr": h})
    out.append({"група": "Размер/Обем", "стойности": [],
                "източник": "core", "shopify_attr": None})
    return out


def _noun_table():
    import db
    con = db.connect()
    con.execute("CREATE TABLE IF NOT EXISTS leaf_nouns(gid TEXT PRIMARY KEY, noun TEXT, gender TEXT)")
    return con


def _load_nouns():
    """DB-backed (WAL handles the 12 concurrent lanes; the old JSON file raced)."""
    import time as _t
    if _cache["nouns"] is not None and _t.time() - _cache.get("nouns_ts", 0) < 120:
        return _cache["nouns"]
    con = _noun_table()
    try:
        _cache["nouns"] = {g: [n, x] for g, n, x in
                            con.execute("SELECT gid, noun, gender FROM leaf_nouns").fetchall()}
    finally:
        con.close()
    _cache["nouns_ts"] = _t.time()
    return _cache["nouns"]


def noun_for(gid):
    """(singular noun, gender) for the leaf — from cache; ensure_nouns() fills gaps."""
    n = _load_nouns().get(gid)
    return (n[0], n[1]) if n else (None, None)


def ensure_nouns(gids):
    """LLM-batch any leaves missing a noun; INSERT OR IGNORE into the DB (concurrent
    lanes may race to fill the same leaf — first writer wins, no lost updates)."""
    import run_one
    nouns = _load_nouns()
    todo = []
    for g in dict.fromkeys(gids):
        if g not in nouns:
            nm = bg_leaf_name(g)
            if nm:
                todo.append((g, nm))
    if not todo:
        return 0
    added = 0
    con = _noun_table()
    try:
        for i2 in range(0, len(todo), 25):
            chunk = todo[i2:i2 + 25]
            items = chr(10).join('- "' + nm + '"' for _g, nm in chunk)
            try:
                out, _model = run_one.generate_with_chain(
                    NOUN_PROMPT.format(items=items), system="Отговаряй само с валиден JSON.")
                data = run_one.extract_json(out) or {}
            except Exception:
                continue
            for g, nm in chunk:
                v = data.get(nm)
                if isinstance(v, (list, tuple)) and len(v) >= 2 and str(v[1]) in ("м", "ж", "ср"):
                    con.execute("INSERT OR IGNORE INTO leaf_nouns VALUES (?,?,?)",
                                (g, str(v[0]).strip(), str(v[1])))
                    added += 1
        con.commit()
        # read back the STORED values: if another lane won the INSERT race, its noun
        # is canonical — using our own answer would give same-leaf products divergent
        # type nouns depending on which lane processed them
        for g, _nm in todo:
            r = con.execute("SELECT noun, gender FROM leaf_nouns WHERE gid=?",
                            (g,)).fetchone()
            if r:
                nouns[g] = [r[0], r[1]]
    finally:
        con.close()
    return added