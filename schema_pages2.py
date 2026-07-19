# -*- coding: utf-8 -*-
"""SCHEMA PAGES part 2 (owner request 2026-07-17): lessons / readiness / dupes / vocab /
ops dashboards. Shares the shell + helpers with schema_pages.py."""
import json
import re
import subprocess
import sys
import time

from schema_pages import (HERE, VOCAB, _SHELL, _MUTEX, esc, load_vocab,
                          _locked_write, _invalidate)

LESSONS_MD = HERE / "edit_lessons.md"
OWNER_RULES = HERE / "owner_style_rules.md"
LESSONS_APPLIED = HERE / "edit_lessons_applied.json"
DUP_DISMISSED = HERE / "dup_dismissed.json"


def _nav_shell(title, body, js=""):
    return _SHELL.format(title=title, body=body, js=js)


def _parse_lessons():
    out = []
    try:
        txt = LESSONS_MD.read_text(encoding="utf-8")
    except FileNotFoundError:
        return out
    pat = (r"- \*\*(.+?)\*\* \[(.+?)\]\n  - защо: (.*?)\n  - доказателство: (.*?)"
           r"\n  - предложение: (.*?)(?:\n(?=[-#\n])|$)")
    for m in re.finditer(pat, txt, re.S):
        out.append({"rule": m.group(1).strip(), "conf": m.group(2).strip(),
                    "why": m.group(3).strip(), "evidence": m.group(4).strip(),
                    "suggestion": m.group(5).strip()})
    return out


def lessons_page():
    applied = set()
    try:
        applied = set(json.loads(LESSONS_APPLIED.read_text(encoding="utf-8")))
    except Exception:
        pass
    cards = []
    for r in _parse_lessons():
        done = r["rule"] in applied
        btn = ('<span class="muted">✓ приложено в инструкциите</span>' if done else
               '<button onclick="applyRule(' + esc(json.dumps(r["rule"], ensure_ascii=False))
               + ', ' + esc(json.dumps(r["suggestion"], ensure_ascii=False))
               + ')">Приложи в инструкциите</button>')
        cls = " off" if done else ""
        cards.append('<div class="ovcard' + cls + '"><b>' + esc(r["rule"]) + '</b> '
                     '<span class="muted">[' + esc(r["conf"]) + ']</span><br>'
                     '<span class="muted">защо:</span> ' + esc(r["why"]) + '<br>'
                     '<span class="muted">доказателство:</span> ' + esc(r["evidence"]) + '<br>'
                     '<span class="muted">предложение:</span> ' + esc(r["suggestion"]) + '<br>' + btn + '</div>')
    own = ""
    try:
        own = OWNER_RULES.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    body = ('<p class="muted">Правила, изведени от ТВОИТЕ редакции (edit_lessons.py ги добавя '
            'при всяка проверка). „Приложи“ добавя правилото към инструкциите на обработващите '
            'агенти — важи за всяка следваща обработка.</p>'
            + ("".join(cards) or '<p class="muted">още няма изведени правила</p>')
            + '<h2>Активни стил-правила в инструкциите</h2>'
            '<pre style="background:#fff;border:1px solid var(--line);padding:.6rem;'
            'font-size:.8rem;white-space:pre-wrap">' + (esc(own) or "(няма още)") + '</pre>')
    js = ("async function applyRule(rule, sugg){"
          "const r=await fetch('/api/lessons',{method:'POST',headers:{'Content-Type':'application/json'},"
          "body:JSON.stringify({action:'apply',rule,suggestion:sugg})});"
          "const d=await r.json(); if(d.error)alert(d.error); else location.reload();}")
    return _nav_shell("Уроци от редакциите", body, js)


def handle_lessons_post(data):
    if data.get("action") != "apply":
        return {"error": "неизвестно действие"}
    rule, sugg = str(data.get("rule") or ""), str(data.get("suggestion") or "")
    if not rule:
        return {"error": "празно правило"}
    with open(OWNER_RULES, "a", encoding="utf-8") as f:
        f.write("- " + rule + " — " + sugg + " (" + time.strftime("%Y-%m-%d") + ")\n")
    try:
        applied = set(json.loads(LESSONS_APPLIED.read_text(encoding="utf-8")))
    except Exception:
        applied = set()
    applied.add(rule)
    LESSONS_APPLIED.write_text(json.dumps(sorted(applied), ensure_ascii=False), encoding="utf-8")
    return {"ok": True}


