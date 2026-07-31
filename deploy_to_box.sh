#!/bin/bash
# Deploy agent-pipeline files to the Contabo box, ALWAYS as LF.
#
# Why this exists: this laptop writes CRLF, the box uses LF, so a plain `scp` produces a file whose
# CONTENT is identical but whose bytes (and therefore hash) are not. On 2026-07-31 that made the
# panel's brand-new drift detector report three shared money-path modules as stale — including the
# Barsy connector — and led to an unnecessary overwrite of production modules on a signal that meant
# nothing. `diff --strip-trailing-cr` showed zero changed lines in all three.
#
# Same root cause as the earlier `~/.hermes/.env` incident, where a trailing \r on a secret silently
# broke webhook HMAC with 401s. Normalising at the point of deploy removes the class, rather than
# teaching each consumer to tolerate it.
#
#   ./deploy_to_box.sh barsy_shopify_connector.py woo_orders.py
#   ./deploy_to_box.sh --all-py
set -euo pipefail

HOST="darling@169.58.69.210"
KEY="$HOME/.ssh/id_ed25519"
DEST="/home/darling/product-review/agent-pipeline"
HERE="$(cd "$(dirname "$0")" && pwd)"

files=()
if [ "${1:-}" = "--all-py" ]; then
    while IFS= read -r f; do files+=("$f"); done < <(cd "$HERE" && ls *.py)
else
    files=("$@")
fi
[ ${#files[@]} -eq 0 ] && { echo "usage: $0 <file.py> [...] | --all-py"; exit 1; }

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

for f in "${files[@]}"; do
    src="$HERE/$f"
    [ -f "$src" ] || { echo "  !! $f not found — aborting (a partial deploy is worse than none)"; exit 1; }
    # strip CR so the byte content matches what the box and the repo expect
    sed 's/\r$//' "$src" > "$tmp/$(basename "$f")"
done

scp -q -o StrictHostKeyChecking=no -i "$KEY" "$tmp"/* "$HOST:$DEST/"

# Verify by comparing the NORMALISED local bytes against the box — never assume the copy landed.
fail=0
for f in "${files[@]}"; do
    b="$(basename "$f")"
    want="$(sha256sum "$tmp/$b" | cut -d' ' -f1)"
    got="$(ssh -o StrictHostKeyChecking=no -i "$KEY" "$HOST" "sha256sum $DEST/$b 2>/dev/null | cut -d' ' -f1")"
    if [ "$want" = "$got" ]; then
        echo "  ok   $b"
    else
        echo "  FAIL $b  (local $want != box $got)"
        fail=1
    fi
done
exit $fail
