# -*- coding: utf-8 -*-
"""Interactive human-review console with fast 1-click / keyboard approval of the
vision-proposed corrections.

The vision verifier proposes edits (name/attributes/description) to match the photo.
High-confidence ones are auto-applied by the pipeline; medium/low ones land here as a
PROPOSAL. This console lets a human clear the queue fast:
  • Keyboard: A approve · R keep original · E edit · J/K (or ↓/↑) next/prev · Z undo
  • Auto-advance to the next pending item after each decision
  • Inline edit the proposed values before approving
  • Bulk-approve all visible proposals
  • Live "remaining" counter · click any photo to zoom
Decisions persist to approvals.jsonl; build_catalog.py applies them to the catalog.

Run:  python review_server.py [port]   ->  http://127.0.0.1:8733/
Reads results fresh on every page load, so it reflects the live pipeline.
"""
import difflib
import html
import io
import json
import re
import sys
import urllib.parse
from datetime import datetime
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import history as H
import db

HERE = Path(__file__).parent
RESULTS = HERE / "results.jsonl"
TASKS = HERE / "tasks.jsonl"
APPROVALS = HERE / "approvals.jsonl"
PROCESSED = HERE.parent / "image-pipeline" / "processed"
ORIGINALS = HERE.parent / "image-pipeline" / "originals"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8733
CARD_LIMIT = 500  # local thumbnails (/thumb) are cheap, so we can show far more than the
                  # old 250 hotlinked-image cap
_THUMB_CACHE = {}


def thumb_bytes(code):
    """A small local JPEG thumbnail from the processed/original image (avoids hotlinking
    full supplier photos, which hung the browser and forced the old low card cap).
    Hardened: path-traversal rejected, filename mapped like the downloader's safe_name,
    cache keyed on file mtime (a reprocessed image refreshes), misses never cached."""
    code = re.sub(r"[^0-9A-Za-zА-Яа-я _.-]", "_", str(code))   # same mapping as safe_name
    if ".." in code or "/" in code or "\\" in code:
        return None
    for d in (PROCESSED, ORIGINALS):
        for ext in ("png", "jpg", "jpeg", "webp"):
            p = d / f"{code}.{ext}"
            if not p.exists():
                continue
            try:
                mt = p.stat().st_mtime
                key = (str(p), mt)
                hit = _THUMB_CACHE.get(key)
                if hit is not None:
                    return hit
                from PIL import Image
                im = Image.open(p)
                if im.mode in ("RGBA", "LA", "P"):
                    # transparent cutout: composite on WHITE (naive .convert("RGB")
                    # fills alpha with BLACK — the owner-reported black backgrounds)
                    im = im.convert("RGBA")
                    bg = Image.new("RGB", im.size, (255, 255, 255))
                    bg.paste(im, mask=im.getchannel("A"))
                    im = bg
                else:
                    im = im.convert("RGB")
                im.thumbnail((240, 240))
                buf = io.BytesIO()
                im.save(buf, "JPEG", quality=80)
                data = buf.getvalue()
                if len(_THUMB_CACHE) < 4000:
                    _THUMB_CACHE[key] = data
                return data
            except Exception:
                continue                                # half-written file mid-reprocess: retry next hit
    return None
EDIT_FIELDS = ("Наименование", "Атрибути", "Описание")
EDIT_ALL_FIELDS = ("Наименование", "Бранд", "Атрибути", "Описание",
                   "Мета наименование", "Мета описание", "Свързани")


def esc(v):
    return html.escape(str(v)) if v not in (None, "") else "—"


# Human-readable Bulgarian labels for the deterministic quality flags (quality_flags.py).
_FLAG_BG = {
    "fabrication": "Възможно ИЗМИСЛЕНИ данни (WIPO/AISI/сертификат) — провери",
    "russian": "Руски букви/думи",
    "brand_recoverable": "Празен бранд, но марка има в атрибутите",
    "json_attrs": "Атрибути в грешен формат (JSON блок)",
    "catcode_in_name": "Каталожен код в наименованието",
    "reasoning_leak": "Разсъждение на модела изтекло в описанието",
    "romanized_synonyms": "Латиница/транслитерация в синонимите",
    "meta_truncated": "Мета текст отрязан по средата",
}
_RISK_W = {"high": 100, "medium": 10, "low": 1}


def _risk_score(qflags):
    return sum(_RISK_W.get(sev, 0) for _c, sev, _d in (qflags or []))


def load_records():
    # Prefer the indexed SQLite mirror (one query) over re-parsing ~26MB of lane files on
    # every page load. Falls back to the JSONL scan if the DB isn't ready.
    try:
        import db
        if db.is_ready():
            return db.canonical_records()
    except Exception:
        pass
    recs = []
    for rp in [RESULTS, *HERE.glob("results.lane*.jsonl")]:
        if rp.exists():
            for line in open(rp, encoding="utf-8", errors="replace"):
                if line.strip():
                    try:
                        recs.append(json.loads(line))
                    except Exception:
                        pass
    by_code = {}
    for r in sorted(recs, key=lambda r: r.get("ts") or ""):
        by_code[str(r.get("code"))] = r
    return by_code


