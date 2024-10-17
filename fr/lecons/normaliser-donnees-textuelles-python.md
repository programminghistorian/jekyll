---
title: Normaliser des données textuelles avec Python
slug: normaliser-donnees-textuelles-python
original: normalizing-data
layout: lesson
collection: lessons
date: 2012-07-17
translation_date: 2024-09-05
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Francesca Benatti
- Frederik Elwert
editors:
- Miriam Posner
translator:
- Fantine Horvath
translation-editor:
- Matthias Gille Levenson
translation-reviewer:
- Marianne Reboul
- Andrea Escobar Castillo
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/564
difficulty: 2
activity: transforming
topics: [python]
abstract: L'objectif de cette leçon est de reprendre la liste créée dans la leçon &laquo;&nbsp;Du HTML à une liste de mots&nbsp;&raquo; et de la rendre plus simple à analyser en normalisant ses données.
avatar_alt: Grande femme trainant un homme plus petit
doi: 10.46430/phfr0033
---

{% include toc.html %}

<div class="alert alert-warning" role="alert">
Le site web du Old Bailey Online a récemment été mis à jour. Malheureusement, à cause de ces <a href="https://www.oldbaileyonline.org/about/whats-new">changements</a>, certains éléments utilisés dans cette leçon (voire tous) ne fonctionneront plus comme ils sont décrits. Les méthodologies enseignées dans cette leçon restent tout de même pertinentes, et peuvent être adaptées à un autre site. Nous essayons actuellement d'adapter la leçon au nouveau site du Old Bailey Online, mais nous ne pouvons pas encore déterminer quand la leçon sera prête. [Avril 2024]
</div>

## Objectif de la leçon

Avant d'aller plus loin, nous avons besoin de &laquo;&nbsp;normaliser&nbsp;&raquo; la liste que nous avons créée dans la leçon [Du html à une liste de mots (2)](/fr/lecons/du-html-a-une-liste-de-mots-1). La normalisation des données est une étape importante qui consiste à préparer les données pour le traitement automatique que l'on veut leur appliquer, en leur donnant une forme que nous pourrons manipuler facilement (par exemple, normaliser des données textuelles peut nécessiter de convertir tous les caractères en minuscules ou de retirer des caractères spéciaux qui ne nous intéressent pas pour la suite). Pour cela, nous allons appliquer des méthodes de traitement des chaines de caractères, ainsi que des expressions régulières de Python. Une fois normalisées, nos données pourront être analysées plus facilement.

## Fichiers nécessaires pour cette leçon

-   `html-to-list-1.py`
-   `obo.py`

Si vous n'avez pas les fichiers de la leçon précédente cités ci-dessus, vous pouvez [télécharger le fichier `python-lessons3.zip`](/assets/python-lessons3.zip) ici.

## Nettoyer notre liste

Dans la leçon [Du html à une liste de mots (2)](/fr/lecons/du-html-a-une-liste-de-mots-1), nous avons rédigé un programme Python, `html-to-list-1.py`. Ce programme télécharge le contenu d'une [page web](https://perma.cc/QN4N-9E9U), extrait le formatage et les métadonnées, puis produit une liste de &laquo;&nbsp;mots&nbsp;&raquo;, comme celle ci-dessous. En réalité, ces entités sont appelées des &laquo;&nbsp;tokens&nbsp;&raquo; (jetons), plutôt que &laquo;&nbsp;mots&nbsp;&raquo;. En effet, certains de ces éléments ne sont pas du tout des &laquo;&nbsp;mots&nbsp;&raquo; à proprement parler (par exemple, l'abréviation &laquo;&nbsp;&c.&nbsp;&raquo; pour &laquo;&nbsp;_et cetera_&nbsp;&raquo;). D'autres peuvent aussi être considérés comme des groupes de plusieurs mots. Dans la liste qui suit, la forme possessive &laquo;&nbsp;Akerman's&nbsp;&raquo; (en anglais) par exemple est parfois analysée par les linguistes comme deux mots&nbsp;: &laquo;&nbsp;Akerman&nbsp;&raquo; accompagné d'un marqueur possessif. En français, on pourrait trouver de la même façon des formes analysables comme deux mots mais récupérées comme un token unique par le programme Python (des verbes pronominaux par exemple, comme &laquo;&nbsp;s'élancer&nbsp;&raquo;).

