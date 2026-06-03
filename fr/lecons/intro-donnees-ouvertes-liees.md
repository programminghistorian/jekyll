---
title: "Introduction aux principes des données ouvertes liées"
slug: intro-donnees-ouvertes-liees
original: intro-to-linked-data
layout: lesson
collection: lesson
date: 2017-05-07
translation_date: 2026-06-03
authors:
- Jonathan Blaney
reviewers:
- Terhi Nurmikko-Fuller
- Matthew Lincoln
editors:
- Adam Crymble
translator:
- David Valentine
translation-editor:
- Daphné Mathelier
translation-reviewer:
- Aude Julien Da Cruz Lima
- Mattia Bunel
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/643
difficulty: 1
activity: acquiring
topics: [lod]
abstract: Cette leçon présente les concepts fondamentaux des données ouvertes liées (Linked Open Data), incluant les URI, les ontologies, les formats de données RDF et une introduction en douceur au langage de requête SPARQL.
avatar_alt: Un vieil homme avec une femme à chaque bras
doi: 10.46430/phfr0042
---

{% include toc.html %}

## Introduction et portée de la leçon

Cette leçon offre une brève et concise introduction aux [données ouvertes liées (DOL)](https://perma.cc/89CY-RJU6) (Linked Open Data, ou LOD en anglais)[^3]. Aucune connaissance préalable n’est attendue. Au terme de votre lecture, vous devriez avoir une bonne compréhension des concepts qui sous-tendent les DOL et de la façon dont elles sont créées et utilisées. La leçon s’organise en cinq sections auxquelles s’ajoutent des lectures complémentaires&nbsp;:

1. Que sont les données ouvertes liées&nbsp;?
2. Le rôle des [identifiants uniformes de ressource](https://perma.cc/B4A4-HUL2) (URI, Uniform Resource Identifier)
3. Comment s’organise la connaissance avec les données ouvertes liées&nbsp;: les [ontologies](https://perma.cc/SBK2-VFGY)
4. Le cadre de description [RDF](https://perma.cc/34AR-SNQB) et ses formats de données
5. Explorer les données ouvertes liées avec [SPARQL](https://perma.cc/Q95R-YHAA)
6. Lectures et ressources complémentaires

Cette leçon peut être complétée en quelques heures et il pourrait vous être utile de vous attarder ou de relire certaines parties pour solidifier votre compréhension. Les termes techniques ont été liés à leur page correspondante sur Wikipédia en français. Nous vous encourageons à prendre le temps de lire les pages consacrées aux termes qui vous posent problème. À la suite de votre initiation à certains principes fondamentaux des DOL, c’est la pratique qui demeure la meilleure façon d’améliorer et d’approfondir vos connaissances. Cette leçon propose une mise en pratique immédiate. À la fin de cette leçon, vous devriez comprendre les fondements des DOL, incluant les termes et les concepts clés.

Si vous souhaitez apprendre à explorer les DOL en utilisant le langage de requête [SPARQL](https://perma.cc/Q95R-YHAA), je recommande la leçon (en anglais) &laquo;&nbsp;[Using SPARQL to access Linked Open Data](/en/lessons/retired/graph-databases-and-SPARQL)&nbsp;&raquo; de Matthew Lincoln, qui vous permettra d’effectuer un suivi pratique du survol conceptuel offert dans la présente leçon.

<div class="alert alert-info">
N.B. La leçon de Matthew Lincoln est obsolète et n’est plus mise à jour par le <i>Programming Historian</i>. La méthodologie enseignée dans cette leçon demeure tout de même fort pertinente et pourrait être adaptée à d’autres contextes. Pour en savoir plus, vous pouvez consulter la note en ouverture de la leçon de Lincoln.
</div>

Afin de fournir une base solide pour la maîtrise de ces fondements, cette leçon ne présentera pas de manière exhaustive l’ensemble des concepts liés aux DOL. Les deux notions suivantes ne seront pas couvertes par cette leçon&nbsp;:

1. Le [web sémantique](https://perma.cc/EM2Z-VBSH) et [les processus d’inférence](https://perma.cc/N348-HLG2) sur les [jeux de données](https://perma.cc/S75G-LVWT). Par exemple, un moteur d’inférence permettrait de déduire que George VI est le frère ou le demi-frère d’Edward VIII, étant donné que a) Edward VIII est le fils de George V et que b) George VI est le fils de George V. Cette leçon ne couvre pas ce type de tâche.
2. La création et la mise en ligne de jeux de données ouvertes liées dans le [&laquo;&nbsp;linked open data cloud&nbsp;&raquo;](https://lod-cloud.net) (en anglais). Le partage de vos DOL est un important principe qui est encouragé plus bas. Cependant, les détails techniques de l’exposition des DOL dans le &laquo;&nbsp;linked data cloud dépassent la portée de cette leçon. Quelques ressources pour vous aider avec cette tâche sont disponibles à la fin de la leçon.

## Que sont les données ouvertes liées&nbsp;?

Les DOL sont constituées d’informations structurées dans des formats conçus pour un traitement par des [agents logiciels](https://perma.cc/984M-QPMT). Elles ne sont donc pas toujours faciles à lire par les humains. Ne vous laissez pas rebuter par cela, puisqu’en comprenant les principes des DOL, vous pourrez demander à un ordinateur d’en effectuer la lecture pour vous.

Si tous les jeux de données publiés étaient ouverts et utilisaient le même format pour structurer l’information, il serait possible de tous les interroger simultanément. L’analyse d’un grand volume de données est potentiellement beaucoup plus puissante que l’utilisation des jeux de données disséminés séparément sur le web, une pratique qui mène au phénomène des [silos d’information](https://perma.cc/9KQQ-PGES) (en anglais). Les jeux de données [interopérables](https://perma.cc/8Q7B-PU68) sont l’objectif vers lequel tendent les communautés praticiennes des DOL.

Pour atteindre ce but, il faut toujours se rappeler les trois principes suivants&nbsp;:

1. **Utiliser un format standard reconnu pour les DOL**.
Afin qu’elles fonctionnent adéquatement, les DOL doivent être [structurées](https://perma.cc/PE67-CDAJ) dans des formats standards afin que les ordinateurs qui les interrogent puissent les reconnaître et les traiter. Il existe plusieurs formats pour les DOL, dont certains sont abordés plus bas.
2. **Référer à une entité de façon normalisée**. Si vous avez des données sur une même sujet (que ce soit un lieu, un endroit ou une personne) dans plusieurs emplacements, il faut s’assurer de s’y référer de la même façon dans toutes les instances.
3. **Publier des données ouvertes**. L’ouverture des données signifie que tout le monde peut accéder et utiliser les données sans frais et dans un format qui ne soit pas dépendant d’un [logiciel propriétaire](https://perma.cc/99LE-8QX4).

Commençons par un exemple de données qui décrivent une personne en utilisant une approche [attribut-valeur](https://perma.cc/4VLG-47XM) (en anglais) typique en informatique[^7]&nbsp;:

```
personne=nombre
```

Dans ce cas, l’attribut indique qu’il s’agit d’une personne et la valeur est un nombre indiquant qui est cette personne.
Le nombre assigné pourrait être généré de façon aléatoire ou utiliser un numéro existant préalablement associé à cet individu.
Cette dernière approche comporte de grands avantages&nbsp;: si tous les jeux de données qui mentionnent cette personne utilisent *exactement le même numéro* et *exactement le même format*, alors nous pouvons assurément retrouver cet individu dans tout ensemble de données respectant ces règles. 

Créons un exemple en utilisant Jack Straw&nbsp;: il s’agit du nom à la fois d’un rebelle anglais du XIV<sup>e</sup> siècle et d’un important ministre britannique de l’administration de Tony Blair. Il sera évidemment utile de pouvoir différencier ces deux personnes qui partagent le même nom. En utilisant le modèle ci-dessus, dans lequel chaque personne est représentée par un numéro unique, associons le ministre britannique Jack Straw au numéro `64183282`. La paire attribut-valeur qui en résulte serait donc&nbsp;:

```
personne=64183282
```

Et associons maintenant [Jack Straw, le leader rebelle](https://perma.cc/96TT-BGN4), au numéro `33059614`. La paire attribut-valeur serait cette fois&nbsp;:

```
personne=33059614
```

Si toute personne qui crée des DOL utilise ces numéros pour faire référence respectivement aux deux Jack Straw, nous pouvons maintenant rechercher la personne identifiée par le numéro `64183282` dans un jeu de données ouvertes liées en étant confiant que nous obtiendrons la bonne personne ― dans ce cas, le ministre.

Les paires attribut-valeur peuvent également contenir de l’information sur d’autres types d’entités&nbsp;: des lieux, par exemple. Jack Straw, le politicien contemporain, était membre du parlement britannique, représentant de la circonscription de Blackburn. Au Royaume-Uni, il y a plusieurs lieux nommés Blackburn, sans mentionner les autres Blackburn à travers le monde. En utilisant les principes esquissés jusqu’ici, nous pouvons désambiguïser les différentes instances de Blackburn en attribuant un identifiant unique au lieu lié à la circonscription britannique&nbsp;: Blackburn située dans le Lancashire, en Angleterre.

```
lieu=2655524
```

À ce stade, vous pourriez penser qu’il s’agit en fait de la fonction d’un catalogue de bibliothèque. En effet, il s’agit bien du concept de la [notice d’autorité](https://perma.cc/K9GL-R435), idée centrale en sciences de l’information (un fichier d’autorité est une liste normalisée de termes qui peuvent être utilisés dans un contexte particulier, par exemple pour le catalogage d’un livre). Dans les deux exemples esquissés plus haut, nous avons utilisé des fichiers d’autorité pour assigner des numéros (les identifiants uniques) aux Jack et à Blackburn. Les numéros utilisés pour les deux Jack Straw viennent du [Virtual International Authority File](https://perma.cc/4F7W-AUQN) (VIAF), qui est maintenu par un consortium international de bibliothèques afin de gérer les problèmes qui découlent de la myriade de possibilités dont nous disposons pour nous référer à une même personne. L’identifiant unique utilisé pour la circonscription de Blackburn est tiré de [GeoNames](http://www.geonames.org), une base de données géographique en accès libre.

Mais essayons d’être plus précis quant à ce que nous voulons dire par Blackburn dans cet exemple. Jack Straw représentait la circonscription parlementaire (un territoire représenté par un seul membre du parlement) de Blackburn dont les frontières ont changé à travers le temps. Le projet [Digging Into Linked Parliamentary Data](https://perma.cc/5VAA-8MHY)[^1], sur lequel j’ai travaillé, a produit des identifiants uniques pour les affiliations parlementaires et les circonscriptions de chaque membre du parlement. Dans cet exemple, Jack Straw représentait la circonscription connue comme &laquo;&nbsp;Blackburn&nbsp;&raquo; dans sa version existante à partir de 1955&nbsp;:

```
blackburn1955-current
```

VIAF étant un fichier d’autorité reconnu et maintenu, dédié aux personnes notables, il était particulièrement pertinent d’avoir recours à ses identifiants pour décrire Jack Straw. Comme la circonscription représentée par Straw était parfaitement couverte par les fichiers d’autorité créés dans le projet Dilipad, il s’agissait également d’une ressource pertinente à mobiliser. Malheureusement, il n’est pas toujours aussi évident de savoir quelle liste publiée en ligne est le meilleur choix. Une liste pourrait être plus largement utilisée qu’une autre, mais cette dernière pourrait être plus pertinente dans certains contextes. Dans certains cas, GeoNames pourrait mieux fonctionner que les identifiants Dilipad. Dans d’autres cas, il vous sera impossible de trouver un jeu de données contenant l’information nécessaire. Par exemple, imaginez que vous voudriez créer les paires attribut-valeur vous décrivant avec vos relations familiales immédiates. Dans ce cas, vous auriez à créer vos propres identifiants.

Le manque de régularité et de compatibilité des fichiers d’autorité est l’un des principaux défis auxquels les DOL sont confrontées à l’heure actuelle. [Tim Berners-Lee](https://perma.cc/YTY7-HZCE), qui a proposé une méthode pour lier les documents entre eux à travers un réseau, ce qui a mené à la création du World Wide Web, a longtemps été un chef de file dans la promotion des DOL. Pour favoriser davantage les usages des DOL, il a également proposé le système d’évaluation cinq étoiles ([*five-star rating system*](https://perma.cc/79VD-G5T4)) afin d’encourager tout le monde à tendre le plus possible vers les DOL. Essentiellement, il soutient non seulement la publication des données ouvertes, particulièrement si elles utilisent des formats ouverts et des standards accessibles, mais rappelle également qu'il est essentiel de lier ces données à celles des autres.

Une fois que tous ces éléments sont dotés d’identifiants uniques, la prochaine étape clé dans la création de DOL consiste à trouver un moyen de *décrire* la relation entre Jack Straw (`64183282`) et Blackburn (`blackburn1955-current`). Dans les DOL, les relations sont exprimées sous la forme de ce qui est connu comme étant un [triplet](https://perma.cc/BZ8X-RLY6). Créons donc un triplet qui représente la relation entre Jack Straw et sa circonscription&nbsp;:

```
personne:64183282
rôle:aReprésentéAuParlementBritannique
circonscription:"blackburn1955-current" .
```

La disposition (ou la [syntaxe](https://perma.cc/9RXD-ZXAL)) des triplets, incluant la ponctuation utilisée ci-dessus, sera abordée plus bas, dans la section sur RDF et sur les formats de données. Pour l’instant, concentrons-nous sur la structure fondamentale. Sans surprise, le triplet est constitué de trois parties, auxquelles on se réfère respectivement comme le sujet, le prédicat et l’objet&nbsp;:

| sujet     | prédicat             | objet              |
| --------------- | ------------------------- | ----------------------- |
| personne 64183282 | aReprésentéAuParlementBritanique | &#34;blackburn1955-current&#34; |

Typiquement, la représentation d’un triplet sous forme de diagramme se présente ainsi&nbsp;:

{% include figure.html filename="fr-tr-intro-aux-donnees-liees-01.png" alt="Graphe constitué de deux nœuds qui représentent respectivement le sujet et l’objet d’un triplet RDF, sous la forme de deux ovales liés entre eux par un arc directionnel, lui-même constitué d’une flèche qui représente le prédicat du triplet, allant du sujet vers l’objet." caption="Figure&nbsp;1. Représentation visuelle typique d’un triplet." %}

Donc notre triplet sur Jack Straw, dans une forme moins abstraite, pourrait être représenté de cette façon&nbsp;:

{% include figure.html filename="fr-tr-intro-aux-donnees-liees-02.png" alt="Graphe constitué de deux nœuds qui représentent respectivement Jack Straw et la circonscription électorale de Blackburn, sous la forme de deux ovales liés entre eux par un arc directionnel, lui-même constitué d’une flèche allant de Jack Straw vers Blackburn pour représenter la relation de représentation politique qui existe entre les deux entités." caption="Figure&nbsp;2. Représentation visuelle d’un triplet montrant que Jack Straw est député de Blackburn." %}

Pour l’instant, il y a trois éléments clés à garder en tête&nbsp;:

- Les DOL doivent être ouvertes et accessibles à quiconque sur internet (autrement, elles ne sont pas ouvertes)
- Les acteurs des DOL visent la standardisation des références aux entités uniques
- Les DOL sont constituées de triplets qui décrivent les relations entre les entités

## Le rôle des identifiants uniformes de ressource (URI)

Les [identifiants uniformes de ressource](https://perma.cc/B4A4-HUL2) (*Uniform Resource Identifier*, ou URI en anglais) sont un élément essentiel des DOL. L’URI permet d’identifier de façon fiable et unique une entité (une personne, un objet, une relation, etc.), de manière à pouvoir être utilisé par quiconque à travers le monde. Dans la section précédente, nous avons utilisé deux différents numéros pour identifier nos deux différents Jack Straw&nbsp;:

```
personne="64183282"
personne="33059614"
```

Le problème ici repose dans l’existence de nombreuses bases de données à travers le monde contenant des informations sur des personnes qui utilisent ces mêmes numéros et qui, pourtant, sont probablement toutes différentes. À l’extérieur de notre contexte immédiat, ces numéros n’identifient pas d’individus uniques. Essayons d’arranger cela. Voici les mêmes identifiants, mais sous forme d’URI&nbsp;:

```
http://viaf.org/viaf/64183282/
http://viaf.org/viaf/33059614/
```

Tout comme le numéro unique permet de différencier nos deux Jack Straw, les URI ci-dessus nous aident cette fois à lever l’ambiguïté entre tous les différents fichiers d’autorité accessibles en ligne. Dans ce cas, l’URI indique explicitement que nous utilisons VIAF comme fichier d’autorité. Vous avez déjà vu plusieurs fois cette forme de distinction sur le web. Il existe de nombreux sites web dans le monde avec des pages nommées `/home` ou `/faq`. Mais il n’y a pas de confusion puisque le [domaine](https://perma.cc/F9ZY-2MKB), soit la première partie du [localisateur uniforme de ressource](https://perma.cc/2A9Y-27A8) (*Uniform Resource Locator*, ou URL en anglais), par exemple `bbc.co.uk` ou `viaf.org`, est unique. Ainsi, toutes les pages qui font partie d’un domaine se différencient des autres `/faq` ou `/home` sur d’autres sites web.

Dans l’adresse `http://www.bbc.co.uk/faqs`, c’est la partie `bbc.co.uk` qui rend uniques les pages subséquentes. Ces considérations sont si évidentes pour les gens qui utilisent le web fréquemment qu’il n’y a même pas besoin d’y penser. De plus, vous savez probablement que si vous souhaitez créer un site web nommé `bbc.co.uk`, vous ne pourrez pas, puisque ce nom est déjà enregistré auprès de l’autorité appropriée, le [système de nom de domaine](https://perma.cc/8RAG-VPYV) (*Domain Name System*, ou DNS en anglais). L’enregistrement d’un nom de domaine en garantit l’unicité. Les URI doivent également être uniques.

Les exemples ci-dessus prennent la forme des URL, mais il est également possible de construire des URI qui n’ont rien de l’URL. Il existe de nombreuses façons d’utiliser des identifiants uniques pour les personnes et les choses. Pourtant, nous y pensons rarement&nbsp;: les codes-barres, les numéros de passeport ou même votre code postal sont tous conçus pour être uniques. Les numéros de téléphone sont fréquemment utilisés dans les annonces commerciales précisément parce qu’ils sont uniques. Toutes ces choses pourraient être utilisées comme des URI.

Lorsque nous avons créé les URI des entités décrites par le projet [Tobias](https://perma.cc/6GUX-Q5U9) (en anglais), nous avons choisi d’utiliser la structure d’une URL avec notre espace web institutionnel, établissant `data.history.ac.uk/tobias-project/` comme l’espace dédié à l’hébergement de ces URI. En utilisant `data.history.ac.uk` plutôt que `history.ac.uk`, nous avons établi une distinction claire entre les URI et les pages du site web. Par exemple, nous utilisons l’URI `http://data.history.ac.uk/tobias-project/person/15601` dans le projet Tobias. Bien que le format des URI mentionnés précédemment soit celui d’une URL, ils ne pointent pas vers des pages web (essayez-les dans un navigateur web). Bien des gens qui découvrent les DOL sont confus par ces distinctions. Toutes les URL sont des URI, mais tous les URI ne sont pas des URL. Un URI peut identifier n’importe quoi, tandis qu’une URL identifie une chose qui se trouve sur le web.

Une URL vous indique donc l’emplacement d’une page web, d’un fichier ou d’une ressource semblable. Un URI fait seulement le travail d’identification d’une chose, comme l’*International Standard Book Number* ([ISBN](https://perma.cc/49B8-JDQN)). Ainsi, l’ISBN `978-0-1-873354-6` identifie de façon unique l’édition reliée de *Baptism, Brotherhood and Belief in Reformation Germany* de Kat Hill, sans vous indiquer où vous pourrez vous en procurer une copie. Pour ce faire, vous aurez besoin d’en connaître la [cote](https://perma.cc/D6TZ-65QR), qui vous fournira l’emplacement exact du livre dans une bibliothèque donnée.

L’univers des URI est quelque peu jargonneux. Elles peuvent être dites [déréférençables](https://perma.cc/2ZV4-X35Q) ou non. Le déréférencement dénote simplement la transformation d’une référence abstraite en quelque chose d’autre. Par exemple, collez un URI dans la barre d’adresse d’un navigateur. Celui-ci renverra-t-il quelque chose&nbsp;? L’URI VIAF de l’historien Simon Schama est le suivant&nbsp;:

```
http://viaf.org/viaf/46784579
```

Si vous l’essayez dans un navigateur, vous obtiendrez une page web sur Simon Schama, qui contient des données structurées à son sujet et son historique de publication. Voilà qui est très pratique, puisque dans ce cas l’URI ne permet pas de déterminer clairement à qui ou même ce à quoi on réfère. De la même manière, si nous utilisions un numéro de téléphone mobile (avec un code international) comme l’URI d’une personne, alors il devrait être déréférençable. À l’autre bout du fil, quelqu’un pourrait répondre et ce pourrait même être Schama[^2].

Mais ce n’est pas essentiel. De nombreux URI ne sont pas déréférençables, comme nous l’avons constaté précédemment avec le projet Tobias.

L’exemple de VIAF nous mène vers une autre considération importante au sujet des URI&nbsp;: évitez d’en créer tant que ce n’est pas nécessaire. En effet, personnes et organismes ont concerté leurs efforts pour créer de bonnes listes d’URI. Les DOL ne pourront fonctionner adéquatement si nous dupliquons ces efforts en créant inutilement de nouveaux URI. VIAF, par exemple, bénéficie du support de nombreuses bibliothèques internationales. Si vous souhaitez utiliser des URI identifiant des personnes, VIAF est un excellent choix. Si une personne est introuvable dans VIAF ou dans d’autres fichiers d’autorité, c’est alors que vous devriez envisager de créer vos URI.

## Comment s’organise la connaissance avec les DOL&nbsp;: les ontologies

Ce n’est peut-être pas évident d’après les triplets examinés dans la première partie, mais les DOL peuvent répondre à des questions complexes. Lorsque vous rassemblez vos triplets, ils se constituent comme un [graphe](https://perma.cc/FA74-9Y8Y) grâce à la façon dont ils sont reliés. Supposons que nous voulons trouver une liste de toutes les personnes qui furent des élèves du compositeur Franz Liszt. Si l’information se trouve dans les triplets des données liées sur les pianistes et leurs professeurs, nous pourrons y accéder en utilisant une requête (nous examinerons ce langage de requête, appelé SPARQL, dans la dernière section).

Par exemple, le pianiste Charles Rosen était un élève de Moriz Rosenthal, lui-même élève de Franz Liszt. Ceci s’exprime avec deux triplets (pour rendre les exemples plus lisibles, nous utiliserons des chaînes de caractères au lieu de numéros d’identification[^6])&nbsp;:

```
"Franz Liszt" aEnseignéPianoÀ "Moriz Rosenthal" .
"Moriz Rosenthal" aEnseignéPianoÀ "Charles Rosen" .
```

Nous pourrions également créer nos triplets de cette façon&nbsp;:

```
"Charles Rosen" aApprisPianoDe "Moriz Rosenthal" .
"Moriz Rosenthal" aApprisPianoDe "Franz Liszt" .
```

Nous créons ces exemples pour illustrer le propos, mais si vous souhaitez lier vos données à d’autres jeux de données en ligne, vous devriez identifier les conventions qu’ils utilisent et vous y conformer. En fait, il s’agit d’une des caractéristiques les plus utiles des DOL&nbsp;:
une bonne partie du travail a été fait pour vous. De nombreuses personnes ont passé beaucoup de temps à développer des façons de modéliser l’information dans différents champs d’études, réfléchissant à la manière dont les relations peuvent être représentées dans ces domaines. Les modèles ainsi créés sont généralement connus comme étant des ontologies. Une ontologie est une abstraction qui permet la représentation de connaissances particulières sur le monde. Elle est conçue comme une [taxonomie](https://perma.cc/AH5E-GHHA) (une structure hiérarchique comme la [classification linnéenne](https://perma.cc/T3CF-P59S) des espèces), mais avec plus de flexibilité.

Une ontologie est plus flexible, car elle n’est pas strictement hiérarchique. Elle vise à représenter la fluidité du monde réel, au sein duquel les choses entretiennent des relations plus complexes que les représentations d’une structure hiérarchique en arbre. Au lieu de cela, une ontologie ressemble davantage à une toile d’araignée.

Peu importe ce que vous cherchez à représenter avec les DOL, nous vous suggérons de trouver un vocabulaire existant et de l’utiliser, plutôt que de tenter de créer le vôtre. Vous trouvez plusieurs des vocabulaires les plus utilisés en consultant le site [Vocabulaires Ouverts](https://vocabulaires-ouverts.inrae.fr/).

Puisque l’exemple présenté plus haut se concentre sur les pianistes, il serait convenable de repérer une ontologie appropriée plutôt que de créer notre propre système. Justement, il existe une [ontologie pour la musique](http://web.archive.org/web/20170715094229/http://www.musicontology.com/) (en anglais). En plus d’offrir une spécification aboutie, la documentation propose aussi des exemples utiles d’utilisations courantes. Vous pouvez visiter les [pages d’introduction](http://web.archive.org/web/20170718143925/http://musicontology.com/docs/getting-started.html) (en anglais) pour vous faire une meilleure idée de la façon dont vous pourriez utiliser cette ontologie en particulier.

Malheureusement, je ne trouve rien qui décrive la relation entre un professeur et son élève dans la *Music Ontology*. Mais elle est publiée de façon ouverte, ce qui permet de l’utiliser pour décrire d’autres caractéristiques du domaine de la musique, puis éventuellement de créer ma propre extension de ce modèle. Si je publie ainsi ouvertement mon extension, d’autres pourront l’utiliser à leur tour s’ils le souhaitent et elle pourrait même devenir un standard. Si la *Music Ontology* n’offre pas la relation dont j’ai besoin, le [projet Linked Jazz](https://perma.cc/AGM6-H9BM) (en anglais) permet l’utilisation du terme `mentorOf` qui semble bien fonctionner dans notre cas. Ce n’est pas une solution idéale, mais c’en est une qui s’efforce d’utiliser ce qui existe déjà.

Maintenant, si vous étudiiez l’histoire du [pianisme](https://perma.cc/98W9-LAMK), vous pourriez chercher à identifier les pianistes qui ont appris des élèves de Liszt afin d’établir une sorte d’arbre généalogique et de voir si les &laquo;&nbsp;descendants&nbsp;&raquo; de Liszt avaient quelque chose en commun. Vous pourriez chercher les élèves de Liszt, en faire une liste exhaustive, puis pour chacun d’eux tenter de dresser la liste de tous les élèves qu’ils ont eus. Avec les DOL, vous pourriez créer (encore une fois, si les triplets existent) une requête dont les grandes lignes seraient&nbsp;:

```
Donne-moi les noms de tous les pianistes qui ont appris de x
    où x a appris le piano de Liszt
```

Cela renverrait toutes les personnes existantes dans le jeu de données qui étaient élèves des élèves de Liszt. Cela dit, ne nous emballons pas trop vite&nbsp;: cette requête ne renverra pas tous les élèves de chaque élève de Liszt qui n’ont jamais vécu, car toutes ces informations n’existent probablement pas ou ne sont tout simplement pas disponibles dans les ensembles existant de triplets. Le traitement des données dans le monde réel révèle toutes sortes d’omissions et d’incohérences, comme nous pourrons le constater dans la section finale, alors que nous explorerons l’un des plus grands jeux de DOL, [DBpedia](https://www.dbpedia.org) (en anglais)[^4].

Si vous avez déjà utilisé des [bases de données relationnelles](https://perma.cc/MCK2-MLX9), vous pourriez penser qu’elles offrent le même genre de fonctionnalité. Dans le cas de Liszt, les informations sur les pianistes décrits plus haut pourraient s’organiser dans la base de données à l’aide d’une [table](https://perma.cc/4D72-AB3M) nommée &laquo;&nbsp;Élèves&nbsp;&raquo;&nbsp;:

| IDeleve | IDprofesseur |
| ------- | ------------ |
| 31      | 17           |
| 35      | 17           |
| 49      | 28           |
| 56      | 28           |
| 72      | 40           |

Si vous n’êtes pas à l’aise avec les bases de données, ne vous en faites pas. Mais vous pouvez probablement tout de même constater que certains pianistes de cette table ont le même professeur (les numéros 17 et 28). Sans entrer dans les détails, si Liszt était dans cette table, il serait assez facile d’extraire les élèves des élèves de Liszt en utilisant une [jointure](https://perma.cc/VM3T-6WVU).

Bien sûr, les bases de données relationnelles offrent des résultats similaires aux DOL. La grande différence, c’est que les DOL peuvent aller plus loin&nbsp;: elles peuvent connecter des ensembles de données qui ont été créés sans l’intention explicite d’être liés entre eux.
Cela est rendu possible par l’utilisation du cadre de description RDF et des URI.

## Le cadre de description [RDF](https://perma.cc/34AR-SNQB) et ses formats

Les DOL utilisent un standard défini par le [*World Wide Web Consortium*](https://perma.cc/E35S-BVHP) (W3C) nommé *[Resource Description Framework](https://perma.cc/34AR-SNQB)* (cadre de description RDF ou simplement RDF). Les standards sont utiles dans la mesure où ils sont largement adoptés ― pensez au système métrique ou aux tailles de vis standards ― même s’ils sont essentiellement arbitraires. RDF a été largement adopté comme standard pour les DOL.

Souvent, les DOL sont simplement appelées RDF (ou données RDF). Nous avons reporté la discussion sur RDF jusqu’à maintenant, car il s’agit d’un enjeu plutôt abstrait. RDF est un [modèle de données](https://perma.cc/K4KY-YLA6) qui décrit sur un plan théorique comment structurer des données. L’insistance sur l’utilisation des triplets (au lieu de quatre parties, de deux ou de neuf) est une règle de RDF. Mais sur le plan pratique, certaines options s’offrent à vous pour l’élaboration des graphes de données. Ainsi, RDF vous indique ce que vous devez faire, mais pas exactement comment vous y prendre. Ces choix se divisent en deux champs&nbsp;: la manière dont vous écrivez les choses (la sérialisation) et les relations que décrivent vos triplets.

### La sérialisation

La [sérialisation](https://perma.cc/2NZF-NAXY) est un terme technique pour parler de &laquo;&nbsp;la manière dont vous écrivez les choses&nbsp;&raquo;. Le mandarin standard peut s’écrire avec les caractères chinois traditionnels, avec les caractères chinois simplifiés ou avec le hanyu pinyin pour la romanisation. La langue elle-même ne change pas. De la même façon, RDF peut s’écrire sous différentes formes et nous examinerons deux d’entre elles. Il en existe d’autres, mais pour garder les choses simples, nous nous concentrerons sur les suivantes&nbsp;:

1. [Turtle](https://perma.cc/SRR9-36GF)
1. [RDF/XML](https://perma.cc/JU3F-HMWU)

Comprendre à quelle sérialisation vous avez affaire signifie que vous pourrez choisir les outils appropriés, conçus pour ce format. Par exemple, RDF peut se présenter dans une sérialisation au format [XML](https://perma.cc/X5QA-TMJB). Vous pourrez alors utiliser un outil ou une [bibliothèque logicielle](https://perma.cc/QBH9-SRGH) conçue spécifiquement pour le traitement de ce format, ce qui est utile si vous en connaissez déjà le fonctionnement. Reconnaître le format vous fournit également les bons mots-clés pour trouver de l’aide en ligne. Plusieurs ressources ouvrent leurs bases de données liées au téléchargement et vous pourriez être en mesure de choisir la sérialisation qui vous convient.

#### Turtle

&laquo;&nbsp;Turtle&nbsp;&raquo; est un jeu de mot en anglais. _Tur_ est le diminutif de &laquo;&nbsp;terse&nbsp;&raquo; et _tle_ celui de &laquo;&nbsp;triple language&nbsp;&raquo;. Turtle est une façon simple et pratique d’écrire des triplets.

Turtle utilise des alias ou des raccourcis que l’on appelle les [préfixes](https://perma.cc/852T-BALF) (en anglais). Ceux-ci nous épargnent d’avoir à écrire chaque fois les URI complets. Retournons vers l’URI que nous avons créé dans la section précédente&nbsp;:

```
http://data.history.ac.uk/tobias-project/person/15601
```

Nous ne voulons pas le saisir chaque fois que nous référons à cette personne (Jack Straw, souvenez-vous). Il suffit donc de déclarer notre raccourci&nbsp;:

```ttl
@prefix toby: <http://data.history.ac.uk/tobias-project/person/> .
```

Ainsi, Jack est `toby:15601`, qui remplace la forme longue de l’URI et qui est plus agréable à l’œil. J’ai choisi `toby`, mais je pourrais tout aussi bien choisir n’importe quelle chaîne de lettres.

Passons maintenant de Jack Straw à William Shakespeare et utilisons Turtle pour décrire certaines choses au sujet de ses œuvres. Nous devrons décider des fichiers d’autorité à utiliser, un processus qui, comme mentionné plus haut, se comprend mieux en examinant d’autres jeux de données ouvertes liées. Pour l’un de nos préfixes, nous utiliserons [Dublin Core](https://perma.cc/3AAT-9G8B), un standard générique pour les [métadonnées](https://perma.cc/9YM2-V88Y) documentaires, le fichier d’autorité du [*Library of Congress Control Number*](https://perma.cc/ZV96-MYTN) pour un autre préfixe et un dernier (VIAF) qui devrait vous être familier. Ensemble, Dublin Core et ces deux fichiers d’autorités fournissent des identifiants uniques pour toutes les entités que je vais utiliser dans cet exemple&nbsp;:

```ttl
@prefix lccn: <http://id.loc.gov/authorities/names/> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix viaf: <http://viaf.org/viaf/> .

lccn:n82011242 dc:creator viaf:96994048 .
```

Notez l’espacement du point final à la dernière ligne. C’est la façon dont Turtle indique la fin d’un triplet. Techniquement, cette espace n’est pas nécessaire, mais cela rend la lecture plus facile à la suite d’une longue chaîne de caractères. Dans l’exemple ci-dessus, `lccn:n82011242` représente Macbeth&nbsp;; `dc:creator` relie Macbeth à son auteur&nbsp;; `viaf:96994048` représente William Shakespeare.

Turtle vous permet également de lister des triplets sans vous obliger à répéter chaque URI lorsque vous venez tout juste de l’utiliser.
Ajoutons la date à laquelle les universitaires pensent que Macbeth a été écrit, en utilisant une paire attribut-valeur avec le vocabulaire Dublin Core&nbsp;: `dc:created "YYYY"`&nbsp;:

```ttl
@prefix lccn: <http://id.loc.gov/authorities/names/> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix viaf: <http://viaf.org/viaf/> .

lccn:n82011242 dc:creator viaf:96994048 ;
               dc:created "1606" .
```

Vous souvenez-vous de la structure d’un triplet, que nous avons traitée dans la section 1&nbsp;? Nous y avons vu cet exemple&nbsp;:

```ttl
1. personne 15601 (le sujet)
2. aReprésentéAuParlementBritanique (le prédicat)
3. "Blackburn" (l’objet)
```

L’essentiel, c’est que le prédicat relie le sujet et l’objet. Il décrit la relation entre eux. Le sujet vient en premier dans le triplet, mais c’est une question de choix, comme nous l’avons vu avec l’exemple d’une personne qui a appris le piano de Liszt.

Vous pouvez utiliser le point-virgule si le sujet est le même, mais que le prédicat et l’objet sont différents, ou une virgule si le sujet et le prédicat sont les mêmes et que seul l’objet diffère.

```ttl
lccn:no2010025398 dc:creator viaf:96994048 ,
    viaf:12323361 .
```

Nous déclarons ici que Shakespeare (96994048) et John Fletcher (12323361) étaient ensemble les créateurs de l’œuvre *The Two Noble Kinsmen*.

Les ontologies que je vous ai suggérées précédemment vous ont permis de jeter un œil sur les exemples de la [Music Ontology](http://web.archive.org/web/20170718143925/http://musicontology.com/docs/getting-started.html). J’espère qu’ils ne vous ont pas découragé.
Examinez-les de nouveau. Cela demeure compliqué, mais ont-ils plus de sens maintenant&nbsp;?

*Friend of a Friend* ([FOAF](https://perma.cc/2Q8U-S2JY)) est l’une des ontologies les plus accessibles. Elle est conçue pour décrire des personnes et les relations entre elles. Pour cette raison, elle est assez intuitive. Par exemple, si vous souhaitez m’écrire pour me dire que cette leçon est la meilleure chose que vous ayez jamais lue, voici mon adresse courriel exprimée par un triplet avec FOAF&nbsp;:

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

:Jonathan_Blaney foaf:mbox <mailto:jonathan.blaney@sas.ac.uk> .
```

#### RDF/XML

Contrairement à Turtle, RDF/XML peut sembler un peu lourd. Pour commencer, convertissons un seul triplet des données Turtle que nous avons créées plus haut&nbsp;: celui affirmant que Shakespeare est le créateur de *The Two Noble Kinsmen*&nbsp;:

```ttl
lccn:no2010025398 dc:creator viaf:96994048 .
```

En RDF/XML, avec les préfixes déclarés dans l’extrait XML suivant, cela donne&nbsp;:

```xml
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:dc="http://purl.org/dc/terms/">
  <rdf:Description rdf:about="http://id.loc.gov/authorities/names/no2010025398">
    <dc:creator rdf:resource="http://viaf.org/viaf/96994048"/>
  </rdf:Description>
</rdf:RDF>
```

Le format RDF/XML véhicule les mêmes informations que Turtle, mais s’écrit très différemment, en s’appuyant sur le principe d’imbrication des éléments XML.

Passons à un autre exemple pour montrer comment RDF/XML combine les triplets et, en même temps, pour présenter le modèle [*Simple Knowledge Organization System*](https://perma.cc/574Q-6U6R) (SKOS) qui est conçu pour encoder des [thésaurus](https://perma.cc/5BMN-BMVS) ou des [taxonomies](https://perma.cc/AH5E-GHHA).

```xml
<skosConcept rdf:about="http://www.ihr-tobias.org/concepts/21250/Abdication">
  <skos:prefLabel>Abdication</skos:prefLabel>
</skosConcept>
```

Nous déclarons ici que le concept SKOS `21250`, abdication, possède une étiquette linguistique préférentielle, &laquo;&nbsp;Abdication&nbsp;&raquo;. Le fonctionnement repose sur l’imbrication du prédicat et de l’objet à l’intérieur de l’élément sujet (qui inclut la partie `21250/Abdication`, valeur de l’attribut dans les termes de XML). L’élément XML imbriqué est le prédicat et le [nœud textuel](https://perma.cc/A4KS-DY94) &laquo;&nbsp;Abdication&nbsp;&raquo; est l’objet. Cet exemple est tiré d’un projet de publication d’un [thésaurus de l’histoire britannique et irlandaise](https://perma.cc/6GUX-Q5U9) (en anglais).

Tout comme avec Turtle, nous pouvons ajouter davantage de triplets. Nous allons déclarer que le terme *Abdication crisis (1936)* est plus spécifique dans notre hiérarchie, d’un niveau inférieur à *Abdication*&nbsp;:

```xml
<skosConcept rdf:about="http://www.ihr-tobias.org/concepts/21250/abdication">
  <skos:prefLabel>Abdication</skos:prefLabel>
</skosConcept>

<skosConcept rdf:about="http://www.ihr-tobias.org/concepts/21250/abdication">
  <skos:narrower rdf:resource="http://www.ihr-tobias.org/concepts/19838/abdication_crisis_1936"/>
</skosConcept>
```

Vous souvenez-vous de la façon dont les prédicats et les objets sont imbriqués dans le sujet&nbsp;? Dans cet exemple, nous l’avons fait deux fois pour le même sujet. Nous pouvons rendre cela moins verbeux en imbriquant les deux paires prédicat-objet dans un seul sujet&nbsp;:

```xml
<skosConcept rdf:about="http://www.ihr-tobias.org/concepts/21250/abdication">
  <skos:prefLabel>Abdication</skos:prefLabel>
  <skos:narrower rdf:resource="http://www.ihr-tobias.org/concepts/19838/abdication_crisis_1936"/>
</skosConcept>
```

Si vous êtes familier avec XML, ce sera un jeu d’enfant pour vous. Autrement, vous pourriez préférer un format comme Turtle. Mais l’avantage de RDF/XML, c’est que vous pouvez utiliser les outils de l’écosystème XML, comme les éditeurs spécialisés et les processeurs XML permettant, par exemple, de vérifier que votre document est bien formé. Si vous n’êtes pas du type XML, je vous recommande Turtle.

Pour valider la syntaxe de Turtle, vous pourrez utiliser des outils en ligne ([Easy RDF Converter](http://www.easyrdf.org/converter) ou [IDLab Turtle Validator](http://ttl.summerofcode.be)) ou encore [TurtleValidator](https://github.com/IDLabResearch/TurtleValidator), un outil facile à utiliser en [ligne de commande](https://perma.cc/Z8KQ-YNQ6).

## Explorer des données RDF avec SPARQL

Pour terminer, nous allons interroger des données ouvertes liées et explorer ce qu’on peut en tirer. Le langage de requête utilisé pour les DOL se nomme [SPARQL](https://perma.cc/Q95R-YHAA). C’est l’un de ces acronymes récursifs chers au monde technologique&nbsp;: *SPARQL Protocol and RDF Query Language*.

Comme je l’ai mentionné d’emblée, *Programming Historian* propose une [leçon entièrement dédiée](/en/lessons/retired/graph-databases-and-SPARQL) (en anglais) à SPARQL par Matthew Lincoln. Ma section finale n’est qu’un survol des fondements conceptuels de SPARQL. Si cela pique votre curiosité, vous pourrez solidifier vos bases avec la leçon de Lincoln[^8].

Nous exécuterons nos requêtes SPARQL sur les données [DBpedia](https://perma.cc/98MF-XF57). Il s’agit d’un très grand jeu de données dérivé de Wikipédia. En plus de contenir une foule d’informations difficiles à trouver en utilisant l’interface normale de Wikipédia, il possède plusieurs [points d’accès](https://perma.cc/XD9P-6TN7) SPARQL ― des interfaces où vous pouvez envoyer des requêtes SPARQL et obtenir les triplets correspondants de l’entrepôt DBpedia.

Le point d’accès SPARQL que nous utiliserons nous permettra d’atteindre les données [publiées et hébergées sur la plateforme TriplyDB](https://triplydb.com/DBpedia-association/dbpedia/sparql) par DBpedia. Cette plateforme offre l’avantage de fournir une [interface conviviale basée sur YASGUI](https://docs.triply.cc/triply-db-getting-started/viewing-data/#sparql-ide), un éditeur de requêtes SPARQL publié en tant que logiciel libre.

<div class="alert alert-info">
Les données du point d’accès de la plateforme TriplyDB ne font pas l’objet d’une mise à jour régulière, mais offrent l’avantage d’une plus grande stabilité, utile aux fins de la présente démonstration. Il serait également tout à fait possible d’exécuter les requêtes suivantes directement sur le <a href='https://dbpedia.org/sparql'>point d’accès de DBpedia</a>, bien que les données qui s’y trouvent sont plus dynamiques, et son interface de requête moins conviviale.
</div>

Si vous accédez à l’URL de l’[interface de requête sur TriplyDB](https://triplydb.com/DBpedia-association/dbpedia/sparql), vous remarquerez d’abord que l’éditeur propose une requête par défaut&nbsp;:

{% include figure.html filename="fr-tr-intro-aux-donnees-liees-03.png" alt="Interface de requête sur la plateforme TriplyDB, permettant d’effectuer des requêtes SPARQL sur le jeu de données de DBpedia hébergé sur cette plateforme. L’interface présente par défaut une requête SPARQL générique." caption="Figure&nbsp;3. Interface de requête sur la plateforme TriplyDB, avec une requête par défaut." %}

Si vous avez déjà écrit une requête avec le langage de requête structuré (*Structured Query Language*, en anglais, mieux connu comme [SQL](https://perma.cc/3BWP-XW94)), cela devrait vous sembler assez familier et pourra vous aider à apprendre SPARQL. Dans le cas contraire, ne vous inquiétez pas.

Les mots-clés utilisés, `select` et `where`, ne sont pas [sensibles à la casse des caractères](https://perma.cc/Z2D9-T3HZ), mais certaines parties de la requête SPARQL peuvent l’être (comme indiqué plus bas). Je vous recommande donc de vous en tenir à la casse proposée dans les exemples de cette leçon.

`select` signifie *affiche quelque chose* et `*` signifie *montre-moi tout* (autrement dit&nbsp;: affiche tout). `where` présente une condition et c’est là que nous détaillerons le genre de choses que nous voulons obtenir de notre requête.

Commençons par un exemple simple afin de voir comment cela fonctionne. Saisissez ceci dans l’éditeur de requête (idéalement sans effectuer de copier-coller)&nbsp;:

```sparql
select * where {
  dbr:Lyndal_Roper ?b ?c
}
```

Notez qu’aussitôt saisi le préfixe `dbr:`, l’interface ajoutera automatiquement la déclaration du préfixe à la première ligne de la requête, ce qui est très pratique. La requête complète est donc celle-ci&nbsp;:

```sparql
prefix dbr: <http://dbpedia.org/resource/>
select * where {
  dbr:Lyndal_Roper ?b ?c
}
```

Pour exécuter la requête, appuyez sur le bouton _Execute query_, situé en haut à droite de l’éditeur, ou effectuez _Ctrl_ + _Entrée_[^5].

Vous devriez obtenir deux colonnes avec les en-têtes **b** et **c**.
Notez bien ici que la casse des caractères fait une différence&nbsp;: `dbr:lyndal_roper` ne renverra rien.

{% include figure.html filename="fr-tr-intro-aux-donnees-liees-04.png" alt="Extrait d’un tableau des résultats d’une requête SPARQL dont chaque ligne renvoie une correspondance avec le modèle de triplet exprimé dans la requête, en affichant deux colonnes correspondant respectivement aux variables b et c dans la requête." caption="Figure&nbsp;4. Extrait des résultats d’une requête qui vise à lister tous les triplets ayant &laquo;&nbsp;Lyndal_Roper&nbsp;&raquo; comme sujet." %}

Que s’est-il donc passé&nbsp;? Et comment savoir ce qu’il faut saisir&nbsp;?

À vrai dire, je ne le savais pas vraiment&nbsp;: c’est une difficulté des points d’accès SPARQL. Lorsque vous apprenez à connaître un jeu de données, vous devez essayer de trouver quels sont les termes utilisés par le modèle. Puisque ces données proviennent de Wikipédia et que je souhaitais obtenir de l’information sur des historiennes, j’ai consulté l’article de Wikipédia sur Lyndal Roper, accessible à cette adresse&nbsp;: [https://fr.wikipedia.org/wiki/Lyndal_Roper](https://perma.cc/76QP-ZRX7).

La partie finale de l’URL est `Lyndal_Roper` et j’ai conclu que cette chaîne de caractères était probablement la façon dont DBpedia se réfère à l’article. Parce que je n’en sais pas plus sur ce qui pourrait se trouver dans les triplets qui mentionnent Roper, j’utilise `?b` et `?c`&nbsp;:
ce ne sont que des éléments de substitution. J’aurais tout aussi bien pu saisir `?peu_importe` et `?comme_vous_voulez` pour que les en-têtes de colonnes aient ces valeurs. Lorsque vous aurez besoin de plus de précision pour vos résultats, il sera important de nommer vos colonnes adéquatement.

Essayez maintenant votre propre requête SPARQL&nbsp;: choisissez un article de Wikipédia et copiez la partie finale de l’URL, celle qui se trouve après la dernière barre oblique, puis collez-la à la place de`Lyndal_Roper` dans l’éditeur, puis exécutez la requête.

À partir des informations disponibles dans ces résultats, il est possible de préparer des requêtes plus précises. Il faut procéder par essais et erreurs, alors ne vous inquiétez pas si certaines ne fonctionnent pas.

Revenons aux résultats de la requête que j’ai exécutée plus tôt&nbsp;:

```sparql
select * where {
  dbr:Lyndal_Roper ?b ?c
}
```

Je peux voir une longue liste de valeurs dans la colonne **c**. Ce sont tous des attributs de Roper dans DBpedia et ils nous aideront à trouver d’autres personnes avec ces attributs. Par exemple, j’y trouve l’URI préfixé `dbr:Historian`. Pourrais-je l’utiliser pour obtenir une liste constituée d’historiens et d’historiennes&nbsp;? Je vais l’insérer dans ma requête, mais à la troisième position, puisque c’est là où je l’ai trouvé dans mes résultats sur Lyndal Roper. 

Voici donc l’allure de ma requête&nbsp;:

```sparql
prefix dbr: <http://dbpedia.org/resource/>
select * where {
  ?historian ?predicate dbr:Historian
}
```

J’ai fait ici un petit changement. Si seulement cette requête fonctionne, je m’attends à ce que les historiennes et historiens soient dans la première colonne, parce que _historian_ ne semble pas être un prédicat&nbsp;: il ne fonctionne pas comme un verbe dans une phrase&nbsp;; donc j’appellerai ma première colonne **historian** et ma seconde, sur laquelle je ne sais pas grand-chose, **predicate**.

Exécutez la requête. Cela fonctionne-t-il pour vous&nbsp;? J’obtiens une longue liste d’historiennes et d’historiens.

{% include figure.html filename="fr-tr-intro-aux-donnees-liees-05.png" alt="Extrait d’un tableau des résultats d’une requête SPARQL dont chaque ligne renvoie une correspondance avec le modèle de triplet exprimé dans la requête, en affichant deux colonnes correspondant respectivement aux variables 'historian' et 'predicate'." caption="Figure&nbsp;5. Historiennes et historiens selon DBpedia." %}

Ainsi, cela fonctionne pour créer des listes, ce qui est utile, mais il serait beaucoup plus intéressant de combiner des listes afin de créer des intersections entre différents ensembles. J’ai trouvé quelques éléments supplémentaires dans les attributs de Lyndal Roper qu’il pourrait être intéressant de chercher sur DBpedia&nbsp;: `dbr:Category:Australian_historians` and `dbr:Category:Australian_women_historians`. Il est très facile de combiner ces attributs en demandant l’affichage d’une variable (dans notre cas`?historienne`), puis de l’utiliser dans de multiples lignes d’une requête. Notez également l’espace suivie du point final de la première ligne commençant avec `?historienne`&nbsp;:

```sparql
prefix dbr: <http://dbpedia.org/resource/>
select ?historienne where {
  ?historienne ?b dbr:Category:Australian_historians .
  ?historienne ?b dbr:Category:Australian_women_historians
}
```

Ça fonctionne&nbsp;! J’obtiens six entrées. Au moment d’écrire cette leçon, il y a six historiennes australiennes, répertoriées au sein de ce jeu de données, qui sont catégorisées à la fois comme spécialiste en histoire d’origine australienne et comme femme australienne spécialiste en histoire.

{% include figure.html filename="fr-tr-intro-aux-donnees-liees-06.png" alt="Liste des historiennes australiennes présentes dans les données de DBpedia sur TriplyDB, apparaissant sous le champ de saisie dans lequel on peut y lire la requête correspondant aux résultats de la liste." caption="Figure&nbsp;6. Liste des historiennes australiennes répertoriées dans le jeu de données." %}

Seulement six historiennes&nbsp;? Bien sûr, en réalité, il y en a bien davantage, comme nous pourrions facilement le constater en remplaçant le nom de Lyndal Roper par Cassandra Pybus dans notre première requête. Voilà qui nous mène au problème que j’ai mentionné plus tôt avec Dbpedia&nbsp;: cet entrepôt n’est pas vraiment constant quant à l’information structurelle sur les types de personnes qu’il utilise. Nos requêtes permettent de lister quelques historiennes britanniques, mais tout indique qu’il est impossible de générer une liste exhaustive de personnes dans cette catégorie. Tout ce que nous avons trouvé, ce sont les personnes qui ont une entrée sur Wikipédia en anglais et qui ont été catégorisées comme &laquo;&nbsp;historienne australienne&nbsp;&raquo;. Cela exclut par exemple les femmes australiennes spécialistes en histoire qui ne sont pas également catégorisées comme spécialiste en histoire d’origine australienne, puisque notre dernière requête renvoie l’intersection des deux ensembles.

En utilisant SPARQL sur DBpedia, vous devez faire preuve de prudence quant à certaines incohérences, car ces contenus sont alimentés par des communautés. Cela dit, vous pourriez utiliser SPARQL exactement de la même manière sur un jeu de données construit à l’aide de méthodes de curation plus rigoureuses.
Par exemple, en utilisant la bibliothèque numérique [Persée](https://data.persee.fr/explorer/sparql-endpoint/), vous pouvez vous attendre à obtenir des résultats plus robustes (voici de la documentation sur cet entrepôt&nbsp;: [https://data.persee.fr/ressources/le-triplestore-de-persee/](https://data.persee.fr/ressources/le-triplestore-de-persee/), avec son schéma de données&nbsp;: [https://data.persee.fr/explorer/schemas-de-donnees/](https://data.persee.fr/explorer/schemas-de-donnees/)).

Quoi qu’il en soit, malgré son manque de constance, DBpedia demeure un excellent choix pour apprendre SPARQL. Cette leçon ne fut qu’une brève introduction en la matière, mais il y bien plus à faire avec la leçon de Lincoln, [&laquo;&nbsp;Using SPARQL to access Linked Open Data&nbsp;&raquo;](/en/lessons/retired/graph-databases-and-SPARQL).

## Ressources et lectures complémentaires

### Ressources

- Bob DuCharme, [bobdc](https://web.archive.org/web/20260328171751/https://www.bobdc.com/blog/), blog qui vaut le détour
- John Philip McCrae, [Linked Open Data Cloud](https://lod-cloud.net), état actuel et historique du _LOD Cloud_
- Max Schmachtenberg, Christian Bizer et Heiko Paulheim, [State of the LOD Cloud 2014](https://perma.cc/5XK5-MZHW), état du _LOD Cloud_ en 2014 avec quelques statistiques intéressantes
- Matthew Lincoln, [Using SPARQL to access Linked Open Data](/en/lessons/retired/graph-databases-and-SPARQL), leçon de *Programming Historian* dédiée à SPARQL (les outils utilisés par la leçon sont obsolètes mais la démarche d’exploration proposée par Lincoln est recommandée)

### Bibliographie sommaire

- Allemang, Dean, Jim Hendler, and Fabien Gandon. *Semantic Web for the Working Ontologist: Effective Modeling for Linked Data, RDFS, and OWL*. 3<sup>e</sup> éd. New York&nbsp;: Association for Computing Machinery, ACM Books Series 33, 2020. [https://doi.org/10.1145/3382097](https://doi.org/10.1145/3382097).
- Berners-Lee, Tim. &laquo;&nbsp;Linked Data&nbsp;&raquo;. *Design Issues*, 18 juin 2009. [https://w3.org/DesignIssues/LinkedData.html](https://perma.cc/79VD-G5T4).
- DuCharme, Bob. *Learning SPARQL: Querying and Updating with SPARQL 1.1*. 2<sup>e</sup> éd. Sebastopol, CA&nbsp;: O’Reilly Media, 2013. [http://www.learningsparql.com](https://perma.cc/NXQ7-KWHJ).
- Gartner, Richard. *Metadata: Shaping Knowledge from Antiquity to the Semantic Web*. 1<sup>re</sup> éd. Cham&nbsp;: Springer, 2016. [https://doi.org/10.1007/978-3-319-40893-4](https://doi.org/10.1007/978-3-319-40893-4).
- Nurmikko-Fuller, Terhi. *Linked Data for Digital Humanities*. 1<sup>re</sup> éd. London&nbsp;: Routledge, 2023. [https://doi.org/10.4324/9781003197898](https://doi.org/10.4324/9781003197898).
- Oldman, Dominic, Martin Doerr, and Stefan Gradmann. &laquo;&nbsp;Zen and the Art of Linked Data&nbsp;&raquo;. In *A New Companion to Digital Humanities*, edited by Susan Schreibman, Ray Siemens, and John Unsworth, 251–73. Chichester&nbsp;: John Wiley & Sons, 2016. [https://doi.org/10.1002/9781118680605.ch18](https://doi.org/10.1002/9781118680605.ch18).
- Van Hooland, Seth, and Ruben Verborgh. *Linked Data for Libraries, Archives and Museums: How to Clean, Link and Publish Your Metadata*. London&nbsp;: Facet Publishing, 2015. [https://doi.org/10.29085/9781783300389](https://doi.org/10.29085/9781783300389).
- Wood, David, Marsha Zaidman, Luke Ruth, and Michael Hausenblas. *Linked Data: Structured Data on the Web*. Manning Publications, 2013. [https://www.manning.com/books/linked-data](https://perma.cc/23DL-M6WU).

## Remerciements

J’aimerais remercier Matthew Lincoln et Terhi Nurmikko-Fuller pour leurs relectures, ainsi que mon éditeur Adam Crymble, qui ont généreusement offert de leur temps pour m’aider à améliorer ce cours, grâce à de nombreuses suggestions, clarifications et corrections. Cette leçon est basée sur une autre leçon rédigée dans le cadre du [projet Tobias](https://perma.cc/6GUX-Q5U9) (*Thesaurus of British and Irish History as SKOS*, 2015-2016), qui fut financé par l’[AHRC](https://perma.cc/XPF5-J8TP). Elle a été révisée pour *Programming Historian*.

## Notes de fin

[^3]: On rencontre couramment le sigle anglais LOD dans la littérature scientifique francophone, mais nous nous conformerons à sa version française DOL afin de refléter adéquatement la formule &laquo;&nbsp;données ouvertes liées&nbsp;&raquo;.

[^1]: Note de traduction&nbsp;: une des retombées intéressantes de ce projet encore accessible aujourd’hui se trouve dans la plateforme [lipad.ca](https://lipad.ca) pour l’exploration et l’interrogation des données parlementaires canadiennes.

[^2]: Les applications web présentent souvent les numéros de téléphone sous la forme d’un URI qui rencontre les critères de la spécification [RFC 3986](https://perma.cc/3NG5-CY44), *Uniform Resource Identifier (URI): Generic Syntax*. Par exemple, l’URI tel:+1-816-555-1212 utilise un protocole (tel:) et un chemin (+1-816-555-1212) permettant d’exécuter une application téléphonique pour joindre l’entité identifiée, tout comme un URI utilisant le protocole HTTP permet d’accéder, s’il est déréférençable, à une description de la ressource identifiée dans un navigateur web.

[^4]: De pair avec DBpedia, [Wikidata](https://www.wikidata.org) est également un incontournable des jeux de données ouvertes liées. En plus d’appliquer les principes du [wiki](https://perma.cc/445G-5BA4) aux données, il revêt aujourd’hui une importance particulière dans les écosystèmes d’information web&nbsp;: comme VIAF (dont les notices sont liées à Wikidata), il peut faire figure de fichier d’autorité.

[^5]: Veuillez noter que l’exécution des requêtes peut mettre un certain temps à aboutir. Si le délai d’attente est dépassé (il s’agit typiquement d’un *timeout*), il suffit de réessayer quelques minutes plus tard.

[^6]: Le modèle RDF 1.1 repose sur l’utilisation des [identifiants internationalisés de ressource](https://perma.cc/LP3E-R5F4) (*Internationalized Resource Identifier*, ou IRI en anglais) pour l’identification des entités. Dans cette leçon, il n’est question que d’URI et d’URL, car ce sont des formes d’IRI couramment utilisés pour l’échange d’information sur le web. Les IRI ont la particularité de permettre l’utilisation des caractères [Unicode](https://perma.cc/Z42F-JFXL), mais il est généralement déconseillé d’utiliser ces caractères directement dans les URI ou les URL pour des enjeux de compatibilité. Les exemples qui suivent utilisent des caractères accentués pour favoriser la lisibilité.

[^7]: Dans les paragraphes qui suivent, les attributs utilisent des termes français pour exemplifier les propos de la leçon. Cependant, les noms d’attribut sont en pratique généralement formulés en anglais.

[^8]: Rappel&nbsp;: la leçon de Matthew Lincoln n’est plus à jour et n’est plus entretenue par le _Programming Historian_.
