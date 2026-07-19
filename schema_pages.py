# -*- coding: utf-8 -*-
"""SCHEMA PAGES for the review site (owner request 2026-07-17): visual editors for the
system's rule/vocabulary files, so conventions can be changed site-wide without touching
JSON by hand.

  /naming — the naming-convention editor: default template, per-type recipes (chips,
            drag to reorder), conditional overrides (seasonal renames, Ø etc.), type
            merge (raw mappings repoint; products follow automatically), re-render.
  /brands — brand gazetteer viewer/editor (add / delete entries).
  /schema — category filter-schema viewer (read-only v1).

All writes go through this module with a simple lock; names re-render only when the
owner clicks Пре-рендирай (spawns name_builder --apply detached, log tail shown).
"""
import html
import json
import re
import subprocess
import sys
import threading
import time
from pathlib import Path

_MUTEX = threading.Lock()   # serializes read-modify-write of the shared config files
                            # across the ThreadingHTTPServer request threads

HERE = Path(__file__).parent
RULES = HERE / "name_rules.json"
VOCAB = HERE / "name_vocab.json"
GAZ = HERE / "brand_gazetteer.jsonl"
RERENDER_LOG = HERE / "naming_rerender.log"
_LOCK = HERE / ".schema_pages.lock"

TOKENS = ["Бранд", "Материал:adj", "Форма:adj", "Тип", "Вариант", "Размер",
          "Обем", "Цвят", "Диаметър"]


def esc(s):
    return html.escape(str(s or ""))


def _locked_write(path, text):
    for _ in range(50):
        try:
            fd = _LOCK.open("x")
            break
        except FileExistsError:
            try:                                    # a crashed holder must not block forever
                if time.time() - _LOCK.stat().st_mtime > 60:
                    _LOCK.unlink(missing_ok=True)
                    continue
            except OSError:
                pass
            time.sleep(0.1)
    else:
        raise RuntimeError("schema lock busy")
    try:
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(text, encoding="utf-8")
        import os
        os.replace(tmp, path)
    finally:
        fd.close()
        _LOCK.unlink(missing_ok=True)


def load_rules():
    import name_builder
    return name_builder.load_rules()


def load_vocab():
    return json.loads(VOCAB.read_text(encoding="utf-8"))


# ------------------------------------------------------------------ data helpers ----
_type_cache = {"ts": 0, "data": None}


def type_stats():
    """{canon: {"count": N, "sample": (code, current, rendered)}} — cached 120s."""
    if _type_cache["data"] is not None and time.time() - _type_cache["ts"] < 120:
        return _type_cache["data"]
    import db
    import name_builder as nb
    vocab = load_vocab()
    rules = load_rules()
    out = {c: {"count": 0, "sample": None} for c in vocab.get("canon", {})}
    con = db.connect()
    try:
        for code, fj in con.execute("SELECT code, fields_json FROM products").fetchall():
            try:
                f = json.loads(fj or "{}")
            except Exception:
                continue
            attrs = nb._attrs(f)
            raw = attrs.get("тип", "").lower()
            hit = vocab["types"].get(raw)
            if not hit:
                continue
            canon = hit[0]
            d = out.setdefault(canon, {"count": 0, "sample": None})
            d["count"] += 1
            if d["sample"] is None:
                nm, _ = nb.build_name(f, vocab, rules)
                d["sample"] = (str(code), str(f.get("Наименование") or ""), nm or "")
    finally:
        con.close()
    _type_cache.update(ts=time.time(), data=out)
    return out


def _invalidate():
    _type_cache["data"] = None


# ------------------------------------------------------------------ POST actions ----
def handle_naming_post(data):
    """Dispatch for POST /api/naming. Returns a JSON-able dict."""
    with _MUTEX:
        return _handle_naming_post(data)


def _handle_naming_post(data):
    action = data.get("action")
    rules = load_rules()
    if action == "save_default":
        tpl = [str(t) for t in (data.get("template") or []) if str(t).strip()]
        if not tpl or "Тип" not in [t.split(":")[0] for t in tpl]:
            return {"error": "шаблонът трябва да съдържа Тип"}
        rules["default"] = tpl
    elif action == "save_type":
        t = str(data.get("type") or "").strip()
        if not t:
            return {"error": "няма тип"}
        tpl = data.get("template")
        rules.setdefault("types", {})
        if tpl:
            rules["types"][t] = [str(x) for x in tpl if str(x).strip()]
        else:
            rules["types"].pop(t, None)          # back to inheriting the default
    elif action == "toggle_override":
        i = int(data.get("idx"))
        rules["overrides"][i]["enabled"] = bool(data.get("enabled"))
    elif action == "del_override":
        i = int(data.get("idx"))
        rules["overrides"].pop(i)
    elif action == "add_override":
        when = {str(k): str(v) for k, v in (data.get("when") or {}).items()
                if str(k).strip() and str(v).strip()}
        if not when:
            return {"error": "правилото трябва да има поне едно условие (атрибут: стойност)"}
        ov = {"id": str(data.get("id") or f"правило-{int(time.time())}"),
              "enabled": True, "when": when}
        tpl = [str(t) for t in (data.get("template") or []) if str(t).strip()]
        if tpl:
            ov["template"] = tpl
        if str(data.get("size_prefix") or "").strip():
            ov["size_prefix"] = str(data["size_prefix"]).strip()
        if "template" not in ov and "size_prefix" not in ov:
            return {"error": "правилото трябва да променя нещо (шаблон или префикс на размера)"}
        rules.setdefault("overrides", []).append(ov)
    elif action == "merge_type":
        return merge_type(str(data.get("src") or ""), str(data.get("dst") or ""))
    elif action == "rerender":
        return start_rerender()
    else:
        return {"error": f"неизвестно действие {action}"}
    _locked_write(RULES, json.dumps(rules, ensure_ascii=False, indent=1))
    _invalidate()
    return {"ok": True}


