SITE_DIR := _site
BUNDLE ?= bundle
HTMLPROOFER_ARGS ?=

.PHONY: all build check check-internal clean

all: clean build check

build:
	@echo "Building Jekyll site..."
	$(BUNDLE) exec jekyll build

check:
	@echo "Checking internal and external HTML links..."
	$(BUNDLE) exec htmlproofer $(SITE_DIR) \
	  --assume-extension .html \
	  --ignore-missing-alt \
	  --ignore-empty-alt \
	  --allow-missing-href \
	  --no-check-internal-hash \
	  --no-enforce-https \
	  --only-4xx \
	  --ignore-status-codes 429,403,400,415 \
	  --ignore-urls "/github\.com\/programminghistorian/,/gutenberg\.org/,/espanol/,/deprecated/,/collection\.britishmuseum\.org/,/analytics\.hathitrust\.org/,/docnow\.io/,/doxygen\.nl/,/doi\.org\/10\.34190\/JEL\.17\.3\.002/,/doi\.org\/10\.22134\/trace\.82\.2022\.819/,/rubenalcaraz\.es\/manual-omeka\/?/,/web\.archive\.org\/web\/20180831094856\/http:\/\/www\.dlsi\.ua\.es\/~borja\/riilua\/6\.TopicModeling_v02\.pdf/" \
	  --ignore-files "/_site\/assets\//,/_site\/blog\//,/_site\/posts\//,/_site\/en\/lessons\/retired\//,/_site\/es\/lecciones\/retirada\//,/_site\/fr\/lecons\/retrait\//,/_site\/pt\/licoes\/retiradas\//" \
	  $(HTMLPROOFER_ARGS)

check-internal:
	$(MAKE) check HTMLPROOFER_ARGS=--disable-external

clean:
	rm -rf $(SITE_DIR)
