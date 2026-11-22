#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
status=0
python3 scripts/check_card.py skill/examples/*.md || status=1
python3 scripts/check_card.py --headers-only skill/talk-card.template.md || status=1
exit $status
