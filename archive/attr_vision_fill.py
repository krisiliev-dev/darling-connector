# -*- coding: utf-8 -*-
"""Vision attribute fill — the deferred half of reconciliation: colour/material for
products the reviewer flags as missing them. Uses ONE targeted vision call per product
(the free Qwen-VL chain, shared with the pipeline), so it's run in BOUNDED batches and
measured against telemetry before scaling.

  python attr_vision_fill.py [N]     # default 25

Append-only + reversible: results.lanez_attrvis.jsonl (ts bumped) + DB dual-write.
Only fills the groups that are actually MISSING; never overwrites an existing value.
"""
import json, re, sys
from datetime import datetime, timedelta
from pathlib import Path
import attr_reconcile as ar
import agent_enrich as ae
import filter_schema_store as fss

HERE = Path(__file__).parent
OUT = HERE / "results.lanez_attrvis.jsonl"
Q = ("Погледни продукта на снимката. Отговори САМО в този формат, с кратки български "
     "думи, без обяснения:\nЦвят: <основен цвят>\nМатериал: <основен материал>")


def _parse(ans, key):
    m = re.search(key + r"\s*:\s*([^\n;]+)", str(ans or ""), re.IGNORECASE)
    if not m:
        return ""
    v = m.group(1).strip(" .;-—")
    # reject non-answers
    if not v or len(v) > 40 or "не " in v.lower() or "unknown" in v.lower() or "?" in v:
        return ""
    return v[:1].upper() + v[1:]


def _add_attr(attrs, key, value):
    parts = [p.strip() for p in str(attrs or "").split(";") if p.strip()]
    parts.append(f"{key}: {value}")
    return "; ".join(parts)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    import db
    cats = fss.load()
    canon = db.canonical_records()
    tasks = db.get_tasks(list(canon))
    try:
        import telemetry as tel
        tel.reset()
    except Exception:
        tel = None

    targets = []
    for code, rec in canon.items():
        miss, _ = ar.missing_groups(rec, cats)
        visual = [g for g in miss if g.lower() in ("цвят", "материал")]
        img = ((tasks.get(code) or {}).get("product") or {}).get("Снимки") or ""
        img = img.split(";")[0].strip()
        if visual and img:
            targets.append((code, rec, visual, img))
        if len(targets) >= n:
            break

    filled = 0
    buf = []
    for code, rec, visual, img in targets:
        ans = ae._vision_ask(img, Q)
        f = dict(rec.get("fields") or {})
        added = []
        for g in visual:
            val = _parse(ans, g)
            if val and g.lower() not in str(f.get("Атрибути") or "").lower():
                f["Атрибути"] = _add_attr(f.get("Атрибути"), g, val)
                added.append(f"{g}={val}")
        if not added:
            print(f"  {code}: vision gave no usable value ({str(ans)[:50]!r})")
            continue
        nd = dict(rec)
        nd["fields"] = f
        try:
            nd["ts"] = (datetime.fromisoformat(rec.get("ts") or "")
                        + timedelta(seconds=5)).isoformat(timespec="seconds")
        except Exception:
            nd["ts"] = datetime.now().isoformat(timespec="seconds")
        meta = dict(nd.get("meta") or {})
        meta["notes"] = list(meta.get("notes") or []) + ["attr_vision_fill:" + ",".join(a.split("=")[0] for a in added)]
        nd["meta"] = meta
        buf.append(json.dumps(nd, ensure_ascii=False))
        try:
            db.record_version(nd)
        except Exception:
            pass
        filled += 1
        print(f"  {code}: +{added}")

    with open(OUT, "a", encoding="utf-8") as fh:
        for line in buf:
            fh.write(line + "\n")
    usage = tel.summary() if tel else {}
    print(f"\nfilled {filled}/{len(targets)} products -> {OUT.name}")
    print(f"vision tokens used: {usage.get('total_tokens')} over {usage.get('calls')} calls "
          f"(~{(usage.get('total_tokens') or 0)//max(filled,1)}/product)")
    print("REVERT: rm results.lanez_attrvis.jsonl && python db.py --ingest")


if __name__ == "__main__":
    main()
