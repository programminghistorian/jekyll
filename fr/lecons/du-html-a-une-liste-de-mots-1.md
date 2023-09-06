---
title: "Du HTML à une liste de mots (partie 1)"
slug: du-html-a-une-liste-de-mots-1
original: from-html-to-list-of-words-1
layout: lesson
collection: lessons
date: 2012-07-17
translation_date: 2023-09-06
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
- Alexandre Wauthier
translation-reviewers:
- Marina Giardinetti
- Marie Flesch
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/560
activity: transforming
topics: [python]
abstract: Dans cette leçon en deux parties, nous allons utiliser les compétences acquises dans la leçon &laquo;&nbsp;Télécharger des pages web avec Python&nbsp;&raquo;, et voir comment supprimer les *balises HTML* de la page de la transcription du procès-verbal de Benjamin Bowsey en 1780 dans le but de créer un texte propre et réutilisable. Nous réaliserons cette tâche en utilisant les *opérateurs et méthodes de chaines de caractères* propres à Python, ainsi que nos compétences relatives à la *lecture attentive*. Nous introduirons ensuite les concepts de *boucles* et *d’instructions conditionnelles* afin de répéter notre processus de traitement et de tester certaines conditions nous permettant de séparer le contenu des balises HTML. Pour finir, nous convertirons les données obtenues et enregistrées sous la forme d’un texte sans balises HTML en une *liste de mots* qui pourra par la suite être triée, indexée et investie lors d’analyses statistiques.
avatar_alt: Un homme qui imite une girafe
doi: 10.46430/phfr0026
---

{% include toc.html %}

# Objectifs de la leçon 

