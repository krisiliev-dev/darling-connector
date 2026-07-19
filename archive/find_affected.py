# -*- coding: utf-8 -*-
"""Identify already-processed records that still carry a catalogue residual the
regex can't safely resolve — so they can be re-queued for the improved agent.
Affected if: (a) a known series/collection token stands alone in the title, (b) the
brand is a compound/prefix/collection that isn't a real gazetteer brand, or (c) the
source leading-prefix / a source model code still survives in the title."""
import json, glob, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import catalogue_guard as cg
import brand_tools

gaz = brand_tools.load()
stoka = {}
for line in open("tasks.jsonl", encoding="utf-8", errors="replace"):
    if not line.strip():
        continue
    try:
        t = json.loads(line)
    except Exception:
        continue
    stoka[t.get("code")] = (t.get("ground_truth") or {}).get("Стока")

res = {}
for f in ["results.jsonl"] + sorted(glob.glob("results.lane*.jsonl")):
    if not os.path.exists(f):
        continue
    for line in open(f, encoding="utf-8", errors="replace"):
        if not line.strip():
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        if "agentic" in ((d.get("meta") or {}).get("notes") or []):
            res[d.get("code")] = d

def word_in(name, tok):
    return re.search(r"(?<![0-9A-Za-zА-Яа-я])" + re.escape(tok) + r"(?![0-9A-Za-zА-Яа-я])",
                     name, re.IGNORECASE) is not None

affected = {}
for code, d in res.items():
    if (d.get("review") or {}).get("verdict"):
        continue
    f = d.get("fields") or {}
    name = str(f.get("Наименование") or "")
    brand = str(f.get("Бранд") or "").strip()
    reasons = []
    # (a) a collection/series token stands alone in the title
    for tok in cg.COLLECTION_TOKENS:
        if word_in(name, tok):
            reasons.append(f"series_in_name:{tok}"); break
    # (b) brand is not a real gazetteer brand but is a compound / prefix / collection / material
    if brand and not brand_tools.lookup(brand, gaz):
        up = re.sub(r"[^0-9A-ZА-Я]", "", brand.upper())
        if ("-" in brand or "/" in brand
                or up in cg.COLLECTION_TOKENS or up in cg.CATALOGUE_PREFIXES
                or brand.lower() in cg.MATERIAL_WORDS
                or up in {"BR", "CN", "CNC", "COK", "AN", "HR", "KN"}):
            reasons.append(f"bad_brand:{brand}")
    # (c) source leading-prefix or a source model code still present in the title
    lead = cg.source_leading_prefix(stoka.get(code), gaz)
    if lead and word_in(name, lead):
        reasons.append(f"prefix_in_name:{lead}")
    for mc in cg.source_model_codes(stoka.get(code)):
        if word_in(name, mc):
            reasons.append(f"code_in_name:{mc}"); break
    if reasons:
        affected[code] = reasons

if "--write" in sys.argv:
    with open("reprocess_affected.txt", "w", encoding="utf-8") as f:
        for c in affected:
            f.write(c + "\n")

import collections
kinds = collections.Counter(r.split(":")[0] for rs in affected.values() for r in rs)
print(f"agentic records: {len(res)}")
print(f"affected (need reprocess): {len(affected)}")
print("reasons:", dict(kinds))
for c, rs in list(affected.items())[:15]:
    print(f"  {c}: {rs}  | {str((res[c].get('fields') or {}).get('Наименование'))[:55]!r}")