def merge_type(src, dst):
    """Repoint every raw-type mapping from canon `src` to canon `dst` and drop `src`.
    Products keep their raw Тип attribute — rendering follows the mapping."""
    if not src or not dst or src == dst:
        return {"error": "избери различни типове"}
    vocab = load_vocab()
    if dst not in vocab.get("canon", {}):
        return {"error": f"'{dst}' не е съществуващ каноничен тип"}
    g = vocab["canon"][dst]
    n = 0
    for raw, cg in list(vocab["types"].items()):
        if cg[0] == src:
            vocab["types"][raw] = [dst, g]
            n += 1
    vocab["canon"].pop(src, None)
    _locked_write(VOCAB, json.dumps(vocab, ensure_ascii=False, indent=1))
    rules = load_rules()
    if (rules.get("types") or {}).pop(src, None) is not None:
        _locked_write(RULES, json.dumps(rules, ensure_ascii=False, indent=1))
    _invalidate()
    return {"ok": True, "repointed": n,
            "note": f"{n} суровi типа сега сочат към {dst}; пусни Пре-рендирай за имената"}


def _rerender_running():
    out = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process -Filter \"name='python.exe'\" | "
         "ForEach-Object { $_.CommandLine }"],
        capture_output=True, text=True).stdout or ""
    return "name_builder.py" in out


def start_rerender():
    if _rerender_running():
        return {"ok": True, "note": "пре-рендиране вече тече — изчакай го"}
    py = sys.executable
    with open(RERENDER_LOG, "w", encoding="utf-8") as log:
        log.write(f"started {time.strftime('%Y-%m-%dT%H:%M:%S')}\n")
    import os
    env = dict(os.environ); env["PYTHONIOENCODING"] = "utf-8"
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    subprocess.Popen([py, str(HERE / "name_builder.py"), "--apply"],
                     cwd=str(HERE), env=env, creationflags=flags,
                     stdout=open(RERENDER_LOG, "a", encoding="utf-8"),
                     stderr=subprocess.STDOUT)
    return {"ok": True, "note": "пре-рендирането тече — виж лога на страницата"}


def rerender_log_tail():
    try:
        lines = RERENDER_LOG.read_text(encoding="utf-8", errors="replace").splitlines()
        return {"log": "\n".join(lines[-6:])}
    except Exception:
        return {"log": ""}


def handle_brands_post(data):
    with _MUTEX:
        return _handle_brands_post(data)


