---
title: "Analyse de réseau avec Python"
slug: analyse-reseau-python
original: exploring-and-analyzing-network-data-with-python
layout: lesson
collection: lessons
date: 2017-08-23
translation_date: 2024-04-19
authors:
- John R. Ladd
- Jessica Otis
- Christopher N. Warren
- Scott Weingart
reviewers:
- Elisa Beshero-Bondar
- Anne Chao
- Qiwei Li
editors:
- Brandon Walsh
translator:
- Laurent Beauguitte
translation-editor:
- Émilien Schultz
translation-reviewer:
- Lucie Loubère
- Léo Mignot
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/582
activity: analyzing
topics: [network-analysis]
abstract: "Cette leçon présente différents indicateurs de réseau et la manière de les interpréter lorsque l'on travaille avec des données relationnelles en sciences humaines et sociales. Vous apprendrez à utiliser la bibliothèque Python NetworkX pour calculer et interpréter ces indicateurs."
avatar_alt: Des voies ferrées qui se croisent
doi: 10.46430/phfr0032
---

{% include toc.html %}

## Introduction

### Objectifs de la leçon

Cette leçon vous apprendra à&nbsp;:

- utiliser le module [NetworkX](https://perma.cc/KG6X-AWN5) pour traiter des données relationnelles avec [Python](/fr/lecons/introduction-et-installation) et
- analyser des données relationnelles afin de&nbsp;:
  - caractériser la structure du réseau et la longueur des chemins
  - détecter les sommets centraux
  - détecter les communautés et les sous-groupes

<div class="alert alert-info">
Cette leçon concerne l'analyse des réseaux. Il se concentre sur les indicateurs et leur interprétation, non sur la visualisation des données relationnelles. Pour combiner analyse et visualisation de vos données, nous recommandons la leçon de <i>Programming Historian</i> &laquo;&nbsp;From Hermeneutics to Data to Networks: Data Extraction and Network Visualization of Historical Sources&nbsp;&raquo; disponible <a href="/en/lessons/creating-network-diagrams-from-historical-sources">en anglais</a> et <a href="/es/lecciones/creando-diagramas-de-redes-desde-fuentes-historicas">en espagnol</a>.
</div>

### Prérequis

Cette leçon suppose que vous avez&nbsp;:

- des notions de base concernant l'analyse de réseau[^1] et/ou que vous avez lu [&laquo;&nbsp;From Hermeneutics to Data to Networks: Data Extraction and Network Visualization of Historical Sources&nbsp;&raquo;](/en/lessons/creating-network-diagrams-from-historical-sources) de Martin Düring (leçon disponible en anglais et en espagnol)
- installé Python 3 (voir le [Hitchhiker's Guide to Python](https://perma.cc/7M6A-LGZ3))
- installé le package `pip`[^2]

### Qu'apprendre des données relationnelles&nbsp;?

Les réseaux intéressent depuis longtemps les universitaires et un certain nombre d'entre eux est passé d'une approche essentiellement qualitative et métaphorique des relations à des outils quantitatifs plus formels pour étudier notamment les intermédiaires, les hubs (sommets adjacents à un grand nombre de liens) et les structures fortement connectées. Comme l'a souligné le sociologue Mark Granovetter dans son important article de 1973 intitulé [&laquo;&nbsp;The Strength of Weak Ties&nbsp;&raquo;](https://perma.cc/H25B-ZA73), remarquer que deux personnes sont connectées l'une à l'autre est rarement suffisant. Des facteurs tels que leur relation structurelle avec d'autres personnes et le fait que ces personnes soient elles-mêmes liées les unes aux autres ont une influence décisive sur les évènements. Dans la mesure où même les universitaires les plus perspicaces ont des difficultés à appréhender la forme générale d'un réseau (sa &laquo;&nbsp;topologie&nbsp;&raquo;) et à identifier les sommets les plus importants reliant les différents groupes, l'analyse quantitative des réseaux offre un moyen de se déplacer de manière relativement fluide entre l'objet social appréhendé dans son ensemble (le &laquo;&nbsp;graphe&nbsp;&raquo;), les caractéristiques des individus et la nature des liens sociaux étudiés.

Cette leçon peut vous aider à répondre à des questions telles que&nbsp;:

- quelle est la structure d'ensemble du réseau&nbsp;?
- quels sont les sommets importants&nbsp;?
- quels sont les sous-groupes ou communautés présent·es&nbsp;?

### Notre exemple&nbsp;: les quakers (Société religieuse des Amis)

Bien avant qu'il n'y ait des ami·es sur Facebook, il y avait la &laquo;&nbsp; Société des Amis &nbsp;&raquo;, connue sous le nom de quakers. Fondés en Angleterre au milieu du XVIIe siècle, les quakers étaient des chrétien·nes protestantes qui s'opposaient à l'Église officielle d'Angleterre et prônaient une large tolérance religieuse, préférant la &laquo;&nbsp;lumière intérieure&nbsp;&raquo; et la conscience des chrétien·nes à l'orthodoxie imposée par l'État. Le nombre de quakers a augmenté rapidement entre le milieu et la fin du XVIIe siècle et leurs membres se sont répandus dans les iles britanniques, en Europe et dans les colonies du Nouveau Monde - en particulier en Pennsylvanie, colonie fondée par le leader quaker William Penn et où vivent les quatre auteurs et autrices de cette leçon.

Les universitaires ayant depuis longtemps lié la croissance des effectifs et la pérennité des quakers à l'efficacité de leurs réseaux, les données utilisées dans cette leçon sont une liste de noms et de relations parmi les premiers quakers du XVIIe siècle. Ce jeu de données est issu du *[Oxford Dictionary of National Biography](http://www.oxforddnb.com)* et du projet *[Six Degrees of Francis Bacon](https://perma.cc/Q63S-UZTU)* qui reconstruit les réseaux sociaux du début de la Grande-Bretagne moderne (1500-1700).

## Préparation des données et installation de NetworkX

Avant de commencer cette leçon, vous devez télécharger deux fichiers qui constituent notre jeu de données relationnelles. Le fichier [quakers_nodelist.csv](/assets/exploring-and-analyzing-network-data-with-python/quakers_nodelist.csv) est une liste de quakers du début de l'ère moderne (sommets) et le fichier [quakers_edgelist.csv](/assets/exploring-and-analyzing-network-data-with-python/quakers_edgelist.csv) est une liste de relations entre ces quakers (liens[^3]). 

Il est important de se familiariser avec la structure des données avant de continuer. Pour en savoir plus sur la structure générale des données de réseau, consultez [cette leçon](/en/lessons/creating-network-diagrams-from-historical-sources#developing-a-coding-scheme) (disponible en anglais et en espagnol). 

Lorsque vous ouvrez le fichier de sommets dans le programme de votre choix, vous constatez que chaque quaker est principalement identifié·e par son nom (`Name`). Chaque sommet possède également un certain nombre d'attributs&nbsp;: l'importance historique (`Historical Significance`), le genre (`Gender`), les dates de naissance (`Birthdate`) et de décès (`Deathdate`) et l'ID SDFB (`ID`) - cet identifiant numérique unique permet de faire la jointure entre ce jeu de données et les données originales *Six Degrees of Francis Bacon*. Voici les premières lignes&nbsp;:

```
Name,Historical Significance,Gender,Birthdate,Deathdate,ID
Joseph Wyeth,religious writer,male,1663,1731,10013191
Alexander Skene of Newtyle,local politician and author,male,1621,1694,10011149
James Logan,colonial official and scholar,male,1674,1751,10007567
Dorcas Erbery,Quaker preacher,female,1656,1659,10003983
Lilias Skene,Quaker preacher and poet,male,1626,1697,10011152
```

Dans un fichier au format `.csv`, la virgule est le séparateur par défaut permettant de créer des colonnes lorsqu'on importe le fichier dans un tableur ou un logiciel d'analyse de données.

Lorsque vous ouvrez le fichier des liens, vous constatez que nous utilisons les noms présents dans le fichier des sommets pour identifier ces derniers. Les liens commencent à un sommet &laquo;&nbsp;source&nbsp;&raquo; (`Source`) et se terminent à un sommet &laquo;&nbsp;cible&nbsp;&raquo; (`Target`). Bien que ces termes soient issus de l'analyse des réseaux dits &laquo;&nbsp;orientés&nbsp;&raquo;, nous considérons nos données comme un réseau &laquo;&nbsp;non orienté&nbsp;&raquo;&nbsp;: si une personne A connait une personne B, alors cette dernière doit également connaitre la personne A. Dans les réseaux orientés, les relations ne sont pas nécessairement réciproques (une personne A peut envoyer une lettre à B sans en recevoir une en retour)&nbsp;; dans les réseaux non orientés, les liens sont toujours réciproques ou &laquo;&nbsp;symétriques&nbsp;&raquo; (le lien peut également être porteur d'une intensité ou d'un poids, généralement appelé &laquo;&nbsp;weight&nbsp;&raquo; en anglais, on parle alors de réseau valué ou pondéré). Étant donné qu'il s'agit d'un réseau de connaissances, considérer que les relations sont non orientées est le plus approprié. Les relations symétriques dans un réseau non orienté sont utiles chaque fois qu'il s'agit de relations qui jouent le même rôle pour les deux parties. Deux ami·es ont une relation symétrique&nbsp;: iels sont chacun l'ami·e de l'autre. L'auteur ou l'autrice et le ou la destinataire d'une lettre ont une relation asymétrique car chacun·e joue un rôle différent. Les réseaux orientés et non orientés offrent chacun leurs potentialités (et parfois leurs mesures spécifiques) et vous devez choisir celui qui convient le mieux au type de relations que vous collectez et aux questions auxquelles vous voulez répondre. Voici les premiers liens du réseau non orienté des quakers&nbsp;:

```
Source,Target
George Keith,Robert Barclay
George Keith,Benjamin Furly
George Keith,Anne Conway Viscountess Conway and Killultagh
George Keith,Franciscus Mercurius van Helmont
George Keith,William Penn
```

Maintenant que vous avez téléchargé les données Quaker et vu comment elles sont structurées, il est temps de commencer à travailler avec ces données à l'aide de Python. Une fois Python et pip installés (voir [Prérequis](#prérequis) ci-dessus), vous devez installer NetworkX, en tapant ceci dans votre ligne de commande (voir notre leçon disponible [en anglais](/en/lessons/intro-to-bash) et [en espagnol](/es/lecciones/introduccion-a-bash))[^4]&nbsp;:

```
pip3 install networkx==3.2
```

La version stable de NetworkX est la 3.2. Si vous rencontrez des problèmes avec le code ci-dessous et que vous avez déjà travaillé avec NetworkX, vous devez mettre à jour le paquet ci-dessus avec `pip3 install networkx==3.2 --upgrade`.

C'est bon ! Vous pouvez commencer à coder.

## Premières manipulations

### Lire les fichiers, importer les données

Créez un fichier texte dans le même répertoire que vos fichiers de données et nommez-le `quaker_network.py`. (Pour plus de détails sur l'installation et l'utilisation de Python avec Mac, voir [cette leçon](/en/lessons/mac-installation).) Les premières lignes de ce fichier permettent d'importer les bibliothèques dont vous avez besoin&nbsp;: celle que nous venons d'installer et deux bibliothèques Python intégrées. Vous pouvez taper&nbsp;:

```python
import csv
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community # Les fonctions de détection de communautés de la bibliothèque NetwokX doivent être importées séparément.
```

Vous pouvez maintenant demander au programme de lire vos fichiers `.csv` et de récupérer les données dont vous avez besoin. Ironiquement, la lecture des fichiers et la réorganisation des données nécessitent souvent un code plus complexe que les fonctions d'analyse de réseau. Voici un ensemble de commandes pour ouvrir et lire la liste de sommets (`nodelist`) et la liste de liens (`edgelist`)&nbsp;:

```python
with open('quakers_nodelist.csv', 'r') as nodecsv: # Ouvrir le fichier des sommets
    nodereader = csv.reader(nodecsv) # Lire le csv
    # Récupérer les données (en utilisant la gestion et le découpage des listes Python pour supprimer la ligne d'en-tête, voir note de bas de page 3)
    nodes = [n for n in nodereader][1:]

node_names = [n[0] for n in nodes] # Créer une liste des noms de sommets

with open('quakers_edgelist.csv', 'r') as edgecsv: # Ouvrir le fichier des liens
    edgereader = csv.reader(edgecsv) # Lire le csv
    edges = [tuple(e) for e in edgereader][1:] # Récupérer les données
```

Ce code exécute des fonctions similaires à celles de [cette leçon](/fr/lecons/travailler-avec-des-fichiers-texte) mais utilise le module CSV pour charger sommets et liens.[^5] Vous obtiendrez plus d'informations sur les sommets plus tard mais pour l'instant vous avez besoin de deux éléments&nbsp;: la liste complète des sommets et une liste de paires de liens (en tant que couple de sommets). Ce sont les formes dont NetworkX a besoin pour créer un objet `Graph`, objet spécifique à NetworkX que vous découvrirez dans la section suivante.

À ce stade, avant de commencer à utiliser NetworkX, vous pouvez faire quelques contrôles de base pour vous assurer que vos données sont correctement chargées en utilisant les fonctions et méthodes intégrées de Python. Tapez&nbsp;:

```python
print(len(node_names))
```

et

```python
print(len(edges))
```

pour savoir combien de sommets et de liens vous avez réussi à charger dans Python. Si vous obtenez 119 sommets et 174 liens, vous avez réussi à charger toutes les données nécessaires.

### Les bases de NetworkX&nbsp;: créer le réseau

Vous avez maintenant vos données sous forme de deux listes Python&nbsp;: une liste de sommets (`node_names`) et une liste de liens (`edges`). Dans NetworkX, vous pouvez rassembler ces deux listes en un seul objet réseau. Cet objet est appelé `Graph`, en référence à l'un des termes courants pour les données relationnelles [N.B. il ne s'agit pas d'une représentation visuelle des données. Le terme graphe est utilisé ici dans un sens purement mathématique, d'analyse de réseau]. Vous devez d'abord créer un objet `Graph` avec la commande suivante&nbsp;:

```python
G = nx.Graph()
```

Ceci crée un nouvel objet `Graph` vide nommé `G`. Vous pouvez maintenant ajouter vos listes de sommets et de liens&nbsp;:

```python
G.add_nodes_from(node_names)
G.add_edges_from(edges)
```

C'est l'une des nombreuses façons d'ajouter des données à un objet `Graph`. Vous pouvez consulter la [documentation NetworkX](https://perma.cc/W9DA-ZE75) pour des informations sur l'ajout de liens pondérés (liens porteurs d'une intensité) ou l'ajout incrémental de sommets et de liens.

Enfin, vous pouvez obtenir des informations de base sur votre réseau nouvellement créé en tapant `print(nom_de_l_objet)`&nbsp;:

```python
print(G)
```

La ligne de code `print(G)` renvoie trois éléments&nbsp;: le type de réseau (orienté ou non orienté), le nombre de sommets et le nombre de liens. 

C'est un moyen rapide d'obtenir des informations générales sur votre graphe mais, comme vous l'apprendrez dans les sections suivantes, cela ne fait qu'effleurer la surface de ce que NetworkX peut vous dire sur vos données.

Votre script devrait ressembler maintenant à ceci&nbsp;:

```python
import csv
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community

# Lire la liste des sommets
with open('quakers_nodelist.csv', 'r') as nodecsv:
    nodereader = csv.reader(nodecsv)
    nodes = [n for n in nodereader][1:]

# Obtenir la liste des noms des sommets (premier élément de chaque ligne)
node_names = [n[0] for n in nodes]

# Lire la liste des liens
with open('quakers_edgelist.csv', 'r') as edgecsv:
    edgereader = csv.reader(edgecsv)
    edges = [tuple(e) for e in edgereader][1:]

# Afficher nombre de sommets (ordre du graphe) et nombre de liens (taille du graphe)
print(len(node_names))
print(len(edges))

G = nx.Graph() # Créer un objet Graph
G.add_nodes_from(node_names) # Ajouter les sommets
G.add_edges_from(edges) # Ajouter les liens
print(G) # Afficher les informations basiques
```

Jusqu'à présent, vous avez lu les données relatives aux sommets et aux liens dans Python à partir de fichiers `.csv` puis vous avez compté ces sommets et ces liens. Vous avez ensuite créé un objet `Graph` à l'aide de NetworkX et chargé vos données dans cet objet.

### Ajouter des attributs

Pour NetworkX, un objet `Graph` est un objet (le réseau) composé de deux éléments (les sommets et les liens). Jusqu'à présent, vous avez chargé des sommets et des liens (en tant que paires de sommets) mais NetworkX vous permet d'ajouter des &laquo;&nbsp;attributs&nbsp;&raquo; aux sommets et aux liens. Plus tard dans cette leçon, vous calculerez des indicateurs et ajouterez certains des résultats au graphe en tant qu'attributs. Pour l'instant, assurons-nous que votre graphe contient tous les attributs qui se trouvent actuellement dans notre CSV.

Revenez à la liste `nodes` que vous avez créée au début de votre script. Cette liste contient toutes les lignes de `quakers_nodelist.csv`, y compris les colonnes pour le nom, l'importance historique, le sexe, l'année de naissance, l'année de décès et l'ID SDFB. Vous allez devoir parcourir cette liste à l'aide d'une boucle et ajouter ces informations à l'objet `Graph`. Il y a plusieurs façons de faire, mais NetworkX fournit deux fonctions pratiques pour ajouter des attributs à tous les sommets et/ou liens d'un graphe en une seule fois&nbsp;: `nx.set_node_attributes()` et `nx.set_edge_attributes()`. Pour utiliser ces fonctions, vos données attributaires doivent être sous forme de dictionnaires Python dans lesquels les noms de sommets sont les &laquo;&nbsp;clés&nbsp;&raquo; et les attributs que vous voulez ajouter les &laquo;&nbsp;valeurs&nbsp;&raquo;.[^6] Vous devez créer un dictionnaire pour chacun de vos attributs puis les ajouter en utilisant les fonctions ci-dessus. La première chose à faire est de créer cinq dictionnaires vides en utilisant des accolades&nbsp;:

```python
hist_sig_dict = {}
gender_dict = {}
birth_dict = {}
death_dict = {}
id_dict = {}
```

Maintenant, nous pouvons itérer sur la liste `nodes` et ajouter les éléments appropriés à chaque dictionnaire. Pour ce faire, nous connaissons à l'avance la position, ou &laquo;&nbsp;index&nbsp;&raquo;, de chaque attribut. Notre fichier `quaker_nodelist.csv` étant bien structuré, nous savons que le nom de la personne est toujours le premier élément de la liste, l'index 0, puisque vous commencez toujours à compter avec 0 en Python. L'importance historique de la personne est l'index 1, son sexe est l'index 2 et ainsi de suite. Nous pouvons donc construire nos dictionnaires comme suit[^7]&nbsp;:

```python
for node in nodes: # Boucle parcourant la liste ligne par ligne
    hist_sig_dict[node[0]] = node[1]
    gender_dict[node[0]] = node[2]
    birth_dict[node[0]] = node[3]
    death_dict[node[0]] = node[4]
    id_dict[node[0]] = node[5]
```

Vous disposez maintenant d'un ensemble de dictionnaires que vous pouvez utiliser pour ajouter des attributs aux sommets de votre objet `Graph`. La fonction `set_node_attributes` prend trois arguments&nbsp;: le graphe auquel vous ajoutez l'attribut, le dictionnaire des paires clés-attribut et le nom du nouvel attribut. Le code pour ajouter vos cinq attributs ressemble à ceci&nbsp;:

```python
nx.set_node_attributes(G, hist_sig_dict, 'importance_historique')
nx.set_node_attributes(G, gender_dict, 'genre')
nx.set_node_attributes(G, birth_dict, 'annee_naissance')
nx.set_node_attributes(G, death_dict, 'annee_deces')
nx.set_node_attributes(G, id_dict, 'sdfb_id')
```

Maintenant, tous vos sommets ont ces cinq attributs et vous pouvez y accéder à tout moment. Par exemple, vous pouvez afficher toutes les années de naissance de vos sommets en les parcourant et en accédant à l'attribut `birth_year` comme ceci&nbsp;:

```python
for n in G.nodes(): # Boucle sur chaque sommet, dans nos données "n" est le nom de la personne.
    print(n, G.nodes[n]['annee_naissance']) # Accéder à chaque sommet par son nom puis par l'attribut "annee_naissance"
```

Avec cette instruction, vous obtenez une ligne en sortie pour chaque sommet du réseau. Elle devrait ressembler à une simple liste de noms et d'années&nbsp;:

```
Anne Camm 1627
Sir Charles Wager 1666
John Bellers 1654
Dorcas Erbery 1656
Mary Pennyman 1630
Humphrey Woolrich 1633
John Stubbs 1618
Richard Hubberthorne 1628
Robert Barclay 1648
William Coddington 1601
```

Les étapes ci-dessus constituent une méthode courante d'ajout d'attributs aux sommets que vous utiliserez à plusieurs reprises dans la suite de la leçon. Voici un récapitulatif du bloc de code de cette section&nbsp;:

```python
# Créer un dictionnaire vide pour chacun des attributs
hist_sig_dict = {}
gender_dict = {}
birth_dict = {}
death_dict = {}
id_dict = {}

for node in nodes: # Boucle parcourant ligne par ligne la liste des sommets
    hist_sig_dict[node[0]] = node[1] # Accès à l'item correct, ajout au dictionnaire correspondant
    gender_dict[node[0]] = node[2]
    birth_dict[node[0]] = node[3]
    death_dict[node[0]] = node[4]
    id_dict[node[0]] = node[5]

# Ajouter chaque dictionnaire comme attribut à l'objet Graph
nx.set_node_attributes(G, hist_sig_dict, 'importance_historique')
nx.set_node_attributes(G, gender_dict, 'genre')
nx.set_node_attributes(G, birth_dict, 'annee_naissance')
nx.set_node_attributes(G, death_dict, 'annee_deces')
nx.set_node_attributes(G, id_dict, 'sdfb_id')

# Boucle parcourant chaque sommet pour accéder à et afficher tous les attributs année de naissance ("annee_naissance")
for n in G.nodes():
    print(n, G.nodes[n]['annee_naissance'])
```

Vous avez maintenant appris à créer un objet `Graph` et à lui ajouter des attributs. Dans la section suivante, vous découvrirez une variété d'indicateurs disponibles dans NetworkX et comment y accéder. Mais pas d'inquiétude, vous connaissez maintenant l'essentiel du code dont vous aurez besoin pour le reste de la leçon&nbsp;!

## Indicateurs disponibles dans NetworkX

Lorsque vous commencez à travailler sur un nouveau jeu de données, il est bon de se faire une idée générale de ce dernier. La première étape, décrite ci-dessus, consiste simplement à ouvrir les fichiers et à voir ce qu'ils contiennent. Comme il s'agit d'un réseau, vous savez qu'il y aura des sommets et des liens, mais combien y en a-t-il&nbsp;? Et quelles informations sont jointes à ces sommets ou liens&nbsp;?

Dans notre cas, il y a 174 arêtes et 119 sommets. Ces liens sont non orientés (il existe une relation symétrique entre les personnes) et ne contiennent pas d'informations supplémentaires. Pour les sommets, nous connaissons leur nom, leur importance historique, leur sexe, leurs dates de naissance et de décès et leur ID SDFB.

Ces caractéristiques indiquent ce que vous pouvez ou devez faire avec votre jeu de données. S'il y a trop peu de sommets (15, par exemple), une analyse de réseau est moins utile que l'exploration visuelle des données&nbsp;; s'il y en a trop (15 millions par exemple), vous devriez envisager de commencer par extraire un sous-ensemble ou de trouver un superordinateur.

Les propriétés du réseau guident également votre analyse. Comme ce réseau est non orienté, votre analyse doit utiliser des mesures qui supposent des relations symétriques entre les sommets. Par exemple, vous pouvez déterminer les communautés dans lesquelles les gens se retrouvent mais vous ne pouvez pas déterminer les chemins orientés par lesquels les informations peuvent circuler dans le réseau (vous auriez besoin d'un réseau orienté pour cela). En utilisant les relations symétriques non orientées, vous êtes en mesure de trouver des communautés et les personnes qui sont importantes pour ces communautés, un processus qui serait plus difficile (bien que toujours possible) avec un réseau orienté. NetworkX vous permet d'effectuer la plupart des analyses que vous pouvez imaginer mais vous devez comprendre les potentialités de votre jeu de données et réaliser que certains algorithmes NetworkX sont plus appropriés que d'autres.

### La forme du réseau

Après avoir vu à quoi ressemble le jeu de données, il est important de voir à quoi ressemble le réseau. Il s'agit de deux choses différentes. Le jeu de données est une représentation abstraite de ce que vous supposez être des relations entre des entités&nbsp;; le réseau est l'instanciation spécifique de ces hypothèses. Le réseau, du moins dans ce contexte, est la manière dont l'ordinateur lit les relations que vous avez encodées dans un jeu de données. Un réseau a une [topologie](https://perma.cc/V9C8-9V5H), ou une forme, qui peut être peu ou fortement centralisée, dense ou clairsemée, cyclique ou linéaire. Un jeu de données n'en a pas, en dehors de la structure du tableau dans lequel il est stocké.

La forme et les propriétés de base du réseau vous donneront une idée de ce avec quoi vous travaillez et des analyses qui semblent pertinentes. Vous connaissez déjà le nombre de sommets et de liens mais à quoi ressemble le réseau&nbsp;? Les sommets se regroupent-ils ou sont-ils répartis de manière égale&nbsp;? Existe-t-il des structures complexes ou chaque sommet est-il disposé le long d'une ligne droite&nbsp;?

La visualisation ci-dessous, créée avec l'outil de visualisation de réseaux [Gephi](https://gephi.org/), vous donne une idée de la topologie de ce réseau.[^8] Vous pouvez créer un graphique similaire dans Palladio en suivant [cette leçon](/en/lessons/creating-network-diagrams-from-historical-sources).

{% include figure.html filename="exploring-and-analyzing-network-data-with-python-1.png" alt="Visualisation des données Quaker par un algorithme force-based, figure créée avec Gephi. La taille de chaque sommet est fonction de son degré (nombre de liens adjacents) ; les sommets les plus connectés sont placés par l'algorithme au centre de la figure."  caption="Figure 1. Visualisation des données Quaker avec un algorithme force-based, créée avec Gephi" %}

Il existe de nombreuses façons de visualiser un réseau et l'utilisation d'un [algorithme de spatialisation force-based](https://perma.cc/CE22-PSYU), dont l'image ci-dessus est un exemple, est l'une des plus courantes. Les algorithmes force-based tentent de trouver l'emplacement optimal des sommets à l'aide d'un calcul basé sur la [loi de Hooke](https://perma.cc/JPB5-ZLKP) ce qui, pour les graphes de taille petite ou moyenne, permet souvent de créer des visualisations efficaces car faciles à lire. La visualisation ci-dessus montre qu'il existe une seule grande &laquo;&nbsp;composante&nbsp;&raquo; de sommets connectés (au centre) et plusieurs petites composantes avec seulement un ou deux liens (sur les côtés). Il s'agit d'une structure de réseau assez courante. Le fait de savoir qu'il y a plusieurs composantes dans le réseau limite les calculs que vous pouvez effectuer sur celui-ci. En faisant varier la taille des sommets en fonction du nombre de liens (indicateur appelé &laquo;&nbsp;degré&nbsp;&raquo;, voir ci-dessous), la visualisation montre également qu'il y a quelques sommets avec beaucoup de liens qui assurent la cohésion de la composante principale. Ces grands sommets sont appelés &laquo;&nbsp;hubs&nbsp;&raquo; et le fait qu'ils apparaissent si clairement ici vous donne un indice sur ce que vous trouverez lorsque vous mesurerez la centralité de degré dans la section suivante.

Les visualisations n'ont toutefois qu'une portée limitée. Plus vous travaillerez sur des réseaux, plus vous vous rendrez compte que la plupart d'entre eux se ressemblent tellement qu'il est difficile de les distinguer les uns des autres. Les mesures permettent de différencier les réseaux, d'en apprendre plus sur leur topologie et de transformer un amas de sommets et de liens en un objet utile pour votre recherche.

Une mesure basique mais utile est la &laquo;&nbsp;densité&nbsp;&raquo; du réseau. Il s'agit du rapport entre le nombre de liens présents et le nombre de liens possibles dans le réseau. Dans un réseau non orienté comme celui-ci, il pourrait y avoir un lien entre chaque paire de sommets mais, comme vous l'avez noté sur la visualisation, seuls quelques-uns des liens possibles sont réellement présents. La densité du réseau vous donne une information rapide sur le niveau d'interconnexion dans votre réseau.

La bonne nouvelle, c'est que la plupart des mesures nécessitent de simples commandes d'une ligne en Python. Vous pouvez désormais continuer à construire votre bloc de code à partir des sections précédentes. Vous n'avez pas besoin d'effacer ce que vous avez déjà tapé et, parce que vous avez créé votre objet réseau `G` dans le bloc de code ci-dessus, tous les indicateurs listés par la suite devraient fonctionner correctement.

Vous pouvez calculer la densité du réseau avec la fonction `nx.density(G)`. Cependant, il est recommandé de stocker votre indicateur dans une variable pour pouvoir l'utiliser ultérieurement&nbsp;:

```python
density = nx.density(G)
print("Densité du réseau :", density)
```

Le résultat du calcul de la densité est un nombre. La densité de notre réseau est ici d'environ 0,0248 (2.48 % des liens possibles sont présents)&nbsp;; ce n'est donc pas un réseau très dense, ce qui correspond à ce que vous pouvez voir dans la visualisation.[^9] Un 0 signifierait qu'il n'y a aucun lien (réseau &laquo;&nbsp;vide&nbsp;&raquo;) et un 1 indiquerait que tous les liens possibles sont présents (réseau &laquo;&nbsp;complet&nbsp;&raquo;)&nbsp;: le réseau quaker se situe dans la partie inférieure de cette échelle mais il est encore loin de 0.

La mesure du plus court chemin est un peu plus complexe. Elle calcule la suite de sommets et de liens la plus courte possible entre deux sommets, ce qui est difficile à voir dans les visualisations de grands réseaux. Cette mesure consiste essentiellement à trouver des ami·es d'ami·es - si ma mère connaît quelqu'un que je ne connais pas alors ma mère est le plus court chemin entre moi et cette personne. Le jeu de données *Six Degrees of Kevin Bacon*, dont [notre projet](https://perma.cc/Q63S-UZTU) tire son nom, consiste essentiellement à trouver les  plus courts chemins (avec une longueur de chemin inférieure ou égale à six) entre Kevin Bacon et n'importe quelle autre personne.

Pour calculer un plus court chemin, vous devez fournir plusieurs arguments (informations que vous donnez à une fonction Python)&nbsp;: le nom de l'objet `Graph`, le sommet source et le sommet cible. Trouvons le plus court chemin entre Margaret Fell et George Whitehead. Puisque nous avons utilisé des noms pour identifier de manière unique nos sommets dans le réseau, il est possible d'accéder à ces sommets (en tant que source et cible de votre chemin) en utilisant directement leurs noms.

```python
fell_whitehead_path = nx.shortest_path(G, source="Margaret Fell", target="George Whitehead")

print("Plus court chemin entre Fell et Whitehead:", fell_whitehead_path)
```

Le temps de calcul est fonction de la taille de votre réseau puisque Python cherche d'abord tous les chemins possibles puis sélectionne le plus court. La sortie de `shortest_path` est une liste de sommets qui inclut la source (Fell), la cible (Whitehead), et les sommets entre eux. Ici, nous pouvons voir que le fondateur quaker George Fox se trouve sur le plus court chemin entre les deux. Comme Fox est également un &laquo;&nbsp;hubs&nbsp;&raquo; (voir ci-dessous degré de centralité) avec de nombreuses relations, nous pouvons supposer que plusieurs plus courts chemins passent par lui en tant qu'intermédiaire. Qu'est-ce que cela peut nous apprendre sur l'importance des fondateurs et fondatrices quakers pour leur réseau social (au sens sociologique du terme)&nbsp;?

Python possède de nombreux outils permettant de calculer les plus courts chemins. Dans la [documentation](https://perma.cc/TV2J-LGDK), il existe des fonctions pour calculer la longueur des plus courts chemins, pour calculer tous les plus courts chemins et pour déterminer si un chemin existe ou non. Vous pouvez utiliser une fonction distincte pour trouver la longueur du chemin de Fell-Whitehead que nous venons de calculer ou vous pouvez simplement prendre la longueur de la liste moins un,[^10] comme ceci&nbsp;:

```python
print("Longueur de ce chemin :", len(fell_whitehead_path)-1)
```

Il existe de nombreuses mesures de réseau dérivées des longueurs des plus courts chemins dont le diamètre, qui est la plus longue de toutes les distances les plus courtes. Après avoir calculé tous les plus courts chemins entre toutes les paires de sommets dans le réseau, le diamètre est la longueur du chemin entre les deux sommets les plus éloignés. Le diamètre donne une idée de la compacité globale du réseau en mesurant la distance d’une extrémité du réseau à l’autre.

Le diamètre se calcule à l'aide de la fonction `nx.diameter(G)`. Cependant, l’exécution de cette commande sur le réseau Quaker produit une erreur vous indiquant que le graphe est &laquo;&nbsp;non connexe&nbsp;&raquo;. Cela signifie simplement que votre réseau, comme vous l’avez déjà vu, possède plus d’une composante. Comme il y a des sommets qui n’ont aucun chemin vers d’autres, il est impossible de trouver tous les plus courts chemins. Examinez de nouveau la visualisation de votre réseau&nbsp;:

{% include figure.html filename="exploring-and-analyzing-network-data-with-python-1.png" alt="Visualisation des données Quaker par un algorithme force-based, figure créée avec Gephi. La taille de chaque sommet est fonction de son degré (nombre de liens adjacents) ; les sommets les plus connectés sont placés par l'algorithme au centre de la figure."  caption="Figure 2. Visualisation des données Quaker avec un algorithme force-based, créée avec Gephi" %}

Comme il n’existe pas de chemin entre les sommets d’une composante et les sommets d’une autre, `nx.diameter()` renvoie l’erreur &laquo;&nbsp;not connected&nbsp;&raquo;. Vous pouvez remédier à cela en cherchant d’abord si votre réseau est connexe (tous les sommets appartiennent à la même composante) et, si ce n'est pas le cas, en trouvant la plus grande composante et en calculant le diamètre de celle-ci. Voici le code&nbsp;:

```python
# Si votre réseau n'est pas connexe, la fonction renvoie `False`.
print(nx.is_connected(G))

# Utilisez nx.connected_components pour obtenir le nombre de composantes
# puis utilisez la fonction max() pour trouver la plus grande:
components = nx.connected_components(G)
largest_component = max(components, key=len)

# Créez un sous-graphe correspondant à la plus grande composante
# Calculez le diamètre de ce sous-graphe comme vous l'avez fait avec la densité.

subgraph = G.subgraph(largest_component)
diameter = nx.diameter(subgraph)
print("Diamètre de la plus grande composante :", diameter)
```

Puisque nous avons pris la plus grande composante, nous pouvons supposer que le diamètre des autres composantes est inférieur. Par conséquent, ce résultat est adapté pour le diamètre de l’ensemble du réseau. Le diamètre du réseau de la plus grande composante de ce réseau est de 8&nbsp;: il existe un chemin composé de 8 liens entre les deux sommets les plus éloignés dans le réseau. Contrairement à la densité qui varie entre 0 à 1, il est difficile de savoir si 8 est un grand ou un petit diamètre. Pour certaines mesures globales, il peut être préférable de les comparer à des réseaux de taille et de forme similaires.[^11]

Le dernier calcul structurel que nous ferons sur ce réseau concerne le concept de &laquo;&nbsp;fermeture triadique&nbsp;&raquo;. La fermeture triadique suppose que, si deux personnes A et B connaissent la même personne C, les personnes A et B sont susceptibles de se connaitre. Si Fox connait à la fois Fell et Whitehead, alors il est probable que Fell et Whitehead se connaissent. Visuellement, cela donne un triangle (ou triade fermée) reliant Fox, Fell et Whitehead. Le nombre de ces triangles dans le réseau peut être utilisé pour trouver des groupes et des communautés de personnes qui se connaissent toutes assez bien.

Une façon de mesurer la fermeture triadique est appelée &laquo;&nbsp;coefficient de clustering&nbsp;&raquo; en raison de cette tendance au regroupement mais la mesure structurelle est connue sous le nom de &laquo;&nbsp;transitivité&nbsp;&raquo;.[^12] La transitivité est le rapport de toutes les triades fermées sur toutes les triades présentes. Une triade est présente chaque fois qu’une personne (Fox) connait deux personnes (Fell et Whitehead). La transitivité, comme la densité, exprime à quel point un graphe est interconnecté en rapportant le  nombre de relations présentes au nombre de relations possibles. N’oubliez pas que les mesures comme la transitivité et la densité concernent les probabilités plutôt que les certitudes. Toutes les sorties de votre script Python doivent être interprétées avec précaution, ce qui est valable pour tout objet de recherche. La transitivité vous permet de penser à toutes les relations dans votre graphe qui pourraient exister, mais qui n’existent pas réellement.

Vous pouvez calculer la transitivité avec une ligne de code, de la même manière que vous avez calculé la densité&nbsp;:

```python
triadic_closure = nx.transitivity(G)
print("Fermeture triadique :", triadic_closure)
```

Tout comme la densité, la transitivité varie entre 0 à 1, et vous pouvez voir que la transitivité du réseau est d’environ 0,1694, ce qui est légèrement supérieur à sa densité (0,0248). Comme le graphe n’est pas très dense, il y a moins de triades présentes, ce qui peut entrainer une transitivité légèrement plus élevée. Autrement dit, les sommets qui ont déjà beaucoup de relations sont susceptibles de faire partie de ces triades fermées. Pour confirmer cela, il est temps de s'intéresser aux sommets ayant de nombreuses relations.

### Centralités

Après avoir obtenu quelques mesures basiques de la structure d'ensemble du réseau, une étape pertinente consiste à chercher quels sommets sont les plus importants. En analyse de réseau, les mesures de l’importance des sommets sont appelées &laquo;&nbsp;mesures de centralité&nbsp;&raquo;. Comme il existe de nombreuses façons de répondre à la question &laquo;&nbsp;Quels sommets sont les plus importants?&nbsp;&raquo;, il existe de nombreuses façons de calculer la centralité. Ici, vous apprendrez trois des mesures de centralité les plus courantes&nbsp;: le degré (degree), la centralité d'intermédiarité (betweenness) et la centralité de vecteur propre (eigenvector).

Le degré est la façon la plus simple et la plus courante d'identifier les sommets importants. Le degré d’un sommet est la somme des liens qui lui sont adjacents. Si un sommet a trois liens vers d’autres sommets, son degré est de trois. S'il a cinq liens, son degré est de cinq. C’est vraiment aussi simple que cela. Puisque chacun de ces liens a toujours un sommet à l’autre extrémité, vous pouvez interpréter le degré comme le nombre de personnes auxquelles une personne donnée est directement connectée. Les sommets avec les degrés les plus élevés dans un réseau social sont les personnes qui connaissent le plus de gens. Ces sommets sont souvent appelés &laquo;&nbsp;hubs&nbsp;&raquo; et le calcul du degré est le moyen le plus rapide de les identifier.

Le calcul de la centralité pour chaque sommet dans NetworkX n’est pas aussi simple que les indicateurs à l’échelle du réseau mais il s’agit encore de fonctions d'une seule ligne. Toutes les fonctions de cette section produisent des dictionnaires dans lesquels les clés sont des sommets et les valeurs des mesures de centralité. Cela signifie qu’ils sont prêts à être ajoutés à votre réseau en tant qu’attribut de sommet, comme vous l’avez fait précédemment. Commencez par calculer le degré et ajoutez-le en tant qu’attribut à votre réseau.

```python
degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degre')
```

Vous venez d’exécuter la méthode `G.degree` sur tous les sommets de votre réseau (`G.nodes()`). Puisque vous l’avez ajouté comme attribut, vous pouvez maintenant afficher le degré de William Penn avec ses autres attributs en accédant directement à ce sommet&nbsp;:

```python
print(G.nodes['William Penn'])
```

Ces résultats peuvent être utilisés de manière plus intéressante. Puisque vous êtes déjà en Python, vous pouvez les trier et les comparer. Vous pouvez utiliser la fonction `sorted()` pour trier un dictionnaire par ses clés ou ses valeurs et afficher par exemple les vingt premiers sommets classés par degré. Pour ce faire, vous devrez utiliser `itemgetter` que nous avons importé au début de la leçon. À l’aide des termes `sorted` et `itemgetter`, vous pouvez trier le dictionnaire des degrés comme suit&nbsp;:

```python
sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
```

La ligne ci-dessus peut paraitre obscure mais concentrez-vous sur les trois arguments que vous avez donnés à `sorted()`. Le premier est le dictionnaire `degree_dict.items()` que vous voulez trier. La seconde est l'élément du dictionnaire à trier&nbsp;: dans ce cas, l’élément 1 est le deuxième élément de la paire, soit la valeur de votre dictionnaire. Enfin, vous demandez à `sorted()` de trier par ordre décroissant (`reverse=True`) afin que les sommets au degré le plus élevé soient les premiers dans la liste obtenue. Une fois que vous avez créé cette liste, vous pouvez la parcourir avec une boucle et utiliser le découpage de liste[^13] pour obtenir uniquement les 20 premiers sommets&nbsp;:

```python
print("Les 20 sommets les plus centraux (degré) :")
for d in sorted_degree[:20]:
    print(d)
```

Comme vous pouvez le voir, le degré de Penn est de 18, ce qui est relativement élevé pour ce réseau. Afficher ce classement permet d'illustrer les limites du degré comme mesure de centralité. Vous n’aviez probablement pas besoin de NetworkX pour savoir que William Penn, leader quaker et fondateur de la Pennsylvanie, était important. La plupart des réseaux sociaux ont seulement quelques hubs avec un degré très élevé et avec le reste des sommets avec un degré beaucoup plus faible.[^14] Le degré renseigne sur les hubs mais n'apprend pas grand-chose sur les autres sommets. Et, dans de nombreux cas, ces hubs (comme Penn ou Margaret Fell, co-fondatrice des quakers, avec un degré de 13) ne sont pas particulièrement surprenants. Dans ce réseau, presque tous les hubs sont des fondateurs et fondatrices de la religion ou des personnalités politiques importantes.

Heureusement, il existe d'autres mesures de centralité qui permettent de hiérarchiser les sommets. La [centralité de vecteur propre](https://perma.cc/JJC8-NK64) est une version du degré qui pondère la centralité d'un sommet en fonction de la centralité de ses voisins. La centralité du vecteur propre se préoccupe de savoir si vous êtes un hub mais aussi de connaitre le nombre de hubs auxquels vous êtes connecté·e. Elle renvoie une valeur comprise entre 0 et 1&nbsp;: plus elle est proche de 1, plus la centralité est élevée. La centralité du vecteur propre est utile pour comprendre quels sommets peuvent transmettre rapidement des informations à de nombreux autres sommets. Si vous connaissez un grand nombre de personnes bien connectées, vous pouvez diffuser un message de manière très efficace. Si vous avez utilisé Google, vous connaissez déjà un peu la centralité du vecteur propre&nbsp;: son algorithme PageRank utilise une extension de cette formule pour déterminer quelles pages web sont placées en tête de ses résultats de recherche.

La [centralité d'intermédiarité](https://perma.cc/87W6-3SVM) est un peu différente des deux précédentes métriques dans la mesure où elle ne se préoccupe pas du nombre de liens adjacents à un sommet ou à un ensemble de sommets. La centralité d'intermédiarité examine tous les plus courts chemins qui passent par un sommet particulier (voir ci-dessus). Pour ce faire, elle doit d'abord calculer tous les plus courts chemins possibles dans le réseau. La centralité d'intermédiarité est donc plus longue à calculer que les autres mesures de centralité (cela ne pose pas de problème avec un jeu de données de cette taille). La centralité d'intermédiarité, qui est également exprimée sur une échelle de 0 à 1, est assez efficace pour trouver les sommets qui relient deux parties d'un réseau qui seraient séparées sans la présence de ces sommets. Si vous êtes le seul élément à relier deux groupes, toutes les communications entre ces groupes doivent passer par vous&nbsp;; ce type de sommet est souvent appelé &laquo;&nbsp;broker&nbsp;&raquo;. La centralité d'intermédiarité n'est pas le seul moyen d'identifier les brokers (d'autres méthodes sont plus systématiques) mais c'est un moyen rapide pour identifier les sommets qui sont importants, non pas parce qu'ils ont eux-mêmes beaucoup de liens, mais parce qu'ils se situent entre les groupes, ce qui confère au réseau connexité et cohésion.

Ces deux mesures de centralité sont plus simples à utiliser que le degré&nbsp;; elles n’ont pas besoin d’avoir comme argument une liste de sommets, le graphe `G` suffit. Vous pouvez les exécuter avec les fonctions suivantes&nbsp;:

```python
betweenness_dict = nx.betweenness_centrality(G) # Calcul de la centralité d'intermédiarité
eigenvector_dict = nx.eigenvector_centrality(G) # Calcul de la centralité de vecteur propre

# Transformation en attributs du réseau
nx.set_node_attributes(G, betweenness_dict, 'betweenness')
nx.set_node_attributes(G, eigenvector_dict, 'eigenvector')
```

Vous pouvez trier la centralité d'intermédiarité (ou de vecteur propre) en changeant le nom de la variable dans le code ci-dessus&nbsp;:

```python
sorted_betweenness = sorted(betweenness_dict.items(), key=itemgetter(1), reverse=True)

print("Les 20 sommets les plus centraux (intermédiarité) :")
for b in sorted_betweenness[:20]:
    print(b)
```

Vous remarquerez que la plupart des sommets qui ont un degré élevé ont également une centralité d'intermédiarité élevée. La centralité d'intermédiarité met cependant en évidence deux femmes, Elizabeth Leavens et Mary Penington, dont le degré est plus faible. Un avantage de faire ces calculs en Python est que vous pouvez rapidement comparer deux ensembles de résultats. Il est facile de mettre en évidence les sommets ayant une forte intermédiarité et un faible degré (ou l'inverse). Vous pouvez combiner les listes triées auparavant&nbsp;:

```python
# Obtenir les 20 sommets ayant la plus forte intermédiarité sous forme de liste
top_betweenness = sorted_betweenness[:20]

# Les récupérer et afficher leur degré
for tb in top_betweenness: # Boucle dans top_betweenness
    degree = degree_dict[tb[0]] # Utiliser degree_dict pour récupérer les degrés des sommets, voir note 3
    print("Nom:", tb[0], "| Centralité d'intermédiarité:", tb[1], "| Degré:", degree)
```

Ces résultats confirment  que certaines personnes, comme Leavens et Penington, ont une centralité d'intermédiarité élevée mais un faible degré. Cela pourrait signifier que ces femmes étaient des intermédiaires importants, reliant des parties éloignées du réseau. Vous pouvez aussi apprendre des choses inattendues sur des gens que vous connaissez déjà — dans cette liste, vous pouvez voir que Penn a un degré inférieur à celui du fondateur de la religion quaker, George Fox, mais une plus grande centralité d'intermédiarité. En résumé, connaitre un plus grand nombre de gens n’est pas tout.

Cette section ne fait qu’effleurer ce qu'il est possible de faire avec les indicateurs de réseau en Python. NetworkX propose des dizaines de fonctions et de mesures pour différents types de réseaux et vous pouvez utiliser Python pour adapter ces mesures de manière presque illimitée. Un langage de programmation comme Python ou R vous donne une grande flexibilité pour explorer votre réseau, flexibilité que d’autres interfaces ne vous permettent pas. Combiner et comparer les résultats statistiques de votre réseau avec d’autres attributs de vos données (comme les dates et les professions que vous avez ajoutées au réseau au début de cette leçon) est un atout majeur.

## Usage avancé de NetworkX&nbsp;: détection de communautés à l'aide de la modularité

Une autre famille de méthodes fréquemment utilisée en analyse de réseau est la recherche de sous-groupes ou de communautés. Votre réseau forme-t-il une grande famille heureuse où tout le monde se connait&nbsp;? S’agit-il à l'inverse d’un ensemble de petits sous-groupes faiblement reliés les uns aux autres par une poignée d'intermédiaires&nbsp;? Le domaine de la détection de communautés dans les réseaux est conçu pour répondre à ces questions. Il existe de nombreuses façons de calculer des &laquo;&nbsp;communautés&nbsp;&raquo;, des &laquo;&nbsp;cliques&nbsp;&raquo; et des &laquo;&nbsp;clusters&nbsp;&raquo; dans un réseau mais la méthode la plus populaire actuellement est basée sur la &laquo;&nbsp;modularité&nbsp;&raquo;. La modularité est une mesure de la densité relative de votre réseau&nbsp;: une communauté (appelée &laquo;&nbsp;module&nbsp;&raquo; ou &laquo;&nbsp;classe de modularité&nbsp;&raquo;) a une densité interne élevée mais peu de liens avec les sommets extérieurs. La modularité vous donne un score global relatif à la structure de votre réseau et ce score peut être utilisé pour partitionner le réseau et détecter les communautés individuelles.[^15]

Les réseaux très denses sont souvent plus difficiles à diviser en partitions pertinentes. Heureusement, comme vous l’avez déjà mis en évidence, ce réseau n’est pas très dense. La densité n'est pas très élevée et il y a plusieurs composantes. Partitionner ce réseau peu dense en utilisant la modularité est pertinent afin d'examiner si le résultat a un sens historique et analytique.

La détection de communautés et le partitionnement dans NetworkX nécessitent un peu plus de lignes de code que certains des indicateurs vus précédemment&nbsp;:

```python
communities = community.greedy_modularity_communities(G)
```

La méthode `greedy_modularity_communities()` tente de déterminer le nombre de communautés pertinentes dans le graphe et regroupe tous les sommets en sous-ensembles en fonction de ces communautés. Contrairement aux fonctions de centralité, le code ci-dessus ne crée pas de dictionnaire&nbsp;: il crée une liste d’objets spéciaux appelés &laquo;&nbsp;frozenset&nbsp;&raquo; (similaires aux listes). On obtient un ensemble pour chaque communauté et les différentes communautés contiennent les noms des personnes de chaque groupe. Pour ajouter ces informations comme attributs à votre réseau, vous devez d’abord créer un dictionnaire qui étiquette chaque personne avec une valeur numérique correspondant à la communauté à laquelle elle appartient&nbsp;:

```python
modularity_dict = {} # Créer un dictionnaire vide
for i,c in enumerate(communities): # Boucle parcourant la liste des communautés et gardant la trace de leur numéro
    for name in c: # Boucle parcourant chaque personne dans la communauté
        modularity_dict[name] = i # Création d'une entrée dans le dictionnaire pour la personne avec sa communauté d'appartenance

# Vous pouvez maintenant ajouter les informations de modularité comme nous l’avons fait pour les autres indicateurs
nx.set_node_attributes(G, modularity_dict, 'modularity')
```

Comme toujours, vous pouvez combiner ces mesures avec d’autres. Voici comment trouver les sommets ayant une forte centralité de vecteur propre dans la classe de modularité 0 (la première)&nbsp;:

```python
# Obtenir une liste de sommets d'une communauté donnée
class0 = [n for n in G.nodes() if G.nodes[n]['modularity'] == 0]

# Créer le dictionnaire des centralités de vecteur propre de ces sommets
class0_eigenvector = {n:G.nodes[n]['eigenvector'] for n in class0}

# Trier ce dictionnaire et afficher les 5 premiers résultats
class0_sorted_by_eigenvector = sorted(class0_eigenvector.items(), key=itemgetter(1), reverse=True)

print("Classe de modularité 0 triée par centralité de vecteur propre :")
for node in class0_sorted_by_eigenvector[:5]:
    print("Nom:", node[0], "| Centralité de vecteur propre :", node[1])
```

L’utilisation de la centralité de vecteur propre peut vous donner une idée des personnes importantes au sein de cette classe de modularité. Vous remarquerez que certaines de ces personnes, en particulier William Penn, William Bradford et James Logan, ont passé beaucoup de temps en Amérique. En outre, Bradford et Tace Sowle étaient tous deux des imprimeurs quakers de premier plan. En creusant un peu, nous pouvons découvrir qu’il existe des raisons à la fois géographiques et professionnelles susceptibles d'expliquer la présence de cette communauté. Ceci semble indiquer que la modularité fonctionne comme prévu.

Dans les petits réseaux comme celui-ci, une tâche fréquente est de trouver et de lister toutes les classes de modularité et leurs membres.[^16] Vous pouvez le faire à l'aide d'une boucle&nbsp;:

```python
for i,c in enumerate(communities): # Boucle parcourant la liste des communautés
    if len(c) > 2: # Exclusion des communautés ayant 1 ou 2 sommets
        print('Class '+str(i)+':', list(c)) # Afficher les communautés et leurs membres
```

Notez que dans le code ci-dessus vous excluez toutes les classes de modularité avec deux sommets ou moins avec la ligne `if len(c) > 2`. La visualisation originale montre qu’il y a beaucoup de petites composantes avec seulement deux sommets. Chacune de ces composantes est considérée comme une classe de modularité puisqu’elle n'est connectée à aucun autre sommet. En les filtrant, vous obtenez une meilleure idée des classes de modularité pertinentes au sein de la composante principale du réseau.

Travailler avec NetworkX permet d'en apprendre beaucoup sur les classes de modularité. Mais vous voudrez presque toujours visualiser vos données (et peut-être exprimer les classes en faisant varier la couleur des sommets). Dans la section suivante, vous apprendrez comment exporter vos données NetworkX pour les utiliser avec d’autres bibliothèques Python ou d'autres logiciels.

## Exporter les données

NetworkX prend en charge un très grand nombre de formats de fichiers pour [exporter les données](https://perma.cc/Z7H3-UMKD). Si vous voulez exporter une liste de liens en format texte à charger dans Palladio, il existe un [outil adapté](https://perma.cc/DWK2-J389). Fréquemment, dans le projet *Six Degrees of Francis Bacon*, nous exportons les données NetworkX en [format JSON d3](https://perma.cc/2STT-F466) pour les visualiser dans un navigateur. Vous pouvez aussi [exporter](https://perma.cc/7UCP-YBX4) votre graphe en tant que [tableau de données Pandas](http://pandas.pydata.org/) si vous souhaitez effectuer des manipulations statistiques plus avancées. Il existe de nombreuses options et, si vous avez ajouté toutes vos mesures dans votre objet `Graph` en tant qu’attributs, toutes vos données seront exportées simultanément.

La plupart des options d’exportation fonctionnent à peu près de la même manière. Dans cette leçon, vous apprendrez comment exporter vos données au format GEXF de Gephi. Une fois le fichier exporté, vous pouvez le charger [directement dans Gephi](https://perma.cc/46UZ-F6PU) pour le visualiser.

L’exportation de données se fait souvent avec une commande d’une seule ligne&nbsp;: il vous suffit de choisir un nom de fichier. Dans ce cas, nous utiliserons `quaker_network.gexf`. Pour exporter, tapez&nbsp;:

```python
nx.write_gexf(G, 'quaker_network.gexf')
```

C’est tout ! Lorsque vous exécutez votre script Python, il place automatiquement le nouveau fichier GEXF dans le même répertoire que votre fichier Python.[^17]

## Synthétiser les résultats

Après avoir traité et examiné un ensemble de mesures de réseau en Python, vous disposez d'éléments permettant de formuler des arguments et de tirer des conclusions sur ce réseau de quakers du début de l'ère moderne en Grande-Bretagne. Vous savez que le réseau a une densité relativement faible, ce qui suggère des relations lâches et/ou des données originales incomplètes. Vous savez que la communauté est organisée autour de plusieurs hubs parmi lesquels les fondateurs et fondatrices comme Margaret Fell et George Fox, ainsi que d'importants leaders politiques et religieux comme William Penn. Plus utile encore, vous connaissez l'existence de femmes au degré relativement faible, comme Elizabeth Leavens et Mary Penington qui, en raison de leur forte centralité d'intermédiarité, ont pu jouer le rôle de brokers en reliant plusieurs groupes entre eux. Enfin, vous avez appris que le réseau est constitué d'une grande composante et de nombreuses très petites. Au sein de cette grande composante, il existe plusieurs communautés distinctes dont certaines semblent organisées en fonction du temps ou de l'espace (comme Penn et ses associés américains). Grâce aux métadonnées que vous avez ajoutées à votre réseau, vous disposez des outils nécessaires pour explorer plus avant ces indicateurs et expliquer éventuellement certaines des caractéristiques structurelles que vous avez identifiées.

Chacun de ces résultats est une invitation à poursuivre la recherche plutôt qu'un aboutissement ou une preuve définitive. L'analyse de réseau est un ensemble d'outils permettant de poser des questions ciblées sur la structure des relations au sein d'un jeu de données et NetworkX fournit une interface relativement simple pour un grand nombre de ces méthodes et mesures. Les réseaux sont un moyen utile d'étendre votre recherche à un groupe en fournissant des informations sur la structure de la communauté. Nous espérons que cette leçon vous incitera à utiliser ces mesures pour enrichir vos propres recherches et explorer la richesse de l'analyse de réseau, qui ne se limite pas à la visualisation.

## Notes de fin

[^1]: Ensemble de concepts et de méthodes étudiant des relations entre des individus, au sens statistique du terme, en partie basé sur la théorie des graphes&nbsp;; un réseau est constitué d'un ensemble de liens (relations) entre des sommets (individus).
[^2]: Dans la plupart des cas, `pip` ou `pip3` est installé automatiquement avec Python3.
[^3]: NdT: J'ai choisi de traduire &laquo;&nbsp;node(s)&nbsp;&raquo; par &laquo;&nbsp;sommet(s)&nbsp;&raquo; et non par &laquo;&nbsp;nœuds&nbsp;&raquo;. Les deux termes sont utilisés en français en théorie des graphes et en analyse de réseau et ils sont parfaitement synonymes. J'ai traduit &laquo;&nbsp;edge&nbsp;&raquo; par &laquo;&nbsp;lien&nbsp;&raquo; qui me parait plus générique qu'&laquo;&nbsp;arête&nbsp;&raquo; (lien non orienté) et moins thématiquement connoté que &laquo;&nbsp;relation&nbsp;&raquo;.
[^4]: Certaines installations vous demanderont de taper `pip` sans le `3` mais, dans Python 3, `pip3` est le plus courant. Si l'un ne fonctionne pas, essayez l'autre&nbsp;!
[^5]: Le module CSV permet d'importer des données tabulaires stockées dans ce format. Il s'agit d'une des options possibles pour importer des données de ce type.
[^6]: Les dictionnaires sont un type de données intégré à Python, composé de paires clé-valeur. Une clé est le mot-clé d'un dictionnaire et une valeur sa définition. Les clés doivent être uniques (une seule par dictionnaire) mais les valeurs peuvent être n'importe quoi. Les dictionnaires sont représentés par des accolades, les clés et les valeurs étant séparées par des deux-points&nbsp;: `{clé1:valeur1, clé2:valeur2, ...}`. Les dictionnaires sont l'un des moyens les plus rapides pour stocker des valeurs que vous devez utiliser ensuite. Un objet `Graph` dans NetworkX est constitué de dictionnaires imbriqués.
[^7]: Notez que ce code utilise les crochets de deux manières. Il utilise des nombres entre crochets pour accéder à des indices spécifiques dans une liste de sommets (par exemple, l'année de naissance dans `node[4]`) mais il utilise aussi des crochets pour assigner une *clé* (toujours `node[0]`, ID) à n'importe lequel de nos dictionnaires vides&nbsp;: `dictionnaire[clé] = valeur`. Pratique&nbsp;!
[^8]: Nous avons supprimé à des fins pédagogiques tous les sommets qui ne sont pas connectés à d'autres. Notre objectif était d'alléger le jeu de données mais il est courant d'avoir un grand nombre de sommets isolés.
[^9]: N'oubliez pas qu'il s'agit de la densité de l'ensemble du réseau, composantes non connectées comprises. Il existe un grand nombre de relations possibles. Si vous preniez la densité de la plus grande composante, vous obtiendriez un résultat différent. Vous pourriez le faire en trouvant la plus grande composante, comme nous vous le montrerons dans la section suivante sur le diamètre, puis en calculant la densité de cette seule composante.
[^10]: Nous prenons la longueur de la liste moins un car nous voulons connaitre le nombre de liens (ou d'étapes) entre les sommets et non le nombre de sommets.
[^11]: La façon la plus courante pour ce genre de comparaison est de créer des graphes aléatoires de même taille pour voir si les résultats obtenus diffèrent de la norme. NetworkX offre de nombreux outils pour [générer des graphes aléatoires](https://perma.cc/EZ7M-966N).
[^12]: Pourquoi parle-t-on de transitivité&nbsp;? Vous avez peut-être déjà rencontré la notion de propriété transitive en géométrie&nbsp;: si A=B et B=C alors A=C. De même, dans la fermeture triadique, si la personne A connait la personne B et que la personne B connait la personne C, alors la personne A connait (probablement) la personne C&nbsp;: c'est ce qu'on appelle la transitivité.
[^13]: Quelques techniques spécifiques à Python sont utilisées dans ce code. La première est la compréhension de liste qui intègre des boucles (`for n in nodes`) pour créer de nouvelles listes (entre crochets), comme par exemple&nbsp;: `nouvelle_liste = [item for item in ancienne_liste]`. La seconde est le découpage de liste, qui vous permet de subdiviser ou de &laquo;&nbsp;trancher&nbsp;&raquo; une liste. La notation de découpage de liste `[1 :]` prend tout excepté le premier élément de la liste. Le 1 indique à Python de commencer par le deuxième élément de la liste (en Python, on commence à compter à 0) et les deux points indiquent à Python de tout prendre jusqu'à la fin de la liste. Étant donné que la première ligne de ces deux listes est la ligne d'en-tête de chaque fichier `.csv`, nous ne voulons pas que ces en-têtes soient inclus dans nos données.
[^14]: Celles et ceux d'entre vous qui ont une formation en statistiques remarqueront que le degré dans certains réseaux suit une loi de puissance mais ce n'est ni inhabituel ni particulièrement utile à savoir. (NdT&nbsp;: cette note est discutable dans la mesure où une hiérachie très forte des degrés oriente sur les mécanismes expliquant la création des liens entre sommets - voir les nombreux travaux mettant en évidence des mécanismes d'attachement préférentiel, c'est-à-dire la tendance pour les nouveaux sommets à se connecter aux sommets les plus centraux.)
[^15]: Bien que nous ne l’abordions pas dans cette leçon, c’est généralement une bonne pratique de calculer d’abord le score global de modularité pour déterminer si vous apprendrez quoi que ce soit en partitionnant votre réseau. Pour connaitre le score global de modularité, prenez les communautés que vous allez calculer ensuite avec `communities = community.best_partition(G)` et exécutez `global_modularity = community.modularity (communities, G)`. Ensuite, il suffit d’exécuter `print(global_modularité)`.
[^16]: Dans les grands réseaux, les listes seraient probablement trop longues mais il est possible de se faire une idée des classes détectées en visualisant le réseau et en colorant les sommets en fonction de leur classe.
[^17]: Chaque format de fichier exportable est également importable. Si vous avez un fichier GEXF (Gephi) que vous voulez importer dans NetworkX, vous pouvez taper `G = nx.read_gexf('nom_fichier.gexf')`.
