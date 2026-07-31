#!/usr/bin/env bash
# Mirror the FULL Barsy docs locally, no login/Chrome:
#   barsy.api  → public _sources/<doc>.rst.txt (reStructuredText: descriptions + param tables + shapes)
#   barsy.help → public rendered HTML (its _sources are disabled), stripped to plain text for grepping
# Enumerated from each section's searchindex.js `docnames` (the authoritative page list; the api
# sitemap.xml is misconfigured and lists only help). Re-runnable.
set -uo pipefail
BASE="https://docs.lukanet.com"
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$HERE/site"; TMP="$HERE/_tmp"
UA="Mozilla/5.0 (docs-mirror; darling admin panel)"
rm -rf "$ROOT"; mkdir -p "$ROOT/barsy.api" "$ROOT/barsy.help" "$TMP"
fetch() { curl -sSL --compressed --retry 3 --retry-delay 1 --max-time 40 -A "$UA" "$@"; }

# 1) docname lists + a tab-separated (url<TAB>dest) job file
for sec in barsy.api barsy.help; do fetch "$BASE/$sec/searchindex.js" -o "$TMP/$sec.js"; done
JOBS="$TMP/jobs.tsv"
python - "$TMP" "$BASE" "$ROOT" > "$JOBS" <<'PY'
import re, json, sys
tmp, base, root = sys.argv[1], sys.argv[2], sys.argv[3]
def docs(sec):
    t=open(f"{tmp}/{sec}.js",encoding="utf-8",errors="replace").read()
    m=re.search(r'"docnames"\s*:\s*(\[[^\]]*\])', t) or re.search(r'docnames\s*:\s*(\[[^\]]*\])', t)
    return json.loads(m.group(1)) if m else []
for d in docs("barsy.api"):
    print(f"{base}/barsy.api/_sources/{d}.rst.txt\t{root}/barsy.api/{d}.rst")
for d in docs("barsy.help"):
    print(f"{base}/barsy.help/{d}.html\t{root}/barsy.help/{d}.html")
PY
sed -i 's/\r$//' "$JOBS"        # Windows python emits \r\n — strip CR or dest paths get mangled
echo "[mirror] $(wc -l < "$JOBS") files to fetch"

# 2) download in parallel (8-way), creating parent dirs
export UA
dl() {
  IFS=$'\t' read -r url dest <<< "$1"
  mkdir -p "$(dirname "$dest")"
  code=$(curl -sSL --compressed --retry 3 --retry-delay 1 --max-time 40 -A "$UA" -o "$dest" -w "%{http_code}" "$url")
  { [ "$code" = "200" ] && [ -s "$dest" ]; } || { rm -f "$dest"; echo "MISS $code $url"; }
}
export -f dl
# feed each job line to dl; xargs -P8 for concurrency
mapfile -t LINES < "$JOBS"
printf '%s\n' "${LINES[@]}" | xargs -d '\n' -P 8 -I{} bash -c 'dl "$@"' _ {} > "$TMP/misses.txt" 2>&1

# 3) strip barsy.help HTML → .txt (grep-friendly), drop the raw .html
python - "$ROOT/barsy.help" <<'PY'
import re, html, pathlib, sys
base=pathlib.Path(sys.argv[1])
def strip(h):
    h=re.sub(r'(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>', ' ', h)
    h=re.sub(r'(?is)<br\s*/?>', '\n', h); h=re.sub(r'(?is)</(p|div|li|tr|h\d|section)>', '\n', h)
    h=re.sub(r'(?s)<[^>]+>', ' ', h); h=html.unescape(h)
    h=re.sub(r'[ \t]+', ' ', h); h=re.sub(r'\n\s*\n\s*\n+', '\n\n', h)
    return "\n".join(l.rstrip() for l in h.splitlines()).strip()
n=0
for f in base.rglob("*.html"):
    try:
        f.with_suffix(".txt").write_text(strip(f.read_text(encoding="utf-8",errors="replace")), encoding="utf-8")
        f.unlink(); n+=1
    except Exception as e: print("conv-err", f, e)
print(f"[mirror] converted {n} help pages to .txt")
PY

api=$(find "$ROOT/barsy.api" -name '*.rst' | wc -l)
help=$(find "$ROOT/barsy.help" -name '*.txt' | wc -l)
miss=$(grep -c "^MISS" "$TMP/misses.txt" 2>/dev/null || echo 0)
echo "[mirror] DONE — barsy.api: $api .rst | barsy.help: $help .txt | misses: $miss (see _tmp/misses.txt)"
echo "[mirror] tree at: $ROOT"
