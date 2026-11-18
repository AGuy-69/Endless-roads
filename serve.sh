#!/bin/sh
# Starts a local web server in this folder and opens Endless Road in your browser.
cd "$(dirname "$0")" || exit 1
PY=""
for c in python3 python; do command -v "$c" >/dev/null 2>&1 && { PY="$c"; break; }; done
if [ -z "$PY" ]; then echo "Python was not found. Install Python 3 from https://www.python.org/ and run this again."; exit 1; fi
exec "$PY" serve.py "$@"
