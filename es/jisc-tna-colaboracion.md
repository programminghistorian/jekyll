---
title: Lecciones publicadas en colaboración con Jisc y The National Archives
layout: blank
redirect_from: /jisc-tna-partnership
---

# Lecciones publicadas en colaboración con [Jisc](https://www.jisc.ac.uk/) y [The National Archives](https://www.nationalarchives.gov.uk/)

<!-- Partnership blurb -->
Estas lecciones forman parte de una serie especial sobre análisis computacional a gran escala de colecciones digitales. Se publican con el generoso apoyo y colaboración de [Jisc](https://www.jisc.ac.uk/) y [The National Archives](https://www.nationalarchives.gov.uk/).

<!-- Defines an array to find the lessons that are part of the partnership -->
{% assign partnership = "Jisc, The National Archives" | split: ", " %}

<!-- Loops through the lessons to find the ones that are part of the partnership -->
{% for lesson in site.pages %}
{% if lesson.lesson-partners == partnership %}

- [{{ lesson.title }}]({{ lesson.url }})

{% endif %}
{% endfor %}
