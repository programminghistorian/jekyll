#!/bin/bash

# Build site, and then run htmlproofer to check for broken internal and external links

bundle exec jekyll build && bundle exec htmlproofer ./_site \
  --assume-extension \
  --empty-alt-ignore \
  --alt-ignore '/.*/' \
  --file-ignore "/assets/,/retired/,/retirada/,/retrait/,/posts/"\
  --timeframe '30d' \
  --only-4xx \
  --http-status-ignore 429,403,400 \
  --url-ignore "/http://www.gutenberg.org/*/,/https://github.com/programminghistorian/jekyll/(commits|blob)/*/,/\#/,/espanol/,/deprecated/,/collection.britishmuseum.org/,/analytics.hathitrust.org/,/fr.wikipedia.org/wiki/,https://web.archive.org/web/20180831094856/http://www.dlsi.ua.es/~borja/riilua/6.TopicModeling_v02.pdf"

# The folllowing comments docuemnt what each line of that build script does.

# bundle exec jekyll build && bundle exec htmlproofer ./_site \
#   # Follow urls that don't have an explicit /index.html after them
#   --assume-extension \
#   # Don't throw a warning if images are missing an alt tag
#   --empty-alt-ignore \
#   --alt-ignore '/.*/' \
#   # Ignore any html files in the assets and the retired lessons folder
#   --file-ignore '/.+/assets/.*/','/.+/lessons/retired/.*/' \
#   # Only re-echeck external links that have not been verified within the last
#   30 # days. This makes reference to a cache directory that is saved when
#   Travis CI
#   # finishes a successful build
#   --timeframe '30d' \
#   # Only report 400-range errors, e.g. missing content. This will silence
#   errors
#   # in the case of e.g. request timeouts.
#   --only-4xx \
#   # Don't throw an error if the external site is protesting under too many
#   # requests, likely from Travis CI. This is usually just a passing error.
#   --http-status-ignore 429 \
#   # Ignore specific url. - Also ignores links to github version histories,
#   which
#   # will not exist for newly-proposed pages in pull requests.
#   --url-ignore http://www.gutenberg.org/ebooks/2600,/https://github.com/programminghistorian/jekyll/commits/*/
