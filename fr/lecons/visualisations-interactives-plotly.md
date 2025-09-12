---
title: "Créer des visualisations interactives avec Plotly"
slug: visualisations-interactives-plotly
original: interactive-visualization-with-plotly
layout: lesson
collection: lessons
date: 2023-12-13
translation_date: YYYY-MM-DD
authors:
- Grace Di Méo
reviewers:
- Mario Bañuelos
- Rob Lewis
editors:
- Scott Kleinman
translator:
- Axel Morin
translation-editor:
- Émilien Schultz
translation-reviewer:
- Paul Guille-Escuret
- Daniela Boaventura
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/651
difficulty: 2
activity: presenting
topics: [python, data-visualization]
abstract: Cette leçon montre comment créer des visualisations de données interactives avec la bibliothèque &laquo;&nbsp;open source&nbsp;&raquo; Plotly. Le jeu de données utilisé provient du ministère de l'éducation nationale, et comptabilise le nombre de personnes admises aux différents baccalauréats.
avatar_alt: Dessin en noir et blanc d'un cygne contemplant son reflet dans l'eau.
mathjax: true
doi: XX.XXXXX/phen0000
---

{% include toc.html %}

## Introduction

### Objectifs de la leçon

Cette leçon montre comment créer des visualisations de données interactives avec la bibliothèque &laquo;&nbsp;[open source](https://perma.cc/W9G9-NW96)&nbsp;&raquo; Plotly. En particulier, vous apprendrez&nbsp;:

- La différence entre les modules Plotly Express, Plotly Graph Objects et Plotly Dash.
- Comment créer et exporter des visualisations à l'aide des modules Plotly Express et Plotly Graph Objects.
- Comment personnaliser vos visualisations.

### Les prérequis

Afin de pouvoir suivre la leçon, il est nécessaire d'avoir&nbsp;:

- Installé [Python 3 (version `3.13.2`)](https://docs.python.org/3/) et le [gestionnaire de paquets (&laquo;&nbsp;package&nbsp;&raquo;) `pip` (version `25.1)`](https://perma.cc/L34R-HC8R).
- Un niveau de compréhension intermédiaire du langage de programmation Python.
- Une connaissance générale des bibliothèques [Pandas (version `2.2.3`)](https://pandas.pydata.org/docs/) et [Numpy (version `2.2.5`)](https://numpy.org/doc/stable/) (ces deux bibliothèques doivent être installées).
- Une connaissance de quelques techniques de base en visualisation de données (en particulier les histogrammes, les diagrammes en barres et les nuages de points).
- Des notions de traitement des données (nous utiliserons Pandas).

### Qu'est ce que Plotly&nbsp;? 

Plotly est une société qui fournit un certain nombre de modules open source permettant aux utilisateur·rice·s de construire des visualisations interactives. Contrairement à des images statiques, les visualisations réalisées avec Plotly offrent ainsi des outils/boutons pour se déplacer, zoomer et bien plus encore. La bibliothèque Plotly est disponible en Python&nbsp;- le sujet de cette leçon&nbsp;- ainsi que dans d'autres langages de programmation comme R et Julia.[^1] Les modules de Plotly permettent de réaliser une large variété de visualisations, que ce soit à des fins statistiques, scientifiques, financières ou géographiques. Ces visualisations peuvent être affichées de plusieurs manières&nbsp;: à travers des notebooks Jupyter, des pages web (HTML) ou dans des applications web développées avec l'environnement Dash de Plotly. Il est aussi possible d'exporter les visualisations sous forme d'images statiques (non interactives) en pixels (&laquo;&nbsp;raster&nbsp;&raquo;) ou vectorielles.

<div class="alert alert-info">
Tout le long de cette leçon, les visualisations générées à l'aide de Plotly seront affichées comme des images statiques. Pour utiliser les fonctionnalités interactives il faudra cliquer sur l'image ou bien sur le lien dans la description de l'image.
</div>

### Plotly, une bibliothèque Graphique de Python&nbsp;: Plotly Express vs Plotly Graph Objects vs Plotly Dash

Afin de comprendre comment utiliser Plotly, il est fondamental de comprendre les différences entre Plotly Express, Plotly Graph Objects et Plotly Dash.

Il s'agit essentiellement de 3 modules distincts&nbsp;- dont les fonctionnalités peuvent se superposer - qui ont leurs propres objectifs&nbsp;:

- Plotly Express (`plotly.express` souvent importé avec l'alias `px`) est une interface de représentation graphique &laquo;&nbsp;de haut niveau&nbsp;&raquo;, facile à prendre en main, et qui permet de créer près de 30 types différents de représentations. Le module fournit des fonctions permettant de créer des visualisations avec une seule ligne de code (bien que plusieurs lignes de code soient nécessaires à la personnalisation de certains éléments), rendant les visualisations rapides et faciles à créer. Puisque `plotly.px` est une interface de haut niveau, cela signifie que l’utilisateur·rice n’a pas besoin de s'attarder sur la structure sous-jacente des visualisations. Plotly recommande aux débutant·e·s de commencer avec Express avant de travailler avec Plotly Graph Objects.
- Les objets graphiques de Plotly&nbsp;- associés aux module Plotly Graph Objects (`plotly.graph_objects` souvent importé avec l'alias `go`) sont les véritables objets que Plotly créé lorsque l'on fait appel à Plotly Express. Plotly génère des `plotly.graph_objs` pour garder en mémoire les données de la visualisation. Ces données incluent les informations à visualiser avec de nombreux autres attributs telles que les couleurs, formes et tailles des objets. Il est alors possible de créer une visualisation plus finement avec Plotly Graph Objects. Il est d'ailleurs possible de recréer n'importe quelle figure créée par Plotly Express à l'aide de Plotly Graph Objects. Il est en général recommandé d’utiliser Plotly Express pour réduire le nombre de lignes de code mais, comme nous le verrons par la suite, certaines visualisations imposent de passer par Plotly Graph Objects.
- Le module Plotly Dash (importé avec l'alias `dash`) est un environnement pour créer des applications web interactives (typiquement des &laquo;&nbsp;dashboards&nbsp;&raquo;) qui peuvent être incrustées dans des sites web et autres plateformes. On ajoute souvent des figures créées avec Express ou Graph Objects dans les applications Dash, faisant des modules de Plotly la boîte à outils parfaite pour créer, manipuler et publier des représentations graphiques interactives de nos données. Plotly Dash est construit sur `React.js` et `Plotly.js` afin de rendre possible l'intégration sur internet, cela signifie que les utilisateur·rice·s n'ont pas besoin de connaissances en Javascript, CSS ou HTML (seulement en Python).

Plotly fournit une documentation complète pour travailler avec Express et Graph Objects ainsi que pour utiliser Dash.[^2]

### Pourquoi Plotly&nbsp;? 

Il existe actuellement une pléthore de bibliothèques graphiques sous Python comme Matplotlib, Seaborn, Bokeh ou Pygal. Chaque bibliothèque présente des avantages. Le cas d'utilisation, les goûts esthétiques ou la facilité d'utilisation, sont tous des critères qui permettent de choisir une bibliothèque. Les avantages principaux de Plotly sont&nbsp;:

- Plotly est l'une des seules bibliothèques spécifiquement tournée vers les représentations interactives. Matplotlib et Pygal ne fournissent que très peu de fonctionnalités interactives. Bokeh[^3] est aussi prévu pour l'interactivité et se présente comme une alternative viable.
- Plotly est la seule bibliothèque de Python qui assure à la fois une création de visualisations et une intégration dans des pages web simple.
- Plotly intègre parfaitement les objets de Pandas (par exemple, on peut directement passer des `pandas.DataFrame` aux objets graphiques de Plotly).
- Des visualisations 3D interactives sont disponibles (ce qui n'est pas le cas des autres bibliothèques).
- Plotly, ses animations et ses menus déroulants sont simples d’utilisation.

## Données utilisées comme exemple 

<div class="alert alert-info">
Note&nbsp;: Le jeu de données original de la leçon portait sur les homicides à Philadelphie (USA) (<a href="/en/lessons/interactive-visualization-with-plotly#sample-dataset">cf. section de l'article original</a>). Pour cette traduction, il a été choisi d'adapter le jeu de données au contexte francophone.
</div>

Le jeu de données utilisé pour cette leçon est issu du site de données publiques françaises [data.gouv.fr](https://www.data.gouv.fr) et agrégées par le [Ministère de l'Éducation Nationale](https://www.education.gouv.fr/). Le jeu de données rassemble le nombre d'admissions au baccalauréat (général, technologique, professionnel et tout baccalauréat confondu) en France, pour chaque origine sociale, et ce entre 1997 et 2024. Pour faciliter le déroulement de la leçon, des erreurs de codage de données ont été corrigées et une transformation des donnés a été réalisée pour limiter les manipulations dans la leçon. Le jeu de données original est disponible sur [la page de data.gouv.fr](https://www.data.gouv.fr/fr/datasets/reussite-au-baccalaureat-selon-lorigine-sociale/#/resources) mais, pour cette leçon, il vous faudra utiliser le jeu de données corrigé, téléchargeable directement depuis le dépôt GitHub de _Programming Historian_ ([data_article.csv](/assets/visualisations-interactives-plotly/data_article.csv)). Vous pourrez aussi y trouver le traitement réalisé ([data_cleaning.py](/assets/visualisations-interactives-plotly/data_cleaning.py)), ainsi qu'une compilation du code utilisé pour générer les figures au cours de cette leçon ([article_routine.py](/assets/visualisations-interactives-plotly/article_routine.py)).

## Construire des visualisations avec Plotly Express

### Configurer Plotly Express

1. Avant de commencer, vous aurez besoin d'installer 3 bibliothèques dans votre environnement.[^4]
	- Plotly (version `6.0.1`)&nbsp;: dans votre terminal, entrez `pip install plotly`.
	- Pandas (version `2.2.3`)&nbsp;: dans votre terminal entrez `pip install pandas`.[^5]
	- Kaleido (version `0.2.1`)&nbsp;: dans votre terminal entrez `pip install kaleido`.[^6]
2. Maintenant que ces bibliothèques sont installées, créez un nouveau Jupyter notebook (ou un nouveau fichier Python dans votre logiciel d'édition de code). Idéalement, placez votre jeu de données et votre fichier Python/notebook dans le même dossier. Nous avons également préparé un notebook contenant l'intégralité du code présenté dans cette leçon, que vous pouvez télécharger depuis le dépôt de _Programming Historian_ ([visualisations-interactives-plotly.ipynb](https://nbviewer.org/github/programminghistorian/jekyll/blob/gh-pages/assets/visualisations-interactives-plotly/visualisations-interactives-plotly.ipynb)).
3. Importez les modules à l'aide de la commande `import` au début de votre fichier&nbsp;: 

```python
import numpy as np
import pandas as pd
import plotly.express as px
```

### Importer et nettoyer les données

La prochaine étape est d'importer le jeu de données et de le nettoyer à l'aide des fonctions de Pandas. Les étapes à réaliser sont&nbsp;:

- Importer uniquement les colonnes du jeu de données qui nous seront utiles.
- Remplacer certains champs par des champs plus courts.

```python
colonnes = ["Année","Origine sociale","Nombre de personnes admises",
    "Proportion de personnes admises","Type de baccalauréat"]

df : pd.DataFrame = pd.read_csv("data_article.csv",usecols = colonnes)

# On raccourcit le nom de chaque colonne
nouvelles_colonnes = {
    "Année" : "annee",
    "Origine sociale" : "origine_sociale",
    "Nombre de personnes admises" : "n_admis",
    "Proportion de personnes admises" : "p_admis",
    "Type de baccalauréat" : "type"
}
df.rename(nouvelles_colonnes, axis = 1, inplace = True)

# On raccourcit le nom de certaines origines sociales pour alléger les visualisations
df["origine_sociale"] = df["origine_sociale"].replace({
    "Professions intermédiaires" : "P. intermédiaires",
    "Cadres, professions intellectuelles supérieures" : "Cadres",
    "Autres personnes sans activité professionnelle" : "Sans activité p.",
    "Artisans, commerçants, chefs d'entreprise" : "Indépendants",
    "Agriculteurs exploitants" : "Agriculteurs",
})

# On raccourcit le nom des types de bacs
df["type"] = df["type"].replace({
    "baccalaureat général" : "bac_g",
    "baccalauréat technologique" : "bac_t",
    "baccalauréat professionnel" : "bac_p",
    "baccalauréat" : "bac_tous",
})

# On supprime les lignes associées aux origines sociales que l'on souhaite écarter 
# pour cette leçon.
df.drop(df[
        (df["origine_sociale"] == "Ensemble") | \
        (df["origine_sociale"] == "Indéterminé") 
    ].index, inplace = True)
```

### Diagrammes en barres

Maintenant que nous avons créé un DataFrame Pandas de notre jeu de données, nous pouvons commencer à créer quelques visualisations simples en utilisant Plotly Express. Commençons par créer un diagramme en barres pour représenter le nombre de personnes admises au baccalauréat (tous types confondus) en 2024 selon leur origine sociale. Puisque notre jeu de données contient déjà ces données, il nous suffit de selectionner une sous-partie de notre jeu de données entier.

```python
# Création d'un nouveau DataFrame
num_admis_par_origine_sociale_2024 = df.loc[
    (df["annee"] == 2024)&(df["type"] == "bac_tous"), ["origine_sociale", "n_admis"]
]
print(num_admis_par_origine_sociale_2024)
```

||origine_sociale|n_admis|
|-|--------------|-------|
|27|        Agriculteurs|    6402|
|55|        Indépendants|   50109|
|83|    Sans activité p.|   64691|
|111|             Cadres|  187632|
|139|           Employés|  146115|
|167|           Ouvriers|   80884|
|195|  P. intermédiaires|  117017|
|223|          Retraités|    7592|

Il suffit alors de créer un diagramme en barres en utilisant ce nouveau DataFrame. Remarquons que cette visualisation est sauvegardée dans la variable `fig`, qui est une convention lorsqu'on travaille avec Plotly&nbsp;:

```python
# Créer le diagramme en barres (bar chart) en utilisant la fonction .bar()
fig = px.bar(num_admis_par_origine_sociale_2024, x = "origine_sociale", y = "n_admis")

# Affiche la figure en utilisant la méthode .show()
fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-01.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-01.png" alt="Diagramme en barres représentant, sur l'axe des abscisses, 8 origines sociales (parmi lesquelles on retrouve les Agriculteurs, Cadres, Indépendants et les Ouvriers) et sur l'axe des ordonnées le nombre de personnes admises au baccalauréat en 2024 (tous types confondus), le nombre d'admis varie entre 6k et 200k.">
	</a>
<figcaption>
    <p>Figure 1. Un diagramme en barres avec une interactivité simple en utilisant Plotly Express. Si les lecteur·rice·s survolent les barres, on peut y voir apparaître des boîtes flottantes. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-01.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

Vous venez de créer votre première visualisation&nbsp;! Remarquons que cette visualisation est déjà en partie interactive&nbsp;: en passant la souris sur chaque barre, nous pouvons voir l'origine sociale de la catégorie et le nombre de personnes qui la compose. Une autre fonctionnalité notable est que l'utilisateur·rice peut sauvegarder la visualisation comme un `.png` (image statique) en cliquant sur l'icône appareil photo qui apparaît lorsque la souris se trouve dans le coin haut droit de l'image. Au même endroit on peut trouver des fonctions de zoom, défilement, changement d'échelle et réinitialiser la vue. Ces fonctionnalités seront disponibles pour toutes les visualisations.

En revanche, la visualisation n'est pas des plus agréable, elle manque de couleurs, d'un titre et de titres d'axes plus visibles. Il est possible de préciser ces informations dès le début, en donnant plus d'arguments à la fonction `.bar()`. Par exemple, grâce à l'argument `labels` nous pouvons changer le nom des axes et grâce à l'argument `color` on peut changer la couleur des barres selon une variable de notre jeu de données (ici nous utiliserons &laquo;&nbsp;Nombre de personnes admises au baccalauréat&nbsp;&raquo; pour l'axe vertical). Pour ajouter un titre, il suffit d'utiliser l'argument `title`&nbsp;:

```python
# Créer un diagramme en barres en utilisant la fonction .bar()
fig = px.bar(
    num_admis_par_origine_sociale_2024,
    x="origine_sociale",
    y="n_admis",
    title="Titre de votre choix",
    labels={"n_admis": "Nombre de personnes admises au baccalauréat"},

    # Notez que l'argument "color" prend une chaîne de caractères se référant à 
    # la colonne "origine_sociale" du jeu de données
    color="origine_sociale"
)

fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-02.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-02.png" alt="Diagramme en barres représentant, sur l'axe des abscisses, 8 origines sociales (parmi lesquelles on retrouve les Agriculteurs, Cadres, Indépendants et les Ouvriers) et sur l'axe des ordonnées le nombre de personnes admises au baccalauréat en 2024 (tous types confondus), le nombre d'admis varie entre 6k et 200k. Chaque barre est d'une couleur différente et décrite dans une légende.">
	</a>
<figcaption>
    <p>Figure 2. Un diagramme en barres avec une interactivité simple en utilisant Plotly Express. Cette visualisation est une variante de la Figure 1 avec cette fois-ci des couleurs et une légende interactive qui permet aux lecteur·rice·s d'isoler ou bien de retirer certaines barres. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-02.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

Comme montré ci-dessus, Plotly ajoute automatiquement une légende à la visualisation si vous distinguez les objets par des couleurs (à savoir que la légende peut être retirée). La légende est elle aussi interactive&nbsp;: en cliquant une fois sur un élément, la barre correspondante disparaît de la visualisation&nbsp;; en double-cliquant sur un élément, cette fois-ci tous les autres objets disparaissent excepté celui que vous avez sélectionné.

### Courbes

Tâchons maintenant de créer une courbe (&laquo;&nbsp;line chart&nbsp;&raquo;). De manière générale, la syntaxe pour créer une visualisation avec Plotly Express est toujours `px.type_de_representation()` où `type_de_representation` désigne le type de représentation que l'on souhaite créer. Comme on a utilisé `px.bar()` pour créer un diagramme en barres (&laquo;&nbsp;bar chart&nbsp;&raquo;), ici nous utiliserons `px.line()` pour créer un &laquo;&nbsp;line chart&nbsp;&raquo;. Tous les types de représentations disponibles et les fonctions associées peuvent être trouvées dans la [documentation Plotly](https://perma.cc/U4N7-2VM5).

Notre courbe représentera l'évolution de la proportion de personnes admises au baccalauréat (tous types confondus) par origine sociale à travers les années. Comme précédemment, nous sélectionnons une partie de notre jeu de données&nbsp;:

```python
# Créer un nouveau DataFrame contenant le pourcentage d'admis au 
# baccalauréat (tous types confondus) par origine sociale et par année
prop_admis_par_origine_sociale_par_annee = df.loc[
    df["type"] == "bac_tous", ["annee", "origine_sociale", "p_admis"]
]
```

Ensuite, nous créons plusieurs courbes en utilisant la fonction `.line()` et utilisons les mêmes paramètres que précédemment à savoir&nbsp;: `label` et `color`. Ici encore il est possible d'ajouter un titre à notre figure, il suffit de retirer le `#` devant l'argument `title` dans l'exemple suivant (et tous ceux qui suivent)&nbsp;:

```python
# Créer des courbes avec la fonction px.line() et ajouter quelques éléments de 
# personnalisation
fig = px.line(
    prop_admis_par_origine_sociale_par_annee,
    x = "annee",
    y = "p_admis",
    # title = "Ajouter le titre de votre choix",
    labels = {"p_admis" : "Proportion de personnes admises au baccalauréat"},
    color = "origine_sociale"
)

fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-03.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-03.png" alt="Courbe du pourcentage d'admission au baccalauréat (tous types confondus) entre 1997 et 2024 associée à une légende. Huit courbes sont présentées, une par origine sociale (parmi lesquelles on retrouve les Agriculteurs, Cadres, Indépendants et les Ouvriers), chacune d'une couleur différente. Le nombre de publication par année varie entre 70% et 100%.">
	</a>
<figcaption>
    <p>Figure 3. Courbe avec une interactivité simple en utilisant Plotly Express. Survoler les lignes révèle une boîte flottante. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-03.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

Nous avons appris à créer de nouvelles visualisations et à les personnaliser&nbsp;- mais comment faire pour personnaliser notre figure après l'avoir créée&nbsp;? À la place nous pouvons utiliser la méthode `.update_layout()` sur notre `fig` pour éditer après coup. Cette méthode peut être appliquée à n'importe quelle figure générée avec Plotly Express afin de modifier un large panel de paramètres. Prenons comme exemple la figure générée précédemment et modifions la police, la couleur et la taille de notre titre&nbsp;: 

```python
fig.update_layout(
    font_family = "Courrier New",   # Modification de la police
    font_color = "blue",            # Modification de la couleur du texte
    legend_title_font_color = "red",# Modification de la couleur du titre de la légende
    title = "Un titre formaté"
)

fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-04.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-04.png" alt="Courbe du pourcentage d'admission au baccalauréat (tous types confondus) entre 1997 et 2024 associée à une légende. Huit courbes sont présentées, une par origine sociale (parmi lesquelles on retrouve les Agriculteurs, Cadres, Indépendants et les Ouvriers), chacune d'une couleur différente. Le nombre de publication par année varie entre 70% et 100%.">
	</a>
<figcaption>
    <p>Figure 4. Courbe avec une interactivité simple en utilisant Plotly Express. Survoler les lignes révèle une boîte flottante. Cette visualisation est une variante de la Figure 3 avec des polices d'écriture, couleurs et titres différents. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-04.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

### Nuages de points

Les nuages de points (&laquo;&nbsp;scatterplots&nbsp;&raquo;), généralement utilisés pour visualiser des relations entre 2 variables continues, peuvent être créés à l'aide de Plotly Express en utilisant la fonction `px.scatter()`. Pour notre jeu de données, il peut être intéressant d'utiliser un nuage de points pour montrer la relation entre le nombre de personnes admises au baccalauréat général et le nombre de personnes admises au baccalauréat technologique par origine sociale chaque année. Pour alléger la visualisations, nous représentons seulement 4 origines sociales, soient les Agriculteurs, Cadres, Indépendants et les Ouvriers. Chaque point représente le nombre de personnes admises aux 2 types de baccalauréat pour une année.

Lorsqu'on crée un nuage de point à partir d'un tableau, chaque ligne sera représentée par un point, et chaque colonne représente une dimension. Pour la figure que l'on souhaite créer, il nous faut un tableau avec 4 colonnes, ce qui nous amène à créer un nouveau DataFrame. Les colonnes à créer sont&nbsp;:

 - L'année (`annee`)
 - L'origine sociale (`origine_sociale`)
 - Le nombre de personnes admises au baccalaureat général (`n_admis_bac_g`)
 - Le nombre de personnes admises au baccalaureat technologique (`n_admis_bac_t`)

Dans notre cas, il nous faut transformer la structure de données en passant par des dictionnaires intermédiaires puis en recréant le tableau sous la forme d'un DataFrame. On procède par un regroupement par année et origine sociale, puis on récupère les informations nécessaire pour chaque entrée que l'on veut représenter.

Ce traitement est bien entendu spécifique à la structure des données que nous utilisons ici.

```python
num_admis_bac_t_bac_g = {
    "annee" : [], 
    "origine_sociale" : [],
    "n_admis_bac_g" : [],
    "n_admis_bac_t" : []
}

# Pour chaque combinaison d'année et origine sociale
for (annee, origine_sociale), _ in df.groupby(["annee", "origine_sociale"]):
    # On sauvegarde: l'année, l'origine sociale, le nombre de personnes admises 
    # au baccalauréat général et au baccalauréat technologique
    
    # Si l'origine sociale n'est pas dans la liste suivante, on passe à la prochaine.
    if origine_sociale not in ["Cadres", "Indépendants", "Ouvriers", "Agriculteurs"]:
        continue
    
    num_admis_bac_t_bac_g["annee"].append(annee)
    num_admis_bac_t_bac_g["origine_sociale"].append(origine_sociale)
    num_admis_bac_t_bac_g["n_admis_bac_g"].append(
        df.loc[
            (df["type"]=="bac_g")&\
            (df["annee"]==annee)&\
            (df["origine_sociale"]==origine_sociale),
            "n_admis"
        ].item()
    )
    num_admis_bac_t_bac_g["n_admis_bac_t"].append(
        df.loc[
            (df["type"]=="bac_t")&\
            (df["annee"]==annee)&\
            (df["origine_sociale"]==origine_sociale),
            "n_admis"
        ].item()
    )

# Transformons maintenant le dictionnaire en DataFrame.
num_admis_bac_t_bac_g = pd.DataFrame(num_admis_bac_t_bac_g)
print(num_admis_bac_t_bac_g)
```

||annee|origine_sociale|n_admis_bac_g|n_admis_bac_t|
|-|-----|---------------|-------------|-------------|
|0     |1997 |Agriculteurs | 8309 | 4980|
|1     |1997 |Cadres | 111616 | 21858|
|2     |1997 |Indépendants | 26253 | 14119|
|3     |1997 |Ouvriers | 33038 | 32351|
|4     |1998 |Agriculteurs | 8356 | 5390|
|..    | ... |... | ... | ...|
|107   |2023 |Ouvriers | 35609 | 20449|
|108   |2024 |Agriculteurs | 3912 | 1206|
|109   |2024 |Cadres | 148642 | 25299|
|110   |2024 |Indépendants | 29309 | 10677|
|111   |2024 |Ouvriers | 33534 | 20416|

```python
fig = px.scatter(
    num_admis_bac_t_bac_g,
    x="n_admis_bac_t",
    y="n_admis_bac_g",
    color = "origine_sociale"
    # title="Titre de votre choix",
)
fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-05.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-05.png" alt="Nuage de points plaçant 27 points (un par année entre 1997 et 2024) par origine sociale sur un plan. Les axes de ce plan sont : en abscisse, le nombre de personnes admises au baccalauréat technologique et en ordonnée le nombre de personnes admises au baccalauréat général. Chaque point est associé à une orignie sociale, identifiée par une couleur décrite dans la légende.">
	</a>
<figcaption>
    <p>Figure 5. Nuage de points avec une interactivité simple. Survoler un point du jeu de données permet d'afficher l'origine sociale ainsi que le nombre de personnes admises au baccalauréat général, puis le nombre de personnes admises au baccalauréat technologie (année non affichée). De plus, la légende interactive permet d'isoler, comparer, retirer des catégories de points. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-05.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

Comme vous pouvez le voir, les nuages de points contiennent aussi certaines interactions par défaut&nbsp;: survoler les points permet d'afficher les données spécifiques aux points comme les coordonnées du point (ie le nombre de personnes admises au baccalauréat technologique et général) et l'origine sociale. Cliquer ou double-cliquer sur le nom des origines sociales dans la légende permet d'isoler certains éléments.

## Créer une visualisation en mosaïque

Les visualisations en mosaïque (&laquo;&nbsp;facet plots&nbsp;&raquo;) sont des visualisations subdivisées en plusieurs figures. Chaque subdivision illustre la même variable selon les mêmes axes mais pour des sous-ensembles différents. Plotly rend la création de telles visualisations très simple. En reprenant les exemples précédents, il suffit de spécifier le type de représentation que vous souhaitez dans les sous-figures. En deuxième instance il suffit d'utiliser le paramètre `facet_col` qui permet de préciser quelle variable utiliser pour distinguer les sous-figures. Dans l'exemple ci dessous, on crée une grille de 2x1 pour montrer le nombre de personnes admises au baccalauréat général et technologique en 2024&nbsp;:

```python
lignes_bac_technologique_et_general_2024 = \
    ((df["type"] == "bac_t") | (df["type"] == "bac_g")) &\
    (df["annee"] == 2024) # (type = "bac_t" ou "bac_g") ET annee = 2024
type_bac_origine_sociales = df.\
    loc[lignes_bac_technologique_et_general_2024, :]

# Utiliser la fonction px.bar pour spécifier le type de représentation
fig = px.bar(
    type_bac_origine_sociales,
    x="origine_sociale",
    y="n_admis",
    # Utiliser le paramètre facet_col pour spécifier la colonne qui doit subdiviser
    facet_col="type", 
    color="origine_sociale",
    # title="Titre de votre choix",
)
fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-06.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-06.png" alt="Une paire de diagrammes en barre partageant un même axe des ordonnées représentant le nombre de personnes admises au baccalauréat général (à gauche) et technologique (à droite) en fonction de leur origine sociale (parmi lesquelles on retrouve les Agriculteurs, Cadres, Indépendants et les Ouvriers). Chaque origine sociale se voit associé une couleur décrite dans une légende.">
	</a>
<figcaption>
    <p>Figure 6. Une mosaïque de deux diagrammes en barres avec une interactivité simple créée avec Plotly Express en distinguant le type de baccalauréat obtenu (technologique ou général). La légende interactive permet aussi d'isoler, comparer ou retirer certaines origines sociales. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-06.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

Notez que cette méthode ne nécessite pas de spécifier les dimensions de la grille puisque Plotly Express divise automatiquement la figure par le nombre de catégories disponibles (ici deux puisque les deux catégories disponibles sont baccalauréat technologique et général). Cependant, cette méthode ne peut fonctionner que pour des figures ne comportant qu’un seul type de visualisation (ici, des diagrammes en barres). Nous discuterons plus bas de la manière de créer des visualisations contenant des sous-figures de dimensions particulières à l’aide de Graph Objects.

### Ajouter des animations&nbsp;: évolution temporelle

Comme nous l’avons vu, Plotly Express contient des fonctionnalités interactives natives. Et pourtant, il y a encore de nombreuses fonctionnalités qui peuvent être implémentées pour augmenter l'interactivité comme les animations à travers les &laquo;&nbsp;animation frames&nbsp;&raquo;.

Une &laquo;&nbsp;animation frames&nbsp;&raquo; représente la manière dont les données changent en fonction d'un certain axe. Dans les recherches historiques, la mesure la plus utile est l'axe temporel bien que d'autres variables numérique avec une relation d'ordre peuvent fonctionner (ex&nbsp;: les entiers, ou un intervalle comme $[0,1]$). Une figure Plotly Express avec une animation contient une barre de défilement interactive permettant de jouer/arrêter l'animation mais aussi de se déplacer manuellement dans les données.

Pour créer une visualisation avec une animation, il faut commencer par sélectionner le type de représentation que nous voulons utiliser comme dans les exemples précédents. Puis, à l'intérieur de la fonction on utilise le paramètre `animation_frame` pour spécifier quelle variable doit être utilisée pour visualiser l'évolution. Dans notre exemple, nous reprenons le nombre de personnes admises au baccalauréat (tous types confondus) et affichons l'évolution à travers les années.

```python
num_admis_par_origine_sociale_par_annee = df.loc[
    df["type"] == "bac_tous", ["annee", "origine_sociale", "n_admis"]
]
# On utilise px.bar pour créer un diagramme en barres
fig = px.bar(
    num_admis_par_origine_sociale_par_annee,
    x="origine_sociale",
    y="n_admis",
    labels={"n_admis": "Nombre de personnes admises au baccalauréat"},
    range_y=[0,200_000],  # Le paramètre range_y permet de personnaliser l'intervalle de l'axe y 
    color="origine_sociale",
    # title="Titre de votre choix",
    # Utiliser le paramètre animation_frame pour spécfier l'axe d'évolution
    animation_frame="annee", 
)
fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-07.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-07.png" alt="Diagramme en barres animé. Sur l'axe des abscisses on retrouve 8 origines sociales (parmi lesquelles on retrouve les Agriculteurs, Cadres, Indépendants et les Ouvriers) et sur l'axe des ordonnées, on trouve le nombre de personnes admises au baccalauréat (tous types confondus) pendant une année. Une barre de défilement permet d'animer la visualisation en changeant l'année, et donc le nombre de personnes admises. Chaque barre est d'une couleur différente décrite dans une légende.">
	</a>
<figcaption>
    <p>Figure 7. Diagramme en barres animé associé à une barre de défilement créé grâce à Plotly Express. Comme précédemment, les lecteur·rice·s peuvent survoler les barres pour faire apparaître des boîtes flottantes. Les lecteur·rice·s peuvent appuyer sur les boutons play/pause ou utiliser la barre de défilement pour naviguer à travers les années. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-07.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

### Ajouter des animations&nbsp;: Menus déroulants

Les menus déroulants sont légèrement plus difficiles que les animation frames. Ils permettent à l'utilisateur·rice de passer d'une configuration d'affichage à une autre comprenant une large variété de paramètres permettant de changer les couleurs, lignes, axes et mêmes les variables. Quand on crée une figure avec un menu déroulant, la première étape est de créer la figure initiale sans menu déroulant (qui correspondra à la première vue que l'utilisateur·rice verra). Dans cet exemple, nous travaillerons avec le nuage de points qui illustre le nombre de personnes admises au baccalauréat général et technologique. La construction est donc la suivante&nbsp;: 

```python
fig = px.scatter(
    num_admis_bac_t_bac_g,
    x="n_admis_bac_t",
    y="n_admis_bac_g",
    color="origine_sociale", 
    # title="Titre de votre choix",
    labels = {
        "n_admis_bac_t" : "Nombre de personnes admises au baccalauréat technologique",
        "n_admis_bac_g" : "Nombre de personnes admises au baccalauréat général"
    }
)
```

Notons que la figure a été créée mais n'est pas visible puisque nous n'avons pas encore utilisé la fonction `fig.show()`. La figure sera affichée une fois que nous aurons ajouté le menu déroulant dans les prochaines étapes.

Après avoir créé la vue initiale, nous pouvons utiliser la méthode `update_layout` à nouveau pour ajouter un menu déroulant.

C'est une étape plus complexe puisque les données de l'objet Plotly Express sont imbriquées à plusieurs niveaux sous le capot, donc nous avons besoin de modifier des attributs à un niveau plus profond qu'à l'habitude pour créer le menu.

Une fois qu'on a appelé la méthode `update_layout`&nbsp;:

- Nous devons d'abord accéder au paramètre `updatemenus`&nbsp;: c'est une liste de dictionnaires, chaque dictionnaire contient les métadonnées pour plusieurs fonctionnalités.
- La seule fonctionnalité qui nous intéresse est la &laquo;&nbsp;dropdown box&nbsp;&raquo; (menu déroulant), qui est contenue dans le dictionnaire `buttons`.
- La clef `buttons` contient comme valeur une autre liste de dictionnaires, chaque dictionnaire représente les options disponibles dans le menu déroulant.
- Nous aurons besoin de créer 5 `buttons`&nbsp;— un par sous-groupe de données&nbsp;— donc notre liste `buttons` contiendra 5 dictionnaires.
- Chacun de ces cinq dictionnaires devra contenir 3 paires clef-valeur&nbsp;:
    - La première paire, avec pour clef `args` précisera le type de représentation que nous voulons afficher.
    - La deuxième paire, avec pour clef `label` précisera le titre à afficher à côté du menu déroulant.
    - La troisième paire, avec pour clef `method`, précisera comment modifier la figure (modifications possibles `update`, `restyle`, `animate`, etc...).

Dans l'exemple ci dessous, nous regarderons comment utiliser le menu déroulant pour changer la catégorie de la variable affichée. Puisque nous travaillons avec un nuage de points qui affiche le nombre de personnes admises au baccalauréat technologique et général pour 4 origines sociales différentes, nous ajouterons un menu déroulant qui permet d'afficher toutes les origines sociales ensemble, puis seulement les enfants d'agriculteurs, de cadres, d'indépendants et enfin d'ouvriers.

Pour créer le menu déroulant nous suivons les étapes suivantes&nbsp;:

 - À la clef `label` nous associons pour valeur, le texte à afficher dans le menu déroulant.
 - À la clef `method`, nous associons la valeur `update` puisque nous modifions l'affichage (`layout`) et les données (`data`).
 - À la clef `args`, nous associons une autre liste de dictionnaires qui spécifiera quelles données seront `visible`(s) (vous trouverez plus d'informations à ce propos plus bas), le titre de la vue (paramètre optionnel), ainsi que les titres pour les axes x et y de cette vue (paramètre optionnel).

Le paramètre `visible` contient une liste, chaque élément de cette liste indiquera si les données à cet index doivent être affichées où non. Dans notre exemple, la liste doit contenir 4 éléments puisque nous avons 4 origines sociales à l'écran. Dans notre cas, le premier bouton doit représenter la visualisation telle qu'elle sera initialement présentée à l'utilisateur·ice et doit donc spécifier `[True, True, True, True]` puisque nous souhaitons que toutes les origines sociales soient affichées. Cependant, pour les 4 autres vues, nous devons seulement inscrire `True` pour un seul élément puisque nous souhaitons n’afficher qu’une seule origine sociale à la fois.

Passons à la pratique&nbsp;:

```python
# Nous utilisons la méthode .update_layout pour ajouter le menu déroulant
fig.update_layout(
    updatemenus = [dict(
        buttons = [
            # Création de la liste de dictionaires pour chaque bouton du menu déroulant.
            dict(
                label = "Toutes les origines sociales", # Nom pour la première vue
                method = "update",
                args = [
                    # Cette vue montre les 4 origines sociales
                    {"visible" : [True, True, True, True]},
                    {
                        "title" : "Toutes les origines sociales",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                            }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
            dict(
                label = "Agriculteurs", # Nom pour la deuxième vue
                method = "update",
                args = [
                    # Cette vue montre seulement la première origine sociale
                    {"visible" : [True, False, False, False]}, 
                    {
                        "title" : "Agriculteurs",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                            }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
            dict(
                label = "Cadres", # Nom pour la troisième vue
                method = "update",
                args = [
                    # Cette vue montre uniquement la deuxième origine sociale
                    {"visible" : [False, True, False, False]}, 
                    {
                        "title" : "Cadres",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                            }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
            dict(
                label = "Indépendants", # Nom pour la quatrième vue
                method = "update",
                args = [
                    # Cette vue montre la 3è origine sociale
                    {"visible" : [False, False, True, False]},
                    {
                        "title" : "Indépendants",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                                }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
            dict(
                label = "Ouvriers", # Nom pour la cinquième vue
                method = "update",
                args = [
                    # Cette vue montre la 4è origine sociale
                    {"visible" : [False, False, False, True]},
                    {
                        "title" : "Ouvriers",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                            }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
        ]
    )]
)

fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-08.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-08.png" alt="Nuage de points plaçant 27 points (un par année entre 1997 et 2024) par origine sociale sur un plan. Les axes de ce plan sont : en abscisse, le nombre de personnes admises au baccalauréat technologique et en ordonnée le nombre de personnes admises au baccalauréat général. Chaque point est associé à une orignie sociale, identifiée par une couleur décrite dans la légende. Un menu déroulant permet de sélectionner une origine sociale à afficher.">
	</a>
<figcaption>
    <p>Figure 8. Nuage de points avec un filtre interactif sous la forme d'un menu déroulant créé grâce à Plotly Express. Cette figure contient une légende interactive qui permet au lecteur d'isoler, comparer et retirer des données. De plus survoler des points permet de faire apparaître des boîtes flottantes. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-08.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

Créer ce menu déroulant dans l’exemple ci-dessus permet aux utilisateur·rice·s d’isoler (et d’examiner) des éléments spécifiques à partir d'une visualisation plus générale. Nous avions découvert cette fonctionnalité de Plotly plus tôt en notant qu'un double-clic sur une catégorie de la légende permettait de retirer tous les autres groupes de la figure. Cependant, le menu déroulant apporte d'autres avantages&nbsp;: il nous permet de créer des titres dynamiques qui peuvent changer en fonction de ce que nous avons sélectionné.

L'exemple ci-dessus montre qu'il est très facile de créer des visualisations avec Plotly Express et qu'il est relativement simple de rajouter de l'interactivité comme des animations ou des menus déroulants. Nous allons maintenant passer à la création de visualisations avec Plotly Graph Objects. Plus précisément, nous allons nous concentrer sur ce que sont les Graph Objects, comment ils fonctionnent et quand (ou pourquoi) vous pourriez avoir envie de créer des visualisations en utilisant Plotly Graph Objects plutôt que Plotly Express.

## Création des visualisations avec Plotly Graph Objects

### Configuration de Plotly Graph Objects

Pour commencer à travailler avec Plotly Graph Objects, vous aurez besoin d'importer le module `graph_objects`&nbsp;:

```python
import plotly.graph_objects as go 
```

<div class="alert alert-info">
Notons que dans un script <code>.py</code> conventionnel, les modules devraient être importés au début du script. On importe les modules ici pour un soucis de clarté.
</div>

### Ce ne sont que des Objets&nbsp;&raquo;! La structure des données de Plotly Graph Objects 

Comme mentionné en introduction de cette leçon, toutes les figures créées avec Plotly Express sont en fait des Graph Objects sous le capot. Cela signifie que, lorsque nous créons une figure avec `plotly.px`, vous êtes en fait en train de créer une instance de Graph Object.

Cela devient évident si l'on utilise la fonction `type` avec la variable `fig`&nbsp;:

```python
# Résultat du type de la figure
print(type(fig))
```

```
<class 'plotly.graph_objs._figure.Figure'>
``` 

Il est alors important de toujours garder en tête que les figures créées avec Plotly sont des Graph Objects.

Les Graph Objects sont représentés comme des structure de données en arbre (ie. hiérarchiques) avec trois racines&nbsp;:

- La racine `data`&nbsp;— &laquo;&nbsp;données&nbsp;&raquo;&nbsp;— contient des informations comme le type de représentation, les catégories disponibles, les points associés à chaque catégorie, l'option d'affichage dans la légende, le type de marqueurs utilisés, les informations à afficher lorsque l'on survole les points.
- La racine `layout`&nbsp;— &laquo;&nbsp;affichage&nbsp;&raquo;&nbsp;— contient des informations telles que les dimensions de la figure, les polices et couleurs d'écriture à utiliser, les annotations, les coordonnées des sous-figures (&laquo;&nbsp;subplots&nbsp;&raquo;), et si des images doivent être utilisées comme arrière plan.
- La racine `frames` contient toutes les informations reliées aux animations utilisées dans la figure, comme les données à afficher à chaque &laquo;&nbsp;frame&nbsp;&raquo;. Cet attribut ne sera pas créé si vous n'ajoutez pas d'animation à la figure.

Il est facile de voir la structure de données sous-jacente d'une figure en l'imprimant comme un dictionnaire avec la fonction `fig.to_dict()`. Pour lire ces données plus facilement, on peut utiliser le format `JSON` avec la fonction `fig.to_json(pretty = True)`. Dans l'exemple ci dessous, nous ne montrons que les 500 premiers caractères comme extrait de sortie après utilisation de cette fonction (une fois encore, en utilisant la variable `fig` créée précédemment).

```python
print(fig.to_json(pretty = True)[0:500] + "\n...")
```

```json
{
  "data": [
    {
      "hovertemplate": "origine_sociale=Agriculteurs\u003cbr\u003en_admis_bac_t=%{x}\u003cbr\u003en_admis_bac_g=%{y}\u003cextra\u003e\u003c\u002fextra\u003e",
      "legendgroup": "Agriculteurs",
      "marker": {
        "color": "#636efa",
        "symbol": "circle"
      },
      "mode": "markers",
      "name": "Agriculteurs",
      "orientation": "v",
      "showlegend": true,
      "x": {
        "dtype": "i2",
        "bdata": "dBMOFX4VThVQFGUTohIjEqERHBEkCxgLIAo0CjsJa
...
```

Examiner la sortie affichée devrait pouvoir vous aider à comprendre la structure de données sous-jacente et les propriétés d'un Graph Object. Si vous imprimez la sortie entière (en utilisant `fig.to_dict()`) vous noterez que&nbsp;: 

- La structure de données contient des `data` chaque origine sociale (Agriculteurs, Cadres, Indépendants et Ouvriers) dispose de son propre dictionnaire.
- L'attribut `data` qualifie quel type de représentation est utilisé (ici `Scatter`).
- L'attribut `layout` contient le titre de la figure.
- L'attribut `layout` contient les données associées aux `buttons` (ie le menu déroulant).
- Il n'y a pas d'attribut `frames` puisqu'il n'y a pas d'animation associée à la figure.

### Utiliser Plotly Graph Objects vs Plotly Express

Un autre point qu'il est important d'avoir à l'esprit&nbsp;: créer des visualisations avec `plotly.go` requiert, en général, bien plus de code que pour créer les mêmes visualisations avec `plotly.px`.

Voyez plutôt l'exemple suivant&nbsp;: construisons un diagramme en barres horizontales pour illustrer le nombre de personnes admises au baccalauréat (tous types confondus) en 2024. Premièrement, sélectionnons une partie du DataFrame pour ne garder que l'année 2024 et le type `"bac_tous"`&nbsp;:

```python
num_admis_par_origine_sociale_2024 = df.loc[
    (df["annee"] == 2024)&(df["type"] == "bac_tous"), ["origine_sociale", "n_admis"]
]
```

Construisons maintenant le diagramme en barres horizontales avec ces données, grâce à `plotly.go`&nbsp;:

```python
fig = go.Figure(
    # Utiliser go.Bar() pour spécifier le type de représentation à créer
    go.Bar(
        x = num_admis_par_origine_sociale_2024["n_admis"], 
        y = num_admis_par_origine_sociale_2024["origine_sociale"],
        orientation = "h",
        # Nous devons formatter le "hover text" alors que c'est automatique avec plotly.px
        hovertemplate = ("Origine Sociale : %{y}<br>"
                         "Nombre de personnes admises : %{x}"
                         "<extra></extra>"  )
    ),
    # layout = {"title" : "Ajouter le titre de votre choix"},
)

fig.update_layout(
    # Nous devons modifier le layout pour les titres d'axes alors que c'est automatique avec plotly.px
    xaxis = {"title" : ("Nombre de personnes admises au baccalauréat (tous "
                        "types confondus)")},
    yaxis = {"title" : "Origine Sociale"}
)

fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-09.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-09.png" alt="Diagramme en barres représentant, sur l'axe des abscisses, 8 origines sociales (parmi lesquelles on retrouve les Agriculteurs, Cadres, Indépendants et les Ouvriers) et sur l'axe des ordonnées le nombre de personnes admises au baccalauréat en 2024 (tous types confondus), le nombre d'admis varie entre 6k et 200k.">
	</a>
<figcaption>
    <p>Figure 9. Diagramme en barres horizontal avec une interactivité simple créé avec Plotly Graph Objects. Les lecteur·rice·s peuvent survoler les barres pour faire apparaître les boîtes flottantes. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-09.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

Notons que lorsque l'on utilise Plotly Graph Objects, on peut fournir un titre en utilisant l'argument `layout`, qui prend un dictionnaire contenant la clef `title` et sa valeur.

Maintenant créons la même visualisation avec `plotly.px`&nbsp;:

```python
fig = px.bar(
    num_admis_par_origine_sociale_2024,
    x = "n_admis", y = "origine_sociale",
    orientation = "h",
    #title = "Titre de votre choix",
    labels = {"n_admis" : ("Nombre de personnes admises au baccalauréat (tous "
                           "types confondus)")}
)
fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-10.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-10.png" alt="Diagramme en barres représentant, sur l'axe des abscisses, 8 origines sociales (parmi lesquelles on retrouve les Agriculteurs, Cadres, Indépendants et les Ouvriers) et sur l'axe des ordonnées le nombre de personnes admises au baccalauréat en 2024 (tous types confondus), le nombre d'admis varie entre 6k et 200k.">
	</a>
<figcaption>
    <p>Figure 10. Diagramme en barres horizontal avec une interactivité simple créé avec Plotly Express. Les lecteur·rice·s peuvent survoler les barres pour faire apparaître les boîtes flottantes. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-10.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

Il est clair d'après les exemples précédents que Plotly Graph Objects requiert plus de code que Plotly Express car de nombreuses fonctionnalités nécessitent d'être manuellement créées dans Plotly Graph Objects. Ainsi, il est en général recommandé d'utiliser Plotly Express quand c'est possible.

### Pourquoi utiliser Plotly Graph Objects

Ceci devrait nous amener à la question centrale&nbsp;: si c'est si simple d'utiliser Plotly Express pour créer des visualisations, pourquoi devrions nous nous embêter avec Plotly Graph Objects&nbsp;? La réponse simple est qu'il y a en réalité de nombreuses fonctionnalités utiles qui ne sont accessibles qu'à travers Plotly Graph Objects. Nous jetons un œil à deux de ces fonctionnalités dans cette section du tutoriel&nbsp;: les tableaux et les compositions de figures (subplots).

#### Tableaux

L'une des fonctionnalités de Plotly Graph Objects la plus utile est l'option de créer des tableaux interactifs et clairs.

Pour cela, suivons les 4 étapes suivantes&nbsp;:

1. Créer une figure avec la fonction `.Figure()`.
2. À la racine `data`, utiliser la fonction `.Table()` pour spécifier que la figure doit être une table.
3. Dans la fonction `.Table()`, créer un dictionnaire entête (`header`) pour stocker la liste des colonnes de l'entête.
4. Dans la fonction `.Table()`, ajouter un dictionnaire cellules (`cells`) pour y mettre les valeurs du tableau.

Il est aussi possible de personnaliser grâce à des labels, couleurs, et des options d'alignement.

Dans l'exemple ci-dessous, nous créons un tableau pour stocker l'entièreté de la base de données.

```python
fig = go.Figure(
    data = [
        go.Table(
            header = {
                "values" : df.columns,
                "fill_color" : "paleturquoise",
                "align" : "left"
            },
            cells = {
                "values" : df.transpose().values.tolist(),
                "fill_color" : "lavender",
                "align" : "left"
            }
        )
    ]
)

fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-11.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-11.png" alt="Tableau montrant une partie du jeu de données. Les colonnes visibles sont : annee, origine_sociale, type, n_admis, p_admis.">
	</a>
<figcaption>
    <p>Figure 11. Tableau contenant le jeu de données et créé avec Plotly Graph Object. Les lecteur·rice·s peuvent faire défiler toutes les entrées du jeu de données comme iels le feraient dans un tableur. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-11.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

De la même manière qu'avec `plotly.px`, les figures de `plotly.go` permettent une certaine interactivité native. Les tableaux par exemple permettent aux utilisateur·rice·s de faire défiler les lignes du tableau (en utilisant le trackpad ou la barre de défilement sur la droite). Ces objets sont ainsi excellents pour économiser de la place. Il est aussi facile de déplacer des colonnes en cliquant sur l'entête d'une colonne et la déplaçant à droite ou à gauche. 

#### La compositions de figures (subplots)

Une autre fonctionnalité très utile de Plotly Graph Objects est le fait de pouvoir créer des compositions de figures. Bien que Plotly Express permette de créer des visualisations en mosaïque, le champ des possibles est relativement limité puisque les sous-figures générées doivent toutes partager le même type de représentation, les axes et les variables à afficher. La composition de figures permet elle de créer des grilles contenant différents types de représentations avec leurs axes et variables propres afin de transformer les figures en des objets proches des dashboards.

Puisque le code est particulièrement long pour créer des compositions de figures, cet exemple sera présenté pas-à-pas. Nous créerons une grille de 3x1 contenant 3 différentes figures&nbsp;: le premier sera un diagramme en barres standard pour quantifier le nombre de personnes admises au baccalauréat (tous types confondus) en 2024&nbsp;; le deuxième sera une courbe affichant l'évolution du pourcentage de personnes admises au baccalauréat (tous types confondus) entre 1997 et 2024. Enfin la dernière figure sera un diagramme en boîte (avec la représentation du minimum, maximum, interquartile d'une distribution) sur la distribution du pourcentage de personnes admises au baccalauréat général, technologique et professionnel.

**Étape 1&nbsp;: importer le module subplots et préparer les données**

```python
# Importer make_subplots
from plotly.subplots import make_subplots

# Préparation des données
num_admis_par_origine_sociale = df.\
    groupby(["type", "annee"]).\
    get_group(("bac_tous", 2024))

# On ne garde que 4 origines sociales pour alléger le graphe
selection_origines_sociales = np.isin(
    df["origine_sociale"], 
    ["Cadres", "Indépendants", "Ouvriers", "Agriculteurs"]
)
prop_admis_par_origine_sociale_par_annee = df.\
    loc[selection_origines_sociales, :].\
    groupby("type").get_group("bac_tous")

pourcentage_reussite_par_type_de_bac = df.\
    loc[df["type"] != "bac_tous",["type", "p_admis"]].\
    groupby("type")
```

**Étape 2&nbsp;: Création d'une composition de sous-figures vide avec une grille 3x1 grâce à la fonction `make_subplots`**

```python
# 1 ligne, 3 colonnes
fig = make_subplots(rows = 1, cols = 3)
```

**Étape 3&nbsp;: création de la première figure (le diagramme en barres) grace à la méthode `.add_trace()`**

```python
fig.add_trace(
    # Utiliser go.Bar() pour spécifier le type de représentation
    go.Bar(
        x = num_admis_par_origine_sociale["n_admis"],
        y = num_admis_par_origine_sociale["origine_sociale"],
        orientation = "h",
        name = "Nombre de personnes admises au baccalauréat",
        hovertemplate = ("<b>Origine sociale :</b> %{y}<br><b>Nombre de personnes "
                        "ayant obtenu le bac</b> : %{x}<extra></extra>")
    ),
    # Les paramètres row et col permettent de positionner la figure dans la bonne case
    row = 1, col = 1 
)
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-12.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-12.png" alt="Une visualisation à trois colonnes, avec dans la colonne de gauche un diagramme en barres. La colonne centrale et de droite sont vides.">
	</a>
<figcaption>
    <p>Figure 12. Une composition de figures avec 3 colonnes et une interactivité simple créée avec le module Plotly Graph Object, et avec un diagramme en barres sur la gauche montrant le nombre de personnes admises au baccalauréat (tous types confondus) par origine sociale en 2024, et deux colonnes vides sur la droite. Les lecteur·rice·s peuvent survoler les barres pour faire apparaître les boîtes flottantes. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-12.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

<div class="alert alert-info">
Nota&nbsp;: si vous créez une composition de figures dans un Notebook Jupyter, relancer le code pourrait dupliquer la trace que vous venez d'ajouter et donc doubler la légende. Si vous avez besoin de relancer le code, il vaudrait mieux relancer à partir de la cellule qui définit la variable <code>fig</code> que vous modifiez.
</div>

**Étape 4&nbsp;: Ajouter la seconde figure (courbe)**

```python
# Pour chaque origine sociale il faut créer un objet go.Scatter différent afin de créer 
# les différentes courbes. 
# Pour se faire, on divise notre DataFrame par origine sociale et on procède comme 
# précédemment en ne travaillant qu'avec les sous-dataset
for origine_sociale, df_origine_sociale in prop_admis_par_origine_sociale_par_annee.\
                                    groupby("origine_sociale") :
    fig.add_trace(
        # Utiliser go.Scatter() pour spécifier le type de représentation
        go.Scatter(
            x = df_origine_sociale["annee"],
            y = df_origine_sociale["p_admis"],
            name = origine_sociale,
            mode = "markers+lines",
            hovertemplate = (f"<b>Origine sociale :</b> {origine_sociale}<br>"
                             "<b>Année :</b> %{x}<br>"
                             "<b>Proportion de personnes admises :</b> %{y}")  

        ),
        # Les paramètres row et col permettent de positionner la figure dans la bonne case
        row = 1, col = 2 
    )
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-13.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-13.png" alt="Une visualisation à trois colonnes, avec dans la colonne de gauche un diagramme en barres et dans la colonne centrale quatre courbes de couleurs. Une légende décrit les éléments affichés. La colonne de droite est vide.">
	</a>
<figcaption>
    <p>Figure 13. Une composition de figures avec 3 colonnes et une interactivité simple créée avec le module Plotly Graph Object, et avec un diagramme en barres sur la gauche montrant le nombre de personnes admises au baccalauréat (tous types confondus) par origine sociale en 2024, une courbe au centre montrant l'évolution de la proportion de personnes admises au baccalauréat (tous types confondus) par origine sociale et une colonnes vide sur la droite. Les lecteur·rice·s peuvent survoler les barres pour faire apparaître les boîtes flottantes. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-13.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

**Étape 5&nbsp;: Ajouter la dernière figure (diagramme en boîte)**

Nous n'avons pas encore exploré les diagrammes en boîte (&laquo;&nbsp;boxplot&nbsp;&raquo;), mais ils sont créés de la même manière que les autres figures et ont une interactivité native similaire (survoler une boîte nous montrera la valeur minimum, maximum, médiane, et les interquartiles des données affichées).

```python
fig.add_trace(
    # Utiliser go.Box() pour spécifier le type de représentation
    go.Box(
        y = pourcentage_reussite_par_type_de_bac.\
            get_group("bac_g")["p_admis"],
        name = "Baccalauréat général"),
        row = 1, col = 3 # puisque c'est la troisième, on le met sur la 3è colonne
)

# On ajoute le deuxième et troisiéme diagramme en boîte puisqu'on a 3 groupes 
# distincts pour chaque type de baccalauréat
fig.add_trace(
    go.Box(
        y = pourcentage_reussite_par_type_de_bac.\
            get_group("bac_t")["p_admis"],
        name = "Baccalauréat technologique"),
        row = 1, col = 3 # puisque c'est la troisième, on le met sur la 3è colonne
)

fig.add_trace(
    go.Box(
        y = pourcentage_reussite_par_type_de_bac.\
            get_group("bac_p")["p_admis"],
        name = "Baccalauréat professionnel"),
        row = 1, col = 3 # puisque c'est la troisième, on le met sur la 3è colonne
)
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-14.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-14.png" alt="Une visualisation à trois colonnes, avec dans la colonne de gauche un diagramme en barres et dans la colonne centrale quatres courbes de couleurs. Une légende décrit les éléments affichés. Dans la colonne de droite on trouve 2 diagrammes en boîte.">
	</a>
<figcaption>
    <p>Figure 14. Une composition de figures avec 3 colonnes et une interactivité simple créée avec le module Plotly Graph Object, et avec un diagramme en barres sur la gauche montrant le nombre de personnes admises au baccalauréat (tous types confondus) par origine sociale en 2024, une courbe au centre montrant l'évolution de la proportion de personnes admises au baccalauréat (tous types confondus) par origine sociale et trois diagrammes en boîte représentant la distribution de la part de personnes admises selon le type de baccalauréat. Les lecteur·rice·s peuvent survoler les barres pour faire apparaître les boîtes flottantes. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-14.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

**Étape 6&nbsp;: Formattage de la Figure**

Il est nécessaire d'ajuster certains paramètres, comme ajouter un titre général à la figure et des sous-titres pour tous les sous-figures. Vous pourriez aussi vouloir changer la police d'écriture, changer la position du texte, la taille de la figure&nbsp;– vous pouvez utiliser la méthode `.update_layout()` pour changer toutes ces propriétés&nbsp;:

```python
fig.update_layout(
    # Changement de la police d'écriture pour toute la figure
    font_family = "Times New Roman", 
    # Changement de la police d'écriture pour les notes hover
    hoverlabel_font_family = "Times New Roman", 
    # changement de la taille d'écriture pour les notes hover
    hoverlabel_font_size = 16, 
    # title_text = "Ajouter un titre ici", # Titre principal
    # Positionnement du titre principal au centre de la visualisation 
    # (note : le paramètre title_x ne prend que des entiers (integers) 
    # ou des réels (floats))
    # title_x = 0.5 
    # ajout d'un titre d'axe pour l'absisse de la première figure
    xaxis1_title_text = ("Nombre de personnes admises au baccalauréat <br>(tous "
                         "types confondus) en 2024"),
    # ajout d'un titre d'axe pour les ordonnées de la première figure
    yaxis1_title_text = "Origine sociale", 
    yaxis2_title_text = ("Part de personnes admises au baccalauréat (tous types"
                         " confondus)"),
    xaxis2_title_text = "Année",
    yaxis3_title_text = "Distribution du pourcentage d'admission au baccalauréat",
    showlegend = False, # Retire la légende
    # Ajuste la taille de la visualisation  - pas toujours nécessaire mais peut 
    # s'avérer utile si les figures sont publiées sur internet
    height = 650
)
``` 

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-15.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-15.png" alt="Une visualisation à trois colonnes, avec dans la colonne de gauche un diagramme en barres et dans la colonne centrale quatres courbes de couleurs. Dans la colonne de droite on trouve 2 diagrammes en boîte.">
	</a>
<figcaption>
    <p>Figure 15. Une composition de figures avec 3 colonnes et une interactivité simple créée avec le module Plotly Graph Object, et avec un diagramme en barres sur la gauche montrant le nombre de personnes admises au baccalauréat (tous types confondus) par origine sociale en 2024, une courbe au centre montrant l'évolution de la proportion de personnes admises au baccalauréat (tous types confondus) par origine sociale et trois diagrammes en boîte représentant la distribution de la part de personnes admises selon le type de baccalauréat. Les lecteur·rice·s peuvent survoler les barres pour faire apparaître les boîtes flottantes. Cette visualisation est une variante de la Figure 14 avec une personalisation avancée. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-15.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

**Étape 7&nbsp;: Ajout d'annotations aux courbes**

Puisque la légende a été retirée, il est impossible de distinguer une origine sociale des autres. Nous pouvons utiliser la méthode `.update_layout` pour ajouter des flèches pointant vers chaque ligne avec une annotation&nbsp;: 

```python
fig.update_layout(
    # annotations reçoit une liste de disctionnaires, un dictionnaire = une annotation
    annotations = [
        # Notre première annotation sera pour identifier l'origine sociale "Agriculteurs"
        dict(
            # coordonnées du points de référence de l'annotation
            x = 2000, y = 85,
            # Spécifie dans quel référentiel on se place, ici comme on annote la
            # figure n°2 on donne comme référence x2, y2
            xref = "x2", yref = "y2",
            # Permet de spécifier la longueur de la flèche, et donc le décalage du 
            # texte par rapport au point
            ax = 0, ay = -100,
            text = "Agriculteurs",
            showarrow = True, # Utilisez False si vous ne voulez pas de la tête
            # de flèche dans l'annotation
            arrowhead = 1, # change la taille de la tête de flèche
        ),
        # Notre deuxième annotation sera pour identifier l'origine sociale "Indépendants"
        dict(
            x = 2001, y = 78.99,
            xref = "x2", yref = "y2",ax = 130, ay = 30,
            text = "Indépendants",showarrow = True, arrowhead = 1, 
        ),
        # Notre troisième annotation sera pour identifier l'origine sociale "Ouvriers"
        dict(
            x = 2019, y = 85.40,
            xref = "x2", yref = "y2",ax = 10, ay = 50,
            text = "Ouvriers",showarrow = True, arrowhead = 1, 
        ),
        # Notre quatrième annotation sera pour identifier l'origine sociale "Cadres"
        dict(
            x = 2020, y = 98.25,
            xref = "x2", yref = "y2",ax = -100, ay = 0,
            text = "Cadres",showarrow = True, arrowhead = 1, 
        ),
    ]
)
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-16.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-16.png" alt="Une visualisation à trois colonnes, avec dans la colonne de gauche un diagramme en barres et dans la colonne centrale quatre courbes de couleurs. Des annotations sont présentes pour indiquer l'origine sociale associée à chacune des quatre courbes. Dans la colonne de droite on trouve 2 diagrammes en boîte.">
	</a>
<figcaption>
    <p>Figure 16. Une composition de figures avec trois colonnes et une interactivité simple créée avec le module Plotly Graph Object, et avec un diagramme en barres sur la gauche montrant le nombre de personnes admises au baccalauréat (tous types confondus) par origine sociale en 2024, une courbe au centre montrant l'évolution de la proportion de personnes admises au baccalauréat (tous types confondus) par origine sociale et trois diagrammes en boîte représentant la distribution de la part de personnes admises selon le type de baccalauréat. Les lecteur·rice·s peuvent survoler les barres pour faire apparaître les boîtes flottantes. Cette visualisation est une variante de la Figure 15 des annotations pour repérer les courbes de la sous-figure du milieu. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-16.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

**Étape 8&nbsp;: Ajout d'annotations en dessous de la figure**

Nous pourrions avoir besoin d'ajouter des annotations en dessous de la figure pour spécifier la direction choisie pour notre analyse (cela s'avère très utile lorsqu'on publie des articles académiques), ce qui peut être fait grâce à la méthode `.add_annotation()`&nbsp;:

```python
fig.add_annotation(
    dict(
        font=dict(color="black", size=15),  # Change la police d'écriture
        x=0.5,  # Utilise x et y pour la position de l'annotation
        y=-0.4,
        showarrow=False,
        text=(
            "Nombre de personnes admises au baccalauréat (tous types confondus)"
            " en 2024 et par origine sociale (gauche); <br>"
            "Proportion de personnes admises au baccalauréat (tous types"
            " confondus) à travers les années et par origine sociale (centre);<br>"
            "Distribution du pourcentage d'admission pour le baccalauréat général,"
            " technologique et professionnel (droite)."),
        # Option pour changer l'orientation de l'écriture, utile pour la gestion de l'espace
        textangle=0,  
        xanchor="center",
        # Régler xref et yref à 'paper' pour que les valeurs de x et y soient 
        # des coordonées absolues
        xref="paper",  
        yref="paper",
    )
)
# On ajoute une marge pour que laisser la place aux annotations
fig.update_layout(margin = {"b" : 200})
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-17.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-17.png" alt="Une visualisation à trois colonnes, avec dans la colonne de gauche un diagramme en barres et dans la colonne centrale quatres courbes de couleurs. Des annotations sont présentes pour indiquer l'origine sociale associée à chacune des quatre courbes. Dans la colonne de droite on trouve trois diagrammes en boîte. Une annotation décrit chacun des graphe : Nombre de personnes admises au baccalauréat (tous types confondus) en 2024 et par origine sociale (gauche); Proportion de personnes admises au baccalauréat (tous types confondus) à travers les années et par origine sociale (centre); Distribution du pourcentage d'admission pour le baccalauréat général, technologique et professionnel (droite).">
	</a>
<figcaption>
    <p>Figure 17. Une composition de figures avec trois colonnes et une interactivité simple créée avec le module Plotly Graph Object, et avec un diagramme en barres sur la gauche montrant le nombre de personnes admises au baccalauréat (tous types confondus) par origine sociale en 2024, une courbe au centre montrant l'évolution de la proportion de personnes admises au baccalauréat (tous types confondus) par origine sociale et trois diagrammes en boîte représentant la distribution de la part de personnes admises selon le type de baccalauréat. Cette visualisation est une variante de la Figure 16 avec des annotations supplémentaires sous les figures. <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-17.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

## Afficher et Exporter les visualisations

Dans les sections précédentes de la leçon, nous avons vu comment créer et modifier les visualisations interactives avec Plotly Express et Plotly Graph Objects. Nous allons maintenant apprendre comment faire apparaître les visualisations et les exporter pour les publier ou les partager.

La méthode illustrée ici exportera la figure 3 créée plus tôt dans la leçon&nbsp;:

```python
fig = px.line(
    prop_admis_par_origine_sociale_par_annee,
    x = "annee",
    y = "p_admis",
    # title = "Ajouter le titre de votre choix",
    labels = {"p_admis" : "Proportion de personnes admises au baccalauréat"},
    color = "origine_sociale"
)
```

### Afficher la visualisation

Comme nous l'avons vu tout le long de cette leçon, la méthode `.show()` peut être utilisée pour faire apparaître la figure. Par défaut, cette méthode utilise le générateur d'image Plotly qui fournit l'interactivité native&nbsp;:

```python
fig.show()
```

<figure style="">
<a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-03.html" style="" target="_blank">
    <img src="/images/interactive-visualization-with-plotly/fr-tr-visualisations-interactives-plotly-03.png" alt="Courbe montrant l'évolution de la part de candidats admis au baccalauréat entre 1997 et 2024 selon leur origine sociale. Huit courbes sont représentées, une par origine sociale et chacune d'une couleur différente. Les parts d'admission sont comprises entre 70% et 100%.">
	</a>
<figcaption>
    <p>Figure 18. Reproduction de la Figure 3, illustrant la fonction fig.show(). <a href="/assets/visualisations-interactives-plotly/fr-tr-visualisations-interactives-plotly-03.html" target="_blank">Cliquez pour explorer une version interactive de cette figure.</a></p>
</figcaption>
</figure>

### Export des visualisations

Les figures Plotly peuvent être exportées en version statique (donc sans interactivité) ou en version interactive. Les visualisations interactives sont utiles pour les sites de recherches et certaines publications numériques, tandis que les versions statiques sont plus appropriées aux publications imprimées.

#### Export en HTML 

Exporter les figures en HTML conserve l'interactivité lorsqu'on les ouvre avec un moteur de recherche. Toute figure peut être sauvegardée en format HTML grâce à la fonction `.write_html()`&nbsp;:

```python
# Sauvegarde de la visualisation en format HTML
fig.write_html("nom_visualisation.html")
```

Par défaut toute figure exportée sera sauvegardée dans le même dossier que celui où se trouve le script. Si vous voulez sauvegarder la figure dans un autre dossier, vous pouvez spécifier le chemin exact vers ce dossier (par exemple `fig.write_html("your_path/nom_visualisation.html")`).

#### Export d'images statistiques

Plotly fournit de nombreuses options pour exporter des images pixellisées (`.png` ou `.jpg`) et images vectorielles (`.pdf` ou `.svg`). Pour cela, il suffit d'utiliser la méthode `write_image()` et spécifier quel type d'image vous souhaitez dans le nom du fichier&nbsp;:

```python
# Export en images classiques (raster ):
fig.write_image("nom_visualisation.png")
fig.write_image("nom_visualisation.jpeg")

# Export en images vectorielles :
fig.write_image("nom_visualisation.svg")
fig.write_image("nom_visualisation.pdf")
```

## Résumé

Plotly offre la possibilité de créer des images de qualité, interactives en utilisant Python ou bien d'autres langages de programmation. Cette leçon fournit un aperçu de Plotly, pourquoi cette bibliothèque est utile et comment on peut l'utiliser sous Python. Elle montre aussi comment utiliser différents modules de Plotly (Plotly Express et Plotly Graph Objects) et les méthodes nécessaires pour créer, éditer et exporter des visualisations. Les syntaxes clefs sont&nbsp;: 

- Installer Plotly en utilisant `pip install plotly`.
- Importer Plotly Express et Plotly Graph Objects à l'aide de `import plotly.express as px` et `import plotly.graph_objects as go`.
- Avec Plotly Express&nbsp;:
    - Créer des visualisations à l'aide de `px.bar()`, `px.line()` et `px.scatter()`.
    - Ajouter des personnalisations tels qu'un titre, des titres d'axes ou modifier les couleurs à l'aide des paramètres (`title`, `labels` et `color`) et même ajouter des animations avec le paramètre `animation_frames`.
    - Modifier les visualisations après leur création à l'aide de la méthode `.update_layout()` et ajouter des menus déroulants.
- Avec Plotly Graph Objects&nbsp;:
    - Reconnaitre la structure sous-jacente de toutes les figures à travers les attributs `data`, `layout` et `frames`.
    - Créer de nouvelles visualisations vides avec la fonction `go.Figure()`.
    - Créer des visualisations avec les fonctions `go.Bar()`, `go.Box()`, `go.Scatter()` et des tables avec `go.Table()`.
    - Créer des compositions de figures (en important le module `from plotly.subplots import make_subplots`, et réaliser l'implémentation grâce à la fonction `make_subplots` puis ajouter des données grâce à la méthode `.add_trace()`).
    - Modifier les figures après leur création à l'aide de la méthode `.update_layout()`.
- Exporter des visualisations créés avec Plotly Express ou Plotly Graph Objects avec la méthode `.write_html()` ou bien `.write_image()`.

## Notes de fin

[^1]: En réalité, toutes ces librairies sont construites à partir de la librairie Plotly pour JavaScript.

[^2]: `Plotly.Dash` est en dehors du cadre de cette leçon, qui se concentre plutôt sur Plotly Express et Plotly Graph Objects.

[^3]: Pour plus d'informations sur Bokeh, voir la leçon *Programming Historian* (en anglais) de Charlie Harper sur [Visualizing Data with Bokeh and Pandas](/en/lessons/visualizing-with-bokeh).

[^4]: Si vous travaillez avec des notebooks Jupyter, il y a une bonne chance que certaines dépendances soient déjà installées. En revanche, si vous travaillez avec un nouvel environnement Python ou dans un logiciel d'édition de code comme VS Code, il sera peut être nécessaire d'installer `ipykernel` (`pip install ipykernel`) et `nbformat` (`pip install nbformat`).

[^5]: Nous utiliserons aussi Numpy mais cette bibliothèque est automatiquement téléchargée avec l'installation de Pandas.

[^6]: Kaleido est une bibliothèque Python de génération d'images statiques (comme les formats JPG et SVG) et sera donc nécessaire pour exporter des visualisations statiques.
