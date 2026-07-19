# -*- coding: utf-8 -*-
"""Build the full Shopify product taxonomy as Barsy categories (owner 2026-07-19).

Source: taxonomy_slim.json (9,795 Shopify categories, each {gid, full, bg, leaf}). Each
Barsy category is created with:
  - cat_name        = Bulgarian leaf name (English leaf as fallback)   [staff-facing]
  - cat_name_ml     = {bg_BG: bg, en_US: english_leaf}
  - cat_name_public = {bg_BG: bg}                                      [e-shop]
  - slug            = gid suffix (e.g. "hg-1-2") — unique, stable, Shopify-aligned
  - remote_ref_id / remote_parent_ref_id = the Shopify gid(s) — the durable link that lets
    us map Barsy cat_id <-> Shopify taxonomy id later (for cat_id assignment + Shopify sync)
  - parent_id       = the Barsy cat_id of the parent (resolved from the checkpoint)

Categories are created parents-first (sorted by gid depth). A gid->cat_id checkpoint
(barsy_cat_map.json) makes the run idempotent + resumable: rerun to continue after an
interruption; already-created gids are skipped.

  python barsy_taxonomy.py --plan     # counts + a few sample payloads, no writes
  python barsy_taxonomy.py --build     # create everything (resumable)
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

import barsy_api as b

HERE = Path(__file__).parent
TAX = HERE / "taxonomy_full.json"          # full 26-vertical taxonomy (was taxonomy_slim)
MAP = HERE / "barsy_cat_map.json"          # {gid: cat_id} checkpoint


def _suffix(gid):
    return gid.split("/")[-1]               # gid://shopify/TaxonomyCategory/hg-1-2 -> hg-1-2


def _parent_gid(gid):
    s = _suffix(gid)
    if "-" not in s:
        return None                         # root
    parent_suffix = s.rsplit("-", 1)[0]
    return gid.rsplit("-", 1)[0] if _suffix(gid) != parent_suffix else None


def _load_map():
    if MAP.exists():
        return json.loads(MAP.read_text(encoding="utf-8"))
    return {}


def _save_map(m):
    MAP.write_text(json.dumps(m, ensure_ascii=False), encoding="utf-8")


_NODE_IDX = None


def _nodes_by_gid():
    global _NODE_IDX
    if _NODE_IDX is None:
        _NODE_IDX = {n["gid"]: n for n in json.loads(TAX.read_text(encoding="utf-8"))}
    return _NODE_IDX


def ensure_path(gid):
    """Just-in-time: ensure `gid` + all its ancestors exist as Barsy categories (create any
    missing, parents-first), return the leaf's cat_id. Lets a product push its category
    immediately without waiting for the full background build. Returns None on unknown gid."""
    if not gid:
        return None
    cmap = _load_map()
    if gid in cmap:
        return cmap[gid]
    idx = _nodes_by_gid()
    chain, g = [], gid                          # root -> leaf ancestor chain
    while g is not None:
        chain.append(g)
        g = _parent_gid(g)
    chain.reverse()
    parent_id = None
    created = False
    for cg in chain:
        if cg in cmap:
            parent_id = cmap[cg]
            continue
        node = idx.get(cg)
        if not node:
            return None
        out = b.call("Categories_create", _payload(node, parent_id))
        cid = out if isinstance(out, int) else (out.get("cat_id") if isinstance(out, dict) else None)
        if not cid:
            return None
        cmap[cg] = cid
        parent_id = cid
        created = True
    if created:
        _save_map(cmap)
    return cmap.get(gid)


def _payload(cat, parent_id):
    gid = cat["gid"]
    eng_leaf = cat["full"].split(" > ")[-1].strip()
    bg = (cat.get("bg") or "").strip() or eng_leaf
    ml = {"bg_BG": bg}
    if eng_leaf and eng_leaf != bg:
        ml["en_US"] = eng_leaf
    body = {"cat": {
        "cat_name": bg,
        "cat_name_ml": ml,
        "cat_name_public": {"bg_BG": bg},
        "slug": _suffix(gid),
        "remote_ref_id": gid,
    }}
    pg = _parent_gid(gid)
    if pg:
        body["cat"]["remote_parent_ref_id"] = pg
    if parent_id is not None:
        body["cat"]["parent_id"] = parent_id
    return body


def _reconcile(cmap):
    """Self-heal: pull any Barsy category NOT in the checkpoint back into it via its `slug`
    (=gid suffix). Guards against re-creating orphans left by an interrupted/raced build."""
    GID = "gid://shopify/TaxonomyCategory/"
    have = set(cmap.values())
    orphans = [c for c in b.call("Categories_getlist")
               if isinstance(c.get("cat_id"), int) and c["cat_id"] >= 76
               and c["cat_id"] not in have]
    added = 0
    for c in orphans:
        try:
            slug = b.call("Categories_get", {"cat_id": c["cat_id"]}).get("slug")
            if slug:
                cmap[GID + slug] = c["cat_id"]
                added += 1
        except b.BarsyError:
            pass
    if added:
        _save_map(cmap)
        print(f"reconciled {added} orphan categories into the checkpoint", flush=True)
    return cmap


def build(plan_only=False):
    tax = json.loads(TAX.read_text(encoding="utf-8"))
    # parents before children: sort by number of gid segments
    tax.sort(key=lambda c: len(_suffix(c["gid"]).split("-")))
    cmap = _load_map()
    if not plan_only:
        cmap = _reconcile(cmap)
    total = len(tax)
    todo = [c for c in tax if c["gid"] not in cmap]
    print(f"taxonomy: {total} categories | already created: {len(cmap)} | todo: {len(todo)}",
          flush=True)

    if plan_only:
        for c in tax[:3] + [c for c in tax if len(_suffix(c['gid']).split('-')) == 4][:2]:
            pg = _parent_gid(c["gid"])
            print(json.dumps(_payload(c, cmap.get(pg, 0) if pg else None),
                             ensure_ascii=False)[:260])
        return

    ok = fail = 0
    for i, c in enumerate(todo):
        gid = c["gid"]
        pg = _parent_gid(gid)
        parent_id = cmap.get(pg) if pg else None
        if pg and parent_id is None:
            print(f"  SKIP {gid}: parent {pg} not created yet", flush=True)
            fail += 1
            continue
        try:
            out = b.call("Categories_create", _payload(c, parent_id))
            cid = out if isinstance(out, int) else (out.get("cat_id") if isinstance(out, dict) else None)
            if not cid:
                raise b.BarsyError(f"no cat_id in response: {out}")
            cmap[gid] = cid
            ok += 1
        except b.BarsyError as e:
            fail += 1
            print(f"  FAIL {gid}: {str(e)[:110]}", flush=True)
        if (ok + fail) % 200 == 0:
            _save_map(cmap)
            print(f"  ... {len(cmap)}/{total} created ({fail} fails this run)", flush=True)
    _save_map(cmap)
    print(f"DONE: created {ok}, failed {fail}. total mapped: {len(cmap)}/{total}", flush=True)


def _acquire_lock():
    """Single-instance guard (the shared-hermes gateway can double-launch a command; two
    concurrent builds race the checkpoint and create orphan categories). Atomic O_EXCL
    create handles the near-simultaneous double-launch; a lock older than STALE_H hours is
    treated as a crashed build and stolen (avoids Windows-unsafe os.kill liveness checks)."""
    import os
    import time
    lock = HERE / ".taxonomy_build.lock"
    STALE_H = 6
    for _ in range(2):
        try:
            fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
            return lock
        except FileExistsError:
            try:
                age_h = (time.time() - lock.stat().st_mtime) / 3600.0
            except OSError:
                age_h = 0
            if age_h < STALE_H:
                return None                           # fresh lock -> another live instance
            try:
                lock.unlink()                         # stale -> steal and retry
            except OSError:
                return None
    return None


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--build", action="store_true")
    a = ap.parse_args()
    if a.plan:
        build(plan_only=True)
    else:
        lock = _acquire_lock()
        if lock is None:
            print("another taxonomy build is already running — exiting.")
            raise SystemExit(0)
        try:
            build(plan_only=not a.build)
        finally:
            try:
                lock.unlink()
            except OSError:
                pass
