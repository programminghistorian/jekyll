---
title: Lições publicadas em parceria com Jisc e The National Archives
layout: blank
redirect_from: /jisc-tna-partnership
---

# Lições publicadas em parceria com [Jisc](https://www.jisc.ac.uk/) e [The National Archives](https://www.nationalarchives.gov.uk/)

<!-- Partnership blurb -->
Estas lições fazem parte de uma série especial que explora a análise computacional de colecções digitais em grande escala. São publicadas com o generoso apoio e parceria da [Jisc](https://www.jisc.ac.uk/) e [The National Archives](https://www.nationalarchives.gov.uk/).

<!-- Defines an array to find the lessons that are part of the partnership -->
{% assign partnership = "Jisc, The National Archives" | split: ", " %}

<!-- Loops through the lessons to find the ones that are part of the partnership -->
{% for lesson in site.pages %}
{% if lesson.lesson-partners == partnership %}

- [{{ lesson.title }}]({{ lesson.url }})

{% endif %}
{% endfor %}
