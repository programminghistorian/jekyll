---
title: Préserver ses données de recherche
layout: lesson
slug: preserver-ses-donnees-de-recherche
date: 2014-04-30
translation_date: 2020-01-16
authors:
- James Baker
reviewers:
- Jane Winters
- Sharon Howard
- William J. Turkel
editors:
- Adam Crymble
translator:
- Anne-Sophie Bessero-Lagarde
translation-editor:
- François Dominic Laramée
translation-reviewer:
- Sofia Papastamkou
- Martin Grandjean
original: preserving-your-research-data
difficulty: 1
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/263
activity: sustaining
topics: [data-management]
abstract: Cette leçon donne des pistes aux historiens et aux historiennes pour documenter, structurer et pérenniser leurs données de recherche.
avatar_alt: Un gros baril
original: preserving-your-research-data
doi: 10.46430/phfr0009
---

{% include toc.html %}





#### Contexte

Dans son essai de 2003 "Scarcity or Abundance" Roy Rosenzweig cherchait à alerter les historiens et les historiennes sur ce qu'il a appelé "la fragilité de l'administration de la preuve à l'ère numérique" (Rosenzweig, 736). Et bien que ses préoccupations se concentrent sur les sources disponibles sur le web ouvert, elles peuvent facilement être étendues aux matériaux nativement numériques - ou données - que les historiens et historiennes créent durant leurs recherches.

C'est à ces données de la recherche que cette leçon va se consacrer. Mais pourquoi ?

De plus en plus, les historiens et les historiennes utilisent leurs ordinateurs comme moyen de stockage par défaut de toutes leurs données de recherche, leurs matériaux. Leurs manuscrits sont devenus des objets numériques depuis un certain temps et leurs recherches s'adaptent en conséquence, que ce soit dans le format de notes dactylographiées, de photographies d'archives, ou de données tabulées. De plus, la conservation des données de la recherche dans un format numérique a clairement des avantages par rapport au précédent format physique : elles peuvent être parcourues et fouillées, hébergées d'une façon qui permette un accès depuis de nombreux endroits, fusionnées ou croisées avec d'autres données de la recherche.

Le simple fait de mettre ses données de la recherche dans un format numérique ne garantit pas qu'elles survivent. Ici je n'entends pas survie au sens littéral ni d'être lisible par la prochaine version de Microsoft Word, mais plutôt dans le sens d'utilisable par des personnes. Car, si ce n'est certes pas un problème résolu, la manière de préserver les données de la recherche pour le futur est une problématique dont des solutions potentielles ont déjà été longuement discutées, en pensant ou non aux historien(ne)s. En outre des experts en gestion de données, tout comme des services et d'autres acteurs concernés, ont exposé des bonnes pratiques académiques pour les documenter, structurer et organiser. Malgré cela, les données de la recherche individuellement produites par les historien(ne)s sont sujettes à un risque de perte, s'ils et elles ne sont pas capables de les générer et de les préserver dans un format compréhensible qui garde du sens des années, voire des décennies plus tard ; sans parler de ceux et celles qui pataugeront dans les idiosyncrasies de leur processus de recherche. En bref, il y a un risque de perte dès lors que les données sont détachées de leur contexte de création, des connaissances tacites qui les ont rendues utiles pour la préparation du discours X ou du manuscrit Y. Comme William Stafford Noble le dit :

> Le principe de base est simple: quelqu'un non familiarisé avec votre
> projet devrait être capable de consulter vos fichiers informatiques et de comprendre
> en détails ce que vous avez fait et pourquoi […] Cependant, le plus souvent ce
> « quelqu'un » c'est vous. Dans quelques mois, vous ne vous souviendrez peut-être plus
> de ce que vous faisiez lorsque vous avez créé un ensemble particulier de fichiers, ou des
> conclusions que vous avez tirées. Vous devrez alors passer
> du temps à reconstruire vos expériences précédentes ou perdre toutes
> les connaissances que vous aviez acquises de ces expériences.
>
> William Stafford Noble (2009) A Quick Guide to Organizing
> Computational Biology Projects. PLoSComputBiol 5(7): e1000424.
> doi:10.1371/journal.pcbi.1000424

S'appuyant sur les leçons et l'expertise de professionnels en données de la recherche, ce guide suggère aux historiennes et aux historiens des moyens de documenter et de structurer leurs propres données de manière à ce qu'elles restent utilisables dans le futur. Il ne se veut pas normatif mais suppose que les lecteurs et lectrices itéreront, changeront et adapteront les idées présentées pour correspondre au mieux à leurs recherches.

* * * * *

