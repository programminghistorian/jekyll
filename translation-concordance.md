---
layout: blank
title: Translation Concordance
---

An automatically-generated list of page translation relationships across this site.

{% assign translated_pages = site.pages | where_exp: "item", "item.original != nil" %}

<table>
  <tr>{% for l in site.data.snippets.language-list %}
    <th>{{ l }}</th>{% endfor %}
  </tr>
{% for p in translated_pages %}
  {% assign s_slug = p.original %}
  {% assign s = site.pages | where_exp: "item", "item.url contains s_slug" | where_exp: "item", "item.url != p.url" | where_exp: "item", "item.name != 'redirect.html'" | first %}
  <tr>
    {% for l in site.data.snippets.language-list %}
      {% if s.lang == l %}
    <td><a href="{{s.url}}">{{ s.title }}</a></td>
      {% else if p.lang == l %}
    <td><a href="{{p.url}}">{{ p.title }}</a></td>
      {% else %}
    <td></td>
    {% endif %}
    {% endfor %}
  </tr>
{% endfor %}
</table>
