# -*- coding: utf-8 -*-
"""Nightly backup of everything the pipeline can't regenerate.

Backs up the source Excel, all enrichment result/version files, human decisions, the
reviewer-adjusted filter schema, the brand gazetteer, and the SQLite mirror. Keeps the
last 7 dated snapshots under ../backups/.

HARDENED (2026-07-16):
  * ALERTS LOUDLY when a CRITICAL file is missing (was: silent skip → you'd notice a lost
    source only days later).
  * Source Excel: prefers a STABLE filename; the AutoRecovered temp file is a fallback and
    triggers a warning to save-as a stable copy.
  * Includes pipeline.db, approvals, review_fixes, category_filters, brand_gazetteer.
  * Optional OFF-MACHINE copy: set env BACKUP_MIRROR to a second dir (e.g. a synced/cloud
    folder) and each snapshot is copied there too — 7 local snapshots are not disaster-proof.
"""
import os
import shutil
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
BACKUPS = HERE.parent / "backups"
DESKTOP = Path(r"C:\Users\lora_\Desktop")

# Source Excel: prefer a stable name; fall back to the AutoRecovered temp (with a warning).
_STABLE_XLSX = DESKTOP / "Local Database - enriched.xlsx"
_AUTORECOVER_XLSX = DESKTOP / "Local Database - enriched(AutoRecovered).xlsx"


def _source_xlsx():
    if _STABLE_XLSX.exists():
        return _STABLE_XLSX, False
    return _AUTORECOVER_XLSX, True                      # (path, is_fragile_fallback)


# Files whose loss would be UNRECOVERABLE — a missing one is an ALERT, not a silent skip.
def _critical():
    src, _ = _source_xlsx()
    return [src] + list(HERE.glob("results.lane*.jsonl"))    # incl. all lanez_* version files


# Additional irreplaceable state (human decisions, reviewer schema, learned data, mirror).
def _extra():
    return [HERE / "approvals.jsonl", HERE / "review_fixes.jsonl",
            HERE / "category_filters.json", HERE / "category_filters_log.jsonl",
            HERE / "brand_gazetteer.jsonl", HERE / "catnum_index.jsonl",
            HERE / "failures.jsonl", HERE / "categories.json",
            HERE / "pipeline.db", HERE / "lookup_cache.jsonl"]


def main():
    stamp = date.today().isoformat()
    target = BACKUPS / stamp
    target.mkdir(parents=True, exist_ok=True)
    warnings = []

    src, fragile = _source_xlsx()
    if fragile and src.exists():
        warnings.append(f"source Excel is the FRAGILE AutoRecovered temp ({src.name}) — "
                        f"do a Save-As to '{_STABLE_XLSX.name}' so a crash can't lose it")

    copied = 0
    for f in _critical():
        if f.exists():
            shutil.copy2(f, target / f.name)
            copied += 1
        else:
            warnings.append(f"⚠️ MISSING CRITICAL FILE (not backed up): {f}")
    for f in _extra():
        if not f.exists():
            continue
        if f.name == "pipeline.db":
            # WAL-mode DB written by 12 live lanes: a raw file copy misses the WAL tail
            # and can be internally inconsistent. Use SQLite's online backup API.
            try:
                import sqlite3
                src = sqlite3.connect(str(f)); dst = sqlite3.connect(str(target / f.name))
                with dst:
                    src.backup(dst)
                src.close(); dst.close()
                copied += 1
            except Exception as e:
                warnings.append(f"pipeline.db online backup FAILED: {str(e)[:80]}")
            continue
        shutil.copy2(f, target / f.name)
        copied += 1

    # optional off-machine mirror
    mirror = os.environ.get("BACKUP_MIRROR")
    if mirror:
        try:
            mtarget = Path(mirror) / stamp
            if mtarget.exists():
                shutil.rmtree(mtarget, ignore_errors=True)
            shutil.copytree(target, mtarget)
            print(f"Mirrored snapshot to {mtarget}")
        except Exception as e:
            warnings.append(f"off-machine mirror FAILED: {str(e)[:80]}")
    else:
        warnings.append("no off-machine backup (set env BACKUP_MIRROR to a synced/cloud dir)")

    snaps = sorted(d for d in BACKUPS.iterdir() if d.is_dir())
    for old in snaps[:-7]:
        shutil.rmtree(old, ignore_errors=True)

    print(f"Backed up {copied} files to {target} ({len(snaps[-7:])} snapshots kept)")
    if warnings:
        print("\n".join("‼️  " + w for w in warnings))


if __name__ == "__main__":
    main()
