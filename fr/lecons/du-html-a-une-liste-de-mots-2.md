---
title: Du HTML à une liste de mots (partie 2)
slug: du-html-a-une-liste-de-mots-2
original: from-html-to-list-of-words-2
layout: lesson
collection: lessons
date: 2012-07-17
translation_date: 2023-11-09 
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Frederik Elwert
editors:
- Miriam Posner
translator: 
- Célian Ringwald
translation-editor:
- Émilien Schultz
translation-reviewer:
- Béatrice Mazoyer 
- Florian Barras
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/584
activity: transforming
topics: [python]
abstract: Dans cette leçon, nous allons implémenter l'algorithme découvert dans la leçon &laquo;&nbsp;Du HTML à une liste de mots, partie 1&nbsp;&raquo;, afin d'apprendre à découper une chaine de caractères en une liste de mots.
avatar_alt: Un soldat au garde-à-vous et un homme moqueur
doi: 10.46430/phfr0028
---

{% include toc.html %}
## Objectifs de la leçon 

Dans cette leçon, nous allons implémenter l’algorithme dont nous avons parlé dans [la première partie](/fr/lecons/du-html-a-une-liste-de-mots-1) de cette leçon. Nous avons jusque-là pu écrire une procédure chargeant le contenu d’une page HTML et retournant le contenu présent entre la première balise `<p>` et la dernière balise `<br/>`. 

La seconde partie de notre algorithme devra inspecter un à un chaque caractère de la chaine `pageContents`&nbsp;:   
- Si le caractère est un crochet ouvrant (`<`), nous sommes alors à l’intérieur d’une balise&nbsp;: nous ignorons donc ce caractère et nous ignorerons aussi les suivants jusqu’à ce que nous soyons à la fin de la balise&nbsp;;   
- Si le caractère est un crochet fermant (`>`) cela signifie que nous sommes toujours dans une balise mais que nous allons ressortir de celle-ci&nbsp;: nous ignorons ce caractère et inspecterons alors avec attention les suivants&nbsp;;   
- Si nous ne sommes pas dans une balise, nous ajoutons alors le caractère courant à une variable appelée `text`;

Nous découperons ensuite la chaine de caractères `text` en une liste de mots que nous manipulerons par la suite.

### Fichiers nécessaires au suivi de la leçon

-   `obo.py`
-   `trial-content.py`

Si vous n’avez pas déjà ces fichiers, vous pouvez télécharger le fichier [`python-lessons2.zip`](/assets/python-lessons2.zip) issu de la leçon précédente.

## Boucles et instructions conditionnelles en Python

La prochaine étape dans l’implémentation de l’algorithme consiste à inspecter chaque caractère de la chaine `pageContents` un à un et à tester si le caractère courant est un élément d’une balise HTML ou bien le contenu de la transcription du procès. 

Pour ce faire, nous allons découvrir quelques techniques permettant de répéter une tâche et d’évaluer si une condition est remplie.

### Les boucles

Comme de nombreux langages de programmation, Python propose plusieurs moyens de répéter l’exécution d’une séquence d’instructions. Le plus adapté à notre problématique est ici la boucle `for`, qui nous permettra de réaliser une tâche sur chaque caractère de la chaine `pageContents`. La variable `char` contiendra alors successivement chaque caractère de la chaine `pageContents` parcourue. 

Nous avons ici nommé cette variable `char`. Toutefois, cela n’a pas d’importance particulière dans le fonctionnement du programme, car nous aurions pu la nommer `trucbidule` ou bien encore `k` si nous en avions envie. Cependant certains termes ne peuvent pas être utilisés car ils sont déjà attribués à une notion spécifique du langage Python (comme par exemple `for`). Pour vérifier si cela est le cas, vous pouvez vous reposer sur la fonction de coloration syntaxique de votre éditeur de texte afin de savoir si le nom d’une variable est possible (comme ici `char`). Par ailleurs, il est préférable de donner aux variables des noms qui nous informent sur leurs contenus. Il sera ainsi plus simple de revenir sur un programme plus tard. C’est pourquoi `trucbidule` n’est pas forcément le meilleur choix de nom de variable.

``` python
for char in pageContents:
    # faire quelque chose avec le caractère courant (char)
```

### Les instructions conditionnelles

Nous avons besoin de vérifier la valeur du caractère courant pour décider quoi en faire. Pour cela, Python propose différents moyens de réaliser des &laquo;&nbsp;tests conditionnels&nbsp;&raquo;. 