def readiness_page():
    import collections
    import db
    con = db.connect()
    try:
        tot, rdy = con.execute("SELECT COUNT(*), SUM(ready) FROM launch_readiness").fetchone()
        hums = con.execute("SELECT COUNT(*) FROM review_state WHERE verdict='human_approve'").fetchone()[0]
        sugg = con.execute("SELECT COUNT(*) FROM review_state WHERE ready=1 "
                           "AND verdict NOT LIKE 'human_%'").fetchone()[0]
        blockers = collections.Counter()
        for (b,) in con.execute("SELECT blockers FROM launch_readiness WHERE ready=0").fetchall():
            for k in str(b or "").split(","):
                if k.strip():
                    blockers[k.strip()] += 1
        enr = con.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    finally:
        con.close()
    lbl = {"name": "име", "brand": "бранд", "image": "снимка", "attributes": "атрибути",
           "price": "цена", "no_fabrication": "риск от измислици", "not_flagged": "нужда от преглед"}
    brows = "".join("<tr><td>" + esc(lbl.get(k, k)) + "</td><td>" + str(v) + "</td></tr>"
                    for k, v in blockers.most_common())
    body = ('<div style="display:flex;gap:2rem;flex-wrap:wrap;font-size:1rem">'
            '<div><b style="font-size:1.6rem">' + str(enr) + '</b><br><span class="muted">обработени (от 14 159)</span></div>'
            '<div><b style="font-size:1.6rem">' + str(rdy or 0) + '</b><br><span class="muted">технически готови (от '
            + str(tot) + ' проверени)</span></div>'
            '<div><b style="font-size:1.6rem;color:var(--ok)">' + str(hums) + '</b><br><span class="muted">одобрени от теб</span></div>'
            '<div><b style="font-size:1.6rem">' + str(sugg) + '</b><br><span class="muted">предложени от рецензента</span></div></div>'
            '<p class="muted">За Shopify тръгва само одобреното от теб; „технически готови“ мери качеството на данните.</p>'
            '<button onclick="recompute()">⟳ Преизчисли</button> <span id="st" class="muted"></span>'
            '<h2>Какво блокира останалите</h2>'
            '<table><tr><th>Блокер</th><th>Продукти</th></tr>' + (brows or "<tr><td colspan=2>нищо</td></tr>") + '</table>')
    js = ("async function recompute(){document.getElementById('st').textContent='смята се (30-60 сек)…';"
          "const r=await fetch('/api/readiness',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'});"
          "const d=await r.json(); document.getElementById('st').textContent=d.note||'';"
          "setTimeout(()=>location.reload(), 45000);}")
    return _nav_shell("Готовност за старт", body, js)


def handle_readiness_post(_data):
    import os
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    subprocess.Popen([sys.executable, str(HERE / "launch_readiness.py")], cwd=str(HERE),
                     env=env, creationflags=flags,
                     stdout=open(HERE / "readiness_recompute.log", "w", encoding="utf-8"),
                     stderr=subprocess.STDOUT)
    return {"ok": True, "note": "преизчислява се — страницата ще се презареди"}


def dupes_page():
    import db
    try:
        dism = set(json.loads(DUP_DISMISSED.read_text(encoding="utf-8")))
    except Exception:
        dism = set()
    con = db.connect()
    cards = []
    try:
        groups, codes_all = [], []
        for sig, kind, cj in con.execute("SELECT sig, kind, codes FROM duplicate_products").fetchall():
            if sig in dism:
                continue
            codes = json.loads(cj)
            groups.append((sig, kind, codes))
            codes_all += codes
        names = {}
        if codes_all:
            q = ",".join("?" * len(codes_all))
            for c, fj in con.execute("SELECT code, fields_json FROM products WHERE code IN ("
                                     + q + ")", codes_all).fetchall():
                try:
                    names[str(c)] = json.loads(fj or "{}").get("Наименование") or ""
                except Exception:
                    pass
        kindlbl = {"catalogue_number": "същия каталожен №", "same_image": "същата снимка",
                   "same_name": "същото име"}
        for sig, kind, codes in groups:
            items = "".join(
                '<div style="display:flex;align-items:center;gap:.5rem;margin:.2rem 0">'
                '<img loading="lazy" src="/thumb?code=' + esc(c) + '" style="width:44px;height:44px;'
                'object-fit:contain;background:var(--vanilla);border-radius:6px" onerror="this.remove()">'
                '<a href="/rows?code=' + esc(c) + '" target="_blank"><b>' + esc(c) + '</b></a> '
                + esc(names.get(str(c), "")[:70]) + '</div>'
                for c in codes)
            cards.append('<div class="ovcard" id="g-' + esc(sig) + '">'
                         '<span class="muted">' + esc(kindlbl.get(kind, kind)) + '</span>' + items
                         + '<button onclick="linkGroup(' + esc(json.dumps(sig)) + ', '
                         + esc(json.dumps(codes)) + ')">⛓ Свържи като варианти</button> '
                         '<button class="ghost" onclick="dismissGroup(' + esc(json.dumps(sig))
                         + ')">Не е дубликат</button></div>')
    finally:
        con.close()
    body = ('<p class="muted">' + str(len(cards)) + ' групи възможни дубликати. „Свържи като '
            'варианти“ ги добавя взаимно в Свързани (нова версия, вижда се като диф). '
            '„Не е дубликат“ скрива групата.</p>'
            + ("".join(cards) or '<p class="muted">няма отворени групи</p>'))
    js = ("async function api(b){const r=await fetch('/api/dupes',{method:'POST',"
          "headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});"
          "const d=await r.json();if(d.error)alert(d.error);return d;}"
          "async function linkGroup(sig, codes){const d=await api({action:'link',sig,codes});"
          "if(d.ok){document.getElementById('g-'+sig)?.remove();}}"
          "async function dismissGroup(sig){const d=await api({action:'dismiss',sig});"
          "if(d.ok){document.getElementById('g-'+sig)?.remove();}}")
    return _nav_shell("Дубликати и варианти", body, js)


