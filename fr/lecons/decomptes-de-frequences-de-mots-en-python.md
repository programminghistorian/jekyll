---
title: "Décomptes d'occurrences de mots en Python"
slug: decomptes-occurrences-de-mots-en-python
original: counting-frequencies
layout: lesson
collection: lessons
date: 2012-07-17
translation_date: 2023-03-08
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Frederik Elwert
editors:
- Miriam Posner
translator:
- François Dominic Laramée
translation-editor:
- Célian Ringwald
translation-reviewer:
- Alice Brenon
- Anaïs Chambat
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/526
difficulty: 2
activity: analyzing
topics: [python]
abstract: "Compter les occurrences de mots spécifiques dans une liste peut constituer une source de données utiles. Cette leçon vous apprendra comment compter ces occurrences facilement en Python."
avatar_alt: Un homme assis sur une bûche entouré d'oiseaux
doi: 10.46430/phfr0025
---

{% include toc.html %}


## Objectifs de la leçon

Supposons que vous ayez en votre possession un texte suffisamment propre pour pouvoir commencer à analyser son contenu. Le décompte des mots spécifiques dans la liste des mots qui composent le texte pourrait constituer une source de données pertinentes. Python dispose d’un mécanisme qui permet de réaliser cette opération facilement. Ce mécanisme requiert cependant l’utilisation d’un nouveau type de variable&nbsp;: le dictionnaire. Mais avant de commencer à travailler avec les dictionnaires, nous allons décrire les étapes nécessaires au calcul des occurrences.

### Fichier requis pour cette leçon

-   `obo.py`

Si vous ne disposez pas déjà d'une copie de ce fichier, vous pouvez télécharger une archive ([`.zip`](/assets/python-lessons4.zip)) contenant tout le code développé dans le cadre des leçons précédentes de cette série.

## Décompte d'occurrences

Nous voulons compter le nombre d'occurrences de chacun des mots qui apparaissent au moins une fois dans une liste. Pour parcourir la liste, nous utiliserons une boucle `for`. Sauvegardez et exécutez le programme suivant. (Rappel&nbsp;: `+=` indique au programme d'ajouter quelque chose à la fin d'une variable qui existe déjà.)

``` python
# compter-items-dans-une-liste.py

message = 'it was the best of times it was the worst of times '
message += 'it was the age of wisdom it was the age of foolishness'

liste_mots = message.split()

frequences_mots = []
for mot in liste_mots:
    frequences_mots.append(liste_mots.count(mot))

print("Le message\n" + message +"\n")
print("La liste de mots\n" + str(liste_mots) + "\n")
print("Fréquences\n" + str(frequences_mots) + "\n")
print("Paires (mot, fréquence)\n" + str(list(zip(liste_mots, frequences_mots))))
```

Le programme commence par diviser une chaîne de caractères en liste de mots, comme nous l'avons déjà fait dans d'autres leçons de cette série. Il crée ensuite une liste (vide au début) nommée *frequences_mots*. Nous examinons chacun des mots dans *liste_mots* et nous comptons le nombre d'apparitions de ce mot dans la liste. 

Nous ajoutons ensuite chacun de ces décomptes à notre liste *frequences_mots*. À l'aide de l'opération `zip`, nous pouvons associer le premier mot de la *liste_mots* avec le premier nombre dans *frequences_mots*, le second mot avec le second nombre, etc. 

Nous obtenons ainsi une liste de paires formées d'un mot et du nombre de ses occurrences dans la liste. Note&#x202F;: la fonction `str` convertit n'importe quel objet Python en une chaîne de caractères pour qu'il puisse être affiché à l'écran.

En exécutant le programme, vous devriez obtenir quelque chose qui ressemble à ceci&nbsp;:

``` python
Le message
it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness

La liste de mots
['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was',
'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age',
'of', 'wisdom', 'it', 'was', 'the', 'age', 'of',
'foolishness']

Fréquences
[4, 4, 4, 1, 4, 2, 4, 4, 4, 1, 4, 2, 4, 4, 4, 2, 4, 1, 4,
4, 4, 2, 4, 1]

Paires (mot, fréquence)
[('it', 4), ('was', 4), ('the', 4), ('best', 1), ('of', 4),
('times', 2), ('it', 4), ('was', 4), ('the', 4),
('worst', 1), ('of', 4), ('times', 2), ('it', 4),
('was', 4), ('the', 4), ('age', 2), ('of', 4),
('wisdom', 1), ('it', 4), ('was', 4), ('the', 4),
('age', 2), ('of', 4), ('foolishness', 1)]
```