Celui dont nous avons besoin est l’instruction conditionnelle `if`. Le code ci-dessous utilise l’instruction `if` pour vérifier si la chaine de caractères nommée `char` est égale à un crochet ouvrant. Comme nous l’avons déjà mentionné, l’indentation est très importante en Python. Si le code est bien indenté, Python n’exécutera le code indenté que si la condition définie est vérifiée.

Notez que la syntaxe Python privilégie l’utilisation du signe égal (&nbsp;=&nbsp;) pour réaliser des &laquo;&nbsp;affectations&nbsp;&raquo;, c’est-à-dire attribuer une valeur à une variable. Pour tester une &laquo;&nbsp;égalité&nbsp;&raquo;, il faut utiliser le double signe égal (&nbsp;==&nbsp;) (les programmeuses et programmeurs débutants ont souvent tendance à confondre ces deux utilisations)&nbsp;:

``` python
if char == '<':
    # faire quelque chose
```

Une forme plus générale de l’instruction `if` permet d’indiquer ce que nous souhaitons faire dans le cas où la condition spécifiée n’est pas réalisée&nbsp;:

``` python
if char == '<':
    # faire quelque chose
else:
    # faire quelque chose d'autre
```

Python laisse aussi la possibilité de vérifier d’autres conditions après la première instruction, et ceci en utilisant l’instruction `elif` (qui est une contraction de `else if`)&nbsp;:

``` python
if char == '<':
    # faire quelque chose
elif char == '>':
    # faire quelque chose d'autre
else:
    # faire quelque chose de complètement différent
```

## Utiliser l’algorithme pour supprimer le balisage HTML

Vous en savez maintenant suffisamment pour implémenter la seconde partie de l’algorithme qui consiste à supprimer toutes les balises HTML. Dans cette partie, nous souhaitons inspecter chaque caractère de la chaine `pageContents` un à un&nbsp;:   
- Si le caractère courant est un chevron ouvrant (`<`) cela signifie que nous entrons dans une balise, dans ce cas nous ignorons ce caractère et ignorerons les suivants&nbsp;;   
- Si le caractère courant est un chevron fermant (`>`), cela signifie que nous ressortons de la balise, nous ignorons alors seulement ce caractère et prêterons attention aux suivants&nbsp;;   
- Si nous ne sommes pas au sein d’une balise, nous ajoutons le caractère courant dans une variable nommée `text`.  

Pour réaliser cela, nous allons utiliser une boucle `for` qui nous permettra d’inspecter de manière itérative chaque caractère de la chaine. Nous utiliserons une suite d’instructions conditionnelles (`if` / `elif`) pour déterminer si le caractère courant est inclus dans une balise. Si, à l’inverse, il fait partie du contenu à extraire, nous ajouterons alors le caractère courant à la variable `text`. 

Comment garder en mémoire le fait d’être ou non à l’intérieur d’une balise&nbsp;? Nous utiliserons pour cela une variable de type &laquo;&nbsp;entier&nbsp;&raquo;, qui vaudra 1 (vrai) si nous sommes dans une balise et qui vaudra 0 (faux) si ce n’est pas le cas (dans l’exemple plus bas nous avons appelé cette variable `inside`).

### La fonction de suppression des balises 

Mettons en pratique ce que nous venons d’apprendre. La version finale de la fonction `stripTags()`, qui nous permet de réaliser notre objectif, est décrite ci-dessous. Lorsque vous remplacerez l’ancienne fonction `stripTags()` par la nouvelle dans le fichier `obo.py`, faites à nouveau bien attention à l’indentation, de manière à ce qu’elle soit identique à ce qui est indiqué ci-dessous.

Si vous avez tenté de construire la fonction vous-même, il est tout à fait normal qu’elle puisse être différente de celle que nous vous présentons ici. Il existe souvent plusieurs moyens d’arriver à la même fin, l’essentiel est pour le moment que cela réalise bien l’objectif que nous nous étions fixé.

Cependant, nous vous conseillons de vérifier que votre fonction renvoie bien le même résultat que la nôtre&nbsp;:

``` python
# obo.py
def stripTags(pageContents):
    # Type le contenu du code source de la page comme une chaine de caractère
    pageContents = str(pageContents)
    # Renvoie l'indice du premier paragraphe
    startLoc = pageContents.find("<p>")
    # Renvoie indice du dernier passage à la ligne
    endLoc = pageContents.rfind("<br/>")
    # Ne garde que le contenu entre le premier paragraphe et le dernier passage à la ligne
    pageContents = pageContents[startLoc:endLoc]
    
    # Initialisation 
    inside = 0 # variable repérant l'intérieur d'une balise
    text = '' # variable agrégeant les contenus

    # Pour chaque caractère
    for char in pageContents:
        # Teste chaque cas :
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text
```