def load_tasks(codes):
    # Indexed DB lookup instead of scanning 167MB tasks.jsonl per page load.
    try:
        import db
        if db.tasks_ready():
            got = db.get_tasks(codes)
            if got:
                return got
    except Exception:
        pass
    tasks = {}
    if TASKS.exists() and codes:
        for line in open(TASKS, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                t = json.loads(line)
            except Exception:
                continue
            if str(t.get("code")) in codes:
                tasks[str(t.get("code"))] = t
    return tasks


def load_decisions():
    d = {}
    if APPROVALS.exists():
        for line in open(APPROVALS, encoding="utf-8", errors="replace"):
            if line.strip():
                try:
                    o = json.loads(line)
                    if o.get("action") == "undo":
                        d.pop(str(o["code"]), None)
                    else:
                        d[str(o["code"])] = o
                except Exception:
                    pass
    return d


def record_decision(code, action, fields=None):
    with open(APPROVALS, "a", encoding="utf-8") as f:
        f.write(json.dumps({"code": code, "action": action, "fields": fields,
                            "ts": datetime.now().isoformat(timespec="seconds")},
                           ensure_ascii=False) + "\n")


def _strip_tags(s):
    return re.sub(r"<[^>]+>", " ", str(s or ""))


def word_diff(old, new):
    """Inline word-level diff: unchanged plain, removed struck-red, added green."""
    a, b = _strip_tags(old).split(), _strip_tags(new).split()
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "equal":
            out.append(esc(" ".join(a[i1:i2])))
        else:
            if i2 > i1:
                out.append(f'<del>{esc(" ".join(a[i1:i2]))}</del>')
            if j2 > j1:
                out.append(f'<ins>{esc(" ".join(b[j1:j2]))}</ins>')
    return " ".join(out)


def diff_row(label, cur, prop):
    """One field as an inline diff (current → proposed), changes highlighted."""
    same = _strip_tags(cur).split() == _strip_tags(prop).split()
    if same:
        return f'<tr class="same"><th>{esc(label)}</th><td class="diff-cell">{esc(_strip_tags(cur))}</td></tr>'
    return f'<tr class="changed"><th>{esc(label)}</th><td class="diff-cell">{word_diff(cur, prop)}</td></tr>'


def sources_block(t, r):
    """Reference panel: Microinvest till name + scraped supplier data, so the
    reviewer can judge the AI text and the vision proposal against the sources."""
    if not t:
        return ""
    gt = t.get("ground_truth") or {}
    prod = t.get("product") or {}
    rows = []

    def row(lbl, val, link=False):
        if val in (None, "", "None"):
            return
        v = (f'<a href="{html.escape(str(val))}" target="_blank">линк ↗</a>' if link
             else esc(val))
        rows.append(f'<tr><th>{esc(lbl)}</th><td>{v}</td></tr>')

    row("Microinvest (Стока)", gt.get("Стока"))
    row("Мярка", prod.get("Мярка"))
    row("Доставчик", gt.get("Източник"))
    row("Съвпадение", f'{gt.get("Съвпадение")} ({gt.get("Match kind")})')
    row("Име (доставчик)", gt.get("BG име (доставчик)"))
    row("Англ. име", gt.get("Английско име"))
    row("Бранд (скрейп)", gt.get("Бранд (скрейп)"))
    row("Материал (скрейп)", gt.get("Материал (скрейп)"))
    row("Размери (скрейп)", gt.get("Размери (скрейп)"))
    row("Описание (скрейп)", gt.get("Описание (скрейп)"))
    row("URL доставчик", gt.get("URL (доставчик)"), link=True)
    scrape_img = gt.get("Снимка")
    imghtml = (f'<img loading="lazy" src="{html.escape(str(scrape_img))}" onclick="zoom(this.src)" title="снимка на доставчика">'
               if scrape_img else "")
    return (f'<details class="sources"><summary>Източници (Microinvest + скрейп)</summary>'
            f'<div class="srcbody"><table class="src">{"".join(rows)}</table>'
            f'<div class="srcimg">{imghtml}</div></div></details>')


def _pending(r, decisions):
    vc = r.get("vision_correction") or {}
    return bool(vc.get("proposed") and not vc.get("applied")
                and str(r.get("code")) not in decisions)


def card(code, r, t, decision):
    f = r.get("fields", {})
    orig = (t or {}).get("product", {})
    img = (orig.get("Снимки") or "").split(";")[0].strip()
    vc = r.get("vision_correction") or {}
    proposed = vc.get("proposed") if vc and not vc.get("applied") else None
    autofixed = bool(vc and vc.get("applied"))
    notes = (r.get("meta") or {}).get("notes") or []
    nh = r.get("needs_human")
    decided = decision.get("action") if decision else None

    if decided == "approve":
        status_cls, badge = "approved", "одобрено ✓"
    elif decided == "reject":
        status_cls, badge = "rejected", "оставено ✓"
    elif autofixed:
        status_cls, badge = "autofixed", "авто-корекция от снимка"
    elif nh:
        status_cls, badge = "flagged", "за преглед"
    else:
        status_cls, badge = "clean", "готов"

    is_pending = bool(proposed and not decided)
    panel = ""
    if is_pending:
        rows = "".join(diff_row(k, f.get(k), proposed.get(k)) for k in EDIT_FIELDS if proposed.get(k))
        edits = "".join(
            f'<label class="edrow"><span>{esc(k)}</span>'
            f'<textarea data-field="{esc(k)}" rows="2">{esc(proposed.get(k))}</textarea></label>'
            for k in EDIT_FIELDS if proposed.get(k))
        note = esc(vc.get("note") or "")
        panel = f"""
    <div class="proposal" data-code="{esc(code)}" id="prop-{esc(code)}">
      <p class="pnote">📸 Визуалната проверка предлага корекция{f' — {note}' if note != '—' else ''}
         <span class="conf2">(сигурност: {esc(vc.get('confidence') or '?')})</span></p>
      <p class="difkey"><del>червено = премахнато</del> · <ins>зелено = добавено</ins></p>
      <table class="diff"><tbody>{rows}</tbody></table>
      <div class="editform" hidden>{edits}</div>
      <div class="acts">
        <button class="approve" onclick="decide(this,'approve')">✓ Одобри <kbd>A</kbd></button>
        <button class="edit" onclick="toggleEdit(this)">✎ Редактирай <kbd>E</kbd></button>
        <button class="reject" onclick="decide(this,'reject')">✗ Откажи (остави оригинала) <kbd>R</kbd></button>
      </div>
    </div>"""

    vv = r.get("vision_verify") or {}
    if vv.get("ok") is True:
        vis = '<span class="vis ok">снимка ✓</span>'
    elif vv.get("ok") is False:
        vis = f'<span class="vis bad">снимка ✗ {esc((vv.get("detail") or {}).get("забележка") or "разминаване")}</span>'
    else:
        vis = ""

    # WHY is this flagged? Surface the deterministic quality flags prominently (was only
    # visible on the separate history page). Sorted by severity.
    qflags = (r.get("meta") or {}).get("quality_flags") or []
    flags_html = ""
    if qflags:
        _sev = {"high": 0, "medium": 1, "low": 2}
        items = "".join(
            f'<li class="qf-{esc(sev)}"><b>{esc(_FLAG_BG.get(fc, fc))}</b>'
            f'{": " + esc(det) if det else ""}</li>'
            for fc, sev, det in sorted(qflags, key=lambda x: _sev.get(x[1], 3)))
        flags_html = f'<div class="flags"><p class="flags-h">⚠️ За проверка:</p><ul>{items}</ul></div>'
    # Action controls for a flagged card with NO vision proposal — previously a dead end
    # (no way to clear it from the queue). Now it can be accepted or sent to manual fix.
    flagged_actions = ""
    if nh and not is_pending and not decided:
        flagged_actions = f"""
    <div class="proposal flagged-actions" data-code="{esc(code)}" id="prop-{esc(code)}">
      {flags_html}
      <div class="acts">
        <button class="approve" onclick="decide(this,'approve')">✓ Приеми както е <kbd>A</kbd></button>
        <button class="reject" onclick="decide(this,'reject')">✗ Остави за ръчна корекция <kbd>R</kbd></button>
      </div>
    </div>"""

    # Prefer the local processed/original thumbnail (fast, no hotlink); the full supplier
    # image opens on click via zoom().
    # zoom() reads data-full — never interpolate a supplier URL into a JS string (the
    # HTML parser decodes entities BEFORE the JS runs, so html.escape can't protect it).
    imgtag = (f'<img loading="lazy" src="/thumb?code={esc(code)}" data-full="{html.escape(img)}" '
              f'onclick="zoom(this.dataset.full)" onerror="this.style.display=\'none\'">'
              if img else '<p class="noimg">няма снимка</p>')
    return f"""
<article class="{status_cls}" data-status="{status_cls}" data-pending="{1 if is_pending else 0}"
         data-nh="{1 if nh else 0}" data-risk="{_risk_score(qflags)}" id="card-{esc(code)}">
  <header><span class="code">{esc(code)}</span>
    <h2>{esc(f.get('Наименование'))}</h2>
    <span class="badge {status_cls}">{badge}</span>{vis}
    <a class="histlink" href="/history?code={esc(code)}" target="_blank" title="хронология на промените">🕘 История</a></header>
  {panel}{flagged_actions}
  <div class="body">
    <div class="img">{imgtag}</div>
    <dl>
      <dt>Бранд</dt><dd>{esc(f.get('Бранд'))}</dd>
      <dt>Атрибути</dt><dd>{esc(f.get('Атрибути'))}</dd>
      <dt>Категория</dt><dd>{esc(f.get('Категории'))}</dd>
      <dt>Мета описание</dt><dd>{esc(f.get('Мета описание'))}</dd>
      <dt>Бележки</dt><dd class="notes">{esc(', '.join(notes))}</dd>
    </dl>
  </div>
  <details><summary>Описание</summary><div class="desc">{_safe_desc_html(f.get('Описание'))}</div></details>
  {sources_block(t, r)}
</article>"""


def render():
    by_code = load_records()
    decisions = load_decisions()
    recs = sorted(by_code.values(), key=lambda r: r.get("ts") or "", reverse=True)
    total = len(recs)
    clean = sum(1 for r in recs if not r.get("needs_human"))
    flagged = total - clean
    pending = sum(1 for r in recs if _pending(r, decisions))
    # Flagged tier ordered by RISK (fabrication/russian first), not just recency — puts the
    # products that most need a human at the top of the queue.
    order = (sorted([r for r in recs if _pending(r, decisions)], key=lambda r: r.get("ts") or "", reverse=True)
             + sorted([r for r in recs if r.get("needs_human") and not _pending(r, decisions)],
                      key=lambda r: (_risk_score((r.get("meta") or {}).get("quality_flags") or []),
                                     r.get("ts") or ""), reverse=True)
             + [r for r in recs if not r.get("needs_human")])
    shown = order[:CARD_LIMIT]
    tasks = load_tasks({str(r.get("code")) for r in shown})
    cards = [card(str(r.get("code")), r, tasks.get(str(r.get("code"))), decisions.get(str(r.get("code"))))
             for r in shown]
    more = f" · показани първите {len(shown)}" if total > len(shown) else ""
    start_filter = "proposals" if pending else "all"
    return PAGE.format(total=total, clean=clean, flagged=flagged, pending=pending,
                       ts=datetime.now().strftime("%Y-%m-%d %H:%M") + more,
                       cards="".join(cards), start_filter=start_filter)


PAGE = r"""<!doctype html><html lang="bg"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Продукти — човешки преглед</title>
<style>
 :root {{ --line:#d9d6ce; --warn:#a33f00; --muted:#77746a; --accent:#2e6e64; --ok:#22662a; }}
 body {{ font:15px/1.5 "Segoe UI", system-ui, sans-serif; margin:0 auto; max-width:1040px;
        padding:1.2rem 1rem 4rem; background:#f3f1ec; color:#26251f; }}
 h1 {{ font-size:1.35rem; margin:0 0 .2rem; }} .sub {{ color:var(--muted); margin:.2rem 0 .8rem; }}
 .stat {{ font-weight:700; }}
 .bar {{ position:sticky; top:0; background:#f3f1ec; padding:.55rem 0; z-index:5; border-bottom:1px solid var(--line);
        display:flex; gap:.5rem; align-items:center; flex-wrap:wrap; }}
 .bar button {{ font:inherit; padding:.35rem .8rem; border:1px solid var(--line); background:#fff; border-radius:4px; cursor:pointer; }}
 .flags {{ background:#fff5ed; border:1px solid #e7c9b0; border-radius:6px; padding:.4rem .6rem; margin:.4rem 0; }}
 .flags-h {{ margin:0 0 .25rem; font-weight:700; color:var(--warn); }}
 .flags ul {{ margin:0; padding-left:1.1rem; }}
 .flags li {{ margin:.1rem 0; }}
 .qf-high {{ color:#8a1f1f; font-weight:600; }} .qf-medium {{ color:#8a4b00; }} .qf-low {{ color:var(--muted); }}
 .flagged-actions {{ border:1px solid #e7c9b0; background:#fffdfa; border-radius:6px; padding:.5rem .6rem; margin:.4rem 0; }}
 .bar button.active {{ background:var(--accent); color:#fff; border-color:var(--accent); }}
 .bar .grow {{ flex:1; }} #remain {{ font-weight:700; color:var(--warn); }}
 .bulk {{ background:var(--ok)!important; color:#fff!important; border-color:var(--ok)!important; }}
 #search {{ font:inherit; padding:.35rem .6rem; border:1px solid var(--line); border-radius:4px; min-width:12rem; }}
 .sess {{ font-size:.8rem; color:var(--muted); font-weight:600; }}
 .help {{ font-size:.75rem; color:var(--muted); margin:.3rem 0 1rem; }}
 kbd {{ font:600 .68rem/1 Consolas, monospace; background:#efeae0; border:1px solid var(--line);
        border-bottom-width:2px; border-radius:3px; padding:.05rem .3rem; margin-left:.25rem; }}
 article {{ background:#fff; border:1px solid var(--line); border-radius:6px; margin-bottom:1rem; padding:.9rem 1.1rem; scroll-margin-top:3.5rem; }}
 article.current {{ outline:3px solid var(--accent); outline-offset:2px; }}
 article header {{ display:flex; gap:.7rem; align-items:baseline; }}
 article h2 {{ font-size:1rem; margin:0; flex:1; }}
 .code {{ font:600 .75rem/1 Consolas, monospace; color:var(--accent); border:1px solid var(--line); padding:.2rem .45rem; border-radius:3px; }}
 .badge {{ font-size:.72rem; font-weight:600; padding:.18rem .5rem; border-radius:10px; }}
 .badge.flagged {{ background:#f7e3d3; color:var(--warn); }} .badge.clean {{ background:#dcefdd; color:var(--ok); }}
 .badge.autofixed {{ background:#e2ecff; color:#254a9a; }} .badge.approved {{ background:#dcefdd; color:var(--ok); }}
 .badge.rejected {{ background:#eee; color:#555; }}
 article.flagged {{ border-left:3px solid var(--warn); }} article.clean {{ border-left:3px solid #4d9955; }}
 article.autofixed {{ border-left:3px solid #4a74d6; }} article.approved,article.rejected {{ border-left:3px solid var(--ok); opacity:.7; }}
 .proposal {{ background:#fbf6ee; border:1px solid #e7dcc7; border-radius:6px; padding:.7rem .9rem; margin:.6rem 0; }}
 .pnote {{ margin:0 0 .5rem; font-weight:600; }} .conf2 {{ color:var(--muted); font-weight:400; }}
 table.diff {{ width:100%; border-collapse:collapse; font-size:.85rem; }}
 table.diff th, table.diff td {{ text-align:left; vertical-align:top; padding:.25rem .4rem; border-top:1px solid #ece4d5; }}
 table.diff thead th {{ color:var(--muted); font-size:.75rem; border:0; }}
 table.diff tr.same td.prop {{ color:var(--muted); }}
 td.cur {{ color:#8a3b1a; width:42%; }} td.prop {{ color:var(--ok); width:42%; }} tr.changed td.prop {{ font-weight:600; }}
 .difkey {{ font-size:.72rem; color:var(--muted); margin:.1rem 0 .3rem; }}
 .difkey del {{ color:#a12020; }} .difkey ins {{ color:var(--ok); }}
 td.diff-cell {{ line-height:1.7; }}
 td.diff-cell del {{ color:#a12020; background:#fbe3e3; text-decoration:line-through; padding:0 .1rem; border-radius:2px; }}
 td.diff-cell ins {{ color:#186034; background:#d8f0dd; text-decoration:none; padding:0 .1rem; border-radius:2px; }}
 .sources {{ margin-top:.5rem; font-size:.85rem; }}
 .sources > summary {{ color:var(--accent); cursor:pointer; }}
 .srcbody {{ display:grid; grid-template-columns:1fr 130px; gap:.8rem; margin-top:.4rem; border-top:1px solid var(--line); padding-top:.5rem; }}
 @media (max-width:640px) {{ .srcbody {{ grid-template-columns:1fr; }} }}
 table.src {{ width:100%; border-collapse:collapse; }}
 table.src th {{ text-align:left; color:var(--muted); font-weight:400; width:9rem; vertical-align:top; padding:.15rem .4rem .15rem 0; }}
 table.src td {{ padding:.15rem 0; vertical-align:top; }}
 .srcimg img {{ max-width:100%; border:1px solid var(--line); border-radius:4px; cursor:zoom-in; }}
 .editform {{ margin:.5rem 0; }} .edrow {{ display:grid; grid-template-columns:6rem 1fr; gap:.5rem; align-items:start; margin-bottom:.4rem; }}
 .edrow span {{ color:var(--muted); font-size:.8rem; padding-top:.3rem; }}
 .edrow textarea {{ width:100%; font:inherit; font-size:.85rem; padding:.3rem; border:1px solid var(--line); border-radius:4px; resize:vertical; }}
 .acts {{ margin-top:.6rem; display:flex; gap:.5rem; flex-wrap:wrap; }}
 .acts button {{ font:inherit; font-weight:600; padding:.4rem 1rem; border-radius:5px; cursor:pointer; border:1px solid var(--line); }}
 .acts .approve {{ background:var(--ok); color:#fff; border-color:var(--ok); }} .acts .edit {{ background:#fff; color:#254a9a; }}
 .acts .reject {{ background:#fff; color:#555; }} .acts kbd {{ background:rgba(255,255,255,.25); border-color:rgba(255,255,255,.4); }}
 .acts .edit kbd, .acts .reject kbd {{ background:#efeae0; border-color:var(--line); }}
 .done {{ color:var(--ok); font-weight:600; }} .done a {{ color:var(--muted); font-size:.8rem; margin-left:.6rem; cursor:pointer; text-decoration:underline; }}
 .body {{ display:grid; grid-template-columns:170px 1fr; gap:1rem; margin-top:.7rem; }}
 @media (max-width:640px) {{ .body {{ grid-template-columns:1fr; }} }}
 .img img {{ max-width:100%; border:1px solid var(--line); border-radius:4px; background:#fff; cursor:zoom-in; }}
 .noimg {{ color:var(--muted); }}
 dl {{ display:grid; grid-template-columns:7rem 1fr; gap:.2rem .7rem; margin:0; font-size:.86rem; }}
 dt {{ color:var(--muted); }} dd {{ margin:0; }} .notes {{ font-family:Consolas, monospace; font-size:.76rem; color:var(--muted); }}
 details {{ margin-top:.7rem; font-size:.87rem; }} summary {{ cursor:pointer; color:var(--accent); }}
 .desc {{ border-top:1px solid var(--line); margin-top:.5rem; padding-top:.5rem; }}
 .vis {{ font-size:.72rem; padding:.18rem .5rem; border-radius:10px; }}
 .vis.ok {{ background:#dcefdd; color:var(--ok); }} .vis.bad {{ background:#f7d3d3; color:#a12020; }}
 #lb {{ position:fixed; inset:0; background:rgba(0,0,0,.85); display:none; align-items:center; justify-content:center; z-index:50; cursor:zoom-out; }}
 #lb img {{ max-width:92%; max-height:92%; border-radius:4px; }}
 #toast {{ position:fixed; bottom:1rem; left:50%; transform:translateX(-50%); background:#26251f; color:#fff;
          padding:.5rem 1rem; border-radius:6px; font-size:.85rem; opacity:0; transition:opacity .2s; z-index:60; }}
</style></head><body>
<h1>Обработени продукти <a href="/" style="font-size:.7rem;font-weight:400;">→ преглед по етапи</a></h1>
<p class="sub"><span class="stat">{total}</span> обработени · <span class="stat">{clean}</span> готови ·
 <span class="stat">{flagged}</span> за преглед · <span id="remain" class="stat">{pending}</span> чакат одобрение · {ts}</p>
<div class="bar">
  <button data-f="proposals" onclick="flt(this)">Предложения ({pending})</button>
  <button data-f="flagged" onclick="flt(this)">За преглед</button>
  <button data-f="clean" onclick="flt(this)">Готови</button>
  <button data-f="all" onclick="flt(this)">Всички</button>
  <input id="search" type="search" placeholder="Търси по код / име…" oninput="applyView()">
  <span class="grow" style="flex:1"></span>
  <span id="sess" class="sess">0 прегледани този сеанс</span>
  <button class="bulk" onclick="bulk()">✓✓ Одобри всички показани</button>
</div>
<p class="help">Клавиши: <kbd>A</kbd> одобри · <kbd>R</kbd> остави · <kbd>E</kbd> редактирай ·
 <kbd>J</kbd>/<kbd>K</kbd> или <kbd>↓</kbd>/<kbd>↑</kbd> следващ/предишен · <kbd>Z</kbd> отмени последното · клик върху снимка = уголеми</p>
{cards}
<div id="lb" onclick="this.style.display='none'"><img></div>
<div id="toast"></div>
<script>
let curFilter="{start_filter}", lastDecided=null, sessionDone=0;
const origPanels = {{}};
function toast(m) {{ const t=document.getElementById('toast'); t.textContent=m; t.style.opacity=1; clearTimeout(t._h); t._h=setTimeout(()=>t.style.opacity=0,1600); }}
function zoom(src) {{ if(!src) return; const lb=document.getElementById('lb'); lb.querySelector('img').src=src; lb.style.display='flex'; }}
function updateRemain() {{ document.getElementById('remain').textContent = pendingCards().length; }}
function bumpSession() {{ sessionDone++; document.getElementById('sess').textContent = sessionDone+' прегледани този сеанс'; }}
function pendingCards() {{ return [...document.querySelectorAll('article[data-pending="1"]')].filter(a=>!a.dataset.done && a.style.display!=='none'); }}
function visibleCards() {{ return [...document.querySelectorAll('article')].filter(a=>a.style.display!=='none'); }}
function applyView() {{
  const q = (document.getElementById('search').value||'').trim().toLowerCase();
  document.querySelectorAll('article').forEach(a=>{{
    const inFilter = curFilter==='all' || (curFilter==='proposals' ? a.dataset.pending==='1' : a.dataset.status===curFilter);
    const hay = (a.id+' '+(a.querySelector('h2')?a.querySelector('h2').textContent:'')).toLowerCase();
    a.style.display = (inFilter && (!q || hay.includes(q))) ? '' : 'none';
  }});
}}
function flt(btn) {{
  document.querySelectorAll('.bar button[data-f]').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active'); curFilter=btn.dataset.f;
  applyView();
  setCurrent(pendingCards()[0] || visibleCards()[0]);
}}
let cur=null;
function setCurrent(el) {{
  if (cur) cur.classList.remove('current');
  cur = el; if (!cur) return;
  cur.classList.add('current'); cur.scrollIntoView({{block:'center', behavior:'smooth'}});
}}
function move(dir) {{
  const list = curFilter==='proposals' ? pendingCards() : visibleCards();
  if (!list.length) return;
  let i = list.indexOf(cur); i = (i<0)?0:i+dir;
  if (i>=0 && i<list.length) setCurrent(list[i]);
}}
function toggleEdit(btn) {{ const p=btn.closest('.proposal'); const ef=p.querySelector('.editform'); ef.hidden=!ef.hidden; if(!ef.hidden) ef.querySelector('textarea').focus(); }}
async function post(code, action, fields) {{
  const r = await fetch('/api/decide', {{method:'POST', headers:{{'Content-Type':'application/json'}}, body: JSON.stringify({{code, action, fields}})}});
  if (!r.ok) throw new Error('server'); return r.json();
}}
async function decide(elOrBtn, action) {{
  const p = elOrBtn.closest ? elOrBtn.closest('.proposal') : elOrBtn;
  const art = p.closest('article'); const code = p.dataset.code;
  let fields = null;
  if (action==='approve') {{ fields={{}}; p.querySelectorAll('.editform textarea').forEach(t=>fields[t.dataset.field]=t.value); }}
  p.querySelectorAll('button').forEach(b=>b.disabled=true);
  try {{
    await post(code, action, fields);
    const next = pendingCards().filter(a=>a!==art)[0] || null;
    origPanels[code] = p.innerHTML;                 // stash so undo can restore in place
    art.dataset.done="1";
    p.innerHTML = '<p class="done">'+(action==='approve'?'✓ Одобрено и приложено':'✓ Оставен оригиналът')+
      '<a onclick="undo(\''+code+'\',this)">отмени</a></p>';
    lastDecided = code; bumpSession(); updateRemain(); toast(action==='approve'?'Одобрено ✓':'Оставено ✓');
    if (curFilter==='proposals' && next) setCurrent(next);
  }} catch(e) {{ alert('Грешка при запис: '+e); p.querySelectorAll('button').forEach(b=>b.disabled=false); }}
}}
async function undo(code, a) {{
  try {{
    await post(code, 'undo', null);
    const art=document.getElementById('card-'+code);
    if(art){{ art.dataset.done=''; const p=art.querySelector('.proposal'); if(p && origPanels[code]) p.innerHTML=origPanels[code]; }}
    if(sessionDone>0) sessionDone--; document.getElementById('sess').textContent=sessionDone+' прегледани този сеанс';
    updateRemain(); toast('Отменено ↩');
  }} catch(e) {{ alert('Грешка: '+e); }}
}}
async function bulk() {{
  const list = pendingCards();
  if (!list.length) {{ toast('Няма показани предложения'); return; }}
  if (!confirm('Одобри '+list.length+' показани предложения?')) return;
  for (const art of list) {{ const p=art.querySelector('.proposal'); if(p) await decide(p,'approve'); }}
  toast('Готово — одобрени '+list.length);
}}
document.addEventListener('keydown', e=>{{
  if (['TEXTAREA','INPUT'].includes(e.target.tagName)) return;
  const k=e.key.toLowerCase();
  if (k==='j'||e.key==='ArrowDown') {{ e.preventDefault(); move(1); }}
  else if (k==='k'||e.key==='ArrowUp') {{ e.preventDefault(); move(-1); }}
  else if (k==='a' && cur) {{ const p=cur.querySelector('.proposal'); if(p&&!cur.dataset.done) decide(p,'approve'); }}
  else if (k==='r' && cur) {{ const p=cur.querySelector('.proposal'); if(p&&!cur.dataset.done) decide(p,'reject'); }}
  else if (k==='e' && cur) {{ const b=cur.querySelector('.acts .edit'); if(b) toggleEdit(b); }}
  else if (k==='z' && lastDecided) {{ const a=document.querySelector('#card-'+CSS.escape(lastDecided)+' .done a'); if(a) a.click(); }}
}});
// init
document.querySelector('.bar button[data-f="'+curFilter+'"]').classList.add('active');
flt(document.querySelector('.bar button[data-f="'+curFilter+'"]'));
</script>
</body></html>"""


def history_page(code):
    """Standalone HTML timeline for one product — every stage, its field-level diffs, and
    a better/worse tag per change. Rendered from history.build_timeline()."""
    events = H.build_timeline(code)
    css = """
    body{font:14px/1.5 system-ui,Segoe UI,sans-serif;max-width:900px;margin:24px auto;padding:0 16px;color:#1a1a1a}
    h1{font-size:20px}h1 .c{color:#666;font-weight:normal}
    a.back{display:inline-block;margin-bottom:14px;color:#2563eb;text-decoration:none}
    .ev{border-left:3px solid #d0d0d0;padding:6px 0 10px 16px;margin-left:8px;position:relative}
    .ev:before{content:'';position:absolute;left:-7px;top:9px;width:11px;height:11px;border-radius:50%;background:#9ca3af}
    .evh{font-size:13px}.evh .ts{color:#888;font-variant-numeric:tabular-nums;margin-right:6px}
    .created{background:#f3f4f6;padding:6px 10px;border-radius:6px;margin-top:4px}
    .fld{margin:6px 0;padding:6px 10px;background:#fafafa;border:1px solid #eee;border-radius:6px}
    .fn{font-weight:600}.d{font-family:ui-monospace,monospace;font-size:12.5px;white-space:pre-wrap;word-break:break-word}
    del{background:#fde8e8;color:#9b1c1c;text-decoration:line-through}
    ins{background:#e6f4ea;color:#166534;text-decoration:none}
    .better{color:#166534;font-size:12px;font-weight:600}.worse{color:#9b1c1c;font-size:12px;font-weight:600}
    .notes{color:#777;font-size:12px;margin-top:4px}.nochg{color:#999;font-size:12px}
    .rev{background:#eff6ff;padding:6px 10px;border-radius:6px}.auto{color:#166534;font-size:12.5px;margin-top:3px}
    .iss{color:#92400e;font-size:12.5px;margin-top:2px}.hum{background:#f5f3ff;padding:6px 10px;border-radius:6px;font-size:12.5px}
    """
    if not events:
        body = f"<p>Няма запазена история за <b>{html.escape(str(code))}</b>.</p>"
    else:
        parts = []
        for kind, ts, label, payload, changes, d in events:
            b = [f'<div class="ev"><div class="evh"><span class="ts">{html.escape(ts)}</span><b>{html.escape(label)}</b></div>']
            if kind == "snap":
                if changes is None:
                    fl = d.get("fields") or {}
                    b.append(f'<div class="created">Създаден: <b>{esc(fl.get("Наименование"))}</b><br>'
                             f'Бранд: {esc(fl.get("Бранд"))} · увереност: {esc(d.get("confidence"))} · '
                             f'за преглед: {esc(d.get("needs_human"))}</div>')
                elif not changes:
                    b.append('<div class="nochg">(без промени по проследяваните полета)</div>')
                else:
                    for fld, bef, aft, q in changes:
                        tag = {"+": '<span class="better">✅ по-добре</span>',
                               "-": '<span class="worse">⚠️ по-зле</span>', "": ""}[q]
                        b.append(f'<div class="fld"><span class="fn">{html.escape(fld)}</span> {tag}'
                                 f'<div class="d"><del>{esc(bef)}</del></div>'
                                 f'<div class="d"><ins>{esc(aft)}</ins></div></div>')
                if payload:
                    b.append(f'<div class="notes">{esc(", ".join(payload))}</div>')
            elif kind == "review":
                b.append(f'<div class="rev">готов за сайта: <b>{esc(payload.get("готов_за_сайта"))}</b> — '
                         f'{esc(payload.get("оценка"))}</div>')
                if payload.get("автоприложени"):
                    b.append(f'<div class="auto">авто-приложено: {esc(", ".join(payload["автоприложени"]))}</div>')
                for p in (payload.get("проблеми") or [])[:6]:
                    b.append(f'<div class="iss">[{esc(p.get("тежест"))}] {esc(p.get("поле"))}: {esc(p.get("проблем"))}</div>')
            elif kind == "human":
                b.append(f'<div class="hum">{esc(json.dumps(payload, ensure_ascii=False)[:400])}</div>')
            b.append("</div>")
            parts.append("".join(b))
        body = "".join(parts)
    return (f"<!doctype html><html lang=bg><head><meta charset=utf-8>"
            f"<meta name=viewport content='width=device-width,initial-scale=1'>"
            f"<title>История · {html.escape(str(code))}</title><style>{css}</style></head><body>"
            f"<a class=back href='/' onclick='history.back();return false'>← назад</a>"
            f"<h1>Хронология <span class=c>· {html.escape(str(code))}</span></h1>{body}</body></html>")


_ALLOWED_TAGS = re.compile(r"</?(?:h2|h3|p|ul|ol|li|b|strong|i|em|br)\s*/?>", re.I)


def _safe_desc_html(desc):
    """Render our own description HTML safely: keep only the harmless formatting tags the
    pipeline generates (h2/p/ul/li/b/i/br), escape everything else. Never truncated
    mid-tag — the card body scrolls instead."""
    s = str(desc or "")
    if not s.strip():
        return "—"
    keep = {}
    def _stash(m):
        token = f"\x00{len(keep)}\x00"
        keep[token] = m.group(0)
        return token
    s = _ALLOWED_TAGS.sub(_stash, s)
    s = re.sub(r"<[^>]+>", " ", s)                      # drop non-allowed tags
    s = html.escape(s)
    for token, tag in keep.items():
        s = s.replace(token, tag)
    return s


def _fmt_price(price):
    if price in (None, "", "0", "0.0"):
        return ""
    v = str(price)
    if v.endswith(".0"):
        v = v[:-2]
    return f'<span class="price">€{esc(v.replace(".", ","))}</span>'


def _related_html(rel_str, by_code, prev_rel_str=None):
    """Related products inside a card: small thumb + code + name, each hyperlinked to that
    product's own row. When prev_rel_str is given, links ADDED this pass show green and
    ones REMOVED show red struck-through."""
    def _codes(v):
        out = []
        for part in re.split(r"[,;]+", str(v or "")):
            p = part.strip().split("|")[0].strip()      # legacy 'код|Име' format
            if p:
                out.append(p)
        return out
    codes = _codes(rel_str)
    prev = _codes(prev_rel_str)
    if not codes and not prev:
        return ""
    prevset, curset = set(prev), set(codes)
    diff_on = prev_rel_str is not None

    def _item(c, cls=""):
        nm = str(((by_code.get(c) or {}).get("fields") or {}).get("Наименование") or "")[:44]
        return (f'<a class="rel{cls}" href="/rows?code={esc(c)}" title="{esc(nm)}">'
                f'<img loading="lazy" src="/thumb?code={esc(c)}" onerror="this.style.display=\'none\'">'
                f'<span><b>{esc(c)}</b> {esc(nm) if nm else ""}</span></a>')

    items = [_item(c, " add" if diff_on and c not in prevset else "") for c in codes[:6]]
    if diff_on:
        items += [_item(c, " del") for c in prev if c not in curset][:3]
    return '<div class="rels"><div class="rels-h">Свързани продукти:</div>' + "".join(items) + "</div>"


_seo_fonts = {}


def _seo_px(text, size):
    """Pixel width of text at a given font size — Google truncates SERP titles/snippets by
    PIXELS (~580px titles @20px, ~990px descriptions @14px), so this is the real check the
    online SEO tools do; PIL measures it locally, no external service needed."""
    try:
        from PIL import ImageFont
        f = _seo_fonts.get(size)
        if f is None:
            f = ImageFont.truetype("arial.ttf", size)
            _seo_fonts[size] = f
        return f.getlength(str(text or ""))
    except Exception:
        return None


def _meta_block(f, prev=None, always=True):
    """Meta title/description rows: value (diffed vs the previous stage when changed —
    old struck-red, new green), char count, pixel width, and a pass/fail SEO mark.
    With always=False (stage cards) only CHANGED metas are shown, keeping cards lean."""
    rows = []
    for lbl, key, lo, hi, fpx, maxpx in (("Мета име", "Мета наименование", 35, 60, 20, 580),
                                         ("Мета описание", "Мета описание", 70, 160, 14, 990)):
        v = str(f.get(key) or "").strip()
        pv = str((prev or {}).get(key) or "").strip() if prev is not None else v
        changed = prev is not None and pv != v
        if not always and not changed:
            continue
        n = len(v)
        w = _seo_px(v, fpx)
        ok = bool(v) and lo <= n <= hi and (w is None or w <= maxpx)
        mark, cls = ("✓", "seo-ok") if ok else ("✗", "seo-bad")
        detail = f"{n} зн." + (f" · {int(w)}px" if w is not None else "")
        val_html = word_diff(pv, v) if changed else (esc(v) if v else "—")
        rows.append(f'<div class="meta-row"><span class="mlabel">{esc(lbl)}</span>'
                    f'<span class="{cls}">{mark}</span> <span class="mlen">{detail}</span>'
                    f'<div class="mval">{val_html}</div></div>')
    if not rows:
        return ""
    return '<div class="metas">' + "".join(rows) + "</div>"


def _parse_attrs(s):
    """'K: V; K2: V2' -> ordered [(K, V)] (tolerates parts without ':')."""
    out = []
    for part in str(s or "").split(";"):
        part = part.strip()
        if not part:
            continue
        if ":" in part:
            k, v = part.split(":", 1)
            out.append((k.strip(), v.strip()))
        else:
            out.append((part, ""))
    return out


def _chips_diff(cur_attrs, prev_attrs):
    """Attribute chips diffed PER KEY vs the previous stage: a changed value renders
    inside one chip as 'Цвят: ~~Черен~~ Антрацит' (old struck-red, new green); a new key
    is a green chip; a removed key stays visible as a struck-red chip."""
    cur = _parse_attrs(cur_attrs)
    prev = dict(_parse_attrs(prev_attrs))
    cur_keys = {k for k, _ in cur}
    out = []
    for k, v in cur:
        pv = prev.get(k)
        if pv is None:
            out.append(f'<span class="chip add">{esc(k)}: {esc(v)}</span>')
        elif pv != v:
            out.append(f'<span class="chip">{esc(k)}: <del>{esc(pv)}</del> <ins>{esc(v)}</ins></span>')
        else:
            out.append(f'<span class="chip">{esc(k)}: {esc(v)}</span>')
    for k, pv in prev.items():
        if k not in cur_keys:
            out.append(f'<span class="chip del">{esc(k)}: {esc(pv)}</span>')
    return "".join(out)


def _val_diff(prev, cur):
    """Short-value inline diff (brand, meta fields): old struck-red, new green."""
    p, c = str(prev or "").strip(), str(cur or "").strip()
    if p == c:
        return esc(c)
    parts = []
    if p:
        parts.append(f"<del>{esc(p)}</del>")
    if c:
        parts.append(f"<ins>{esc(c)}</ins>")
    return " ".join(parts) or "—"


def _sf_card(label, cls, code, name, price, brand, attrs, desc, extra="", buttons="",
             related="", name_html=None, chips_html=None, metas="", brand_html=None,
             data_attrs="", photo_html=None):
    """A storefront-style card (shows the product as it would look on the shop)."""
    if photo_html is not None:
        thumb = photo_html
    else:
        _js = ("if(!this.dataset.r){this.dataset.r=1;"
               "this.src='/thumb?code=" + esc(code or "") + "&r='+Date.now();}"
               "else this.style.display='none';")
        thumb = (('<img loading="lazy" src="/thumb?code=' + esc(code)
                  + '" onerror="' + _js + '">') if code else "")
    chips = chips_html if chips_html is not None else "".join(
        f'<span class="chip">{esc(p.strip())}</span>'
        for p in str(attrs or "").split(";") if p.strip())
    if brand_html is not None:
        br = f'<span class="brand">{brand_html}</span>'
    else:
        br = f'<span class="brand">{esc(brand)}</span>' if str(brand or "").strip() else ""
    nm = name_html if name_html is not None else esc(name)
    return (f'<div class="sfcard {cls}"{data_attrs}><div class="lbl">{esc(label)}</div>'
            f'<div class="ph">{thumb}</div><div class="nm">{nm}</div>'
            f'<div class="meta">{_fmt_price(price)}{br}</div><div class="chips">{chips}</div>'
            f'<div class="sfdesc">{desc or "—"}</div>{related}{metas}{extra}{buttons}</div>')


def _review_fixes_map():
    """{code: latest proposal} loaded ONCE (was re-scanned per product = O(N×M))."""
    m = {}
    p = HERE / "review_fixes.jsonl"
    if p.exists():
        for line in open(p, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            if str(o.get("code")) and (o.get("предложения") or o.get("автоприложени")):
                m[str(o.get("code"))] = o
    return m


def _reviewer_card(code, rvmap):
    """The reviewer's suggestion card (last proposal for this code) with Approve/Edit."""
    latest = rvmap.get(str(code))
    if not latest:
        return ""
    props = latest.get("предложения") or []
    auto = latest.get("автоприложени") or {}
    body = ""
    if auto:
        body += '<div class="rvauto">Авто-приложено: ' + esc(", ".join(auto)) + "</div>"
    for pr in props[:5]:
        body += (f'<div class="rvprop"><b>{esc(pr.get("поле"))}</b>: {esc(pr.get("причина") or "")}'
                 f'<div class="rvnew">{esc(str(pr.get("нов"))[:160])}</div></div>')
    verdict = esc(latest.get("оценка") or "")
    btns = (f'<div class="acts"><button class="approve" onclick="rvDecide(\'{esc(code)}\',\'approve\')">✓ Одобри</button>'
            f'<button class="edit" onclick="location.href=\'/history?code={esc(code)}\'">✎ Виж историята</button></div>')
    return _sf_card("🔎 Предложение от рецензента", "reviewer", None, verdict or "Предложени корекции",
                    None, None, None, body, buttons=btns)


def _supplier_card(code, mi, sup):
    """Scraped-supplier card populated from EVERYTHING the scrape captured: BG+EN names,
    the supplier's OWN photo (hotlinked — distinct from our processed cutout), match
    quality, structured fields, raw-JSON fallback, and any ADDITIONAL source images."""
    raw = {}
    try:
        raw = json.loads(sup.get("Scrape raw (JSON)") or "{}")
        if not isinstance(raw, dict):
            raw = {}
    except Exception:
        pass
    bg_name = sup.get("BG име (доставчик)") or raw.get("bg_name")
    en_name = sup.get("Английско име") or raw.get("en_name")
    chips = []
    if sup.get("Източник"):
        chips.append(f'<span class="chip">Източник: {esc(sup.get("Източник"))}</span>')
    mk = str(sup.get("Match kind") or "")
    if mk:
        weak = mk.lower().startswith(("name", "model"))
        chips.append(f'<span class="chip{" del" if weak else ""}">Съвпадение: {esc(mk)}'
                     f'{" ⚠️ слабо" if weak else ""}</span>')
    for lbl, key in (("Бранд", "Бранд (скрейп)"), ("Материал", "Материал (скрейп)"),
                     ("Размери", "Размери (скрейп)")):
        v = sup.get(key)
        if v not in (None, "", "None"):
            chips.append(f'<span class="chip">{esc(lbl)}: {esc(str(v)[:40])}</span>')
    if en_name:
        chips.append(f'<span class="chip">EN: {esc(str(en_name)[:48])}</span>')
    desc = sup.get("Описание (скрейп)")
    if not desc:
        skip = {"image_url", "en_name", "bg_name", "url"}
        bits = [f"{k}: {v}" for k, v in raw.items()
                if k not in skip and isinstance(v, str) and v.strip()][:6]
        desc = "<br>".join(esc(x) for x in bits) if bits else None
    desc_html = _safe_desc_html(desc) if desc else '<span class="rawnote">няма скрейпнато описание</span>'
    sphoto = sup.get("Снимка") or raw.get("image_url")
    photo_html = (f'<img loading="lazy" src="{html.escape(str(sphoto))}" '
                  f'data-full="{html.escape(str(sphoto))}" onclick="zoom(this.dataset.full)" '
                  f'onerror="this.remove()">') if sphoto else ""
    urls = [u.strip() for u in str(mi.get("Снимки") or "").split(";") if u.strip()]
    extra_imgs = ""
    if len(urls) > 1:
        mini = "".join(f'<img loading="lazy" src="{html.escape(u)}" data-full="{html.escape(u)}" '
                       f'onclick="zoom(this.dataset.full)" onerror="this.remove()">'
                       for u in urls[1:7])
        extra_imgs = (f'<div class="morepics"><div class="rels-h">Още снимки от източника '
                      f'({len(urls) - 1}):</div>{mini}</div>')
    link = (f'<a class="srclink" href="{html.escape(str(sup.get("URL (доставчик)")))}" '
            f'target="_blank">сайт на доставчика ↗</a>' if sup.get("URL (доставчик)") else "")
    return _sf_card("🌐 Доставчик (скрейп)", "src-sup", None, bg_name or en_name or "—",
                    None, None, None, desc_html, chips_html="".join(chips),
                    extra=extra_imgs + link, photo_html=photo_html)


def product_row(code, canon_rec, rvmap, by_code=None, task=None, chained=False, rstate=None, show_v1=False):
    by_code = by_code or {}
    if task is None:                                     # single-row callers only; pages prefetch
        task = db.get_tasks([code]).get(str(code)) or {}
    mi, sup = (task.get("product") or {}), (task.get("ground_truth") or {})
    price = mi.get("Цена")
    _mi_chips = "".join(f'<span class="chip">{esc(k)}: {esc(v)}</span>'
                        for k, v in [("Код", code), ("Количество", mi.get("Количество")),
                                     ("Мярка", mi.get("Мярка")), ("Група", sup.get("Група"))]
                        if v not in (None, "", "None"))
    cards = [
        # RAW till record ONLY — the product sheet carries pre-filled content that is NOT
        # Microinvest source data (owner report 2026-07-17). No photo/desc/attrs here.
        _sf_card("🏬 Microinvest (склад — сурови данни)", "src-mi", None,
                 sup.get("Стока") or mi.get("Наименование"), price, None, None,
                 '<span class="rawnote">сурово складово име · без описание/снимка/атрибути</span>',
                 chips_html=_mi_chips),
        _supplier_card(code, mi, sup),
    ]
    if canon_rec is None:
        # Not yet enriched: sources only + a queue placeholder card.
        cards.append('<div class="sfcard pend"><div class="lbl">⏳ В опашката</div>'
                     '<div class="sfdesc">Продуктът още не е обработен от агентите. '
                     'Ще се появи тук след обогатяване.</div></div>')
        nm = esc(mi.get("Наименование"))
        return (f'<section class="prow" id="row-{esc(code)}"><h3><span class="rcode">{esc(code)}</span> {nm}'
                f' <span class="pendtag">необработен</span></h3><div class="cards">{"".join(cards)}</div></section>')
    snaps = db.snapshots(code)
    # V2 POLICY (owner 2026-07-18): v1 processing steps are HIDDEN by default so the
    # human reviewer sees Microinvest + supplier + the v2 pipeline only. A version is
    # v2 if its notes carry the "v2" marker; the CURRENT (last) version always shows.
    # ?v1=1 restores the full history.
    if not show_v1:
        def _is_v2(rec):
            return "v2" in [str(n) for n in ((rec.get("meta") or {}).get("notes") or [])]
        last_v2 = max((i2 for i2, t in enumerate(snaps) if _is_v2(t[2])), default=None)
        if last_v2 is not None:
            kept = snaps[last_v2:]                      # latest v2 result + later stages
        else:
            kept = snaps[-1:]                           # not yet v2-processed
        n_hidden = len(snaps) - len(kept)
        snaps = kept
    else:
        n_hidden = 0
    for i, (ts, _s, rec) in enumerate(snaps):
        f = rec.get("fields") or {}
        is_cur = (i == len(snaps) - 1)
        stage, _ = H._stage_of((rec.get("meta") or {}).get("notes"))
        _m = rec.get("meta") or {}
        _isv2 = "v2" in [str(n) for n in (_m.get("notes") or [])]
        stage_lbl = ("⚙ v2 обработка" if _isv2 else stage)
        label = ("✔ Текущо състояние" if is_cur else stage_lbl) + (f" · {str(ts)[11:16]}" if ts else "")
        catline = ""
        if is_cur:
            _cat = str(f.get("Категории") or "").strip()
            _leaf = str(_m.get("leaf_name") or "").strip()
            if _cat or _leaf:
                catline = ('<div class="catline">'
                           + ('<span class="catchip">📁 ' + esc(_cat) + '</span>' if _cat else '')
                           + ('<span class="catchip leaf">🌿 ' + esc(_leaf) + '</span>' if _leaf else '')
                           + '</div>')
        pf = (snaps[i - 1][2].get("fields") or {}) if i > 0 else None
        # EVERY card with a predecessor shows exactly what ITS stage changed: word-level
        # diff in name/description, per-key value diff inside attribute chips
        # ('Цвят: ~~Черен~~ Антрацит'), brand/meta value diffs, related-link diffs.
        if pf is not None:
            nm_html = (word_diff(pf.get("Наименование"), f.get("Наименование"))
                       if _strip_tags(pf.get("Наименование")) != _strip_tags(f.get("Наименование")) else None)
            if _strip_tags(pf.get("Описание")).split() != _strip_tags(f.get("Описание")).split():
                desc_html = word_diff(pf.get("Описание"), f.get("Описание"))
            else:
                desc_html = _safe_desc_html(f.get("Описание"))
            brand_html = (_val_diff(pf.get("Бранд"), f.get("Бранд"))
                          if str(pf.get("Бранд") or "").strip() != str(f.get("Бранд") or "").strip() else None)
            rel_changed = str(pf.get("Свързани") or "") != str(f.get("Свързани") or "")
            related = (_related_html(f.get("Свързани"), by_code, pf.get("Свързани"))
                       if (is_cur or rel_changed) else "")
            chips_html = _chips_diff(f.get("Атрибути"), pf.get("Атрибути"))
            metas = _meta_block(f, prev=pf, always=is_cur)
        else:
            nm_html, desc_html, brand_html = None, _safe_desc_html(f.get("Описание")), None
            related = _related_html(f.get("Свързани"), by_code) if is_cur else ""
            chips_html, metas = None, (_meta_block(f) if is_cur else "")
        buttons = ""
        data_attrs = ""
        if is_cur:
            # Edit -> fields become writable; Approve saves the edits as a new HUMAN
            # version and moves the product to the approved pile.
            _d = {"nm": f.get("Наименование"), "brand": f.get("Бранд"),
                  "attrs": f.get("Атрибути"), "desc": f.get("Описание"),
                  "metan": f.get("Мета наименование"), "metad": f.get("Мета описание"),
                  "rel": f.get("Свързани")}
            data_attrs = "".join(f' data-{k}="{html.escape(str(v or ""))}"' for k, v in _d.items())
            _rd, _vd = (rstate or (0, ""))
            if _vd == "human_approve":
                sugg = '<span class="approved-tag">✓ Одобрено от теб</span> '
            elif _rd == 1:
                sugg = '<span class="rvsugg">🔎 Рецензентът предлага: готов за сайта</span> '
            elif _vd and not _vd.startswith("human_"):
                sugg = '<span class="rvsugg warn">🔎 Рецензентът: има забележки</span> '
            else:
                sugg = ""
            buttons = (catline + f'<div class="acts" id="cur-acts-{esc(code)}">{sugg}'
                       f'<button class="approve" onclick="curApprove(\'{esc(code)}\')">✓ Одобри</button>'
                       f'<button class="edit" onclick="curEdit(\'{esc(code)}\')">✎ Редактирай</button></div>')
        cards.append(_sf_card(label, "current" if is_cur else "stage", code, f.get("Наименование"),
                              price, f.get("Бранд"), f.get("Атрибути"), desc_html,
                              related=related, name_html=nm_html, chips_html=chips_html,
                              metas=metas, brand_html=brand_html, buttons=buttons,
                              data_attrs=(f' id="cur-{esc(code)}"' + data_attrs) if is_cur else ""))
    rv = _reviewer_card(code, rvmap)
    if rv:
        cards.append(rv)
    nm = esc((canon_rec.get("fields") or {}).get("Наименование"))
    chip = ' <span class="famchip">⛓ свързан с горния</span>' if chained else ""
    if n_hidden:
        chip += (' <a class="v1link" href="/rows?code=' + esc(code) + '&v1=1" '
                 'title="покажи скритите v1 стъпки">🗂 ' + str(n_hidden) + ' v1</a>')
    return (f'<section class="prow" id="row-{esc(code)}"><h3><span class="rcode">{esc(code)}</span> {nm}{chip}</h3>'
            f'<div class="cards">{"".join(cards)}</div></section>')


ROWS_LIMIT = 60  # each row is heavy (source + every stage); page a manageable slice


def _review_locked():
    """{code: (ready, verdict)} from review_state. IMPORTANT (owner policy): the LLM
    reviewer's ready=1 is only a SUGGESTION — nothing counts as approved unless the
    verdict is a human one."""
    con = None
    try:
        con = db.connect()
        if not con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='review_state'").fetchone():
            return {}
        return {c: (r, v or "") for c, r, v in
                con.execute("SELECT code, ready, verdict FROM review_state").fetchall()}
    except Exception:
        return {}
    finally:
        if con is not None:
            con.close()


ROW_FILTERS = [("all", "Всички обработени"), ("needs_review", "За преглед"),
               ("suggested", "С предложение"), ("approved", "Одобрени"),
               ("unenriched", "Необработени")]


def render_rows(only_code=None, flt="all", page=0, show_v1=False):
    by_code = load_records()
    rvmap = _review_fixes_map()
    decisions = load_decisions()
    locked = _review_locked()
    unenriched_rows = ""
    total_in_filter = 0
    if only_code:
        # single-product view (related-product links): the product plus its relatives,
        # so review can hop through a variant family.
        rec = by_code.get(str(only_code))
        recs = [rec] if rec else []
        rel = re.split(r"[,;]+", str(((rec or {}).get("fields") or {}).get("Свързани") or ""))
        recs += [by_code[c.strip()] for c in rel if c.strip() in by_code]
    elif flt == "unenriched":
        # products with SOURCE data only — not yet enriched. Rendered from the DB task
        # store (source cards + a queue placeholder), so /rows covers the whole catalog.
        recs = []
        try:
            allc = db.all_task_codes()
            pend_all = [c for c in allc if c not in by_code]
            total_in_filter = len(pend_all)
            pend = pend_all[page * ROWS_LIMIT:(page + 1) * ROWS_LIMIT]
            tmap = db.get_tasks(pend)                   # one batched query, not 60
            unenriched_rows = "".join(product_row(c, None, rvmap, by_code, tmap.get(str(c)) or {},
                                                  rstate=locked.get(str(c)))
                                      for c in pend)
        except Exception as e:
            unenriched_rows = f'<section class="prow"><h3>Грешка: {esc(str(e)[:80])}</h3></section>'
    else:
        recs = sorted(by_code.values(), key=lambda r: r.get("ts") or "", reverse=True)
        if flt == "needs_review":
            recs = [r for r in recs if r.get("needs_human")
                    and (decisions.get(str(r.get("code"))) or {}).get("action") != "approve"]
        elif flt == "suggested":
            recs = [r for r in recs if str(r.get("code")) in rvmap]
        elif flt == "approved":
            recs = [r for r in recs if (decisions.get(str(r.get("code"))) or {}).get("action") == "approve"
                    or (locked.get(str(r.get("code"))) or (0, ""))[1] == "human_approve"]
        # FAMILY-ADJACENT ordering: a product's related items follow it immediately, so
        # variant families can be reviewed/renamed in one uninterrupted run.
        idx = {str(r.get("code")): r for r in recs}
        ordered, seen, chained = [], set(), set()
        for r in recs:
            c = str(r.get("code"))
            if c in seen:
                continue
            ordered.append(r); seen.add(c)
            rel = [x.strip() for x in re.split(r"[,;]+", str((r.get("fields") or {}).get("Свързани") or "")) if x.strip()]
            for rc in rel:
                if rc in idx and rc not in seen:
                    ordered.append(idx[rc]); seen.add(rc); chained.add(rc)
        recs = ordered
        total_in_filter = len(recs)
        recs = recs[page * ROWS_LIMIT:(page + 1) * ROWS_LIMIT]
    if not unenriched_rows:
        codes = [str(r.get("code")) for r in recs]
        tmap = db.get_tasks(codes)                      # one batched query per page
        rows = "".join(product_row(c, r, rvmap, by_code, tmap.get(c) or {},
                                   chained=(c in (chained if 'chained' in dir() else set())),
                                   rstate=locked.get(c), show_v1=show_v1)
                       for c, r in zip(codes, recs))
    else:
        rows = unenriched_rows
    if not rows:
        rows = '<section class="prow"><h3>Няма продукти за този филтър.</h3></section>'
    n = len(recs) if not unenriched_rows else unenriched_rows.count('class="prow"')
    tabs = "".join(f'<a class="ftab{" on" if flt == k else ""}" href="/?f={k}">{lbl}</a>'
                   for k, lbl in ROW_FILTERS)
    if only_code:
        pager = f'<a class="ftab" href="/?f=all">← всички</a>'
    else:
        pages = max(1, -(-total_in_filter // ROWS_LIMIT))
        prev_l = f'<a class="ftab" href="/?f={flt}&p={page-1}">← предишни</a>' if page > 0 else ''
        next_l = f'<a class="ftab" href="/?f={flt}&p={page+1}">следващи →</a>' if page + 1 < pages else ''
        pager = (f'{prev_l}<span class="pginfo">стр. {page+1}/{pages} · {total_in_filter} продукта</span>{next_l}')
    tabs += f'<span class="pager">{pager}</span>' 
    return (ROWS_PAGE.replace("{{ROWS}}", rows).replace("{{N}}", str(n))
            .replace("{{TABS}}", tabs))


ROWS_PAGE = r"""<!doctype html><html lang="bg"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Darling · преглед по етапи</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<style>
 :root{--cream:#FFF6E9;--vanilla:#FFE9C9;--cherry:#D42A3C;--honey:#E8A61B;--cocoa:#3A1D20;--line:#e7d9c4;}
 *{box-sizing:border-box}
 body{font:15px/1.5 system-ui,"Segoe UI",sans-serif;margin:0;background:var(--cream);color:var(--cocoa);}
 header{background:var(--vanilla);padding:.55rem 1.4rem;border-bottom:2px solid var(--honey);position:sticky;top:0;z-index:5;}
 header h1{font-family:"Playfair Display",serif;margin:0;font-size:1.25rem;color:var(--cocoa);}
 .hdr-top{display:flex;align-items:center;justify-content:space-between;gap:.6rem;}
 #hdr-toggle{font:inherit;font-size:.75rem;line-height:1;padding:.25rem .6rem;border:1px solid var(--honey);background:#fff;border-radius:10px;cursor:pointer;color:var(--cocoa);}
 header.collapsed .hdr-body{display:none;}
 header.collapsed{padding:.35rem 1.4rem;}
 header.collapsed h1{font-size:1.02rem;}
 header .sub{color:#8a6f52;font-size:.85rem;}
 .prow{padding:1rem 1.2rem;border-bottom:1px solid var(--line);}
 .prow h3{font-family:"Playfair Display",serif;font-size:1.05rem;margin:.2rem 0 .7rem;font-weight:600;}
 .rcode{font:600 .72rem/1 Consolas,monospace;background:#fff;border:1px solid var(--line);padding:.15rem .4rem;border-radius:4px;color:var(--cherry);margin-right:.4rem;}
 .cards{display:flex;gap:.8rem;overflow-x:auto;padding-bottom:.6rem;scroll-snap-type:x proximity;}
 .sfcard{flex:0 0 400px;max-height:760px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:.9rem;scroll-snap-align:start;display:flex;flex-direction:column;box-shadow:0 1px 3px rgba(58,29,32,.06);overflow:hidden;}
 .editpane{border-top:2px solid var(--cherry);margin-top:.5rem;padding-top:.5rem;}
 .edrow2{display:block;margin-bottom:.45rem;}
 .edrow2 span{display:block;font-size:.68rem;font-weight:700;text-transform:uppercase;color:#8a6f52;margin-bottom:.15rem;}
 .edrow2 textarea{width:100%;font:inherit;font-size:.82rem;padding:.35rem;border:1px solid var(--line);border-radius:6px;resize:vertical;box-sizing:border-box;}
 .approved-tag{color:#186034;font-weight:700;}
 .rvsugg{font-size:.8rem;background:#eaf3ff;color:#25508f;border:1px solid #c4dcf5;border-radius:10px;padding:.2rem .6rem;font-weight:600;}
 .rvsugg.warn{background:#fff4e0;color:#8a5a12;border-color:#f0d9a8;}
 .catline{margin:.3rem 0;display:flex;gap:.4rem;flex-wrap:wrap;}
 .catchip{font-size:.72rem;background:var(--vanilla);border:1px solid var(--honey);border-radius:9px;padding:.1rem .5rem;}
 .catchip.leaf{background:#eef8ee;border-color:#b5d9b5;color:#1d6b34;}
 .composebtn{font-size:.78rem;margin:-.2rem 0 .4rem 0;padding:.25rem .6rem;border:1px solid var(--honey);background:var(--vanilla);border-radius:8px;cursor:pointer;}
 .composebtn:hover{background:var(--honey);}
 .minitoast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#333;color:#fff;padding:.5rem 1rem;border-radius:8px;font-size:.85rem;z-index:99;}
 .relchips{display:flex;flex-wrap:wrap;gap:.3rem;margin-bottom:.3rem;}
 .relchip{font-size:.76rem;background:var(--vanilla);border:1px solid var(--honey);border-radius:10px;padding:.15rem .5rem;font-family:Consolas,monospace;}
 .relchip a{color:#a12020;cursor:pointer;font-weight:700;margin-left:.2rem;}
 .reladd{width:100%;font:inherit;font-size:.82rem;padding:.35rem;border:1px solid var(--line);border-radius:6px;box-sizing:border-box;}
 .reldrawer{background:#fff;border:1px solid var(--line);border-radius:6px;max-height:220px;overflow-y:auto;}
 .reldrawer:empty{display:none;}
 .reldrawer-item{display:flex;align-items:center;gap:.4rem;padding:.3rem .45rem;cursor:pointer;font-size:.78rem;border-bottom:1px solid #f2ece0;}
 .reldrawer-item:hover{background:var(--cream);}
 .reldrawer-item img{width:34px;height:34px;object-fit:contain;background:var(--cream);border-radius:5px;}
 .reldrawer-item b{color:var(--cherry);font-family:Consolas,monospace;}
 .rawnote{color:#8a6f52;font-style:italic;font-size:.78rem;}
 .morepics{border-top:1px dashed var(--line);margin-top:.4rem;padding-top:.35rem;}
 .morepics img{width:44px;height:44px;object-fit:contain;background:var(--cream);border:1px solid var(--line);border-radius:6px;margin-right:.25rem;cursor:zoom-in;}
 .v1link{font-size:.68rem;color:#8a7d68;text-decoration:none;border:1px dashed var(--honey);border-radius:8px;padding:.05rem .4rem;}
 .famchip{font-size:.68rem;font-weight:700;background:#f0e6ff;color:#6b3fa0;border-radius:10px;padding:.12rem .5rem;vertical-align:middle;}
 .sfcard .lbl{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.03em;color:#8a6f52;margin-bottom:.4rem;}
 .sfcard.src-mi{background:#fff9f0;border-color:var(--honey);} .sfcard.src-mi .lbl{color:var(--honey);}
 .sfcard.src-sup{background:#f0f6ff;border-color:#8fb3e0;} .sfcard.src-sup .lbl{color:#3a6ea5;}
 .sfcard.current{border:2px solid var(--cherry);background:#fff;} .sfcard.current .lbl{color:var(--cherry);}
 .sfcard.reviewer{background:#f6f0ff;border-color:#b79be0;} .sfcard.reviewer .lbl{color:#6b3fa0;}
 .ph{height:150px;background:var(--cream);border-radius:8px;display:flex;align-items:center;justify-content:center;overflow:hidden;margin-bottom:.5rem;}
 .ph img{max-width:100%;max-height:100%;object-fit:contain;}
 .nm{font-family:"Playfair Display",serif;font-size:.95rem;font-weight:600;line-height:1.25;margin-bottom:.3rem;}
 .meta{display:flex;gap:.5rem;align-items:baseline;margin-bottom:.4rem;flex-wrap:wrap;}
 .price{color:var(--cherry);font-weight:700;} .brand{font-size:.78rem;color:#8a6f52;}
 .chips{display:flex;flex-wrap:wrap;gap:.25rem;margin-bottom:.4rem;}
 .chip{font-size:.68rem;background:var(--vanilla);border-radius:10px;padding:.1rem .45rem;color:var(--cocoa);}
 .sfdesc{font-size:.84rem;line-height:1.55;color:#5d4b39;overflow-y:auto;flex:1;min-height:4.5rem;padding-right:.25rem;}
 .sfdesc h2,.sfdesc h3{font-size:.85rem;margin:.3rem 0 .2rem;font-family:"Playfair Display",serif;}
 .sfdesc p{margin:.2rem 0;} .sfdesc ul{margin:.2rem 0;padding-left:1.1rem;} .sfdesc li{margin:.1rem 0;}
 .rels{border-top:1px dashed var(--line);margin-top:.4rem;padding-top:.35rem;}
 .rels-h{font-size:.68rem;font-weight:700;text-transform:uppercase;color:#8a6f52;margin-bottom:.25rem;}
 .rel{display:flex;align-items:center;gap:.4rem;font-size:.74rem;color:var(--cocoa);text-decoration:none;padding:.15rem 0;}
 .rel:hover span{color:var(--cherry);}
 .rel img{width:30px;height:30px;object-fit:contain;background:var(--cream);border-radius:6px;border:1px solid var(--line);flex:0 0 30px;}
 .rel b{color:var(--cherry);font-family:Consolas,monospace;font-weight:600;margin-right:.2rem;}
 .sfcard del{color:#a12020;background:#fbe3e3;text-decoration:line-through;border-radius:2px;padding:0 .12rem;}
 .sfcard ins{color:#186034;background:#d8f0dd;text-decoration:none;border-radius:2px;padding:0 .12rem;}
 .chip.add{background:#d8f0dd;color:#186034;border:1px solid #9fd3ac;}
 .chip.del{background:#fbe3e3;color:#a12020;text-decoration:line-through;border:1px solid #e5b3b3;}
 .rel.add span{color:#186034;} .rel.add{background:#eef9f0;border-radius:6px;}
 .rel.del span{color:#a12020;text-decoration:line-through;} .rel.del{opacity:.75;}
 .metas{border-top:1px dashed var(--line);margin-top:.4rem;padding-top:.35rem;}
 .meta-row{font-size:.74rem;margin-bottom:.3rem;}
 .mlabel{font-weight:700;color:#8a6f52;text-transform:uppercase;font-size:.66rem;margin-right:.3rem;}
 .seo-ok{color:#186034;font-weight:700;} .seo-bad{color:#a12020;font-weight:700;}
 .mlen{color:#8a6f52;font-size:.7rem;}
 .mval{color:#6f5a44;margin-top:.1rem;}
 .srclink{font-size:.75rem;color:#3a6ea5;margin-top:.3rem;display:inline-block;}
 .rvauto{font-size:.75rem;color:#166534;margin-bottom:.3rem;} .rvprop{font-size:.76rem;margin-bottom:.35rem;}
 .rvnew{background:#e9f7ee;border-radius:6px;padding:.2rem .4rem;margin-top:.1rem;}
 .acts{margin-top:auto;display:flex;gap:.4rem;padding-top:.5rem;}
 .acts button{font:inherit;font-size:.8rem;font-weight:600;padding:.35rem .7rem;border-radius:6px;cursor:pointer;border:1px solid var(--line);}
 .acts .approve{background:var(--cherry);color:#fff;border-color:var(--cherry);} .acts .edit{background:#fff;}
 .nav{margin-top:.4rem;font-size:.85rem;} .nav a{color:var(--cherry);text-decoration:none;margin-right:1rem;}
 .ftabs{margin-top:.55rem;display:flex;gap:.4rem;flex-wrap:wrap;}
 .ftab{font-size:.8rem;font-weight:600;padding:.28rem .75rem;border-radius:14px;border:1px solid var(--honey);color:var(--cocoa);text-decoration:none;background:#fff;}
 .ftab.on{background:var(--cherry);border-color:var(--cherry);color:#fff;}
 .pager{margin-left:auto;display:flex;gap:.5rem;align-items:center;}
 .pginfo{font-size:.78rem;color:#8a6f52;font-weight:600;}
 .sfcard.pend{background:#f4f4f2;border-style:dashed;} .sfcard.pend .lbl{color:#8a8a86;}
 .pendtag{font-size:.68rem;font-weight:700;background:#eee;border-radius:10px;padding:.12rem .5rem;color:#777;vertical-align:middle;}
</style></head><body>
<header id="hdr"><div class="hdr-top"><h1>Darling · преглед по етапи</h1>
 <button id="hdr-toggle" onclick="toggleHdr()" title="свий/разгъни">▲</button></div>
 <div class="hdr-body">
  <div class="sub">Всеки продукт: Microinvest → доставчик → етапи на обработка → текущо състояние → предложение на рецензента. Показани {{N}}.</div>
  <div class="ftabs">{{TABS}}</div>
  <div class="nav"><a href="/classic">Класически изглед</a><a href="/rows">Преглед по етапи</a><a href="/naming">Именуване</a><a href="/vocab">Типове</a><a href="/brands">Брандове</a><a href="/schema">Категории</a><a href="/lessons">Уроци</a><a href="/dupes">Дубликати</a><a href="/readiness">Готовност</a><a href="/ops">Обработка</a><a href="/help" style="font-weight:700">❓ Помощ</a></div>
 </div></header>
{{ROWS}}
<script>
async function rvDecide(code, action){
  try{ await fetch('/api/decide',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({code,action,source:'reviewer'})});
    alert('Записано: '+action); }catch(e){ alert('Грешка: '+e); }
}
function toggleHdr(){
  const h = document.getElementById('hdr');
  h.classList.toggle('collapsed');
  const on = h.classList.contains('collapsed');
  document.getElementById('hdr-toggle').textContent = on ? '▼' : '▲';
  try{ localStorage.setItem('hdrCollapsed', on ? '1' : ''); }catch(e){}
}
try{ if (localStorage.getItem('hdrCollapsed')==='1') toggleHdr(); }catch(e){}
const FIELD_MAP = {nm:'Наименование', brand:'Бранд', attrs:'Атрибути', desc:'Описание', metan:'Мета наименование', metad:'Мета описание'};
function curEdit(code){
  const card = document.getElementById('cur-'+code);
  if (!card || card.querySelector('.editpane')) return;
  card.style.maxHeight = 'none';                 // card is height-capped; let the form show
  const pane = document.createElement('div');
  pane.className = 'editpane';
  for (const [k, label] of Object.entries(FIELD_MAP)){
    const wrap = document.createElement('label');
    wrap.className = 'edrow2';
    const span = document.createElement('span'); span.textContent = label; wrap.appendChild(span);
    const ta = document.createElement('textarea');
    ta.rows = (k==='desc') ? 8 : (k==='attrs' ? 3 : 2);
    ta.dataset.f = k;
    ta.value = card.dataset[k] || '';
    wrap.appendChild(ta);
    pane.appendChild(wrap);
    if (k === 'nm'){
      const bt = document.createElement('button');
      bt.type = 'button'; bt.className = 'composebtn';
      bt.textContent = '↻ Състави името от атрибутите';
      bt.title = 'Бранд + Материал + Форма + Тип + Размер (по конвенцията)';
      bt.onclick = async () => {
        const attrs = pane.querySelector('textarea[data-f="attrs"]');
        const brand = pane.querySelector('textarea[data-f="brand"]');
        const r = await fetch('/api/buildname?nm=' + encodeURIComponent(ta.value)
          + '&brand=' + encodeURIComponent(brand ? brand.value : '')
          + '&attrs=' + encodeURIComponent(attrs ? attrs.value : ''));
        const d = await r.json();
        if (d.name) { ta.value = d.name; toastMini('Съставено от атрибутите'); }
        else toastMini('Не може: ' + (d.reason || 'липсва Тип в атрибутите'));
      };
      pane.appendChild(bt);
    }
  }
  // --- connected-products editor: chips with x, autocomplete add box ---
  const relWrap = document.createElement('div');
  relWrap.className = 'edrow2';
  const relLbl = document.createElement('span'); relLbl.textContent = 'Свързани продукти'; relWrap.appendChild(relLbl);
  const chips = document.createElement('div'); chips.className = 'relchips'; relWrap.appendChild(chips);
  (card.dataset.rel || '').split(/[,;]+/).map(x => x.trim()).filter(Boolean).forEach(c => addRelChip(chips, c));
  const inp = document.createElement('input');
  inp.type = 'text'; inp.placeholder = 'код или име на продукт…'; inp.className = 'reladd';
  relWrap.appendChild(inp);
  const drawer = document.createElement('div'); drawer.className = 'reldrawer'; relWrap.appendChild(drawer);
  let relT = null;
  inp.addEventListener('input', () => {
    clearTimeout(relT);
    const q = inp.value.trim();
    if (q.length < 2) { drawer.innerHTML = ''; return; }
    relT = setTimeout(async () => {
      try {
        const r = await fetch('/api/prodsearch?q=' + encodeURIComponent(q));
        const items = await r.json();
        drawer.innerHTML = '';
        items.forEach(it => {
          const row = document.createElement('div');
          row.className = 'reldrawer-item';
          const im = document.createElement('img'); im.loading = 'lazy';
          im.src = '/thumb?code=' + encodeURIComponent(it.code); im.onerror = () => im.remove();
          const bb = document.createElement('b'); bb.textContent = it.code;
          const sp = document.createElement('span'); sp.textContent = it.name || '';
          row.append(im, bb, ' ', sp);
          row.onclick = () => { addRelChip(chips, it.code); inp.value = ''; drawer.innerHTML = ''; inp.focus(); };
          drawer.appendChild(row);
        });
      } catch (e) {}
    }, 250);
  });
  pane.appendChild(relWrap);
  card.appendChild(pane);
  card.querySelector('.edit').textContent = '✕ Откажи редакцията';
  card.querySelector('.edit').onclick = () => { pane.remove(); card.style.maxHeight=''; resetEditBtn(code); };
}
function resetEditBtn(code){
  const card = document.getElementById('cur-'+code);
  const b = card && card.querySelector('.edit');
  if (b){ b.textContent = '✎ Редактирай'; b.onclick = () => curEdit(code); }
}
function addRelChip(container, code){
  if ([...container.querySelectorAll('.relchip')].some(c => c.dataset.code === code)) return;
  const chip = document.createElement('span');
  chip.className = 'relchip'; chip.dataset.code = code;
  chip.innerHTML = code + ' <a>×</a>';
  chip.querySelector('a').onclick = () => chip.remove();
  container.appendChild(chip);
}
function toastMini(msg){
  const t = document.createElement('div'); t.className = 'minitoast'; t.textContent = msg;
  document.body.appendChild(t); setTimeout(() => t.remove(), 2200);
}
async function curApprove(code){
  const card = document.getElementById('cur-'+code);
  const pane = card && card.querySelector('.editpane');
  let fields = null, source = 'human';
  if (pane){
    fields = {};
    pane.querySelectorAll('textarea').forEach(t => { fields[FIELD_MAP[t.dataset.f]] = t.value; });
    const rel = [...pane.querySelectorAll('.relchip')].map(c => c.dataset.code);
    fields['Свързани'] = rel.join(', ');
    source = 'human_edit';
  }
  try{
    await fetch('/api/decide',{method:'POST',headers:{'Content-Type':'application/json'},
      body: JSON.stringify({code, action:'approve', fields, source})});
    const acts = document.getElementById('cur-acts-'+code);
    if (acts) acts.innerHTML = '<span class="approved-tag">✓ Одобрено'+(pane?' (с редакции)':'')+'</span>';
    if (pane) pane.remove();
  }catch(e){ alert('Грешка: '+e); }
}
</script>
</body></html>"""


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"                       # keep-alive: a /rows page fires
    # hundreds of /thumb requests; HTTP/1.0 opened a new TCP conn + thread for each.

    def _send(self, code, body, ctype="text/html; charset=utf-8"):
        b = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/index.html", "/rows"):       # row-of-cards view is the MAIN page
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            try:
                _pg = max(0, int((q.get("p") or ["0"])[0]))
            except ValueError:
                _pg = 0
            self._send(200, render_rows((q.get("code") or [None])[0],
                                        (q.get("f") or ["all"])[0], _pg,
                                        show_v1=(q.get("v1") or ["0"])[0] == "1"))
        elif path == "/classic":                        # the old console, kept as a tab
            self._send(200, render())
        elif path == "/history":
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            code = (q.get("code") or [""])[0]
            self._send(200, history_page(code))
        elif path == "/help":
            import schema_help
            self._send(200, schema_help.help_page())
        elif path == "/menu":
            import schema_menu
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            try:
                mn = int((q.get("min") or ["30"])[0])
            except Exception:
                mn = 30
            self._send(200, schema_menu.menu_page(mn))
        elif path == "/taxonomy":
            import schema_taxonomy
            self._send(200, schema_taxonomy.taxonomy_page())
        elif path == "/naming":
            import schema_pages
            self._send(200, schema_pages.naming_page())
        elif path == "/lessons":
            import schema_pages2
            self._send(200, schema_pages2.lessons_page())
        elif path == "/readiness":
            import schema_pages2
            self._send(200, schema_pages2.readiness_page())
        elif path == "/dupes":
            import schema_pages2
            self._send(200, schema_pages2.dupes_page())
        elif path == "/vocab":
            import schema_pages2
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            self._send(200, schema_pages2.vocab_page(str((q.get("q") or [""])[0])))
        elif path == "/ops":
            import schema_pages2
            self._send(200, schema_pages2.ops_page())
        elif path == "/brands":
            import schema_pages
            self._send(200, schema_pages.brands_page())
        elif path == "/schema":
            import schema_pages
            self._send(200, schema_pages.schema_page())
        elif path == "/api/stats":
            try:
                con = db.connect()
                enr = con.execute("SELECT COUNT(*) FROM products").fetchone()[0]
                appr = con.execute("SELECT COUNT(*) FROM review_state "
                                   "WHERE verdict='human_approve'").fetchone()[0]
                sugg = con.execute("SELECT COUNT(*) FROM review_state WHERE ready=1 "
                                   "AND verdict NOT LIKE 'human_%'").fetchone()[0]
                con.close()
                out = {"enriched": enr, "total": 14159, "approved": appr, "suggested": sugg}
            except Exception as e:
                out = {"error": str(e)[:80]}
            self._send(200, json.dumps(out), "application/json; charset=utf-8")
        elif path == "/api/naming/log":
            import schema_pages
            self._send(200, json.dumps(schema_pages.rerender_log_tail(), ensure_ascii=False),
                       "application/json; charset=utf-8")
        elif path == "/api/buildname":
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            fields = {"Наименование": str((q.get("nm") or [""])[0]),
                      "Бранд": str((q.get("brand") or [""])[0]),
                      "Атрибути": str((q.get("attrs") or [""])[0])}
            try:
                import name_builder as _nb
                nm, reason = _nb.build_name(fields, _nb.load_vocab())
            except Exception as e:
                nm, reason = None, str(e)[:80]
            self._send(200, json.dumps({"name": nm, "reason": reason}, ensure_ascii=False),
                       "application/json; charset=utf-8")
        elif path == "/api/prodsearch":
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            term = str((q.get("q") or [""])[0]).strip()
            out = []
            if len(term) >= 2:
                con = db.connect()
                try:
                    seen = set()
                    for sql, arg in (("SELECT code, fields_json FROM products WHERE code LIKE ? LIMIT 12",
                                      term + "%"),
                                     ("SELECT code, fields_json FROM products WHERE fields_json LIKE ? LIMIT 12",
                                      "%" + term + "%")):
                        for code2, fj in con.execute(sql, (arg,)).fetchall():
                            if code2 in seen:
                                continue
                            seen.add(code2)
                            try:
                                nm = (json.loads(fj or "{}").get("Наименование") or "")[:60]
                            except Exception:
                                nm = ""
                            out.append({"code": str(code2), "name": nm})
                            if len(out) >= 8:
                                break
                        if len(out) >= 8:
                            break
                finally:
                    con.close()
            self._send(200, json.dumps(out, ensure_ascii=False), "application/json; charset=utf-8")
        elif path == "/thumb":
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            data = thumb_bytes((q.get("code") or [""])[0])
            if data:
                self._send(200, data, "image/jpeg")
            else:
                self._send(404, b"", "image/jpeg")
        else:
            self._send(404, "not found", "text/plain; charset=utf-8")

    def do_POST(self):
        if self.path in ("/api/naming", "/api/brands", "/api/lessons",
                         "/api/readiness", "/api/dupes", "/api/vocab"):
            import schema_pages
            import schema_pages2
            _H = {"/api/naming": schema_pages.handle_naming_post,
                  "/api/brands": schema_pages.handle_brands_post,
                  "/api/lessons": schema_pages2.handle_lessons_post,
                  "/api/readiness": schema_pages2.handle_readiness_post,
                  "/api/dupes": schema_pages2.handle_dupes_post,
                  "/api/vocab": schema_pages2.handle_vocab_post}
            n = int(self.headers.get("Content-Length") or 0)
            try:
                data = json.loads(self.rfile.read(n).decode("utf-8"))
                out = _H[self.path](data)
            except Exception as e:
                out = {"error": str(e)[:200]}
            return self._send(200, json.dumps(out, ensure_ascii=False),
                              "application/json; charset=utf-8")
        if self.path != "/api/decide":
            return self._send(404, "not found", "text/plain")
        n = int(self.headers.get("Content-Length") or 0)
        try:
            data = json.loads(self.rfile.read(n).decode("utf-8"))
            code, action = str(data["code"]), data["action"]
        except Exception as e:
            return self._send(400, json.dumps({"error": str(e)}), "application/json")
        fields = None
        if action == "approve":
            fields = data.get("fields") or None
        # A reviewer-card approve applies the REVIEWER's proposed values.
        if action == "approve" and not fields and data.get("source") == "reviewer":
            latest = _review_fixes_map().get(code) or {}
            fields = {p.get("поле"): p.get("нов") for p in (latest.get("предложения") or [])
                      if p.get("поле") and p.get("нов")} or None
        # The vision-proposal fallback belongs ONLY to the classic proposal card (which
        # displays that proposal and sends no source). A plain /rows Одобри (source
        # 'human') must approve the CURRENT state — never a proposal the owner never saw.
        if action == "approve" and not fields and not data.get("source"):
            fields = ((db.get_record(code) or {}).get("vision_correction") or {}).get("proposed")
        # HUMAN EDIT: the reviewer edited fields inline before approving — persist them
        # as a new product VERSION (JSONL first, then DB) so the edit IS the product,
        # not just an approval note.
        if action == "approve" and fields and data.get("source") in ("human_edit", "reviewer"):
            try:
                rec = db.get_record(code)
                if rec:
                    nf = dict(rec.get("fields") or {})
                    nf.update({k: v for k, v in fields.items() if k in EDIT_ALL_FIELDS})
                    nd = dict(rec)
                    nd["fields"] = nf
                    nd["ts"] = datetime.now().isoformat(timespec="seconds")
                    nd["needs_human"] = False
                    meta = dict(nd.get("meta") or {})
                    meta["notes"] = list(meta.get("notes") or []) + [
                        "human_edit" if data.get("source") == "human_edit" else "reviewer_applied"]
                    nd["meta"] = meta
                    with open(HERE / "results.lanez_human.jsonl", "a", encoding="utf-8") as hf:
                        hf.write(json.dumps(nd, ensure_ascii=False) + "\n")
                        hf.flush()
                    db.record_version(nd)
            except Exception as e:
                print(f"human_edit persist failed for {code}: {e}", flush=True)
        record_decision(code, action, fields)
        # A human decision also stamps the option-B review_state: an approve is
        # reviewed+ready+LOCKED; an UNDO removes the stamp so the product re-queues.
        try:
            import review_all as _rall
            con = db.connect(); _rall._ensure(con)
            if action == "undo":
                con.execute("DELETE FROM review_state WHERE code=? AND verdict LIKE 'human_%'", (code,))
            elif action in ("approve", "reject"):
                rec = db.get_record(code)
                if rec:
                    con.execute("INSERT OR REPLACE INTO review_state(code,sig,reviewed_ts,ready,verdict) "
                                "VALUES(?,?,?,?,?)",
                                (code, _rall.signature(rec),
                                 datetime.now().isoformat(timespec="seconds"),
                                 1 if action == "approve" else 0,
                                 f"human_{action}"))
            con.commit(); con.close()
        except Exception as e:
            print(f"review_state stamp failed for {code}: {e}", flush=True)
        self._send(200, json.dumps({"ok": True}), "application/json; charset=utf-8")

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"review console on http://127.0.0.1:{PORT}/  (approvals -> {APPROVALS.name})")
    srv.serve_forever()
