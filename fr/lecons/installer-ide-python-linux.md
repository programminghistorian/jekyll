---
title: Installer un environnement de développement intégré pour Python (Linux)
layout: lesson
slug: installer-ide-python-linux
date: 2012-07-17
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Amanda Morton
editors:
- Miriam Posner
translation_date: 2021-10-06 
translator:
- Thomas Soubiran
translation-editor:
- Matthias Gille Levenson
translation-reviewer:
- Alexandre Bartz
difficulty: 1
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/359
activity: transforming
topics: [get-ready, python]
abstract: "Cette leçon vous montrera comment installer un environnement de développement pour Python sur un ordinateur exécutant le système d'exploitation Linux."
original: linux-installation
avatar_alt: Une bande de trois musiciens
doi: 10.46430/phfr0019 
---

{% include toc.html %}





Tout d'abord, merci à John Fink d'avoir fourni les bases de cette leçon. 
Elle a été préparée avec une distribution Ubuntu 18.04 LTS mais son contenu est aussi valable pour n'importe quel système utilisant apt tel que Debian ou Linux Mint à la seule condition d'avoir installé sudo.

## Sauvegarder son disque dur

Veillez à faire des sauvegardes de votre disque dur régulièrement. Ce conseil est valable en général et ne se limite pas à vos activités de programmation.

## Installer Python 3
  
1.  Lancez un terminal (allez dans le menu Applications, puis tapez `Terminal`, et cliquez sur l'icone)
2.  Dans le terminal, tapez : `sudo apt-get install python3`
3.  Entrez votre mot de passe, puis tapez `Y` pour lancer l'installation (*NdT : ou* `sudo  apt-get -y install python3` *pour éviter d'avoir à taper `Y` à chaque fois*). 
    Notez qu'il est fort probable que Python soit déjà installé (*NdT: la commande* `dpkg -l python3` *permet de savoir si Python 3 est déjà installé*).

## Créer un répertoire de travail

Conservez vos programmes Python dans ce répertoire. Il peut se trouver n'importe où mais il vaut mieux que vous le placiez dans votre répertoire personnel. Pour créer le répertoire, vous pouvez faire quelque chose comme cela:

```
cd ~
mkdir programming-historian
```

## Installer Komodo Edit

Komodo Edit est un éditeur de texte libre et open source, mais il en existe [de nombreux autres][]. Vous pouvez télécharger Komodo Edit depuis le site [Komodo Edit Website][]. Une fois téléchargé, ouvrez-le avec le gestionnaire de paquets d'Ubuntu, et suivez les instructions d'installation. Après avoir installé Komodo Edit,
ouvrez le répertoire `Komodo-Edit-11/bin` de votre répertoire personnel, et cliquez sur `komodo`.


## Exécuter une commande ```Run Python``` dans Komodo Edit

1.  Dans Komodo Edit, assurez-vous que la barre ```Toolbox``` est visible
2.  Cliquez sur l'icône crénelée et sélectionnez `New Command`
3.  En haut, tapez `Run Python File`
4.  Dans le champ ```Command```, tapez: `%(python3) %F`. Puis appuyez sur OK en bas de la fenêtre qui permet d'ajouter une commande.
   
{% include figure.html caption="Ajouter une nouvelle commande dans Komodo Edit" filename="komodo-edit-tools-linux.png" %}


## &laquo;&#x202F;Hello World&#x202F;&raquo; en Python

Il est de coutume de commencer l'initiation à un langage de programmation en écrivant en programme qui affiche &laquo;&#x202F;hello world&#x202F;&raquo; et puis s'arrête.

Python est un langage de choix pour les personnes qui débutent la programmation car c'est un langage de très haut niveau. En d'autres termes, il permet faire beaucoup de choses avec des programmes de quelques lignes. Et, plus un programme sera concis, moins il prendra de place à l'écran et plus il est facile à suivre.

Python est un langage dit interprété. Autrement dit, il existe un programme appelé interpréteur qui sait comment suivre les instructions écrites dans ce langage. Une façon d'utiliser l'interpréteur consiste à stocker toutes vos instructions dans un fichier et exécuter l'interpréteur avec ce fichier en entrée. Un fichier qui contient des instructions s'appelle un programme. L'interpréteur va exécuter chacune des instructions que vous lui soumettez. 
Voyons maintenant ce que cela donne.  

Dans votre éditeur de texte, créer un nouveau fichier, puis copiez-collez les deux lignes suivantes et enregistrez-le dans votre répertoire `programming-historian` sous le nom `hello-world.py`:

``` python
# hello-world.py
print('hello world')
```

La commande ```Run Python File``` vous permet d'exécuter votre programme. Si vous utilisez un autre éditeur de texte, il proposera sûrement une fonctionnalité similaire. Si tout c'est bien passé, le résultat devrait ressembler à cela:

{% include figure.html caption="hello world dans Komodo Edit sur Linux" filename="komodo-edit-output-linux.png" %}

## Interagir avec un shell Python

Une autre façon d'interagir avec un interpréteur est d'utiliser ce qu'on appelle un shell. Vous pouvez alors taper des commandes et appuyer sur entrée et le shell retournera le résultat. Le shell est très pratique si vous souhaitez tester des portions de code pour vous assurer qu'elles font bien ce que vous voulez qu'elles fassent.

Vous pouvez exécuter un shell Python en lançant un terminal. Dans le terminal, tapez:

``` python
python3
```

Ceci aura pour effet de lancer l'invite de commande de Python qui vous permet de soumettre des commandes Python dans le shell. À présent, tapez:

``` python
print('hello world')
```

et appuyez sur entrée. L'ordinateur répondra par:

``` python
hello world
```

Pour indiquer une interaction avec le shell, nous utiliserons `->` pour marquer la réponse du shell à votre commande comme suit:

``` python
print('hello world')
-> hello world
```

À l'écran, voici ce que vous devriez obtenir:

{% include figure.html caption="hello world dans un terminal Linux" filename="terminal-output-linux.png" %}

Maintenant que tout est prêt, vous pouvez passer à des choses plus intéressantes. Si vous souhaitez suivre les leçons dans l'ordre, nous vous suggérons &laquo;&#x202F;[Comprendre les pages web et le HTML][]&#x202F;&raquo; pour continuer.

  [de nombreux autres]: https://wiki.python.org/moin/PythonEditors/
  [Komodo Edit Website]: https://www.activestate.com/products/komodo-edit/
  [Comprendre les pages web et le HTML]: /fr/lecons/comprendre-les-pages-web
