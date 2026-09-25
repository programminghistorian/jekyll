#!/usr/bin/env bash

set -euo pipefail

# Build the site, then run the same link checker used by GitHub Actions.
bundle exec jekyll build
"$(dirname "$0")/check-links.sh"
