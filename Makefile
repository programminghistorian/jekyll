SITE_DIR := _site
BUNDLE ?= bundle
HTMLPROOFER_ARGS ?=

.PHONY: all build check clean

all: clean build check

build:
	$(BUNDLE) exec jekyll build

check:
	./_build/check-links.sh $(HTMLPROOFER_ARGS)

clean:
	rm -rf $(SITE_DIR)