def _dismiss(sig):
    try:
        dism = set(json.loads(DUP_DISMISSED.read_text(encoding="utf-8")))
    except Exception:
        dism = set()
    dism.add(sig)
    DUP_DISMISSED.write_text(json.dumps(sorted(dism), ensure_ascii=False), encoding="utf-8")


def handle_dupes_post(data):
    action = data.get("action")
    sig = str(data.get("sig") or "")
    if action == "dismiss":
        _dismiss(sig)
        return {"ok": True}
    if action == "link":
        from datetime import datetime
        import db
        codes = [str(c) for c in (data.get("codes") or [])]
        if len(codes) < 2:
            return {"error": "групата е твърде малка"}
        con = db.connect()
        n = 0
        try:
            with open(HERE / "results.lanez_duplink.jsonl", "a", encoding="utf-8") as fh:
                for c in codes:
                    row = con.execute("SELECT record_json FROM products WHERE code=?", (c,)).fetchone()
                    if not row:
                        continue
                    rec = json.loads(row[0])
                    f = dict(rec.get("fields") or {})
                    cur = [x.strip() for x in re.split(r"[,;]+", str(f.get("Свързани") or "")) if x.strip()]
                    add = [x for x in codes if x != c and x not in cur]
                    if not add:
                        continue
                    f["Свързани"] = ", ".join(cur + add)
                    nd = dict(rec)
                    nd["fields"] = f
                    nd["ts"] = datetime.now().isoformat(timespec="seconds")
                    meta = dict(nd.get("meta") or {})
                    meta["notes"] = list(meta.get("notes") or []) + ["dup_linked_by_owner"]
                    nd["meta"] = meta
                    fh.write(json.dumps(nd, ensure_ascii=False) + "\n")
                    fh.flush()
                    db.record_version(nd)
                    n += 1
        finally:
            con.close()
        _dismiss(sig)
        return {"ok": True, "linked": n}
    return {"error": "неизвестно действие"}


def vocab_page(q=""):
    vocab = load_vocab()
    canon = vocab.get("canon", {})
    ql = q.strip().lower()
    rows = []
    for raw, (c, g) in sorted(vocab["types"].items()):
        if ql and ql not in raw.lower() and ql not in c.lower():
            continue
        opts = "".join('<option' + (' selected' if x == c else '') + '>' + esc(x) + '</option>'
                       for x in sorted(canon))
        rows.append('<tr data-raw="' + esc(raw) + '"><td>' + esc(raw) + '</td>'
                    '<td><select class="c">' + opts + '</select></td>'
                    '<td class="muted">' + esc(g) + '</td>'
                    '<td><button onclick="saveMap(this)">Запази</button> '
                    '<button class="ghost" onclick="delMap(this)">✕</button></td></tr>')
    body = ('<p class="muted">' + str(len(vocab["types"])) + ' сурови типа → ' + str(len(canon))
            + ' канонични. Смяната на канона пренасочва продуктите (пусни Пре-рендирай от '
            '/naming след промени); изтриването прави типа неразпознат.</p>'
            '<form method="get" action="/vocab"><input type="text" name="q" value="' + esc(q)
            + '" placeholder="търси…"> <button>Филтрирай</button></form>'
            '<table><tr><th>Суров тип (от данните)</th><th>Каноничен тип</th><th>род</th><th></th></tr>'
            + "".join(rows) + '</table>')
    js = ("async function api(b){const r=await fetch('/api/vocab',{method:'POST',"
          "headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});"
          "const d=await r.json();if(d.error)alert(d.error);return d;}"
          "async function saveMap(btn){const tr=btn.closest('tr');"
          "if((await api({action:'set',raw:tr.dataset.raw,canon:tr.querySelector('.c').value})).ok)"
          "btn.textContent='✓';}"
          "async function delMap(btn){const tr=btn.closest('tr');"
          "if(confirm('Изтриване на съответствието?')&&(await api({action:'del',raw:tr.dataset.raw})).ok)"
          "tr.remove();}")
    return _nav_shell("Речник на типовете", body, js)