#### Documentation des données de la recherche

> Birkwood, Katie (girlinthe).
>“Victory is mine: while ago I worked out some Clever Stuff ™ in Excel. And I MADE NOTES ON IT. And those notes ENABLED ME TO DO IT AGAIN.” 7 October 2013, 3:46 a.m.. Tweet.
>
>“La victoire est mienne : il y a quelques temps, j'ai travaillé
> sur Des Trucs Brillants ™ dans Excel. Et J'AI PRIS DES NOTES DESSUS. Et ces notes
> M'ONT PERMIS DE LE REFAIRE.” 7 octobre 2013, 3:46 a.m.. Tweet.
>
> <https://twitter.com/Girlinthe/status/387166944094199809>

L'intérêt de la documentation est de saisir le processus de création des données, les modifications qui peuvent être apportées à celles-ci et les connaissances tacites qui leur sont associées. Des méthodologies de gestion de projet, comme [PRINCE2][], accordent une grande importance à une documentation précise, structurée et détaillée. Bien que cette approche présente des avantages, particulièrement pour les grands projets, complexes et multipartenaires, le travail de l'historien(ne) moyen(ne) est plus susceptible de tirer des bénéfices d'une approche flexible et sur mesure d'une documentation qui s'appuiera sur les principes de la gestion de projet. Dans le cas de la recherche historique, le type de documentation qui pourrait être produit pour préserver l’utilité des données de recherche comprend:
- une documentation décrivant les notes prises lors de la consultation d'un document d'archives, comme la référence archivistique de l'original, la représentativité des notes (par exemple: transcription complète, transcription partielle ou résumé), la degré d'exhaustivité de l'étude du document, ou en revanche les décisions prises d'exclure certaines sections du document du processus de recherche;
- une documentation décrivant les données tabulées, comme la façon dont elles ont été générées (par exemple, manuellement ou de manière automatisée), les références archivistiques des sources dont les données ont été extraites, ou les attributs des sources d'origine conservés (et pourquoi);
- une documentation décrivant le répertoire des images numériques, comme la façon dont chaque image a été créée, où elle a été téléchargée et les notes de recherche qui s'y rapportent.

Comme le dernier exemple le suggère, l'un des principaux objectifs de la documentation est de décrire les liens significatifs qui existent entre les données de la recherche, liens dont on risque de perdre le sens au fil du temps.

Le moment de la documentation dépend beaucoup de l'individu et du rythme de ses recherches. La règle principale est de prendre l'habitude de rédiger et de mettre à jour la documentation à intervalles réguliers, idéalement chaque fois qu'une partie du travail est terminée pour la matinée, l'après-midi ou la journée. En même temps, il est important de ne pas s’inquiéter de la perfection, mais plutôt de chercher à rédiger une documentation cohérente et efficace qui vous sera utile et, espérons-le, qui le sera aussi à une autre personne utilisant vos données de recherche, des années plus tard.

* * * * *

#### Formats des fichiers

Les données de la recherche et la documentation devraient dans l'idéal être sauvegardées dans des formats ouverts, qui sont [compatibles avec tous les systèmes d'exploitation][], comme .txt pour les notes et .csv (comma-separated values) ou .tsv (tab-seperated values) pour les données tabulées. Ces formats texte brut sont préférables aux formats propriétaires utilisés par défaut avec Microsoft Office ou iWork parce qu'ils peuvent être ouverts avec de nombreux logiciels et ont une forte chance de rester lisibles et modifiables dans le futur. La plupart des suites bureautiques standards incluent une option permettant de sauvegarder les fichiers dans les formats .txt, .csv et .tsv, ce qui signifie que vous pouvez continuer à travailler avec vos logiciels habituels tout en faisant ce qu'il faut pour préserver votre travail. Comparés à du .doc ou du .xls, ces formats ont en plus l'atout, dans une perspective de préservation, de ne contenir que des éléments lisibles par la machine. Bien que l'utilisation des caractères gras, italiques ou colorés pour signifier des titres ou établir des connections visuelles entre des données soit une pratique courante, ces annotations servent à l'affichage sans être lisibles par les machines et ne peuvent pas être interrogées ni fouillées. Elles ne sont pas non plus appropriées pour les grandes quantités d'informations. Il est préférable d'utiliser des schémas de notations simples comme des doubles astérisques ou des triples croisillons pour représenter des caractéristiques: dans mes notes, par exemple, trois points d'interrogations indiquent un point que je dois suivre, j'ai choisi "???' car cette suite peut être facilement trouvée avec une recherche CTRL+F.