Reprenez votre programme `html-to-list-1.py` et vérifiez qu'il renvoie bien quelque chose comme suit&nbsp;:

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

En soi, séparer ainsi le texte en mots n'est pas très utile, mais c'est une étape nécessaire. Nous pouvons maintenant utiliser le texte pour réaliser des mesures qui ne sont normalement pas faisables sans logiciels spécifiques. Nous allons commencer par calculer les fréquences des tokens et d'autres unités linguistiques, ce qui se fait fréquemment dans le cadre d'une analyse textuelle.

La liste aura besoin d'être nettoyée avant d'être utilisée pour mesurer des fréquences. À l'aide des méthodes vues dans la leçon précédente [Du html à une liste de mots (1)](/fr/lecons/du-html-a-une-liste-de-mots-1), essayons dans un premier temps de décrire notre algorithme avec des phrases en français. Ce que nous voulons, c'est savoir combien de fois les mots sémantiquement importants apparaissent dans notre texte. Les étapes à réaliser devraient donc ressembler à cela&nbsp;:

-   Convertir tous les mots en minuscules, pour que _BENJAMIN_ et
    _benjamin_ soient comptés comme un seul token
-   Retirer tout caractère qui ne ferait pas partie des caractères qui nous intéressent (les
  emojis ou les signes diacritiques (accents, cédilles) par exemple)