def handle_vocab_post(data):
    with _MUTEX:
        return _handle_vocab_post(data)


def _handle_vocab_post(data):
    vocab = load_vocab()
    raw = str(data.get("raw") or "").strip().lower()
    if data.get("action") == "set":
        c = str(data.get("canon") or "").strip()
        if c not in vocab.get("canon", {}):
            return {"error": "'" + c + "' не е каноничен тип"}
        vocab["types"][raw] = [c, vocab["canon"][c]]
    elif data.get("action") == "del":
        vocab["types"].pop(raw, None)
    else:
        return {"error": "неизвестно действие"}
    _locked_write(VOCAB, json.dumps(vocab, ensure_ascii=False, indent=1))
    _invalidate()
    return {"ok": True}


def ops_page():
    import collections
    import datetime
    import db
    con = db.connect()
    try:
        now = datetime.datetime.now()
        c30 = (now - datetime.timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%S")
        c60 = (now - datetime.timedelta(minutes=60)).strftime("%Y-%m-%dT%H:%M:%S")
        st = "stage IN ('enrich','enrich_fallback')"
        n30 = con.execute("SELECT COUNT(DISTINCT code) FROM versions WHERE " + st + " AND ts>=?", (c30,)).fetchone()[0]
        n60 = con.execute("SELECT COUNT(DISTINCT code) FROM versions WHERE " + st + " AND ts>=?", (c60,)).fetchone()[0]
        tot = con.execute("SELECT COUNT(DISTINCT code) FROM versions WHERE " + st).fetchone()[0]
        mix = collections.Counter(r[0] for r in con.execute(
            "SELECT primary_model FROM versions WHERE " + st + " AND ts>=?", (c60,)).fetchall())
        rv, rr = con.execute("SELECT COUNT(*), SUM(ready) FROM review_state").fetchone()
        hum = con.execute("SELECT COUNT(*) FROM review_state WHERE verdict='human_approve'").fetchone()[0]
        newest = con.execute("SELECT MAX(ts) FROM versions").fetchone()[0]
    finally:
        con.close()
    try:
        import run_one
        billed = run_one.billed_overflow_tokens() / 1e6
        cap = run_one._billed_cap_millions()
        meter = "%.1fM от %sM (~€%.0f)" % (billed, cap, billed * 0.42)
    except Exception as e:
        meter = "грешка: " + str(e)[:60]
    mixrows = "".join("<tr><td>" + esc(m or "?") + "</td><td>" + str(n) + "</td></tr>"
                      for m, n in mix.most_common())
    body = ('<meta http-equiv="refresh" content="120">'
            '<div style="display:flex;gap:2rem;flex-wrap:wrap">'
            '<div><b style="font-size:1.6rem">' + str(n30 * 2) + '/ч</b><br>'
            '<span class="muted">темпо (последните 30 мин: ' + str(n30) + ')</span></div>'
            '<div><b style="font-size:1.6rem">' + str(n60) + '</b><br><span class="muted">за последния час</span></div>'
            '<div><b style="font-size:1.6rem">' + str(tot) + '</b><br><span class="muted">обработени общо ('
            + str(tot * 100 // 14159) + '%)</span></div>'
            '<div><b style="font-size:1.6rem">' + str(rv) + '</b><br><span class="muted">рецензирани ('
            + str(rr or 0) + ' предложени, ' + str(hum) + ' одобрени)</span></div></div>'
            '<p class="muted">последен запис: ' + esc(newest) + ' · платен DashScope: ' + esc(meter)
            + ' · страницата се опреснява на 2 мин</p>'
            '<h2>Модели (последният час)</h2>'
            '<table><tr><th>Модел</th><th>Продукти</th></tr>'
            + (mixrows or "<tr><td colspan=2>нищо</td></tr>") + '</table>')
    return _nav_shell("Обработка — на живо", body)
