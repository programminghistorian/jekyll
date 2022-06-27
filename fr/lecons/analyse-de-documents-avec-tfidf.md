---
title: "Analyse de documents avec TF-IDF"
collection: lessons
layout: lesson
slug: analyse-de-documents-avec-tfidf
date: 2019-05-13
authors:
- Matthew J. Lavin
reviewers:
- Quinn Dombrowski
- Catherine Nygren
editors:
- Zoe LeBlanc
translation_date: 2022-06-27 
translator:
- François Dominic Laramée
translation-editor:
- Célian Ringwald
translation-reviewer:
- Amélie Daloz
- Rémi Cardon
original: analyzing-documents-with-tfidf
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/454
difficulty: 2
activity: analyzing
topics: [distant-reading]
abstract: Cette leçon présente une méthode de traitement automatique des langues et de recherche d'informations nommée Term Frequency - Inverse Document Frequency (tf-idf). Elle en expose les fondations et introduit à l'occasion des questions et des concepts liés à l'analyse de textes.
avatar_alt: Machine à écrire
mathjax: true
doi: 10.46430/phfr0022
---

{% include toc.html %}

# Aperçu

Cette leçon présente une méthode de traitement automatique des langues et de recherche d'informations nommée **tf-idf**, une appellation tirée de l'anglais _Term Frequency - Inverse Document Frequency_. Vous avez peut-être déjà entendu parler du **tf-idf** dans le contexte d'une discussion de la modélisation thématique, de l'apprentissage automatique ou d'autres méthodes d'analyse textuelle. **Tf-idf** apparaît régulièrement dans la littérature scientifique car il s'agit à la fois d'une méthode d'exploration de [corpus](https://perma.cc/G2LA-EKTH) et d'une étape de prétraitement utile pour plusieurs autres méthodes de fouille de textes et de modélisation.

En étudiant **tf-idf**, vous découvrirez une méthode d'analyse textuelle que vous pourrez appliquer immédiatement. Cette leçon vous permettra aussi de vous familiariser avec certaines des questions et certains des concepts de l'analyse textuelle assistée par ordinateur. Notamment, cette leçon explique comment isoler les mots les plus significatifs d'un document, des mots qui ont tendance à apparaître fréquemment dans de nombreux documents rédigés dans une même langue. Outre **tf-idf**, il existe de nombreuses méthodes qui permettent de déterminer les mots et les locutions spécifiques à un ensemble de documents. Je recommande fortement la lecture de ce billet de blogue de Ted Underwood[^1] en complément d'information.

# Préparation

## Connaissances préalables recommandées

