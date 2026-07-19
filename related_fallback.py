# -*- coding: utf-8 -*-
"""Related-products FALLBACK — fills empty Свързани with the most textually similar
products from the SAME category, so every product has cross-sell links at launch
(research: PDP/cart recommendations are among the best-documented revenue lifts, and
~3/4 of our products had none).

Pure-python TF-IDF cosine over name+synonyms+attribute tokens, computed WITHIN each
category (keeps it relevant and O(small²)). Zero LLM, zero network. Only touches
products whose Свързани is EMPTY (the stronger signals — catalogue ±1, shared photo,
base-name variants — always win). Append-only + DB, revert by deleting the lanez file.

  python related_fallback.py            # dry-run stats + samples
  python related_fallback.py --apply
"""
import json, math, re, sys, collections
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "results.lanez_relfallback.jsonl"
CAP = 6
MIN_SIM = 0.18


def _tokens(f):
    blob = " ".join(str(f.get(k) or "") for k in ("Наименование", "Синоними", "Атрибути"))
    return [w for w in re.findall(r"[а-яa-z0-9]{3,}", blob.lower())]


def build(canon):
    # group by primary category
    bycat = collections.defaultdict(list)
    for code, rec in canon.items():
        f = rec.get("fields") or {}
        cat = str(f.get("Категории") or "").split(";")[0].strip()
        if cat:
            bycat[cat].append((code, f))
    fills = {}
    for cat, items in bycat.items():
        if len(items) < 3:
            continue
        docs = {c: collections.Counter(_tokens(f)) for c, f in items}
        df = collections.Counter()
        for tf in docs.values():
            for t in tf:
                df[t] += 1
        n = len(docs)
        vecs = {}
        for c, tf in docs.items():
            v = {t: (1 + math.log(cnt)) * math.log(n / (1 + df[t])) for t, cnt in tf.items() if df[t] < n * 0.8}
            norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
            vecs[c] = (v, norm)
        for c, f in items:
            if str(f.get("Свързани") or "").strip():
                continue                                # only fill EMPTY related
            v1, n1 = vecs[c]
            sims = []
            for c2, _f2 in items:
                if c2 == c:
                    continue
                v2, n2 = vecs[c2]
                small, big = (v1, v2) if len(v1) < len(v2) else (v2, v1)
                dot = sum(w * big.get(t, 0.0) for t, w in small.items())
                s = dot / (n1 * n2)
                if s >= MIN_SIM:
                    sims.append((s, c2))
            sims.sort(reverse=True)
            if sims:
                fills[c] = [c2 for _s, c2 in sims[:CAP]]
    return fills


def main(apply=False):
    import db
    canon = db.canonical_records()
    empty = sum(1 for r in canon.values() if not str((r.get("fields") or {}).get("Свързани") or "").strip())
    fills = build(canon)
    print(f"products: {len(canon)} | empty Свързани: {empty} | fillable by similarity: {len(fills)}")
    shown = 0
    for c, rel in fills.items():
        nm = str((canon[c].get("fields") or {}).get("Наименование"))[:44]
        rn = [str((canon[r].get("fields") or {}).get("Наименование"))[:34] for r in rel[:3]]
        print(f"  {c} ({nm}) -> {rel[:3]} {rn}")
        shown += 1
        if shown >= 6:
            break
    if not apply:
        print("\n(dry-run; --apply to write)")
        return
    changed = 0
    with open(OUT, "a", encoding="utf-8") as fh:
        for c, rel in fills.items():
            rec = canon[c]
            nf = dict(rec.get("fields") or {})
            nf["Свързани"] = ", ".join(rel)
            nd = dict(rec); nd["fields"] = nf
            try:
                base = datetime.fromisoformat(rec.get("ts") or "") + timedelta(seconds=9)
            except Exception:
                base = datetime.now()
            nd["ts"] = max(base, datetime.now()).isoformat(timespec="seconds")
            meta = dict(nd.get("meta") or {})
            meta["notes"] = list(meta.get("notes") or []) + ["related_fallback:tfidf"]
            nd["meta"] = meta
            fh.write(json.dumps(nd, ensure_ascii=False) + "\n")
            fh.flush()
            try:
                db.record_version(nd)
            except Exception:
                pass
            changed += 1
    print(f"\nfilled {changed} products -> {OUT.name}")
    print("REVERT: rm results.lanez_relfallback.jsonl && python db.py --ingest")


if __name__ == "__main__":
    main(apply="--apply" in sys.argv)
