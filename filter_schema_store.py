# -*- coding: utf-8 -*-
"""Living per-category filter schema — the attribute vocabulary that makes products
findable by filters on the site. Seeded from the 'Филтри по категории' Excel sheet
(embedded in tasks.jsonl) but MUTABLE: the reviewer agent adjusts it over time when
the hard rules don't fit a category (add a group like 'Лумени' for lamps, drop
'Форма' where shape is irrelevant, extend allowed values). Every change is logged
(old + new + reason) so it is auditable and revertible.

Read by BOTH the enrichment agent (to populate the right attributes) and the reviewer
(to check filterability). Concurrency-safe: atomic write, tolerant reload.
"""
import json, os, re, time, hashlib
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
STORE = HERE / "category_filters.json"          # {category_path: [ {група, стойности, ...} ]}
LOG = HERE / "category_filters_log.jsonl"        # append-only change history
LOCKFILE = HERE / ".category_filters.lock"


@contextmanager
def _locked(timeout_s=10):
    """Cross-process mutex for the store's read-modify-write. Without it, two concurrent
    adjust() calls (reviewer fleet + curator) could each rewrite the whole file from
    their own snapshot and silently drop the other's change."""
    fd = None
    deadline = time.time() + timeout_s
    while True:
        try:
            fd = os.open(str(LOCKFILE), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError:
            # steal a stale lock (crashed holder)
            try:
                if time.time() - LOCKFILE.stat().st_mtime > 60:
                    LOCKFILE.unlink(missing_ok=True)
                    continue
            except OSError:
                pass
            if time.time() > deadline:
                raise TimeoutError("category_filters lock busy")
            time.sleep(0.15)
    try:
        yield
    finally:
        try:
            os.close(fd)
            LOCKFILE.unlink(missing_ok=True)
        except OSError:
            pass


def _norm_name(s):
    return re.sub(r"[^0-9a-zа-я]", "", str(s or "").lower())


def _seed_from_tasks():
    cats = {}
    tp = HERE / "tasks.jsonl"
    if tp.exists():
        for line in tp.open(encoding="utf-8", errors="replace"):
            if not line.strip():
                continue
            try:
                t = json.loads(line)
            except Exception:
                continue
            cat = str((t.get("product") or {}).get("Категории") or "").strip()
            fs = t.get("filter_schema")
            if cat and fs and cat not in cats:
                cats[cat] = fs
    return cats


def load():
    if STORE.exists():
        # NEVER fall through to reseed when the store exists — a transient read failure
        # (Windows sharing violation during a concurrent _write) previously reseeded from
        # the Excel base, silently DESTROYING every taxonomy/curator/reviewer adjustment.
        last = None
        for _ in range(6):
            try:
                return json.loads(STORE.read_text(encoding="utf-8"))
            except Exception as e:
                last = e
                time.sleep(0.25)
        raise RuntimeError(f"category_filters.json unreadable after retries: {last}")
    cats = _seed_from_tasks()
    _write(cats)
    return cats


def _write(cats):
    tmp = str(STORE) + ".tmp"
    Path(tmp).write_text(json.dumps(cats, ensure_ascii=False, indent=1), encoding="utf-8")
    for _ in range(6):
        try:
            os.replace(tmp, STORE)
            return True
        except PermissionError:
            time.sleep(0.3)
    try:
        os.remove(tmp)
    except OSError:
        pass
    return False


def get_filters(category):
    """Effective filter groups for a category path (live)."""
    return load().get(str(category or "").strip(), [])


def category_fingerprint(category, cats=None):
    """A short, stable hash of a category's CURRENT filter-group NAMES. Stamped onto a
    product at enrichment time; when the category schema later grows/shrinks, the stored
    fingerprint no longer matches -> that product is 'stale' and the reconciliation pass
    knows to re-check its attributes. Cheap and deterministic (no quota)."""
    groups = (cats or load()).get(str(category or "").strip(), [])
    names = sorted(str((g or {}).get("група") or g).strip().lower() for g in groups)
    h = hashlib.md5("|".join(names).encode("utf-8")).hexdigest()[:8]
    return h


def stale_categories(stamps):
    """Given {category: fingerprint_seen}, return the set of categories whose live
    fingerprint differs — i.e. whose filter schema changed since products were stamped."""
    cats = load()
    return {c for c, fp in stamps.items() if category_fingerprint(c, cats) != fp}


def adjust(category, groups, reason, by="reviewer"):
    """Set the filter groups for a category. `groups` is the full new list of
    {"група","стойности",...}. Logged with the previous value for revert. Runs under the
    store lock so a concurrent adjust can't be clobbered — but NOTE: a full-list adjust
    still overwrites the key with the CALLER's snapshot; prefer adjust_delta for
    programmatic edits."""
    category = str(category or "").strip()
    if not category or not isinstance(groups, list):
        return False
    with _locked():
        cats = load()
        old = cats.get(category)
        cats[category] = groups
        if not _write(cats):
            return False
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": datetime.now().isoformat(timespec="seconds"),
                            "category": category, "by": by, "reason": reason,
                            "old": old, "new": groups}, ensure_ascii=False) + "\n")
    return True


