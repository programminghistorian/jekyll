#!/bin/bash

# Intended to be run after prep_for_pandoc.py

for file in `ls ./modified_html/*.html`
do
	pandoc \
	--from=html \
	--to=markdown-header_attributes-fenced_code_attributes \
	--standalone \
	--template=jekyll.md \
	--reference-links \
	--filter=pandoc_filter.py \
	$file -o ./lessons/`basename $file .html`.md
done
