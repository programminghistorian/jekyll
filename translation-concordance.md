---
layout: blank
title: Translation Concordance
---

An automatically-generated list of page translation relationships across this site.

{% assign original_slugs = site.pages | where_exp: "item", "item.original != nil" | map: "original" | uniq %}

<table>
  <tr>{% for l in site.data.snippets.language-list %}
    <th>{{ l }}</th>{% endfor %}
  </tr>
  {% for s in original_slugs %}
  {% assign aug_s = "." | prepend: s %}
  {% assign translated_pages = site.pages | where: "original", s %}
  {% assign original_page = site.pages | where_exp: "item", "item.name contains aug_s" | where_exp: "item", "item.name != 'redirect.html'" %}
  {% assign page_versions = translated_pages | concat: original_page %}
  <tr>
    {% for l in site.data.snippets.language-list %}
    {% assign p = page_versions | where: "lang", l | first %}
    <td><a href="{{p.url}}">{{ p.title }}</a></td>
    {% endfor %}
  </tr>
{% endfor %}
</table>