- Être familiarisé(e) avec Python ou un langage de programmation similaire. Le code de cette leçon a été programmé en Python 3.6, mais vous pouvez exécuter **tf-idf** dans toutes les versions courantes de Python, en utilisant l'un des divers modules appropriés, ainsi que dans plusieurs autres langages de programmation. Le niveau de compétence en programmation requis est difficile à évaluer, mais vous devrez au moins être à l'aise avec les types de données et les opérations élémentaires. Pour tirer profit de cette leçon, il serait aussi souhaitable de suivre un cours comme celui proposé par Antoine Rozo sur [zestedesavoir.com](https://perma.cc/7WJ4-WD3P) ou d'avoir suivi certaines des [leçons d'introduction à la programmation en Python](/fr/lecons/introduction-et-installation) du _Programming Historian_. Si vous avez accès à une bibliothèque, n'hésitez pas à consulter le livre d'Émilien Schultz et de Matthias Bussonnier [*Python pour les sciences humaines et sociales*](http://www.worldcat.org/oclc/1232233436).   
- À défaut de pouvoir suivre la recommandation précédente, vous pourriez [réviser les bases de Python](https://perma.cc/YDT4-9JJ6), dont les types de données élémentaires (chaînes de caractères, nombres entiers, nombres réels, tuples, listes et dictionnaires), les variables, les boucles, les classes d'objets et leurs instances.
- La maîtrise des bases d'Excel ou d'un autre tableur pourrait être utile si vous souhaitez examiner les feuilles de calcul au format CSV liées à cette leçon de plus près. Vous pouvez aussi employer le module Pandas du langage Python pour lire ces fichiers CSV.

## Avant de commencer

- Installez la version Python 3 de l'environnement de développement Anaconda. La méthode à suivre est expliquée dans la leçon [Text Mining in Python through the HTRC Feature Reader](/en/lessons/text-mining-with-extracted-features) (en anglais). Vous obtiendrez le langage Python 3.6 (ou une version plus récente), le module [Scikit-Learn](https://scikit-learn.org/stable/install.html) (qui contient la version de **tf-idf** que nous présentons ici) et tout ce qu'il faut pour exécuter du code Python dans un [carnet Jupyter](https://jupyter.org/).
- Il est possible d'obtenir toutes les librairies nécessaires sans installer Anaconda ou en choisissant plutôt une alternative plus légère comme [Miniconda](https://docs.conda.io/en/latest/miniconda.html). Pour plus d'informations, consultez la section [&laquo;&#x202F;Alternatives à Anaconda&#x202F;&raquo;](#alternatives-à-anaconda) à la fin de cette leçon.

## Jeu de données

Pour comprendre comment fonctionne **tf-idf**, prenons un exemple. J'ai donc préparé pour vous un jeu de données formé de 366 [nécrologies](https://perma.cc/73CL-ZKL3) historiques publiées dans le _New York Times_ et moissonnées sur le site [https://archive.nytimes.com/www.nytimes.com/learning/general/onthisday/]([https://archive.nytimes.com/www.nytimes.com/learning/general/onthisday/](https://perma.cc/R2V7-UBXX)) sur lequel, à chaque jour de l'année, le _New York Times_ mettait en vedette la nécrologie d'une personne dont c'était l'anniversaire de naissance.

Les fichiers requis pour suivre la leçon, dont ce jeu de données, peuvent être téléchargés [ici](/assets/tf-idf/lecon-fichiers.zip). Le jeu de données est assez petit pour que vous puissiez ouvrir et lire au moins quelques-uns des fichiers textes. Les données moissonnées sont également disponibles à deux endroits&#x202F;: 


1. Dans le répertoire `necrologies` contenant les fichiers .html téléchargés à partir du site web «&#x202F;On This Day&#x202F;» de 2011
2. Dans le répertoire `txt` contenant des fichiers .txt.

Dans ces derniers se trouve le corps du texte de chaque nécrologie. Ces fichiers ont été générés à l'aide du [module Python](https://perma.cc/N6KK-ADEG) nommé [BeautifulSoup](https://perma.cc/2KTE-AEM3).

Ce corpus nécrologique constitue un artéfact historique en soi. Le choix éditorial des nécrologies est le reflet de choix d'inclusion et de représentation historiquement situé. Et cela a un fort impact sur le corpus. La signification de ce genre de décisions a été soulignée par le _New York Times_ lui-même en mars 2018, lorsque le journal a commencé à publier les nécrologies de &laquo;&#x202F;femmes négligées&#x202F;&raquo;.[^2] Comme l'ont souligné à ce moment Amisha Padnani et Jessica Bennett, &laquo;&#x202F;de qui l'on se souvient - et comment on le fait - dépend invariablement d'un jugement. Revoir l'archive nécrologique peut ainsi constituer une leçon brutale sur la manière dont la société évaluait certaines réalisations et les personnes qui en sont responsables&#x202F;&raquo; (traduction libre). Vu sous cet angle, le jeu de données proposé ici constitue non pas un échantillon représentatif des nécrologies historiques, mais plutôt une vitrine vers les personnes que le _New York Times_ jugeait dignes d'être mises en valeur en 2010-2011. Vous remarquerez que plusieurs des personnages historiques mentionnés sont bien connus, ce qui suggère un effort conscient de se pencher sur l'histoire du _New York Times_ pour choisir les nécrologies selon des critères particuliers.[^3]

## Définition et description de tf-idf

L'opération appelée &laquo;&#x202F;Term Frequency - Inverse Document Frequency&#x202F;&raquo; a été présentée pour la première fois, sous le nom de &laquo;&#x202F;term specificity&#x202F;&raquo; (spécificité terminologique), dans un article de Karen Spärck Jones publié en 1972.[^4] Comme il se  doit, Spärck Jones a fait l'objet d'une notice nécrologique &laquo;&#x202F;Overlooked No More&#x202F;&raquo; en janvier 2019[^5]. Plutôt que de représenter un terme par la fréquence brute de ses apparitions dans un document (c'est-à-dire son nombre d'occurrences) ou par sa fréquence relative (soit son nombre d'occurrences divisé par la longueur du document), l'importance de chaque terme est pondérée en divisant son nombre d'occurrences par le nombre de documents qui contiennent le mot dans le corpus. Cette pondération a pour effet d'éviter un problème fréquent en analyse textuelle&#x202F;: les mots les plus courants dans un document sont souvent les mots les plus courants dans _tous_ les documents. Résultat&#x202F;: les termes dont les scores **tf-idf** sont les plus élevés dans un document sont ceux qui apparaissent dans ce document particulièrement souvent par rapport à leur fréquence dans les autres documents du corpus.

Si cette explication n'est pas tout à fait claire, voici une analogie qui pourrait vous aider. Supposez que vous passez un week-end de vacances dans une ville nommée Idf. Vous désirez choisir un restaurant pour votre dîner en tenant compte de deux facteurs. Premièrement, vous voulez très bien manger. Deuxièmement, vous aimeriez essayer une cuisine locale pour laquelle la ville d'Idf est particulièrement réputée. Autrement dit&#x202F;: vous ne voulez pas vous contenter d'un plat que vous pourriez manger n'importe où. Vous pourriez passer la journée à consulter des évaluations de restaurants en ligne, ce qui serait approprié pour atteindre votre premier objectif. Mais si vous voulez aussi atteindre le second, il vous faudra un moyen de faire la différence entre ce qui est sans plus, typiquement bon ou seulement bon.

Il est assez facile, je crois, de constater que la nourriture servie dans un restaurant peut être soit&#x202F;:

1. Á la fois bonne et originale
2. Bonne mais pas très originale
3. Originale mais pas très bonne
4. Ni bonne, ni originale

On peut caractériser les fréquences d'occurrence des mots de la même façon. Un mot peut être&#x202F;:

1. Utilisé couramment dans une langue comme le français ou l'anglais et particulièrement fréquent (ou rare) dans un document spécifique
2. Utilisé couramment dans une langue et ni plus ni moins fréquent dans un document spécifique qu'à l'habitude
3. Rarement utilisé dans une langue et particulièrement fréquent (ou rare) dans un document spécifique
4. Rarement utilisé dans une langue et ni plus ni moins fréquent dans un document spécifique qu'à l'habitude

Pour comprendre comment des mots peuvent apparaître fréquemment sans laisser de traces significatives, ou apparaître rarement et être fortement caractéristiques d'un document, examinons un exemple. Le tableau suivant contient une liste des dix mots les plus fréquents dans l'une des nécrologies de notre corpus du _New York Times_ et leurs nombres d'occurrences respectifs&#x202F;:

| Rang | Terme    | Décompte (tf) |
| ---- | -------- | -------- |
| 1    | the      | 21       |
| 2    | of       | 16       |
| 3    | her      | 15       |
| 4    | in       | 14       |
| 5    | and      | 13       |
| 6    | she      | 10       |
| 7    | at       | 8        |
| 8    | cochrane | 4        |
| 9    | was      | 4        |
| 10   | to       | 4        |

Observez cette liste et imaginez-vous en train d'essayer de deviner le sujet de la nécrologie représentée par le tableau. On pourrait émettre l'hypothèse que la présence de _her_ (qui peut avoir la fonction du pronom personnel ou de l'adjectif possessif féminin) et de _cochrane_ signifie que l'on parle d'une femme nommée Cochrane. Mais il pourrait tout aussi bien s'agir d'une personne originaire de la ville de Cochrane, au Wisconsin (États-Unis), ou d'une personne impliquée dans l'organisation non gouvernementale sans but lucratif [Cochrane](https://perma.cc/5GU7-2YR2). Le problème est que la plupart des mots qui apparaissent dans cette liste feraient partie de la liste des mots les plus fréquents dans n'importe quelle nécrologie et même dans n'importe quel bloc de texte en langue anglaise d'une taille le moindrement considérable. En effet, la plupart des langues reposent sur une utilisation massive de mots structurels comme les articles, les conjonctions et les prépositions (dont _the,_ _as,_ _of,_ _to_ et _from_ en anglais) qui forment l'ossature grammaticale des textes et qui apparaissent donc partout, quels que soient les sujets dont les textes traitent. Une liste des mots les plus fréquents dans une nécrologie ne nous fournit donc pas nécessairement beaucoup d'information sur la personne à qui le texte rend hommage. Utilisons maintenant **tf-idf** pour pondérer les décomptes d'occurrences des mots et comparer cette même nécrologie au reste du corpus nécrologique du _New York Times_. Les dix mots qui obtiennent les scores les plus élevés sont les suivants&#x202F;: 

| Rang | Terme     | Décompte (tf) |
| ---- | --------- | -------- |
| 1    | cochrane  | 24.85    |
| 2    | her       | 22.74    |
| 3    | she       | 16.22    |
| 4    | seaman    | 14.88    |
| 5    | bly       | 12.42    |
| 6    | nellie    | 9.92     |
| 7    | mark      | 8.64     |
| 8    | ironclad  | 6.21     |
| 9    | plume     | 6.21     |
| 10   | vexations | 6.21     |

Dans ce nouveau tableau, _she_ et _her_ gagnent en importance. _cochrane_ fait toujours partie de la liste, mais on y retrouve aussi deux autres mots qui ressemblent à des noms propres: _nellie_ et _bly_. Or, [Nellie Bly](https://perma.cc/8GFT-D73V) était une journaliste américaine du début du XXe siècle, renommée pour ses enquêtes de fond dont une particulièrement célèbre au cours de laquelle elle s'est fait enfermer dans une institution psychiatrique pendant dix jours pour dénoncer les mauvais traitements infligés aux patients victimes de maladies mentales. De son vrai nom Elizabeth Cochrane Seaman, elle utilisait Nellie Bly comme nom de plume. Ces quelques détails biographiques suffisent à expliquer la présence de sept des dix mots qui apparaissent dans le tableau des scores **tf-idf**: _cochrane,_ _her,_ _she,_ _seaman,_ _bly,_ _nellie_ et _plume._ Pour comprendre la présence de _mark_, _ironclad_ et _vexations_, il suffit de consulter la nécrologie. Bly est morte à l'hôpital Saint Mark à New York. [Son mari](https://perma.cc/C7FX-AKJA) était le président de la *Ironclad Manufacturing Company*. Enfin, une série de _vexations_ (&laquo;&#x202F;tracas&#x202F;&raquo;), dont des fraudes commises par ses employés, des litiges juridiques et une faillite, ont anéanti sa fortune.[^6] Plusieurs des termes qui apparaissent dans cette liste ne sont mentionnés dans la nécrologie qu'une, deux ou trois fois&#x202F;; ils ne sont donc absolument pas fréquents, mais leur présence dans ce texte se distingue malgré tout de la norme du corpus.

# Exécution de tf-idf

## Fonctionnement de l'algorithme

**Tf-idf** peut être implémenté de plusieurs façons, certaines plus complexes que d'autres. Avant d'entrer dans les détails, j'aimerais décrire les grandes lignes du fonctionnement d'une version particulière de l'algorithme. Pour ce faire, nous allons revenir à la nécrologie de Nellie Bly et convertir les décomptes des mots les plus fréquents dans ce texte en scores **tf-idf**. Nous le ferons en répétant les étapes suivies par l'implémentation de **tf-idf** que l'on retrouve dans le module [Scikit-Learn](https://perma.cc/JUN8-39Z6), qui a servi à produire l'exemple présenté à la section précédente. La plupart des opérations mathématiques requises sont de simples additions, multiplications et divisions. Il faudra cependant, à un moment donné, calculer le [logarithme naturel](https://perma.cc/V3GF-P6RL) d'une variable&#x202F;; la plupart des calculatrices en sont capables. Le tableau ci-dessous présente les décomptes d'occurrences bruts pour les 30 premiers mots qui apparaissent dans la nécrologie de Nellie Bly, par ordre alphabétique (**tf**)&#x202F;; la dernière colonne (**df**) contient le nombre de documents du corpus dans lesquels ces mots sont présents, il s'agit d'une mesure appelée la _fréquence de document_. La fréquence de document d'un mot particulier *i* peut être représentée par **df<sub>i</sub>**.

| Indice | Mot        | Décompte (tf) | Df  |
| -----  | ---------- | -------- | --- |
| 1      | afternoon  | 1        | 66  |
| 2      | against    | 1        | 189 |
| 3      | age        | 1        | 224 |
| 4      | ago        | 1        | 161 |
| 5      | air        | 1        | 80  |
| 6      | all        | 1        | 310 |
| 7      | american   | 1        | 277 |
| 8      | an         | 1        | 352 |
| 9      | and        | 13       | 364 |
| 10     | around     | 2        | 149 |
| 11     | as         | 2        | 357 |
| 12     | ascension  | 1        | 6   |
| 13     | asylum     | 1        | 2   |
| 14     | at         | 8        | 362 |
| 15     | avenue     | 2        | 68  |
| 16     | balloon    | 1        | 2   |
| 17     | bankruptcy | 1        | 8   |
| 18     | barrel     | 1        | 7   |
| 19     | baxter     | 1        | 4   |
| 20     | be         | 1        | 332 |
| 21     | beat       | 1        | 33  |
| 22     | began      | 1        | 241 |
| 23     | bell       | 1        | 24  |
| 24     | bly        | 2        | 1   |
| 25     | body       | 1        | 112 |
| 26     | born       | 1        | 342 |
| 27     | but        | 1        | 343 |
| 28     | by         | 3        | 349 |
| 29     | career     | 1        | 223 |
| 30     | character  | 1        | 89  |

La formule la plus directe pour calculer la fréquence _inverse_ de document **idf** d'un mot _i_, requise par **tf-idf**, est **N/df<sub>i</sub>**, où _N_ représente le nombre total de documents dans le corpus. Plusieurs implémentations normalisent cependant les résultats à l'aide de calculs supplémentaires. En règle générale, **tf-idf** utilise la normalisation pour deux raisons&#x202F;: d'abord pour éviter que les calculs de fréquences ne soient biaisés par la présence de documents très courts ou très longs, ensuite pour calculer les valeurs de fréquence inverse de document de chaque mot. Par exemple, l'implémentation de Scikit-Learn remplace **N** par **N+1**, calcule le logarithme naturel de **(N+1)/df<sub>i</sub>** et ajoute 1 au résultat. Nous reviendrons sur la notion de normalisation dans la section intitulée [&laquo;&#x202F;Paramètres Scikit-Learn&#x202F;&raquo;](#paramètres-scikit-learn)

L'équation suivante décrit les opérations que Scikit-Learn applique pour calculer les valeurs d'**idf**[^7]&#x202F;:

$$ idf_i = ln[\, ({N}+1) /\, {df_i}] + 1 $$

Une fois **idf<sub>i</sub>** calculé, **tf-idf<sub>i</sub>** est **tf<sub>i</sub>** multiplié par **idf<sub>i</sub>**.

$$ tf{\text -}idf_i = tf_i \, \times \, idf_i $$

Les équations mathématiques comme celles-ci peuvent être intimidantes lorsqu'on n'a pas l'habitude d'en lire. Cependant, une fois qu'on a acquis l'expérience nécessaire, elles expliquent le fonctionnement d'un algorithme plus clairement que n'importe quelle explication textuelle bien écrite. Pour plus de détails sur ce sujet, le billet en anglais &laquo;&#x202F;Do Digital Humanists Need to Understand Algorithms&#x202F;?&#x202F;&raquo; de Ben Schmidt constitue un bon point de départ.[^8] Afin de rendre la signification des équations du **idf** et du **tf-idf** plus concrètes, j'ai ajouté deux nouvelles colonnes au tableau des fréquences de termes que nous avons vu précédemment. La première nouvelle colonne contient les scores **idf** calculés, tandis que la seconde multiplie les valeurs **Décompte** et **Idf** pour obtenir les scores **tf-idf** finaux.  Notez que les valeurs **idf** sont plus élevées lorsque  les documents apparaissent dans moins de documents (c'est-à-dire,  lorsque leurs valeurs **df** sont basses). Les valeurs ainsi obtenues dans notre exemple sont comprises entre 1 et 6.

D’autres méthodes de normalisation pourraient produire des échelles de valeurs différentes&#x202F;: en utilisant la [valeur centrée réduite](https://perma.cc/XF7S-B533) par exemple, mais ce n'est pas la seule ([cf. l'article Wikipédia en anglais sur le sujet](https://perma.cc/Q47J-VCXM)).

Notez aussi que la formule de calcul de **tf-idf** implémentée par cette version de l'algorithme fait en sorte que les valeurs ne peuvent jamais être inférieures aux décomptes d'occurrences. Il s'agit d'un effet secondaire de la méthode de normalisation: en ajoutant 1 à la valeur **idf**, nous nous assurons de ne jamais multiplier nos **Décomptes** par des nombres inférieurs à 1. Cela évite de trop perturber la distribution des valeurs.

| Indice | Mot       | Décompte | Df  | Idf        | Tf-idf      |
| ------ | --------- | -------- | --- | ---------- | ----------- |
| 1      | afternoon  | 1       | 66  | 2.70066923 | 2.70066923  |
| 2      | against    | 1       | 189 | 1.65833778 | 1.65833778  |
| 3      | age        | 1       | 224 | 1.48926145 | 1.48926145  |
| 4      | ago        | 1       | 161 | 1.81776551 | 1.81776551  |
| 5      | air        | 1       | 80  | 2.51091269 | 2.51091269  |
| 6      | all        | 1       | 310 | 1.16556894 | 1.16556894  |
| 7      | american   | 1       | 277 | 1.27774073 | 1.27774073  |
| 8      | an         | 1       | 352 | 1.03889379 | 1.03889379  |
| 9      | and        | 13      | 364 | 1.00546449 | 13.07103843 |
| 10     | around     | 2       | 149 | 1.89472655 | 3.78945311  |
| 11     | as         | 2       | 357 | 1.02482886 | 2.04965772  |
| 12     | ascension  | 1       | 6   | 4.95945170 | 4.95945170  |
| 13     | asylum     | 1       | 2   | 5.80674956 | 5.80674956  |
| 14     | at         | 8       | 362 | 1.01095901 | 8.08767211  |
| 15     | avenue     | 2       | 68  | 2.67125534 | 5.34251069  |
| 16     | balloon    | 1       | 2   | 5.80674956 | 5.80674956  |
| 17     | bankruptcy | 1       | 8   | 4.70813727 | 4.70813727  |
| 18     | barrel     | 1       | 7   | 4.82592031 | 4.82592031  |
| 19     | baxter     | 1       | 4   | 5.29592394 | 5.29592394  |
| 20     | be         | 1       | 332 | 1.09721936 | 1.09721936  |
| 21     | beat       | 1       | 33  | 3.37900132 | 3.37900132  |
| 22     | began      | 1       | 241 | 1.41642412 | 1.41642412  |
| 23     | bell       | 1       | 24  | 3.68648602 | 3.68648602  |
| 24     | bly        | 2       | 1   | 6.21221467 | 12.42442933 |
| 25     | body       | 1       | 112 | 2.17797403 | 2.17797403  |
| 26     | born       | 1       | 342 | 1.06763140 | 1.06763140  |
| 27     | but        | 1       | 343 | 1.06472019 | 1.06472019  |
| 28     | by         | 3       | 349 | 1.04742869 | 3.14228608  |
| 29     | career     | 1       | 223 | 1.49371580 | 1.49371580  |
| 30     | character  | 1       | 89  | 2.40555218 | 2.40555218  |

Rappelons que les tableaux ci-dessus représentent une version spécifique de l'algorithme **tf-idf**. Il en existe d'autres. On calcule généralement des valeurs **tf-idf** pour tous les mots et pour tous les documents du corpus, pas seulement pour 30 mots dans un seul document. C'est ce qui nous permet de savoir quels mots ont les scores **tf-idf**  les plus élevés dans chaque document. Pour avoir une meilleure idée de ce à quoi ressemblent les résultats d'un calcul **tf-idf** complet, veuillez télécharger et ouvrir le fichier Excel des valeurs calculées pour la nécrologie de Bly dans [les documents d'accompagnement de la leçon](/assets/tf-idf/lecon-fichiers.zip). Pour ce faire, ouvrez le fichier d'archive (de type .zip) et choisissez le fichier `bly_tfidf_complet.xlsx`.

## Comment exécuter tf_idf en Python 3

Dans cette section de la leçon, nous retracerons pas à pas le chemin que j'ai parcouru pour calculer des valeurs de **tf-idf** pour tous les termes apparaissant dans tous les documents du corpus nécrologique. Si vous désirez suivre le processus de plus près, vous pouvez télécharger les fichiers associés à la leçon, ouvrir l'archive `.zip` et exécuter le carnet Jupyter Notebook intitulé `TF-IDF-code-fr.ipynb` qui se trouve dans le dossier `lecon-fichiers`. Vous pouvez aussi créer votre propre carnet Jupyter au même endroit et copier-coller les blocs de code qui apparaissent ci-dessous au moment approprié. Si vous travaillez dans l'environnement Anaconda, consultez la [documentation des carnets Jupyter](https://perma.cc/W92W-C3Z3) pour savoir comment changer le répertoire de travail des carnets. Notez que, comme dans tous les langages de programmation, il existe plusieurs manières de compléter chacune des étapes que nous étudierons ci-dessous.

Mon premier bloc de code est conçu pour récupérer les noms de tous les fichiers .txt qui se trouvent dans le répertoire `txt`. Ces lignes de code importent la classe `Path` du module `pathlib` et invoquent la méthode `Path().rglob()` pour produire une liste de tous les fichiers qui se trouvent dans le répertoire 'txt' et dont les noms se terminent avec l'extension .txt. `pathlib` concaténera le chemin du répertoire, `file.parent`, à chaque nom de fichier pour construire des chemins complets pour chaque fichier (sous macOS ou Windows).

J'ajoute ainsi chaque nom de fichier à une liste nommée `tous_fichiers_txt`. Enfin, je renvoie la longueur de `tous_fichiers_txt` pour vérifier que j'ai bien trouvé les 366 fichiers attendus. Cette approche boucler-et-ajouter est très courante en Python.

```python
from pathlib import Path

tous_fichiers_txt =[]
for fichier in Path("txt").rglob("*.txt"):
     tous_fichiers_txt.append(fichier.parent / fichier.name)

# décompte du nombre de fichiers dans la liste
n_fichiers = len(tous_fichiers_txt)
print(n_fichiers)
```

Concernant le choix des noms de variables il existe deux méthodes courantes qui donne respectivement la priorité à la commodité puis à la sémantique. Par commodité, on pourrait choisir de nommer une variable **x** pour qu'il soit facile et rapide de taper son nom au besoin. Un nom de variable sémantique tente, quant à lui, de transmettre au lecteur une information sur la fonction ou l'usage de la variable. En nommant ma liste de fichiers textuels `tous_fichiers_txt` et la variable qui contient la taille de cette liste `n_fichiers`, j'accorde la priorité à la sémantique. En même temps, j'utilise des abréviations comme `txt` pour &laquo;&#x202F;texte&#x202F;&raquo; et `n` pour &laquo;&#x202F;nombre&#x202F;&raquo; pour gagner du temps et j'ai choisi `tous_fichiers_txt` plutôt que `les_noms_de_tous_les_fichiers_textuels` parce que la concision demeure un objectif important. Les normes concernant l'utilisation des majuscules et des barres de soulignement en Python sont codifiées dans PEP-8, le guide stylistique officiel du langage, avec lequel je vous recommande de vous familiariser.[^9]

Pour diverses raisons, nous voulons que nos calculs s'effectuent par ordre journalier et mensuel (le corpus contient un fichier pour chaque jour et pour chaque mois de l'année). Pour ce faire, nous pouvons utiliser la méthode `sort()` pour classer les fichiers par ordre numérique ascendant, puis afficher le premier nom de fichier pour nous assurer qu'il s'agit bien de `txt/0101.txt`.

```python
tous_fichiers_txt.sort()
tous_fichiers_txt[0]
```

Nous pouvons ensuite utiliser la liste des noms de fichiers pour lire chaque fichier en mémoire et le convertir en un format que Python peut interpréter comme du texte. Le prochain bloc de code contient une autre opération de type boucler-et-ajouter qui parcourt la liste de noms de fichiers et ouvre chacun d'entre eux. L'instruction  `with open(txt_file) as f` permet notamment d'ouvrir un fichier, d'effectuer une action sur celui-ci et de le refermer, ce que nous faisons ici sur tout les fichiers de notre liste. J'invoque ensuite la méthode `read()` de Python pour convertir le contenu de chaque fichier textuel en une chaîne de caractères (`str`), ce qui constitue la manière d'indiquer à Python que les données doivent être interprétées comme du texte. J'ajoute chacune de ces chaînes de caractères, une par une, à une nouvelle liste nommée `tous_documents`. Note importante&#x202F;: les chaînes de caractères qui constituent cette liste y apparaissent dans le même ordre que les noms de fichiers dans la liste `tous_fichiers_txt`.

```python
tous_documents = []
for fichier_txt in tous_fichiers_txt:
    with open(fichier_txt) as f:
        fichier_txt_chaine = f.read()
    tous_documents.append(fichier_txt_chaine)
```

C'est tout le travail de mise en place dont nous avons besoin. Les étapes de traitement du texte comme la [tokenisation](https://perma.cc/8SZP-DCGF) et l'élimination de la ponctuation seront effectuées automatiquement lorsque nous utiliserons le `TfidfVectorizer` de Scikit-Learn pour représenter nos documents à l'aide des scores **tf-idf** calculés en fonction de leur contenu. Le bloc de code ci-dessous importe `TfidfVectorizer` du module Scikit-Learn, qui est préinstallé avec Anaconda. `TfidfVectorizer` est une classe d'objets Python développée en programmation orientée objet. Je construis donc une instance de cette classe, nommée `vectoriseur`, à laquelle je fournis des paramètres spécifiques (j’aurai plus de choses à dire au sujet de ces paramètres dans la section intitulée [&laquo;&#x202F;Paramètres Scikit-Learn&#x202F;&raquo;](#paramètres-scikit-learn)). J'applique ensuite la méthode `fit_transform()` de cet objet à ma liste de chaînes de caractères (la variable nommée `tous_documents`). La variable `documents_transformes` contient les résultats de l'opération `fit_transform()`. Notez que nous pourrions aussi fournir à `TfidfVectorizer` une liste de mots vides (rappelons qu'il s'agit de mots structurels communs) dont nous ne voulons pas nous préoccuper. En outre, pour réaliser certaines opérations, comme la division en lexèmes ou le filtrage des mots vides, dans une langue autre que l'anglais, il pourrait être nécessaire de prétraiter les textes à l'aide d'un autre module Python ou de fournir à `TfidfVectorizer` un analyseur (tokenizer) et/ou une liste de mots vides sur mesure.

```python
# importer le vectoriseur TfidfVectorizer de Scikit-Learn.  
from sklearn.feature_extraction.text import TfidfVectorizer

vectoriseur = TfidfVectorizer(max_df=.65, min_df=1, stop_words=None, use_idf=True, norm=None)
documents_transformes = vectoriseur.fit_transform(tous_documents)
```

La méthode `fit_transform()` ci-dessus transforme la liste de chaînes de caractères en une [matrice creuse](https://perma.cc/4C3Y-M6FD). Dans le cas qui nous concerne, la matrice contient des valeurs **tf-idf** pour tous les mots et tous les textes. Les matrices creuses épargnent de la mémoire en laissant de côté toutes les valeurs égales à zéro. Nous avons cependant besoin d'accéder à toutes les valeurs. Le prochain bloc de code invoque donc la méthode `toarray()` pour convertir la matrice creuse en un [tableau NumPy](https://perma.cc/78YF-4K7K). Nous pouvons afficher la longueur de ce tableau pour nous assurer qu'il est de la même taille que notre liste de documents.

```python
documents_transformes_tableau = documents_transformes.toarray()
# la prochaine ligne de code vérifie que le tableau numpy contient le même nombre
# de documents que notre liste de fichiers
len(documents_transformes_tableau)
```
Un tableau NumPy ressemble à une liste sans y être identique. Je pourrais rédiger une leçon complète rien que sur les différences entre les deux, mais une seule des caractéristiques des tableaux NumPy est importante pour le moment&#x202F;: ils convertissent les données stockées dans `documents_transformes` dans un format qui contient explicitement les scores **tf-idf** de tous les mots dans tous les documents. Rappelons que la matrice creuse, elle, excluait toutes les valeurs égales à zéro.

Nous voulons que toutes les valeurs soient représentées pour que chaque document soit associé au même nombre de valeurs, soit une pour chaque mot qui existe dans le corpus. Chaque ligne du tableau `documents_transformes_tableau` est elle-même un tableau qui représente un des documents du corpus. Nous disposons donc essentiellement d'une grille dans laquelle chaque ligne représente un document et chaque colonne, un mot. Imaginez un tableau semblable à ceux des sections précédentes pour chaque document, mais sans étiquettes pour identifier les lignes et les colonnes.

Pour combiner les valeurs avec leurs étiquettes, il nous faut deux éléments d'information&#x202F;: l'ordre des documents et et l’ordre des tf-idf obtenu pour chaque mot. L'ordre des documents est facile à obtenir puisqu'il s'agit du même que dans la liste `tous_documents`. La liste de tous les mots du corpus, elle, est stockée dans la variable `vectoriseur` et elle suit le même ordre qu'utilise `documents_transformes_tableau` pour emmagasiner les données. Nous pouvons utiliser la méthode `get_feature_names()` de la classe `TFIDFVectorizer` pour accéder à cette liste de mots. Puis, chaque ligne de `documents_transformes_tableau` (qui contient les valeurs **tf-idf** d'un document) peut être jumelée avec la liste de mots. Pour plus de détails sur les structures de données de type DataFrame du module Pandas de Python, veuillez consulter la leçon [&laquo;&#x202F;Visualizing Data with Bokeh and Pandas&#x202F;&raquo;](/en/lessons/visualizing-with-bokeh).

```python
import pandas as pd

# créer un répertoire de sortie s'il n'existe pas déjà
Path("./tf_idf_resultats").mkdir(parents=True, exist_ok=True)

# construire une liste de noms de fichiers de résultats à partir de
# la liste de noms de fichiers de données et du répertoire de sortie
fichiers_resultats = [str(fichier_txt).replace(".txt", ".csv").replace("txt/", "tf_idf_resultats/") for fichier_txt in tous_fichiers_txt]

# traiter chacun des documents du tableau documents_transformes_tableau
# en utilisant enumerate() pour conserver la trace de la position courante dans le tableau
for compteur, document in enumerate(documents_transformes_tableau):
    # construire un objet de la classe DataFrame
    tf_idf_tuples = list(zip(vectoriseur.get_feature_names(), document))
    un_document_format_df = pd.DataFrame.from_records(tf_idf_tuples, columns=['terme', 'pointage']).sort_values(by='pointage', ascending=False).reset_index(drop=True)

    # enregistrer les résultats dans un document CSV, en utilisant
    # la variable 'compteur' pour choisir le nom de fichier
    un_document_format_df.to_csv(fichiers_resultats[compteur])
```


Le bloc de code ci-dessus est composé de trois parties&#x202F;:

1. Après avoir importé le module pandas, le code vérifie l'existence du répertoire de sortie `tf_idf_resultats`. Si ce répertoire n'existe pas déjà, il est créé à ce moment.
2. Un chemin vers un fichier .csv est construit à partir de chacun des noms de fichiers .txt qui apparaissent dans la liste construite plus haut. Le processus de construction de la variable `fichiers_resultats` convertira, par exemple, `txt/0101.txt` (le chemin du premier fichier .txt de la liste) en `tf_idf_resultats/0101.csv`, et ainsi de suite pour tous les fichiers du corpus.
3. À l'aide d'une boucle, on associe chaque vecteur de scores **tf-idf** avec la liste des mots extraite de `vectoriseur`, on convertit les paires mot/score en objets de type DataFrame, et on enregistre chaque DataFrame dans son propre fichier .csv (un format textuel courant pour les feuilles de calcul).

## Interpréter les listes de mots : meilleures pratiques et mises en garde

Lorsque vous exécuterez les blocs de code ci-dessus, vous obtiendrez un répertoire nommé `tf_idf_resultats` contenant 366 fichiers de type .csv. Chacun de ces fichiers contient une liste de mots et de leurs scores **tf-idf** pour un document spécifique. Comme nous avons pu le constater dans le cas de la nécrologie de Nellie Bly, ces listes de mots peuvent être très significatives, cependant, il faut bien comprendre qu'une surinterprétation de ce genre de résultats peut déformer notre compréhension du texte sous-jacent.

En général, il vaut mieux approcher ces listes de mots en se disant qu'elles seront utiles pour susciter des hypothèses ou des questions de recherche, mais que les résultats de **tf-idf** ne justifieront peut-être pas de conclusions définitives à eux seuls. À titre d'exemple, j'ai assemblé une liste de nécrologies d'individus ayant vécus à la fin du <span style="font-variant:small-caps;">XIX</span><sup>e</sup> et au début du <span style="font-variant:small-caps;">XX</span><sup>e</sup> siècle qui ont écrit pour des journaux ou pour des magazines et qui étaient associés d'une quelconque façon aux mouvements de réforme sociale. Cette liste inclut Nellie Bly, [Willa Cather](https://perma.cc/6RGB-UQHV), [W.E.B. Du Bois](https://perma.cc/QYW8-SL8D), [Upton Sinclair](https://perma.cc/43WH-G6XL) et [Ida Tarbell](https://perma.cc/TC7V-8CEY), mais il est possible que d'autres individus dont les nécrologies apparaissent dans le corpus correspondent également à cette description.[^10]

Je m'attendais initialement à ce que plusieurs mots significatifs soient partagés entre ces individus, mais ce n'est pas toujours le cas. Le tableau ci-dessous présente les 20 mots dont les scores **tf-idf** sont les plus élevés dans chacune des cinq nécrologies. Chaque liste est dominée par des mots spécifiques à son document (noms propres, lieux, entreprises, etc.) que l'on peut filtrer à l'aide des paramètres de **tf-idf** ou tout simplement ignorer. La section &laquo;&#x202F;Paramètres Scikit-Learn&#x202F;&raquo; approfondit les questions liées aux entités nommées ou un syntagme comme des tokens uniques. D'autre part, on peut chercher des mots qui expriment clairement la relation entre un individu et sa profession littéraire.

| Rang Tf-idf | Nellie Bly | Willa Cather | W.E.B. Du Bois | Upton Sinclair | Ida Tarbell |
| 1 | cochrane | cather | dubois | sinclair | tarbell |
| 2 | her | her | dr | socialist | she |
| 3 | she | she | negro | upton | her |
| 4 | seaman | nebraska | ghana | **books** | lincoln |
| 5 | bly | miss | peace | lanny | miss |
| 6 | nellie | forrester | **encyclopedia** | social | oil |
| 7 | mark | sibert | communist | budd | abraham |
| 8 | ironclad | twilights | barrington | jungle | mcclure |
| 9 | **plume** | willa | fisk | brass | easton |
| 10 | vexations | antonia | atlanta | california | **volumes** |
| 11 | phileas | mcclure | folk | **writer** | minerva |
| 12 | 597 | **novels** | booker | vanzetti | standard |
| 13 | elizabeth | pioneers | successively | macfadden | business |
| 14 | **nom** | cloud | souls | sacco | titusville |
| 15 | balloon | **book** | council | **wrote** | **articles** |
| 16 | forgeries | calif | party | meat | bridgeport |
| 17 | mcalpin | **novel** | disagreed | **pamphlets** | expose |
| 18 | asylum | southwest | harvard | my | trusts |
| 19 | fogg | **verse** | **arts** | industry | mme
| 20 | verne | **wrote** | soviet | **novel** | **magazine** |

J'ai utilisé les caractères gras pour souligner des termes qui semblent particulièrement reliés à l'écriture. Cette liste inclut _articles_, _arts_, _book_ (livre), _books_ (livres), _encyclopedia_ (encyclopédie), _magazine_, _nom_, _novel_ (roman), _novels_ (romans), _pamphlets_, _plume_, _verse_ (vers/poésie), _volumes_, _writer_ (auteur/autrice) et _wrote_ (écrit), auxquels on pourrait ajouter les titres de livres spécifiques ou les noms de magazines. Ne tenons pas compte de ces détails pour le moment et remarquons que, si les listes de Cather et de Sinclair contiennent plusieurs mots associés aux livres et à l'écriture, ce n'est pas le cas pour Bly, Du Bois et Tarbell.

On pourrait facilement tirer des conclusions hâtives. L'identité de Cather semble fortement reliée à son genre, à son attachement à des lieux, à sa fiction et à sa poésie. Sinclair est plus fortement associé à la politique et à ses écrits au sujet de la viande, de l'industrie et du procès controversé de [Nicola Sacco et Bartolomeo Vanzetti](https://perma.cc/3VZK-PLDG) qui a mené à l'exécution des deux individus. Bly est reliée à son pseudonyme, à son mari et à ses écrits portant sur les institutions psychiatriques. Du Bois est relié aux questions de race et à sa carrière universitaire. Quant à Tarbell, ce sont les thèmes sur lesquels elle écrit qui la définissent&#x202F;: les affaires, les monopoles, le géant du pétrole Standard Oil et le président américain Abraham Lincoln. En allant un peu plus loin, je pourrais argumenter que la discussion du genre semble plus caractéristique des nécrologies de femmes, tandis que la question raciale n'apparaît parmi les termes les plus importants que dans le cas du seul Afro-Américain de la liste.

Chacune de ces observations nécessite d’être approfondie et ne doit  pas impliquer une généralisation. D'abord, je dois vérifier si les paramètres que j'ai choisis pour **tf-idf** produisent des effets qui pourraient disparaître dans d'autres conditions&#x202F;; des résultats probants devraient être assez stables pour résister à ce genre d'ajustements. Notez que nous discuterons de certains de ces paramètres dans la section [&laquo;&#x202F;Paramètres Scikit-Learn&#x202F;&raquo;](#paramètres-scikit-learn). Je devrai ensuite lire au moins quelques-unes des nécrologies pour m'assurer que certains termes ne me transmettent pas de faux signaux. En lisant la nécrologie de Du Bois, par exemple, je pourrais constater que les mentions de son oeuvre &laquo;&#x202F;The Encyclopedia of the Negro&#x202F;&raquo; contribue au moins en partie à la valeur du score du mot _negro_ dans le texte.

Par ailleurs, je pourrais découvrir que la nécrologie de Bly inclut effectivement des mots comme _journalism_, _journalistic_, _newspapers_ (journaux) et _writing_ (écriture), mais cette nécrologie est très courte et la plupart des mots qui y apparaissent ne le font qu'une ou deux fois. Des mots qui ont de très forts scores **idf** sont donc plus susceptibles d'apparaître au sommet de sa liste. Puisque je veux vraiment équilibrer les poids de **tf** et d'**idf**, je pourrais ne pas tenir compte des mots qui apparaissent seulement dans quelques documents ou encore ignorer les résultats provenant de nécrologies dont la longueur est inférieure à un certain seuil.

Enfin, je peux concevoir des tests pour répondre directement à des questions comme: est-ce que les nécrologies d'Afro-Américains sont plus susceptibles de mentionner la race&#x202F;? Je crois que l'hypothèse &laquo;&#x202F;oui&#x202F;&raquo; est plausible mais je devrais tout de même assujettir mes hypothèses à l'épreuve d'un examen minutieux avant de tirer d'en des conclusions.

## Quelques manières d'utiliser tf-idf en histoire numérique

Comme je l'ai déjà mentionné, **tf-idf** provient du domaine de la reherche d'informations. La normalisation de la fréquence d'occurrence de mots dans les différents documents d'un corpus constitue d'ailleurs toujours une opération courante dans l'industrie du développement Web, notamment dans le cas des moteurs de recherche textuels. En contexte d'analyse culturelle ou d'histoire numérique, cependant, la pertinence de **tf-idf** se limite à des tâches bien précises. En général, celles-ci appartiennent à l'une de trois catégories&#x202F;:

### 1. Outil d'exploration ou de visualisation

Nous avons déjà démontré que des listes de mots accompagnées de scores **tf-idf** pour chacun des documents d'un corpus peuvent constituer de puissants outils d'interprétation. Elles peuvent notamment suggérer des hypothèses ou des questions de recherche. Ces listes peuvent aussi former les bases de stratégies d'exploration et de visualisation plus sophistiquées. L'article [&laquo;&#x202F;A full-text visualization of the Iraq War Logs&#x202F;&raquo;](https://perma.cc/QBZ4-DKTE) de Jonathan Stray et Julian Burgess en constitue un bon exemple.[^11] Stray et Burgess utilisent des valeurs **tf-idf** pour construire une visualisation de réseau dans laquelle des registres de la guerre en Irak sont reliés à leurs mots-clés les plus distinctifs. Cette technique de visualisation d'information textuelle a permis à Stray de développer le [projet Overview](https://perma.cc/L8PN-KQ5B), qui propose aux usagers un tableau de bord à partir duquel naviguer dans des milliers de documents pour visualiser leurs contenus. Nous pourrions employer cette approche pour visualiser notre corpus nécrologique et peut-être y identifier des groupes d'articles dont les mots-clés se ressemblent.

### 2. Outil pour calculer la similarité des textes et des ensembles de traits caractéristiques

Puisque **tf-idf** produit souvent des scores bas pour les mots structurels fréquents et des scores plus élevés pour les mots associés au contenu thématique d'un texte, cette méthode est appropriée pour les tâches qui requièrent l'identification de similarités entre des textes. Un moteur de recherche appliquera souvent **tf-idf** à un corpus pour ensuite proposer à l'usager des résultats classés en fonction de la [similarité cosinus](https://perma.cc/9NV6-SS9G) entre les documents et les mots-clés de recherche entrés par l'usager. Le même raisonnement s'applique à des questions comme: &laquo;&#x202F;quelle nécrologie de notre corpus ressemble le plus à celle de Nellie Bly&#x202F;&raquo;&#x202F;?

Nous pouvons aussi utiliser **tf-idf** pour découvrir les mots les plus importants dans un document ou dans un groupe de documents. Par exemple, je pourrais regrouper un ensemble de nécrologies de journalistes (dont celle de Nellie Bly) dans un seul document avant d'appliquer **tf-idf** à celui-ci. Les résultats de l'opération pourraient servir de règle heuristique pour identifier des termes spécifiques aux nécrologies de journalistes, en comparaison avec l'ensemble des nécrologies du corpus. La liste de mots ainsi obtenue pourrait ensuite servir dans une variété d'autres tâches informatiques.

### 3. Étape de prétraitement

Les paragraphes ci-dessus ont permis d'introduire les raisons pour lesquelles le score **tf-idf** sert souvent d'étape de prétraitement dans les calculs d'apprentissage automatique. Par exemple, les scores **tf-idf** ont tendance à être plus révélateurs que les décomptes bruts lorsqu'on développe un modèle de classification par apprentissage automatique supervisé, notamment parce qu'ils augmentent les poids des mots reliés aux thèmes des documents tout en réduisant ceux des mots structurels fréquents. Il existe cependant une exception notable à cette règle&#x202F;: l'identification de l'auteur d'un texte anonyme, pour laquelle les mots structurels ont une forte valeur prédictive. 

<div class="alert alert-info">
<p>Note du traducteur&#x202F;: la leçon intitulée <a href="https://programminghistorian.org/fr/lecons/introduction-a-la-stylometrie-avec-python">&laquo;&#x202F;Introduction à la stylométrie en Python&#x202F;&raquo;</a> présente une application de ce genre de calculs.</p>
</div>    

Comme nous le verrons dans la section sur les [paramètres de Scikit-Learn](#paramètres-scikit-learn), **tf-idf** peut aussi émonder les listes de traits caractéristiques des modèles d'apprentissage automatique&#x202F;; or, il est souvent préférable de développer des modèles basés sur le moins de traits caractéristiques possible.

## Variations sur le thème de tf-idf

### Paramètres Scikit-Learn

L'objet `TfidfVectorizer` de Scikit-Learn dispose de plusieurs paramètres internes qu'on peut modifier pour influencer les résultats de calcul. En règle générale, tous ces paramètres ont leurs avantages et leurs inconvénients&#x202F;: il n'existe pas de configuration parfaite unique. Il est donc préférable de bien connaître chacun des réglages possibles afin de pouvoir expliquer et défendre vos choix le moment venu. La liste complète des paramètres peut être consultée dans la [documentation de Scikit-Learn](https://perma.cc/JUN8-39Z6)&#x202F;; en voici quelques-uns parmi les plus importants&#x202F;:

#### 1. Mots vides (stopwords)

Dans le code ci-dessus, j'ai utilisé `stop_words=None` mais `stop_words='english'` est aussi disponible. Ce réglage filtrera automatiquement de votre corpus les mots très courants, comme &laquo;&#x202F;the&#x202F;&raquo;, &laquo;&#x202F;to&#x202F;&raquo;, and &laquo;&#x202F;of&#x202F;&raquo;, qui apparaissent dans une [liste prédéfinie](https://perma.cc/6CSZ-G9BL). Notez que la plupart de ces mots vides ont probablement déjà des scores **tf-idf** très bas en raison de leur ubiquité, même si d'autres réglages peuvent influencer ces scores. Pour une discussion des listes de mots vides qu’on retrouve dans divers outils open-source de traitement du langage naturel, veuillez lire [&laquo;&#x202F;Stop Word Lists in Free Open-source Software Packages&#x202F;&raquo;](https://perma.cc/V5WN-4E8P).

<div class="alert alert-info">
Note du traducteur&#x202F;: il est aussi possible de remplacer &laquo;&#x202F;None&#x202F;&raquo; par une liste de mots vides personnalisée, comme `stop_words=['le', 'la', 'les']`. Si vous travaillez avec des documents en français, il s'agit d'une alternative potentiellement plus efficace que de se fier au faible score <b>tf-idf</b> de la plupart des mots-vides.
</div>

#### 2. min_df, max_df

Ces paramètres contrôlent le nombre minimal et le nombre maximal de documents dans lesquels un mot doit apparaître pour être inclus dans les calculs. Les deux paramètres peuvent être exprimés sous forme de nombres réels entre 0 et 1, qui représentent alors des pourcentages de l'ensemble du corpus, ou sous forme de nombres entiers qui représentent des décomptes de documents bruts. En règle générale, spécifier une valeur inférieure à 0.9 pour max_df éliminera la majorité (voire la totalité) des mots vides.

#### 3. max_features

Ce paramètre élague les termes les moins fréquents du corpus avant d'appliquer **tf-idf**. Il peut être particulièrement utile en contexte d'apprentissage automatique, où l'on ne souhaite habituellement pas dépasser le nombre de traits caractéristiques recommandé par les concepteurs de l'algorithme choisi.

#### 4. norm, smooth_idf, and sublinear_tf

Chacun de ces paramètres influencera l'éventail de valeurs numériques que l'algorithme **tf-idf** produira. Le paramètre `norm` est compatible avec la normalisation l1 et l2, expliquée sur [machinelearningmastery.com](https://perma.cc/3ULS-SUB2). `Smooth_idf` lisse les résultats en ajoutant la valeur 1 à chaque fréquence de document, comme s'il existait un document additionnel qui contient exactement une occurrence de tous les mots qui apparaissent dans le corpus. `Sublinear_tf'` applique une opération de changement d'échelle aux résultats en remplaçant tf par log(tf). Pour plus de détails au sujet du lissage et de la normalisation dans le contexte de **tf-idf**, veuillez consulter Manning, Raghavan et Schütze.[^12]

### Traits caractéristiques : au-delà des mots

Le concept fondamental de **tf-idf**, qui consiste à pondérer les décomptes d'occurrences en fonction du nombre de documents dans lesquels les mots apparaissent, peut s'appliquer à d'autres traits caractéristiques des textes. Par exemple, il est relativement facile de combiner **tf-idf** avec la [racinisation](https://perma.cc/WV3J-BF3B) ou la [lemmatisation](https://perma.cc/T3XA-Q9HG), deux méthodes courantes qui permettent de regrouper de multiples déclinaisons et conjugaisons du même mot en une seule forme. Par exemple, la racine de _happy_ et _happiness_ est _happi_ tandis que le lemme qui les regroupe est _happy_. Une fois la racinisation ou la lemmatisation complétée, on peut remplacer les décomptes de mots par les décomptes de racines ou de lemmes avant d'appliquer **tf-idf**. Notez que, puisque ces opérations fusionnent plusieurs formes apparentées en une seule, les lemmes et les racines auront des décomptes d'occurrences plus élevés que chacun des mots qu'ils regroupent, et donc des valeurs **tf-idf** habituellement plus basses.

On peut aussi appliquer la transformation **tf-idf** à des locutions ou à des n-grammes, c'est-à-dire à des séquences de mots consécutifs. Un article intitulé  [&laquo;&#x202F;These Are The Phrases Each GOP Candidate Repeats Most&#x202F;&raquo;](https://perma.cc/37WS-MB8F), publié sur fivethirtyeight.com en mars 2016, utilise cette approche pour calculer les fréquences inverses de documents de phrases entières plutôt que celles de mots.[^13]

## tf-idf et méthodes alternatives communes

On peut comparer **tf-idf** à plusieurs autres méthodes qui servent à isoler et/ou à classifier les mots les plus importants dans un document ou dans une collection de documents. Cette section mentionne brièvement trois de ces méthodes alternatives, apparentées mais distinctes, qui mesurent des aspects similaires mais non identiques de l'information textuelle.

### 1. Spécificité (Keyness)

Plutôt que de transformer les décomptes d'occurrences à l'aide de calculs, la spécificité produit une valeur numérique qui indique jusqu'à quel point la présence d'un mot dans un document est statistiquement typique ou atypique par rapport à l'ensemble du corpus. Par exemple, à l'aide d'un [test du khi-carré](https://perma.cc/4Z2W-SZCS), il est possible de mesurer l'écart entre la fréquence d'occurrence d'un mot et la norme du corpus, puis de dériver une [valeur p](https://perma.cc/X3AW-F6B9) qui indique la probabilité d'observer cette fréquence d'occurrence dans un échantillon aléatoire. Pour plus d'information sur la spécificité, voir Bondi et Scott.[^14]


<div class="alert alert-info">
Note du traducteur &#x202F;: En anglais, &laquo;&#x202F;keyness&#x202F;&raquo; est un terme générique qui regroupe toute une panoplie de mesures statistiques qui tentent d'assigner une signification quantifiable à la présence d'un terme dans un document ou dans un ensemble de documents, en comparaison avec un corpus plus étendu. En français, le terme &laquo;&#x202F;spécificité&#x202F;&raquo; a acquis un sens plus précis suite aux travaux de Pierre Lafon&#x202F;; voir notamment l'article de 1980 &laquo;&#x202F;Sur la variabilité de la fréquence des formes dans un corpus&#x202F;&raquo;, publié dans la revue <i>Mots</i>, vol. 1, no. 1.
</div>

### 2. Modèles thématiques

La modélisation thématique et **tf-idf** sont des techniques radicalement différentes, mais je constate que les néophytes en matière d'humanités numériques désirent souvent modéliser les thèmes d'un corpus dès le début alors que **tf-idf** constituerait parfois un meilleur choix.[^15] Puisque l'algorithme est transparent et que ses résultats sont reproductibles, **tf-idf** est particulièrement utile lorsqu'on souhaite obtenir une vue d'ensemble d'un corpus, à vol d'oiseau, pendant la phase d'exploration initiale de la recherche. Comme le mentionne Ben Schmidt, les chercheurs qui emploient la modélisation thématique doivent reconnaître que les thèmes qui en ressortent ne sont pas forcément aussi cohérents qu'on le souhaiterait.[^16] C'est l'une des raisons pour lesquelles **tf-idf** a été intégré au [projet Overview](https://perma.cc/L8PN-KQ5B).

Les modèles thématiques peuvent aussi aider les chercheurs à explorer leurs corpus et ils offrent de nombreux avantages, notamment la capacité de suggérer de vastes catégories ou &laquo;&#x202F;communautés&#x202F;&raquo; de textes, mais il s'agit d'une caractéristique commune à l'ensemble des méthodes d'apprentissage automatique non supervisées. Les modèles thématiques sont particulièrement attrayants parce qu'ils assignent à chaque document des valeurs numériques qui mesurent jusqu'à quel point chacun des thèmes y est important et parce qu'ils représentent ces thèmes sous forme de listes de mots coprésents, ce qui suscite de fortes impressions de cohérence. Cependant, l'algorithme probabiliste qui sous-tend la modélisation thématique est très sophistiqué et simple d'en déformer les résultats si l'on n'est pas assez prudent. Les mathématiques derrière **tf-idf**, elles, sont assez simples pour être expliquées dans une feuille de calcul Excel.

### 3. Résumé automatique des textes

Le résumé automatique est une autre manière d'explorer un corpus. Rada Mihalcea et Paul Tarau, par exemple, ont publié au sujet de TextRank, un modèle de classement basé sur la théorie des graphes, aux possibilités prometteuses pour l'extraction automatique de mots et de phrases-clés.[^17] Comme dans le cas de la modélisation thématique, TextRank approche la recherche d'informations d'une manière complètement différente du **tf-idf** mais les objectifs des deux algorithmes ont beaucoup en commun. Cette méthode pourrait être appropriée pour votre propre recherche, surtout si votre but consiste à obtenir assez rapidement une impression générale du contenu de vos documents avant de construire un projet de recherche plus poussé.

# Références et lectures supplémentaires

- Milo Beckman, «&nbsp;These Are The Phrases Each GOP Candidate Repeats Most,&nbsp;», _FiveThirtyEight_, le 10 mars 2016,  consulté le 9 juin 2022, [https://fivethirtyeight.com/features/these-are-the-phrases-each-gop-candidate-repeats-most/](https://perma.cc/37WS-MB8F).

- Jessica Bennett et Amisha Padnani, «&nbsp;Overlooked&nbsp;», _The New York Times_, 8 mars 2018, [https://www.nytimes.com/interactive/2018/obituaries/overlooked.html](https://perma.cc/HWZ7-XS23).

- David M. Blei, Andrew Y. Ng et Michael I. Jordan, «&nbsp;Latent Dirichlet Allocation«&nbsp;, _Journal of Machine Learning Research_ 3 (Janvier 2003): 993-1022.

- Marina Bondi et Mike Scott, dirs. _Keyness in Texts_. Philadelphie: John Benjamins, 2010.

- Scikit-Learn Developers «&nbsp;TfidfVectorizer&nbsp;»(en anglais), consulté le 9 juin 2022, [https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html](https://perma.cc/JUN8-39Z6).

- Justin Grimmer et Gary King. [«&nbsp;Quantitative Discovery from Qualitative Information: A General-Purpose Document Clustering Methodology (2009)&nbsp;»](https://perma.cc/4YAL-H6VN), _Rencontre APSA 2009 à Toronto_, le 24 août 2009, [PDF](https://perma.cc/NUS2-J3YP).

- «&nbsp;Ida M. Tarbell, 86, Dies in Bridgeport&nbsp;», [_The New York Times_, 17 janvier 1944](https://perma.cc/NBV6-S2XM).

- Pierre Lafon, «&nbsp;Sur la variabilité de la fréquence des formes dans un corpus&nbsp;», _Mots_ 1, no. 1 (1980): 127-165.

- C.D. Manning, P. Raghavan et H. Schütze, _Introduction to Information Retrieval_. Cambridge: Cambridge University Press, 2008.

- Rada Mihalcea et Paul Tarau. «&nbsp;Textrank: Bringing order into text&nbsp;», _Proceedings of the 2004 Conference on Empirical Methods in Natural Language Processing_, Barcelone, Espagne, 2004. [http://www.aclweb.org/anthology/W04-3252](https://perma.cc/SMV5-7MYY)

- «&nbsp;Nellie Bly, Journalist, Dies of Pneumonia&nbsp;», [_The New York Times_, 28 janvier 1922](https://perma.cc/LA5B-65HL).

- G. Salton et M.J. McGill, _Introduction to Modern Information Retrieval_. New York: McGraw-Hill, 1983.

- Ben Schmidt, «&nbsp;Do Digital Humanists Need to Understand Algorithms?&nbsp;», _Debates in the Digital Humanities 2016_. Édition en ligne. Minneapois: University of Minnesota Press. [http://dhdebates.gc.cuny.edu/debates/text/99](https://perma.cc/95WD-SDM5).

- Ben Schmidt, «&nbsp;Words Alone: Dismantling Topic Models in the Humanities&nbsp;», _Journal of Digital Humanities_. Vol. 2, No. 1 (2012): n.p. [http://journalofdigitalhumanities.org/2-1/words-alone-by-benjamin-m-schmidt/](https://perma.cc/LT4N-X4MZ).

- Karen Spärck Jones, «&nbsp;A Statistical Interpretation of Term Specificity and Its Application in Retrieval.&nbsp;», _Journal of Documentation_ 28, no. 1 (1972): 11–21.

- Jonathan Stray et Julian Burgess. «&nbsp;A Full-text Visualization of the Iraq War Logs&nbsp;», 10 décembre 2010 (dernière mise à jour en avril 2012), [http://jonathanstray.com/a-full-text-visualization-of-the-iraq-war-logs](https://perma.cc/QBZ4-DKTE).

- Ted Underwood, «&nbsp;Identifying diction that characterizes an author or genre: why Dunning's may not be the best method&nbsp;», _The Stone and the Shell_, 9 novembre 2011, [https://tedunderwood.com/2011/11/09/identifying-the-terms-that-characterize-an-author-or-genre-why-dunnings-may-not-be-the-best-method/](https://perma.cc/SY25-UXK3).

- Ted Underwood, «&nbsp;The Historical Significance of Textual Distances&nbsp;», Atelier LaTeCH-CLfL (Version préimpression), COLING, Santa Fe, 2018, [https://doi.org/10.48550/arXiv.1807.00181](https://doi.org/10.48550/arXiv.1807.00181).

- Guido van Rossum, Barry Warsaw et Nick Coghlan. «&nbsp;PEP 8 - Style Guide for Python Code&nbsp;», 5 juillet 2001 (mise à jour août 2013), [https://www.python.org/dev/peps/pep-0008/](https://perma.cc/P2ZM-VPQM).

- Alden Whitman, «&nbsp;Upton Sinclair, Author, Dead; Crusader for Social Justice, 90&nbsp;», [_The New York Times_, 26 novembre 1968](https://perma.cc/E4N7-2KD6).

- «&nbsp;W. E. B. DuBois Dies in Ghana; Negro Leader and Author, 95&nbsp;», [_The New York Times_, 28 août 1963](https://perma.cc/W5NX-XZRV).

- «&nbsp;Willa Cather Dies; Noted Novelist, 70&nbsp;», [_The New York Times_, 25 avril 1947](https://perma.cc/2L7H-WGKN).

## Alternatives à Anaconda

Si vous n'utilisez pas Anaconda, il faudra vous assurer de disposer des outils prérequis suivants&#x202F;:

1. Une installation de Python 3 (préférablement Python 3.6 ou une version plus récente)
2. Idéalement, un environnement virtuel dans lequel installer et exécuter le Python
3. Le module Scikit-Learn et ses dépendances (voir [http://scikit-learn.org/stable/install.html](http://scikit-learn.org/stable/install.html))
4. Jupyter Notebook et ses dépendances

# Notes

[^1]: Ted Underwood, «&nbsp;Identifying diction that characterizes an author or genre: why Dunning's may not be the best method&nbsp;», _The Stone and the Shell_, 9 novembre 2011, [https://tedunderwood.com/2011/11/09/identifying-the-terms-that-characterize-an-author-or-genre-why-dunnings-may-not-be-the-best-method/](https://perma.cc/SY25-UXK3).

[^2]: Jessica Bennett et Amisha Padnani, «&nbsp;Overlooked&nbsp;», _The New York Times_, 8 mars 2018, [https://www.nytimes.com/interactive/2018/obituaries/overlooked.html](https://perma.cc/HWZ7-XS23).

[^3]: Ce jeu de données est tiré d'une version du site &laquo;&#x202F;On This Day&#x202F;&raquo; du *New York Times* qui n'a pas été mise à jour depuis le 31 janvier 2011 et qui a été remplacée par un nouveau blogue plus élégant situé au [https://learning.blogs.nytimes.com/on-this-day/](https://perma.cc/W627-RBUS). Ce qui reste sur le site "On This Day" est une page HTML statique pour chaque jour de l'année (0101.html, 0102.html, etc.), y compris une page pour le 29 février (0229.html). Le contenu semble avoir été écrasé à chaque mise à jour&#x202F;; il n'y a donc pas d'archives du contenu publié à chaque année. On peut présumer que les pages associées aux jours de janvier ont été mises à jour pour la dernière fois en 2011, tandis que celles pour les dates entre le 1er février et de 31 décembre ont probablement été mises à jour pour la dernière fois en 2010. La page du 29 février a probablement été changée pour la dernière fois le 29 février 2008.

[^4]: Karen Spärck Jones, «&nbsp;A Statistical Interpretation of Term Specificity and Its Application in Retrieval.&nbsp;», _Journal of Documentation_ 28, no. 1 (1972): 16.

[^5]: «&nbsp;Nellie Bly, Journalist, Dies of Pneumonia&nbsp;», [_The New York Times_, 28 janvier 1922: 11](https://perma.cc/LA5B-65HL).

[^6]: Scikit-Learn Developers, «&nbsp;TfidfVectorizer&nbsp;» (en anglais), consulté le 9 juin 2022, [https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html](https://perma.cc/JUN8-39Z6).

[^7]: Ben Schmidt, «&nbsp;Do Digital Humanists Need to Understand Algorithms?&nbsp;», _Debates in the Digital Humanities 2016_. Édition en ligne. Minneapolis: University of Minnesota Press. [http://dhdebates.gc.cuny.edu/debates/text/99](https://perma.cc/95WD-SDM5).

[^8]: Guido van Rossum, Barry Warsaw et Nick Coghlan. «&nbsp;PEP 8 - Style Guide for Python Code&nbsp;», 5 juillet 2001 (mise à jour août 2013), [https://www.python.org/dev/peps/pep-0008/](https://perma.cc/P2ZM-VPQM).

[^9]: «&nbsp;Ida M. Tarbell, 86, Dies in Bridgeport&nbsp;», [_The New York Times_, 17 janvier 1944](https://perma.cc/NBV6-S2XM); «&nbsp;W. E. B. DuBois Dies in Ghana; Negro Leader and Author, 95&nbsp;», [_The New York Times_, 28 août 1963](https://perma.cc/W5NX-XZRV); Alden Whitman, «&nbsp;Upton Sinclair, Author, Dead; Crusader for Social Justice, 90&nbsp;», [_The New York Times_, 26 novembre 1968](https://perma.cc/E4N7-2KD6); «&nbsp;Willa Cather Dies; Noted Novelist, 70&nbsp;», [_The New York Times_, 25 avril 1947](https://perma.cc/2L7H-WGKN).

[^10]: Jonathan Stray et Julian Burgess. «&nbsp;A Full-text Visualization of the Iraq War Logs&nbsp;», 10 décembre 2010 (dernière mise à jour en avril 2012), [http://jonathanstray.com/a-full-text-visualization-of-the-iraq-war-logs](https://perma.cc/QBZ4-DKTE).

[^11]: C.D. Manning, P. Raghavan et H. Schütze, _Introduction to Information Retrieval_ (Cambridge: Cambridge University Press, 2008), 118-120.

[^12]: Milo Beckman, «&nbsp;These Are The Phrases Each GOP Candidate Repeats Most&nbsp;», _FiveThirtyEight_, le 10 mars 2016,  consulté le 9 juin 2022, [https://fivethirtyeight.com/features/these-are-the-phrases-each-gop-candidate-repeats-most/](https://perma.cc/37WS-MB8F).

[^13]: Marina Bondi et Mike Scott (dir.). _Keyness in Texts_. (Philadelphie: John Benjamins, 2010).

[^14]: Il n'est habituellement pas recommandé d'appliquer **tf-idf** comme prétraitement avant de produire un modèle thématique. Voir&nbsp;: [https://datascience.stackexchange.com/questions/21950/why-we-should-not-feed-lda-with-tfidf](https://perma.cc/N5W9-TYX7).

[^15]: Ben Schmidt, «&nbsp;Words Alone: Dismantling Topic Models in the Humanities&nbsp;», _Journal of Digital Humanities_. Vol. 2, No. 1 (2012): n.p., [http://journalofdigitalhumanities.org/2-1/words-alone-by-benjamin-m-schmidt/](https://perma.cc/LT4N-X4MZ).

[^16]: Rada Mihalcea et Paul Tarau. «&nbsp;Textrank: Bringing order into text&nbsp;», _Proceedings of the 2004 Conference on Empirical Methods in Natural Language Processing_, Barcelone, Espagne, 2004, [http://www.aclweb.org/anthology/W04-3252](https://perma.cc/SMV5-7MYY).
