---
title: Installation de bibliothèques Python avec pip
layout: lesson
slug: installation-modules-python-pip
authors: 
- Fred Gibbs
reviewers:
- Ben Hurwitz
- Amanda Morton
date: 2013-05-06
translation_date: 2021-01-06
translator: 
- Lucas Terriel
translation-reviewer: 
- François Dominic Laramée
translation-editor:
- Sofia Papastamkou
difficulty: 1
activity: acquiring
topics: [get-ready, python]
abstract: "Il existe de nombreuses manières d'installer des bibliothèques Python externes; cette leçon explique l'une des méthodes les plus courantes utilisant pip."
exclude_from_check:
  - editors
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/320
original: installing-python-modules-pip
avatar_alt: Branche avec poires
doi: 10.46430/phfr0015
---


{% include toc.html %}


Objectifs de la leçon
-----------------------

Cette leçon vous présente la manière de télécharger et d'installer des bibliothèques Python en plus des bibliothèques standards distribuées (built-in) avec le langage de base. Il existe de nombreuses façons d'installer des bibliothèques externes, ici nous allons utiliser un programme appelé [pip], facilement installable sur les distributions [Mac/Linux/Windows]. Depuis Python 3.4, pip est inclus dans l’installation par défaut. Si pour quelque raison que ce soit vous avez besoin d'installer ou mettre à jour vous-même pip, ces instructions devraient vous aider.


Présentation des bibliothèques
-----------------

L'un des principaux avantages dans l'utilisation de Python est le nombre important de bibliothèques de code qui sont mises à la disposition des programmeurs. Elles permettent d'économiser du temps de programmation, ou simplement de rendre une tâche spécifique (comme la création d'un fichier [CSV](https://fr.wikipedia.org/wiki/Comma-separated_values), ou la copie d'information d'une page web de manière automatique - *scraping*) beaucoup plus facile. Quand vous recherchez des solutions à des problèmes sur Google, vous trouverez souvent des exemples de code qui utilisent des bibliothèques dont vous n'avez jamais entendu parler auparavant. Ne les laissez pas vous impressionner ! Une fois ces bibliothèques installées sur votre ordinateur, vous pouvez les utiliser en les important au début de votre code; vous pouvez importer autant de bibliothèques que vous le souhaitez, par exemple :

```python
import csv
import requests
import kmlwriter
import pprint
```
Pour les nouveaux utilisateurs de Python, il peut être quelque peu intimidant de télécharger et d'installer des bibliothèques externes la première fois. Il existe de nombreuses façons de le faire, ce qui ajoute ainsi de la confusion; cette leçon présente l'une des plus simples et des plus couramment utilisées.

Le but ici est d'installer un gestionnaire sur votre ordinateur qui peut télécharger et installer automatiquement des bibliothèques Python pour vous. Ce programme s'appelle [pip].


### Instructions pour Mac et Linux

Selon la documentation de [pip], nous pouvons installer un *script* Python qui se chargera d'installer `pip` pour nous. En utilisant un Mac ou un Linux, nous pouvons installer `pip` via la ligne de commande en utilisant la [commande curl], qui télécharge le *script* [Perl](https://fr.wikipedia.org/wiki/Perl_(langage)) d'installation de `pip`.  

```bash
$ curl -O https://bootstrap.pypa.io/get-pip.py
```
Une fois que vous avez téléchargé le fichier **get-pip.py**, vous devez l'exécuter avec l'interpréteur Python. Cependant, si vous essayez d’exécuter le *script* avec Python de cette manière :

```bash
$ python get-pip.py
```
le *script* échouera très probablement, car il n'aura pas les permissions pour mettre à jour certains répertoires de votre système de fichiers, qui sont par défaut définis de sorte que les *scripts* de provenance inconnue ne puissent pas modifier les fichiers importants et vous transmettre des virus. Dans ce cas - et dans les cas où vous devez autoriser un *script* dans lequel vous avez confiance à écrire dans votre système - vous pouvez utiliser la commande `sudo` (abréviation de "Super User Do") devant la commande Python, tel que :

```bash
$ sudo python get-pip.py
```

### Instructions pour Windows

Comme pour les distributions précédentes, la façon la plus simple d'installer `pip` est d'utiliser un programme Python appelé **get-pip.py**, que vous pouvez télécharger [ici](https://bootstrap.pypa.io/get-pip.py). Lorsque vous ouvrez ce lien, vous pourriez prendre peur devant le fouillis massif de code qui vous attend. Je vous en pris, n'ayez crainte. Utilisez simplement votre navigateur pour enregistrer cette page sous son nom par défaut, qui est **get-pip.py**. Il peut être judicieux d'enregistrer ce fichier dans votre répertoire Python, afin que vous sachiez où le trouver.

Une fois que vous l'avez enregistré, vous devez l’exécuter. Deux options s'offrent à vous : si vous préférez utiliser l'interpréteur Python, faites un clic droit sur le fichier **get-pip.py** et choisissez l'option «ouvrir avec» puis sélectionnez l'interpréteur Python que vous souhaitez utiliser.

Si vous préférez installer `pip` à l'aide de la ligne de commande Windows, accédez au répertoire dans lequel se trouvent **Python** et **get-pip.py**. Pour cet exemple, nous supposerons que ce répertoire est **Python27**, nous utiliserons donc la commande `C:\>cd python27`. Une fois dans ce répertoire, pour installer `pip`, exécutez la commande :

```bash
$ python get-pip.py
```
Si vous souhaitez plus d'informations ou de l'aide concernant un étrange message d'erreur, consultez la page [StackOverflow](https://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows) qui semble être régulièrement mise à jour.


Installation des bibliothèques
--------------------------

Maintenant que vous disposez de `pip`, il est facile d'installer des bibliothèques Python car `pip` fait tout le travail pour vous. Lorsque vous trouvez une bibliothèque que vous souhaitez utiliser, généralement, la documentation ou les instructions d'installation incluent la commande `pip` nécessaire, telle que :

```bash
$ pip install requests
$ pip install beautifulsoup4
$ pip install simplekml
```
*(Note du traducteur: Le gestionnaire pip crée des liens logiques vers les versions de Python. En effet, si votre ordinateur inclut initialement la version 2.x de Python, la commande `pip` pointera alors sur cette version de Python. En revanche, si vous décidez d'installer Python en version 3.x en plus de Python 2.x, il vous faudra très certainement utiliser la  commande `pip3` dans votre terminal et non plus `pip` pour installer des bibliothèques pour Python 3.x. Afin de connaître quelle version de Python vous utilisez avec la commande `pip`, il suffit de lancer dans le terminal la commande `pip -V` ou `pip --version`).*

N'oubliez pas, pour les mêmes raisons expliquées ci-dessus (sous les distributions Mac ou Linux, mais pas sous Windows), vous devrez peut-être exécuter `pip` avec `sudo`, comme suit :

```bash
$ sudo pip install requests
```
Parfois, en particulier sous Windows, vous pouvez trouver utile d'utiliser l'indicateur `-m` (pour aider Python a trouver la bibliothèque `pip`), comme :

```bash
$ python -m pip install nom_de_la_bibliothèque
```

Bonne installation ! 

[pip]: https://pip.pypa.io/en/stable/
[Mac/Linux/Windows]: https://docs.python.org/fr/3.5/installing/index.html#how-do-i
[commande curl]: https://riptutorial.com/fr/curl
