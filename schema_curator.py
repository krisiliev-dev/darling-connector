# -*- coding: utf-8 -*-
"""Schema curator — keeps the living filter schema COHERENT after the Shopify-taxonomy
baseline merge and the reviewer's ad-hoc adjustments.

Three passes:
  A) COMPOUND-KEY LEAK FIX (deterministic): schema keys covering two categories
     ("Фруктиери...; Великден") received taxonomy groups from BOTH; groups that belong
     only to the NON-primary category are removed (power-source on a fruit bowl).
  B) DUPLICATE MERGE (deterministic): a Shopify-added group whose normalized name
     contains/is contained by an existing group's name ("Материал на декорацията" vs
     "Материал") merges INTO the existing group — vocab united, provenance kept, and a
     RENAME MAP recorded.
  C) PRODUCT RENAME (append-only): products already carrying a merged-away attribute key
     get the key renamed so their attributes co-filter with the consolidated schema.

Every schema change goes through filter_schema_store.adjust() (logged, revertible);
product changes land in results.lanez_curator.jsonl (+DB), delete-to-revert.

  python schema_curator.py            # dry-run
  python schema_curator.py --apply
"""
import json, re, sys
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).parent
TAXO = HERE / "shopify_taxonomy"
OUT = HERE / "results.lanez_curator.jsonl"


def _norm(s):
    return re.sub(r"[^0-9a-zа-я]", "", str(s or "").lower())


def _taxonomy_handles():
    """{norm(bg category name): set(attribute handles)} from the taxonomy dist."""
    cats = json.load(open(TAXO / "categories.json", encoding="utf-8"))
    by_gid = {}
    for v in cats["verticals"]:
        for c in v["categories"]:
            by_gid[c["id"]] = {a.get("handle") for a in (c.get("attributes") or [])}
    catmap = json.loads((HERE / "category_shopify_map.json").read_text(encoding="utf-8"))
    out = {}
    for m in catmap:
        if m.get("bg") and m.get("shopify_id"):
            out[_norm(m["bg"])] = by_gid.get(m["shopify_id"]) or set()
    return out


def plan():
    import filter_schema_store as fss
    schema = fss.load()
    tax = _taxonomy_handles()
    leak_removals = {}                                   # key -> [group names removed]
    merges = {}                                          # key -> [(old_name, into_name)]
    new_schema = {}
    for key, groups in schema.items():
        groups = [g for g in groups if isinstance(g, dict)]
        # --- A: compound-key leaks ---
        parts = [p.strip() for p in str(key).split(";") if p.strip()]
        if len(parts) > 1:
            primary = parts[0]
            ph = tax.get(_norm(primary)) or tax.get(_norm(primary.split("->")[-1]))
            if ph is not None:
                kept = []
                for g in groups:
                    if g.get("източник") == "shopify_taxonomy" and g.get("shopify_attr") not in ph:
                        leak_removals.setdefault(key, []).append(g.get("група"))
                    else:
                        kept.append(g)
                groups = kept
        # --- B: duplicate merge (shopify group -> existing group), SAME-OBJECT only.
        # 'Материал на декорацията' == the item's own material -> merges into 'Материал'.
        # 'Материал на дръжката' (handle) / 'Тип монтаж' (mount) describe a DIFFERENT
        # aspect and stay separate — a knife has a steel blade and a wooden handle.
        SAME_OBJECT = {"", "надекорацията", "напредмета", "напродукта", "наизделието",
                       "наартикула", "наматериала", "наосновата"}
        ours = [g for g in groups if g.get("източник") != "shopify_taxonomy"]
        shop = [g for g in groups if g.get("източник") == "shopify_taxonomy"]
        drop = set()
        for sg in shop:
            sn = _norm(sg.get("група"))
            for og in ours:
                on = _norm(og.get("група"))
                if not on or not sn or on not in sn:
                    continue
                remainder = sn.replace(on, "", 1)
                if remainder not in SAME_OBJECT:
                    continue                             # qualifier names a sub-part/aspect
                ov = [x.strip() for x in str(og.get("стойности") or "").split(",") if x.strip()]
                sv = [x.strip() for x in str(sg.get("стойности") or "").split(",") if x.strip()]
                og["стойности"] = ", ".join(dict.fromkeys(ov + sv))[:800]
                og["shopify_attr"] = sg.get("shopify_attr")
                merges.setdefault(key, []).append((sg.get("група"), og.get("група")))
                drop.add(id(sg))
                break
        groups = [g for g in groups if id(g) not in drop]
        new_schema[key] = groups
    return new_schema, leak_removals, merges


