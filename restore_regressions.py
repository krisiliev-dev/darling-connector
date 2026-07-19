# -*- coding: utf-8 -*-
"""Restore the products a past re-processing step degraded.

history.py --regressions flags steps where a field got WORSE (brand lost, catalogue
code re-introduced, big content loss) and last-wins then made the worse version
canonical. This script does a SURGICAL, FIELD-LEVEL restore: for each regressed field it
takes the good pre-regression value and writes it onto a copy of the CURRENT canonical
record (so later genuine improvements — unit tidy, related links — are kept). Only the
specific regressed fields are reverted.

Append-only + reversible: writes results.lanez_restore.jsonl (ts = latest+3s so it wins).
Delete that file to undo. Skips a field if the canonical has already moved off the bad
value (a later stage fixed it).
"""
import json, glob
from datetime import datetime, timedelta
from pathlib import Path
import history as H

HERE = Path(__file__).parent
OUT = HERE / "results.lanez_restore.jsonl"


def all_versions():
    by = {}
    for fp in glob.glob(str(HERE / "results.lane*.jsonl")):
        if Path(fp).name == OUT.name:
            continue
        for line in open(fp, encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("code"):
                by.setdefault(str(d["code"]), []).append(d)
    for c in by:
        by[c].sort(key=lambda d: d.get("ts") or "")
    return by


def main():
    versions = all_versions()
    # {code: {field: good_value}} — earliest good value before each regression
    good = {}
    for code, ds in versions.items():
        for i in range(1, len(ds)):
            for f, b, a, q in H.diff_fields(ds[i - 1].get("fields"), ds[i].get("fields")):
                if q == "-":
                    good.setdefault(code, {}).setdefault(f, b)

    restored = 0
    field_counts = {}
    buf = []
    for code, fixes in good.items():
        canon = versions[code][-1]                     # current canonical (latest ts)
        cf = dict(canon.get("fields") or {})
        applied = []
        for f, goodval in fixes.items():
            # BRAND-ONLY restore. Restoring an old Наименование/Описание is unsafe — the
            # newer version is often legitimately CLEANER (brand/catalogue code removed
            # from the title), so reverting it would re-introduce the leak. The one
            # unambiguous regression is a VERIFIED BRAND dropped to empty: recover it and
            # leave the (cleaner) current name in place -> clean name + real brand.
            if f != "Бранд":
                continue
            if str(goodval or "").strip() and not str(cf.get(f) or "").strip():
                cf[f] = goodval
                applied.append(f)
        if not applied:
            continue
        nd = dict(canon)
        nd["fields"] = cf
        try:
            nd["ts"] = (datetime.fromisoformat(canon.get("ts") or "")
                        + timedelta(seconds=3)).isoformat(timespec="seconds")
        except Exception:
            nd["ts"] = datetime.now().isoformat(timespec="seconds")
        meta = dict(nd.get("meta") or {})
        meta["notes"] = list(meta.get("notes") or []) + ["regression_restore:" + ",".join(applied)]
        nd["meta"] = meta
        buf.append(json.dumps(nd, ensure_ascii=False))
        try:
            import db as _db
            _db.record_version(nd)
        except Exception:
            pass
        restored += 1
        for f in applied:
            field_counts[f] = field_counts.get(f, 0) + 1
        print(f"  {code}: restored {applied}")
        for f in applied:
            print(f"      {f}: canonical {str(canon.get('fields',{}).get(f))[:55]!r}")
            print(f"           -> good  {str(fixes[f])[:55]!r}")

    OUT.write_text("\n".join(buf) + ("\n" if buf else ""), encoding="utf-8")
    print(f"\nrestored {restored} products -> {OUT.name}  (by field: {field_counts})")
    print("REVERT with: rm results.lanez_restore.jsonl")


if __name__ == "__main__":
    main()
