---
title: Manipuler des chaînes de caractères en Python
layout: lesson
slug: manipuler-chaines-caracteres-python
date: 2012-07-17
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
editors:
- Miriam Posner
translator:
- Camille Carette
translation-editor:
- François Dominic Laramée
translation-reviewer:
- Marie-Christine Boucher
- Florian Cafiero
translation_date: 2020-04-02
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/284
activity: transforming
topics: [python]
abstract: Cette leçon constitue une brève introduction aux techniques de manipulation des chaînes de caractères en Python.
# next: from-html-to-list-of-words-1
# previous: working-with-web-pages
python_warning: false
original: manipulating-strings-in-python
avatar_alt: Homme jouant la guitare
doi: 10.46430/phfr0008
---

{% include toc.html %}

## Objectifs de la leçon

Cette leçon constitue une courte introduction à la manipulation des [chaînes de caractères](https://fr.wikipedia.org/wiki/Cha%C3%AEne_de_caract%C3%A8res) en Python. Pour la plupart des tâches de traitement du langage naturel, il est crucial de savoir comment manipuler les chaînes de caractères. Si vous souhaitez mettre la leçon en pratique, vous pouvez écrire et exécuter des programmes courts dans votre environnement de programmation favori ou encore ouvrir un terminal en Python pour tester le code à la ligne de commande.

## Manipuler les chaînes de caractères en Python

Si vous avez déjà été confrontés à un autre langage de programmation auparavant, vous avez peut-être appris que vous aviez besoin de *déclarer* ou de *typer* vos variables avant de pouvoir y stocker des données. Ce n’est pas nécessaire lorsque l’on travaille avec Python. En effet, on peut simplement créer une chaîne de caractères en mettant entre guillemets le contenu de la variable et en utilisant le signe égal (=) :

```python
	message = "Bonjour le monde!"
```

## Les opérateurs de chaînes : additionner et multiplier

Une chaîne de caractères est une classe d’objets qui consiste en une série de caractères. Python sait déjà gérer un certain nombre de types de données polyvalents et puissants, y compris les chaînes de caractères. L’une des façons de manipuler ces chaînes de caractères est d’utiliser un *opérateur de chaînes*. Ces opérateurs sont représentés par des signes que l’on associe généralement avec les mathématiques, tels que +, -, \*, / et =. Lorsqu’on les utilise avec des chaînes de caractères, ces opérateurs effectuent des actions qui sont comparables, mais non similaires, à leurs équivalents mathématiques.

### Concaténer

Ce terme signifie “joindre des chaînes de caractères”. Ce processus est appelé *la concaténation de chaînes*, et s’effectue en utilisant l’opérateur plus (+). Notez qu’il vous faut indiquer explicitement là où vous voulez que des espaces apparaissent, en les mettant eux aussi entre des guillemets simples.

Dans cette exemple, on attribue le contenu “Bonjour le monde!” à la chaîne de caractères “message1”.

```python
	message1 = 'Bonjour le' + ' ' + 'monde'
	print(message1)
	-> Bonjour le monde
```

### Multiplier

Si vous voulez plusieurs copies d’une chaîne de caractères, utilisez l’opérateur de la multiplication (\*). Dans cet exemple, on attribue le contenu “bonjour” trois fois à la chaîne de caractères *message2a* et le contenu “le monde” à la chaîne de caractères *message2b*. Puis, nous imprimons ces deux chaînes.

``` python
	message2a = 'bonjour ' * 3
	message2b = 'le monde'
	print(message2a + message2b)
	-> bonjour bonjour bonjour le monde
```

### Ajouter

Que faire si vous souhaitez ajouter quelque chose à la fin d’une chaîne de caractères, à la suite du contenu ? Il existe un opérateur spécial conçu à cette fin (+=).

```python
	message3 = 'bonjour'
	message3 += ' '
	message3 += 'le monde'
	print(message3)
	-> bonjour le monde
```

## Méthodes pour les chaînes de caractères : rechercher, modifier

En plus des opérateurs, Python possède des douzaines de *méthodes* pré-installées qui nous permettent de manipuler les chaînes de caractères. Utilisées seules ou en combinaisons, ces méthodes peuvent appliquer à peu près toutes les opérations imaginables aux chaînes de caractères. Vous pouvez consulter une liste de ces méthodes sur [le site de Python](https://docs.python.org/3.8/library/stdtypes.html#string-methods), y compris des informations sur la manière de les utiliser correctement. Pour vous aider à bien démarrer votre exploration, voici un bref aperçu de quelques-unes des méthodes les plus couramment utilisées :

### Longueur

Vous pouvez déterminer le nombre de caractères contenus dans une chaîne de caractères à l'aide de `len`. Notez que l'espace blanc compte comme un caractère séparé.

```python
	message4 = 'bonjour' + ' ' + 'le monde'
	print(len(message4))
	-> 16
```

### Rechercher une sous-chaîne

Vous pouvez rechercher *une sous-chaîne* dans une chaîne de caractères et votre programme retournera la position de l'index de départ de cette sous-chaîne. Cela vous sera utile lors de nombreuses opérations plus complexes. Notez que les index sont numérotés de gauche à droite et que le décompte commence à la position 0 et non 1.

``` python
	message5 = "bonjour le monde"
	message5a = message5.find("mond")
	print(message5a)
	-> 11
```

Si la sous-chaîne n'est pas présente, le programme renvoie une valeur de -1.

``` python
	message6 = "bonjour le monde"
	message6b = message6.find("oiseau")
	print(message6b)
	-> -1
```

### Minuscules

Il est parfois utile de convertir une chaîne de caractères en minuscules. Par exemple, il est plus facile pour l'ordinateur de reconnaître que "Parfois" et "parfois" sont le même mot si nous standardisons les casses au préalable.

``` python
	message7 = "BONJOUR LE MONDE"
	message7a = message7.lower()
	print(message7a)
	-> bonjour le monde
```

L'effet inverse, qui consiste à transformer tous les caractères en majuscules, peut être obtenu en changeant `.lower()` en `.upper().`

### Remplacer

Si vous avez besoin de remplacer une sous-chaîne à l'intérieur d'une chaîne, vous pouvez le faire avec la méthode `replace`.

```python
	message8 = "BONJOUR LE MONDE"
	message8a = message8.replace("L", "pizza")
	print(message8a)
	-> BONJOUR pizzaE MONDE
```

### Couper (Slice)

Si vous voulez couper (`slice`) les parties non désirées au début ou à la fin d'une chaîne de caractères, vous pouvez le faire en créant une nouvelle chaîne à l'aide de l'opérateur ':'. La même technique vous permet également de diviser une longue chaîne de caractères en composantes plus faciles à gérer.

```python
	message9 = "Bonjour le monde"
	message9a = message9[1:9]
	print(message9a)
	-> onjour l
```

Vous pouvez substituer des variables aux entiers utilisés dans cet exemple.

```python
	debut = 2
	fin = 9
	message9b = message9[debut:fin]
	print(message9b)
	-> njour l
```

Le découpage d'une partie d'une chaîne facilite de beaucoup l'utilisation de cette méthode en conjonction avec la méthode `find`.  L'exemple suivant vérifie la présence de la lettre "d" dans les six premiers caractères de "Bonjour le monde" et nous dit correctement qu'elle n'est pas présente (-1). Cette technique est beaucoup plus utile dans des chaînes de caractères plus longues - des documents entiers par exemple. Notez que l'absence d'un entier avant les deux points signifie que nous voulons commencer au début de la chaîne. Nous pourrions utiliser la même technique pour dire au programme d'aller jusqu'au bout, en ne mettant aucun entier après les deux points. Et n'oubliez pas que l'on commence à compter les positions de l'indice à partir de 0 plutôt que de 1.

```python
	message9 = "Bonjour le monde"
	print(message9[:5].find("d"))
	-> -1
```

Il existe beaucoup d'autres méthodes de manipulation des chaînes, mais celles décrites ci-dessus constituent un bon début. Notez que dans ce dernier exemple, nous utilisons des crochets au lieu de parenthèses. Cette différence de syntaxe signale une distinction importante. En Python, les parenthèses sont généralement utilisées pour passer un *argument* à une fonction. Donc quand on voit quelque chose comme

```python
	print(len(message7))
```

cela signifie passer la chaîne de caracteres "message" à la fonction `len`, puis envoyer la valeur retournée par cette fonction à l'instruction d'impression (`print`). Si une fonction peut être appelée sans argument, vous devez souvent inclure une paire de parenthèses vides après le nom de la fonction. Nous en avons aussi vu un exemple :

```python
	message7 = "BONJOUR LE MONDE"
	message7a = message7.lower()
	print(message7a)
	-> bonjour le monde
```

Cette instruction demande à Python d'appliquer la fonction `lower` à la chaîne "message7", puis de stocker la valeur retournée dans la chaîne *message7a*.

Les crochets ont une fonction différente. Si vous concevez une chaîne de caractères comme une séquence de caractères, et que vous voulez accéder à une partie du contenu de la chaîne en spécifiant son emplacement dans la séquence, alors vous avez évidemment besoin d'un moyen d'indiquer à Python un emplacement dans une séquence. C'est ce que font les crochets : indiquer un emplacement de début et de fin dans une séquence, comme nous l'avons vu en utilisant la méthode `slice`.

## Séquence d'échappement

Que faire lorsque vous devez inclure des guillemets dans une chaîne de caractères ? Vous ne voulez pas que l'interpréteur Python se méprenne et mette fin à la chaîne lorsqu'il rencontre l'un de ces caractères. En Python, vous pouvez placer une barre oblique inversée devant un guillemet pour que ce guillemet ne termine pas la chaîne. C'est ce qu'on appelle les *séquences d'échappement*.

```python
	print('\"')
	-> "
```

```python
	print('Le programme imprime \"Bonjour le monde!\"')
	-> Le programme imprime "Bonjour le monde!"
```

Deux autres séquences d'échappement vous permettent d'imprimer des tabulateurs et des fins de lignes :

```
	print('bonjour\tbonjour\tbonjour\nle monde')
	->bonjour bonjour bonjour
	le monde
```

## Bibliographie
- Mark Lutz, *[Learning Python](http://www.worldcat.org/oclc/1061273329)*
	- Ch. 7: Strings *(Chaînes de caractères)*
	- Ch. 8: Lists and Dictionaries *(Listes et dictionnaires)*
	- Ch. 10: Introducing Python Statements *(Introduction aux déclarations en Python)*
	- Ch. 15: Function Basics *(Les fondamentaux des fonctions en Python)*

## Synchronisation de code

Pour suivre les leçons à venir, il est important d'avoir les bons fichiers et programmes dans votre répertoire programming-historian. À la fin de chaque chapitre, vous pouvez télécharger le fichier zip de programming-historian pour vous assurer que vous avez le bon code. Notez que nous avons supprimé les fichiers inutiles des leçons précédentes. Votre répertoire peut contenir plus de fichiers et c'est OK !

- programming-historian-1 ([zip](/assets/python-lessons1.zip))

Super ! Vous êtes maintenant prêt à passer à [la leçon suivante](/en/lessons/from-html-to-list-of-words-1) (en anglais).