Prenez le temps de bien étudier le code ci-dessus jusqu'à ce que vous le maîtrisiez avant de poursuivre. Vous ne le regretterez pas.

Python inclut aussi un mécanisme très pratique appelé la [compréhension de liste](https://perma.cc/42NM-93XZ), que l'on peut utiliser pour accomplir les mêmes tâches que la boucle `for` plus efficacement&nbsp;:

``` python
## compter-items-dans-une-liste-2.py

message = 'it was the best of times it was the worst of times '
message += 'it was the age of wisdom it was the age of foolishness'

liste_mots = message.split()

frequences_mots = [liste_mots.count(mot) for mot in liste_mots]  # Une compréhension de liste
for mot in liste_mots:
    frequences_mots.append(liste_mots.count(mot))

print("Le message\n" + message +"\n")
print("La liste de mots\n" + str(liste_mots) + "\n")
print("Fréquences\n" + str(frequences_mots) + "\n")
print("Paires (mot, fréquence)\n" + str(list(zip(liste_mots, frequences_mots))))
```

Si vous examinez bien cette compréhension de liste, vous constaterez qu'elle accomplit exactement la même chose que la boucle `for` de l'exemple précédent, mais de façon plus concise. Les deux approches fonctionnent aussi bien l'une que l'autre&nbsp;; utilisez celle qui vous convient le mieux. En règle générale, il est préférable d'utiliser du code que l'on comprend bien, quitte à sacrifier un peu de vitesse d'exécution au besoin.

Nous disposons maintenant d'une liste de paires dans laquelle chaque paire contient un mot et son nombre d'occurrences. Cette liste est plutôt redondante. Si le mot &laquo;&#x202F;le&#x202F;&raquo; apparaissait 500 fois dans notre texte d'origine, la liste contiendrait 500 copies de la paire (&laquo;&#x202F;le&#x202F;&raquo;, 500). La liste est aussi classée dans l'ordre où les mots apparaissent dans le texte et non pas en ordre décroissant de fréquences. Nous pouvons régler les deux problèmes en convertissant la liste en dictionnaire et en affichant le dictionnaire en ordre décroissant d'occurrences, du mot qui apparait le plus fréquemment à celui qui apparaît le moins fréquemment.

## Les dictionnaires en Python

Les chaînes de caractères et les listes sont des structures de données séquentielles. Cela signifie que l'on peut accéder à leurs contenus à l'aide d'un *indice*, c'est-à-dire un nombre entier supérieur ou égal à zéro. Si vous disposez d'une liste qui contient des chaînes de caractères, vous pouvez utiliser une paire d'indices pour accéder à une chaîne spécifique dans la liste, puis à un caractère particulier dans cette chaîne. Étudiez les exemples ci-dessous:

``` python

phrase = 'bonjour le monde'
print(phrase[0])
-> b

print(phrase[1])
-> o

mots = ['bonjour', 'le', 'monde']
print(mots[0])
-> bonjour

print(mots[2])
-> monde

print(mots[0][1])
-> o

print(mots[1][0])
-> l
```

Nous allons maintenant enregistrer nos décomptes d'occurrences dans un nouveau type d'objet Python&#x202F;: le dictionnaire. Un dictionnaire est une collection *non séquentielle* d'objets. Cela signifie qu'il est impossible d'utiliser un indice pour accéder aux éléments contenus dans le dictionnaire. On peut cependant y accéder par la clé à laquelle ils sont associés dans ce dictionnaire (d'où le nom &laquo;&#x202F;dictionnaire&#x202F;&raquo;). Voici un exemple&nbsp;:

``` python

dictionnaire = {'monde': 1, 'bonjour': 0}
print(dictionnaire['bonjour'])
-> 0

print(dictionnaire['monde'])
-> 1

print(dictionnaire.keys())
dict_keys(['monde', 'bonjour'])
```

Le fonctionnement des dictionnaires peut être déroutant pour les novices, mais il ressemble à celui des dictionnaires linguistiques. Si vous avez oublié la différence entre la &laquo;&#x202F;bijection&#x202F;&raquo; et la &laquo;&#x202F;surjection&#x202F;&raquo; en mathématiques, par exemple, vous pouvez consulter les définitions des deux termes dans votre Larousse. Le même principe s'applique lorsque vous entrez la commande `print(dictionnaire['monde'])` sauf qu'au lieu d'accéder à la définition d'un mot vous obtenez plutôt la valeur associée au mot-clé &laquo;&#x202F;monde&#x202F;&raquo; dans le dictionnaire, telle que vous l'avez définie vous-même en créant le dictionnaire. Dans le cas présent, cette valeur est &laquo;&#x202F;1&#x202F;&raquo;.

Notez que nous utilisons des accolades pour définir un dictionnaire, mais des crochets pour accéder aux objets contenus dans celui-ci. La méthode `keys` (qui signifie &laquo;&#x202F;clés&#x202F;&raquo;) renvoye une liste de toutes les clés qui ont été définies dans le dictionnaire.

## Paires mot-occurrences

Nous voulons maintenant construire une fonction capable de traduire une liste de mots en un dictionnaire de paires (mot, *occurrences*). La seule nouvelle commande dont nous aurons besoin est `dict`, qui construit un dictionnaire à partir d'une liste de paires. Copiez le code ci-dessous et ajoutez-le au module `obo.py`.

<div class="alert alert-info">
Note du traducteur&nbsp;: le nom de la fonction qui apparaît dans le bloc ci-dessous n'a pas été traduit de l'anglais, pas plus que ceux des autres fonctions à venir, afin de maintenir la compatibilité avec les différentes versions du fichier obo.py utilisées dans le cadre de cette série de leçons.
</div>

``` python
# À partir d'une liste de mots, construire un dictionnaire
# de paires (mot, fréquence)

def wordListToFreqDict(liste_mots):
    freqs_mots = [liste_mots.count(mot) for mot in liste_mots]
    return dict(list(zip(liste_mots,freqs_mots)))
```

Il nous faut aussi une fonction capable de trier un dictionnaire de paires (mot, occurrences) en ordre décroissant d'occurrences. Copiez aussi le segment de code suivant dans le module `obo.py`:

``` python
# Trier un dictionnaire de paires (mot, fréquence)
# en ordre décroissant de fréquences

def sortFreqDict(freqs_mots):
    aux = [(freqs_mots[mot], mot) for mot in freqs_mots]
    aux.sort()
    aux.reverse()
    return aux
```

Nous pouvons maintenant écrire un programme qui calcule les décomptes d'occurrences de chacun des mots qui apparaissent dans la page web qui se trouve à un URL spécifique, en ordre décroissant d'occurrences. Copiez le programme suivant dans votre éditeur de texte, sauvegardez-le et exécutez-le. Étudiez minutieusement le code et les résultats avant de poursuivre.

``` python
#html-vers-freqs.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

reponse_url = urllib.request.urlopen(url)
html = reponse_url.read()
texte_brut = obo.stripTags(html).lower()
liste_mots = obo.stripNonAlphaNum(texte_brut)
frequences_mots = obo.wordListToFreqDict(liste_mots)
frequences_en_ordre = obo.sortFreqDict(frequences_mots)

for paire in frequences_en_ordre: print(str(paire))
```

## Élimination des mots vides

Lorsque l'on examine les résultats produits par le programme `html-vers-freqs.py` ci-dessus, on remarque que la plupart des mots les plus fréquents sont des mots qui jouent des rôles structurels dans le langage, comme &laquo;&#x202F;the&#x202F;&raquo;, &laquo;&#x202F;of&#x202F;&raquo;, &laquo;&#x202F;to&#x202F;&raquo; et &laquo;&#x202F;and&#x202F;&raquo; (&laquo;&#x202F;le/la&#x202F;&raquo;, &laquo;&#x202F;de&#x202F;&raquo;, &laquo;&#x202F;vers&#x202F;&raquo; et &laquo;&#x202F;et&#x202F;&raquo;).

``` python
(192, 'the')
(105, 'i')
(74, 'to')
(71, 'was')
(67, 'of')
(62, 'in')
(53, 'a')
(52, 'and')
(50, 'you')
(50, 'he')
(40, 'that')
(39, 'his')
(36, 'it')
```

Ces petits mots (conjonctions, articles, etc.) occupent presque toujours le sommet de la liste des mots les plus fréquents *quel que soit le texte que l'on examine*, en français comme en anglais. Ils ne nous éclaire par réellement sur les sujets évoqués lors du procès de Bowsey. En règle générale, nous chercherons plutôt à identifier les mots qui nous aideront à distinguer un texte d'un ensemble d'autres textes portant sur des sujets différents. Pour ce faire, nous allons filtrer les mots structurels les plus courants avant de produire notre liste de décomptes. Ces mots structurels omniprésents sont souvent appelés [&laquo;&#x202F;mots vides&laquo;&#x202F;](https://perma.cc/GL2H-XAHQ) par les linguistes, ou &laquo;&#x202F;stopwords&#x202F;&raquo; en anglais. Pour les besoins de cette leçon, nous utiliserons une liste de mots vides de la langue anglaise adaptée de celle publiée en ligne par des [informaticiens de Glasgow, en Écosse](https://perma.cc/RX7Z-F9YA). Copiez-collez cette liste au début du module `obo.py` que vous êtes en train de bâtir&nbsp;:

``` python
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']
```

Filtrer les mots vides qui apparaissent dans une liste ne requiert qu'une compréhension de liste supplémentaire. Ajoutez la fonction ci-dessous à `obo.py`, elle aussi&nbsp;:

``` python
# Filtrer les mots vides ('stopwords') d'une liste de mots

def removeStopwords(liste_mots, mots_vides):
    return [mot for mot in liste_mots if mot not in mots_vides]
```

## L'assemblage final

Nous avons maintenant tout ce qu'il nous faut pour calculer des décomptes d'occurrences de mots dans des pages web. Copiez le code ci-dessous dans votre éditeur de texte, sauvegardez-le dans un fichier nommé `html-vers-freqs-2.py` et exécutez-le&nbsp;:

``` python
# html-vers-freqs-2.py

import urllib.request, urllib.error, urllib.parse
import obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

reponse_url = urllib.request.urlopen(url)
html = reponse_url.read()
texte_brut = obo.stripTags(html).lower()
liste_mots = obo.stripNonAlphaNum(texte_brut)
liste_mots_filtree = obo.removeStopwords(liste_mots, obo.stopwords)
frequences_mots = obo.wordListToFreqDict(liste_mots_filtree)
frequences_en_ordre = obo.sortFreqDict(frequences_mots)

for paire in frequences_en_ordre: print(str(paire))
```

Si tout s'est bien passé, vous devriez obtenir des résultats qui ressemblent à ceci&nbsp;:

``` python
(25, 'house')
(20, 'yes')
(20, 'prisoner')
(19, 'mr')
(17, 'man')
(15, 'akerman')
(14, 'mob')
(13, 'black')
(12, 'night')
(11, 'saw')
(9, 'went')
(9, 'sworn')
(9, 'room')
(9, 'pair')
(9, 'know')
(9, 'face')
(8, 'time')
(8, 'thing')
(8, 'june')
(8, 'believe')
...
```

## Lectures suggérées

Lutz, _Learning Python_

-   Ch. 9: Tuples, Files, and Everything Else
-   Ch. 11: Assignment, Expressions, and print
-   Ch. 12: if Tests
-   Ch. 13: while and for Loops

Pilgrim, _Diving into Python_

-   Ch. 7: [Regular Expressions](https://web.archive.org/web/20180416143856/http://www.diveintopython.net/regular_expressions/index.html)

### Synchronisation du code

Afin de suivre la progression des leçons suivantes, il est important de disposer des bons fichiers et des bons programmes dans votre répertoire &laquo;&#x202F;programming-historian&#x202F;&raquo;. À la fin de chacune des leçons de la série, vous pouvez télécharger une version à jour de l'archive zip &laquo;&#x202F;programming-historian&#x202F;&raquo; pour vous assurer d'avoir le bon code en main.

-   programming-historian-5 ([synchronisation du code](/assets/python-lessons5.zip))