def apply_product_renames(merges):
    """Rename merged-away attribute keys on existing products (append-only + DB)."""
    import db
    rename_by_cat = {}                                   # norm(cat key) -> {old: new}
    for key, pairs in merges.items():
        rename_by_cat[key] = {o: n for o, n in pairs}
    canon = db.canonical_records()
    buf = []
    changed = 0
    for code, rec in canon.items():
        f = rec.get("fields") or {}
        cat = str(f.get("Категории") or "").strip()
        rmap = rename_by_cat.get(cat)
        if not rmap:
            continue
        attrs = str(f.get("Атрибути") or "")
        if not attrs:
            continue
        parts = [p.strip() for p in attrs.split(";") if p.strip()]
        have = {p.split(":")[0].strip() for p in parts if ":" in p}
        newparts, ch = [], False
        for p in parts:
            if ":" not in p:
                newparts.append(p); continue
            k, v = p.split(":", 1)
            nk = rmap.get(k.strip())
            if nk and nk not in have:                    # rename only if target key absent
                newparts.append(f"{nk}:{v}"); ch = True
            elif nk:
                ch = True                                # duplicate semantics -> drop old
            else:
                newparts.append(p)
        if not ch:
            continue
        nf = dict(f); nf["Атрибути"] = "; ".join(newparts)
        nd = dict(rec); nd["fields"] = nf
        try:
            nd["ts"] = (datetime.fromisoformat(rec.get("ts") or "")
                        + timedelta(seconds=8)).isoformat(timespec="seconds")
        except Exception:
            nd["ts"] = datetime.now().isoformat(timespec="seconds")
        meta = dict(nd.get("meta") or {})
        meta["notes"] = list(meta.get("notes") or []) + ["schema_curator:attr_rename"]
        nd["meta"] = meta
        buf.append((json.dumps(nd, ensure_ascii=False), nd))
        changed += 1
    # JSONL first, DB second (a crash must never leave DB-only versions that a JSONL
    # replay would silently revert).
    with open(OUT, "a", encoding="utf-8") as fh:
        for line, nd in buf:
            fh.write(line + "\n")
            fh.flush()
            try:
                db.record_version(nd)
            except Exception:
                pass
    return changed


def main(apply=False):
    import filter_schema_store as fss
    new_schema, leaks, merges = plan()
    n_leak = sum(len(v) for v in leaks.values())
    n_merge = sum(len(v) for v in merges.values())
    print(f"A) compound-key leak removals: {n_leak} groups across {len(leaks)} keys")
    for k, v in list(leaks.items())[:3]:
        print(f"   {k[:70]}: -{v}")
    print(f"B) duplicate merges: {n_merge} across {len(merges)} keys")
    shown = 0
    for k, pairs in merges.items():
        for o, n in pairs[:2]:
            print(f"   {k[:56]}: '{o}' -> '{n}'")
        shown += 1
        if shown >= 5:
            break
    if not apply:
        print("\n(dry-run; --apply to write)")
        return
    # DELTA application under the store lock: only the leaked/merged groups are touched,
    # so a reviewer adjustment made while the plan was computing is never clobbered.
    changed = 0
    for key in set(list(leaks.keys()) + list(merges.keys())):
        remove = list(leaks.get(key, [])) + [o for o, _n in merges.get(key, [])]
        into_names = {n for _o, n in merges.get(key, [])}
        updates = [g for g in new_schema.get(key, [])
                   if isinstance(g, dict) and g.get("група") in into_names]
        if fss.adjust_delta(key, remove_names=remove, update_groups=updates,
                            reason="curator: leak-fix + duplicate merge", by="schema_curator"):
            changed += 1
    print(f"\nschema updated for {changed} categories (delta, lock-protected)")
    renamed = apply_product_renames(merges)
    print(f"C) product attribute keys renamed on {renamed} products -> {OUT.name}")
    print("REVERT schema: filter_schema_store revert_last per change | products: rm the lanez file + re-ingest")


if __name__ == "__main__":
    main(apply="--apply" in sys.argv)
