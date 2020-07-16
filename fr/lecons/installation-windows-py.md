---
title: Installer un environnement de développement intégré pour Python (Windows)
layout: lesson
slug: installation-windows-py
date: 2012-07-17
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Amanda Morton
editors:
- Miriam Posner
translation_date: 2020-07-13
translator:
- Sofia Papastamkou
translation-editor:
- François Dominic Laramée
translation-reviewer:
- Marie-Christine Boucher
difficulty: 1
exclude_from_check:
  - review-ticket
activity: transforming
topics: [get-ready, python]
abstract: "Cette leçon vous montrera comment installer un environnement de développement pour Python sur un ordinateur exécutant le système d'exploitation Windows."
original: windows-installation
doi: 10.46430/phfr0011
avatar_alt: Un groupe de trois musiciens
---

{% include toc.html %}





## Sauvegarder son disque dur

Faites en sorte de toujours disposer de sauvegardes régulières et récentes du contenu de votre disque dur. L'importance de cette pratique dépasse largement le cadre de vos activités de programmation, et il serait avisé d’en faire une habitude.

## Installer Python (v.3)

Rendez-vous sur le [site web de Python][], téléchargez la dernière version stable du langage de programmation Python (version 3.8 au mois d'avril 2020) et procédez à l'installation selon les instructions fournies sur le site. *N.D.L.R. Notez que les versions les plus récentes de Python, à partir de la v. 3.5, ne sont pas compatibles avec Windows XP ni avec les versions antérieures de Windows.* 

## Créer un répertoire dédié

Pour mieux organiser votre travail, il est recommandé de créer un répertoire (dossier) dédié sur votre disque dur, à l'emplacement de votre choix, pour y ranger vos fichiers de programmation (par exemple, `programming-historian`).

## Installer Komodo Edit

Komodo Edit est un éditeur de texte au code source ouvert et gratuit que vous pouvez télécharger depuis [son site web "Komodo Edit"][]. Il existe néanmoins [un vaste choix d'éditeurs de texte][], si vous souhaitez utiliser un autre programme.

## Démarrer Komodo Edit

Ouvrez Komodo Edit; vous devriez obtenir quelque chose qui ressemble à ceci:

{% include figure.html filename="komodo-edit11-windows-main.png" caption="Komodo Edit sur Windows" %}

Si vous ne voyez pas le volet `Toolbox` (*Boîte à outils*) en haut à droite, vous pouvez y accéder via le menu `View -> Tabs & Sidebars -> Toolbox` (*Vue -> Onglets & Volets latéraux -> Boîte à outils*). Peu importe pour le moment si le volet du projet est ouvert ou non. Prenez le temps d'explorer l'interface et de vous familiariser avec son agencement. Si besoin, le menu d'aide `Help` offre une documentation détaillée.

### Configurer Komodo Edit

Vous devez maintenant configurer l'éditeur pour pouvoir exécuter vos programmes en Python. 

Sélectionnez d'abord `Edit -> Preferences -> Languages -> Python 3` (*Modifier -> Préférences -> Langages -> Python 3*) puis `Browse` (*Parcourir*). Puis, sélectionnez le chemin du répertoire d'installation de Python, qui ressemble à ceci: `C:\Utilisateurs\VotreNomUtilisateur\AppData\Local\Programs\Python\Python38-32`). Lorsque vous avez trouvé le bon chemin, cliquez sur `OK`:

{% include figure.html caption="Définissez l'interpréteur Python par défaut" filename="komodo-edit11-windows-interpreter.png" %}

*(N.D.L.R. En effectuant la manipulation décrite plus haut, après avoir cliqué sur `Browse` pour parcourir votre disque dur et afficher la boîte de dialogue `Open Executable File`, il se peut que vous n'arriviez pas à localiser le dossier AppData pour récupérer le chemin et définir l'interpréteur par défaut. Dans ce cas, entrez `%AppData%` dans la barre de recherche du menu `Démarrer` de Windows, puis cliquez sur l'emplacement pour l'ouvrir. Localisez le chemin spécifié ci-haut (`\AppData\Local\Programs\Python\Python38-32`) puis retournez à la boîte de dialogue `Open Executable File` (à l'intérieur de Komodo Edit) et copiez-le dans la barre `Nom du fichier`. Une fois le répertoire ouvert, sélectionnez `python.exe` (type de fichier: application) et cliquez sur `Ouvrir`.*

Ensuite, depuis le menu `Preferences` (*Préférences*) à gauche sélectionnez `Internationalization`. Maintenant, allez à la section `Language-specific Default Encoding` (*Encodage par défaut selon le langage de programmation*) et, dans le menu déroulant de `Language-specific`, sélectionnez `Python`. Vérifiez que l'encodage [UTF-8][] est sélectionné en tant qu'encodage par défaut.

{% include figure.html caption="Paramètre d'encodage du texte en format UTF-8" filename="komodo-edit11-windows-utf-set.png" %}

Ensuite sélectionnez `Toolbox->Add->New Command` (*Boite à outils->Ajouter->Nouvelle commande*). Vous ouvrirez ainsi une nouvelle fenêtre de dialogue. Renommez votre commande `‘Run Python’` (*Exécuter Python*). Dans la barre `‘Command’` (*Commande*), tapez:

``` python
%(python3) %f
``` 

Si vous oubliez d'exécuter cette commande, Python ne saura pas coment interpréter les instructions envoyées.

Dans la barre `‘Start in’`, tapez:

`%D`

Si vous obtenez ceci, cliquez sur `OK`:

{% include figure.html filename="komodo-edit11-windows-python-command.png" caption="Commande &laquo; Exécuter Python3 &raquo;" %}
{% include figure.html filename="komodo-edit11-windows-python-start.png" caption="Configuration de la commande &laquo; Run Python3 Start &raquo; ." %}

Votre nouvelle commande devrait apparaître dans le panneau de la boite à outils `Toolbox`. Après avoir complété cette étape, vous devrez peut-être redémarrer votre ordinateur avant d’être en mesure de travailler avec Python dans Komodo Edit.

Étape 2 – 'Hello World' en Python
--------------------------------

Il est de coutume d'inaugurer l'utilisation d'un nouveau langage de programmation avec un script qui dit tout simplement *"hello world"* soit "bonjour le monde". Nous allons voir ensemble comment faire cela en Python et en HTML.

Python est un langage de très haut niveau, ce qui en fait un choix fréquemment recommandé pour les personnes qui débutent en programmation. Autrement dit: il est possible d'écrire en Python de courts programmes qui sont très performants. Plus un programme est court, plus il est susceptible de tenir sur la taille d'un écran et donc plus il a des chances de rester gravé dans votre mémoire.

Python est un langage de programmation interprété. Cela signifie qu'il existe un programme informatique spécifique, appelé interpréteur, qui sait reconnaître les instructions écrites dans ce langage. Une manière d'utiliser un interpréteur consiste à stocker toutes vos instructions Python dans un fichier puis à soumettre ce fichier à l'interpréteur. Un fichier contenant des instructions écrites avec un langage de programmation s'appelle un programme (informatique). L'interpréteur exécute chacune des instructions contenues dans le programme, puis il s'arrête. Voyons les étapes à suivre pour y parvenir.

Dans votre éditeur de texte, créez un nouveau fichier, entrez ce petit programme de deux lignes, puis sauvegardez-le dans votre répertoire `programming-historian` sous le nom
`hello-world.py`

``` python
# hello-world.py
print('hello world')
```

L'éditeur de texte de votre choix doit avoir un bouton de menu “`Run`” qui vous permet d'exécuter votre programme. Si tout s'est bien passé, vous devriez obtenir un résultat semblable à celui présenté dans la figure ci-dessous, que nous avons obtenue avec Komodo Edit:

{% include figure.html filename="komodo-edit11-windows-hello.png" caption="'Hello World'" %}

## Interagir via une console Python (shell)

Une autre manière d'interagir avec un interpréteur est d'utiliser ce que nous appelons une console. Dans ce cas, il suffit de taper une instruction au clavier et d'appuyer sur la touche Entrée pour que la console exécute votre commande. La console est un moyen parfait pour tester votre code et avoir la certitude que vous allez obtenir le résultat que vous recherchez. 

Vous pouvez exécuter une console Python en double-cliquant sur le fichier `python.exe`. Si vous avez installé la version 3.8 (la plus récente au moment de cette traduction en avril 2020), ce fichier se trouve fort probablement dans votre répertoire `C:\Utilisateurs\VotreNomUtilisateur\AppData\Local\Programs\Python\Python38-32`. Lorsque la fenêtre de la console s'affiche sur votre écran, tapez:

``` python
print('hello world')
```

puis appuyez sur la touche Entrée. Votre ordinateur va vous répondre:

``` python
hello world
```

Pour représenter une interaction via la console, nous utilisons -\> pour indiquer la réponse reçue dans celle-ci, comme suit: 

``` python
print('hello world')
-> hello world
```
Sur votre écran, l'affichage ressemble plutôt à cela: 
    
{% include figure.html caption="La console Python sous Windows" filename="windows-python3-cmd.png" %}

Maintenant, votre ordinateur est prêt et vous êtes en mesure d'exécuter des tâches plus intéressantes. Si vous travaillez avec nos tutoriels sur Python dans l'ordre, nous vous recommandons de consulter par la suite la leçon &laquo; [Comprendre les pages web et le HTML][] &raquo; .

  [site web de Python]: http://www.python.org/
  [un vaste choix d'éditeurs de texte]: http://wiki.python.org/moin/PythonEditors/
  [son site web "Komodo Edit"]: http://www.activestate.com/komodo-edit
  [UTF-8]: http://en.wikipedia.org/wiki/UTF-8
  [Comprendre les pages web et le HTML]: /fr/lecons/comprendre-les-pages-web
