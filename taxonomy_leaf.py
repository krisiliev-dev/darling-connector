# -*- coding: utf-8 -*-
"""TAXONOMY LEAF MAPPING (owner-approved plan 2026-07-17):

P1 (this script): map each canonical product type (name_vocab.canon, ~135) to its best
Shopify-taxonomy leaf, LLM-assisted: candidates are pre-narrowed by Bulgarian-name token
overlap, the model picks the best leaf or NONE. Output: canon_leaf_map.json.

P2 (--assign): derive per-product leaf: Тип attr → canon → leaf; fallback = the coarse
category→node mapping. Stored in DB table product_taxonomy(code, gid, full_name, source)
— export metadata only, product fields untouched.

The agent refinement pass (leaf_refine.py) later reviews assignments product-by-product.

  python taxonomy_leaf.py            # P1: build/refresh the canon→leaf map
  python taxonomy_leaf.py --assign   # P2: (re)assign all products
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "canon_leaf_map.json"
TAXO = HERE / "shopify_taxonomy"

PROMPT = """Ти класифицираш типове продукти от български магазин за дома в таксономията на
Shopify. За ВСЕКИ тип по-долу избери НАЙ-ТОЧНИЯ лист от предложените кандидати (те са с
номер, българско име и пълен английски път). Ако никой кандидат не е подходящ, върни null.
Гледай ТЪРГОВСКИЯ смисъл: "Чаша за вино" е stemware, не coffee cup; "Сач" е clay cooking
pot; "Дозатор" за сапун е soap dispenser.

{items}

