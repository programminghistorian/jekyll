#!/usr/bin/env bash

set -euo pipefail

# Keep the local and CI link checks identical. These options use the
# HTMLProofer 5 command-line names.
bundle exec htmlproofer _site \
  --assume-extension .html \
  --ignore-missing-alt \
  --ignore-empty-alt \
  --allow-missing-href \
  --no-check-internal-hash \
  --no-enforce-https \
  --only-4xx \
  --ignore-status-codes 429,403,400,415 \
  --ignore-files "/_site\/assets\//,/_site\/blog\//,/_site\/posts\//,/_site\/en\/lessons\/retired\//,/_site\/es\/lecciones\/retirada\//,/_site\/fr\/lecons\/retrait\//,/_site\/pt\/licoes\/retiradas\//" \
  --ignore-urls "/github\.com\/programminghistorian/,/gutenberg\.org/,/espanol/,/deprecated/,/collection\.britishmuseum\.org/,/analytics\.hathitrust\.org/,/docnow\.io/,/doxygen\.nl/,/doi\.org\/10\.34190\/JEL\.17\.3\.002/,/doi\.org\/10\.22134\/trace\.82\.2022\.819/,/rubenalcaraz\.es\/manual-omeka\/?/,/web\.archive\.org\/web\/20180831094856\/http:\/\/www\.dlsi\.ua\.es\/~borja\/riilua\/6\.TopicModeling_v02\.pdf/" \
  "$@"
