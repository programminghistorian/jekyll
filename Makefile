# Makefile to build Jekyll and run HTMLProofer without YAML

SITE_DIR := _site
LOG_FILE := htmlproofer-output.txt

all: build check

build:
	@echo "🔨 Building Jekyll site..."
	@bundle exec jekyll build

check:
	@echo "⏱️ Checking HTML links in $(SITE_DIR)..."
	@start=$$(date +%s); \
	bundle exec htmlproofer $(SITE_DIR) \
	  --assume-extension \
	  --check-img-alt=false \
	  --only-4xx \
	  --http-status-ignore 429,403,400 \
	  --url-ignore \
	    "/\/\/www.gutenberg.org\/.*?/" \
	    "/https:\/\/github.com\/programminghistorian\/.*?/" \
	    "/https:\/\/github.com\/orgs\/programminghistorian\/.*?/" \
	    "/\#/" \
	    "/espanol/" \
	    "/deprecated/" \
	    "/collection.britishmuseum.org/" \
	    "/analytics.hathitrust.org/" \
	    "/fr.wikipedia.org\/wiki/" \
	    "/https:\/\/web.archive.org\/web\/20180831094856\/http:\/\/www.dlsi.ua.es\/~borja\/riilua\/6.TopicModeling_v02.pdf/" \
	    "https://github.com/programminghistorian/jekyll/commits/gh-pages" \
	    "https://github.com/programminghistorian/jekyll/commits/gh-pages/.*" \
	  --directory-ignore \
	    $(SITE_DIR)/assets \
	    $(SITE_DIR)/retired \
	    $(SITE_DIR)/retirada \
	    $(SITE_DIR)/retrait \
	    $(SITE_DIR)/posts \
	  --ignore-elements pre,code,script \
	  --log-level debug \
	  > $(LOG_FILE) 2>&1 \
	|| echo "❌ HTMLProofer found issues. See $(LOG_FILE)"; \
	end=$$(date +%s); \
	echo "✅ Finished in $$((end-start)) seconds"

clean:
	rm -rf $(SITE_DIR) $(LOG_FILE)