Върни САМО валиден JSON: {{"тип": номер_или_null, ...}} — по един запис за всеки тип."""


def load_nodes():
    # FULL Shopify taxonomy (14,606 cats across all 26 verticals) is now the working set —
    # products are no longer constrained to the 8 home-goods verticals (owner 2026-07-19).
    full = HERE / "taxonomy_full.json"
    if full.exists():
        return json.loads(full.read_text(encoding="utf-8"))
    slim = HERE / "taxonomy_slim.json"
    if slim.exists():
        return json.loads(slim.read_text(encoding="utf-8"))
    import yaml
    cats = json.load(open(TAXO / "categories.json", encoding="utf-8"))
    bg = yaml.safe_load(open(TAXO / "categories_bg.yml", encoding="utf-8"))["bg-BG"]["categories"]
    cmap = json.load(open(HERE / "category_shopify_map.json", encoding="utf-8"))
    used_verticals = {(m.get("shopify_category") or "").split(" > ")[0] for m in cmap} - {""}
    nodes = []
    for v in cats["verticals"]:
        if v["name"] not in used_verticals:
            continue
        for c in v["categories"]:
            short = c["id"].rsplit("/", 1)[-1]
            nodes.append({"gid": c["id"], "full": c["full_name"],
                          "bg": (bg.get(short) or {}).get("name") or c["name"],
                          "leaf": not c.get("children")})
    return nodes


def _toks(s):
    return {w[:5] for w in re.findall(r"[а-яa-z]{4,}", str(s).lower())}


def candidates(nodes, canon, samples, k=25):
    ct = _toks(canon) | _toks(" ".join(samples))
    scored = []
    for n in nodes:
        sc = len(ct & _toks(n["bg"])) * 2 + len(ct & _toks(n["full"]))
        if n["leaf"]:
            sc += 0.5
        if sc > 0:
            scored.append((sc, n))
    scored.sort(key=lambda x: -x[0])
    return [n for _s, n in scored[:k]]


def sample_names():
    """{canon: [up to 2 product names]} from the live catalog."""
    import db
    import name_builder as nb
    vocab = nb.load_vocab()
    out = {}
    con = db.connect()
    try:
        for code, fj in con.execute("SELECT code, fields_json FROM products").fetchall():
            try:
                f = json.loads(fj or "{}")
            except Exception:
                continue
            hit = vocab["types"].get(nb._attrs(f).get("тип", "").lower())
            if not hit:
                continue
            c = hit[0]
            if len(out.setdefault(c, [])) < 2:
                out[c].append(str(f.get("Наименование") or "")[:70])
    finally:
        con.close()
    return out


def build_map():
    import run_one
    import name_builder as nb
    nodes = load_nodes()
    vocab = nb.load_vocab()
    samples = sample_names()
    canons = sorted(vocab.get("canon", {}))
    result = {}
    if OUT.exists():
        try:
            result = json.loads(OUT.read_text(encoding="utf-8"))
        except Exception:
            pass
    todo = [c for c in canons if c not in result]
    print(f"{len(canons)} canonical types, {len(todo)} to map", flush=True)
    BATCH = 8
    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
        blocks, cand_ix = [], {}
        for c in chunk:
            cs = candidates(nodes, c, samples.get(c) or [])
            cand_ix[c] = cs
            lines = [f"  {j}. {n['bg']}  [{n['full']}]" for j, n in enumerate(cs)]
            ex = "; ".join(samples.get(c) or []) or "(няма примери)"
            blocks.append(f'ТИП "{c}" (примери: {ex})\nКандидати:\n' + "\n".join(lines))
        try:
            out, model = run_one.generate_with_chain(
                PROMPT.format(items="\n\n".join(blocks)),
                system="Отговаряй само с валиден JSON.")
            data = run_one.extract_json(out) or {}
        except Exception as e:
            print(f"  batch {i//BATCH}: LLM failed {str(e)[:70]}", flush=True)
            continue
        ok = 0
        for c in chunk:
            v = data.get(c, "missing")
            if v is None:
                result[c] = None
                ok += 1
            elif isinstance(v, (int, float)) and 0 <= int(v) < len(cand_ix[c]):
                n = cand_ix[c][int(v)]
                result[c] = {"gid": n["gid"], "full": n["full"], "bg": n["bg"]}
                ok += 1
        OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  batch {i//BATCH + 1}/{-(-len(todo)//BATCH)}: {ok}/{len(chunk)} mapped "
              f"({model})", flush=True)
    mapped = sum(1 for v in result.values() if v)
    print(f"DONE: {mapped}/{len(result)} types mapped to leaves -> {OUT.name}")


def assign():
    import db
    import name_builder as nb
    vocab = nb.load_vocab()
    leafmap = json.loads(OUT.read_text(encoding="utf-8"))
    cmap = json.load(open(HERE / "category_shopify_map.json", encoding="utf-8"))
    bycat = {m["bg"]: m for m in cmap if m.get("shopify_id")}
    con = db.connect()
    con.execute("""CREATE TABLE IF NOT EXISTS product_taxonomy(
        code TEXT PRIMARY KEY, gid TEXT, full_name TEXT, source TEXT)""")
    n_leaf = n_cat = n_none = 0
    for code, fj in con.execute("SELECT code, fields_json FROM products").fetchall():
        try:
            f = json.loads(fj or "{}")
        except Exception:
            continue
        hit = vocab["types"].get(nb._attrs(f).get("тип", "").lower())
        leaf = leafmap.get(hit[0]) if hit else None
        if leaf:
            row = (str(code), leaf["gid"], leaf["full"], "type_leaf")
            n_leaf += 1
        else:
            m = None
            for part in str(f.get("Категории") or "").split(";"):
                p = part.strip()
                m = bycat.get(p.split("->")[-1].strip()) or bycat.get(p.split("->")[0].strip())
                if m:
                    break
            if m:
                row = (str(code), m["shopify_id"], m["shopify_category"], "category_fallback")
                n_cat += 1
            else:
                row = (str(code), None, None, "unassigned")
                n_none += 1
        con.execute("INSERT OR REPLACE INTO product_taxonomy VALUES (?,?,?,?)", row)
    con.commit()
    con.close()
    print(f"assigned: {n_leaf} via type-leaf, {n_cat} via category fallback, {n_none} unassigned")


if __name__ == "__main__":
    if "--assign" in sys.argv:
        assign()
    else:
        build_map()
