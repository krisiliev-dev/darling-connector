# -*- coding: utf-8 -*-
"""Per-product provenance TIMELINE — what each stage changed, when, and whether it made
the product better or worse.

Reconstructs a chronological history for any product by merging every trace we keep:
  * every stored version in results.lane*.jsonl (enrichment, deterministic guards,
    field-tidy, reviewer auto-fix) — each is a state snapshot with a ts + meta.notes,
  * reviewer verdicts/proposals in review_fixes.jsonl,
  * human decisions in approvals.jsonl.

For consecutive snapshots it shows the FIELD-LEVEL diff and labels the stage from the
record's notes, so you can see exactly where a value improved — or regressed. A
--regressions scan flags, across the whole catalogue, any step where a field got worse
(catalogue number re-introduced, brand emptied, big content loss): the 'where/when did
a pipeline change make it worse' signal.

Usage:
  python history.py <code>            # timeline for one product
  python history.py --regressions     # catalogue-wide list of worsening steps
"""
import json, glob, sys, re
from pathlib import Path

HERE = Path(__file__).parent
FIELDS = ("Наименование", "Бранд", "Категории", "Атрибути", "Синоними", "Свързани",
          "Мета наименование", "Мета описание", "Описание", "Тегло (кг)")

# map a record's notes to a human stage label (first match wins)
_STAGE = [
    ("regression_restore", "♻️ Regression restore (recovered a lost value)"),
    ("field_tidy_applied", "🧹 Deterministic tidy (units/related/brand-marker)"),
    ("reviewer_autofix", "🔎 Reviewer auto-fix"),
    ("agent_fallback_direct", "🤖 Enrichment (agent fell back to direct)"),
    ("agentic", "🤖 Enrichment agent"),
]


def _stage_of(notes):
    ns = [str(n) for n in (notes or [])]
    for key, label in _STAGE:
        if any(n == key or n.startswith(key + ":") for n in ns):
            extra = [n for n in ns if n.startswith(("catnum_stripped", "brand_", "meta_trimmed",
                     "field_tidy", "reviewer_autofix", "confidence_", "reverted_"))]
            return label, extra
    return "• snapshot", []