Dans cette leçon en deux parties, nous allons utiliser les compétences acquises dans la leçon [Télécharger des pages web avec Python](/fr/lecons/telecharger-des-pages-web-avec-python), et voir comment supprimer les *balises HTML* de la page de la [transcription du procès-verbal de Benjamin Bowsey en 1780](https://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33) dans le but de créer un texte propre et réutilisable. Nous réaliserons cette tâche en utilisant les *opérateurs et méthodes de chaines de caractères* propres à Python, ainsi que nos compétences relatives à la [*lecture attentive*](https://perma.cc/V4GX-9N5R). Nous introduirons ensuite les concepts de *boucles* et *d’instructions conditionnelles* afin de répéter notre processus de traitement et de tester certaines conditions nous permettant de séparer le contenu des balises HTML. Pour finir, nous convertirons les données obtenues et enregistrées sous la forme d’un texte sans balises HTML en une *liste de mots* qui pourra par la suite être triée, indexée et investie lors d’analyses statistiques.

# Enjeux de la leçon

Pour rendre plus clair l’objectif de la séance, ouvrez le fichier `obo-t17800628-33.html` que vous avez créé lors de la leçon [Télécharger des pages web avec Python](/fr/lecons/telecharger-des-pages-web-avec-python).  [Ouvrez cette page web et téléchargez son code source](/assets/obo-t17800628-33.html) si ce n’est pas le cas (via la commande Ctrl+S sur Windows ou ⌘-S sur Mac). Inspectez ensuite le code HTML de ce document. En fonction du navigateur web que vous avez, il est possible d’accéder au code source d’une page en cliquant sur l’onglet `Tools -> Web Developer -> Page Source`. Il est aussi généralement possible d’y accéder via les commandes Ctrl+U (Windows) ou ⌘-Option-U (Mac).

En parcourant le fichier, vous remarquerez que celui-ci est composé de balises HTML mélangées avec du texte. Si vous êtes néophyte en matière de développement web, nous vous recommandons de consulter les tutoriels de la W3 School et de la Mozilla Foundation&nbsp;:
* HTML&nbsp;: [W3 School](https://www.w3schools.com/html/) / [Mozilla Fondation](https://perma.cc/9NFS-5Z3G)
* CSS&nbsp;: [W3 School](https://perma.cc/6HLV-LBKQ) / [Mozilla Fondation](https://perma.cc/BR5N-BDEH)

Ces tutoriels vous permettront de vous familiariser avec la syntaxe de ces formats et de mieux comprendre le contexte d’utilisation des balises HTML lorsque vous les rencontrerez.

## Matériel nécessaire au suivi de la leçon

- le fichier de la transcription du procès&nbsp;: [`obo-t17800628-33.html`](/assets/obo-t17800628-33.html)
- un éditeur de texte permettant de compiler du code Python. Dans la série de leçons d’introduction à Python du *Programming Historian en français*, nous utilisons Komodo Edit (cf. [la leçon d’introduction de la série](/fr/lecons/introduction-et-installation)), mais [il en existe beaucoup d’autres](https://perma.cc/X98A-KME8).



# Conception de l’algorithme

Puisque le but est de se défaire du balisage HTML, la première étape de ce tutoriel consiste donc à créer un algorithme nous permettant d’extraire seulement le texte de la transcription (sans balises HTML).

Un algorithme est un ensemble de procédures suffisamment détaillées pour être implémentées sur un ordinateur. Lors de la conception d’un algorithme, il est conseillé dans un premier temps, de poser sur le papier son fonctionnement de l’algorithme. C’est une manière d’expliciter ce que l’on souhaite faire avant de traduire cela en un code informatique. Pour construire cet algorithme, une lecture vigilante de la page et de sa structure sera notamment nécessaire afin de pouvoir envisager par la suite un moyen de capturer le contenu du compte rendu du procès.

À la lecture du code source de `obo-t17800628-33.html`, vous remarquerez que le contenu de la transcription n’est pas visible dès le début du fichier. Au lieu de cela, vous trouverez de nombreuses balises HTML relatives aux métadonnées. Le contenu qui nous intéresse n’est alors visible qu’à partir de la ligne 81&nbsp;!

```html
<p>324.
    <a class="invisible" name="t17800628-33-defend448"></a> 
    BENJAMIN BOWSEY (a blackmoor ) was indicted for that 
    he together with five hundred other persons and more,
    did, unlawfully, riotously, and tumultuously assemble 
    on the 6th of June 
[..]
```

Nous nous intéressons uniquement à la transcription du procès, et non pas aux métadonnées contenues dans les balises. Toutefois, vous remarquerez que les différentes parties de la transcription débutent après ces métadonnées. L’emplacement de ces balises est donc potentiellement un indice utile nous permettant d’isoler le texte de la transcription.

En un coup d’œil, vous remarquerez que la transcription du procès commence avec une balise HTML : `<p>`, qui marque ici le début d’un paragraphe. Il s’agit de là du premier paragraphe de notre document. Nous allons donc utiliser cette information pour identifier le début du texte de la transcription. Dans le cas présent, nous avons de la chance, car il s’avère que cette balise est un moyen fiable nous permettant de repérer le début d’une partie de la transcription (vous pouvez vérifier les autres parties du procès et vous verrez que c’est la même chose).

Le texte du procès se termine à la ligne 82 avec une autre balise HTML&nbsp;: `<br/>`, qui indique un passage à la ligne. Il s’agit ici du dernier passage à la ligne du document. Ces deux balises (la balise de début de paragraphe et le dernier saut de ligne) nous offrent un moyen d’isoler le texte que nous ciblons. Les sites web bien conçus ont la plupart du temps une syntaxe unique permettant de signaler la fin d’un contenu. En général, il suffit de bien inspecter les pages / le code HTML pour repérer ces indices.

La prochaine étape est donc de supprimer les balises HTML contenues au sein du contenu textuel. Maintenant, vous savez que les balises HTML se trouvent toujours entre deux chevrons. Il y a fort à parier que si nous supprimons tout ce qui est contenu entre chevrons, alors nous supprimerons par la même occasion tout ce qui est attribué à la syntaxe HTML afin de n’obtenir que le contenu de nos transcriptions. Notez que nous faisons ici l’hypothèse que celles-ci ne contiennent pas de symboles mathématiques, tels que &laquo;&#x202F;inférieur à&#x202F;&raquo; ou 
&laquo;&#x202F;supérieur à&#x202F;&raquo;. Si Bowsey était un mathématicien, cette hypothèse serait alors plus fragile.

Nous allons maintenant décrire la procédure de notre algorithme explicitement en français&nbsp;:

Pour isoler le contenu de la transcription&nbsp;:

- Charger le document HTML contenant la transcription.
- Chercher dans le code HTML et mémoriser l’emplacement de la première balise `<p>`.
- Chercher dans le code HTML et mémoriser l’emplacement de la dernière balise `</br>`.
- Sauvegarder dans une variable de type *chaine de caractères* nommée `pageContents` tout ce qui se situe entre la balise `<p>` et `</br>`.

Nous avons maintenant la transcription du texte, avec en plus des balises HTML. Nous allons donc&nbsp;:
- Inspecter un à un chaque caractère de la chaine `pageContents`.
- Si le caractère passé en revue est un chevron ouvrant (`<`), nous sommes donc à partir de celui au sein d’une balise HTML et nous allons ignorer les prochains caractères.
- Si le caractère passé en revue est un chevron fermant (`>`), nous ressortons d’une balise HTML. Nous ignorerons ce caractère, mais serons à partir de celui-ci attentifs aux prochains.
- Si nous ne sommes pas à l’intérieur d’une balise HTML, nous ajouterons alors le caractère courant dans une nouvelle variable&nbsp;: `text`.

Enfin&nbsp;:
- Nous découperons notre chaine de caractères (`pageContents`) en une liste de mots que nous utiliserons ensuite.

# Isoler le contenu de la transcription

La suite de ce tutoriel tirera parti des commandes Python introduites dans la leçon [Manipuler des chaines de caractères en Python](/fr/lecons/manipuler-chaines-caracteres-python), notamment dans la première partie de notre algorithme, afin de supprimer tous les caractères avant la balise `<p>` et après la balise `</br>`.

Récapitulons, notre algorithme&nbsp;:
- Chargera le texte de la transcription.
- Cherchera dans le code HTML la location de la première balise `<p>` et enregistrera sa position.
- Cherchera dans le code HTML la location de la dernière balise `</br>` et enregistrera sa position.
- Sauvegardera tout ce qui se situe après la balise `<p>` et avant la balise `</br>` dans une *chaine de caractères*&nbsp;: `pageContents`.

Pour réaliser cela, nous utiliserons les *méthodes de chaine de caractères* `find` (qui renvoie la première position dans une chaine d’un caractère donné) et `.rfind()` (qui renvoie la dernière position dans une chaine d’un caractère donné). Cela nous permettra de récupérer la sous-chaine de caractères contenant le contenu textuel compris entre les deux indices renvoyés par ces méthodes.

Pour illustrer et comprendre comment ces méthodes fonctionnent, vous pouvez tester cet exemple, qui renvoie la position du premier paragraphe et celle du dernier, à travers la recherche des balises `<p>` et`</br>`&nbsp;:

```python
text=’’’<!DOCTYPE html>
<html>
<body>

<p>Benjamin Bowsey</p>
<p>Robert Gates</p>
<p>John Northington</p>

</body>
</html>
’’’

print("Début :",text.find("<p>"))
print("Fin :",text.rfind("</br>"))
```

Au fur et à mesure de l’implémentation, nous prendrons soin de bien séparer nos fichiers de travail. Nous appelons `obo.py` (pour &laquo;&nbsp;Old Bailey Online&nbsp;&raquo;) le fichier dans lequel nous inscrivons le code que nous souhaiterons réutiliser&nbsp;; `obo.py` sera alors un module. Nous avons abordé la notion de module dans le tutoriel [Réutilisation de code et modularité](/fr/lecons/reutilisation-de-code-et-modularite) dans lequel nous avions enregistré nos fonctions dans un fichier nommé `greet.py`.

Créez donc un nouveau fichier nommé `obo.py` et sauvegardez-le dans votre répertoire `programming-historian`. Nous utiliserons ce fichier pour faire appel aux fonctions dont nous aurons besoin durant le traitement de The Old Bailey Online. Entrez ou copiez le code suivant de votre fichier.

```python
# obo.py

def stripTags(pageContents):
  # Convertit le contenu en chaine de caractères
  pageContents = str(pageContents)
  # récupère l’indice de la première occurrence de la balise <p>
  startLoc = pageContents.find("<p>")
  # récupère l’indice de la première occurrence de la dernière balise </br>
  endLoc = pageContents.rfind("<br/>")
  # remplace le contenu de la variable par texte contenu entre les deux balises
  pageContents = pageContents[startLoc:endLoc]
  return pageContents
```

Créez ensuite un nouveau fichier, `trial-content.py`, dans lequel vous copierez par la suite le code suivant&nbsp;:

```python
# trial-content.py

import urllib.request, urllib.error, urllib.parse, obo

url = ’http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33’

# télécharge le contenu de la page web 
response = urllib.request.urlopen(url)
HTML = response.read()

# On teste ici le fonctionnement de notre fonction
print((obo.stripTags(HTML)))
```

Lorsque vous exécutez `trial-content.py`, le programme ira dans un premier temps chercher le contenu de la page web de la transcription du procès de Bowsey, puis ira rechercher dans le module `obo.py` la fonction `stripTags` . Le programme utilisera cette fonction pour extraire le contenu compris entre la première balise `<p>` et la dernière balise `</br>`. Si tout est correct, cela nous renverra bien le contenu de la transcription de Bowsey, avec, comme nous le prévoyons, quelques balises HTML. 

Il se peut que vous obteniez en réponse une épaisse ligne noire dans votre sortie de commande, mais ne vous inquiétiez pas. La sortie de l’éditeur de texte Komodo Edit est limitée à un nombre maximum de caractères qu’il est possible d’afficher, après lequel les caractères s’écriront littéralement les uns sur les autres à l’écran, donnant l’apparence d’une tache noire. Pas de panique, le texte est dans ce cas bien ici, mais vous ne pouvez pas le lire&nbsp;; afin de résoudre ce problème d’affichage, vous pouvez copier/coller ce texte dans un nouveau fichier, à titre de vérification.

Prenons maintenant un moment pour nous assurer que vous avez bien compris comment fonctionne `trial-contents.py`, qui est capable d’utiliser les fonctions présentes dans `obo.py`. La fonction `stripTags` du module `obo.py` a besoin d’être lancée avec un argument. En d’autres termes, pour lancer cette fonction correctement, nous avons donc besoin de lui fournir cette information. La fonction `stripTags` de `obo.py` a besoin d’une seule chose&nbsp;: une chaine de caractères nommée `pageContents`. Mais vous remarquerez que lorsque l’on appelle la fonction `stripTags` à la fin de notre programme (`trialcontents.py`) nous ne mentionnons pas de variable nommée `pageContents`. Au lieu de cela, la fonction reçoit une variable nommée HTML comme argument. Cela peut être déroutant pour de nombreuses personnes lorsqu’elles commencent à programmer. Quand l’on déclare une fonction et ses arguments, nous ne sommes pas obligé⸱e⸱s de nommer les variables d’entrée de la même manière. Tant que le type de l’argument est le correct, tout devrait fonctionner comme prévu, peu importe le nom que nous lui donnons. 

Dans notre cas, nous souhaitons faire passer à l’argument `pageContents` le contenu de notre variable *HTML*. Vous auriez pu lui passer n’importe quelle chaine de caractères, y compris celle que vous aviez saisie directement entre les parenthèses. Essayez de relancer `trial-content.py`, en remplaçant l’argument fourni à `stripTags` par &laquo;&nbsp;J’aime beaucoup les chiens&nbsp;&raquo; et observez ce qui se passe. Notez qu’en fonction de la manière dont vous définissez votre fonction (et ce qu’elle est censée faire), votre argument peut être autre chose qu’une chaine de caractères&nbsp;: un *entier*, par exemple. Pour mieux appréhender les différents types de données disponibles à travers Python, nous vous invitons à consulter [les cours de Zeste de Savoir](https://perma.cc/QH3X-BS79) sur le sujet.


# Lectures suggérées

- Lutz, Mark. *Learning Python* (5th edition). O’Reilly Media, Inc., 2013.
    - Ch. 7: Strings
    - Ch. 8: Lists and Dictionaries
    - Ch. 10: Introducing Python Statements
    - Ch. 15: Function Basics

# Synchronisation du code

Pour suivre les leçons à venir, il est important que vous ayez les bons fichiers et programmes dans votre répertoire `programming-historian`. À la fin de chaque chapitre, vous pouvez télécharger le fichier zip contenant le matériel de cours du the programming-historian afin de vous assurer d’avoir le bon code. Notez que nous avons supprimé les fichiers inutiles des leçons précédentes. Votre répertoire peut contenir plus de fichiers&nbsp;; ce n’est pas grave, l’important est de s’assurer que les codes que nous utiliserons par la suite fonctionneront.

- [`programming-historian-2.zip`](/assets/python-lessons2.zip)