def adjust_delta(category, add=None, remove_names=None, update_groups=None,
                 reason="", by="curator"):
    """Compare-and-swap style edit: reloads the CURRENT store under the lock and applies
    a DELTA to one key — so concurrent edits to other groups of the same key (or other
    keys) are never lost to a stale snapshot.
      add           — groups appended only if no group with the same normalized name exists
      remove_names  — group names removed (normalized match)
      update_groups — groups replacing the same-named existing group
    Returns the number of effective changes."""
    category = str(category or "").strip()
    if not category:
        return 0
    changed = 0
    with _locked():
        cats = load()
        groups = [g for g in cats.get(category, []) if isinstance(g, dict)]
        have = {_norm_name(g.get("група")): i for i, g in enumerate(groups)}
        rm = {_norm_name(n) for n in (remove_names or [])}
        if rm:
            kept = [g for g in groups if _norm_name(g.get("група")) not in rm]
            changed += len(groups) - len(kept)
            groups = kept
            have = {_norm_name(g.get("група")): i for i, g in enumerate(groups)}
        for ug in (update_groups or []):
            i = have.get(_norm_name(ug.get("група")))
            if i is not None and groups[i] != ug:
                groups[i] = ug
                changed += 1
        for ag in (add or []):
            if _norm_name(ag.get("група")) not in have:
                groups.append(ag)
                have[_norm_name(ag.get("група"))] = len(groups) - 1
                changed += 1
        if changed:
            cats[category] = groups
            if not _write(cats):
                return 0
    if changed:
        with LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": datetime.now().isoformat(timespec="seconds"),
                                "category": category, "by": by, "reason": reason,
                                "delta": {"add": [g.get("група") for g in (add or [])],
                                          "remove": list(remove_names or []),
                                          "update": [g.get("група") for g in (update_groups or [])]}},
                               ensure_ascii=False) + "\n")
    return changed


def revert_last():
    """Undo the most recent FULL-LIST adjust (for oversight). Delta entries carry no
    'old' snapshot and are skipped."""
    if not LOG.exists():
        return None
    lines = [l for l in LOG.read_text(encoding="utf-8").splitlines() if l.strip()]
    for raw in reversed(lines):
        last = json.loads(raw)
        if "delta" in last:
            continue                                    # delta entries aren't snapshot-revertible
        with _locked():
            cats = load()
            if last.get("old") is None:
                cats.pop(last["category"], None)
            else:
                cats[last["category"]] = last["old"]
            _write(cats)
        return last["category"]
    return None


if __name__ == "__main__":
    import sys
    if "--seed" in sys.argv:
        c = _seed_from_tasks(); _write(c); print(f"seeded {len(c)} categories")
    elif "--revert" in sys.argv:
        print("reverted:", revert_last())
    else:
        c = load(); print(f"{len(c)} categories; e.g. {list(c)[:3]}")
