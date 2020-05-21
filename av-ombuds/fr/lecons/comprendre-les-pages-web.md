---
title: Comprendre les pages web et le HTML
layout: lesson
slug: comprendre-les-pages-web
date: 2012-07-17
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Amanda Morton
editors:
- Miriam Posner
translator:
- Sylvain Machefert
translation-editor:
- Sofia Papastamkou
translation-reviewer:
- Frédéric Clavert
- François Dominic Laramée
translation_date: 2019-07-06
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/228
activity: presenting
topics: [python]
abstract: "Cette leçon propose une introduction au langage HTML et à la structuration des pages web."
original: viewing-html-files
avatar_alt: Une femme entend un homme parler à travers un cornet acoustique
doi: 10.46430/phfr0002
---

"Hello World" en HTML
---------------------

## Consulter des fichiers HTML

Lorsque vous travaillez avec des sources en ligne, vous utilisez
la plupart du temps des fichiers qui ont été encodés en HTML (Hyper Text Markup
Language). Votre navigateur web sait interpréter ce code, et vous permet
de consulter le *code source* HTML pour n'importe quelle page que vous visitez.
Les deux images ci-dessous montrent une page web classique (du site *Old Bailey Online*)
et le code source utilisé pour générer cette page. Vous pouvez voir ce code source
dans votre navigateur par le menu : `Outils -> Développement -> Code source de la page`
sous Firefox (ou par le raccourci `Ctrl + U`).

Lorsque vous naviguez sur le web, vous n'avez en général pas besoin de consulter
le code source de la page. Cependant, si vous devez créer une page, il peut être
très utile de voir comment d'autres ont réalisé un effet particulier. Il vous sera
aussi utile de consulter les sources des pages si vous devez manipuler leur contenu
ou en extraire automatiquement de l'information.

{% include figure.html filename="obo.png" caption="Capture d'écran du Old Bailey Online" %}

{% include figure.html filename="obo-page-source.png" caption="Code HTML de Old Bailey Online" %}

(À ce point de la lecture, vous pourrez trouver intéressant de naviguer sur les
[tutoriels W3 Schools HTML][]. Une connaissance approfondie du HTML n'est pas nécessaire
pour poursuivre la lecture, mais tout temps passé à apprendre le HTML sera forcément
utile dans vos activités d'humaniste numérique.)

## "Hello World" en HTML

HTML est ce que l'on appelle un langage de *balisage*. En d'autres termes,
le HTML est du texte qui a été "encodé" avec des *balises* qui fournissent
des informations supplémentaires à l'interprète (souvent le navigateur web).
Supposez que vous souhaitiez formatter une référence bibliographique et
souhaitez placer le titre en italique. En HTML on utilise le mot-clé `em`
("em" pour emphasis, accentuation). Une partie de votre code HTML pourrait
ressembler à :
``` xml
... dans l’œuvre de Cohen et Rosenzweig <em>Digital History</em>, par exemple ...
```

Le plus simple des documents HTML est constitué de balises indiquant le début
et la fin du fichier, et des balises qui identifient une 'en-tête' (head) et un 'corps' (body)
à l'intérieur du document. Les informations sur le document se placent dans l'en-tête,
alors que l'information qui sera affichée à l'écran se placera dans le corps.

``` xml
<html>
<head></head>
<body>Hello World!</body>
</html>
```

Pour créer du code HTML : dans votre éditeur de texte, créez un nouveau fichier et collez
le code ci-dessous. La première ligne indique au navigateur le type de fichier.
La balise `html` a pour attribut l'orientation du texte, définie à `ltr` (left to right,
gauche à droite) et l'attribut `lang` (language, langue) définie à *US English*, anglais des États-Unis.
La balise `title` dans l'en-tête contient les information qui sont souvent
affichées dans la barre du haut du navigateur, ou au niveau de l'onglet
sous Firefox.

``` xml
<!doctype html>
<html dir="ltr" lang="en-US">

<head>
    <title><!-- Insérer le titre ici --></title>
</head>

<body>
    <!-- Insérer le contenu ici -->
</body>
</html>
```

Remplacer :

``` xml
<!-- Insérer le titre ici -->
```

et

``` xml
<!-- Insérer le contenu ici -->
```

par

``` xml
Hello World!
```

Enregistrez le fichier dans un dossier `programming-historian` sous le nom
`hello-world.html`. Dans Firefox, rendez-vous dans le menu
`Fichier > Nouvel onglet` puis `Fichier > Ouvrir un fichier`. Choisissez
le fichier `hello-world.html`. En fonction de l'éditeur de texte utilisé,
vous pourrez avoir dans les menus une option 'ouvrir dans le navigateur'.
Après avoir ouvert le fichier, votre message devrait apparaître dans le navigateur.
Vous noterez la différence d'affichage entre le navigateur (qui interprète le code)
et l'éditeur de texte qui ne l'interprète pas.

## Suggestions de ressources pour l'apprentissage du HTML

- [tutoriels W3 Schools HTML][]
- [tutoriels W3 Schools HTML5][]

  [tutoriels W3 Schools HTML]: http://www.w3schools.com/html/default.asp
  [tutoriels W3 Schools HTML5]: http://www.w3schools.com/html/html5_intro.asp
