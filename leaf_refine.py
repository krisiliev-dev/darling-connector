# -*- coding: utf-8 -*-
"""LEAF REFINEMENT AGENT (owner request 2026-07-17): reviews per-product taxonomy-leaf
assignments and proposes a better leaf where the product's name/attributes clearly fit a
SIBLING or nearby node better (wine glass -> Stemware, not generic Drinkware).

Runs on the free chain (DASHSCOPE_OFF=1 recommended). Batches products that share an
assigned leaf; the model sees each product's name+attrs and the nearby-leaf options.
Confirms (no write) or overrides: product_taxonomy.source='agent_refined'.

  python leaf_refine.py [N]          # refine up to N products (default 200)
  python leaf_refine.py --status
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
STATE = HERE / "leaf_refine_state.json"

PROMPT = """Продуктите по-долу са класифицирани в Shopify категорията "{leaf}".
За ВСЕКИ продукт прецени: това ли е НАЙ-ТОЧНИЯТ лист, или някой от съседните пасва по-добре?
Съседни листа:
{siblings}

Продукти:
{items}

Върни САМО валиден JSON: {{"код": null_ако_е_вярно_или_номер_на_по-добър_съсед, ...}}."""


def _nodes():
    import yaml
    cats = json.load(open(HERE / "shopify_taxonomy" / "categories.json", encoding="utf-8"))
    bg = yaml.safe_load(open(HERE / "shopify_taxonomy" / "categories_bg.yml",
                             encoding="utf-8"))["bg-BG"]["categories"]
    node, kids = {}, {}
    for v in cats["verticals"]:
        for c in v["categories"]:
            node[c["id"]] = c
            kids.setdefault(c.get("parent_id"), []).append(c)
    def bgname(c):
        return (bg.get(c["id"].rsplit("/", 1)[-1]) or {}).get("name") or c["name"]
    return node, kids, bgname


def run(limit=200):
    import collections
    import db
    import run_one
    node, kids, bgname = _nodes()
    seen = set()
    if STATE.exists():
        try:
            seen = set(json.loads(STATE.read_text(encoding="utf-8")).get("seen", []))
        except Exception:
            pass
    con = db.connect()
    by_leaf = collections.defaultdict(list)
    rows = con.execute(
        "SELECT pt.code, pt.gid, p.fields_json FROM product_taxonomy pt "
        "JOIN products p ON p.code = pt.code WHERE pt.gid IS NOT NULL "
        "AND pt.source != 'agent_refined'").fetchall()
    for code, gid, fj in rows:
        if str(code) in seen or len(seen) + sum(len(v) for v in by_leaf.values()) >= limit + len(seen):
            continue
        try:
            f = json.loads(fj or "{}")
        except Exception:
            continue
        by_leaf[gid].append((str(code), str(f.get("Наименование") or "")[:70],
                             str(f.get("Атрибути") or "")[:120]))
    done = confirmed = moved = 0
    for gid, prods in by_leaf.items():
        cur = node.get(gid)
        if cur is None:
            continue
        sibs = [s for s in kids.get(cur.get("parent_id"), []) if s["id"] != gid][:14]
        if not sibs:
            for code, _n, _a in prods:
                seen.add(code)
            continue
        sib_lines = "\n".join(f"  {i}. {bgname(s)}  [{s['full_name']}]"
                              for i, s in enumerate(sibs))
        for i in range(0, len(prods), 12):
            chunk = prods[i:i + 12]
            items = "\n".join(f'  {c}: "{n}" ({a})' for c, n, a in chunk)
            try:
                out, model = run_one.generate_with_chain(
                    PROMPT.format(leaf=bgname(cur) + " [" + cur["full_name"] + "]",
                                  siblings=sib_lines, items=items),
                    system="Отговаряй само с валиден JSON.")
                data = run_one.extract_json(out) or {}
            except Exception as e:
                print(f"  LLM failed: {str(e)[:70]}", flush=True)
                continue
            for code, _n, _a in chunk:
                v = data.get(code, "missing")
                seen.add(code)
                done += 1
                if v is None or v == "missing":
                    confirmed += 1
                    continue
                try:
                    s = sibs[int(v)]
                except Exception:
                    continue
                con.execute("UPDATE product_taxonomy SET gid=?, full_name=?, "
                            "source='agent_refined' WHERE code=?",
                            (s["id"], s["full_name"], code))
                moved += 1
            con.commit()
            print(f"  [{done}] confirmed {confirmed} / moved {moved} ({model})", flush=True)
    con.close()
    STATE.write_text(json.dumps({"seen": sorted(seen)}), encoding="utf-8")
    print(f"DONE: {done} reviewed, {confirmed} confirmed, {moved} moved to better leaves")


if __name__ == "__main__":
    if "--status" in sys.argv:
        try:
            print(len(json.loads(STATE.read_text(encoding='utf-8'))["seen"]), "reviewed")
        except Exception:
            print("0 reviewed")
    else:
        n = next((int(a) for a in sys.argv[1:] if a.isdigit()), 200)
        run(n)
