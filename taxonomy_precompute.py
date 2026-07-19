# -*- coding: utf-8 -*-
"""One-time precompute so lanes never parse the 80MB taxonomy per batch:
  * taxonomy_slim.json — [{gid, full, bg, leaf}] (~2MB, loads in <100ms)
  * DB table leaf_schemas(gid, schema_json) — the compiled per-leaf attribute schema
Re-run only after a taxonomy version bump."""
import json

import db
import leaf_schema as ls
import taxonomy_leaf as tl

nodes = tl.load_nodes()
slim = [{"gid": n["gid"], "full": n["full"], "bg": n["bg"], "leaf": n["leaf"]}
        for n in nodes]
(tl.HERE / "taxonomy_slim.json").write_text(json.dumps(slim, ensure_ascii=False),
                                            encoding="utf-8")
print(f"taxonomy_slim.json: {len(slim)} nodes")

con = db.connect()
con.execute("CREATE TABLE IF NOT EXISTS leaf_schemas(gid TEXT PRIMARY KEY, schema_json TEXT)")
n = 0
for nd in slim:
    if not nd["leaf"]:
        continue
    sc = ls.schema_for(nd["gid"])
    con.execute("INSERT OR REPLACE INTO leaf_schemas VALUES (?,?)",
                (nd["gid"], json.dumps(sc, ensure_ascii=False)))
    n += 1
    if n % 2000 == 0:
        con.commit()
        print(f"  {n} leaf schemas...")
con.commit()
con.close()
print(f"DONE: {n} leaf schemas cached in DB")
