---
title: Lessons published in partnership with Jisc and The National Archives
layout: blank
redirect_from: /jisc-tna-partnership
---

# Lessons published in partnership with [Jisc](https://www.jisc.ac.uk/) and [The National Archives](https://www.nationalarchives.gov.uk/)

<!-- Partnership blurb -->
These lessons are part of a special series exploring computational analysis of large-scale digital collections. They are published with the generous support and partnership of [Jisc](https://www.jisc.ac.uk/) and [The National Archives](https://www.nationalarchives.gov.uk/).

<!-- Defines an array to find the lessons that are part of the partnership -->
{% assign partnership = "Jisc, The National Archives" | split: ", " %}

<!-- Loops through the lessons to find the ones that are part of the partnership -->
{% for lesson in site.pages %}
{% if lesson.lesson-partners == partnership %}

- [{{ lesson.title }}]({{ lesson.url }})

{% endif %}
{% endfor %}
