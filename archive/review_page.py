# -*- coding: utf-8 -*-
"""Generate the human-review HTML page from results.jsonl (needs_human items).

Each card shows the product photo (hotlinked), the produced fields, what the
agents flagged, and the ground-truth reference — everything needed to decide
in one glance. Output: ../results/review_page.html (open in any browser).

Usage: python review_page.py [max_items]
"""
import html
import io
import json
import sys
from datetime import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = Path(__file__).parent
RESULTS = HERE / "results.jsonl"
TASKS = HERE / "tasks.jsonl"
OUT = HERE.parent / "results" / "review_page.html"


def esc(v):
    return html.escape(str(v)) if v not in (None, "") else "—"


def flag_reason(r, notes):
    """One plain-Bulgarian sentence for WHY a product needs a human."""
    strip = lambda n: n[7:] if n.startswith("review_") else n
    s = [strip(n) for n in notes]
    if any(n.startswith("vision_mismatch") for n in s):
        return "Снимката не съответства на описанието (тип/форма/цвят) — провери и коригирай."
    if any(n.startswith("weak_match") for n in s):
        return "Скрейпнатите данни са по приблизително име — може да описват друг продукт."
    if any(n.startswith("final_misspelled:") for n in s):
        return "Останаха съмнителни думи в текста след автоматичната корекция."
    if any(n.startswith("duplicate_desc_of") for n in s):
        return "Описанието съвпада с друг продукт — нужен е уникален текст."
    if any(n.startswith("review_fact_conflict") for n in s):
        return "Разминаване между източниците за категория/бранд/свързани продукти."
    if any("no_visual" in n or n.startswith("vision_unverified") for n in s):
        return "Има снимка, но визуалната проверка не успя — потвърди ръчно."
    return "Агентът отбеляза нерешен въпрос — виж бележките."


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    records = []
    for rp in [RESULTS, *HERE.glob("results.lane*.jsonl")]:
        if Path(rp).exists():
            records += [json.loads(l) for l in open(rp, encoding="utf-8") if l.strip()]
    records.sort(key=lambda r: r.get("ts") or "")
    flagged = records[:limit]  # all processed products; cards carry a status class
    codes = {r["code"] for r in flagged}

    tasks = {}
    if codes:
        with open(TASKS, encoding="utf-8") as f:
            for line in f:
                t = json.loads(line)
                if t["code"] in codes:
                    tasks[t["code"]] = t

    cards = []
    for r in flagged:
        t = tasks.get(r["code"], {})
        orig = t.get("product", {})
        gt = t.get("ground_truth", {})
        f = r["fields"]
        img = (orig.get("Снимки") or "").split(";")[0].strip()
        issues = r.get("review", {}).get("issues") or []
        notes = r.get("meta", {}).get("notes") or []
        status_cls = "flagged" if r.get("needs_human") else "clean"
        badge = "за преглед" if r.get("needs_human") else "готов"
        reason = flag_reason(r, notes) if r.get("needs_human") else ""
        vv = r.get("vision_verify") or {}
        if vv.get("ok") is True:
            vis = '<span class="vis ok">снимка ✓</span>'
        elif vv.get("ok") is False:
            det = vv.get("detail", {})
            vis = f'<span class="vis bad">снимка ✗ {esc(det.get("забележка") or "разминаване")}</span>'
        else:
            vis = ""
        cards.append(f"""
<article class="{status_cls}">
  <header><span class="code">{esc(r['code'])}</span>
    <h2>{esc(f.get('Наименование'))}</h2>
    <span class="badge {status_cls}">{badge}</span>
    <span class="conf">{esc(r.get('confidence'))}</span>{vis}</header>
  {f'<p class="reason">⚠ {esc(reason)}</p>' if reason else ''}
  <div class="body">
    <div class="img">{f'<img loading="lazy" src="{html.escape(img)}">' if img else '<p class="noimg">няма снимка</p>'}</div>
    <dl>
      <dt>GT Стока</dt><dd>{esc(gt.get('Стока'))}</dd>
      <dt>Бранд</dt><dd>{esc(f.get('Бранд'))}</dd>
      <dt>Атрибути</dt><dd>{esc(f.get('Атрибути'))}</dd>
      <dt>Категория</dt><dd>{esc(f.get('Категории'))}</dd>
      <dt>Тегло</dt><dd>{esc(f.get('Тегло (кг)'))} кг</dd>
      <dt>Мета име</dt><dd>{esc(f.get('Мета наименование'))}</dd>
      <dt>Мета описание</dt><dd>{esc(f.get('Мета описание'))}</dd>
      <dt>Свързани</dt><dd>{esc(f.get('Свързани'))}</dd>
      <dt>Синоними</dt><dd class="notes">{esc(f.get('Синоними'))}</dd>
      <dt>Коригирано/бележки</dt><dd>{esc(r.get('Проблеми'))}</dd>
    </dl>
  </div>
  <details><summary>Описание</summary><div class="desc">{f.get('Описание') or '—'}</div></details>
</article>""")

    page = f"""<!doctype html><html lang="bg"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Продукти за човешки преглед — {datetime.now():%Y-%m-%d %H:%M}</title>
<style>
  :root {{ --line:#d9d6ce; --warn:#a33f00; --muted:#77746a; --accent:#2e6e64; }}
  body {{ font: 15px/1.5 "Segoe UI", system-ui, sans-serif; margin: 0 auto; max-width: 1000px;
         padding: 2rem 1rem; background: #f3f1ec; color: #26251f; }}
  h1 {{ font-size: 1.4rem; }} .sub {{ color: var(--muted); margin-bottom: 1.6rem; }}
  article {{ background: #fff; border: 1px solid var(--line); border-radius: 6px;
             margin-bottom: 1.2rem; padding: 1rem 1.2rem; }}
  article header {{ display: flex; gap: .7rem; align-items: baseline; }}
  article h2 {{ font-size: 1.02rem; margin: 0; flex: 1; }}
  .code {{ font: 600 .75rem/1 Consolas, monospace; color: var(--accent);
           border: 1px solid var(--line); padding: .2rem .45rem; border-radius: 3px; }}
  .conf {{ font-size: .75rem; color: var(--muted); }}
  .body {{ display: grid; grid-template-columns: 190px 1fr; gap: 1rem; margin-top: .8rem; }}
  @media (max-width: 640px) {{ .body {{ grid-template-columns: 1fr; }} }}
  .img img {{ max-width: 100%; border: 1px solid var(--line); border-radius: 4px; background: #fff; }}
  .noimg {{ color: var(--muted); }}
  dl {{ display: grid; grid-template-columns: 7.5rem 1fr; gap: .25rem .8rem; margin: 0; font-size: .88rem; }}
  dt {{ color: var(--muted); }} dd {{ margin: 0; }}
  .warn {{ color: var(--warn); }} .notes {{ font-family: Consolas, monospace; font-size: .78rem; }}
  details {{ margin-top: .8rem; font-size: .88rem; }} summary {{ cursor: pointer; color: var(--accent); }}
  .desc {{ border-top: 1px solid var(--line); margin-top: .5rem; padding-top: .5rem; }}
  .badge {{ font-size: .72rem; font-weight: 600; padding: .18rem .5rem; border-radius: 10px; }}
  .badge.flagged {{ background: #f7e3d3; color: var(--warn); }}
  .badge.clean {{ background: #dcefdd; color: #22662a; }}
  article.flagged {{ border-left: 3px solid var(--warn); }}
  article.clean {{ border-left: 3px solid #4d9955; }}
  .reason {{ margin: .5rem 0 0; font-size: .86rem; color: var(--warn); font-weight: 600; }}
  .vis {{ font-size: .72rem; padding: .18rem .5rem; border-radius: 10px; }}
  .vis.ok {{ background: #dcefdd; color: #22662a; }}
  .vis.bad {{ background: #f7d3d3; color: #a12020; }}
  .filters {{ margin-bottom: 1.4rem; display: flex; gap: .5rem; }}
  .filters button {{ font: inherit; padding: .35rem .9rem; border: 1px solid var(--line);
    background: #fff; border-radius: 4px; cursor: pointer; }}
  .filters button.active {{ background: var(--accent); color: #fff; border-color: var(--accent); }}
</style></head><body>
<h1>Обработени продукти</h1>
<p class="sub"><b>{len(flagged)}</b> обработени · <b>{sum(1 for r in flagged if not r.get('needs_human'))}</b> готови ·
<b>{sum(1 for r in flagged if r.get('needs_human'))}</b> за преглед ·
генерирано {datetime.now():%Y-%m-%d %H:%M}</p>
<p class="sub">„Готов" = минал през работник + текстово ревю + визуален контрол без открити проблеми.
„За преглед" = има конкретна причина (виж ⚠ на всяка карта). Бележките са какво е коригирано, не открити грешки.</p>
<div class="filters">
  <button class="active" onclick="flt('all',this)">Всички</button>
  <button onclick="flt('clean',this)">Готови</button>
  <button onclick="flt('flagged',this)">За преглед</button>
</div>
{''.join(cards)}
<script>
function flt(kind, btn) {{
  document.querySelectorAll('.filters button').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('article').forEach(a => {{
    a.style.display = (kind === 'all' || a.classList.contains(kind)) ? '' : 'none';
  }});
}}
</script>
</body></html>"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"{len(flagged)} flagged of {len(records)} results -> {OUT}")


if __name__ == "__main__":
    main()
