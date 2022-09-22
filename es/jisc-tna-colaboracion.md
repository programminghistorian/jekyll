---
title: Lecciones publicadas en colaboración con JISC y The National Archives
layout: blank
redirect_from: /jisc-tna-partnership
---

# Lecciones publicadas en colaboración con [JISC](https://www.jisc.ac.uk/) y [The National Archives](https://www.nationalarchives.gov.uk/)

<!-- Partnership blurb -->
Esta lección es parte de una serie especial sobre el análisis computacional de colecciones digitales a gran escala. Se publica con el generoso apoyo y colaboración de [Jisc](https://www.jisc.ac.uk/) y [The National Archives](https://www.nationalarchives.gov.uk/).

<!-- Defines an array to find the lessons that are part of the partnership -->
{% assign partnership = "JISC, The National Archives" | split: ", " %}

<!-- Loops through the lessons to find the ones that are part of the partnership -->
{% for lesson in site.pages %}
{% if lesson.lesson-partners == partnership %}

- [{{ lesson.title }}]({{ lesson.url }})

{% endif %}
{% endfor %}