Ce code nous fait découvrir deux nouvelles instructions&nbsp;: `continue` et `return`.

L’instruction Python `continue` est utilisée dans les boucles pour passer directement à l’itération suivante. Quand nous arrivons à un caractère inclus au sein d’une balise HTML, nous pouvons par ce moyen passer au prochain caractère sans avoir à ajouter celui-ci à la variable `text`.

Dans la [première partie](/fr/lecons/du-html-a-une-liste-de-mots-1) de cette leçon, nous avons amplement usé de la fonction `print()`. Elle permet d’afficher à l’écran le résultat d’un programme pour qu’il puisse être lu par l’utilisateur. Cependant, dans la majorité des cas, nous souhaitons simplement faire parvenir une information d’une partie d’un programme à une autre. À ce titre, quand l’exécution d’une fonction se termine, elle peut renvoyer une valeur au code qui l’a appelée via l’instruction `return`. 

Si nous souhaitons appeler la fonction `stripTags()` dans un autre programme, voici comment nous y prendre&nbsp;:

``` python
# Pour comprendre comment fonctionne l'instruction return

import obo

myText = "Ceci est un message <h1>HTML</h1>"

theResult = obo.stripTags(myText)
```

L’instruction `return` nous permet de transférer directement la valeur de sortie de la fonction `stripTags()` dans une variable appelée `theResult`, que nous pourrons réutiliser par la suite.

Dans l’exemple ci-dessus, vous remarquerez que le contenu renvoyé par la fonction `stripTags()` n’est plus égal au contenu de `myText` mais bien au contenu sans balises HTML.

Pour tester notre nouvelle fonction `stripTags()`, vous pouvez relancer `trial-content.py`. Maintenant que nous avons redéfini `stripTags()`, le programme `trial-content.py` fournit un résultat différent, plus proche de notre objectif. Avant de continuer, vérifiez que vous avez bien compris pourquoi le comportement de `trial-content.py` change lorsque l’on édite `obo.py`.

## Les listes Python 

Maintenant que nous avons la possibilité d’extraire le texte d’une page web, nous souhaitons transformer ce texte de manière à ce qu’il soit plus facile à traiter. 