def load_snapshots(code):
    """All stored versions of a code, sorted by ts. Prefers the indexed SQLite mirror
    (one keyed query) and falls back to scanning the lane files if the DB isn't ready."""
    try:
        import db
        if db.is_ready():
            snaps = db.snapshots(code)
            if snaps:
                return snaps
    except Exception:
        pass
    snaps = []
    for fp in glob.glob(str(HERE / "results.lane*.jsonl")):
        for line in open(fp, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if str(d.get("code")) == str(code):
                snaps.append((d.get("ts") or "", Path(fp).name, d))
    snaps.sort(key=lambda x: x[0])
    return snaps


def _load_jsonl_for(path, code):
    out = []
    if path.exists():
        for line in open(path, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            if str(o.get("code")) == str(code):
                out.append(o)
    return out


_CATCODE = re.compile(r"[A-Za-zА-Яа-я]{1,4}-?\d{2,}[A-Za-z]{0,2}")


def _quality_delta(field, before, after):
    """A crude better/worse signal for a single field change. Returns
    '+'(better) / '-'(worse) / '' (neutral)."""
    b, a = str(before or ""), str(after or "")
    if field == "Бранд":
        if b.strip() and not a.strip():
            return "-"                                 # brand lost
        if not b.strip() and a.strip():
            return "+"
    if field in ("Наименование", "Описание"):
        if _CATCODE.search(a) and not _CATCODE.search(b):
            return "-"                                 # a code got RE-introduced
        if _CATCODE.search(b) and not _CATCODE.search(a):
            return "+"                                 # a code got cleaned
        if len(a) < len(b) * 0.5 and len(b) > 30:
            return "-"                                 # >50% content vanished
    if field == "Свързани":
        if a.strip() and not b.strip():
            return "+"                                 # gained related links
    return ""


def diff_fields(prev, cur):
    changes = []
    for f in FIELDS:
        b, a = (prev or {}).get(f), (cur or {}).get(f)
        if str(b or "") != str(a or ""):
            changes.append((f, b, a, _quality_delta(f, b, a)))
    return changes


def build_timeline(code):
    """Structured chronological events for a product (used by the CLI and the review
    site). Each event: (kind, ts, label, payload, changes, record)."""
    snaps = load_snapshots(code)
    if not snaps:
        return []
    events = []
    prev_fields = None
    for ts, fname, d in snaps:
        stage, extra = _stage_of((d.get("meta") or {}).get("notes"))
        changes = diff_fields(prev_fields, d.get("fields")) if prev_fields is not None else None
        events.append(("snap", ts, stage, extra, changes, d))
        prev_fields = d.get("fields")
    for rf in _load_jsonl_for(HERE / "review_fixes.jsonl", code):
        events.append(("review", rf.get("ts") or "", "📝 Reviewer verdict", rf, None, None))
    for ap in _load_jsonl_for(HERE / "approvals.jsonl", code):
        events.append(("human", ap.get("ts") or "", "👤 Human review", ap, None, None))
    events.sort(key=lambda e: e[1])
    return events


def timeline(code):
    events = build_timeline(code)
    if not events:
        print(f"no records for {code}"); return
    print(f"\n===== TIMELINE for {code} =====")
    for kind, ts, label, payload, changes, d in events:
        print(f"\n[{ts}] {label}")
        if kind == "snap":
            if changes is None:
                fl = d.get("fields") or {}
                print(f"    created: {str(fl.get('Наименование'))[:70]!r}")
                print(f"    Бранд={fl.get('Бранд')!r} conf={d.get('confidence')} needs_human={d.get('needs_human')}")
            elif not changes:
                print("    (no field changes)")
            else:
                for f, b, a, q in changes:
                    tag = {"+": " ✅better", "-": " ⚠️WORSE", "": ""}[q]
                    print(f"    {f}{tag}:")
                    print(f"        - {str(b)[:90]!r}")
                    print(f"        + {str(a)[:90]!r}")
            if payload:
                print(f"    notes: {', '.join(payload)}")
        elif kind == "review":
            print(f"    готов_за_сайта={payload.get('готов_за_сайта')} | оценка={str(payload.get('оценка'))[:80]}")
            if payload.get("автоприложени"):
                print(f"    auto-applied: {list(payload['автоприложени'])}")
            for p in (payload.get("проблеми") or [])[:4]:
                print(f"      - [{p.get('тежест')}] {p.get('поле')}: {str(p.get('проблем'))[:70]}")
        elif kind == "human":
            print(f"    {json.dumps(payload, ensure_ascii=False)[:160]}")
    print()


def history_summary(code, max_events=14):
    """Compact TEXT timeline for the reviewer's prompt — one line per stage, changed
    fields with direction, regressions flagged. Token-light; empty string if the product
    has only its original version (nothing to say)."""
    events = build_timeline(code)
    if not events:
        return ""
    # Only surface history when it's INFORMATIVE — a regression, a re-processing, a
    # restore, or a prior reviewer/human pass. The normal path (one enrichment + routine
    # deterministic tidy) tells the reviewer nothing new and would just burn tokens.
    any_regression = False
    for kind, ts, label, payload, changes, d in events:
        if kind == "snap" and changes:
            if any(q == "-" for _f, _b, _a, q in changes):
                any_regression = True
    enrich_snaps = [e for e in events if e[0] == "snap" and str(e[2]).startswith("🤖")]
    has_restore = any(str(e[2]).startswith("♻️") for e in events)
    has_review_human = any(e[0] in ("review", "human") for e in events)
    if not (any_regression or has_restore or has_review_human or len(enrich_snaps) > 1):
        return ""
    lines = []
    had_regression = False
    for kind, ts, label, payload, changes, d in events[-max_events:]:
        short_ts = ts.replace("T", " ")[:16]
        if kind == "snap":
            if changes is None:
                fl = d.get("fields") or {}
                lines.append(f"[{short_ts}] {label}: създаден · Бранд={fl.get('Бранд')!r}")
            elif not changes:
                lines.append(f"[{short_ts}] {label}: (без промени)")
            else:
                bits = []
                for fld, b, a, q in changes:
                    if q == "-":
                        had_regression = True
                        bits.append(f"{fld} {str(b)[:22]!r}→{str(a)[:22]!r} ⚠️ПО-ЗЛЕ")
                    elif q == "+":
                        bits.append(f"{fld} ✅подобрено")
                    else:
                        bits.append(fld)
                lines.append(f"[{short_ts}] {label}: " + "; ".join(bits[:6]))
        elif kind == "review":
            lines.append(f"[{short_ts}] {label}: готов={payload.get('готов_за_сайта')} "
                         f"{str(payload.get('оценка') or '')[:50]}")
        elif kind == "human":
            act = payload.get("action") or payload.get("decision") or payload
            lines.append(f"[{short_ts}] {label}: {str(act)[:60]}")
    header = "ИСТОРИЯ НА ПРОДУКТА (какво и кога се е променяло по етапите):"
    if had_regression:
        header += ("\n⚠️ ВНИМАНИЕ: този продукт е РЕГРЕСИРАЛ на някой етап (виж 'ПО-ЗЛЕ'). "
                   "Провери дали текущата стойност не е по-лоша от по-ранна — ако верен "
                   "бранд/факт е бил загубен или каталожен код е върнат, отбележи го и предложи връщане.")
    return header + "\n" + "\n".join(lines)


def scan_regressions():
    """Every step, across all products, where a field got WORSE. The 'a pipeline change
    made it worse — where and when' detector."""
    bycode = {}
    for fp in glob.glob(str(HERE / "results.lane*.jsonl")):
        for line in open(fp, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("code"):
                bycode.setdefault(str(d["code"]), []).append(d)
    hits = []
    for code, ds in bycode.items():
        ds.sort(key=lambda d: d.get("ts") or "")
        for i in range(1, len(ds)):
            stage, _ = _stage_of((ds[i].get("meta") or {}).get("notes"))
            for f, b, a, q in diff_fields(ds[i - 1].get("fields"), ds[i].get("fields")):
                if q == "-":
                    hits.append((ds[i].get("ts"), code, stage, f, str(b)[:50], str(a)[:50]))
    hits.sort()
    print(f"\n{len(hits)} worsening steps found:\n")
    for ts, code, stage, f, b, a in hits[:60]:
        print(f"[{ts}] {code} {stage} | {f}: {b!r} -> {a!r}")
    if not hits:
        print("  none — no stored step degraded a tracked field.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    if "--regressions" in args:
        scan_regressions()
    elif args:
        timeline(args[0])
    else:
        print("usage: python history.py <code>   |   python history.py --regressions")
