---
title: Politique de retrait des leçons
layout: blank
original: lesson-retirement-policy
---

# Politique de retrait des leçons

Les rédacteurs et les rédactries du _Programming Historian_ font de leur mieux pour maintenir les leçons en ligne, même si des problèmes mineurs peuvent inévitablement survenir.
Néanmoins, l'évolution au fil du temps des technologies ou des concepts mobilisés dans un cours peut être importante au point que les utilisateurs et les utilisatrices ne seront plus en mesure de terminer la leçon avec succès.
Dans de tels cas, l'équipe éditoriale du _Programming Historian_ peut prendre la décision de "retirer" une leçon: si la page reste publiée, un avertissement est ajouté informant que certaines composantes du cours peuvent ne pas fonctionner comme initialement prévu, et la leçon est enlevée du répertoire des leçons actives.

Nous ne procédons pas facilement au retrait des leçons.
Si l'équipe éditoriale commence à recevoir des informations concernant d'éventuels problèmes sur une leçon, nous allons les examiner et tenter de les résoudre.
Il arrive fréquemment de décider qu'il n'est pas nécessaire de retirer la leçon:

- Lorsque des corrections peuvent se faire facilement pour réviser le formattage d'une leçon ou remplacer quelques URLs obsolètes, nous les prenons en charge.
- Lorsque de nouvelles méthodes semblent préférables à celles discutées dans une leçon, mais que les technologies mobilisées restent néanmoins efficaces et disponibles, la leçon **n'est pas** retirée. Elle peut en effet servir encore en tant qu'outil d'apprentissage, tout en illustrant quelles étaient les techniques de l'histoire numérique au moment de sa publication.

Toutefois, lorsqu'il devient clair que des changements essentiels sont nécessaires dans le code, le texte et/ou les images fournies, qui déboucheraient sur le remaniement complet de la leçon, dans ce cas nous ouvrons un ticket public pour discuter entre tous les membres de l'équipe éditoriale de la possibilité de retirer cette leçon.

Si des membres de l'équipe éditoriale ou de la communauté plus large qui l'entoure ont la volonté et la possibilité d'offrir leur expertise, il peut alors être envisagé de créer une leçon mise à jour, dérivée de celle d'origine.
En accord avec notre licence [CC-BY](https://creativecommons.org/licenses/by/4.0/deed.fr), cette version dérivée sera créditée à l'auteur(e) de la leçon originale, ainsi qu'aux personnes qui auront contribué à son élaboration.

Qu'une leçon dérivée soit créée ou pas, voici les étapes à suivre pour retirer une leçon :

1. La leçon sera déplacée de `https://programminghistorian.org/fr/lecon/TITRE-DE-LA-LEÇON` à `https://programminghistorian.org/fr/lecons/retrait/TITRE-DE-LA-LEÇON`. Une redirection sera mise en place pour que des liens pointant à l'URL originelle renvoient l'utilisateur à la nouvelle URL.

2. Une fois la leçon retirée, celle-ci n'apparaît plus dans le répertoire des leçons et elle est aussi enlevée de la liste de publications sur Twitter. Les rédacteurs et les rédactrices du Programming Historian peuvent trouver toutes les instructions nécessaires sur le wiki pour enlever une leçon du bot Twitter. 

3. L'avertissement suivant est ajouté en haut de la page de la leçon retirée:
    <div class="alert alert-warning">{{ site.data.snippets.retired-definition[page.lang] | markdownify }}

## Autres consignes sur la pérennisation des leçons

{% comment %}
The following anchors need to be checked/replaced once all pages have been created and published in the FR branch)
[Author Guidelines for Writing Sustainably](/author-guidelines#write-sustainably)

[Reviewer Guidelines for Assessing Lesson Sustainability](/reviewer-guidelines#sustainability)

[Consignes aux rédacteurs et rédactrices pour assurer la pérennisation des leçons]((/consignes-redacteurs#c-perennisation-et-internationalisation)) [Editor Guidelines for Fostering Lesson Sustainability](/editor-guidelines#c-sustainability-review)
{% endcomment %}

## Leçons retirées

{% assign retired = site.pages | where: "retired", "true" %}
{% for lesson in retired %}
[{{ lesson.title }}]({{ lesson.url }})
{% endfor %}
