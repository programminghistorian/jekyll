# Makefile to build Jekyll and run HTMLProofer without YAML

SITE_DIR := _site
LOG_FILE := htmlproofer-output.txt

all: build check

build:
	@echo "🔨 Building Jekyll site..."
	bundle exec jekyll build

check:
	@echo "⏱️ Checking HTML links in $(SITE_DIR)..."
	@start=$$(date +%s); \
	bundle exec htmlproofer $(SITE_DIR) \
	  --assume-extension \
	  --ignore-missing-alt \
	  --ignore-empty-alt \
	  --only-4xx \
	  --ignore-status-codes "429,403,400" \
	  --ignore-urls "/github\.com\/programminghistorian/,/gutenberg\.org/,/espanol/,/deprecated/,/collection\.britishmuseum\.org/,/analytics\.hathitrust\.org/,/images\/intro-a-google-maps-y-google-earth\/geo-es\d+\.png/,/http:\/\/humanidadesdigitaleshispanicas\.es\//,/http:\/\/dhawards\.org\//,/es\/guia-para-autores#paso-1-proponer-una-nueva-lección/,/fr\/consignes-auteurs#étape-1-proposer-une-nouvelle-leçon/,/pt\/directrizes-autor#etapa-1-propor-uma-nova-lição/" \
	  --ignore-files "/_site\/assets\//,/_site\/retired\//,/_site\/retirada\//,/_site\/retrait\//,/_site\/posts\//,/_site\/blog\//" \
	  > $(LOG_FILE) 2>&1 \
	|| echo "❌ HTMLProofer found issues. See $(LOG_FILE)"; \
	end=$$(date +%s); \
	echo "✅ Finished in $$((end-start)) seconds"

clean:
	rm -rf $(SITE_DIR) $(LOG_FILE)