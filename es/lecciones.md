---
title: Índice de lecciones
layout: blank
permalink: /es/lecciones/
original: lessons
---


# Índice

Nuestras lecciones se organizan en fases del proceso de investigación y por temas generales. Utiliza los botones para filtrar las lecciones por categoría. Si no encuentras una habilidad, técnica o herramienta, por favor, ponte en [contacto]({{ site.baseurl }}/es/retroalimentacion) con nosotros.


{% comment %}
See documentation on the use of alllessons and lesson-index in /lessons.md
{% endcomment %}

{% assign alllessons = site.pages | where: "lesson", "true" | where: "lang", "es" %}

{% include lesson-index.html %}
