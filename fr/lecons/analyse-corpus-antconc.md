---
title: Analyse de corpus avec AntConc
layout: lesson
slug: analyse-corpus-antconc
date: 2015-06-19
authors:
- Heather Froehlich
reviewers:
- Nabeel Siddiqui
- Rob Sieczkiewicz
editors:
- Fred Gibbs
translator:
- Hugo Bonin
translation-editor:
- Sofia Papastamkou
translation-reviewer:
- Antoine Champigny
- François Dominic Laramée
translation_date: 2019-06-19
original: corpus-analysis-with-antconc
difficulty: 1
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/240
activity: analyzing
topics: [distant-reading]
abstract: |
  L'analyse de corpus est un type d'analyse textuelle qui permet de faire des comparaisons d'objets textuels à grande échelle (la fameuse "lecture à distance" (_distant reading_)).
original: corpus-analysis-with-antconc
avatar_alt: Trois grandes bibliothèques ornées
doi: 10.46430/phfr0001
---

{% include toc.html %}





## Introduction
L'analyse de corpus est un type d'analyse textuelle qui permet de faire des comparaisons d'objets textuels à grande échelle — la fameuse "lecture à distance" (_distant reading_). Cela nous permet de voir des choses que nous n'observons pas nécessairement lorsque nous lisons à l'oeil nu. Si vous avez une collection de documents, vous voudrez peut-être trouver des schémas grammaticaux ou les phrases récurentes dans votre corpus. Vous voudrez peut-être aussi identifier de manière statistique les expressions probables ou improbables chez un(e) auteur(e) ou dans un genre particulier, trouver des exemples spécifiques de structures grammaticales ou encore examiner beaucoup d'occurrences d'un concept particulier à travers une série de documents. L'analyse de corpus est surtout utile pour vérifier des intuitions et/ou trianguler des résultats issus d'autres méthodes digitales.

À la fin de ce tutoriel, vous serez en mesure de :

* créer et télécharger un corpus de texte
* conduire une recherche de mot-clé-en-contexte (_keyword-in-context_)
* identifier les schémas récurrents autour d'un mot particulier
* utiliser des requêtes de recherche plus spécifiques
* examiner les différences statistiquement significatives entre les corpus
* effectuer des comparaisons multimodales à l'aide de méthodes de linguistique de corpus

Vous avez déjà fait ce genre de choses auparavant, si vous avez déjà...

* recherché un terme spécifique dans un document .pdf ou .doc
* utilisé [Voyant Tools][48] pour analyser des schémas dans un texte
* suivi les tutoriels d'introduction à Python du [Programming Historian][51]

