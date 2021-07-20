---
title: Índice de Lições
layout: blank
permalink: /pt/licoes/
original: lessons
---

# Índice de Lições

As nossas lições estão organizadas por diferentes fases do processo de pesquisa, bem como por tópicos gerais. Use os botões para filtrar as lições por categoria. Se não encontrar a competência, tecnologia ou ferramenta que procura, por favor, [informe-nos]({{ site.baseurl }}/pt/reportar-um-erro)!

{% comment %}
This creates a variable you can call to just pull lessons (which are the only pages with 'Lesson: true' in their front matter, courtesy of config.yml setting the scope of site URLs containing the 'lessons' path to follow 'lesson: true').
{% endcomment %}

{% assign alllessons = site.pages | where: "lesson", "true" | where: "lang", "pt" %}

{% comment %}
Pulls the parts of the page that filter and sort lesson info from includes/lesson-index.html. Note that a separate file, includes/lesson_describe.html, creates the actual display of lesson info on the page, and includes/lesson-slug.html creates the appropriate lesson slug (used in the link to individual lesson pages, avatar links, and image paths.).
{% endcomment %}

{% include lesson-index.html %}
