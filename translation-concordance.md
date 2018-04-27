---
layout: blank
title: Translation Concordance
---

An automatically-generated list of page translation relationships across this site.

{% assign translated_pages = site.pages | where_exp: "item", "item.original != nil" %}
{% for p in translated_pages %}
  {% assign s_slug = p.original %}
  {% assign s = site.pages | where_exp: "item", "item.url contains s_slug" | where_exp: "item", "item.url != p.url" | where_exp: "item", "item.name != 'redirect.html'" | first %}
  - [{{ s.title }}]({{ s.url }}) [{{ s.lang }}] <-> [{{ p.title }}]({{ p.url }}) [{{ p.lang }}]
{% endfor %}