En quelque sorte, [Voyant Tools](http://voyant-tools.org/) est une passerelle vers la réalisation d'analyses plus sophistiquées et reproductibles, car l'esthétique de bricolage des scripts Python ou R peut ne pas convenir à tout le monde. [AntConc](http://www.laurenceanthony.net/software/antconc/) comble ce vide en étant un logiciel autonome d'analyse linguistique de textes, disponible gratuitement pour Windows, Mac OS et Linux. Par ailleurs, il est régulièrement mis à jour par son créateur,  [Laurence Anthony](http://www.laurenceanthony.net/). Il existe d'autres logiciels de concordance, mais AntConc est librement disponible sur toutes les plateformes et très bien maintenu. Voir la [bibliographie][56] pour d'autres ressources.

Ce tutoriel explore différentes façons d'aborder un corpus de textes. Il est important de noter que les approches issues de la linguistique de corpus sont rarement, voire jamais, l'unique possibilité. Ainsi, à chaque étape, il vaut la peine de réfléchir à ce que vous faites et comment cela peut vous aider à répondre à une question spécifique avec vos données. Bien que je présente dans ce tutoriel une approche modulaire qui explique 'comment faire ceci puis cela pour atteindre x', il n'est pas toujours nécessaire de suivre l'ordre exact décrit ici. Cette leçon donne un aperçu de certaines des méthodes disponibles, plutôt qu'une recette du succès.

### Téléchargements nécessaires
1. Logiciel : [AntConc](http://www.laurenceanthony.net/software/antconc/).
Dézippez le fichier si nécessaire, et lancez l'application. Les captures d'écran ci-dessous peuvent varier légèrement par rapport à la version que vous avez (et selon le système d'exploitation, bien sûr), mais les procédures sont plus ou moins les mêmes sur les plateformes et les versions récentes d'AntConc. Ce tutoriel a recours à une version plus ancienne d'AntConc, car je la trouve plus facile à utiliser dans un contexte d'introduction. Vous pouvez utiliser la version la plus récente, mais si vous souhaitez suivre avec les captures d'écran fournies, vous pouvez télécharger la version utilisée ici, [version 3.2.4](http://www.laurenceanthony.net/software/antconc/releases/AntConc324/).

2. Corpus test : Téléchargez un [fichier zip de critiques de films](/assets/corpus-analysis-with-antconc/antconc_corpus_files.zip).

### Les grandes lignes de ce tutoriel :
1. Travailler avec des fichiers texte brut
2. L'interface utilisateur d'AntConc, importer un corpus
3. Recherche de mot-clé-en-contexte (_keyword-in-context_)
4. Fonctions avancées de mot-clé-en-contexte (_keyword-in-context_)
5. Cooccurrences et listes de mots
6. Comparer des corpus
7. Discussion : Faire des comparaisons significatives
8. Ressources supplémentaires


### Travailler avec des fichiers texte brut
* AntConc fonctionne avec des fichiers texte brut avec l'extension .txt (ex. : Hamlet.txt).
* AntConc **ne lira pas** les fichiers en .doc, .docx, .pdf. Vous allez devoir convertir ces fichiers en .txt.
* Il lira les fichiers XML qui sont enregistrés en tant que fichiers .txt (ce n'est pas grave si vous ne savez pas ce qu'est un fichier XML).

Visitez votre site Web d'actualités préféré, et cliquez sur un article (peu importe lequel, pourvu qu'il s'agisse principalement de texte). Sélectionnez tout le texte de l'article (en-tête, signature, etc.), et faites un clic droit sur "copier".

Ouvrez un éditeur de texte tel que Notepad (sous Windows) ou TextEdit (sous Mac) et collez votre texte.

D'autres options gratuites pour les éditeurs de texte, telles que [Notepad++][53] (Windows) ou [TextWrangler][54] (Mac), offrent des fonctionnalités plus avancées, et sont particulièrement utiles pour le nettoyage de texte. Par nettoyage de texte, j'entends la suppression des informations extratextuelles qui apparaissent régulièrement tout au long du texte. Si vous conservez cette information, elle va influencer vos données. Ainsi, les logiciels d'analyse de texte traiteront ces mots dans le compte de mots, les analyses statistiques et les relations lexicales. Par exemple, vous pouvez supprimer les en-têtes et pieds de page standards qui apparaîtront sur chaque page. Voir le tutoriel ["Nettoyer ses données avec OpenRefine"](/fr/lecons/nettoyer-ses-donnees-avec-openrefine) pour plus d'informations sur la façon d'automatiser cette tâche. Sur des corpus plus petits, il peut être plus facile de le faire vous-même, et vous aurez une bien meilleure idée de l'allure de votre corpus de cette façon.

Enregistrez l'article en tant que fichier .txt sur le bureau. Vous pouvez faire un petit nettoyage de texte pour enlever d'autres informations, telles que le titre ou l'auteur(e) (supprimez-les, puis enregistrez de nouveau le fichier). Rappelez-vous que tout ce que vous laissez dans le fichier peut et sera traité comme du texte par un logiciel d'analyse de texte.

Allez sur votre bureau et vérifiez que vous pouvez trouver votre fichier texte.

Répétez la procédure plusieurs fois et c'est ainsi que vous construirez un corpus de fichiers texte brut. Ce processus s'appelle la construction de corpus, ce qui implique très souvent d'aborder des questions d'échantillonnage, de représentativité et d'organisation. Rappelez-vous, *chaque fichier que vous voulez utiliser dans votre corpus __doit__ être un fichier texte brut pour qu'AntConc puisse l'utiliser.* Il est d'usage de nommer les fichiers avec le suffixe .txt pour que vous sachiez de quel type de fichier il s'agit.

Comme vous pouvez l'imaginer, il peut être assez fastidieux de constituer un corpus substantiel un fichier à la fois, surtout si vous avez l'intention de traiter un ensemble important de documents. Il est donc très courant d'utiliser l'extraction de contenus (_webscraping_) (en utilisant un petit programme pour télécharger automatiquement les fichiers sur le web pour vous) pour construire votre corpus. Pour en savoir plus sur les concepts et les techniques d'extraction, consultez les tutoriels du _Programming Historian_ sur l'[extraction avec Beautiful Soup][50] et le [téléchargement automatique avec wget][51] (en anglais).
Plutôt que de construire un corpus un document à la fois, nous allons utiliser un corpus préparé de critiques de films positives et négatives, emprunté au [_Natural Language Processing Toolkit_](http://www.nltk.org/). Le corpus des critiques de films de la NLTK compte 2000 critiques, organisées par résultats positifs et négatifs ; aujourd'hui, nous allons aborder un petit sous-ensemble d'entre eux (200 positifs, 200 négatifs).


La construction de corpus est un sous-domaine à part entière. Voir "[_Representativeness in Corpus Design_](https://academic.oup.com/dsh/article-abstract/8/4/243/928942)", _Literary and Linguistic Computing_, 8 (4) : 243-257 et [_Developing Linguistic Corpora : a Guide to Good Practice_](http://www.amazon.com/Developing-Linguistic-Corpora-Practice-Guides/dp/1842172050/ref=sr_1_1_1) pour plus d'informations.



### Premiers pas avec AntConc :  importer un corpus, l'interface utilisateur d'AntConc

Quand AntConc sera lancé, il ressemblera à ceci.
{% include figure.html filename="antconc1.png" caption="Écran d'ouverture d'AntConc." %}

Sur le côté gauche, il y a une colonne (_Corpus Files_) qui affiche les différents fichiers chargés (que nous allons utiliser dans un instant).

Il y a 7 onglets en haut:
**Concordance** _(Concordance)_: Cela vous montrera ce que l'on appelle la vue mot-clé en contexte (_KeyWord-In-Context_, abréviation KWIC, plus d'informations à ce sujet dans une minute), en utilisant la barre de recherche en dessous.
**Concordance Plot** _(Graphe des concordances)_: Ceci vous montrera une visualisation très simple de votre recherche KWIC, où chaque occurence du mot recherché sera représentée par une petite ligne noire du début à la fin de chaque fichier contenant le terme.
**File View** _(Vue de fichier)_: Cela vous montrera une vue complète du fichier, pratique pour voir le contexte plus large d'un résultat.
**Clusters** _(Grappes)_: Cette vue vous montre les mots qui apparaissent souvent ensemble.
**Collocates** _(Cooccurrences)_: Les clusters nous montrent des mots qui apparaissent _définitivement_ ensemble dans un corpus ; les cooccurrences (_collocates_) montrent des mots qui sont statistiquement susceptibles d'apparaître ensemble.
**Word List** _(Liste des mots)_: Tous les mots de votre corpus.
**Keyword List** _(Liste des mots-clés)_: Ceci permet des comparaisons entre deux corpus.

En guise d'introduction, ce tutoriel ne fait qu'effleurer la surface de ce que vous pouvez faire avec AntConc. Nous nous concentrerons sur les fonctions _Concordance_, _Collocates_, _Keywords_ et _Word List_.

#### Chargement des corpus

Comme pour ouvrir un fichier ailleurs, nous allons commencer par File > Open (Ouvrir > Fichier), mais au lieu d'ouvrir UN seul fichier, nous voulons ouvrir le répertoire de tous nos fichiers.  AntConc vous permet d'ouvrir des répertoires entiers, donc si vous êtes à l'aise avec ce concept, vous pouvez simplement ouvrir le dossier "_All review_" et passer à l'explication de l'interface, ci-dessous. Sinon, suivez les étapes suivantes.

{% include figure.html filename="open-file-21.png" caption="Ouvrir un répertoire de fichiers." %}

Rappelez-vous que nous avons mis nos fichiers sur le Bureau, alors naviguez dans le menu déroulant.
{% include figure.html filename="files-on-desktop-open.png" caption="Ouvrir un répertoire de fichiers sur votre Bureau." %}

Depuis le Bureau, vous voulez aller vers notre dossier "movie reviews from nltk" :
{% include figure.html filename="browse-for-directory-inside-folder.png" caption="Trouvez les critiques de films." %}

Sélectionnez d'abord "_Negative Review_" et cliquez sur OK. 200 textes devraient être chargés dans la colonne de gauche nommée _Corpus Files_ — regardez la case Total No. !
{% include figure.html filename="open-negative-reviews.png" caption="Importer les critiques négatives." %}

Ensuite, vous allez répéter le processus pour charger le dossier "_Positive Reviews_". Vous devriez maintenant avoir 400 textes dans la colonne _Corpus Files_.
{% include figure.html filename="positive-reviews.png" caption="Importer les critiques positives." %}

{% include figure.html filename="all-reviews-loaded.png" caption="Toutes les critiques importées." %}

## Recherche de mots-clés en contexte

### Commencez par une recherche de base
L'une des forces des outils de corpus comme AntConc, c'est de trouver des schémas de langage que nous avons du mal à identifier par une simple lecture. Les petits mots répétitifs comme *le, la, les, je, il, elle, un, une, avoir, être, faire* (*the, I, he, he, she, a, a, an, is, have, will*) sont particulièrement difficiles à suivre, parce qu'ils sont très communs, mais les ordinateurs sont très doués pour accomplir la tâche. Ces mots sont communément connus sous le nom de "mots vides" (_stopwords_) en humanités numériques ; ce sont souvent des marques caractéristiques d'un(e) auteur(e) ou d'un genre. Par conséquent, ils peuvent être des termes de recherche très puissants en eux-mêmes ou combinés à des termes plus axés sur le contenu, ce qui aide les chercheurs et chercheuses à identifier des tendances qui n'avaient peut-être pas été répérées.


Dans le champ de recherche en bas, tapez "_the_" et cliquez sur "start" (démarrer). La vue Concordance vous montrera chaque fois que le mot apparaît dans notre corpus de critiques de films, et un certain contexte pour cela. C'est ce qu'on appelle une visionneuse "mots-clés en contexte" (_Key Words in Context_).

{% include figure.html filename="the-thinking.png" caption="'_The_' est un mot commun." %}


(14618 fois, selon la case "_Concordance Hits_" en bas au centre qui indique le nombre d'occurrences.)

Comme ci-dessus, la liste KWIC est un bon moyen de commencer à chercher des schémas récurrents. Même s'il y a encore beaucoup d'informations, quels sont les mots qui apparaissent à proximité de "_the_" ?


Essayez une recherche similaire pour "_a_". Les deux "_a_" et "_the_" sont des articles, mais l'un est un article défini et l'autre un article indéfini - et les résultats que vous obtiendrez vous en donneront une idée.


Maintenant que vous êtes à l'aise avec une ligne KWIC, recommencez avec le mot "_shot_" : vous obtiendrez des exemples à la fois du nom ("_line up the **shot**_") et du verbe ("_this scene was **shot** carefully_").

Que voyez-vous ? Je comprends que cela peut être difficille d'identifier des schémas. Essayez d'appuyer sur le bouton jaune "_sort_" (trier). Que se passe-t-il maintenant ?


{% include figure.html filename="sorting-shot-1l1r.png" caption="Les mots qui apparaissent près de '_shot_'." %}


(Ceci est peut-être plus facile à lire !)
Vous pouvez ajuster la façon dont AntConc trie les informations en modifiant les paramètres dans le cercle rouge : L correspond à 'gauche' (pour _left_) et R à 'droite' (pour _right_) ; vous pouvez les étendre jusqu'à ±5 dans les deux sens. La valeur par défaut est 1 gauche, 2 droite, 3 droite, mais vous pouvez changer cela pour rechercher 3 gauche, 2 gauche, 1 droite (pour obtenir des phrases et/ou des trigrammes qui se terminent avec le terme qui vous intéresse, par exemple) en cliquant sur les boutons flèches haut ou bas. Si vous ne voulez pas inclure une option de tri, vous pouvez l'ignorer (comme par défaut : 1L, 2R, 3R) ou l'inclure comme un 0. Des options de tri moins linéaire sont disponibles, telles que 4 gauche, 3 droite, 5 droite, qui comprend beaucoup d'autres informations contextuelles. Ces paramètres peuvent être lents à réagir, mais soyez patients. Si vous n'êtes pas sûr(e) du résultat de la recherche, appuyez simplement sur "_sort_" (trier) pour voir ce qui s'est passé et ajuster en conséquence.


### Opérateurs de recherche

#### L'opérateur * (métacaractère)
L'opérateur * (qui trouve zéro ou plus de caractères) peut aider, par exemple, à trouver les formes singulière et plurielle des noms.

**Exercice :**
Recherchez "qualit*", puis triez cette recherche. Qu'est-ce qui tend à précéder et à suivre la _quality_ (qualité) et les _qualities_ (qualités) ? (Indice : en anglais, ce sont des mots différents, et ils ont des contextes différents. Encore une fois, recherchez les modèles d'utilisation à l'aide du KWIC !)


Pour obtenir la liste complète des opérateurs de replacement disponibles et ce qu'ils signifient, allez à _Global Settings_ > _Wildcard Settings_  (Paramètres globaux > Paramètres des métacaractères)
{% include figure.html filename="wildcard-settings.png" caption="Réglage des paramètres des métacaractères." %}

Pour connaître la différence entre * et ?, recherchez "_th*n_" et "_th?n_". Ces deux requêtes de recherche se ressemblent beaucoup, mais donnent des résultats très différents.


L'opérateur ? est plus spécifique que l'opérateur * :
"_wom?n+_" - à la fois "_woman_" (femme) et "_women_" (femmes)
"_m?n_" - "_man_" (homme) et "_men_" (hommes), mais aussi "_min_"
comparativement "_m*n_" n'est pas utile, parce que vous allez avoir "_mean_", "_melon_", etc.



**Exercice :**
Comparez ces deux recherches : "_wom?n_" et "_m?n_"
1. Triez chaque recherche de façon significative (par exemple par terme de recherche puis 1L puis 2L)
2. Puis, cliquez sur _File_ > _Save output to text file_ (Enregistrer les résultats dans un fichier texte)

>ASTUCE : Au cours de vos recherches, vous pouvez générer de nombreux fichiers de ce type pour référence ; il est utile d'utiliser des noms de fichiers clairs qui décrivent ce qu'ils contiennent (tels que "wom?n-results.text", et non "antconc_results.txt").

{% include figure.html filename="save-output-as-text-file.png" caption="Enregistrer les résultats dans un fichier texte" %}

{% include figure.html filename="save-as.png" caption="Fenêtre Enregistrer sous." %}

Et maintenant vous pouvez ouvrir le fichier texte dans votre éditeur de texte ; vous devrez peut-être élargir la fenêtre de l'application pour la rendre lisible :
{% include figure.html filename="results.png" caption="Le fichier texte brut affiché dans un éditeur de texte." %}


Effectuez cette opération pour chacune des deux recherches, puis examinez les deux fichiers texte côte à côte. Qu'est-ce que vous remarquez ?



#### L'opérateur | ("ou")

**Exercice:**
Recherchez  "_she|he_".

Maintenant, recherchez-les séparément : combien d'occurences "_she_" comparé à "_he_" ?

Il y a beaucoup moins de cas de "_she_"- pourquoi ? C'est une question de recherche ! Une bonne question de suivi pourrait être de trier la recherche "_she|he_" et de voir si des verbes particuliers suivent chacun d'eux.


**Exercice :**
Entraînez-vous à rechercher un mot de votre choix, à le trier de différentes façons, à utiliser des métacaractères et enfin à exporter les résultats. La question centrale à se poser ici : quels types de modèles voyez-vous ? Pouvez-vous les expliquer ?


### Cooccurrences (_collocates_) et listes des mots (_word lists_)
Après avoir regardé les lignes KWIC à la recherche de schémas, n'aimeriez-vous pas que l'ordinateur puisse vous donner une liste des mots qui apparaissent le plus souvent en compagnie de votre mot-clé ?

Bonne nouvelle, il y a un moyen d'obtenir cette information, et elle est disponible dans l'onglet _Collocates_ (Cooccurrences). Cliquez dessus, et AntConc vous dira qu'il doit créer une liste de mots. Appuyez sur OK ; il le fera automatiquement.


> REMARQUE : Vous n'obtiendrez cet avis que si vous n'avez pas encore créé de liste de mots.
{% include figure.html filename="wordlistwarning.png" caption="Avertissement liste de mots." %}

Essayez de générer des coooccurrences pour "_she_"


Les résultats non triés sembleront commencer par des mots vides (mots qui construisent des phrases) puis descendre jusqu'aux mots de contenu (mots qui construisent du sens). Les mots vides sont ces petits mots ennuyeux, [les mots les plus fréquents en anglais][55], qui sont pour la plupart des créateurs de phrases. Les versions ultérieures d'AntConc incluent souvent le terme de recherche comme premier résultat, probablement parce que le terme de recherche que vous recherchez apparaît dans le texte et nous recherchons des mots qui sont susceptibles d'apparaître avec ce mot.

Certaines personnes voudront peut-être supprimer ces petits mots à l'aide d'une liste de mots vides (_stopword list_) ; c'est une étape courante dans la modélisation thématique (_topic modelling_).  Personnellement, je n'encourage pas cette pratique parce qu'examiner les mots très fréquents est justement la force des ordinateurs ! La lecture humaine a  tendance à ne pas les remarquer beaucoup. Mais les ordinateurs, en particulier les logiciels comme AntConc, peuvent nous montrer où ces mots apparaissent et où ils n'apparaissent pas, ce qui peut être très intéressant, surtout dans de très grandes collections de textes - comme nous l'avons vu précédemment dans le tutoriel, avec *the*, *a*, *she* et *he*.

De plus, dans les corpus en anglais, il se peut qu'une seule lettre *s* apparaisse, placée assez haute également - qui représente les *'s* possessifs (l'apostrophe ne sera pas comptée), mais AntConc considère qu'il s'agit d'un autre mot. Un autre exemple de ceci est *'t* apparaissant avec *do*, car ils se contractent comme *don't*. Comme ils apparaissent si souvent ensemble, il est fort probable qu'ils soient colocalisés.


**Exercice :**
Générez des cooccurrences pour "_m?n_" et "_wom?n_". Maintenant, triez-les par fréquence jusqu'à 1L.
Cela nous renseigne sur ce qui rend un homme ou une femme digne d'être vu(e) au cinéma " :
- les femmes doivent être "belles" ou "enceintes" ou "sophistiquées".
- les hommes doivent être en quelque sorte hors norme - "saints" ou "noirs" ou "vieux ".


Ceci ne nous dit pas grand-chose sur les films en eux-mêmes, mais plutôt sur la façon dont ces films sont décrits dans les critiques, et cela peut nous amener à poser des questions plus nuancées, comme "Comment les femmes dans les comédies romantiques sont-elles décrites dans les critiques écrites par des hommes comparativement à celles écrites par des femmes ?"



### Comparer des corpus
L'un des types d'analyse les plus intéressant consiste à comparer votre corpus à un corpus de référence plus volumineux.


J'ai sélectionné des critiques de films auxquels Steven Spielberg est associé (en tant que réalisateur ou producteur). On peut les comparer à un corpus de référence de films de différents réalisateurs.

Réfléchissez bien à ce à quoi pourrait ressembler un corpus de référence pour votre propre recherche (par exemple, une étude des écrits d'Agatha Christie dans ses dernières années serait très utile comme corpus d'analyse pour la comparaison avec un corpus de référence constitué de tous ses romans). Rappelez-vous, encore une fois, que la construction de corpus est un sous-domaine à part entière.


Allez dans _Settings_ > _Tool preferences_ > _Keyword List_ (Paramètres > Options des outils > Liste des mots-clés).
Sous "_Reference Corpus_" (Corpus de référence) assurez vous que "_Use raw files_" (Utiliser des fichiers bruts) est coché.
Puis, cliquez sur _Add Directory_ > _Open_ (Ajouter répertoire > Ouvrir) pour ouvrir le répertoire contenant les fichiers qui composent le corpus de référence.
Assurez-vous d'avoir une liste complète de fichiers !

{% include figure.html filename="adding-a-reference-corpus.png" caption="Ajouter un corpus de référence." %}

Cliquez sur "_Load_" (Charger), attendez et une fois que la boite "_Loaded_" (Chargé) est cochée, appuyez sur "_Apply_" (Appliquer).
Vous pouvez également opter pour l'échange de corpus de référence et de fichiers principaux (_Swap Ref/Main files_). Il vaut la peine de regarder ce que les deux résultats montrent.

> Si vous utilisez une version plus récente d'AntConc, l'option Swap Ref/Main files peut être marquée comme "swap with target files", et vous devrez vous assurer que les corpus cible et de référence ont été chargés (appuyez sur le bouton "Load" à chaque fois que vous téléchargez, ou échangez, un corpus).


Dans _Keyword List_ (Liste des mots-clés), appuyez simplement sur "_Start_" (Démarrer) (sans rien taper dans le champ de recherche). Si vous venez de changer le corpus de référence et les fichiers cibles, il se peut qu'on vous demande de créer une nouvelle liste de mots avant qu'AntConc ne calcule les mots-clés. Nous voyons une liste de mots-clés qui ont des mots qui sont beaucoup plus "inhabituels" - plus statistiquement inattendus - dans le corpus que nous regardons en comparaison avec le corpus de référence.

> Keyness (spécificité) : c'est la fréquence d'un mot dans le texte par rapport à sa fréquence dans un corpus de référence, "telle que la probabilité statistique calculée par une procédure appropriée soit inférieure ou égale à une valeur p indiquée par l'utilisateur" (tiré d'[ici][41]). Pour ceux et celles qui s'intéressent aux détails statistiques, voir la section sur la spécificité (Keyness) à la page 7 du [fichier read me](http://www.laurenceanthony.net/software/antconc/releases/AntConc335/help.pdf) de Laurence Anthony.



Quels sont nos mots-clés ?

{% include figure.html filename="spielberg-vs-movie-reviews.png" caption="Spielberg vs critiques de films." %}


## Discussion : Faire des comparaisons significatives
Gardez à l'esprit que la façon dont vous organisez vos fichiers textes fait une différence entre les types de questions que vous pouvez poser et les types de résultats que vous obtiendrez.  N'oubliez pas que nous comparons ici les critiques "négatives" et "positives" de manière assez simpliste. Vous pourriez, par exemple, faire d'autres comparaisons avec différents sous-ensembles, qui donnent lieu à des questions de nature très différente.

Bien sûr, les fichiers que vous mettez dans votre corpus façonneront vos résultats. Là encore, la question de la représentativité et de l'échantillonnage est très pertinente - il n'est pas toujours nécessaire ou même idéal d'utiliser *tous* les ensembles de données en même temps, même si vous les avez. À ce stade, il vaut vraiment la peine de s'interroger sur la façon dont ces méthodes aident à produire des questions de recherche.

Lorsque vous réfléchissez à la façon dont les critiques de films fonctionnent en tant que genre, vous pourriez envisager, par exemple....

* Critiques de films vs critiques de musique
* Critiques de films vs critiques de livres
* Critiques de films vs actualités sur le sport
* Critiques de films vs actualités en général

Chacune de ces comparaisons vous dira quelque chose de différent, et peut produire différentes questions de recherche, telles que :

* En quoi les critiques de films sont-elles différentes des autres types de critiques de médias ?
* En quoi les critiques de films sont-elles différentes des autres types d'écrits publiés ?
* Comment les critiques de films se comparent-elles à d'autres types spécifiques d'écriture, comme l'écriture sportive ?
* Quel est le point commun entre les critiques de films et les critiques de musique ?

Et bien sûr, vous pouvez retourner ces questions pour faire d'autres questions de recherche :

* En quoi les critiques de livres sont-elles différentes des critiques de films ?
* En quoi les critiques musicales sont-elles différentes des critiques de films ?
* Qu'est-ce que les articles de journaux publiés ont en commun ?
* Comment les critiques de films sont-elles similaires à d'autres types d'écrits publiés ?

En résumé, il vaut la peine de réfléchir :

* Pourquoi vous voudrez comparer deux corpus ?
* Quels sont les types de requêtes qui rendent les questions de recherche pertinentes ?
* Aux principes de construction de corpus : échantillonnage et s'assurer que vous pouvez obtenir quelque chose de représentatif



-----

## Ressources supplémentaires pour ce tutoriel
#### En anglais
[Une courte bibliographie sur la linguistique des corpus][43].  
[Une version plus détaillée de ce tutoriel, en supposant que vous n'avez aucune connaissance en informatique.](http://hfroehli.ch/workshops/getting-started-with-antconc/)  

#### En français (notes de la version traduite)
[Page AntConc de EduTech Wiki de l'UNIGE](http://edutechwiki.unige.ch/fr/AntConc#)    
[Page AntConc sur le site Exploration de corpus : outils et pratiques](http://explorationdecorpus.corpusecrits.huma-num.fr/antconc/)    
[Tutoriel AntConc du CID-ENS Lyon](http://cid.ens-lyon.fr/ac_article.asp?fic=antconc.asp)    

En France, des outils similaires à AntConc ont été dévéloppés dans le cadre de la textométrie, de la lexicométrie, et de la logométrie, souvent par des historien(ne)s. On peut nommer notamment [Hyperbase](http://ancilla.unice.fr/), [Iramuteq](http://iramuteq.org/), [Lexico](http://www.lexi-co.com/) ou [TXM](http://textometrie.ens-lyon.fr/?lang=fr). Merci de consulter également: Bénédicte Pincemin, ["Sept logiciels de textométrie"](https://halshs.archives-ouvertes.fr/halshs-01843695/document), 2018.  

#### Bibliographie non-exhaustive

Ludovic Lebart et André Salem, [*Statistique textuelle*](http://lexicometrica.univ-paris3.fr/livre/st94/st94-tdm.html), 1994.    
Damon Mayaffre, ["L’entrelacement lexical des textes. Cooccurrences et lexicométrie"](https://hal.archives-ouvertes.fr/hal-00553808), _Journées de linguistique de corpus_, 2008, p. 91-102.  
[La cooccurrence, du fait statistique au fait textuel](https://journals.openedition.org/corpus/2183), _Corpus_, 11, 2012, numéro coordonné par Damon Mayaffre et Jean-Marie Viprey.  

[41]: http://www.lexically.net/downloads/version6/HTML/index.html?keyness_definition.htm
[43]: http://hfroehlich.wordpress.com/2014/05/11/intro-bibliography-corpus-linguistics/
[47]: http://hfroehli.ch/workshops/getting-started-with-antconc/
[48]: http://voyant-tools.org/
[50]: /en/lessons/intro-to-beautiful-soup
[51]: /en/lessons/automated-downloading-with-wget
[52]: http://www.antlab.sci.waseda.ac.jp/
[53]: http://notepad-plus-plus.org/
[54]: http://www.barebones.com/products/textwrangler/
[55]: http://www.wordfrequency.info/free.asp
[56]: http://hfroehli.ch/2014/05/11/intro-bibliography-corpus-linguistics/