Jusqu’à présent, pour stocker de l’information dans un programme Python, nous avons choisi de le faire avec le format &laquo;&nbsp;chaine de caractères&nbsp;&raquo; ([string](https://perma.cc/D4RC-6TT4)), que nous avons déjà manipulé dans une leçon précédente ([Manipuler des chaines de caractères en Python](/fr/lecons/manipuler-chaines-caracteres-python)).

Cependant, il existe d’autres formats comme les &laquo;&nbsp;entiers&nbsp;&raquo; ([integers](https://perma.cc/Y7DW-L6YA)), que nous avons utilisés dans la fonction `stripTags()` pour stocker la valeur 1 quand nous étions au sein d’une balise et 0 lorsque ce n’était pas le cas. Les entiers permettent de réaliser des opérations mathématiques, mais il n’est pas possible d’y stocker des fractions ou des nombres décimaux.

``` python
inside = 1
```

De plus, sans le savoir, à chaque fois que vous avez eu besoin de lire ou d’écrire dans un fichier, vous avez utilisé un objet spécifique permettant de manipuler des fichiers, comme `f` dans l’exemple ci-dessous&nbsp;:

``` python
f = open('helloworld.txt','w')
f.write('hello world')
f.close()
```

Un autre [type d’objets](https://perma.cc/X2M2-EWVC) proposé par Python est la &laquo;&nbsp;[liste]&nbsp;&raquo; ([list](https://perma.cc/FC9Y-JSSV), correspondant à une collection ordonnée d’objets (pouvant inclure potentiellement d’autres listes).

Convertir une chaine de caractères en liste de caractères ou de mots est assez simple. Copiez ou écrivez le programme suivant dans votre éditeur de texte pour comprendre les deux moyens de réaliser cette opération. Sauvegardez le fichier en le nommant `string-to-list.py` et exécutez-le. Comparez ensuite les deux listes obtenues dans la sortie de la commande et à la vue de ces résultats, essayez de comprendre comment fonctionne ce bout de code&nbsp;:

``` python
# string-to-list.py
# deux chaines de caractères
s1 = 'hello world'
s2 = 'howdy world'

# liste de 'caractères'
charlist = []
for char in s1:
    charlist.append(char)
print(charlist)

# liste de 'mots'
wordlist = s2.split()
print(wordlist)
```

Le premier bloc de ce code définit deux variables. La seconde partie fait intervenir une boucle `for` pour parcourir chaque caractère de la chaine `s1` puis ajoute chaque caractère à la fin de `charlist`. Le dernier bloc de code utilise l’opération `split` qui permet de découper la chaine `s2` là où se trouve un caractère invisible (espace, tabulation, retour charriot et autres caractères similaires). 

Pour le moment, nous avons simplifié un peu les choses concernant la procédure utilisée pour le découpage de la chaine en liste de mots. Modifiez la chaine `s2` utilisée dans le programme et donnez-lui la valeur &laquo;&nbsp;salut le monde!&nbsp;&raquo; puis relancez le programme. 
 
Qu’est-il arrivé au point d’exclamation&nbsp;? 
 
Si vous avez écrit &laquo;&nbsp;salut le monde!&nbsp;&raquo; sans espace avant le point d’exclamation, celui-ci se retrouvera dans le même élément de la liste que &laquo;&nbsp;monde&nbsp;&raquo;, alors que si vous avez ajouté une espace pour corriger cette erreur typographique, le point d’exclamation sera placé dans un élément différent de la liste de mots. Vérifiez si cela est bien le cas.

Notez que vous devez sauvegarder les modifications apportées au programme avant de pouvoir relancer Python.

En vous servant de vos nouvelles connaissances, ouvrez maintenant l’URL, téléchargez la page web, sauvegardez son contenu dans une chaine de caractères et, comme nous venons de le voir, découpez celle-ci en une liste de mots. Essayez d’exécuter alors le programme suivant&nbsp;:

``` python
#html-to-list1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/print.jsp?div=t17800628-33'

response = urllib.request.urlopen(url) # requête la page et récupère le code source
html = response.read().decode('UTF-8') # lit le contenu 
text = obo.stripTags(html) # utilisation de la fonction permettant la suppression des balises
wordlist = text.split() # transformation en liste de mots

print((wordlist[0:120]))

```

Le résultat obtenu devrait ressembler à la liste ci-dessous&nbsp;:

``` python
['324.', '\xc2\xa0', 'BENJAMIN', 'BOWSEY', '(a', 'blackmoor', ')', 'was',
'indicted', 'for', 'that', 'he', 'together', 'with', 'five', 'hundred',
'other', 'persons', 'and', 'more,', 'did,', 'unlawfully,', 'riotously,',
'and', 'tumultuously', 'assemble', 'on', 'the', '6th', 'of', 'June', 'to',
'the', 'disturbance', 'of', 'the', 'public', 'peace', 'and', 'did', 'begin',
'to', 'demolish', 'and', 'pull', 'down', 'the', 'dwelling', 'house', 'of',
'\xc2\xa0', 'Richard', 'Akerman', ',', 'against', 'the', 'form', 'of',
'the', 'statute,', '&amp;c.', '\xc2\xa0', 'ROSE', 'JENNINGS', ',', 'Esq.',
'sworn.', 'Had', 'you', 'any', 'occasion', 'to', 'be', 'in', 'this', 'part',
'of', 'the', 'town,', 'on', 'the', '6th', 'of', 'June', 'in', 'the',
'evening?', '-', 'I', 'dined', 'with', 'my', 'brother', 'who', 'lives',
'opposite', 'Mr.', "Akerman's", 'house.', 'They', 'attacked', 'Mr.',
"Akerman's", 'house', 'precisely', 'at', 'seven', "o'clock;", 'they',
'were', 'preceded', 'by', 'a', 'man', 'better', 'dressed', 'than', 'the',
'rest,', 'who']
```

Pour le moment, disposer d’une telle liste ne nous avance pas à grand à chose, surtout qu’un humain pourait facilement lire le texte initial. Cependant, comme nous le verrons dans les prochaines leçons, ce format est plus adapté pour automatiser le traitement de contenus textuels.


## Lectures suggérées

- Lutz, Mark. _Learning python: Powerful object-oriented programming_. O'Reilly Media, Inc., 2013.
    -   Ch. 7&nbsp;: &laquo;&nbsp;Strings&nbsp;&raquo;
    -   Ch. 8&nbsp;: &laquo;&nbsp;Lists and Dictionaries&nbsp;&raquo;
    -   Ch. 10&nbsp;: &laquo;&nbsp;Introducing Python Statements&nbsp;&raquo;
    -   Ch. 15&nbsp;: &laquo;&nbsp;Function Basics&nbsp;&raquo;

## Synchronisation du code

Pour suivre les leçons à venir, il est important que vous ayez les bons fichiers et programmes dans votre répertoire ```programming-historian```. À la fin de chaque chapitre, vous pouvez télécharger le fichier `.zip` contenant le matériel de cours afin de vous assurer d’avoir une version mise à jour du code.

- python-lessons3.zip ([zip sync](/assets/python-lessons3.zip))
