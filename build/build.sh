#!/bin/bash

# Build site, and then run htmlproofer to check for broken internal and external links

bundle exec jekyll build && bundle exec htmlproofer ./_site \
  --assume-extension \
  --empty-alt-ignore \
  --alt-ignore '/.*/' \
  --file-ignore '/.+/assets/.*/','/.+/lessons/deprecated/.*/' \
  --timeframe '30d' \
  --only-4xx \
  --http-status-ignore 429 \
  --url-ignore http://www.gutenberg.org/ebooks/2600,/https://github.com/programminghistorian/jekyll/commits/*/
  