def _handle_brands_post(data):
    action = data.get("action")
    if action == "add":
        name = str(data.get("name") or "").strip()
        if not name:
            return {"error": "празно име"}
        try:
            from run_one import SUPPLIER_NAMES
            if any(x in name.lower() for x in SUPPLIER_NAMES):
                return {"error": f"'{name}' е доставчик, не бранд"}
        except Exception:
            pass
        with open(GAZ, "a", encoding="utf-8") as f:
            f.write(json.dumps({"name": name, "variant": str(data.get("variant") or "") or None,
                                "source": "owner", "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                               ensure_ascii=False) + "\n")
        return {"ok": True}
    if action == "delete":
        name = str(data.get("name") or "")
        lines = GAZ.read_text(encoding="utf-8").splitlines()
        keep = []
        for ln in lines:
            try:
                if json.loads(ln).get("name") == name:
                    continue
            except Exception:
                pass
            keep.append(ln)
        _locked_write(GAZ, "\n".join(keep) + "\n")
        return {"ok": True, "removed": len(lines) - len(keep)}
    if action == "accept_candidate":
        cand = str(data.get("candidate") or "").strip()
        if not cand:
            return {"error": "празен кандидат"}
        try:
            from run_one import SUPPLIER_NAMES
            if any(x in cand.lower() for x in SUPPLIER_NAMES):
                return {"error": "'" + cand + "' е доставчик"}
        except Exception:
            pass
        with open(GAZ, "a", encoding="utf-8") as f:
            f.write(json.dumps({"name": cand, "variant": None,
                                "source": "owner_confirmed",
                                "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                               ensure_ascii=False) + chr(10))
        # re-stamp the queued products: set the brand + recompose the name
        applied = 0
        try:
            import db
            import json as _j
            from datetime import datetime as _dt
            import name_builder as nb
            codes = []
            for line in (HERE / "brand_candidates.jsonl").read_text(
                    encoding="utf-8", errors="replace").splitlines():
                try:
                    d2 = _j.loads(line)
                except Exception:
                    continue
                if str(d2.get("candidate") or "").strip().lower() == cand.lower():
                    codes.append(str(d2.get("code")))
            vocab = nb.load_vocab()
            con = db.connect()
            with open(HERE / "results.lanez_brandfix.jsonl", "a", encoding="utf-8") as fh:
                for c in dict.fromkeys(codes):
                    r = con.execute("SELECT record_json FROM products WHERE code=?",
                                    (c,)).fetchone()
                    if not r:
                        continue
                    rec = _j.loads(r[0])
                    fl = dict(rec.get("fields") or {})
                    fl["Бранд"] = cand
                    nm, _rs = nb.build_name(fl, vocab)
                    if nm:
                        fl["Наименование"] = nm
                    nd = dict(rec)
                    nd["fields"] = fl
                    nd["ts"] = _dt.now().isoformat(timespec="seconds")
                    meta = dict(nd.get("meta") or {})
                    meta["notes"] = list(meta.get("notes") or []) + ["v2", "brand_owner_confirmed"]
                    nd["meta"] = meta
                    fh.write(_j.dumps(nd, ensure_ascii=False) + chr(10))
                    db.record_version(nd)
                    applied += 1
            con.close()
        except Exception as e:
            return {"ok": True, "note": "в речника; re-stamp грешка: " + str(e)[:60]}
        return {"ok": True, "note": "в речника + приложен на " + str(applied) + " продукта"}
    if action == "reject_candidate":
        cand = str(data.get("candidate") or "").strip().lower()
        try:
            rej = set(json.loads((HERE / "brand_rejected.json").read_text(encoding="utf-8")))
        except Exception:
            rej = set()
        rej.add(cand)
        (HERE / "brand_rejected.json").write_text(
            json.dumps(sorted(rej), ensure_ascii=False), encoding="utf-8")
        return {"ok": True}
    return {"error": "неизвестно действие"}


# ------------------------------------------------------------------ pages -----------
_SHELL = """<!doctype html><html lang="bg"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>
:root {{ --cherry:#8c1d2f; --cream:#faf6ee; --vanilla:#fdf9f0; --honey:#e8d9b8; --line:#e5dcc8; --ok:#186034; }}
* {{ box-sizing:border-box; }}
body {{ font-family:Georgia,'Times New Roman',serif; background:var(--cream); color:#2a2118; margin:0; padding:1.2rem 2rem 4rem; }}
h1 {{ color:var(--cherry); font-size:1.5rem; }}
h2 {{ font-size:1.05rem; border-bottom:2px solid var(--honey); padding-bottom:.3rem; margin-top:2rem; }}
.nav a {{ color:var(--cherry); margin-right:1rem; font-size:.9rem; }}
table {{ border-collapse:collapse; width:100%; background:#fff; font-size:.85rem; }}
th,td {{ border:1px solid var(--line); padding:.4rem .6rem; text-align:left; vertical-align:top; }}
th {{ background:var(--vanilla); }}
.chiprow {{ display:flex; flex-wrap:wrap; gap:.3rem; min-height:2rem; padding:.3rem; background:var(--vanilla); border:1px dashed var(--honey); border-radius:8px; }}
.chip {{ background:#fff; border:1px solid var(--honey); border-radius:10px; padding:.2rem .55rem; font-size:.8rem; cursor:grab; user-select:none; }}
.chip.lit {{ background:#eef6ee; border-color:#bcd8bc; }}
.chip .x {{ color:#a12020; margin-left:.3rem; cursor:pointer; font-weight:700; }}
.chip.dragging {{ opacity:.4; }}
button {{ font:inherit; font-size:.8rem; padding:.3rem .8rem; border:1px solid var(--cherry); background:var(--cherry); color:#fff; border-radius:8px; cursor:pointer; }}
button.ghost {{ background:#fff; color:var(--cherry); }}
select,input[type=text] {{ font:inherit; font-size:.8rem; padding:.25rem; border:1px solid var(--line); border-radius:6px; }}
.preview {{ font-size:.8rem; color:#555; }} .preview b {{ color:var(--ok); }}
.muted {{ color:#8a7d68; font-size:.78rem; }}
.ovcard {{ background:#fff; border:1px solid var(--line); border-left:3px solid var(--cherry); border-radius:8px; padding:.6rem .8rem; margin:.5rem 0; font-size:.85rem; }}
.ovcard.off {{ opacity:.55; border-left-color:#aaa; }}
#log {{ background:#222; color:#cfc; font-family:Consolas,monospace; font-size:.75rem; padding:.6rem; border-radius:8px; white-space:pre-wrap; }}
.addrow {{ display:flex; gap:.4rem; flex-wrap:wrap; align-items:center; margin:.5rem 0; }}
</style></head><body>
<div class="nav"><a href="/">← Продукти</a><a href="/naming">Именуване</a><a href="/vocab">Типове</a><a href="/brands">Брандове</a><a href="/schema">Категории</a><a href="/lessons">Уроци</a><a href="/dupes">Дубликати</a><a href="/readiness">Готовност</a><a href="/ops">Обработка</a><a href="/help" style="font-weight:700">❓ Помощ</a></div>
<h1>{title}</h1>
{body}
<script>{js}</script></body></html>"""


def naming_page():
    rules = load_rules()
    stats = type_stats()
    vocab = load_vocab()
    canon = vocab.get("canon", {})

    def chiprow(tpl, rid, inherited=False):
        chips = "".join(
            f'<span class="chip{" lit" if str(t).startswith("lit:") else ""}" draggable="true" data-t="{esc(t)}">'
            f'{esc(t[4:] + " (текст)") if str(t).startswith("lit:") else esc(t)}<span class="x">×</span></span>'
            for t in tpl)
        cls = ' style="opacity:.55"' if inherited else ""
        addsel = ('<select class="addtok"><option value="">+ добави…</option>'
                  + "".join(f'<option>{esc(t)}</option>' for t in TOKENS)
                  + '<option value="lit:">свободен текст…</option></select>')
        return f'<div class="chiprow" id="{rid}"{cls}>{chips}</div><div class="addrow">{addsel}</div>'

    # per-type rows
    rows = []
    typed = rules.get("types") or {}
    for c in sorted(canon, key=lambda x: -(stats.get(x, {}).get("count", 0))):
        st = stats.get(c) or {}
        n = st.get("count", 0)
        smp = st.get("sample")
        prev = f'<div class="preview">напр. <b>{esc(smp[2])}</b><br><span class="muted">{esc(smp[0])}: сега „{esc(smp[1])}“</span></div>' if smp else '<span class="muted">няма продукти</span>'
        own = typed.get(c)
        merge = ('<select class="mergesel"><option value="">слей в…</option>'
                 + "".join(f'<option>{esc(x)}</option>' for x in sorted(canon) if x != c)
                 + '</select>')
        body = chiprow(own or rules.get("default") or [], f"t-{esc(c)}", inherited=not own)
        tag = '' if own else '<span class="muted">(наследен шаблон — влачи чип за да персонализираш)</span>'
        rows.append(f'<tr data-type="{esc(c)}"><td><b>{esc(c)}</b> <span class="muted">({canon[c]}, {n} прод.)</span><br>{merge}</td>'
                    f'<td>{body}{tag}<div class="addrow"><button onclick="saveType(this)">Запази</button>'
                    f'{"<button class=ghost onclick=resetType(this)>← наследи default</button>" if own else ""}</td>'
                    f'<td>{prev}</td></tr>')

    # overrides
    ovs = []
    for i, ov in enumerate(rules.get("overrides") or []):
        when = "; ".join(f"{k} = {v}" for k, v in (ov.get("when") or {}).items())
        what = (f'шаблон: {" + ".join(ov.get("template", []))}' if ov.get("template") else "") + \
               (f' размер с префикс „{ov.get("size_prefix")}“' if ov.get("size_prefix") else "")
        on = ov.get("enabled", True)
        ovs.append(f'<div class="ovcard{"" if on else " off"}"><b>{esc(ov.get("id") or f"правило {i}")}</b> — когато {esc(when)} → {esc(what)}<br>'
                   f'<label><input type="checkbox" {"checked" if on else ""} onchange="toggleOv({i}, this.checked)"> активно</label> '
                   f'<button class="ghost" onclick="delOv({i})">изтрий</button></div>')

    body = f"""
<p class="muted">Имената се РЕНДВАТ от атрибутите по тези правила. Промениш ли нещо — натисни
<b>Пре-рендирай</b>: всички продукти (без ръчно одобрените/редактираните) получават новите имена,
всяка промяна се вижда като диф на картата. Връщането на правило + пре-рендиране връща и имената.</p>
<button onclick="rerender()">⟳ Пре-рендирай имената</button> <span id="rr" class="muted"></span>
<div id="log"></div>

<h2>Основен шаблон (важи за всички типове без собствена рецепта)</h2>
{chiprow(rules.get("default") or [], "t-default")}
<div class="addrow"><button onclick="saveDefault()">Запази основния шаблон</button></div>

<h2>Правила по условие (сезонни, Ø и др.)</h2>
{"".join(ovs) or '<p class="muted">няма</p>'}
<div class="addrow">
 <input type="text" id="ov-id" placeholder="име на правилото">
 <input type="text" id="ov-when" placeholder="условия: Тип=Тенджера; Цвят=розов" size="34">
 <input type="text" id="ov-tpl" placeholder="шаблон: lit:Свети Валентинска + Тип + Размер" size="40">
 <input type="text" id="ov-pre" placeholder="префикс размер (Ø)" size="14">
 <button onclick="addOv()">Добави правило</button>
</div>

<h2>Типове продукти ({len(canon)}) — рецепта на ред</h2>
<table><tr><th style="width:16rem">Тип</th><th>Рецепта</th><th style="width:22rem">Преглед</th></tr>{"".join(rows)}</table>
"""
    js = """
let dragEl=null;
document.addEventListener('dragstart',e=>{if(e.target.classList?.contains('chip')){dragEl=e.target;e.target.classList.add('dragging');}});
document.addEventListener('dragend',e=>{if(dragEl){dragEl.classList.remove('dragging');dragEl=null;}});
document.addEventListener('dragover',e=>{
  const row=e.target.closest('.chiprow'); if(!row||!dragEl||dragEl.parentElement!==row) return;
  e.preventDefault();
  const after=[...row.querySelectorAll('.chip:not(.dragging)')].find(c=>e.clientX < c.getBoundingClientRect().left + c.offsetWidth/2);
  if(after) row.insertBefore(dragEl, after); else row.appendChild(dragEl);
});
document.addEventListener('click',e=>{if(e.target.classList?.contains('x')) e.target.parentElement.remove();});
document.addEventListener('change',e=>{
  if(!e.target.classList?.contains('addtok')) return;
  let v=e.target.value; if(!v) return;
  if(v==='lit:'){const t=prompt('Свободен текст в името:'); if(!t){e.target.value='';return;} v='lit:'+t;}
  const row=e.target.closest('td, body').querySelector('.chiprow') || e.target.parentElement.previousElementSibling;
  const ch=document.createElement('span'); ch.className='chip'+(v.startsWith('lit:')?' lit':''); ch.draggable=true; ch.dataset.t=v;
  ch.innerHTML=(v.startsWith('lit:')?v.slice(4)+' (текст)':v)+'<span class="x">×</span>';
  row.appendChild(ch); row.style.opacity='1'; e.target.value='';
});
function tokens(rowId){return [...document.getElementById(rowId).querySelectorAll('.chip')].map(c=>c.dataset.t);}
async function api(body){const r=await fetch('/api/naming',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});const d=await r.json();if(d.error)alert(d.error);return d;}
async function saveDefault(){if((await api({action:'save_default',template:tokens('t-default')})).ok) location.reload();}
async function saveType(btn){const tr=btn.closest('tr'); const t=tr.dataset.type;
  if((await api({action:'save_type',type:t,template:[...tr.querySelectorAll('.chip')].map(c=>c.dataset.t)})).ok) location.reload();}
async function resetType(btn){const t=btn.closest('tr').dataset.type;
  if((await api({action:'save_type',type:t,template:null})).ok) location.reload();}
async function toggleOv(i,on){await api({action:'toggle_override',idx:i,enabled:on}); location.reload();}
async function delOv(i){if(confirm('Изтриване на правилото?')&&(await api({action:'del_override',idx:i})).ok) location.reload();}
async function addOv(){
  const when={}; document.getElementById('ov-when').value.split(';').forEach(p=>{const m=p.split('='); if(m.length===2) when[m[0].trim()]=m[1].trim();});
  const tpl=document.getElementById('ov-tpl').value.split('+').map(s=>s.trim()).filter(Boolean);
  const d=await api({action:'add_override',id:document.getElementById('ov-id').value,when,template:tpl,size_prefix:document.getElementById('ov-pre').value});
  if(d.ok) location.reload();}
document.querySelectorAll('.mergesel').forEach(s=>s.addEventListener('change',async e=>{
  const src=e.target.closest('tr').dataset.type, dst=e.target.value; if(!dst) return;
  if(confirm('Сливане на "'+src+'" в "'+dst+'"? Продуктите ще се пренасочат.')){
    const d=await api({action:'merge_type',src,dst}); if(d.ok){alert(d.note); location.reload();}
  } else e.target.value='';
}));
async function rerender(){const d=await api({action:'rerender'}); document.getElementById('rr').textContent=d.note||''; pollLog();}
async function pollLog(){const r=await fetch('/api/naming/log'); const d=await r.json();
  document.getElementById('log').textContent=d.log||'';
  const done=(d.log||'').includes('applied')||(d.log||'').includes('Traceback')||(d.log||'').includes('Error');
  if(!done) setTimeout(pollLog, 3000);}
"""
    return _SHELL.format(title="Именуване — правила и типове", body=body, js=js)


def _brand_usage():
    """{canonical-brand-lower: count} from the live catalog (cached 300s)."""
    import time as _t
    if _schema_cache.get("brand_counts") is not None and \
            _t.time() - _schema_cache.get("brand_ts", 0) < 300:
        return _schema_cache["brand_counts"]
    import db
    import json as _j
    import collections
    counts = collections.Counter()
    con = db.connect()
    try:
        for (fj,) in con.execute("SELECT fields_json FROM products").fetchall():
            try:
                b = str(_j.loads(fj or "{}").get("Бранд") or "").strip()
            except Exception:
                continue
            if b:
                counts[b.lower()] += 1
    finally:
        con.close()
    _schema_cache["brand_counts"] = counts
    _schema_cache["brand_ts"] = _t.time()
    return counts


def _brand_queue():
    """Pending candidates grouped by candidate string, minus rejected ones."""
    import json as _j
    rej = set()
    try:
        rej = set(_j.loads((HERE / "brand_rejected.json").read_text(encoding="utf-8")))
    except Exception:
        pass
    groups = {}
    try:
        for line in (HERE / "brand_candidates.jsonl").read_text(
                encoding="utf-8", errors="replace").splitlines():
            try:
                d = _j.loads(line)
            except Exception:
                continue
            cand = str(d.get("candidate") or "").strip()
            if not cand or cand.lower() in rej:
                continue
            g = groups.setdefault(cand, {"codes": [], "sources": set(), "stoka": []})
            if d.get("code") not in g["codes"]:
                g["codes"].append(d.get("code"))
                g["stoka"].append(str(d.get("stoka") or "")[:60])
            g["sources"].update(d.get("sources") or [])
    except FileNotFoundError:
        pass
    return groups


def brands_page():
    entries = {}
    try:
        for ln in GAZ.read_text(encoding="utf-8").splitlines():
            try:
                e = json.loads(ln)
            except Exception:
                continue
            d = entries.setdefault(e.get("name"), {"variants": set(), "sources": set()})
            if e.get("variant"):
                d["variants"].add(e["variant"])
            d["sources"].add(e.get("source") or "?")
    except FileNotFoundError:
        pass
    usage = _brand_usage()
    queue = _brand_queue()

    qcards = []
    for cand, g in sorted(queue.items(), key=lambda kv: -len(kv[1]["codes"])):
        prods = "".join(
            '<div style="display:flex;align-items:center;gap:.4rem;margin:.15rem 0">'
            '<img loading="lazy" src="/thumb?code=' + esc(c) + '" '
            'style="width:34px;height:34px;object-fit:contain;background:var(--vanilla);'
            'border-radius:5px" onerror="this.remove()">'
            '<a href="/rows?code=' + esc(c) + '" target="_blank"><b>' + esc(c) + '</b></a> '
            '<span class="muted">' + esc(st) + "</span></div>"
            for c, st in list(zip(g["codes"], g["stoka"]))[:5])
        more = ("<span class='muted'>и още " + str(len(g["codes"]) - 5) + "…</span>"
                if len(g["codes"]) > 5 else "")
        qcards.append(
            '<div class="ovcard" id="bq-' + esc(cand) + '"><b>' + esc(cand) + "</b> "
            '<span class="muted">(' + str(len(g["codes"])) + ' прод. · източник: '
            + esc(", ".join(sorted(g["sources"])) or "?") + ")</span>" + prods + more
            + '<div style="margin-top:.35rem">'
            '<button onclick="bqAccept(' + esc(json.dumps(cand, ensure_ascii=False))
            + ')">✓ Истинска марка</button> '
            '<button class="ghost" onclick="bqReject(' + esc(json.dumps(cand, ensure_ascii=False))
            + ')">✗ Не е марка</button></div></div>')

    rows = []
    for n, d in sorted(entries.items(), key=lambda kv: kv[0].lower()):
        cnt = usage.get(n.lower(), 0)
        warn = ' <span style="color:#a12020" title="употребен от ≤1 продукт — провери">⚠</span>'                if cnt <= 1 else ""
        rows.append(
            "<tr><td><b>" + esc(n) + "</b>" + warn + "</td>"
            "<td>" + str(cnt) + "</td>"
            "<td>" + esc(", ".join(sorted(d["variants"]))) + "</td>"
            '<td class="muted">' + esc(", ".join(sorted(d["sources"]))) + "</td>"
            '<td><button class="ghost" onclick="delBrand(' + json.dumps(n, ensure_ascii=False)
            + ')">изтрий</button></td></tr>')

    body = ('<p class="muted">' + str(len(entries)) + " канонични бранда. ⚠ = употребен от "
            "≤1 продукт (кандидат за проверка). Кандидатите долу са открити от само един "
            "източник — нищо не влиза в речника без твоето „Истинска марка“.</p>"
            + ("<h2>Чакащи кандидати (" + str(len(queue)) + ")</h2>" + "".join(qcards)
               if queue else "")
            + '<h2>Речник</h2>'
            '<div class="addrow"><input type="text" id="b-name" placeholder="каноничен бранд">'
            '<input type="text" id="b-var" placeholder="вариант/изписване (по избор)">'
            '<button onclick="addBrand()">Добави</button></div>'
            '<table><tr><th>Бранд</th><th>Прод.</th><th>Варианти</th><th>Източник</th><th></th></tr>'
            + "".join(rows) + "</table>")
    js = """
async function api(b){const r=await fetch('/api/brands',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});const d=await r.json();if(d.error)alert(d.error);return d;}
async function addBrand(){const d=await api({action:'add',name:document.getElementById('b-name').value,variant:document.getElementById('b-var').value}); if(d.ok) location.reload();}
async function delBrand(n){if(confirm('Изтриване на "'+n+'" от речника?')&&(await api({action:'delete',name:n})).ok) location.reload();}
async function bqAccept(c){const d=await api({action:'accept_candidate',candidate:c}); if(d.ok){alert(d.note||'Прието'); location.reload();}}
async function bqReject(c){const d=await api({action:'reject_candidate',candidate:c}); if(d.ok) location.reload();}
"""
    return _SHELL.format(title="Брандове — речник", body=body, js=js)



_schema_cache = {"ts": 0, "counts": None}


def _category_counts():
    """{category-name-fragment: product count} from the products' Категории field, cached."""
    import time as _t
    if _schema_cache["counts"] is not None and _t.time() - _schema_cache["ts"] < 300:
        return _schema_cache["counts"]
    import db
    import json as _j
    import collections
    counts = collections.Counter()
    con = db.connect()
    try:
        for (fj,) in con.execute("SELECT fields_json FROM products").fetchall():
            try:
                v = _j.loads(fj or "{}").get("Категории") or ""
            except Exception:
                continue
            for part in str(v).replace(">", ",").split(","):
                p = part.strip()
                if p:
                    counts[p] += 1
    finally:
        con.close()
    _schema_cache.update(ts=_t.time(), counts=counts)
    return counts


_taxattr_cache = {"data": None}


def _shopify_attr_names():
    """{our-category-key: set(normalized Shopify attribute names for its mapped node)} —
    used to mark groups that exist in BOTH our schema and the taxonomy."""
    if _taxattr_cache["data"] is not None:
        return _taxattr_cache["data"]
    out = {}
    try:
        import json as _j
        import shopify_schema_align as ssa
        by_gid, attr_def, bg_name_for, _bgv = ssa.load_taxonomy()
        catmap = _j.load(open(HERE / "category_shopify_map.json", encoding="utf-8"))
        import filter_schema_store as fss
        schema = fss.load()
        key_ix = {}
        for k in schema:
            key_ix.setdefault(ssa._norm(k), []).append(k)
            key_ix.setdefault(ssa._norm(str(k).split("->")[-1]), []).append(k)
        for m in catmap:
            bg, gid = m.get("bg"), m.get("shopify_id")
            if not bg or not gid:
                continue
            names = set()
            for ta in (by_gid.get(gid) or []):
                h = ta.get("handle") or ""
                names.add(ssa._norm(bg_name_for(h, ta.get("name") or h)))
            for skey in set(key_ix.get(ssa._norm(bg)) or []):
                out.setdefault(skey, set()).update(names)
    except Exception:
        pass
    _taxattr_cache["data"] = out
    return out


def schema_page(q=""):
    try:
        import filter_schema_store as fss
        cats = fss.load()
    except Exception as e:
        return _SHELL.format(title="Категории", body="<p>грешка: " + esc(e) + "</p>", js="")
    import json as _j
    import re as _re
    try:
        smap = {m["bg"]: m.get("shopify_category") or ""
                for m in _j.load(open(HERE / "category_shopify_map.json", encoding="utf-8"))}
    except Exception:
        smap = {}
    counts = _category_counts()
    taxnames = _shopify_attr_names()

    tot_groups = shop_groups = 0
    cards = []
    for cat in sorted(cats, key=str):
        groups = cats[cat] if isinstance(cats[cat], list) else []
        leaf = str(cat).split("->")[-1].strip()
        root = str(cat).split("->")[0].strip()
        n_prod = max(counts.get(leaf, 0), counts.get(str(cat), 0))
        snode = smap.get(leaf) or smap.get(root) or ""
        chips = []
        for gi, g in enumerate(groups):
            if not isinstance(g, dict):
                continue
            tot_groups += 1
            is_shop = g.get("източник") == "shopify_taxonomy"
            if is_shop:
                shop_groups += 1
            gn = _re.sub(r"[^0-9a-zа-я]", "", str(g.get("група") or "").lower())
            is_both = (not is_shop) and gn in (taxnames.get(cat) or ())
            vals = [v.strip() for v in str(g.get("стойности") or "").split(",") if v.strip()]
            tags = "".join('<span class="vtag">' + esc(v) + "</span>" for v in vals)
            cls = " shop" if is_shop else (" both" if is_both else "")
            tip = ' title="има я и в Shopify таксономията"' if is_both else ""
            chips.append(
                '<div class="fchip' + cls + '" onclick="tgl(this)"' + tip + ">"
                + esc(g.get("група")) + ' <span class="vc">' + str(len(vals)) + "</span>"
                + '<div class="vals">' + tags + "</div></div>")
        cards.append(
            '<div class="scard" data-t="' + esc(str(cat).lower()) + '">'
            '<div class="schead"><b>' + esc(cat) + "</b>"
            + ('<span class="pcount">' + str(n_prod) + " прод.</span>" if n_prod else "")
            + "</div>"
            + ('<div class="snode">→ Shopify: ' + esc(snode) + "</div>" if snode else
               '<div class="snode none">без Shopify съответствие (наследява от родителя)</div>')
            + '<div class="fchips">' + "".join(chips) + "</div></div>")

    body = ("""
<style>
 .scard{background:#fff;border:1px solid var(--line);border-radius:10px;padding:.7rem .9rem;margin:.6rem 0;}
 .schead{display:flex;justify-content:space-between;align-items:baseline;font-size:.95rem;}
 .pcount{font-size:.72rem;color:#8a7d68;}
 .snode{font-size:.7rem;color:#5a7f5a;margin:.15rem 0 .4rem;}
 .snode.none{color:#a5977f;font-style:italic;}
 .fchips{display:flex;flex-wrap:wrap;gap:.35rem;}
 .fchip{background:var(--vanilla);border:1px solid var(--honey);border-radius:10px;padding:.2rem .6rem;font-size:.78rem;cursor:pointer;}
 .fchip.shop{background:#eef2fb;border-color:#b8c6e8;color:#2c4a8a;}
 .fchip .vc{font-size:.64rem;color:#8a7d68;background:#fff;border-radius:8px;padding:0 .3rem;margin-left:.15rem;}
 .fchip .vals{display:flex;flex-wrap:wrap;gap:.25rem;margin-top:.35rem;}
 .fchip.closed .vals{display:none;}
 .fchip.both{background:linear-gradient(90deg,var(--vanilla) 50%,#eef2fb 50%);border-color:#b8a06a;}
 .vtag{background:#fff;border:1px solid var(--line);border-radius:7px;padding:.06rem .4rem;font-size:.68rem;color:#5a4a3a;}
 .legend{display:flex;gap:1rem;font-size:.76rem;margin:.4rem 0;}
 .legend span{display:inline-flex;align-items:center;gap:.3rem;}
 .dot{width:.7rem;height:.7rem;border-radius:3px;display:inline-block;}
 #q{font:inherit;font-size:.85rem;padding:.35rem .6rem;border:1px solid var(--line);border-radius:8px;width:20rem;}
</style>
<p class="muted">Категориите са НАШИТЕ (от оригиналния сайт и касата) — всяка е СЪОТНЕСЕНА към
възел от официалната Shopify таксономия (зеления ред). Групите с атрибути са смесица:
кехлибарените са наши (от твоя Excel + доуточнени от curator-а по реалните продукти), сините
са добавени от стандартните Shopify атрибути за съответния възел — само там, където ние
нямахме такава група; нашите никога не се презаписват. <b>Кликни група</b>, за да видиш стойностите ѝ
(те са и опциите на филтъра в магазина).</p>
<div class="legend">
 <span><span class="dot" style="background:var(--vanilla);border:1px solid var(--honey)"></span> наши групи ("""
            + str(tot_groups - shop_groups) + """)</span>
 <span><span class="dot" style="background:#eef2fb;border:1px solid #b8c6e8"></span> от Shopify таксономията ("""
            + str(shop_groups) + """)</span>
 <span><span class="dot" style="background:linear-gradient(90deg,var(--vanilla) 50%,#eef2fb 50%);border:1px solid #b8a06a"></span> и наша, и в Shopify</span>
 <span class="muted">""" + str(len(cats)) + """ категории · """ + str(tot_groups) + """ групи</span>
</div>
<input id="q" type="text" placeholder="търси категория или група…" oninput="filt(this.value)">
""" + "".join(cards))
    js = ("function tgl(c){c.classList.toggle('closed');}\n"
          "function filt(v){v=v.toLowerCase();document.querySelectorAll('.scard').forEach(c=>{"
          "c.style.display=(c.dataset.t.includes(v)||c.textContent.toLowerCase().includes(v))?'':'none';});}")
    return _SHELL.format(title="Категории и филтърни групи", body=body, js=js)
