---
title: "Réutilisation de code et modularité"
slug: reutilisation-de-code-et-modularite
original: code-reuse-and-modularity
layout: lesson
collection: lessons
date: 2012-07-17
translation_date: 2023-MM-DD
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
editors:
- Miriam Posner 
translator: 
- Célian Ringwald
translation-editor:
- Marie Flesch
translation-reviewer:
- Hee-Soo Choi
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/539
activity: transforming
python_warning: true
topics: [python]
avatar_alt: Trois visages caricaturés
abstract: "Un programme informatique peut vite devenir un très long fichier et ainsi devenir peu commode à maintenir, notamment quand aucune stratégie n'a été mise en place afin de contrôler cette complexité. Cette leçon sera l'occasion de vous expliquer comment réutiliser des parties de votre code à l'aide de l'écriture de fonctions, mais aussi comment organiser un programme en modules, de manière à rendre celui-ci plus concis et plus facile à débugger."
doi: 10.46430/phfr0024
---

{% include toc.html %}

# Objectifs de la leçon

Un programme informatique peut vite devenir un très long fichier et ainsi devenir peu commode à maintenir, notamment quand aucune stratégie n'a été mise en place afin de contrôler cette  complexité. Cette leçon sera l'occasion de vous expliquer comment réutiliser des parties de votre code à l'aide de l'écriture de *fonctions*, mais aussi comment organiser un programme en *modules*, de manière à rendre celui-ci plus concis et plus facile à débugger. En effet, être capable de repérer et de supprimer un module dysfonctionnel vous permettra d'économiser en temps et en efforts.

## Les fonctions

Dans la pratique, vous vous rendrez compte qu'il est souvent nécessaire de répéter certaines séries d'instructions, généralement parce que l'on est amené à réaliser certaines tâches à plusieurs reprises. Les programmes sont, pour la plupart, composés de routines qui sont assez robustes et générales pour être réutilisées. Elles sont connues sous le nom de fonction et Python propose un moyen de définir de nouvelles fonctions. Pour illustrer cela, observons un exemple simple de fonction. Supposons que vous souhaitez définir une fonction qui saluerait des personnes. Copiez la définition de cette fonction dans un éditeur de texte et sauvegardez-la dans un fichier nommé ```salutation.py```.

``` python
# salutation.py

def saluer(x):
    print("Bonjour " + x)

saluer("tout le monde")
saluer("Programming Historian")
```