Dans de nombreuses occasions, il est probable que ces schémas de notation émergent de la pratique individuelle (et doivent par conséquent être documentés), alors qu'il existe des schémas comme le [Markdown][] de [GitHub](https://github.com) (les fichiers Markdown sont enregistrés au format .md). Un excellent aide-mémoire au Markdown est disponible sur [GitHub](https://github.com/adam-p/markdown-here) pour ceux qui veulent suivre - ou adapter - le schéma existant. [Notepad++](http://notepad-plus-plus.org) est recommandé pour les utilisateurs de Windows, bien que nullement essentiel pour travailler avec des fichiers .md. Les utilisateurs de Mac ou d'Unix peuvent utiliser [Komodo Edit](https://www.activestate.com/products/komodo-edit/) ou [Text Wrangler](https://www.barebones.com/support/textwrangler/updates.html).

* * * * *

#### Récapitulatif 1

Pour résumer, les points clés sur les formats de documentation et de fichiers sont les suivants :

-   Tentez de documenter pour saisir de manière précise et cohérente les connaissances tacites relatives au processus de recherche, qu’il s’agisse de la prise de notes, de la génération de données sous forme de tableaux ou de la collecte de sources visuelles.
-   Privilégiez une documentation simple en utilisant des formats de fichiers et des pratiques de notation compatibles avec tous les systèmes d'exploitation et lisibles par machine.
-   Prévoyez du temps pour mettre à jour et créer de la documentation dans votre flux de travail sans que cela ne devienne un fardeau.
-   Investissez maintenant pour laisser des traces écrites, cela vous économisera le temps que vous risquez de perdre dans l'avenir en essayent de reconstituer ce cheminement.

* * * * *

#### Structurer les données de la recherche

Il est plus facile de documenter votre recherche en structurant vos données de recherche de manière cohérente et intuitive.

Pourquoi ?

Pour naviguer dans les données (physiques et numériques) que contient une bibliothèque ou un centre d'archives, nous nous appuyons sur les informations structurées de leurs catalogues et inventaires. Sans cette information structurée, notre recherche serait beaucoup plus pauvre.

L'examen des URL est un bon moyen de réfléchir à la raison pour laquelle la structuration cohérente et intuitive des données peut s'avérer utile dans votre recherche. Pour être reproductibles et citées dans un contexte scientifique, les URL doivent représenter avec clarté le contenu de la page qu'ils identifient, soit en contenant des éléments sémantiques, soit en utilisant un seul élément de données trouvé sur un ensemble ou la majorité des pages.

Les URL utilisés par les sites d’informations ou les blogues en sont un exemple typique. Les URL Wordpress suivent le format suivant :

-   *nom du site Web*/*année (4 chiffres)*/*mois (2 chiffres)*/*jour (2 chiffres)*/*mots du titre séparés par des traits d'union*
-   <http://cradledincaricature.com/2014/02/06/comic-art-beyond-the-print-shop/>

Un usage similaire est utilisé par les agences de presse telles que le journal *The Guardian* :

-   *nom du site Web*/*section de section*/*année (4 chiffres)*/*mois (3 caractères)*/*jour (2 chiffres)*/*mots-descripteurs-contenus-séparés-par-tirets*
-   <http://www.theguardian.com/uk-news/2014/feb/20/rebekah-brooks-rupert-murdoch-phone-hacking-trial>

De leur côté, les catalogues d’archives utilisent souvent des URL structurées avec un seul élément de données. La British Cartoon Archive structure ses archives en ligne en utilisant le format :

-   *nom du site*/record/*numéro de référence*
-   <http://www.cartoons.ac.uk/record/SBD0931>

Et l'Old Bailey (la Haute Cour criminelle britannique) utilise le format :

-   *nom du site*/browse.jsp?ref=*numéro de référence*
-   <http://www.oldbaileyonline.org/browse.jsp?ref=OA16780417>

Ce que nous apprenons de ces exemples, c’est qu’une combinaison de description parlante et d’éléments de données rend les structures de données cohérentes et intuitives, lisibles à la fois par les humains et par les machines. Appliqué aux données numériques accumulées au cours de recherches historiques, cela facilite la navigation, la recherche et l'interrogation des données de recherche à l'aide des outils standard fournis par nos systèmes d'exploitation (et, comme nous le verrons dans une prochaine leçon, d'outils plus perfectionnés).

