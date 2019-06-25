---
title: Index des leçons
layout: blank
permalink: /fr/lecons/
original: lessons
---

# Index des leçons
Nos leçons sont organisées en fonction des phases essentielles du processus de recherche, mais aussi en fonction de sujets généraux. Utilisez les boutons pour filtrer les leçons par catégories. Si vous ne pouvez pas trouver la compétence, la technologie ou l'outil que vous recherchez, [faites-le nous savoir]({{site.baseurl}}/feedback) s'il-vous-plaît!

{% comment %}
Cela crée une variable que vous pouvez appeler pour juste chercher ("pull") des leçons (qui sont les seules pages comportant 'Lesson: true' dans leur en-tête, avec l'aimable autorisation de config.yml qui fixe le champ des URLs contenant le chemin vers les 'leçons' de façon à suivre 'lesson true').
{% endcomment %}

{% assign alllessons = site.pages | where: "lesson", "true" | where: "lang", "fr" %}

{% comment %}
Cherche ("pulls") les parties de la page qui filtre et présente les informations associées aux leçons depuis includes/lesson-index.html. Notez qu'un fichier séparé,  includes/lesson_describe.html, crée la présentation actuelle des informations associées aux leçons sur la page, et includes/lesson-slug.html crée le slug de leçon approprié (utilisé dans les liens vers les pages individuelles des leçons, les liens vers les avatars et les chemins vers les images.).
{% endcomment %}

{% include lesson-index.html %}
