---
title: Générer un jeu de données structuré à partir d’un texte océrisé
layout: lesson
slug: generer-jeu-donnees-texte-ocr
date: 2014-11-25
translation_date: 2021-11-19
authors:
- Jon Crump
reviewers:
- Brandon Hawk
editors:
- Fred Gibbs
translator: 
- Antoine Gourlay
translation-editor: 
- Gwenaëlle Patat
translation-reviewer:
- Floriane Chiffoleau
- Jean-Luc Mirepoix
original: generating-an-ordered-data-set-from-an-OCR-text-file
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/362
difficulty: 3
activity: transforming
topics: [data-manipulation]
abstract: "Ce tutoriel présente des stratégies pour traiter la sortie OCR brute issue d’un texte scanné, l’analyser afin d'isoler et de corriger les éléments essentiels des métadonnées, et générer un ensemble de données structuré (un dictionnaire Python) à partir de celle-ci."
avatar_alt: Une petite boîte avec une rangée de livres
doi: 10.46430/phfr0020
---

{% include toc.html %}

## Objectifs de la leçon
Ce tutoriel présente des stratégies pour obtenir un jeu de données ordonné (un dictionnaire de données Python) à partir d'un document scanné qui sera traité de façon à en extraire et éventuellement à en corriger les éléments de métadonnées. Les exemples présentés sont spécifiques à un texte particulier mais la stratégie globale ainsi que certaines procédures plus caractéristiques peuvent être appliquées pour traiter n'importe quel document scanné, même si ceux-ci ne sont pas forcément similaires au document présenté ici.