La première ligne commençant par ```def``` est la déclaration de la fonction. Nous y définissons (&laquo;&#x202F;def&#x202F;&raquo;) une fonction qui s'appelle &laquo;&#x202F;saluer&#x202F;&raquo;. Le *paramètre* de la fonction est ```(x)```, vous comprendrez bientôt à quoi celui-ci va nous servir. La seconde ligne contient le code de notre fonction. Une fonction peut contenir autant de lignes que vous le souhaitez&#x202F;; dans notre cas, elle n'est composée que d'une ligne.

Notez que *l'indentation* est très importante en Python. L'espace avant le ```print``` contenu dans notre fonction ```saluer``` indique à l'interpréteur que nous nous situons au sein de &#x202F;la fonction. Nous en apprendrons plus à ce sujet plus tard&#x202F;; pour le moment, vérifiez que l'indentation dans votre fichier soit bien la même que celle que nous vous présentons. 
Lancez le programme. Vous devriez obtenir quelque chose ressemblant à cela&nbsp;:

``` python
Bonjour tout le monde
Bonjour Programming Historian
```

Cet exemple ne contient qu'une seule fonction&nbsp;: *saluer*. Celle-ci est &laquo;&#x202F;appelée&#x202F;&raquo; deux fois (on peut aussi dire qu'elle est &laquo;&#x202F;invoquée&#x202F;&raquo;). Appeler une fonction ou l'invoquer signifie juste que nous demandons au programme d'exécuter le code compris dans celle-ci. Nous avons ici appelé notre fonction avec deux paramètres différents. Éditez le fichier ```salutation.py```en invoquant à la fin de celui-ci une nouvelle fois notre fonction en remplaçant le paramètre par votre prénom. Lancez le programme, cela devrait éclairer ce que ```(x)``` représente dans la déclaration de la fonction.

Avant de passer à la prochaine étape, éditez ```salutation.py``` de manière à supprimer les appels de fonctions et en ne gardant que la déclaration de la fonction et son contenu. Nous allons maintenant apprendre à appeler une fonction depuis un autre programme. Lorsque vous aurez terminé, votre fichier ```salutation.py``` devrait ressembler à cela&nbsp;:

``` python
# salutation.py

def saluer(x):
    print("Bonjour " + x)
```

# Modularité

Dans notre exemple, le programme est très court et tient naturellement dans un unique fichier. Mais quand un programme contient un nombre important de lignes, il sera alors judicieux de le séparer en plusieurs  fichiers appelés *modules*.  Cette modularité facilitera grandement la maintenance de votre code, qui ne serait pas aussi évidente si vous le stockez dans un grand fichier. En effet, cette méthode de travail permet de travailler de manière indépendante sur chaque partie de votre code avant de les faire tenir toutes ensemble. En utilisant des modules, vous ne simplifierez pas seulement la réutilisation de votre code. Vous serez notamment capable de repérer plus facilement la source des erreurs de vos programmes. Lorsque vous divisez un programme en modules, vous n'êtes plus obligés de réécrire le détail de chaque procédure que vous souhaitez utiliser. Les autres modules n'ont pas besoin de savoir comment elle est codée s'ils n'en sont pas responsables. Ce principe est appelé &laquo;&#x202F;l'encapsulation&#x202F;&raquo;.

Supposons que vous construisiez une voiture. Vous pourriez commencer par ajouter une à une des pièces à celle-ci, mais il serait peut-être judicieux de commencer par construire et tester un module — comme par exemple un moteur — avant d'ajouter le reste. Le moteur lui-même pourrait être envisagé comme étant composé d'un certain nombre de modules, plus petits, comme un carburateur, un système  d'allumage, qui pourraient eux-mêmes être composés de modules, encore plus basiques et plus petits... Il en est de même lorsque l'on travaille sur un code informatique&nbsp;: on essaye de décomposer chaque problème en petits morceaux et de les résoudre un à un.

Vous avez déjà créé un module quand nous avons écrit le programme ```salutation.py```. Vous allez maintenant en écrire un second, ```utiliser-salutation.py```, qui comme l'indique son nom va *importer* le code du module pour en tirer parti. Python possède une instruction spécifique appelée ```import``` qui permet à un programme d'accéder au contenu d'un autre programme. C'est ce que nous allons utiliser.

Copiez ce code dans Komodo Edit et sauvegardez-le dans un fichier nommé `utiliser-salutation.py`. Ce fichier est votre programme, `salutation.py` est ici un module.

``` python
# utiliser-salutation.py

import salutation
salutation.saluer("Tout le monde")
salutation.saluer("Programming Historian")
```

Nous faisons ici plusieurs choses&nbsp;: premièrement, nous demandons à l'interpréteur d'*importer* (commande ```import``` ) le module ```salutation.py``` que nous avons créé précédemment.

Vous remarquerez aussi que nous ne pouvons pas appeler une fonction directement à travers son nom de cette manière&nbsp;: saluer("Tout le monde"), nous devons faire précéder celui-ci du nom du module suivi d'un point (.). Ce qui en clair signifie&nbsp;: lancez la fonction *saluer*, que vous devriez trouver dans le module ```salutation.py```.

Vous pouvez lancer alors le programme ```utiliser-salutation.py``` avec la commande &laquo;&#x202F;Run Python&#x202F;&raquo; de Komodo Edit. Notez que vous n'avez pas à lancer vous-même le module... mais seulement un programme qui fait appel à celui-ci. Si tout se passe bien, vous devriez voir les lignes suivantes s'afficher dans la sortie de Komodo Edit&nbsp;: 

``` python
Bonjour tout le monde
Bonjour Programming Historian
```

Avant de poursuivre les tutoriels suivants, assurez-vous de bien avoir compris la différence entre le chargement d'un fichier de données (ex. `helloworld.txt`) et l'importation d'un programme (e.g. `salutation.py`).

# Lectures suggérées

- [Python Basics](https://perma.cc/DLH4-2M8W)
