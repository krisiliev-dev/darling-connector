# -*- coding: utf-8 -*-
"""Align our filter schema with Shopify's Standard Product Taxonomy attributes.

For every BG category we've mapped to a Shopify taxonomy category
(category_shopify_map.json), pull the taxonomy's standard attributes for that category
and MERGE them into our living filter schema (category_filters.json) — with OFFICIAL
Bulgarian names and value vocabularies from Shopify's own bg-BG localization.

Merge policy (additive, auditable, reviewer-refinable):
  * existing groups are NEVER touched (owner Excel + reviewer refinements stay),
  * a Shopify attribute is added only if no existing group has the same normalized name,
  * every change goes through filter_schema_store.adjust() -> logged + revertible,
  * per-group provenance is kept ("източник": "shopify_taxonomy", "shopify_attr": handle)
    so the future Shopify import can map our attributes straight to taxonomy metafields.

  python shopify_schema_align.py            # dry-run report
  python shopify_schema_align.py --apply    # merge into the schema
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
TAXO = HERE / "shopify_taxonomy"
MAX_VALUES = 25                                          # vocab cap per group (prompt size)


def _norm(s):
    return re.sub(r"[^0-9a-zа-я]", "", str(s or "").lower())


def load_taxonomy():
    cats = json.load(open(TAXO / "categories.json", encoding="utf-8"))
    attrs = json.load(open(TAXO / "attributes.json", encoding="utf-8"))
    import yaml
    bg_attr = yaml.safe_load(open(TAXO / "attributes_bg.yml", encoding="utf-8"))["bg-BG"]["attributes"]
    bg_val = yaml.safe_load(open(TAXO / "values_bg.yml", encoding="utf-8"))["bg-BG"]["values"]

    # gid -> [attribute dicts] walking every vertical/category
    by_gid = {}
    def _walk(c):
        by_gid[c["id"]] = c.get("attributes") or []
        for ch in c.get("children") or []:
            if isinstance(ch, dict) and ch.get("id"):
                pass                                     # children are refs in dist; categories list is flat
    for v in cats["verticals"]:
        for c in v["categories"]:
            by_gid[c["id"]] = c.get("attributes") or []

    # attribute handle -> {en, values:[(en_handle, en_name)]}
    attr_def = {}
    for a in attrs["attributes"]:
        attr_def[a["handle"]] = a
    # bg-BG localization keys use snake_case handles; dist handles use kebab-case
    def bg_name_for(handle, en_name):
        k = handle.replace("-", "_")
        d = bg_attr.get(k) or bg_attr.get(handle)
        return (d or {}).get("name") or en_name

    def bg_value_for(vhandle, en_name):
        k = str(vhandle).replace("-", "_")
        d = bg_val.get(k) or bg_val.get(vhandle)
        return (d or {}).get("name") or en_name

    return by_gid, attr_def, bg_name_for, bg_value_for


def build_plan():
    import filter_schema_store as fss
    by_gid, attr_def, bg_name_for, bg_value_for = load_taxonomy()
    catmap = json.loads((HERE / "category_shopify_map.json").read_text(encoding="utf-8"))
    schema = fss.load()
    # index our schema keys by normalized full key and leaf
    key_ix = {}
    for k in schema:
        key_ix.setdefault(_norm(k), []).append(k)
        key_ix.setdefault(_norm(str(k).split("->")[-1]), []).append(k)

    plan = {}                                            # schema_key -> [new group dicts]
    unmatched, no_attrs = [], []
    for m in catmap:
        bg, gid = m.get("bg"), m.get("shopify_id")
        if not bg or not gid:
            continue
        skeys = key_ix.get(_norm(bg)) or []
        if not skeys:
            unmatched.append(bg)
            continue
        tax_attrs = by_gid.get(gid) or []
        if not tax_attrs:
            no_attrs.append(bg)
            continue
        for skey in set(skeys):
            existing = {_norm(g.get("група")) for g in schema.get(skey, []) if isinstance(g, dict)}
            for ta in tax_attrs:
                handle = ta.get("handle") or ""
                en = ta.get("name") or handle
                bgname = bg_name_for(handle, en)
                if _norm(bgname) in existing or not bgname:
                    continue
                adef = attr_def.get(handle) or {}
                vals = [bg_value_for(v.get("handle"), v.get("name"))
                        for v in (adef.get("values") or [])[:MAX_VALUES]]
                plan.setdefault(skey, []).append({
                    "група": bgname,
                    "стойности": ", ".join(dict.fromkeys(x for x in vals if x)),
                    "източник": "shopify_taxonomy",
                    "shopify_attr": handle,
                })
                existing.add(_norm(bgname))
    return plan, unmatched, no_attrs


def main(apply=False):
    import filter_schema_store as fss
    plan, unmatched, no_attrs = build_plan()
    total_groups = sum(len(v) for v in plan.values())
    print(f"categories to extend: {len(plan)} | new groups to add: {total_groups}")
    print(f"map entries with no matching schema key: {len(unmatched)} {unmatched[:6]}")
    print(f"mapped taxonomy categories carrying no attributes: {len(no_attrs)}")
    shown = 0
    for k, groups in plan.items():
        print(f"\n  {k}:")
        for g in groups[:6]:
            print(f"    + {g['група']}  [{g['shopify_attr']}]  values: {g['стойности'][:70]}")
        shown += 1
        if shown >= 4:
            break
    if not apply:
        print("\n(dry-run; --apply to merge — every change logged & revertible)")
        return
    changed = 0
    for k, groups in plan.items():
        # delta add-if-missing under the store lock — never clobbers concurrent edits
        if fss.adjust_delta(k, add=groups,
                            reason="Shopify taxonomy baseline (official bg-BG names/values)",
                            by="shopify_taxonomy"):
            changed += 1
    print(f"\nAPPLIED: extended {changed} categories with {total_groups} standard groups")
    print("revert per-category with: python filter_schema_store.py --revert (last change first)")


if __name__ == "__main__":
    main(apply="--apply" in sys.argv)