## Introduction
On rencontre souvent le cas de l'historien(ne) impliqué(e) dans un projet numérique et désirant travailler avec des documents numérisés, se disant&#x202F;: &laquo;&#x202F;OK, je n'ai qu'à scanner l'ensemble de ces ressources documentaires d'une incroyable richesse et exploiter les documents numériques obtenus&#x202F;!&#x202F;&raquo;. (Ceux d'entre nous qui se sont retrouvés dans ce cas de figure ont un petit sourire désabusé au coin des lèvres). Ces historien(ne)s découvrent bien vite que même les meilleurs systèmes de [reconnaissance optique de caractères](https://fr.wikipedia.org/wiki/Reconnaissance_optique_de_caract%C3%A8res) ou OCR (*optical character recognition*) entraînent un nombre d'erreurs important. Alors les historien(ne)s se disent&#x202F;: &laquo;&#x202F;OK, je vais réunir des fonds et constituer une armée d'étudiants, diplomés ou non, ou même de n'importe quel gamin sachant lire et écrire, pour corriger les approximations de mon OCR&#x202F;&raquo;. (Le sourire désabusé s'accentue sur les visages).

1. Il y a très peu de fonds accordés à ce type de recherche. De plus en plus, l'attention se porte sur les projets concernant les domaines du traitement automatique des langues (TAL), de la fouille de données (Data Mining), du Machine Learning, de l'analyse des graphes et apparentés, si bien que la question de produire de la documentation numérisée exploitable est délaissée. Sur le sujet, on a tendance à penser que Google s'occupe déjà des numérisations, n'est ce pas&#x202F;? Et quel pourrait bien être le problème avec les scans de Google&#x202F;? Et bien, vous trouverez la réponse à la fin...


2. Même si vous trouviez le moyen de réunir un grand nombre de petites mains pour vous assister dans votre projet, il y a de grandes chances pour qu'une collection de chartes italiennes écrites au <span style="font-variant:small-caps;">XII</span><sup>e</sup> siècle, traduites et publiées en 1935, les plongent dans un état de profonde dépression, fassent saigner leurs yeux et que le résultat soit toujours une grosse pile de documents contenant toujours une grande quantité d'erreurs sur lequel vous devrez encore effectuer un travail __difficile__ et __fastidieux__ afin de les rendre exploitables.

Parcourir un document ligne par ligne et corriger les erreurs de l'OCR quand elles se présentent est une source d'erreurs inévitables. Il existe toutefois des moyens d'éviter une partie de ce travail fastidieux en automatisant certaines tâches. Un langage de script tel que Perl ou Python peut vous permettre d'identifier et de traiter les erreurs communes de l'OCR et de les corriger à l'aide des [expressions régulières](https://fr.wikipedia.org/wiki/Expression_régulière), une façon d'identifier des motifs dans un texte (voir le tutoriel sur les [expressions régulières de L.T O'Hara)](/en/lessons/cleaning-ocrd-text-with-regular-expressions). Cependant, les expressions régulières ne vous seront utiles que si les expressions que vous recherchez sont régulières bien sûr. Malheureusement, une grande partie de ce que vous obtiendrez en sortie après avoir utilisé l'OCR sera tout sauf *régulier*. Si vous pouviez structurer ces données, votre outil d'analyse d'expression régulière deviendrait beaucoup plus utile.

Que se passerait-il si, par exemple, votre OCR interprétait les chaînes de caractères telles que &laquo;&#x202F;21 July, 1921&#x202F;&raquo; en &laquo;&#x202F;2l July, 192l&#x202F;&raquo;, remplaçant les &laquo;&#x202F;1&#x202F;&raquo; par des &laquo;&#x202F;l&#x202F;&raquo;. Vous apprécieriez grandement de savoir écrire un script de recherche et remplacement de toutes les instances de &laquo;&#x202F;2l&#x202F;&raquo; en &laquo;&#x202F;21&#x202F;&raquo;, mais que se passerait-il dans le cas où vous auriez un grand nombre d'occurences de cette chaîne de caractère dans votre document&#x202F;: &laquo;&#x202F;2lb. hammers&#x202F;&raquo;. Vous obtiendriez alors des &laquo;&#x202F;21b hammer&#x202F;&raquo;, ce que vous ne souhaitiez évidemment pas. Si seulement vous pouviez dire à votre script de ne changer les &laquo;&#x202F;2l&#x202F;&raquo; en &laquo;&#x202F;21&#x202F;&raquo; que dans les sections contenant des dates et non des unités de mesures. Si vous aviez à disposition un ensemble de données stucturé, vous pourriez faire ça.

Bien souvent, les documents que les historien(ne)s souhaitent numériser sont déjà des structures ordonnées de données&#x202F;: une collection ordonnée de documents issus d'une source primaire, un code juridique ou encore un cartulaire. Mais la structure éditoriale imposée à ces ressources est généralement conçue pour un type particulier de technologie d’extraction de données, c'est-à-dire un codex, un livre. Pour un texte numérisé, la structure utilisée sera différente. Si vous pouvez vous débarrasser de l’infrastructure liée au livre et réorganiser le texte selon les sections et les divisions qui vous intéressent, vous vous retrouverez avec des données sur lesquelles il sera beaucoup plus facile d'effectuer des recherches et des opérations de remplacement, et en bonus, votre texte deviendra immédiatement exploitable dans une multitude d’autres contextes.


C'est là qu'un langage de script comme Python devient très utile. Pour notre projet nous avons voulu préparer certains des documents d’une collection du <span style="font-variant:small-caps;">XII</span><sup>e</sup> siècle d’*imbreviatura* du scribe italien connu sous le nom de [Giovanni Scriba](http://www.worldcat.org/oclc/17591390) afin qu’ils puissent être traités par des historien(ne)s à des fins d’analyse TAL ou autres. Les pages de l'édition de 1935 ressemblent à cela&#x202F;:


{% include figure.html filename="gs_pg110.png" caption="GS page 110" %}


Le document issu du traitement OCR à partir du fichier scanné ressemble à cela malgré les nombreuses améliorations apportées (j'ai redimensionné les lignes les plus longues afin qu'elles s'adaptent à la mise en page)&#x202F;:

```
    110	MARIO CHIAUDANO MATTIA MORESCO
        professi sunt Alvernacium habere de i;psa societate lb. .c., in reditu
        tracto predicto capitali .ccc. lb. proficuum. debent dividere per medium. Ultra
        vero .cc. lb. capitalis Ingo de Volta lb. .xiv. habet quas cum ipso capitali de
        scicietate extrahere debet. Dedit preterea prefatus Ingo de Volta licenciam (1)
        ipsi Ingoni Nocentio portandi lb. .xxxvII. 2 Oberti Spinule et Ib. .xxvII.
        Wuilielmi Aradelli. Actum ante domum W. Buronis .MCLVII., .iiii. kalendas
        iulias, indicione quarta (2).
    L f o. 26 v.] .	CCVIII.
    Ingone Della Volta si obbliga verso Ingone Nocenzio di indennizzarlo di ogni
    danno che gli fosse derivato dalle societa che egli aveva con i suoi figli (28
    giugno 1157).
    Testes Ingonis Nocentii] .
        Die loco (3) ,predicto et testibus Wuilielmo Burone, Bono Iohanne
        Malfiiastro, Anselmo de Cafara, W. de Racedo, Wuilielmo Callige Pallii. Ego Ingo
        de Volta promitto tibi Ingoni Nocentio quod si aliquod dampnum acciderit tibi
        pro societate vel societatibus quam olim habueris cum filiis meis ego illud
        totum tibi restaurato et hoc tibi promitto sub pena dupli de quanto inde dampno
        habueris. Do tibi preterea licentiam accipiendi bisancios quos ultra mare
        acciipere debeo et inde facias tona fide quicquid tibi videbitur et inde ab omni
        danpno te absolvo quicquid inde contingerit.
    CCIX.
        Guglielmo di Razedo dichiara d'aver ricevuto in societatem da Guglielmo
    Barone una somma di denaro che portera laboratum ultramare (28 giugno 1157).
    Wuilielmi Buronis] .
            Testes Anselmus de Cafara, Albertus de Volta, W. Capdorgol, Corsus
    Serre, Angelotus, Ingo Noncencius. Ego W. de Raeedo profiteor me accepisse a te
    Wuilielmo Burone lb. duocentum sexaginta tre et s. .XIII. 1/2 in societatem ad
    quartam proficui, eas debeo portare laboratum ultra mare et inde quo voluero, in
    reditu,
    (11 Licentiam in sopralinea in potestatem cancellato.
    (2) A margine le postille: Pro Ingone Nocentio scripta e due pro Alvernacio.
    (3) Cancellato: et testibus supradictis.
```

Dans le scan de l’original, l'œil du lecteur analyse facilement la page&#x202F;: la mise en page a un sens. Mais comme vous pouvez le voir, réduit à un texte simple comme celui-ci, aucune des métadonnées impliquées par la mise en page et la typographie ne peut être différenciée par des processus automatisés.


Vous pouvez constater à partir du scan que chaque charte comporte les métadonnées qui lui sont associées&#x202F;:

* Numéro de charte
* Numéro de page
* Numéro de folio
* Un résumé italien, se terminant par une date quelconque
* Une ligne, qui se termine habituellement par un crochet fermant (]) qui représente une note de marge dans l’original
* Un ensemble de marqueurs de bas de page numérotés, dont la représentation textuelle apparaît au bas de chaque page de façon séquentielle, et redémarrant à partir de 1 sur chaque nouvelle page.
* Le texte latin de la charte elle-même

Tout cela est typique de ce type de ressources, bien que les conventions d'éditions puissent varier. Le fait est qu'il s'agit bien d'un ensemble **ordonné** de données et non simplement d'une chaîne de caractères interminable. Avec des scripts Python assez simples, nous pouvons transformer notre sortie OCR en un ensemble de données ordonnées, dans ce cas un [dictionnaire Python](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries), **avant** de commencer à apporter des corrections au texte en lui-même. Avec un tel jeu de données ordonné en main, nous pouvons apporter des éléments de correction, et potentiellement effectuer beaucoup d’autres types de tâches, de manière plus efficace. 


Ainsi, le but de ce tutoriel est de prendre un fichier texte brut, comme la sortie OCR ci-dessus, et de le transformer en un dictionnaire Python avec des champs pour le texte latin de la charte et pour chacun des éléments de métadonnées mentionnés ci-dessus&#x202F;:


```python
{
.
.
.
 52: {'chid': 'GScriba_LII',
      'chno': 52,
      'date': datetime.date(1156, 3, 27),
      'folio': '[fo. 6 r.]',
      'footnotes': [(1, 'Cancellato: m.')],
      'marginal': 'no marginal]',
      'pgno': 29,
      'summary': 'I consoli di Genova riconoscono con sentenza il diritto di Romano di Casella di pagarsi sui beni di Gerardo Confector per un credito che aveva verso il medesimo (27 marzo 1156).',
      'text': ['    In pontili capituli consules E. Aurie, W. Buronus, Ogerius Ventus laudaverunt quod Romanus de Casella haberet in bonis Gerardi Confectoris s. .xxvi. denariorum et possit eos accipere sine contradicione eius et omnium pro eo. Hoc ideo quia, cum; Romanus ante ipsos inde conquereretur, ipso Gerardo debitum non negante, sed quod de usura esset obiiciendo, iuravit nominatus Romanus quod capitalis erat (1) et non de usura, unde ut supra laudaverunt , .MCLVI., sexto kalendas aprilis, indicione tercia.\n']},
 53: {'chid': 'GScriba_LIII',
      'chno': 53,
      'date': datetime.date(1156, 3, 27),
      'folio': '[fo. 6 r.]',
      'footnotes': [],
      'marginal': 'Belmusti]',
      'pgno': 29,
      'summary': "Maestro Arnaldo e Giordan nipote del fu Giovanni di Piacenza si obbligano di pagare una somma nell'ottava della prossima Pasqua, per merce ricevuta (27 marzo 1156).",
      'text': ['  Testes Conradus Porcellus, Albericus, Vassallus Gambalixa, Petrus Artodi. Nos Arnaldus magister et Iordan nepos quondam Iohannis Placentie accepimus a te Belmusto tantum bracile unde promittimus dare tibi vel tuo certo misso lb. .xLIII. denariorum usque octavam proximi pasce, quod si non fecerimus penam dupli tibi stipulanti promittimus, bona pignori, possis unumquemque convenire de toto. Actum prope campanile Sancti Laurentii, millesimo centesimo .Lv., sexto kalendas aprilis, indictione tercia.\n']},
.
.
. etc.
}
```

Souvenez-vous qu'il s'agit simplement d'une représentation textuelle d'une structure de données hébergée quelque part dans la mémoire de votre machine. Python désigne ce type de structure par le terme &laquo;&#x202F;dictionnaire&#x202F;&raquo;, mais d'autres langages de programmation y font référence en tant que &laquo;&#x202F;hachage&#x202F;&raquo; ou &laquo;&#x202F;tableau associatif&#x202F;&raquo;. Le fait est qu’il est infiniment plus facile de faire n’importe quelle sorte d’analyse ou de manipulation d’un texte numérique s’il est sous une telle forme, plutôt que sous la forme d’un fichier texte brut. L’avantage est qu’une telle structure de données peut être interrogée, ou des calculs peuvent être effectués sur les données, sans avoir à analyser le texte.

## Quelques informations utiles avant de démarrer
Nous allons emprunter quelques fonctions rédigées par d’autres. Elles représentent toutes les deux des programmes assez sophistiqués. Comprendre ce qui se passe dans ces fonctions est instructif, mais pas indispensable. Lire et réutiliser le code des autres est une bonne façon d'apprendre la programmation, et représente le cœur du mouvement open source. Même si vous ne comprenez pas tout à fait comment elles fonctionnent, vous pouvez néanmoins tester des fonctions comme celle-ci pour voir si elles fonctionnent vraiment, et les adapter à votre problématique si elles sont pertinentes.

### La distance de Levenshtein
Vous remarquerez que certaines des métadonnées énumérées ci-dessus sont liées à des pages et que d’autres sont liées à la charte. Le but, c’est de les séparer les unes des autres. Il y a une classe de données liées à la page qui ne nous est pas utile dans ce contexte, et seulement significative dans le contexte d’un livre physique&#x202F;: les en-têtes et pieds de page. Dans notre document, ils prennent cette forme-ci sur les feuilles recto (dans un codex, un livre, *recto* est la page de droite, et *verso* son inverse, la page de gauche)&#x202F;:


{% include figure.html filename="gs_recto_header.png" caption="en-tête recto" %}

et cette forme-là sur les feuilles *verso*&#x202F;:

{% include figure.html filename="gs_verso_header.png" caption="en-tête verso" %}

Nous aimerions préserver la pagination pour chaque page de la charte, mais le texte d’en-tête ne nous est pas utile et va simplement rendre toute opération de recherche ou de remplacement plus complexe. Nous aimerions donc l'identifier et le remplacer par une chaîne qui est facile à trouver avec une expression régulière, et enfin stocker le numéro de page.
Malheureusement, les expressions régulières ne vous seront pas d'une grande utilité dans le cas présent. Ces en-têtes peuvent apparaître sur n’importe quelle ligne du document obtenu après le traitement OCR, et l'efficacité avec laquelle le logiciel OCR peut les traiter est limitée. Voici quelques exemples d’en-têtes de page, *recto* et *verso*, dans notre sortie OCR brute.

```
    260	11141110 CH[AUDANO MATTIA MORESCO
    IL CIRTOL4RE DI CIOVINN1 St'Itlltl	269
    IL CJIRTOL.%RE DI G:OVeNNl FIM P%	297
    IL CIP.TQLIRE DI G'OVeNNI SCI Dt	r.23
    332	T1uu:0 CHIAUDANO M:11TIA MGRESCO
    IL CIRTOL.'RE DI G:OV.I\N( sca:FR	339
    342	NI .\ßlO CHIAUDANO 9LtTTIA MORESCO
```

Ces chaînes de caractères ne sont pas assez régulières pour être identifiées de façon fiable avec des expressions régulières; cependant, si vous savez ce à quoi les chaînes sont censées ressembler, vous pouvez composer une sorte d’algorithme de similarité de chaîne pour tester chaque chaîne par rapport à un modèle et mesurer la probabilité qu’il s’agisse d’un en-tête de page. Heureusement, je n’ai pas eu à composer un tel algorithme, [Vladimir Levenshtein l’a fait pour nous en 1965](https://fr.wikipedia.org/wiki/Distance_de_Levenshtein). Un langage informatique peut encoder cet algorithme de plusieurs façons ; voici une fonction Python efficace qui fera très bien l'affaire&#x202F;:


```python
'''
Code extrait de https://www.datacamp.com/community/tutorials/fuzzy-string-python
'''
def lev(seq1, seq2):
    """ levenshtein_ratio_and_distance:
        Pour tout i et j, la distance[i,j] contiendra la distance de 
        Levenshtein entre les premiers carcatères i de seq1 
        et les premiers carcatères j de seq2.
    """
    # Initialiser la matrice de zéros
    rows = len(seq1)+1
    cols = len(seq2)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Alimenter la matrice de zéros avec les indices de chaque caractère des deux chaînes de caractères
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Itérer sur la matrice pour calculer le taux de suppresssion, insertions et/ou substitutions   
    for col in range(1, cols):
        for row in range(1, rows):
            if seq1[row-1] == seq2[col-1]:
                cost = 0 # Si les caractères sont les mêmes dans les deux chaînes dans une position donnée [i,j] alors le taux est égal à 0
            else:
                # Afin d'aligner les résultats avec ceux du package Levenshtein de Python, si nous choisissons de calculer le ratio
                # le taux d'une substitution est égal à 2. Si nous calculons simplement la distance, alors le taux d'une substitution est égal à  1.
                cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Taux de suppressions
                                 distance[row][col-1] + 1,          # Taux d'insertions
                                 distance[row-1][col-1] + cost)     # Taux de substitutions

    return distance[row][col]
```

Encore une fois, il s'agit d'un algorithme assez sophistiqué, mais pour notre objectif tout ce que nous avons besoin de savoir c’est que la fonction `lev()` prend deux chaînes comme paramètres et retourne un nombre qui indique la &laquo;&#x202F;distance&#x202F;&raquo; entre les deux chaînes, ou combien de changements ont dû être apportés pour aller de la première chaîne à seconde. Donc&#x202F;: `lev("fizz", "buzz")` retourne &laquo;&#x202F;2&#x202F;&raquo;.


### Des chiffres romains aux chiffres arabes
Vous remarquerez aussi que dans l’édition publiée, les chartes sont numérotées en chiffres romains. Convertir des chiffres romains en arabe constitue un défi très formateur en Python. Voici la solution la plus propre et la plus élégante que je connaisse&#x202F;:


```python
def rom2ar(rom):
    """ Depuis la liste:
    János Juhász janos.juhasz at VELUX.com
    retourne l'équivalent numérique arabe de la valeur numérique romaine """
    roman_codec = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    roman = rom.upper()
    roman = list(roman)
    roman.reverse()
    decimal = [roman_codec[ch] for ch in roman]
    result = 0

    while len(decimal):
        act = decimal.pop()
        if len(decimal) and act < max(decimal):
            act = -act
        result += act

    return result
```
Exécutez ce <[petit script](/assets/chiffres_romains_arabes.txt)> pour voir en détail comment `rome2ar` fonctionne. Une programmation élégante comme celle-ci peut presque s'apparenter à de la poésie.

## D'autres informations importantes
Si vous avez besoin d'importer des modules faisant partie de la bibliothèque standard de Python, il faudra que les premières lignes de votre programme soient les imports de ces modules. Si besoin, voir le tutoriel de Fred Gibbs sur [*l'installation des bibliothèques Python avec pip*](/fr/lecons/installation-modules-python-pip).


1. Le premier est le module "re" (expression régulière) `import re`. Les expressions régulières sont vos amies. Cependant, n’oubliez pas la blague de Jamie Zawinski&#x202F;:


    >Quand elles se retrouvent confrontées à un problème, certaines personnes se disent&#x202F;: &laquo;&#x202F;Je n'ai qu'à utiliser les expressions régulières&#x202F;!&#x202F;&raquo; Elles se retrouvent alors avec deux problèmes.


    (Je vous recommande une nouvelle fois de jeter un coup d’œil à la présentation de L.T. O’Hara ici sur le site du Programming Historian [Cleaning OCR’d text with Regular Expressions](/en/lessons/cleaning-ocrd-text-with-regular-expressions))


2. Vous devrez réaliser l'import d'une bibliothèque Python qui nous sera utile&#x202F;: `from pprint import pprint`. Il s'agit d'un outil de formatage pour les objets Python comme les listes et les dictionnaires. Vous en aurez besoin parce que les dictionnaires Python sont beaucoup plus faciles à lire s’ils sont formatés.

3. L'import `from collections import Counter` nous sera utile pour la section [Identifier les notes de bas de page à l'aide d'une expression régulière](/en/lessons/generer-jeu-donnees-texte-ocr#identifier-notes-bas-de-page) que nous aborderons juste après. Ce n’est pas vraiment nécessaire, mais nous allons faire des opérations de comptage qui exigeraient beaucoup de lignes de code et cela nous épargnera du temps. Le module des collections a beaucoup d'utilité et vaut la peine qu'on se familiarise avec. Encore une fois, voir la présentation Pymotw de Doug Hellmann concernant le module des [collections](https://docs.python.org/fr/3/library/collections.html). Je souligne également que son livre [The Python Standard Library By Example](https://doughellmann.com/books/the-python-3-standard-library-by-example/) vaut le coût.

## Un petit aperçu des expressions régulières telles qu'elles sont implémentées en Python

[L’introduction](/en/lessons/cleaning-ocrd-text-with-regular-expressions#introduction) de L.T. O’Hara à l’utilisation d’expressions régulières en Python est inestimable. Dans ce contexte, nous devrions passer en revue quelques principes de base sur l’implémentation par Python d’expressions régulières, le module `re`, qui fait partie de la bibliothèque standard de Python.

1. `re.compile()` crée un objet de type expression régulière qui a un certain nombre de méthodes. Vous devriez vous familiariser avec `.match()`, et `.search()`, mais aussi `.findall()` et `.finditer()`.
2. Gardez à l’esprit la différence entre `.match()` et `.search()`: `.match()` ne cherche une correspondance qu’au **début** d’une ligne, alors que `.search()` parcourt toute la ligne mais **s’arrête à la première correspondance** et ne retourne que la première occurrence qu’il trouve.
3. `.match()` et `.search()` retournent les correspondances sous forme d'objets. Pour récupérer la chaîne de caractères correspondante, vous aurez besoin de `mymatch.group(0)`. Si votre expression régulière compilée contient des parenthèses de regroupement (comme notre regex 'slug' ci-dessous), vous pouvez les récupérer sous forme de sous-chaînes de la chaîne appariée en utilisant `mymatch.group(1)` etc.
4. `.findall()` et `.finditer()` retourneront **toutes** les occurrences de la chaîne correspondante ; `.findall()` les retournera sous forme de liste de chaînes, mais `.finditer()` retourne un **itérateur d’objets correspondant aux occurrences**. (lisez la documentation sur la méthode [.finditer()](https://docs.python.org/fr/3/library/re.html#re.finditer).



# Traitement itératif  de fichiers textes
Nous allons commencer avec un seul fichier issu d'un traitement OCR. Nous générerons itérativement de nouvelles versions corrigées de ce fichier en l’utilisant comme entrée pour nos scripts Python. Parfois notre script va apporter des corrections automatiques mais, le plus souvent, nos scripts vont simplement nous alerter de l’endroit où se trouvent les problèmes dans le fichier d’entrée, et nous allons apporter des corrections manuellement. Ainsi, pour les premières opérations, nous voudrons produire de nouveaux fichiers textes révisés que nous utiliserons comme entrées pour les traitements à venir. Chaque fois que vous produisez un fichier texte, vous devrez le versioner et le dupliquer pour pouvoir toujours y revenir. La prochaine fois que vous exécutez votre code (au moment ou vous le développez) vous pourriez altérer le fichier et il sera toujours plus simple de restaurer l’ancienne version.

Le code de ce tutoriel est fortement édité&#x202F;; il n’est **pas** exhaustif. Au fur et à mesure que vous peaufinerez vos fichiers d’entrée, vous écrirez beaucoup de petits scripts *ad hoc* pour vérifier l’efficacité de ce que vous avez fait jusqu’à présent. La gestion des versions vous permettra de mener vos expérimentations sans compromettre le travail déjà réalisé.

## Un mot sur le déploiement du code dans ce tutoriel
Le code proposé dans ce tutoriel est valable pour la version 3 de Python.

Lorsque vous écrivez du code dans un fichier texte et que vous l’exécutez, soit en ligne de commande, soit à partir de votre éditeur de texte ou de l’IDE, l’interpréteur Python exécute le code ligne par ligne, de haut en bas. Ainsi, le code au bas de la page dépendra souvent du code au-dessus.

Une façon d’utiliser les extraits de code de la section 2 pourrait être de les réunir dans un seul fichier et de commenter les lignes que vous ne voulez pas exécuter. Chaque fois que vous exécuterez le fichier, vous voudrez avoir la certitude qu’il y a un déroulement logique à partir de la ligne `#!` en haut, à travers vos différentes `import`s et dans la déclaration de variables globales, et à chaque boucle ou bloc.

Sinon, chacune des sous-sections de la section 2 peut également être traitée comme un script à part et chacun devra alors faire sa propre `import`ation et déclaration de variables globales.

Dans la section 3, « Création du dictionnaire », vous utiliserez un ensemble de données stockées en mémoire (le dictionnaire des `chartes`) qui sera généré à partir du texte d’entrée le plus récent et cohérent que vous avez. Vous voudrez donc conserver un unique module Python dans lequel vous définirez en premier lieu le dictionnaire, avec vos déclarations d’`import` et l’attribution de variables globales, suivi de chacune des quatre boucles qui modifieront le dictionnaire.

```python
#!/usr/bin/python

import re
from pprint import pprint
from collections import Counter

# suivi de toutes les variables globales dont vous aurez besoin, par exemple:

n = 0
this_folio  = '[fo. 1 r.]'
this_page = 1

# les expressions régulières compilées:
slug = re.compile("(\[~~~~\sGScriba_)(.*)\s::::\s(\d+)\s~~~~\]")
fol = re.compile("\[fo\.\s?\d+\s?[rv]\.\s?\]")
pgbrk = re.compile("~~~~~ PAGE (\d+) ~~~~~")

# le fichier original à partir duquel vous commencerez à travailler
fin = open("/path/to/your/current/canonical.txt", 'r')
GScriba = fin.readlines()


# enfin le dictionnaire vide:
charters = dict()

# suivi des 4 boucles 'for' de la section qui vont alimenter et modifier le dictionnaire
```
## Découpage du texte par pages

Tout d’abord, nous voulons trouver tous les en-têtes de page présents au *recto* et au *verso* et les remplacer par des chaînes cohérentes que nous pouvons facilement identifier avec une expression régulière. Le code suivant recherche des lignes qui sont similaires à ce que nous savons être nos en-têtes de page jusqu'à un certain seuil. Il faudra quelques expérimentations pour trouver ce seuil pour votre texte. Comme mes en-têtes *recto* et *verso* sont à peu près de la même longueur, les deux ont le même score de similitude de 26.
> NOTA BENE&#x202F;: la fonction `lev()` décrite ci-dessus retourne une mesure de la &laquo;&#x202F;distance&#x202F;&raquo; entre deux chaînes, donc, plus la chaîne d’en-tête de page est courte, plus il est probable que cette technique ne fonctionnera pas. Si votre en-tête de page est simplement &laquo;&#x202F;en-tête&#x202F;&raquo;, alors toute ligne composée d’un mot de sept lettres pourrait vous donner une distance de chaîne de 7, par exemple&#x202F;: `lev("en-tête", "palavas")` retourne '7', ce qui ne vous éclaire pas plus. Dans notre texte, cependant, les chaînes d’en-tête sont assez longues et complexes pour vous donner des indications significatives, par exemple&#x202F;:

`lev("UNE CHAÎNE LAMBDA DE MÊME LONGUEUR: 38", 'IL CARTOLARE DI GIOVANNI SCRIBA')`

retourne 33, mais une de nos chaînes d’en-tête, même estropiée par l’OCR, retourne 20&#x202F;:

`lev("IL CIRTOL4RE DI CIOVINN1 St'Itlltl     269", 'IL CARTOLARE DI GIOVANNI SCRIBA')`

Nous pouvons donc utiliser `lev()` pour trouver et modifier nos chaînes d’en-tête ainsi&#x202F;:

```python
# en premier lieu, faites les import dont vous aurez besoin et définissez la fonction lev() comme décrite ci-dessus, et enfin:

fin = open("our_base_OCR_result.txt", 'r') # lit notre texte récupéré de l’OCR
fout = open("out1.txt", 'w') # crée un nouveau fichier texte pour le modifier quand nous sommes prêts
GScriba = fin.readlines() # transforme notre fichier d’entrée en une liste de lignes

for line in GScriba:
    # obtenez la distance de Levenshtein pour chaque ligne du texte
    recto_lev_score = lev(line, 'IL CARTOLARE DI GIOVANNI SCRIBA')
    verso_lev_score = lev(line, 'MARIO CHIAUDANO - MATTIA MORESCO')

    # vous voulez utilisez les scores les plus élevés possibles,
    # tout en voulant cibler uniquement les en-têtes de page.
    if recto_lev_score < 26 :

        # Si nous incrémentons une variable 'n' pour compter le nombre d'en-têtes trouvés
        # alors la valeur de cette variable devrait être équivalente à notre nombre de page.
        n += 1
        print(f"recto: {recto_lev_score} {line}")

        # Une fois que nous avons pu établir notre score lev() optimal, nous pouvons 'décommenter'
        # tout ces `fout.write()` pour rédiger notre nouveau document texte
        # en remplacant chaque en-tête par une chaîne de caractères facilement identifiable qui contiendra
        # le numéro de la page: notre variable 'n'.

        #fout.write("~~~~~ PAGE %d ~~~~~\n\n" % n)
    elif verso_lev_score < 26 :
        n += 1
        print(f"verso: {verso_lev_score} {line}")
        #fout.write("~~~~~ PAGE %d ~~~~~\n\n" % n)
    else:
        #fout.write(line)
        pass

print(n)
```

Il y a beaucoup de calculs qui s'éxécutent dans la fonction `lev()`. Il n’est pas très efficace de l’appeler sur toutes les lignes de notre texte, donc cela pourrait prendre un certain temps, selon la longueur de notre texte. Nous n’avons que 803 chartes dans le vol. 1. C’est un nombre qui reste modeste. Si cela prend 30 secondes ou même une minute pour exécuter notre scénario, alors qu’il en soit ainsi.

Si nous exécutons ce script sur notre texte après traitement OCR, nous obtenons une sortie qui ressemble à ceci&#x202F;:

```python
.
.
.
verso: 8 426	MARIO CHIAUDANO MAITIA MORESCO
recto: 5 IL CARTOLARE DI GIOVANNI SCRIBA	427
verso: 11 , ,	428	MARIO CHIAUDANO MATTIA MORESCO
recto: 5 IL CARTOLARE DI GIOVANNI SCRIBA	499
verso: 7 430	MARIO CHIAUDANO MATTIA MORESCO
recto: 5 IL CARTOLARE DI GIOVANNI SCRIBA	431
verso: 8 432	MARIO CHIAUDASO MATTIA MORESCO
430
```

Pour chaque ligne, la sortie nous indique si c'est la page *verso* ou *recto*, le &laquo;&#x202F;score&#x202F;&raquo; de Levenshtein, puis le texte de la ligne (avec toutes les erreurs dedans). Notez que l'OCR a mal interprété le chiffre de la page pour la page 429. Plus le « score » de Levenshtein est bas, plus la ligne se rapproche du modèle que vous lui avez donné.

Cela vous indique que le script a trouvé 430 lignes qui sont probablement des en-têtes de page. Vous savez combien de pages il devrait y avoir, donc si le script n’a pas trouvé tous les en-têtes, vous pouvez passer par la sortie en regardant les numéros de page, trouver les pages qu’il a manqué, et corriger les en-têtes manuellement, puis répéter l'opération jusqu’à ce que le script trouve tous les en-têtes de page.

Une fois que vous avez trouvé et corrigé les en-têtes que le script n’a pas trouvés, vous pouvez alors écrire le texte corrigé dans un nouveau fichier qui servira de base pour les autres opérations ci-dessous. Donc à la place de

```python
quicquid volueris sine omni mea et
(1) Spazio bianco nel ms.

12	MARIO CSIAUDANO MATTIA MORESCO
heredum meorum contradicione. Actum in capitulo .MCLV., mensis iulii, indicione secunda.
```

Nous aurons le fichier texte&#x202F;:

```Python
quicquid volueris sine omni mea et
(1) Spazio bianco nel ms.

~~~~~ PAGE 12 ~~~~~

heredum meorum contradicione. Actum in capitulo .MCLV., mensis iulii, indicione secunda.
```

Notez que pour beaucoup des opérations suivantes, nous utiliserons `Gscriba = fin.readlines()` donc Gscriba sera une **liste python** des lignes de notre texte d’entrée. Gardez cela à l’esprit, car les boucles `for` que nous utiliserons dépendront du fait que nous allons itérer à travers les lignes de notre texte dans l'ordre du document.

## Découpage du texte par charte (ou par section, lettre ou ce que vous souhaitez)

Le texte est découpé en plusieurs sous parties que constituent nos chartes et celles-ci sont délimitées par des chiffres romains majuscules sur une ligne à part. Nous avons donc besoin d’une regex pour trouver des chiffres romains de ce type. En voici une&#x202F;: `romstr = re.compile(" s*[IVXLCDM]{2,}")`. Nous la placerons en haut de notre fichier comme variable &laquo;&#x202F;globale&#x202F;&raquo;, de sorte qu’elle sera accessible à n’importe lequel des morceaux de code que nous écrirons plus tard.

Le script ci-dessous va chercher des chiffres romains majuscules qui apparaissent sur une ligne à part. Bon nombre de nos numéros de chartes échoueront à ce test et le script indiquera qu'il manque un numéro de charte, souvent parce qu’il y a quelque chose avant ou après sur la ligne&#x202F;; ou, `KeyError`, souvent parce que l’OCR a brouillé les caractères (par ex. CCG pour 300, XOII pour 492). Exécutez ce script plusieurs fois, en corrigeant `out1.txt` comme vous savez maintenant le faire jusqu’à ce que toutes les chartes soient prises en compte.

```python
# En premier lieu, réalisez les import dont vous aurez besoin, puis définissez rom2ar() de la même façon que ci-dessus, et enfin&#x202F;:
n = 0
romstr = re.compile("\s*[IVXLCDM]{2,}")
fin = open("out1.txt", 'r')
fout = open("out2.txt", 'w')
GScriba = fin.readlines()

for line in GScriba:
    if romstr.match(line):
        rnum = line.strip().strip('.')
        # à chaque fois que nous trouvons un chiffre romain isolé sur une ligne nous incrémentons n:
        # cela représente notre numéro de charte.
        n += 1
        try:
            # traduisez les chiffres romains en chiffres arabes et cela devrait être égal à n.
            if n != rom2ar(rnum):
                # si ce n'est pas le cas, alors signalez-le nous
                print(f"{n}, il manque un numéro de charte en chiffre romain?, car la ligne numéro {GScriba.index(line)} indique: {line}")
                # puis réinitialisez 'n' à la bonne valeur
                n = rom2ar(rnum)
        except KeyError:
            print(f"{n}, KeyError, line number {GScriba.index(line)} reads: {line}")
```

Puisque nous savons combien de chartes il devrait y avoir. À la fin de notre boucle, la valeur de n devrait être la même que le nombre de chartes. Et, dans toute itération de la boucle, si la valeur de n ne correspond pas au numéro de la charte qui suit, alors nous savons que nous avons un problème quelque part, et les `print` pour l'affichage en console devraient nous aider à le trouver.

Voici un exemple de sortie que notre script devrait nous donner&#x202F;:

```python
23 il manque un numéro de charte en chiffre romain?, car la ligne numéro  156  indique:  XXIV.
25 il manque un numéro de charte en chiffre romain?, car la ligne numéro  186  indique:  XXVIII.
36 KeyError, la ligne numéro  235  indique:  XXXV1.
37 KeyError, la ligne numéro  239  indique:  XXXV II.
38 il manque un numéro de charte en chiffre romain?, car la ligne numéro  252  indique:  XL.
41 il manque un numéro de charte en chiffre romain?, car la ligne numéro  262  indique:  XLII.
43 KeyError, la ligne numéro  265  indique:  XL:III.
```

> NOTA BENE&#x202F;: notre regex signalera une erreur pour les chiffres romains à un chiffre (« I », « V », « X », etc.). Vous pourriez les tester dans le code, mais parfois laisser une erreur connue et commune est une aide pour vérifier l’efficacité de ce que vous faites. Notre objectif est de nous assurer que toutes les incohérences sur la ligne de numéro de la charte sont bien détectées.

Une fois que nous avons trouvé et corrigé tous les en-têtes de charte en chiffres romains, alors nous pouvons écrire un nouveau fichier avec une chaîne facile à trouver grâce à notre regex, une &laquo;&#x202F;slug&#x202F;&raquo;, pour chaque charte à la place du nombre romain de départ. Mettez la boucle `for` ci-dessus en commentaire, et remplacez-la par celle-ci&#x202F;:

```python
for line in GScriba:
    if romstr.match(line):
        rnum = line.strip().strip('.')
        num = rom2ar(rnum)
        fout.write("[~~~~ GScriba_%s :::: %d ~~~~]\n" % (rnum, num))
    else:
        fout.write(line)
```

Bien qu’il soit important en soi pour nous d’avoir transformé notre sortie OCR de façon fiable et de l'avoir divisée par page et par charte, la chose la plus importante à propos de ces opérations est que vous connaissez le nombre de pages et de chartes, et que vous pouvez utiliser ces connaissances pour vérifier les opérations subséquentes. Si vous voulez réaliser une opération pour chaque charte, vous pouvez vérifier si celle-ci a fonctionné ou non parce que vous pouvez compter le nombre de chartes sur lesquelles elle aura fonctionné préalablement.

## Identifier les marqueurs de folio à l'aide d'une expression régulière

Notre texte est tiré de l’édition de 1935 de Giovanni Scriba. Il s’agit d’une transcription d’un manuscrit cartulaire sous la forme d’un livre relié. L’édition publiée conserve la pagination de l'original en notant où les pages originales changent&#x202F;: [fo. 16 r.] le recto de la <span style="font-variant:small-caps;">16</span><sup>e</sup> feuille du livre, suivie de son verso[fo. 16 v.]. Il s’agit de métadonnées que nous voulons préserver pour chacune des chartes afin qu’elles puissent être référencées par rapport à l’original, ainsi que par rapport à l’édition publiée par numéro de page.

Bon nombre des marqueurs de folio (par ex. &laquo;&#x202F;[fo. 16 v.]&#x202F;&raquo;) apparaissent sur la même ligne que le chiffre romain de l’en-tête de la charte. Pour normaliser ces en-têtes de chartes pour l’opération ci-dessus, nous avons dû créer une rupture de ligne entre le marqueur de folio et le numéro de charte, de sorte que beaucoup de marqueurs de folio sont déjà sur leur propre ligne. Cependant, il arrive que le folio change quelque part au milieu du texte de la charte. Nous voulons que ces balises restent là où elles sont&#x202F;; nous devrons traiter ces deux cas différemment. Dans les deux cas, nous devons nous assurer que tous les marqueurs de folio sont exempts d’erreurs afin de pouvoir les trouver de façon fiable au moyen d’une expression régulière. Encore une fois, puisque nous savons combien il y a de folios, nous pouvons savoir si nous les avons tous trouvés. Notez que parce que nous avons utilisé `.readlines()`, `Gscriba` est une liste, donc le script ci-dessous va afficher en console le numéro de ligne du fichier 
source ainsi que la ligne elle-même. Cela va vous permettre d'identifier tous les marqueurs de folio correctement formatés, de sorte que vous puissiez trouver et réparer ceux qui ont un problème.

```python
# vous voyez le quantificateur optionnel '\s?'. Nous voulons en trouver le plus possible,
# l'OCR  a un traitement assez chaotique des espaces alors notre regex est plutôt permissive. Mais à mesure que 
# vous trouverez et corrigerez ces chaînes, vous voudrez les rendre constantes.
fol = re.compile("\[fo\.\s?\d+\s?[rv]\.\s?\]")

for line in GScriba:
    if fol.match(line):
        # comme GScriba est une liste, nous pouvons obtenir l'index de n'importe lequel de ses éléments pour trouver le numéro de ligne correspondant dans notre fichier d'entrée.
        print GScriba.index(line), line
```

Nous voulons aussi nous assurer qu'aucune ligne ne possède plus d'un marqueur de folio. Nous pouvons nous en assurer en faisant ceci&#x202F;:

```python
for line in GScriba:
    all = fol.findall(line)
    if len(all) > 1:
        print GScriba.index(line), line
```

Comme vous l'avez fait précedemment, une fois que vous avez trouvé et corrigé tous les marqueurs de folio dans votre fichier d’entrée, enregistrez-le avec un nouveau nom et 
utilisez-le comme entrée à la section suivante.

## Identifier le résumé de la page en italien à l'aide d'une expression régulière
Cette ligne est invariablement la première après l'en-tête de la charte.

{% include figure.html filename="gs_italian_summary.png" caption="Ligne de résumé en italien" %}

Étant donné que les en-têtes en chiffres romains sont maintenant facilement repérables grâce à notre regex &laquo;&#x202F;slug&#x202F;&raquo;, nous pouvons maintenant isoler la ligne qui apparaît immédiatement après. Nous savons aussi que les résumés se terminent toujours par une sorte de référence datée entre parenthèses. Ainsi, nous pouvons composer une expression régulière pour trouver le &laquo;&#x202F;slug&#x202F;&raquo; et la ligne qui lui succède&#x202F;:

```python
slug_and_firstline = re.compile("(\[~~~~\sGScriba_)(.*)\s::::\s(\d+)\s~~~~\]\n(.*)(\(\d?.*\d+\))")
```

Décomposons cette regex en utilisant le mode verbeux (voir le tutoriel d’[O’Hara](/en/lessons/cleaning-ocrd-text-with-regular-expressions)). Notre &laquo;&#x202F;slug&#x202F;&raquo; pour chaque charte prend la forme « [~~~~ Gscriba_ccvii ::: : 207 ~~~~]» par exemple. Le modèle compilé ci-dessus est exactement équivalent à celui-ci(notez le commutateur re.VERBOSE à la fin)&#x202F;:

```python
slug_and_firstline = re.compile(r"""
    (\[~~~~\sGScriba_)  # capture le morceau "[~~~~ GScriba_"
    (.*)                # capture le numéro de charte en chiffre romain
    \s::::\s            # capture le morceau " :::: "
    (\d+)               # capture le numéro de charte en chiffre arabe
    \s~~~~\]\n          # capture le dernier morceau " ~~~~ " et la fin de la ligne
    (.*)                # capture tout le bloc de test jusqu'à :
    (\(\d?.*\d+\))      # l'expression entre parenthèses à la fin
    """, re.VERBOSE)
```

Les parenthèses délimitent les groupes de matchs, de sorte que chaque fois que notre regex trouve une correspondance, nous pouvons nous référer dans notre code à des morceaux spécifiques de la correspondance qu’il a trouvé&#x202F;:

* `match.group(0)` est l’ensemble de ce qui est capturé, à la fois notre " slug " et la ligne qui le suit.
* `match.group(1)` = « [~~~~ Gscriba_»
* `match.group(2)` = le numéro romain de la charte
* `match.group(3)` = le numéro arabe de la charte 
* `match.group(4)` = l’ensemble de la ligne comprenant le résumé en italien jusqu’à la date entre parenthèses
* `match.group(5)` = l’expression de la date entre parenthèses. Notez l'échappement des parenthèses.

Parce que notre sortie OCR contient beaucoup de ces mystérieux espaces blancs (les logiciels OCR ne sont pas bons pour interpréter les espaces blancs et vous êtes susceptible d’obtenir des nouvelles lignes, onglets, espaces, tous mélangés sans raison apparente), nous voulons identifier cette regex comme sous-chaîne d’une plus grande chaîne, donc cette fois nous allons utiliser `.read()` au lieu de `.readlines()`. Et nous aurons également besoin d’un compteur pour numéroter les lignes que nous trouvons. Ce script indiquera les numéros de chartes lorsque la première ligne n’est pas conforme à notre modèle regex. Cela se produit généralement s’il n’y a pas de saut de ligne après notre en-tête de charte, ou si la ligne de résumé a été divisée en plusieurs lignes.

```python
num_firstlines = 0
fin = open("your_current_source_file.txt", 'r')
# NB: GScriba n'est pas une liste de lignes cette fois, mais une simple chaîne de caractères
GScriba = fin.read()

# finditer() génère un itérateur 'i' sur lequel nous pouvons effectuer une boucle 'for'
i = slug_and_firstline.finditer(GScriba)

# chaque élément 'x' dans cet itérateur est un objet 'match' de notre regex.
for x in i:
    # compter les lignes de résumé que nous trouvons. Rappelez-vous, nous savons combien
    # il devrait y en avoir, parce que nous savons combien il y a de chartes.
    num_firstlines += 1

    chno = int(x.group(3)) # notre numéro de charte est une chaîne et nous avons besoin d'un nombre entier

    # chno devrait être égal à n + 1, et si ce n'est pas le cas signale le nous
    if chno != n + 1:
        print(f"problème dans la charte: {(n + 1)}") # NB: cela ne permettra pas de résoudre de potentiels problèmes consécutifs.
    # puis réinitialisez n au bon numéro de charte
    n = chno

# écrire en console le nombre de lignes de résumé que nous avons trouvé
print(f"nombre de lignes de résumé en italien: {num_firstlines}")
```

Exécutez de nouveau le script plusieurs fois jusqu’à ce que toutes les lignes de résumé soient présentes et correctes, puis enregistrez-le avec un nouveau nom et réutilisez-le comme fichier d’entrée&#x202F;:

## Identifier les notes de bas de page à l'aide d'une expression régulière

Un des aspects les plus difficiles à gérer est la convention éditoriale exaspérante qui consiste à redémarrer la numérotation des notes de bas de page avec chaque nouvelle page. Il est donc difficile d’associer un texte de note de bas de page (données liées à la page) à un marqueur de note de bas de page (données liées à la charte). Avant de le faire, nous devons nous assurer que le texte de chaque note qui apparaît au bas de la page, apparaît aussi dans notre fichier source sur sa propre ligne distincte sans commencer par un espace blanc. Et, par ailleurs, qu’**aucun** des marqueurs de note dans le texte n’apparaît au début d’une ligne. Aussi, nous devons veiller à ce que chaque chaîne de note de bas de page, par exemple &laquo;&#x202F;(1)&#x202F;&raquo; apparait **exactement** deux fois sur une page, une fois comme un marqueur dans le texte, et une fois au bas du texte de la note de bas de page. Le script suivant indique le numéro de page de toute page qui échoue à ce test, ainsi qu’une liste de la note de bas de page.

```python
# n'oubliez pas d'importer le module Counter:
from collections import Counter
fin = open("your_current_source_file.txt", 'r')
GScriba = fin.readlines() # GScriba est de nouveau une liste
r = re.compile("\(\d{1,2}\)") # l'OCR peut très facilement générer des erreurs sur cette partie, alors soyez vigilant.
pg = re.compile("~~~~~ PAGE \d+ ~~~~~")
pgno = 0

pgfnlist = []
# rappelez-vous, nous traitons les lignes dans l’ordre des documents. Donc, pour chaque page
# nous allons remplir un conteneur temporaire, 'pgfnlist', avec des valeurs. Puis
# quand nous arriverons à une nouvelle page, nous rendrons compte de ces valeurs
# et enfin nous réinitialiserons notre conteneur à la liste vide.

for line in GScriba:
    if pg.match(line):
        # si ce test est vrai, alors nous commençons une nouvelle page, donc il faut incrémenter pgno
        pgno += 1

        # si nous avons commencé une nouvelle page, puis testé notre liste de marqueurs de note de bas de page
        if pgfnlist:
            c = Counter(pgfnlist)

            # s’il y a des marqueurs fn qui n’apparaissent pas exactement deux fois,
            # alors nous signaler le numéro de page correspondant
            if 1 in c.values(): print(pgno, pgfnlist)

            # puis réinitialiser notre liste à vide
            pgfnlist = []

    # pour chaque ligne, rechercher TOUS les événements de notre marqueur regex de bas de page
    i = r.finditer(line)
    for mark in [eval(x.group(0)) for x in i]:
        # et ajouter les à la liste pour cette page
        pgfnlist.append(mark)
```

> Note&#x202F;: les éléments de l’itérateur &laquo;&#x202F;i&#x202F;&raquo; sont des correspondances de chaînes. Nous voulons les chaînes qui ont été appariées,  `group(0)`, par ex. &laquo;&#x202F;(1)&#x202F;&raquo;. Et si nous faisons eval(&laquo;&#x202F;(1)&#x202F;&raquo;), nous obtenons un entier que nous pouvons ajouter à notre liste.

Notre `compteur` est une structure de données spéciale très pratique. Nous savons que nous voulons que chaque valeur de notre `pgfnlist` apparaisse deux fois. Notre `compteur` nous donnera un hash (tableau clef/valeur), équivalent d'un dictionnaire Python où les clés sont les éléments qui apparaissent, et les valeurs représentent les occurences de ces éléments. Comme ceci&#x202F;:

```python
>>> l = [1,2,3,1,3]
>>> c = Counter(l)
>>> print(c)
Counter({1: 2, 3: 2, 2: 1})
```

Donc si pour une page donnée nous obtenons une liste de marqueurs de note de bas de page comme ceci `[1,2,3,1,3]`, alors le test `if 1 in c.values()` indiquera une erreur parce que nous savons que chaque élément doit apparaître **exactement deux fois**&#x202F;:

```Python
>>> l = [1,2,3,1,3]
>>> c = Counter(l)
>>> print(c.values())
[2, 1, 2]
```

Tandis que, si notre liste de marqueurs de note en bas de page pour la page est complète `[1,2,3,1,2,3]`, alors&#x202F;:

```python
>>> l = [1,2,3,1,2,3]
>>> c = Counter(l)
>>> print(c.values())
[2, 2, 2] # c.-à-d. 1 n’est pas dans c.values()
```

Comme précédemment, exécutez ce script plusieurs fois, corrigez votre fichier d’entrée manuellement lorsque vous découvrez des erreurs, jusqu’à ce que vous soyez satisfait(e) du résultat et que toutes les notes de bas de page soient présentes et correctes pour chaque page. Puis enregistrez votre fichier d’entrée corrigé avec un nouveau nom.

Notre fichier texte contient encore beaucoup d’erreurs issues du traitement OCR, mais nous l’avons maintenant parcouru et avons trouvé et corrigé tous les octets de métadonnées spécifiques que nous voulons dans notre ensemble de données ordonnées. Maintenant, nous pouvons utiliser notre fichier texte corrigé pour construire un dictionnaire Python.


# Créer le dictionnaire de données

Maintenant que nous avons suffisamment nettoyé l'OCR pour pouvoir différencier les parties constitutives de chacune des pages, nous pouvons trier les différents éléments de métadonnées, et le texte de la charte elle-même, dans leurs propres champs d’un dictionnaire Python.

Nous avons un certain nombre de choses à faire&#x202F;: numéroter correctement chaque charte, chaque folio et chaque page&#x202F;; séparer le résumé des annotations de la marge&#x202F;; et, enfin, associer les textes de note de bas de page à leur charte respective. Pour faire tout cela, il peut être commode de décomposer les tâches&#x202F;:

## Créer la structure du dictionnaire de données

Nous allons commencer par générer un dictionnaire Python dont les clés sont les numéros de charte, et dont les valeurs sont un dictionnaire imbriqué qui a des champs pour certaines des métadonnées que nous voulons stocker pour chaque charte. Le dictionnaire aura la forme suivante&#x202F;:

```python
charters = {
    .
    .
    .
    300: {
            'chid': "our charter ID",
            'chno': 300,
            'footnotes': [], # pour le moment c'est une liste vide
            'folio': "le marqueur folio de cette charte",
            'pgno': "le numéro de page correspondant dans l'édition papier",
            'text': [] # pour le moment c'est une liste vide
          },
    301: {
            'chid': "our charter ID",
            'chno': 301,
            'footnotes': [], # pour le moment c'est une liste vide
            'folio': "le marqueur folio de cette charte",
            'pgno': "le numéro de page correspondant dans l'édition papier",
            'text': [] # pour le moment c'est une liste vide
          },
    .
    .
    . etc.
}
```

Pour ce premier passage, nous allons simplement créer cette structure de base puis, dans les boucles suivantes, nous ajouterons et modifierons ce dictionnaire jusqu’à ce que nous obtenions un dictionnaire pour chaque charte, et des champs pour toutes les métadonnées de chacun des chartes. Une fois que cette boucle permet une identification des lignes qui nous intéressent (folio, page, en-têtes de charte) et crée un conteneur vide pour les notes de bas de page, l'étape suivante sera d’ajouter les lignes restantes au champ de texte, qui est une liste Python.


```python
slug = re.compile("(\[~~~~\sGScriba_)(.*)\s::::\s(\d+)\s~~~~\]")
fol = re.compile("\[fo\.\s?\d+\s?[rv]\.\s?\]")
pgbrk = re.compile("~~~~~ PAGE (\d+) ~~~~~")

fin = open("votre_fichier_source.txt", 'r')
GScriba = fin.readlines()

# nous aurons également besoin de ces variables globales initialisées avec des valeurs de départ comme nous l’avons mentionné plus haut
n = 0
this_folio  = '[fo. 1 r.]'
this_page = 1

#'charters' est également défini comme une variable globale. La boucle 'for' ci-dessous
# et dans les sections suivantes, s’appuiera dessus et modifiera ce dictionnaire
charters = dict()

for line in GScriba:
    if fol.match(line):
        # utiliser cette variable globale pour suivre le numéro de folio
        # nous allons créer le champ 'folio' en utilisant la valeur de cette variable
        this_folio = fol.match(line).group(0)
        continue # mettre à jour la variable mais ne pas faire d'opération particulière sur cette ligne.
    if slug.match(line):
        # si notre regex 'slug' correspond, nous savons que nous avons une nouvelle charte
        # donc obtenir les données des groupes de match
        m = slug.match(line)
        chid = "GScriba_" + m.group(2)
        chno = int(m.group(3))

        # puis créer un dictionnaire imbriqué vide
        charters[chno] = {}

        # et un conteneur vide pour toutes les lignes que nous n’utiliserons pas dans cette opération
        templist = [] # cela fonctionne parce que nous procédons dans l’ordre des documents : templist continue d’exister comme nous itérerons à travers chaque ligne de la charte, puis est réinitialisé à la liste vide lorsque nous commençons une nouvelle charte(slug.match(line)))
        continue # nous générons l’entrée, mais ne faisons rien avec le texte de cette ligne.
    if chno:
        # si un dictionnaire de charte a été créé,
        # alors nous pouvons maintenant le remplir avec les données de notre slug.match ci-dessus.
        d = charters[chno] # 'd' est simplement plus pratique que 'charters[chno]'
        d['footnotes'] = [] # Nous allons remplir cette liste vide dans une opération à part
        d['chid'] = chid
        d['chno'] = chno
        d['folio'] = this_folio
        d['pgno'] = this_page

        if re.match('^\(\d+\)', line):
            # cette ligne est le texte de la note de bas de page, car il a un marqueur de note de bas de page
            # par exemple "(1)" au début. Nous nous en occuperons plus tard
            continue
        if pgbrk.match(line):
            # si la ligne est un saut de page, mettre à jour la variable
            this_page = int(pgbrk.match(line).group(1))
        elif fol.search(line):
            # si le folio change dans le texte de la charte, mettre à jour la variable
            this_folio = fol.search(line).group(0)
            templist.append(line)
        else:
            # toute ligne non comptabilisée est ajoutée à notre conteneur temporaire
            templist.append(line)
        # ajouter le conteneur temporaire au dictionnaire après utilisation
        # une liste pour enlever les lignes vides.
        d['text'] = [x for x in templist if not x == '\n'] # enlève les lignes vides

```

## Ajouter les notes de la marge et le résumé de la page au dictionnaire de données
Lorsque nous avons généré le dictionnaire des dictionnaires ci-dessus, nous avons attribué des champs pour les notes de bas de page (juste une liste vide pour l’instant), un identifiant pour les chartes (charterID), un numéro de charte, le folio, et le numéro de page. Toutes les lignes restantes ont été ajoutées à une liste et attribuées au champ &laquo;&#x202F;texte&#x202F;&raquo;. Dans tous les cas, la première ligne du champ de texte de chaque charte devrait être le résumé italien comme nous nous en sommes assurés ci-dessus. Dans la PLUPART des cas, la deuxième ligne représente une sorte de notation marginale qui se termine habituellement par le caractère « ] » (que l'OCR interprète souvent mal). Nous devons trouver les cas qui ne satisfont pas à ce critère, fournir ou corriger le « ] » manquant, et dans les cas où il n’y a pas de notation marginale, j’ai ajouté la spécification &laquo;&#x202F;aucune marge&#x202F;&raquo;. Le script suivant fera un &laquo;&#x202F;print&#x202F;&raquo; du numéro de la charte et des deux premières lignes du champ de texte pour les chartes qui ne répondent pas à ces critères. Exécutez ce script sur chaque `charte` du dictionnaire des chartes, corrigez et mettez à jour votre texte en conséquence.

```python
n = 0
for ch in charters:
    txt = charters[ch]['text'] # souvenez vous que le champ texte est une liste de chaînes en Python
    try:
        line1 = txt[0]
        line2 = txt[1]
        if line2 and ']' not in line2:
            n += 1
            print(f"charter: {ch}\ntext, line 1: {line1}\ntext, line 2: {line2}")
    except:
        print(ch, "oops") # pour passer les chartes de la page manquante 214
```

> Note&#x202F;: les blocs `try: except:` sont rendus nécessaires par le fait que, dans ma sortie OCR, les données de la page 214 ont en quelque sorte été oubliées. Cela arrive souvent. Numériser ou photographier chaque page d’un livre de 600 pages est fastidieux à l’extrême. Il est très facile de sauter une page. Vous aurez inévitablement des anomalies comme celle-ci dans votre texte que vous devrez isoler et contourner. Le bloc `try: except:` de Python rend cela plus facile. Python est également très utile ici en ce sens que vous pouvez aller beaucoup plus loin dans la gestion des exceptions que d'afficher &laquo;&#x202F;oups&#x202F;&raquo; dans votre console. Vous pourriez par exemple appeler une fonction spécifique qui effectue une opération tout à fait distincte sur ces éléments anormaux.

Une fois que nous sommes sûrs que la ligne 1 et la ligne 2 dans le champ « texte » pour chaque charte du dictionnaire des `chartes` soient respectivement le résumé italien et la notation marginale, nous pouvons faire une autre itération du dictionnaire des `chartes`, supprimer ces lignes du champ de texte et créer de nouveaux champs dans la nouvelle entrée de la charte qui leurs seront dédiés.

> NOTA BENE&#x202F;: nous modifions maintenant une structure de données en mémoire plutôt que d’éditer des fichiers de texte successifs. Ce script devrait donc être **ajouté** à celui ci-dessus qui a créé le squelette de votre dictionnaire. Le premier script crée le dictionnaire des `chartes` en mémoire, tandis que celui-ci le modifie.

```python
for ch in charters:
    d = charters[ch]
    try:
        d['summary'] = d['text'].pop(0).strip()
        d['marginal'] = d['text'].pop(0).strip()
    except IndexError: # cela signalera que les chartes à la page 214 sont manquantes
        print(f"charte manquante {ch}")
```

## Attribuer les notes de bas de page à leur chartre respective puis les ajouter au dictionnaire de données
La partie la plus difficile est de faire en sorte que les notes de bas de page apparaissent au bas de la page et soient associées à leurs chartes respectives. Puisque nous analysons nécessairement notre texte ligne par ligne, nous sommes confrontés au problème d’associer une référence donnée à son texte approprié alors qu’il y a peut-être beaucoup de lignes à prendre en compte.

Pour cela, nous revenons à la même liste de lignes à partir de laquelle nous avons construit le dictionnaire. Nous nous reposons sur le fait que tous les repères figurent dans le texte de la charte, c'est-à-dire qu'aucun d’entre eux ne se trouve au début d’une ligne. De plus, chacun des textes de note de bas de page se trouve sur une ligne distincte commençant par &laquo;&#x202F;(1)&#x202F;&raquo;, etc. Nous concevons des regex qui peuvent faire la distinction entre les deux et construisons un conteneur pour les retenir au fur et à mesure que nous les itérons sur les lignes. Comme nous itérons sur les lignes du fichier texte, nous trouvons et attribuons des marqueurs et des textes à notre conteneur temporaire et, ensuite, chaque fois que nous atteignons un saut de page, nous les assignons à leurs champs appropriés dans nos `chartes` de dictionnaire Python existantes et réinitialisons notre conteneur temporaire au `dictionnaire` vide.

Notez comment nous construisons ce conteneur temporaire. `fndict` commence comme un dictionnaire vide. Au fur et à mesure que nous parcourons les lignes de notre texte d’entrée, si nous trouvons des marqueurs de note dans la ligne, nous créons une entrée dans `fndict` dont la clé est le numéro de note de bas de page et dont la valeur est un autre dictionnaire. Dans ce dictionnaire, nous inscrivons l’identité de la charte à laquelle appartient la note de bas de page et nous créons un champ vide pour le texte de cette dernière. Lorsque nous trouvons les textes de note (`ntexts`) au bas de la page, nous recherchons le numéro de note de bas de page dans notre conteneur `fndict` et écrivons le texte de la ligne au champ vide correspondant. Donc, à la fin de la page, nous avons un dictionnaire de notes qui ressemble à ceci&#x202F;:

```python
{1: {'chid': 158, 'fntext': 'Nel ms. de due volte e ripa cancellato.'},
 2: {'chid': 158, 'fntext': 'Sic nel ms.'},
 3: {'chid': 159, 'fntext': 'genero cancellato nel ms.'}}
```

Nous avons maintenant toute l’information nécessaire pour attribuer les notes de bas de page à la liste vide de &laquo;&#x202F;notes de bas de page&#x202F;&raquo; dans le dictionnaire des `chartes`&#x202F;: le numéro de la note de bas de page (la clé), la charte à laquelle elle appartient (`chid`) et le texte de la note de bas de page (`fntext`).

C’est une façon de faire habituelle dans la programmation et très utile&#x202F;: dans un processus itératif quelconque, vous utilisez un accumulateur (notre `fndict`) pour recueillir des octets de données, puis lorsque lorsque la sentinelle que vous avez programmée rencontre une condition spécifiée (le changement de page) elle fait quelque chose avec les données.


```python
fin = open("your_current_source_file.txt", 'r')
GScriba = fin.readlines()

# dans la variable notemark, notez l’expression 'lookbehind' '?<!' pour s'assurer que
# le marqueur '(1)' ne commence pas la chaîne
notemark = re.compile(r"\(\d+\)(?<!^\(\d+\))")
notetext = re.compile(r"^\(\d+\)")
this_charter = 1
pg = re.compile("~~~~~ PAGE \d+ ~~~~~")
pgno = 1
fndict = {}

for line in GScriba:
    nmarkers = notemark.findall(line)
    ntexts = notetext.findall(line)
    if pg.match(line):
        # C’est notre 'sentinelle'. Nous sommes arrivés à la fin d’une page,
        # Nous enregistrons donc nos données de note de bas de page accumulées dans le dictionnaire 'charters'.
        for fn in fndict:
            chid = fndict[fn]['chid']
            fntext = fndict[fn]['fntext']
            charters[int(chid)]['footnotes'].append((fn, fntext))
        pgno += 1
        fndict = {}  # puis réinitialisez notre conteneur temporaire
    if slug.match(line): # c’est le début d’une charte, il faut donc actualiser la variable
        this_charter = int(slug.match(line).group(3))
    if nmarkers:
        for marker in [eval(x) for x in nmarkers]:
            # créer une entrée avec l’identifiant de la charte et un champ de texte vide
            fndict[marker] = {'chid':this_charter, 'fntext': ''}
    if ntexts:
        for text in [eval(x) for x in ntexts]:
            try:
                # remplir le champ vide approprié.
                fndict[text]['fntext'] = re.sub('\(\d+\)', '', line).strip()
            except KeyError:
                print("printer's error? ", "pgno:", pgno, line)
```

Notez que les blocs `try: except:` viennent de nouveau à la rescousse. La boucle ci-dessus a cassé parce que, dans 3 cas, il est apparu qu’il existait des notes en bas de page pour lesquelles il n’y avait pas de marqueurs dans le texte. Il s’agissait d’un oubli éditorial dans l’édition publiée et non d’une erreur de l'OCR. Le résultat est que, quand j’ai essayé de corriger l’entrée inexistante dans `fndict`, j’ai eu une `KeyError`. Ma clause `except` m’a permis de trouver et d’examiner l’erreur, de déterminer que cette dernière était déjà dans l’original et que rien de ce que je pouvais faire n'y changerait quoi que ce soit, de sorte que lors de la génération de la version finale des `chartes`, j’aie remplacé la commande `print` par la commande `pass`. Les textes rédigés par les humains contiennent des erreurs&#x202F;; on ne peut pas les contourner. `try: except :` existent pour composer avec cette réalité.

> NOTA BENE&#x202F;: encore une fois, gardez à l’esprit que nous modifions une structure de données en mémoire plutôt que d’éditer des fichiers de texte successifs. Cette boucle devrait donc être **ajoutée** à votre script **sous** le résumé et la boucle qui traite les marges, qui se trouve **sous** la boucle qui a créé le squelette de votre dictionnaire.

## Convertir les éléments de type date et les ajouter au dictionnaire de données
Les dates sont difficiles à traiter. Les étudiant(e)s en histoire qui travaillent sur l’histoire britanniques s’accrochent ainsi à [Cheyney](https://www.worldcat.org/title/handbook-of-dates-for-students-of-british-history/oclc/41238508) comme à une bouée sur un océan agité. Et, compte tenu de la façon progressive par laquelle le calendrier grégorien a été adopté, et des nombreuses variations locales, une juste appréciation de la date pour les ressources médiévales nécessitera toujours des connaissances particulières. Néanmoins, ici aussi Python peut être d’une certaine utilité.

Notre ligne de résumé en italien contient invariablement une date tirée du texte, commodément séparée du reste de la ligne par des parenthèses. Nous pouvons donc les analyser et créer des objets de `date` en Python. Ensuite, si nous le voulons, nous pouvons faire un simple calcul à partir du calendrier.

Premièrement, nous devons trouver et corriger toutes les dates de la même façon que nous l’avons fait pour les autres éléments de métadonnées. Vous devez donc concevoir un script de diagnostic qui itérera sur votre dictionnaire de `chartes`, signaler l’emplacement des erreurs dans votre texte puis les corriger manuellement. Quelque chose comme ça&#x202F;:

```python
summary_date = re.compile('\((\d{1,2})?(.*?)(\d{1,4})?\)') # nous voulons tous les attraper, mais certains n’ont ni jour ni mois, d’où le quantificateur optionnel : `?`

# et nous voulons que Python parle italien :
ital2int = {'gennaio': 1, 'febbraio': 2, 'marzo': 3, 'aprile': 4, 'maggio': 5, 'giugno': 6, 'luglio': 7, 'agosto': 8, 'settembre': 9, 'ottobre': 10, 'novembre': 11, 'dicembre': 12}

import sys
for ch in charters:
    try:
        d = charters[ch]
        i = summary_date.finditer(d['summary'])
        dt = list(i)[-1] # toujours la dernière expression entre parenthèses, au cas où il y en aurait plus d’une.
        if dt.group(2).strip() not in ital2int.keys():
            print(f"chno. {d['chno']} fix the month {dt.group(2)}")
    except:
        print(d['chno'], "The usual suspects ", sys.exc_info()[:2])
```
> Note&#x202F;: lorsque vous utilisez les blocs `try/except`, vous devez généralement attraper des erreurs **spécifiques** dans la clause except, comme `ValueError` et autres ; cependant, dans les scripts ad hoc comme ceci, utiliser `sys.exc_info` est un moyen rapide d’obtenir des informations sur toute exception qui peut être soulevée. (Le module [sys](https://pymotw.com/2/sys/index.html#module-sys) est plein de ces trucs, utile pour le débogage).

Une fois que vous vous êtes assuré(e) que toutes les expressions de date entre parenthèses sont présentes, correctes et conformes à votre expression régulière, vous pouvez les extraire et les ajouter à votre structure de données sous forme de dates, plutôt que de simples chaînes de caractères. Pour cela, vous pouvez utiliser le module `datetime`.

Ce module, qui fait partie de la bibliothèque standard, est un sujet vaste et devrait faire l’objet de son propre tutoriel, compte tenu de l’importance des dates pour les historien(ne)s. Comme avec beaucoup d’autres modules Python, une bonne introduction est [Pymotw](https://pymotw.com/3/datetime/index.html) de Doug Hellmann (module de la semaine&#x202F;!). Une bibliothèque d’extension encore plus complète est [mxDateTime](https://www.egenix.com/products/python/mxBase/mxDateTime/). Il suffit de dire ici que le module `datetime.date` attend des paramètres comme ceci&#x202F;:

```python
>>> from datetime import date
>>> dt = date(1160, 12, 25)
>>> dt.isoformat()
'1160-12-25'
```

Voici donc notre boucle pour analyser les dates à la fin des lignes de résumé en italien et les stocker dans notre dictionnaire de chartes (en nous souvenant que nous voulons modifier la structure de données de nos chartes créées précédemment)&#x202F;:

```python
summary_date = re.compile('\((\d{1,2})?(.*?)(\d{1,4})?\)')
from datetime import date
for ch in charters:
    c = charters[ch]
    i = summary_date.finditer(c['summary'])
    for m in i:
        # souvenez-vous: 'i' est un itérateur donc même s’il y a plus d’une
        # expression entre parenthèses dans c['summary'], la clause try 
        # réussira sur la dernière, ou échouera sur chacune d'entre elles
        try:
            yr = int(m.group(3))
            mo = ital2int[m.group(2).strip()]
            day = int(m.group(1))
            c['date'] = date(yr, mo, day)
        except:
            c['date'] = "date won't parse, see summary line"
```

Sur 803 chartes, 29 ne seraient pas correctement analysées, principalement parce que la date inclut seulement mois et année. Vous pouvez stocker ces chaînes, mais vous avez deux types de données qui correspondent à des dates. Ou vous pouvez fournir un 01 comme jour par défaut et ainsi stocker un objet date Python, mais <span style="font-variant:small-caps;">1</span><sup>er</sup> janvier 1160 n’est pas la même chose que janvier 1160 et donc déforme vos métadonnées. Ou vous pouvez simplement faire comme moi et vous référer au texte source pertinent&#x202F;: la ligne de résumé en italien dans l’édition imprimée.

Une fois que vous avez des objets date, vous pouvez faire le calcul de la date. Supposons que nous voulions trouver toutes les chartes de moins de 3 semaines avant ou après Noël 1160.

```python
# nous importons ici l'intégralité du module et utilisons la notation datetime.date() etc.
import datetime

# un timedelta correspond à une certaine une durée dans le temps
week = datetime.timedelta(weeks=1)

for ch in charters:
    try:
        dt = charters[ch]['date']
        christmas = datetime.date(1160,12,25)
        if abs(dt - christmas) < week * 3:
            print(f"chno: {charters[ch]['chno']}, date: {dt}")
    except:
        pass # évite cet item dans le code produit
```

Ce qui nous donnera le résultat suivant&#x202F;:

```Python
chno: 790, date: 1160-12-14
chno: 791, date: 1160-12-15
chno: 792, date: 1161-01-01
chno: 793, date: 1161-01-04
chno: 794, date: 1161-01-05
chno: 795, date: 1161-01-05
chno: 796, date: 1161-01-10
chno: 797, date: 1161-01-10
chno: 798, date: 1161-01-06
```

Sympa, n'est-ce pas&#x202F;?

# Notre structure de données finale

Maintenant, nous avons suffisamment corrigé notre texte pour différencier les octets de métadonnées que nous voulons capturer, et nous avons aussi créé une structure de données en mémoire, notre dictionnaire de `chartes`, en faisant 4 itérations, chacune prolongeant et modifiant le dictionnaire en mémoire.

1. Créer le squelette
2. Séparer le `résumé` et les lignes `de marge` et leur attribuer des champs dans le dictionnaire
3. Recueillir et attribuer des notes de bas de page à leurs chartes respectives
4. Analyser les dates dans le champ résumé et les ajouter à leur charte respective

Imprimez en console notre dictionnaire en utilisant `pprint(charters)` et vous verrez quelque chose comme ceci&#x202F;:

```python
{
.
.
.
 52: {'chid': 'GScriba_LII',
      'chno': 52,
      'date': datetime.date(1156, 3, 27),
      'folio': '[fo. 6 r.]',
      'footnotes': [(1, 'Cancellato: m.')],
      'marginal': 'no marginal]',
      'pgno': 29,
      'summary': 'I consoli di Genova riconoscono con sentenza il diritto di Romano di Casella di pagarsi sui beni di Gerardo Confector per un credito che aveva verso il medesimo (27 marzo 1156).',
      'text': ['    In pontili capituli consules E. Aurie, W. Buronus, Ogerius Ventus laudaverunt quod Romanus de Casella haberet in bonis Gerardi Confectoris s. .xxvi. denariorum et possit eos accipere sine contradicione eius et omnium pro eo. Hoc ideo quia, cum; Romanus ante ipsos inde conquereretur, ipso Gerardo debitum non negante, sed quod de usura esset obiiciendo, iuravit nominatus Romanus quod capitalis erat (1) et non de usura, unde ut supra laudaverunt , .MCLVI., sexto kalendas aprilis, indicione tercia.\n']},
 53: {'chid': 'GScriba_LIII',
      'chno': 53,
      'date': datetime.date(1156, 3, 27),
      'folio': '[fo. 6 r.]',
      'footnotes': [],
      'marginal': 'Belmusti]',
      'pgno': 29,
      'summary': "Maestro Arnaldo e Giordan nipote del fu Giovanni di Piacenza si obbligano di pagare una somma nell'ottava della prossima Pasqua, per merce ricevuta (27 marzo 1156).",
      'text': ['  Testes Conradus Porcellus, Albericus, Vassallus Gambalixa, Petrus Artodi. Nos Arnaldus magister et Iordan nepos quondam Iohannis Placentie accepimus a te Belmusto tantum bracile unde promittimus dare tibi vel tuo certo misso lb. .xLIII. denariorum usque octavam proximi pasce, quod si non fecerimus penam dupli tibi stipulanti promittimus, bona pignori, possis unumquemque convenire de toto. Actum prope campanile Sancti Laurentii, millesimo centesimo .Lv., sexto kalendas aprilis, indictione tercia.\n']},
.
.
. etc.
}
```

Imprimer en console votre dictionnaire Python comme une chaîne littérale peut être une bonne idée. Pour un texte de cette taille, le fichier résultant est parfaitement gérable, peut être envoyé et lu dans un programme de réponse en Python très simplement en utilisant `eval()` ou collé directement dans un fichier de module Python. D’autre part, si vous voulez un moyen encore plus fiable le de sérialiser dans un contexte exclusivement Python, regardez dans [Pickle](https://docs.python.org/3.7/library/pickle.html). Si vous avez besoin de le déplacer vers un autre contexte, Javascript par exemple, ou des triplestores `RDF`, le module [json](https://docs.python.org/3.7/library/json.html#module-json) de Python fera très bien l'affaire. Si jamais vous devez obtenir une sortie XML, je suis vraiment désolé pour vous, mais le module Python [lxml](https://lxml.de/) pourra peut-être un peu atténuer vos souffrances.

## Du désordre à l'ordre, hip hip hip...
Maintenant que nous avons une structure de données ordonnée, nous pouvons faire beaucoup de choses avec elle. Un exemple très simple&#x202F;: ajoutons un code qui affiche des `chartes` comme HTML pour l’affichage sur un site web&#x202F;:

```python
fout = open("your_page.html", 'w') # créer un fichier texte dans lequel on pourra écrire en HTML

# écrire dans le fichier votre en-tête HTML avec quelques déclarations de formatage CSS
fout.write("""
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">

<html>
<head>
  <title>Giovanni Scriba Vol. I</title>
  <style>
    h1 {text-align: center; color: #800; font-size: 16pt; margin-bottom: 0px; margin-top: 16px;}
    ul {list-style-type: none;}
    .sep {color: #800; text-align: center}
    .charter {width: 650px; margin-left: auto; margin-right: auto; margin-top: 60px; border-top: double #800;}
    .folio {color: #777;}
    .summary {color: #777; margin: 12px 0px 12px 12px;}
    .marginal {color: red}
    .charter-text {margin-left: 16px}
    .footnotes
    .page-number {font-size: 60%}
  </style></head>

<body>
""")

# une boucle qui va écrire un bloc de code html pour chacune des chartes de notre dictionnaire :
for x in charters:

    # utiliser une copie de vos fichiers afin que les chartes[x] ne soient pas modifiées à cette fin précise
    d = charters[x].copy()

    try:
        if d['footnotes']:
            # rappelez-vous, c’est une liste de tuples. Ainsi, vous pouvez les soumettre directement
            # à l’opérateur d’interpolation de chaîne de la liste.
            fnlist = ["<li>(%s) %s</li>" % t for t in d['footnotes']]
            d['footnotes'] = "<ul>" + ''.join(fnlist) + "</ul>"
        else:
            d['footnotes'] = ""

        d['text'] = ' '.join(d['text']) # d['text'] est une liste de chaînes de caractères

        blob = """
            <div>
                <div class="charter">
                    <h1>%(chid)s</h1>
                    <div class="folio">%(folio)s (pg. %(pgno)d)</div>
                    <div class="summary">%(summary)s</div>
                    <div class="marginal">%(marginal)s</div>
                    <div class="text">%(text)s</div>
                    <div class="footnotes">%(footnotes)s</div>
                </div>
            </div>
            """

        fout.write(blob % d)

        # "string % dictionary" est une astuce pour le template html
        # qui utilise la syntaxe d’interpolation de chaîne de Python
        # voir: http://www.diveintopython.net/html_processing/dictionary_based_string_formatting.html

        fout.write("\n\n")
    except:
        # insérer des entrées indiquant l’absence de chartes sur la page manquante 214
        erratum = """
            <div>
                <div class="charter">
                    <h1>Charter no. %d is missing because the scan for Pg. 214 was ommited</h1>
                </div>
            </div>
            """  % d['chno']

        fout.write(erratum)

fout.write("""</body></html>""")
```

Ouvrez le fichier résultant avec un navigateur web et vous obtenez une édition numérique parfaitement formatée.

{% include figure.html filename="gs_gscriba207.png" caption="Exemple de charte formatée en HTML" %}

Être en mesure d'obtenir cela avec votre sortie OCR en grande partie non corrigée n’est pas un avantage anecdotique. Si vous tenez à émettre une édition électronique propre et sans erreur, vous devez faire un certain travail de correction. Avoir un texte source formaté pour la lecture est crucial&#x202F;; de plus, si votre correcteur peut changer la police, l’espacement, la couleur, la mise en page, et ainsi de suite à volonté, vous pouvez augmenter considérablement sa précision et sa productivité. Avec cet exemple dans un navigateur web moderne, peaufiner ces paramètres avec quelques déclarations CSS simples est facile. 

Ainsi, notre problème de départ, le nettoyage OCR, est maintenant beaucoup plus gérable parce que nous pouvons cibler des expressions régulières pour les types spécifiques de métadonnées que nous avons&#x202F;: erreurs dans le résumé en italien ou dans le texte latin&#x202F;? Ou nous pourrions concevoir des routines de recherche et de remplacement uniquement pour des chartes spécifiques ou des groupes de chartes.

Au-delà de cela, il y a beaucoup de choses que vous pouvez faire avec un ensemble de données ordonnnées, y compris l'alimenter grâce à un outil de balisage comme [le &laquo;&#x202F;brat&#x202F;&raquo;](http://brat.nlplab.org/) dont nous nous sommes servis pour le projet ChartEx. Des spécialistes peuvent alors commencer à ajouter des couches de balisage sémantique, même si vous ne faites plus de correction d’erreur OCR. En outre, avec un ensemble de données ordonnnées, nous pouvons obtenir toutes sortes de sorties&#x202F;: TEI (Text Encoding Initiative) ou EAD (Encoded Archival Description). Ou encore vous pouvez lire votre ensemble de données directement dans une base de données relationnelle ou un répertoire de stockage qui associe une clé et une valeur. Toutes ces choses sont tout bonnement impossibles, si vous travaillez seulement avec un simple fichier texte.

Les morceaux de code ci-dessus ne sont en aucun cas une solution clé en main pour nettoyer une sortie OCR lambda. Il n'existe pas de telle baguette magique. L’approche de Google pour scanner le contenu des bibliothèques de recherche menace de nous noyer dans un océan de mauvaises données. Pire encore, elle élude un fait fondamental du savoir numérique&#x202F;: les sources numériques sont difficiles à obtenir. Des textes numériques fiables, flexibles et utiles nécessitent une rédaction soignée et une conservation pérenne. Google, Amazon, Facebook et d'autres géants du Web n’ont pas à se soucier de la qualité de leurs données, juste de leur quantité. Les historien(ne)s, par contre, doivent d’abord se soucier de l’intégrité de leurs sources.

Les vastes projets d’édition des <span style="font-variant:small-caps;">XVIII</span><sup>e</sup> et <span style="font-variant:small-caps;">XIX</span><sup>e</sup> siècles, tels que la Série Rolls, la Monumenta Germaniae Historica et beaucoup d’autres, nous ont légué un trésor de ressources matérielles à travers une énorme quantité de travail très minutieux et détaillé par des armées d’érudits dévoués et bien formés. Leur tâche était la même que la nôtre&#x202F;: transmettre fidèlement l’héritage de l’histoire de ses formes antérieures sous une forme plus moderne, le rendant ainsi plus largement accessible. Nous ne pouvons pas faire moins. Nous avons des outils puissants à notre disposition, mais même si cela peut changer l’ampleur de la tâche, cela ne change pas pour autant sa nature.
