# -*- coding: utf-8 -*-
"""HIDDEN page /menu — proposed storefront menu under the Shopify taxonomy, per the
owner's shelf design: display at parent level, leaves become filters. A shelf is the
deepest node whose product count >= threshold (?min=30); its descendants collapse into
it and are listed as the shelf's filter values. Uses product_taxonomy assignments."""
import json

from schema_pages import HERE, _SHELL, esc


def _bg_names():
    import yaml
    bg = yaml.safe_load(open(HERE / "shopify_taxonomy" / "categories_bg.yml",
                             encoding="utf-8"))["bg-BG"]["categories"]
    return {k: v.get("name") for k, v in bg.items()}


def menu_page(minprod=30):
    import db
    cats = json.load(open(HERE / "shopify_taxonomy" / "categories.json", encoding="utf-8"))
    bg = _bg_names()
    con = db.connect()
    try:
        rows = con.execute("SELECT gid, COUNT(*) FROM product_taxonomy "
                           "WHERE gid IS NOT NULL GROUP BY gid").fetchall()
        n_un = con.execute("SELECT COUNT(*) FROM product_taxonomy WHERE gid IS NULL").fetchone()[0]
    except Exception:
        rows, n_un = [], 0
    finally:
        con.close()
    direct = {g: n for g, n in rows}

    # build node index + cumulative counts up the tree
    node = {}
    for v in cats["verticals"]:
        for c in v["categories"]:
            node[c["id"]] = c
    cum = {}
    for gid, n in direct.items():
        cur = node.get(gid)
        while cur is not None:
            cum[cur["id"]] = cum.get(cur["id"], 0) + n
            cur = node.get(cur.get("parent_id"))

    def bgname(c):
        return bg.get(c["id"].rsplit("/", 1)[-1]) or c["name"]

    kids_ix = {}
    for c in node.values():
        kids_ix.setdefault(c.get("parent_id"), []).append(c)

    shelves = []

    def walk(c, path):
        total = cum.get(c["id"], 0)
        if total == 0:
            return
        kids = [k for k in kids_ix.get(c["id"], []) if cum.get(k["id"], 0) > 0]
        big_kids = [k for k in kids if cum.get(k["id"], 0) >= minprod]
        if big_kids and total >= minprod:
            # keep splitting: recurse into big children; small siblings roll into a shelf
            small = [k for k in kids if k not in big_kids]
            rest = sum(cum.get(k["id"], 0) for k in small) + direct.get(c["id"], 0)
            if rest > 0:
                shelves.append((path + [bgname(c)], rest,
                                sorted(bgname(k) for k in small)))
            for k in big_kids:
                walk(k, path + [bgname(c)])
        else:
            shelves.append((path + [bgname(c)], total,
                            sorted(bgname(k) for k in kids)))

    for v in cats["verticals"]:
        for c in v["categories"]:
            if c.get("level") == 0:
                walk(c, [])

    shelves.sort(key=lambda s: (-s[1], " > ".join(s[0])))
    rows_html = []
    for path, n, filters in shelves:
        crumb = " › ".join(esc(p) for p in path[:-1])
        f_html = ("".join('<span class="fpill">' + esc(f) + "</span>" for f in filters)
                  or '<span class="muted">— (листов рафт)</span>')
        rows_html.append(
            '<div class="shelf"><div class="shead"><b>' + esc(path[-1]) + "</b>"
            + '<span class="scount">' + str(n) + " прод.</span></div>"
            + ('<div class="scrumb">' + crumb + "</div>" if crumb else "")
            + '<div class="sfilters-row">' + f_html + "</div></div>")

    body = ("""
<style>
 .shelf{background:#fff;border:1px solid var(--line);border-radius:10px;padding:.6rem .9rem;margin:.5rem 0;}
 .shead{display:flex;justify-content:space-between;align-items:baseline;font-size:.95rem;}
 .scount{font-size:.74rem;color:var(--cherry);font-weight:700;}
 .scrumb{font-size:.68rem;color:#8a7d68;}
 .sfilters-row{display:flex;flex-wrap:wrap;gap:.3rem;margin-top:.35rem;}
 .fpill{background:var(--vanilla);border:1px solid var(--honey);border-radius:9px;padding:.12rem .5rem;font-size:.72rem;}
</style>
<p class="muted">ПРЕДЛОЖЕНИЕ за менюто на магазина по Shopify дървото (скрита страница).
Всеки блок е РАФТ (колекция) — показва се на едно ниво, а изброените под него листа стават
ФИЛТРИ на страницата му, точно по твоя дизайн. Праг за самостоятелен рафт:
<b>""" + str(minprod) + """ продукта</b> (смени с ?min=50 в адреса). Продукти без възел: """
            + str(n_un) + """. Броят расте с обработката — прегледай отново след като всичко мине.</p>
""" + "".join(rows_html))
    return _SHELL.format(title="Меню по Shopify таксономията (чернова)", body=body, js="")
