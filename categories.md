---
layout: directory
title: Categories
---

This page lists all lessons on the Programming Historian by category.  
See the [main directory]({{ site.baseurl }}/lessons) for a more 
structured listing of lessons.

{% for cat in site.data.categories %}
# {{ cat }}

{% for page in site.pages %}
{% for pc in page.categories %}

{% if pc == cat %} 
- [{{ page.title }}]({{ page.url }})
{% endif %} 

{% endfor %}
{% endfor %}

{% endfor %}
         
