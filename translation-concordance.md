---
layout: blank
title: Translation Concordance
---

An automatically-generated list of lessons translation relationships across our publications.

{% assign original_pages = site.pages | where: "layout", "lesson" | where_exp: "item", "item.retired != 'true'" %}

<table>
  <tr>{% for l in site.data.snippets.language-list %}
    <th>{{ l }}</th>{% endfor %}
  </tr>
  {% for p in original_pages %}
  {% assign reverse_p = p.name | split: "." | first %}
  {% assign translated_pages = site.pages | where: "original", reverse_p %}
  {% assign page_versions =  p | concat: translated_pages %}
  <tr>
    {% for l in site.data.snippets.language-list %}
    {% assign sp = page_versions | where: "lang", l | first %}
    <td><a href="{{sp.url}}">{{ sp.title }}</a></td>
    {% endfor %}
  </tr>
{% endfor %}
</table>
