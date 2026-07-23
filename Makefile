# Makefile to build Jekyll and run HTMLProofer without YAML

SITE_DIR := _site
LOG_FILE := htmlproofer-output.txt
BUNDLE ?= bundle

all: clean build check

build:
	@echo "🔨 Building Jekyll site..."
	$(BUNDLE) exec jekyll build

check:
	@echo "⏱️ Checking HTML links in $(SITE_DIR)..."
	@start=$$(date +%s); \
	$(BUNDLE) exec htmlproofer $(SITE_DIR) \
	  --assume-extension .html \
	  --ignore-missing-alt \
	  --ignore-empty-alt \
	  --only-4xx \
	  --ignore-status-codes "429,403,400,415" \
	  --ignore-urls "/github\.com\/programminghistorian/,/gutenberg\.org/,/espanol/,/deprecated/,/collection\.britishmuseum\.org/,/analytics\.hathitrust\.org/,/docnow\.io/,/doxygen\.nl/,/doi\.org\/10\.34190\/JEL\.17\.3\.002/,/doi\.org\/10\.22134\/trace\.82\.2022\.819/,/rubenalcaraz\.es\/manual-omeka\/?/,/web\.archive\.org\/web\/20180831094856\/http:\/\/www\.dlsi\.ua\.es\/~borja\/riilua\/6\.TopicModeling_v02\.pdf/" \
	  --ignore-files "/_site\/assets\//,/_site\/blog\//,/_site\/posts\//,/_site\/en\/lessons\/retired\//,/_site\/es\/lecciones\/retirada\//,/_site\/fr\/lecons\/retrait\//,/_site\/pt\/licoes\/retiradas\//" \
	  > $(LOG_FILE) 2>&1 \
	|| echo "❌ HTMLProofer found issues. See $(LOG_FILE)"; \
	end=$$(date +%s); \
	echo "✅ Finished in $$((end-start)) seconds"

clean:
	rm -rf $(SITE_DIR) $(LOG_FILE)