-   Compter, pour chaque mot, le nombre de fois où il apparait
    (son nombre d'occurrences)
-   Retirer les mots outils (stopwords), des mots à faible poids sémantique mais très courants, 
    comme _it_, _the_, _and_, etc.
    (en français, _le_, _et_, _un_, etc.)


## Convertir en minuscules

Généralement, les tokens sont convertis en minuscules pour faire des mesures de fréquences. C'est ce que nous allons faire en appliquant la méthode `lower()` à chaque token. Il s'agit d'une méthode applicable à des chaines de caractères et qui a déjà été introduite dans la leçon [Manipuler des chaines de caractères en Python](/fr/lecons/manipuler-chaines-caracteres-python). Nous allons donc devoir l'appliquer à la chaine de caractères qui est renvoyée par la fonction `stripTags(html)` du module `obo.py`, dans le programme `html-to-list1.py`. 

En effet, la fonction `stripTags()` du module `obo.py` retourne une chaine de caractère à partir des données extraites (contenues dans la variable `html`), que nous convertissons en minuscules avec la fonction `lower()`. En appliquant ainsi les deux fonctions sur une même ligne, nous gardons un code assez court tout en apportant des modifications majeures à notre programme.

Modifier `html-to-list1.py` pour y appliquer la méthode `lower()` à `obo.stripTags(html)`&nbsp;:

<div class="alert alert-warning">
Attention&nbsp;: à cause des modifications faites au site du Old Bailey Online depuis la publication de cette leçon, le lien <code>http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33</code> ne fonctionnera plus dans le code ci-dessous. Vous avez deux options pour contourner le problème&nbsp;: si vous suivez actuellement cette leçon en utilisant un autre site qui fonctionne, vous pouvez simplement remplacer le lien du Old Bailey Online avec votre propre lien correspondant&nbsp;: 
</div>

``` python
#html-to-list1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = str(response.read().decode('UTF-8'))
text = obo.stripTags(html).lower() # ajouter la méthode applicable à une chaine de caractères ici.
wordlist = text.split()

print(wordlist)
```

<div class="alert alert-warning">
Si vous préférez suivre cette leçon en continuant d'utiliser notre exemple du Old Bailey Online, il vous faudra d'abord <a href="/assets/normaliser-donnees-textuelles-python/obo-t17800628-33.html">télécharger le fichier HTML de la page en question</a>, que nous vous avons mis à disposition, puis adapter les premières lignes du code pour pointer vers le fichier sur votre propre ordinateur, comme ceci&nbsp;:
</div>

```
import obo

old_bailey_online_example = 'USER/FILE/PATH/obo-t17800628-33.html'

with open(old_bailey_online_example, "r") as input_example:
    html_as_string = input_example.read()
text = obo.stripTags(html_as_string).lower() #add the string method here.
wordlist = text.split()
print((wordlist))
```

Normalement, vous devriez obtenir la même liste de mots que précédemment, mais cette fois avec tous les caractères en minuscules.

Comme nous l'avons déjà vu, Python permet de faire beaucoup, facilement et avec peu de code&nbsp;!

À partir de là, nous pourrions parcourir un grand nombre d'autres entrées de Old Bailey Online et de nouvelles sources pour être sûrs qu'il n'y ait pas d'autres caractères spéciaux qui pourraient nous poser problème plus tard. Nous pourrions également anticiper toutes les situations où nous voudrions conserver la ponctuation (par exemple, pour distinguer des quantités monétaires, comme &laquo;&nbsp;1300$&nbsp;&raquo; ou &laquo;&nbsp;1865£&nbsp;&raquo;, des dates, ou reconnaitre la différence entre &laquo;&nbsp;1629-40&nbsp;&raquo; et &laquo;&nbsp;1629 40&nbsp;&raquo;). C'est le travail des programmeurs professionnels&nbsp;: essayer de penser à tout ce qui pourrait clocher et traiter le problème en amont.

Nous allons utiliser une autre approche. Notre objectif est de développer des techniques utilisables par un historien ou une historienne en activité durant le processus de recherche. Cela signifie que nous favoriserons presque toujours des solutions approximativement correctes mais pouvant être développées rapidement. Alors plutôt que de prendre du temps tout de suite pour créer un programme solide face à l'exceptionnel, nous allons simplement nous débarrasser de tout ce qui n'est pas une lettre, accentuée ou non, ou un chiffre arabe. La programmation est par essence un processus &laquo;&nbsp;d'affinement pas à pas&nbsp;&raquo;. On commence avec un problème et le début d'une solution, puis on affine cette solution jusqu'à obtenir quelque chose qui fonctionne au mieux.

## Expressions régulières en Python

Nous avons retiré les majuscules, il ne reste plus qu'à éliminer toute la ponctuation. Si on la laisse dans le texte, la ponctuation va perturber nos mesures de fréquences. En effet, nous voulons bien évidemment considérer _evening?_ (soir) comme _evening_ et &laquo;&nbsp;1780.&nbsp;&raquo; comme &laquo;&nbsp;1780&nbsp;&raquo;.

Il est possible d'utiliser la méthode `.replace()` sur la chaine de caractères pour en retirer tous les types de ponctuation&nbsp;:

``` python
text = text.replace('[', '')
text = text.replace(']', '')
text = text.replace(',', '')
#etc...
```

Cependant, ce n'est pas optimal. Pour continuer à créer un programme court et puissant, nous allons utiliser ce qu'on appelle des &laquo;&nbsp;expressions régulières&nbsp;&raquo;. Les expressions régulières sont disponibles dans de nombreux langages de programmation, sous différentes formes.

Les expressions régulières permettent de rechercher des patrons lexicaux (&laquo;&nbsp;patterns&nbsp;&raquo;) bien définis et qui peuvent raccourcir drastiquement votre code. Par exemple, mettons que vous vouliez trouver une lettre de l'alphabet dans une chaine de caractères. Plutôt que de créer une boucle `if`/`else` qui vérifie si chaque caractère de la chaine correspond à &laquo;&nbsp;a&nbsp;&raquo;, puis à &laquo;&nbsp;b&nbsp;&raquo;, puis à &laquo;&nbsp;c&nbsp;&raquo;, etc., vous pouvez vous servir d'une expression régulière pour voir si le caractère de la chaine est une lettre entre &laquo;&nbsp;a&nbsp;&raquo; et &laquo;&nbsp;z&nbsp;&raquo;. Vous pourriez aussi vous en servir pour chercher un chiffre, une lettre majuscule, un caractère alphanumérique, un retour chariot, ou encore une combinaison de ces différents éléments, et bien plus.

Dans Python, les expressions régulières sont disponibles dans un module. Ce dernier n'est pas chargé automatiquement, car il n'est pas nécessaire pour tous les programmes et le charger à chaque fois prendrait du temps inutilement. Il va donc falloir l'importer (`import` le module nommé `re`), comme vous aviez importé le module `obo.py`.

Comme nous ne nous intéressons qu'aux caractères alphanumériques, nous allons créer une expression régulière qui isole uniquement ces éléments, et retire tout le reste. Copiez la fonction ci-dessous et collez-la à la fin du module `obo.py`. Vous pouvez laisser les autres fonctions du module tranquilles, nous allons continuer à les utiliser.

``` python
# Prend une chaine de caractère text, la segmente en liste avec pour délimiteurs
# les caractères non-alphanumériques (en utilisant la définition
# Unicode des alphanumériques) ou suite de caractères non-alphanumériques
# qui sont ainsi supprimés 

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)
```

L'expression régulière dans ce code est le contenu de la chaine de caractères, autrement dit `\W+`. `\W` est le diminutif utilisé pour la classe des caractères non-alphanumériques. Dans une expression régulière Python, le signe plus `+` correspond à une ou plusieurs occurrences d'un caractère donné. `re.UNICODE` informe l'interpréteur que nous voulons inclure les caractères des autres langues du monde dans notre définition &laquo;&nbsp;d'alphanumériques&nbsp;&raquo;, tout comme les lettres de A à Z, de a à z et les chiffres de 0 à 9. Les expressions régulières doivent être &laquo;&nbsp;compilées&nbsp;&raquo; avant de pouvoir être utilisées. C'est ce que fait la dernière ligne de la fonction présentée plus haut. Inutile de vous embêter à comprendre la compilation pour le moment.

Après avoir peaufiné notre programme `html-to-list1.py`, il doit ressembler à cela&nbsp;:

``` python
#html-to-list1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)

print(wordlist)
```

En exécutant le programme et en regardant ce qu'il en ressort dans le panneau `Command Output`, vous verrez qu'il fait plutôt du bon travail. Ce code sépare les mots composés avec un trait d'union comme _coach-wheels_ en deux mots, et compte le possessif anglais _'s_ ou la forme _o'clock_ comme des mots distincts, en retirant l'apostrophe. Il s'agit cependant d'une approximation  satisfaisante de ce que nous voulions obtenir, et nous pouvons continuer d'avancer vers nos mesures de fréquences avant d'essayer de l'améliorer. (Si les sources sur lesquelles vous travaillez sont dans plus d'une langue, vous aurez besoin d'en apprendre plus sur le standard [Unicode](https://home.unicode.org/) et sur sa [prise en charge Python](https://web.archive.org/web/20180502053841/http://www.diveintopython.net/xml_processing/unicode.html).)

## Pour aller plus loin

Si vous souhaitez pratiquer davantage les expressions régulières, le chapitre 7 de [Dive into Python](https://web.archive.org/web/20180416143856/http://www.diveintopython.net/regular_expressions/index.html) de Mark Pilgrim peut être un bon entrainement.

### Synchronisation du code

Pour pouvoir continuer vers les leçons suivantes, il est important d'avoir les bons dossiers et les bons programmes dans votre répertoire `programming-historian`. À la fin de chaque chapitre de cette série de leçons, vous pouvez télécharger le fichier `.zip` correspondant pour être sûr.e d'avoir le bon code&nbsp;:

- [`python-lessons4.zip`](/assets/python-lessons4.zip)
