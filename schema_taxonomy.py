# -*- coding: utf-8 -*-
"""HIDDEN page /taxonomy — the official Shopify product taxonomy as a collapsible tree,
scoped to the verticals our catalog maps into, with OUR categories pinned onto their
mapped nodes. Not linked from the navigation (owner request: a temporary reference view).
Official public explorer: https://shopify.github.io/product-taxonomy/"""
import json

from schema_pages import HERE, _SHELL, esc

_cache = {"html": None}


def taxonomy_page():
    if _cache["html"] is not None:
        return _cache["html"]
    cats = json.load(open(HERE / "shopify_taxonomy" / "categories.json", encoding="utf-8"))
    try:
        cmap = json.load(open(HERE / "category_shopify_map.json", encoding="utf-8"))
    except Exception:
        cmap = []
    ours_by_gid = {}
    for m in cmap:
        if m.get("shopify_id"):
            ours_by_gid.setdefault(m["shopify_id"], []).append(m.get("bg") or "")

    used_verticals = {(m.get("shopify_category") or "").split(" > ")[0] for m in cmap}
    used_verticals.discard("")

    total = mapped_nodes = 0
    vert_html = []
    for v in cats["verticals"]:
        if v["name"] not in used_verticals:
            continue
        by_parent = {}
        for c in v["categories"]:
            by_parent.setdefault(c.get("parent_id"), []).append(c)
        roots = [c for c in v["categories"] if c.get("level") == 0]

        def render(node, depth):
            nonlocal total, mapped_nodes
            total += 1
            kids = sorted(by_parent.get(node["id"], []), key=lambda x: x.get("name") or "")
            ours = ours_by_gid.get(node["id"]) or []
            if ours:
                mapped_nodes += 1
            n_attr = len(node.get("attributes") or [])
            pin = "".join('<span class="ourpin">◀ ' + esc(b) + "</span>" for b in ours)
            attr_badge = ('<span class="abadge">' + str(n_attr) + " атр.</span>") if n_attr else ""
            label = ('<span class="tnode' + (" mapped" if ours else "") + '">'
                     + esc(node.get("name")) + " " + attr_badge + pin + "</span>")
            if not kids:
                return '<li>' + label + "</li>"
            inner = "".join(render(k, depth + 1) for k in kids)
            return ('<li><details' + (" open" if depth < 1 or ours else "") + ">"
                    "<summary>" + label + ' <span class="kc">' + str(len(kids))
                    + "</span></summary><ul>" + inner + "</ul></details></li>")

        body_v = "".join(render(r, 0) for r in sorted(roots, key=lambda x: x.get("name") or ""))
        vert_html.append('<ul class="ttree">' + body_v + "</ul>")

    body = ("""
<style>
 .ttree{list-style:none;padding-left:0;font-size:.85rem;}
 .ttree ul{list-style:none;padding-left:1.3rem;border-left:1px dotted var(--honey);margin:.15rem 0;}
 .ttree li{margin:.12rem 0;}
 .ttree summary{cursor:pointer;list-style:none;}
 .ttree summary::before{content:'▸ ';color:#b98a2e;font-size:.75rem;}
 .ttree details[open]>summary::before{content:'▾ ';}
 .tnode.mapped{background:#eef8ee;border:1px solid #b5d9b5;border-radius:6px;padding:.05rem .4rem;}
 .ourpin{background:var(--cherry);color:#fff;border-radius:6px;padding:.04rem .4rem;font-size:.68rem;margin-left:.35rem;}
 .abadge{color:#2c4a8a;background:#eef2fb;border-radius:6px;padding:0 .3rem;font-size:.66rem;}
 .kc{color:#8a7d68;font-size:.68rem;}
 #tq{font:inherit;font-size:.85rem;padding:.35rem .6rem;border:1px solid var(--line);border-radius:8px;width:22rem;}
</style>
<p class="muted">Официалната Shopify таксономия (версията, която ползваме локално), само
върху вертикалите, в които попада нашият каталог. <b>Зелените възли</b> са тези, към които
сме съотнесли наша категория — червеният етикет показва коя. Синият брояч е колко
стандартни атрибута дефинира Shopify за възела. Пълният официален браузър:
<a href="https://shopify.github.io/product-taxonomy/" target="_blank">shopify.github.io/product-taxonomy ↗</a></p>
<p class="muted">Възли: """ + str(total) + " · с наша категория: " + str(mapped_nodes) + """ ·
страницата не е в менюто (временна справка).</p>
<input id="tq" type="text" placeholder="търси възел…" oninput="tfilt(this.value)">
""" + "".join(vert_html))
    js = ("function tfilt(v){v=v.toLowerCase();"
          "document.querySelectorAll('.ttree li').forEach(li=>{"
          "const hit=!v||li.textContent.toLowerCase().includes(v);"
          "li.style.display=hit?'':'none';"
          "if(hit&&v){let p=li.parentElement;while(p&&p.closest){const d=p.closest('details');"
          "if(!d)break;d.open=true;d.parentElement.style.display='';p=d.parentElement;}}});}")
    _cache["html"] = _SHELL.format(title="Shopify таксономия (справка)", body=body, js=js)
    return _cache["html"]
