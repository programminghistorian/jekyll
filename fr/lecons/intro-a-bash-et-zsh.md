---
title: "Introduction à l'interface en ligne de commande Bash et Zsh"
slug: intro-a-bash-et-zsh
original: intro-to-bash
layout: lesson
collection: lessons
date: 2014-09-20
translation_date: 2024-04-24
authors:
- Ian Milligan
- James Baker
reviewers:
- M. H. Beals
- Allison Hegel
- Charlotte Tupman
editors:
- Adam Crymble
translator:
- Melvin Hersent
translation-editor:
- Alexandre Wauthier
translation-reviewer:
- Louis-Olivier Brassard
- Julien Du Crest
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/568
difficulty: 1
activity: transforming
topics: [data-manipulation, get-ready]
abstract: Cette leçon vous apprendra comment entrer des commandes dans une interface en ligne de commande, plutôt qu'à travers une interface graphique. Les interfaces en ligne de commande présentent des avantages pour les utilisateurs qui ont besoin de plus de précision dans leur travail. Elles permettent de détailler le lancement de certains programmes, en autorisant l'ajout d'argument pour spécifier exactement la façon dont vous voulez que votre programme se lance. De plus, il est possible de les automatiser facilement en créant des scripts, qui peuvent être considérés comme des recettes (une suite d'instructions précises) reposant sur des commandes au format textuel.
avatar_alt: Soldats en armure antique avec des lances
doi: 10.46430/phfr0031
---

{% include toc.html %}

## Introduction

De nombreuses leçons de _Programming Historian_ vous demandent d'entrer des commandes à travers une &laquo;&nbsp;interface en ligne de commande&nbsp;&raquo;, aussi appelée &laquo;&nbsp;invite de commande&nbsp;&raquo; ou CLI (Command-Line Interface). Aujourd'hui, l'interaction standard entre un utilisateur et le système de son ordinateur se fait par le biais d'une &laquo;&nbsp;interface graphique&nbsp;&raquo;, ou GUI (Graphical-User Interface), grâce à sa souris. Cela signifie par exemple que pour aller dans un répertoire (ou dossier), vous pouvez cliquer directement sur une image dudit répertoire. Pour lancer un programme, vous double-cliquez dessus. Lorsque vous naviguez sur internet, vous interagissez avec les éléments de la page web. Néanmoins, avant la popularisation des interfaces graphiques à la fin des années 1980, la façon principale d'interagir avec un ordinateur était à travers une interface en ligne de commande.

{% include figure.html filename="en-or-intro-to-bash-01.png" alt="Interface graphique de l'ordinateur de Ian Milligan" caption="Figure 1. GUI de l'ordinateur de Ian Milligan" %}

Les interfaces en ligne de commande présentent des avantages pour les utilisateurs et utilisatrices qui ont besoin de plus de précision dans leur travail, tel que les chercheur·es en humanités numériques. Elles permettent de détailler le lancement de certains programmes, car vous pouvez ajouter des modificateurs pour spécifier exactement comment vous voulez que le programme s'exécute. De plus, la plupart des tâches répétitives peuvent être automatisées avec des [scripts](https://perma.cc/D3YX-KFL9), qui peuvent être vus comme une recette à suivre composée de commandes écrites en texte.

Il existe deux familles d'interfaces en ligne de commande&nbsp;: celle utilisée par les systèmes [Unix](https://perma.cc/V5TZ-2ZV3) (Linux et macOS, pour résumer) et celle utilisée par les systèmes Windows. Sur de nombreuses distributions Linux et jusqu'à macOS Mojave, le shell `bash`, ou &laquo;&nbsp;Bourne-again shell&nbsp;&raquo; est utilisé par défaut. Depuis macOS Catalina, c'est le shell `zsh`, ou &laquo;&nbsp;Z shell&nbsp;&raquo;, très proche de bash qui est utilisé par défaut. Les commandes que nous utiliserons dans cette leçon seront les mêmes pour les deux.

Enfin, pour les utilisateurs et utilisatrices de Windows, l'interface en ligne de commande est par défaut basé sur `MS-DOS`, qui utilise des commandes et une syntaxe différentes, mais permet d'effectuer les mêmes tâches. Cette leçon propose une introduction basique à `bash`/`zsh` et les personnes qui utilisent Windows peuvent aussi le suivre en installant un shell bash, comme présenté un peu plus loin.

