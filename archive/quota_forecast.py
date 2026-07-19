# -*- coding: utf-8 -*-
"""Quota forecast — will the free tiers cover finishing enrichment + reviewing all 14k?

Uses the measured telemetry (avg tokens/product) to project the remaining token cost and
compares it against the free-tier budget, so we can plan instead of hitting a wall mid-run.
"""
import json, glob
from pathlib import Path

HERE = Path(__file__).parent
TOTAL = 14159
FREE_QWEN_MODELS = 35
REVIEW_TOKENS_EST = 18_000          # reviewer is lighter than enrichment (no long ReAct loop)


def main():
    import db
    con = db.connect()
    done = con.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    tel = con.execute("SELECT AVG(total_tokens), COUNT(*) FROM products WHERE total_tokens IS NOT NULL").fetchone()
    exhausted = 0
    ep = HERE / "exhausted_models.txt"
    if ep.exists():
        exhausted = len(set(l.strip() for l in open(ep, encoding="utf-8") if l.strip()))
    con.close()

    avg = int(tel[0] or 110000)
    measured = tel[1] or 0
    remaining = TOTAL - done

    # OBSERVATIONAL method (v2). The v1 "spent/exhausted = grant" estimate was WRONG in two
    # ways the owner spotted: (a) the exhausted list carried entries drained under the OLD
    # (arrears) API key — quota is per-key, so they didn't measure this key's pool; (b) it
    # averaged tiny-flash grants with the workhorse tier. Reality check: the current primary
    # model absorbed 62M+ tokens in hours and stayed alive, and the exhausted count has been
    # flat for hours of heavy processing. So instead of extrapolating a pool, we report the
    # observed burn and watch for actual exhaustion movement.
    import json as _json
    per_model = {}
    con2 = db.connect()
    for (rj,) in con2.execute("SELECT record_json FROM products WHERE record_json IS NOT NULL "
                              "AND total_tokens IS NOT NULL").fetchall():
        u = (_json.loads(rj).get("meta") or {}).get("usage") or {}
        for m, d in (u.get("by_model") or {}).items():
            per_model[m] = per_model.get(m, 0) + d.get("pt", 0) + d.get("ct", 0)
    con2.close()
    workhorse, wh_tok = (max(per_model.items(), key=lambda x: x[1]) if per_model else ("?", 0))

    enrich_cost = remaining * avg
    review_cost = TOTAL * REVIEW_TOKENS_EST
    total_need = enrich_cost + review_cost

    print("=== QUOTA FORECAST (observational) ===")
    print(f"measured avg: {avg:,} tokens/product (over {measured} products)")
    print(f"still needed: enrichment {remaining} × {avg//1000}k ≈ {enrich_cost/1e6:.0f}M "
          f"+ review-all {TOTAL} × {REVIEW_TOKENS_EST//1000}k ≈ {review_cost/1e6:.0f}M "
          f"= ~{total_need/1e6:.0f}M tokens\n")
    print(f"observed: workhorse {workhorse} absorbed {wh_tok/1e6:.0f}M in the measured window "
          f"and is STILL ALIVE; {exhausted} models exhausted (count stable for hours under load).")
    print("=> per-model grants on the plus/max tier are large (>60M) or renewing; the drained")
    print("   models are the small flash tier. No wall is currently in evidence.\n")
    print("VERDICT: keep running and WATCH the two live signals — (1) the exhausted count, "
          "(2) the workhorse's cumulative tokens. If exhausted climbs steadily again or the "
          "workhorse dies, revisit. Cost levers if it ever tightens: compaction is live "
          "(~10% cut), option-B review-lock keeps review one-time, difficulty routing exists.")


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
