---
title: Leçons publiées en partenariat avec Jisc et The National Archives
layout: blank
redirect_from: /jisc-tna-partnership
---

# Leçons publiées en partenariat avec [Jisc](https://www.jisc.ac.uk/) et [The National Archives](https://www.nationalarchives.gov.uk/)

<!-- Partnership blurb -->
Ces leçons font partie d'une série spéciale explorant l'analyse computationnelle de corpus numériques à grande échelle. Elles sont publiées grâce au soutien généreux et au partenariat de [Jisc](https://www.jisc.ac.uk/) et [The National Archives](https://www.nationalarchives.gov.uk/). 

<!-- Defines an array to find the lessons that are part of the partnership -->
{% assign partnership = "Jisc, The National Archives" | split: ", " %}

<!-- Loops through the lessons to find the ones that are part of the partnership -->
{% for lesson in site.pages %}
{% if lesson.lesson-partners == partnership %}

- [{{ lesson.title }}]({{ lesson.url }})

{% endif %}
{% endfor %}