Cette leçon utilise un [shell Unix](https://perma.cc/8KVK-G3MV), qui est un interpréteur de commande procurant une interface utilisateur pour le système d'exploitation Unix et d'autres systèmes basés sur celui-ci. Cette leçon couvrira un nombre restreint de commandes basiques. À la fin de cette leçon vous serez capable de naviguer dans votre système de fichier, d'ouvrir un fichier, d'effectuer des manipulations simples dessus, telles que les copier, les lire, en combiner plusieurs ou de faire des éditions simples. Ces commandes constituent les bases permettant de construire d'autres commandes plus complexes pouvant s'adapter à vos données de recherches ou vos projets. Les personnes souhaitant un guide de référence plus complet que cette leçon peuvent lire l'ouvrage (en anglais) de Deborah S. Ray et Eric J. Ray, *Unix and Linux: Visual Quickstart Guide*, 5th édition (2014).

## Windows&nbsp;: Installation d'un shell

Pour les utilisateurs et utilisatrices de Windows, une étape en plus est nécessaire, car vous devrez installer un shell bash.
Vous avez plusieurs outils à votre disposition, mais la méthode recommandée est d'installer le Sous-système Windows pour Linux (WSL), disponible depuis Windows 10. Vous trouverez un tutoriel détaillé sur le [site de Microsoft](https://perma.cc/T7NP-JS54). En cas de version Windows plus ancienne, ou si vous préférez ne pas installer une distribution Linux complète, vous avez deux autres choix&nbsp;: vous pouvez installer Git Bash en téléchargeant la dernière version sur [cette page](https://git-for-windows.github.io/) et en suivant les instructions ici sur [Open Hatch](https://perma.cc/7KM8-DR3D). Ou bien, vous pouvez choisir d'installer [Cygwin](https://www.cygwin.com/).

## Ouvrir son shell

Maintenant que nous avons installé notre shell, démarrons-le.

Pour Windows, lancez votre distribution Linux (Ubuntu par défaut) installée par le biais de WSL, vous arriverez automatiquement sur un terminal. Si vous avez choisi d'installer Git Bash, ou cygwin, démarrez cette application.

Sous macOS, par défaut le terminal se trouve ici&nbsp;:

`Applications -> Utilitaires -> Terminal`

{% include figure.html filename="en-or-intro-to-bash-02.png" alt="Icône du programme Terminal.app sur macOS" caption="Figure 2. Le programme Terminal.app sur macOS" %}

Sous Linux, vous pouvez utiliser le raccourci `Ctrl + alt + T` pour ouvrir le terminal ou vous pouvez simplement rechercher &laquo;&nbsp;terminal&nbsp;&raquo; dans vos applications.

Une fois lancé, vous verrez cette fenêtre&nbsp;:

{% include figure.html filename="en-or-intro-to-bash-03.png" alt="Un terminal ouvert sur un bureau macOS" caption="Figure 3. Un écran de terminal vide sur notre bureau macOS" %}

Vous pourriez avoir envie de changer l'apparence par défaut de votre terminal, car du texte noir sur un fond blanc peut être vite fatiguant pour les yeux. Dans l'application macOS par défaut, cliquez sur l'onglet **Paramètres** et changez le schéma de couleur. Nous préférons personnellement une interface avec moins de contraste entre le fond et le texte, car nous regarderons beaucoup le terminal. Les palettes de couleurs &laquo;&nbsp;Novel&nbsp;&raquo; et &laquo;&nbsp;[Solarisée](https://perma.cc/G2BK-X2TU)&nbsp;&raquo; sont plus reposantes. Pour les utilisateurs Windows, un effet similaire peut être obtenu dans Git Bash en cliquant sur l'onglet **Propriétés**&nbsp;: cliquez n'importe où sur la barre du haut et vous pourrez sélectionner **Propriétés**.

{% include figure.html filename="en-or-intro-to-bash-04.png" alt="L'écran des paramètres du terminal sur macOS" caption="Figure 4. L'écran des paramètres de notre terminal sur macOS" %}

Une fois que vous êtes satisfait avec l'interface, nous pouvons démarrer.

## Se déplacer dans le système de fichiers de votre ordinateur

Si vous ne savez pas exactement où vous vous trouvez dans le système de fichiers de votre ordinateur la première étape est d'obtenir cette information. Vous pouvez savoir dans quel dossier vous vous trouvez grâce à la commande `pwd`, qui est la contraction de &laquo;&nbsp;print working directory&nbsp;&raquo;. Tapez&nbsp;:

```bash
pwd
```

et pressez la touche _Entrée_. Si vous êtes sur MacOS, votre ordinateur affichera sûrement `/Users/USERNAME` avec votre propre nom d'utilisateur à la place de `USERNAME`. Par exemple, le chemin pour Ian sur macOS est `/Users/ianmilligan1/`.

Sur Windows, l'utilisateur James est à&nbsp;:

`C:\Users\jbaker`

Tandis que sur Ubuntu (Linux), l'utilisateur admin se trouve à&nbsp;:

`/home/admin`

Vous pouvez voir qu'il y a des différences mineures en fonction de votre système d'exploitation, mais ne vous inquiétez pas&nbsp;; une fois que vous vous déplacerez et que vous manipulerez des fichiers, ces différences s'effaceront.

Pour nous orienter, affichons une liste des fichiers présents dans notre dossier. Entrez la commande&nbsp;:

```bash
ls
```

Vous verrez alors une liste de tous les fichiers et dossiers présents à votre position. Votre dossier peut être encombré ou vide, mais vous verrez à minima quelques endroits familiers. Sur macOS, par exemple, vous verrez `Applications`, `Desktop`, `Documents`, `Downloads`, `Library`, `Pictures`, etc.

Si vous désirez obtenir plus d'informations que simplement une liste de fichiers, vous pouvez spécifier différentes options, ou &laquo;&nbsp;flags&nbsp;&raquo;, à ajouter à nos commandes basiques. Les options permettent de préciser la façon d'exécuter une commande. Cela permet de modifier par exemple le format de sortie de notre commande ou bien la façon de manipuler nos données. Pour obtenir une liste de ces arguments, les utilisateurs macOS/Linux peuvent utiliser la commande présente par défaut `man` (manuel). Ainsi, ces derniers peuvent taper&nbsp;:

```bash
man ls
```

{% include figure.html filename="en-or-intro-to-bash-05.png" alt="La page de manuel sur le terminal pour la commande ls" caption="Figure 5. La page du manuel pour la commande ls" %}

Ici, vous pouvez voir une liste avec le nom de la commande et les différents arguments que vous pouvez utiliser, accompagnés de la description de leurs effets. Pour le moment, beaucoup de ces informations ne vous seront pas compréhensibles, mais ne vous inquiétez pas, vous deviendrez plus familier avec ces commandes au fil du temps. Vous pouvez explorer cette page de plusieurs façons&nbsp;: la barre d'espacement permet de déplacer la page vers le bas ou vous pouvez utiliser les flèches haut et bas.

Pour quitter la page du manuel, pressez `q` et vous retournerez à l'interface en ligne de commande où vous étiez avant d'entrer dans la page du manuel.

Vous pouvez essayer la commande `man` pour la commande que nous avons vue précédemment, `pwd`, ainsi que pour celles que nous verrons après. Vous pouvez même taper `man man`.

Les utilisateurs Windows peuvent utiliser la commande `help` à la place de `man`, même si cette commande présente moins de fonctionnalités que son équivalent sur macOS/Linux. Essayez `help` pour voir l'aide disponible, et `help pwd` pour un exemple de résultat de la commande.

Essayons quelques-unes des options que nous avons vues sur la page `man` pour `ls`. Peut-être souhaitez-vous voir uniquement les fichiers TXT présents dans votre dossier d'accueil. Tapez&nbsp;:

```bash
ls *.txt
```

Cette commande retourne une liste de fichiers texte si vous en avez dans votre dossier d'accueil. La commande \* est un &laquo;&nbsp;métacaractère&nbsp;&raquo; (&laquo;&nbsp;wildcard&nbsp;&raquo; ou &laquo;&nbsp;joker&nbsp;&raquo; en anglais) - il signifie zéro, un ou plusieurs caractères quelconques. Donc, dans notre cas, vous indiquez que tout ce qui correspond au modèle `quelquechose.txt` sera affiché.

Essayons différentes combinaisons. Si par exemple vous avez différents fichiers `1-Canadien.txt`, `2-Canadien.txt` et ainsi de suite, la commande `ls *-Canadien.txt` affichera ces fichiers tout en excluant les autres ne respectant pas ce modèle.

Imaginons que vous vouliez plus d'informations. Sur la page `man`, vous avez vu une option qui peut être utile&nbsp;:

>     -l      use a long listing format

Donc si vous entrez&nbsp;:

```bash
ls -l
```

l'ordinateur retournera une &laquo;&nbsp;liste longue&nbsp;&raquo; des fichiers contenant les informations similaires que vous trouveriez dans votre explorateur de fichier&nbsp;: la taille des fichiers en bits, la date de leur création ou de leur dernière modification, ainsi que le nom de chacun d'entre eux. La taille exprimée en bits peut être déroutante, prenons pour exemple un fichier `test.html` mesurant 6020 bits. Nous avons plutôt l'habitude de parler en octet (ou bytes), kilooctet, mégaoctet, gigaoctet, etc.

Heureusement, il existe une autre option&nbsp;:

>     -h      Utilisé avec l'option -l, exprime la taille du fichier en : octet, kilooctet,
>             mégaoctet, gigaoctet, téraoctet and pétaoctet afin de réduire le nombre
>             de chiffres à trois ou mois en utilisant la base 2.

Quand vous souhaitez utiliser deux options, vous pouvez simplement les exécuter ensemble. Ainsi en tapant&nbsp;:

```bash
ls -lh
```

vous recevrez un affichage dans un format lisible par un humain&nbsp;; vous apprendrez ainsi que 6020 bits sont équivalents à 5.9Ko (ou KB), qu'un autre fichier mesure 1Mo et ainsi de suite.

Ces options sont très importantes. Vous les rencontrerez dans d'autres leçons de _Programming Historian_, comme celles sur [Wget](/en/lessons/applied-archival-downloading-with-wget), [MALLET](/en/lessons/topic-modeling-and-mallet), et [Pandoc](/fr/lecons/redaction-durable-avec-pandoc-et-markdown), qui utilisent tous la même syntaxe. Heureusement, vous n'avez pas besoin de mémoriser celle-ci. Vous pouvez conserver ces leçons à portée de main afin de pouvoir y jeter un œil si vous désirez. Ces leçons peuvent être suivies dans le sens que vous désirez.

Nous avons passé un bon moment dans notre dossier d'accueil, il est temps de nous déplacer. Vous pouvez faire cela avec la commande `cd` pour &laquo;&nbsp;Change Directory&nbsp;&raquo; (changer de répertoire).

Si vous entrez&nbsp;:

```bash
cd desktop
```

vous serez désormais sur votre bureau. Ceci est semblable au fait de double-cliquer sur le dossier **Bureau** au sein de votre explorateur de fichier. Pour vérifier, tapez `pwd` et vous devriez voir s'afficher quelque chose comme&nbsp;:

`/Users/ianmilligan1/desktop`

Essayez les commandes que vous venez d'apprendre&nbsp;: explorez votre dossier courant en utilisant la commande `ls`.

Si vous voulez revenir en arrière, vous pouvez taper&nbsp;:

```bash
cd ..
```

Cela nous fait remonter d'un niveau dans l'arborescence de dossiers. Nous revenons ainsi à `/Users/ianmilligan1/`. Si vous êtes complètement perdu, vous pouvez taper&nbsp;:

```bash
cd
```

et vous retournerez au dossier d'accueil, là où vous aviez démarré.

Essayez d'explorer&nbsp;: visitez vos bibliothèques, vos images, vos dossiers présents sur votre ordinateur. Habituez-vous à vous déplacer dans les dossiers et à en sortir. Imaginez que vous naviguez au travers d'une [arborescence](https://perma.cc/AFN4-F78C). Si vous êtes sur votre bureau, vous ne pourrez pas vous déplacer vers vos documents avec `cd documents`, car il est un &laquo;&nbsp;enfant&nbsp;&raquo; de votre dossier d'accueil et donc au même niveau dans l'arborescence que votre dossier **Documents**. Pour aller vers un dossier situé au même niveau dans l'arborescence, vous devez revenir au parent commun avec la commande `cd ..` et aller ensuite vers le dossier voulu avec `cd documents`.

Être capable de naviguer dans votre système de fichier en utilisant un shell (bash ou zsh) est important pour beaucoup de leçons de _Programming Historian_. Avec l'habitude, vous naviguerez directement au dossier qui vous intéresse. Dans notre cas, depuis n'importe quel endroit, vous pouvez taper&nbsp;:

```bash
cd /Users/ianmilligan1/mallet-2.0.7
```

ou, sur Windows, quelque chose comme&nbsp;:

```bash
cd C:\mallet-2.0.7\
```

et vous serez amené directement à votre dossier MALLET pour des leçons de [topic modeling](/en/lessons/topic-modeling-and-mallet).

Enfin, sous macOS ou Linux, testez&nbsp;:

```bash
open .
```

ou, sous Windows, tapez&nbsp;:

```bash
explorer .
```

Cette commande ouvrira votre GUI dans le dossier courant. Faites attention de bien laisser un espace entre votre commande (`open` ou `explorer`) et le point, qui sert à signifier &laquo;&nbsp;depuis le répertoire actuel&nbsp;&raquo;.

## Interagir avec des fichiers

De la même façon que vous pouvez naviguer entre les répertoires, vous pouvez interagir avec les fichiers depuis l'interface en ligne de commande&nbsp;: vous pouvez les lire, les ouvrir, les exécuter ou même les éditer, souvent sans même avoir besoin de quitter l'interface. La principale raison d'utiliser l'interface de cette façon est de pouvoir travailler sans avoir à utiliser la souris et, même si la courbe d'apprentissage est raide, cela peut même devenir le seul lieu d'écriture. De plus, beaucoup de programmes requièrent de passer par l'interface en ligne de commande pour les utiliser. Ainsi, comme vous utiliserez des programmes en ligne de commande, il est souvent plus rapide d'effectuer des modifications mineures sans changer de programme. Pour en savoir plus, lisez l'article de Jon Beltran de Heredia intitulé [Why, oh WHY, do those #?@! nutheads use vi?](https://perma.cc/W3Q9-LA6Y) (ressource en anglais).

Nous allons désormais voir quelques façons simples d'interagir avec des fichiers.

Premièrement, vous pouvez créer un nouveau répertoire avant d'y ajouter des fichiers textes. Pour des raisons de simplicité, nous allons le créer sur notre bureau. Naviguez vers votre bureau en utilisant votre shell, et tapez&nbsp;:

```bash
mkdir proghist-texte
```

Cette commande, qui est la contraction de &laquo;&nbsp;make directory&nbsp;&raquo;, crée ici un répertoire nommé &laquo;&nbsp;proghist-texte&nbsp;&raquo;. Attention, il existe une commande [`make`](https://perma.cc/7M88-WMVC)&nbsp;&raquo;, qui fait tout autre chose et qui dépasse le cadre de cette leçon.

De manière générale, il est préférable d'éviter les espaces dans les noms de fichiers et de répertoires lorsque l'on utilise l'interface en ligne de commande (ce n'est bien sûr pas impossible, c'est juste plus simple). Vous pouvez regarder votre bureau pour vérifier que la commande a bien fonctionné. Maintenant, déplacez-vous dans ce répertoire, avec la commande `cd`.

C'est le moment de vous donner un conseil qui vous fera gagner du temps&nbsp;: il existe une fonction d'autocomplétion dans votre shell et voici comment l'utiliser. Retournez sur votre bureau si vous vous êtes déjà déplacé dans votre nouveau dossier (`cd ..`). Pour vous déplacer dans le répertoire `proghist-texte` vous pouvez taper `cd proghist-texte` en entier ou alors, pour utiliser l'autocomplétion, tapez `cd prog` et ensuite pressez la touche `tabulation`. Vous remarquerez que l'interface complète la ligne en `cd proghist-texte`. 

<div class="alert alert-info">
Enfoncer la touche tabulation (<i>TAB</i>) à n'importe quel moment dans le shell lui demandera de tenter l'autocomplétion de la ligne, basée sur les répertoires et fichiers présents dans le répertoire courant. En fonction de votre shell (bash notamment) cette fonction est sensible à la casse, ainsi dans notre exemple précédent <code>cd Prog</code> (avec une majuscule) ne se complétera pas automatiquement en <code>proghist-texte</code>. Lorsque deux possibilités ou plus existent (exemple&nbsp;: <code>proghist-texte</code> et <code>proghist-image</code>), l'autocomplétion s'arrêtera à la première différence rencontrée (ici <code>proghist-</code>). Nous vous encourageons à utiliser cette méthode tout au long de cette leçon pour voir comment elle se comporte.
</div>

Sous Windows, les extensions de fichier sont invisibles par défaut. Si vous souhaitez manipuler des fichiers sous Windows, nous vous recommandons d'activer l'affichage des extensions de fichier. Pour faire cela, ouvrez votre explorateur de fichiers et sous **Affichage**, dans le groupe **Afficher/masquer**, cochez la case **Extensions de nom de fichier**.
Pour plus d'informations, vous pouvez vous référer à [cet article](https://perma.cc/5ZWL-XRFF) du support Windows.

Nous avons désormais besoin d'un fichier texte pour nos futures commandes. Nous pouvons utiliser un livre réputé pour être long, l'épique *Guerre et Paix* de Léon Tolstoï. Le fichier est disponible, en anglais, grâce au [Projet Gutenberg](http://www.gutenberg.org/ebooks/2600). Si vous avez déjà installé [wget](/en/lessons/applied-archival-downloading-with-wget), vous pouvez simplement taper&nbsp;:

```bash
wget http://www.gutenberg.org/files/2600/2600-0.txt
```

Si ce n'est pas le cas, vous pouvez télécharger le texte directement depuis votre navigateur grâce au lien précédent. Une fois sur la page, faites un clic droit pour utiliser la commande **Enregistrer sous...** et sauvegardez le fichier dans votre dossier récemment créé. Désormais, lorsque vous tapez&nbsp;:

```bash
ls -lh
```

vous voyez&nbsp;:

> -rw-r--r--+ 1 ianmilligan1  staff   3.1M  1 May 10:03 2600-0.txt

`2600-0.txt` étant ici le fichier que vous avez téléchargé.

Vous pouvez lire le texte contenu dans le fichier de différentes manières. Premièrement, vous pouvez dire à votre ordinateur que vous voulez le lire en utilisant le programme standard que vous utilisez pour ouvrir des fichiers texte. Par défaut, cela peut être TextEdit sur macOS ou Notepad sur Windows. Pour ouvrir un fichier de cette façon sur macOS et Linux, tapez&nbsp;:

```bash
open 2600-0.txt
```

ou, sous Windows&nbsp;:

```bash
explorer 2600-0.txt
```

Cela sélectionne le programme par défaut pour ouvrir ce type de fichier et ouvre le fichier demandé.

Néanmoins, vous voudrez la plupart du temps travailler dans votre interface en ligne de commande sans la quitter. Vous pouvez aussi lire les fichiers au sein de cet environnement. Pour faire cela, nous allons utiliser la commande &laquo;&nbsp;concatenate&nbsp;&raquo; en tapant&nbsp;:

```bash
cat 2600-0.txt
```

La fenêtre du terminal va alors afficher l'intégralité du contenu de votre fichier. En théorie, c'est intéressant, mais ici vous ne pouvez pas faire grand-chose du résultat obtenu à cause de la quantité de texte. Vous pouvez avoir envie de juste regarder le début ou la fin de votre fichier.

La commande&nbsp;:

```bash
head 2600-0.txt
```

vous fourni les dix premières lignes, tandis que&nbsp;:

```bash
tail 2600-0.txt
```

procure une vue des dix dernières. C'est une bonne façon de rapidement déterminer le contenu de votre fichier. Vous pouvez ajouter un paramètre à votre commande pour modifier le nombre de lignes affichées&nbsp;: `head -20 2600-0.txt` par exemple affichera les vingt premières lignes.

Vous pourriez aussi avoir envie de renommer votre fichier en quelque chose de plus descriptif. Pour cela, vous pouvez utiliser la commande `mv` pour &laquo;&nbsp;move&nbsp;&raquo; (déplacer)&nbsp;:

```bash
mv 2600-0.txt tolstoy.txt
```

Après, en effectuant la commande `ls`, vous verrez que votre fichier s'appelle bien `tolstoy.txt`. Si vous souhaitez le dupliquer, vous pouvez utiliser la commande `cp` (&laquo;&nbsp;copy&nbsp;&raquo;) en tapant&nbsp;:

```bash
cp 2600-0.txt tolstoy.txt
```

Nous reverrons ces commandes peu après.

Maintenant que vous avez appris quelques nouvelles commandes, voici une nouvelle astuce. Enfoncez la flèche du haut de votre clavier&nbsp;: la dernière commande réalisée apparait devant votre curseur. Vous pouvez continuer à utiliser la flèche du haut pour remonter dans l'historique de vos commandes précédentes. La flèche du bas vous ramène à vos commandes plus récentes.

Après avoir lu et renommé quelques fichiers, vous pourriez avoir envie de joindre leur texte en un seul fichier. Pour combiner (ou concaténer) deux fichiers ou plus, vous pouvez utiliser la commande `cat`. Commençons par copier le fichier Tolstoy si ce n'est pas déjà fait ( `cp tolstoy.txt tolstoy2.txt`). Maintenant que nous avons deux copies de *War and Peace*, assemblons-les pour créer un livre encore plus long.

Tapez&nbsp;:

```bash
cat tolstoy.txt tolstoy2.txt
```

et pressez _Entrée_. Cela imprimera, ou affichera, la combinaison des fichiers dans votre shell. Néanmoins, le résultat est trop long pour être lu dans votre fenêtre. Heureusement, en utilisant la commande `>`, vous pouvez envoyer le résultat dans un nouveau fichier plutôt que dans votre terminal. Tapez&nbsp;:

```bash
cat tolstoy.txt tolstoy2.txt > tolstoy-double.txt
```

Maintenant, lorsque vous tapez `ls` vous verrez `tolstoy-double.txt` apparaitre dans votre répertoire.

Lorsque vous combinez plus de deux fichiers, utiliser un métacaractère peut éviter d'écrire le nom de chaque fichier. Comme nous avons vu avant, le symbole `*` représente un nombre quelconque (possiblement zéro) de caractères. Ainsi, si vous tapez&nbsp;:

```bash
cat *.txt > tout-ensemble.txt
```

et pressez _Entrée_, une combinaison par ordre alphabétique de tous les fichiers `.txt` présent dans le répertoire courant sera enregistrée dans le fichier `tout-ensemble.txt`. Cela peut être très utile si vous souhaitez concaténer un grand nombre de fichiers présent dans un répertoire afin de travailler avec eux dans un programme d'analyse de texte. Un autre métacaractère intéressant est le symbole `?` qui permet de substituer un caractère ou un chiffre. Ainsi la commande&nbsp;:

```bash
cat tolstoy?.txt
```

affichera le texte de notre fichier `tolstoy2.txt`.

## Éditer des fichiers texte directement en ligne de commande

Si vous souhaitez lire un fichier dans son intégralité sans quitter le terminal, vous pouvez lancer [Vim](https://perma.cc/V9MG-FPKU). Vim est un éditeur de texte très puissant, parfait pour l'utiliser avec des programmes tels que [Pandoc](https://perma.cc/Q5YT-K3GT) pour faire de l'édition de texte ou pour éditer votre code sans avoir besoin de passer par un autre programme. Il est inclus par défaut sur la plupart des distributions Linux, macOS et Windows. Vim possède une courbe d'apprentissage assez raide, nous nous limiterons donc à quelques fonctionnalités de base.

Tapez&nbsp;:

```bash
vim tolstoy.txt
```

Vous devriez voir apparaitre Vim, un éditeur de texte en ligne de commande.

{% include figure.html filename="en-or-intro-to-bash-06.png" alt="l'éditeur de texte en ligne de commande Vim" caption="Figure 6. Vim" %}

Si vous souhaitez vous lancer dans l'apprentissage de Vim, il existe un [bon guide (en anglais)](https://perma.cc/G8X7-TZ4G) disponible.

Utiliser Vim pour lire des fichiers est relativement simple. Vous pouvez utiliser les flèches du clavier pour naviguer dans votre fichier et vous pourriez théoriquement lire *Guerre et Paix* de cette façon, bien que ce ne soit pas particulièrement agréable.

Voici quelques commandes basiques pour naviguer dans votre fichier&nbsp;:

_Ctrl_+_F_ (en maintenant la touche _control_ et en pressant la lettre _F_) vous déplacera d'une page vers le bas (_MAJ_+_FlècheBas_ pour Windows).

_Ctrl_+_B_ vous déplacera d'une page vers le haut (_MAJ_+_FlècheHaut_ pour les utilisateurs Windows).

Si vous voulez vous déplacer rapidement à la fin d'une ligne, vous pouvez presser la touche _$_ et pour vous déplacer au début d'une ligne pressez _0_. Vous pouvez aussi vous déplacer entre les phrases en tapant `)` (en avant) ou `(` (en arrière). Pour les paragraphes, tapez `}` et `{`. Puisque vous êtes en train de faire tout avec votre clavier, plutôt que de maintenir votre flèche du bas pour vous déplacer dans votre document, cela vous laisse vous déplacer rapidement en avant ou en arrière.

Retournons au début de notre document et effectuons une modification mineure, comme ajouter un champ **Lecteur** dans l'en-tête. Déplacez votre curseur entre **Author** et **Translators**, tel que présenté ici&nbsp;:

{% include figure.html filename="en-or-intro-to-bash-07.png" alt="Notre fichier tolstoy.txt ouvert dans Vim, avant d'y insérer du texte" caption="Figure 7. Sur le point de faire une insertion" %}

Si vous essayez d'écrire, vous aurez un message d'erreur ou le curseur commencera à se déplacer. C'est parce que vous devez spécifier que vous souhaitez éditer. Pressez la lettre `a` ou `i`.

En bas de l'écran, vous verrez&nbsp;:

`-- INSERT --`

Cela signifie que vous êtes en mode insertion. Vous pouvez désormais écrire et éditer le texte comme si vous étiez dans un éditeur de texte standard. Pressez _Entrée_ deux fois, ensuite _flèche du haut_, et tapez&nbsp;:

`Lecteur : un chercheur en humanités numériques`

Lorsque vous avez terminé, pressez _Échap_ pour retourner en mode lecture.

Pour quitter Vim ou sauvegarder, vous devez entrer une suite de commandes. Pressez `:` et vous lancerez l'invite de commande de Vim. Si vous souhaitez sauvegarder le fichier, tapez `w` pour &laquo;&nbsp;write&nbsp;&raquo; (écrire) le fichier, puis pressez sur _Entrée_ pour exécuter cette commande. Vous verrez alors&nbsp;:

> "tolstoy.txt" [dos] 65009L, 3291681C written

{% include figure.html filename="en-or-intro-to-bash-08.png" alt="Notre fichier tolstoy.txt ouvert dans Vim, après avoir inséré du texte" caption="Figure 8. Après avoir écrit sur notre fichier" %}

Si vous souhaitez quitter, pressez `:` à nouveau, puis `q` (pour &laquo;&nbsp;quit&nbsp;&raquo;). Vous retournerez alors à l'interface en ligne de commande. Comme en bash, vous auriez pu ici combiner les deux commandes. Ainsi, presser `:` puis taper `wq` aurait sauvegardé le fichier puis quitté Vim. Si vous aviez voulu quitter sans sauvegarder, la commande `q!` vous aurait permis de faire cela en ignorant les modifications effectuées, qui auraient alors été perdues.

Vim est sûrement différent de ce que vous avez l'habitude d'utiliser et vous demandera plus de pratique pour vous y habituer. Mais si vous voulez effectuer de petites modifications dans vos fichiers, c'est un bon point de départ. En devenant plus à l'aise, vous pourriez même finir par écrire des articles avec lui, en profitant [des notes de bas de page et du formatage proposé par Pandoc et Markdown](/fr/lecons/redaction-durable-avec-pandoc-et-markdown).

## Déplacement, copie et suppression de fichiers

Disons que vous en avez terminé avec ce répertoire et que vous souhaitez déplacer `tolstoy.txt` ailleurs. Premièrement, vous devriez créer une sauvegarde. Le shell ne pardonne pas les erreurs et sauvegarder est encore plus important qu'avec les GUI. Si vous supprimez quelque chose ici il n'y a pas de corbeille pour repêcher vos fichiers. Pour créer une sauvegarde (backup), vous pouvez taper&nbsp;:

```bash
cp tolstoy.txt tolstoy-sauvegarde.txt
```

Désormais, lorsque vous lancez la commande `ls` vous verrez plusieurs fichiers dont au moins deux sont identiques&nbsp;: `tolstoy.txt` et `tolstoy-sauvegarde.txt`.

Copions le premier ailleurs. Pour l'exercice, créons un deuxième répertoire sur votre bureau. Déplacez-vous sur votre bureau (`cd ..`) et créez (`mkdir`) un autre répertoire. Nommons-le `proghist-dest`.

Restons ici et copions le fichier `tolstoy.txt`. La commande &laquo;&nbsp;copier&nbsp;&raquo; s'utilise de la façon suivante&nbsp;: `cp [source] [destination]`, ce qui signifie que vous tapez d'abord `cp`, puis vous entrez le ou les fichiers que vous souhaitez copier suivi de l'emplacement où ils devront aller.

Dans notre cas, la commande&nbsp;:

```bash
cp /Users/ianmilligan1/desktop/proghist-texte/tolstoy.txt /Users/ianmilligan1/desktop/proghist-dest/
```

copiera Tolstoy depuis le premier répertoire dans le second. Vous aurez à insérer votre propre nom d'utilisateur à la place de &laquo;&nbsp;ianmilligan1&nbsp;&raquo;.

Vous avez désormais trois copies de l'ouvrage sur votre ordinateur&nbsp;: l'original, la sauvegarde et la nouvelle copie dans le deuxième répertoire. Nous aurions pu choisir de déplacer (move) le fichier, donc de ne pas laisser de copie dans le fichier source, en remplaçant la commande `cp` par `mv`; mais ne testons pas cela tout de suite.

Vous pouvez aussi copier plusieurs fichiers en une seule commande. Si vous souhaitiez copier le fichier original et sa sauvegarde, vous pouvez utiliser un métacaractère.

```bash
cp /Users/ianmilligan1/desktop/proghist-texte/*.txt /Users/ianmilligan1/desktop/proghist-dest/
```

Cette commande copie tous les fichiers textes depuis le répertoire d'origine vers le répertoire de destination.

Note&nbsp;: Si vous vous trouvez dans le répertoire depuis ou vers lequel vous déplacez des fichiers, vous n'avez pas besoin d'écrire tout le chemin du répertoire. Faisons deux exemples rapides. Déplacez-vous dans le répertoire `proghist-texte`. Depuis cet emplacement, si vous souhaitez copier vos fichiers vers `proghist-dest`, cette commande fonctionnera&nbsp;:

```bash
cp *.txt /Users/ianmilligan1/desktop/proghist-dest/
```

De la même façon, si vous êtes dans le répertoire `proghist-dest`, la même commande s'écrit&nbsp;:

```bash
cp /Users/ianmilligan1/desktop/proghist-texte/*.txt ./
```

La commande `./` ou `.` représente le &laquo;&nbsp;répertoire courant&nbsp;&raquo; dans lequel vous vous trouvez. C'est une commande très importante.

Enfin, si vous souhaitez effacer un fichier, vous devrez utiliser la commande `rm` (&laquo;&nbsp;remove&nbsp;&raquo;). Soyez très prudent avec la commande `rm` afin de ne pas supprimer des fichiers par erreur. Contrairement à la suppression en passant par le GUI, il n'y a pas de corbeille ou de retour en arrière possible. Pour ces raisons, si vous avez un doute, soyez très prudent ou effectuez une sauvegarde régulière de vos données. Ces conseils sont d'autant plus valables si vous utilisez des métacaractères pour supprimer plusieurs fichiers d'un coup.

Déplacez-vous dans `proghist-texte` et supprimez le fichier original en tapant&nbsp;:

```bash
rm tolstoy.txt
```

Vérifiez que le fichier n'est plus là avec la commande `ls`.

Si vous souhaitez supprimer un répertoire entier, vous avez deux options:
- Pour un répertoire vide, vous pouvez utiliser `rmdir`, l'opposé de `mkdir`
- Pour un répertoire contenant des fichiers, vous pouvez utiliser la commande `rm` avec l'option `-r` (signifiant &laquo;&nbsp;recursive&nbsp;&raquo;) qui supprimera le dossier et tout ce qu'il contient

Ainsi, depuis le bureau vous pouvez exécuter la commande&nbsp;:

```bash
rm -r proghist-texte
```

## Conclusion

À ce stade, vous avez sans doute envie de prendre une pause et de fermer votre terminal. Pour faire cela, tapez&nbsp;:

```bash
exit
```

Il existe de nombreuses autres commandes à essayer lorsque vous serez plus à l'aise avec l'interface en ligne de commande. Une commande très utile est `du`, qui permet de connaitre combien de stockage est utilisé (`du -h` affiche la mémoire d'une façon lisible par l'humain). Pour les personnes qui utilisent Linux ou macOS, `top` procure un aperçu des processus en cours (`mem` sous Windows). Si vous souhaitez créer un fichier texte basique, vous pouvez utiliser `touch FILENAME`, qui fonctionne sur tous les systèmes.

Nous espérons que vous avez maintenant une bonne compréhension des fonctionnalités de base de l'interface en ligne de commande&nbsp;: vous déplacer à travers l'arborescence, déplacer, copier et supprimer des fichiers ou répertoires, ainsi qu'effectuer de petites modifications dans les fichiers. Cette leçon destinée aux débutant·es avait pour but de vous faire découvrir les bases et de vous faire gagner en confiance dans l'utilisation du terminal. À l'avenir, vous pourriez même avoir envie d'écrire des scripts&nbsp;!

Amusez-vous et expérimentez&nbsp;! Très rapidement, vous pourriez vous mettre à apprécier la ligne de commande pour son côté pratique et sa précision (pour certains usages, en tout cas) et surtout pour sa légèreté en comparaison aux lourdes interfaces graphiques de votre système d'exploitation. Dans tous les cas, vous venez d'ajouter une nouvelle corde à votre arc.

## Guide de référence

Pour qu'il soit plus facile de retrouver les commandes vues durant la leçon, voici un tableau récapitulatif&nbsp;:

| Commande              | Ce qu'elle fait                                                                                                                      |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pwd`                | Imprime le répertoire courant (&laquo;&nbsp;print working directory&nbsp;&raquo;) pour vous permettre de savoir où vous êtes                                                           |
| `ls`                 | Liste les fichiers présents dans le répertoire courant                                                                                          |
| `man <commande>`              | Affiche le manuel pour une commande nommée `<commande>`                                            |
| `cd <répertoire>`               | Change le répertoire courant pour `<répertoire>`                                                                                              |
| `mkdir <répertoire>`            | Crée un répertoire nommé `<répertoire>`                                                                                                       |
| `open <fichier>` ou `explorer <fichier>` | Ouvre un fichier nommé `<fichier>` (`open` pour Linux ou Mac et `explorer` pour Windows)      |
| `cat <fichier>`              | `cat` est une commande versatile&nbsp;: elle lira un fichier nommé `<fichier>`, mais peut aussi être utilisée pour afficher la combinaison de plusieurs fichiers |
| `head <fichier>`             | Affiche les dix premières lignes de `<fichier>`                                                                                               |
| `tail <fichier>`             | Affiche les dix dernières lignes de `<fichier>`                                                                                                |
| `mv`                 | Déplace un fichier ou un répertoire                                                                                                                      |
| `cp`                 | Copie un fichier ou un répertoire                                                                                                                     |
| `rm`                 | Supprime un fichier                                                                                                                    |
| `vim`                | Ouvre l'éditeur de document `vim`  