En pratique (pour les utilisateurs d'OS X et de Linux, remplacez les antislashs par des slashs), la structure d'un bon archivage des données de la recherche devrait ressembler à ceci :

Un répertoire de base ou racine qui pourrait s'appeler "travail".

```
\travail\
```

Une série de sous-répertoires.

```
     \travail\evenements\
     \recherche\
     \enseignement\
     \publication\
```

Ces répertoires contiennent des séries de dossiers pour chaque événement, projet de recherche, module ou document écrit. L'introduction d'une convention de nommage incluant des éléments de date permet de conserver les informations organisées sans avoir besoin de sous-répertoires par année ou par mois.

```
\travail\recherche\2014-01_Journal_Articles
              \2014-02_Infrastructure
```

Enfin, d'autres sous-répertoires peuvent être utilisés pour séparer les informations à mesure que le projet se développe.

```
\travail\recherche\2014_Journal_Articles\analyse
                                    \donnees
                                    \notes
```

Bien évidemment, toutes les informations ne s'intègreront pas parfaitement dans une structure donnée et, à mesure que de nouveaux projets apparaissent, la classification devra être réexaminée. D'une manière ou d'une autre, l'idiosyncrasie est acceptable tant que la structure globale du répertoire est cohérente et intuitive, et que tout ce qui ne l’est pas est clairement documenté: par exemple, le sous-répertoire "écriture" de la structure ci-dessus peut inclure un fichier .txt indiquant ce qu’il contient (brouillons et version finale du travail écrit) et ce qu’il ne contient pas (recherche concernant ce travail écrit).

Le nommage de ce fichier .txt, de même que de toute documentation et de toutes les données de recherche, est important pour garantir sa lisibilité et son contenu. "Notes sur ce dossier.docx" n'est pas un nom qui remplit cet objectif, alors que "2014-01-31\_Publication\_Lisez-moi.txt" avec une réplique du titre du répertoire et quelques éléments de dates parvient à le faire. Les lecteurs nord-américains remarqueront que j'ai choisi la structure année\_mois\_jour. Un exemple de [fichier Lisez-moi que j'ai rédigé pour un projet](/assets/preserving-your-research-data/network_analysis_of_Isaac_Cruikshank_and_his_publishers_readme.txt) contient le type d'information dont vous et les autres utilisateurs de vos données pourriez avoir besoin.

Un retour d'expérience devrait être suffisant pour confirmer l'intérêt de cette approche. Au cours d'un projet de recherche précédent, j'ai rassemblé quelque 2 000 images numériques d'empreintes satiriques georgiennes provenant de plusieurs sources en ligne, en conservant les noms de fichier lors du téléchargement. Si j’avais appliqué dès le départ une convention de nommage (par exemple, «ANNEE DE PUBLICATION \_NOM DE L'ARTISTE\_TITRE DE L'OEUVRE.FORMAT»), je serais en mesure de rechercher et d’interroger ces images. En effet, commencer les noms de chaque fichier avec AAAAMMDD aurait permis que les fichiers puissent être triés par ordre chronologique sous Windows, OS X et Linux. Et s'assurer que tous les espaces, signes de ponctuation et caractères accentués (sauf les tirets, les points et les traits de soulignement) soient absents des noms de fichiers afin de les rendre cohérents et intuitis aurait permis de faire fonctionner la ligne de commande avec les fichiers. Mais je ne l’ai pas fait et, dans l’état actuel des choses, j’aurais besoin de beaucoup de temps pour modifier chaque nom de fichier individuellement afin de rendre les données utilisables de cette manière. <!--Il existe l'outil Vrenamer lorsqu'on est dans cette situation https://vrenamer.com/ -->

En outre, l'application de telles conventions de nommage à toutes les données de recherche de manière cohérente et intuitive facilite la lisibilité et la compréhension de la structure de données. Par exemple, pour un projet sur des articles de revues, nous pourrions choisir le répertoire…

```
\travail\recherche\2014-01_Journal_Articles\
```

… Où les éléments année-mois indiquent la date de début du projet.

Dans ce répertoire, nous incluons un répertoire \\donnees\\ où sont conservées les données d'origine utilisées dans le projet.

```
2014-01-31_Journal_Articles.tsv
```

En plus des données, on y trouve la documentation qui décrit 2014-01-31\_Journal\_Articles.tsv.

```
2014-01-31_Journal_Articles_notes.txt
```

Au niveau du répertoire \\2014-01\_Journal\_Articles\\ nous créons un dossier \\analyse\\ dans lequel on place \:

```
2014-02-02_Journal_Articles_analyse.txt
2014-02-15_Journal_Articles_analyse.txt
```

Notez les différences de mois et de date ici. Celles-ci reflètent les dates auxquelles l'analyse des données a eu lieu, cette convention est décrite brièvement dans 2014-02-02\_Journal\_Articles\_analyse\_lisez-moi.txt.

Enfin, un répertoire dans \\donnees\\ appelé \\donnees_derivees\\ contient les données dérivées du fichier original 2014-01-31\_Journal\_Articles.tsv. Dans ce cas, chaque fichier .tsv dérivé contient des lignes comprenant les mots-clés "afrique", "amérique", "art", etc., et porte le nom correspondant.

```
2014-01-31_Journal_Articles_MC_afrique.tsv

2014-01-31_Journal_Articles_MC_amerique.tsv

2014-02-01_Journal_Articles_MC_art .tsv

2014-02-02_Journal_Articles_MC_britannique.tsv
```

* * * * *

#### Récapitulatif 2

Pour récapituler, les points clés de la structuration des données de recherche sont les suivants :

-   Les structures de données doivent être cohérentes et intuitives.
-   Pensez à utiliser des éléments parlants ou des identifiants de données pour structurer les répertoires de données de recherche.
-   Ajustez et adaptez la structure des données à votre recherche.
-   Appliquez des conventions de nommage aux répertoires et aux noms de fichiers pour les identifier, créer des associations entre des éléments de données et contribuer à la lisibilité et à la compréhension à long terme de la structure de vos données.


* * * * *

#### Résumé

Cette leçon a suggéré des façons de documenter et de structurer les données de recherche afin de garantir leur conservation en capturant les connaissances tacites acquises au cours du processus de recherche et en facilitant ainsi l'utilisation future des informations. Elle a recommandé l'utilisation de formats libres et lisibles par machine pour la documentation et les données de recherche. Elle a suggéré que les URL offrent un exemple pratique de structures de données bonnes et mauvaises pouvant être répliquées aux fins des données de recherche des historiens et des historiennes.

Ces suggestions ne font qu'offrir quelques pistes que les chercheurs et les chercheuses devront adapter à leurs objectifs. Ce faisant, il est recommandé de garder à l’esprit les stratégies de préservation numérique et les bonnes pratiques de gestion de projet, tout en veillant à ce que le temps consacré à documenter et à structurer la recherche ne devienne pas un fardeau. Après tout, le but de ce guide est de faciliter et non de rendre moins efficace les recherches historiques qui génèrent des données. Au final, c'est votre recherche à vous.

* * * * *

#### Lectures complémentaires

Ashton, Neil, 'Seven deadly sins of data publication', School of Data
blog (17 octobre 2013)
<http://schoolofdata.org/2013/10/17/seven-deadly-sins-of-data-publication/>

Hitchcock, Tim, 'Judging a book by its URLs', Historyonics blog (3
janvier 2014)
<http://historyonics.blogspot.co.uk/2014/01/judging-book-by-its-url.html>

Howard, Sharon, 'Unclean, unclean! What historians can do about sharing
our messy research data', Early Modern Notes blog (18 mai 2013)
<http://earlymodernnotes.wordpress.com/2013/05/18/unclean-unclean-what-historians-can-do-about-sharing-our-messy-research-data/>

Noble, William Stafford, A Quick Guide to Organizing Computational
Biology Projects.PLoSComputBiol 5(7): e1000424 (2009)
<https://doi.org/10.1371/journal.pcbi.1000424>

Oxford University Computing Services, 'Sudamih Project. Research
Information Management: Organising Humanities Material' (2011)
<https://zenodo.org/record/28329>

Pennock, Maureen, 'The Twelve Principles of Digital Preservation (and a
cartridge in a repository…)', British Library Collection Care blog (3
septembre 2013)
<http://britishlibrary.typepad.co.uk/collectioncare/2013/09/the-twelve-principles-of-digital-preservation.html>

Pritchard, Adam, 'Markdown Cheatsheet' (2013)
<https://github.com/adam-p/markdown-here>

Rosenzweig, Roy, 'Scarcity or Abundance? Preserving the Past in a
Digital Era', The American Historical Review 108:3 (2003), 735-762.

UK Data Archive, 'Documenting your Data'
<http://data-archive.ac.uk/create-manage/document>

  [PRINCE2]: https://fr.wikipedia.org/wiki/PRINCE2
  [compatibles avec tous les systèmes d'exploitation]: https://fr.wikipedia.org/wiki/Logiciel_multiplateforme
  [Markdown]: https://fr.wikipedia.org/wiki/Markdown
  [GitHub] : https://github.com/adam-p/markdown-here
  [Notepad++] : http://notepad-plus-plus.org/fr/
  [Komodo Edit]: https://www.activestate.com/products/komodo-edit/
  [Text Wrangler]: https://www.barebones.com/support/textwrangler/updates.html
