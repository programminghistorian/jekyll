---
title: "Introduction à la publication web de fichiers TEI avec CETEIcean"
slug: publier-archives-tei-ceteicean
original: publicar-archivos-tei-ceteicean
collection: lessons
layout: lesson
date: 2021-12-14
translation_date: 2026-04-01
authors:
- Gabriel Calarco
- Gimena del Río Riande
reviewers:
- Melissa Jerome
- Aldo Barriente
editors:
- Joshua G. Ortiz Baco
translator:
- Yanet Hernández Pedraza
translation-editor:
- Matthias Gille Levenson
translation-reviewer:
- Lucence Ing
- Andrés Echavarria
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/666
difficulty: 2
activity: transforming
topics: [website, text-encoding]
abstract: Cette leçon vous enseigne les étapes nécessaires pour publier en ligne un fichier TEI en utilisant CETEIcean.
avatar_alt: Gravure représentant différentes sources typographiques.
doi: 10.46430/phfr0039
---

{% include toc.html %}

>**Note&nbsp;:** Pour suivre ce tutoriel, vous devez savoir ce qu'est le langage de balisage XML-TEI développé par la [Text Encoding Initiative ou TEI](https://tei-c.org/) et quelle est sa fonction en tant que langage standard dans l'édition numérique savante de textes en sciences humaines et sociales. Vous pouvez trouver des ressources et des tutoriels en français sur l'encodage de textes en TEI sur [La TEI Lite](https://perma.cc/4GLQ-B33D). Nous vous recommandons également les parties 1 et 2 de la leçon [Introduction à l'encodage de textes en TEI par Nicolás Vaughan](/es/lecciones/introduccion-a-tei-1) (les parties 1 et 2 sont disponibles dans la version originale en espagnol, la partie 1 est également disponible en anglais et en portugais) et l'[Initiation XML-TEI par Lauranne Bertrand](https://perma.cc/H3SC-8J7D). Durant ce tutoriel, d'autres langages informatiques seront utilisés (comme le [JavaScript](https://www.javascript.com/) et le [CSS](https://perma.cc/4MZP-W3L3)), mais il n'est pas nécessaire d'avoir des connaissances préalables sur leur fonctionnement pour utiliser [CETEIcean](https://perma.cc/Q74Z-P8XJ).

## Introduction et logiciels que nous utiliserons
Pour les personnes qui débutent avec la TEI, l'un des obstacles les plus courants est que, une fois que les textes ont été encodés avec ce langage de balisage, il est difficile de savoir comment les publier en ligne. Pour être visualisés dans un navigateur, les fichiers XML-TEI doivent d'abord être transformés en [HTML](https://perma.cc/T4Z2-EBAG) à l'aide de feuilles de transformation [XSLT](https://perma.cc/5RKM-M6TQ). Cependant, ce processus requiert des connaissances techniques et des outils qui ne sont pas toujours à la portée des humanistes numériques, en particulier des personnes qui abordent l'utilisation de la TEI pour la première fois, qui ne connaissent pas encore en profondeur l'utilisation de logiciels d'édition ou qui n'ont pas accès à des serveurs propres. CETEIcean est un logiciel d'édition numérique qui permet de visualiser des fichiers XML-TEI dans le navigateur sans avoir à appliquer une transformation XSLT.

Ce tutoriel vous guidera à travers les étapes nécessaires pour publier un fichier TEI en ligne en utilisant CETEIcean, une bibliothèque ouverte écrite dans le langage de programmation JavaScript. CETEIcean permet d'afficher les documents TEI dans un navigateur web sans les transformer au préalable en HTML. CETEIcean charge le fichier TEI dynamiquement dans le navigateur et convertit les éléments TEI en éléments HTML, de sorte que ceux-ci nous permettent de visualiser dans le navigateur web les phénomènes textuels que nous balisons dans nos fichiers en utilisant la TEI.

Tout d'abord, une clarification concernant la visualisation de votre travail&nbsp;: la méthode par défaut de CETEIcean pour afficher les fichiers TEI consiste à charger les fichiers depuis un autre emplacement. Cependant, tous les navigateurs ne vous permettront pas de charger les fichiers s'ils sont stockés sur votre ordinateur. Vous pouvez essayer, mais si cela ne fonctionne pas, vous devrez générer un serveur local, placer les fichiers sur un serveur en ligne, ou utiliser un éditeur de code avec des fonctions de prévisualisation. Pour ce tutoriel, nous suivrons cette dernière option, car nous utiliserons l'éditeur [Visual Studio Code](https://code.visualstudio.com/), avec l'extension *HTML Preview*. Néanmoins, il existe d'autres options libres pour éditer des fichiers TEI et générer des prévisualisations HTML, comme [jEdit](http://www.jedit.org/) ou [Atom](https://atom.io), ainsi que des versions propriétaires comme [Oxygen](https://www.oxygenxml.com/).

<div class="alert alert-warning">
Mise à jour de mars 2025&nbsp;: La version originale en espagnol utilise l'éditeur <em>Atom</em>&nbsp;; cependant nous ne recommandons pas d'utiliser Atom, car le logiciel n'a pas reçu de maintenance ni de mises à jour depuis sa fermeture en décembre 2022. Nous avons donc décidé d'utiliser <em>VS Code</em> de la même manière, à condition d'installer également l'extension <em>HTML Preview</em> depuis l'onglet Extensions.
</div>

Vous devrez donc télécharger et installer [Visual Studio Code](https://code.visualstudio.com/) avant de continuer avec ce tutoriel. Une fois VS Code lancé, installez l'extension *HTML Preview* (créée par George Oliveira) que vous pouvez trouver en ouvrant l'onglet *Extensions* (l'icône des quatre carrés dans la barre latérale). Dans la barre de recherche, tapez le nom de l'extension *HTML Preview*. Lorsque l'extension que nous recherchons apparait dans la liste des résultats, vous devez cliquer sur l'extension et ensuite sur le bouton bleu *Installer*&nbsp;:

{% include figure.html filename="fr-tr-publier-archives-tei-ceteicean-01.png" alt="Capture d'écran de l'application VS Code qui dirige les lecteurs vers le marketplace d'extensions (le cinquième bouton du menu à gauche) et qui montre comment après une recherche pour 'HTML Preview' les lecteurs peuvent installer l'extension." caption="Figure 1. Processus d'installation de l'extension HTML Preview pour prévisualiser les fichiers en HTML." %}

Nous utiliserons en tant que texte d'exemple *La Dernière Incarnation de Vautrin*, quatrième partie du roman *Splendeurs et misères des courtisanes*, par l'écrivain et essayiste français [Honoré de Balzac](https://perma.cc/73RH-XBVZ). Ce texte du XIXe siècle a paru en feuilleton dans *La Presse* du 13 avril au 17 mai 1847. Il s'agit de la conclusion du roman, qui explore les aspects souterrains, tels que le crime et la prostitution, de la société française du XIXe siècle. Vous pouvez trouver une édition numérique complète du texte réalisée par le projet *ANR Phœbus (&laquo;&nbsp;Projet d’hypertexte de l’œuvre de Balzac par l’utilisation de similarités&nbsp;&raquo;)* sur&nbsp;: [https://www.ebalzac.com/edition/42-splendeurs-miseres-courtisanes/presse](https://www.ebalzac.com/edition/42-splendeurs-miseres-courtisanes/presse).

Nous commencerons avec un fichier simple (bien qu'un peu long) au format TEI P5, que nous voulons rendre visible dans un navigateur web&nbsp;: [`balzac-42-splendeurs-miseres-courtisanes-presse-derniere-incarnation-vautrin.xml`](https://api.nakala.fr/data/10.34847/nkl.4fb47i30/a29cf71aeb3f98543df574d5efddf11c8b34d7ef). Pour télécharger le fichier, faites un clic droit sur le lien de téléchargement et sélectionnez l'option *Enregistrer le lien sous...*.

## Étape 1&nbsp;: Créer une structure pour nos fichiers
La structuration des dossiers et fichiers prendra l'aspect suivant, avec un dossier racine `tutoriel_fr` qui contiendra tous les sous-dossiers et fichiers que nous vous indiquerons ci-dessous. Vous pouvez télécharger le répertoire complet du dépôt [CETEIcean sur GitHub](https://github.com/TEIC/CETEIcean) et travailler dans le dossier `tutoriel_fr`, ou vous pouvez télécharger les fichiers individuellement, à condition qu'ils conservent la même structure que sur le dépôt git du projet, qui est la suivante&nbsp;:

```
  tutoriel_fr/
      |
      |--- css/
            |
            |--- tei.css
      |
      |--- js/
            |
            |--- CETEI.js
      |
      |--- balzac-42-splendeurs-miseres-courtisanes-presse-derniere-incarnation-vautrin.xml
      |--- README.md (le fichier que vous êtes en train de lire)
```

L'étape suivante consistera à créer un nouveau fichier dans VS Code avec le nom `index.html`. Pour cela, vous pouvez ouvrir le dossier `tutoriel_fr` dans VS Code et ensuite sélectionner Fichier > Nouveau fichier... ou utiliser le raccourci Ctrl + N (Cmd + N sur Mac). Dans ce document, vous devez copier le contenu suivant&nbsp;:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">

</head>
<body>

</body>
</html>
```

Ensuite, vous devez enregistrer ce fichier dans le répertoire racine (dans notre cas, le dossier `tutoriel_fr`)&nbsp;; rappelez-vous que son titre doit être `index.html`. Ce fichier servira de structure dans laquelle nous mettrons les instructions pour afficher nos fichiers TEI. Tout comme les fichiers TEI, les fichiers HTML ont un entête, appelé `<head>`, et un corps de texte, appelé `<body>`. Tout au long de ce tutoriel, nous utiliserons ce fichier pour ajouter des liens vers notre CSS (_Cascading Style Sheet_, également appelée _feuille de style_ ou [_feuille de styles en cascade_](https://perma.cc/4MZP-W3L3) en français) et vers nos fichiers JavaScript, et nous écrirons un peu de JavaScript pour obtenir une visualisation de notre document TEI qui reflète les aspects du balisage que nous souhaitons mettre en évidence. Dans la première ligne vide du `<head>`, écrivez&nbsp;:

```html
  <link rel="stylesheet" href="css/tei.css">
```

Cela connectera notre fichier CSS à notre page HTML, lui donnant accès aux directives de style qu'il contient (il n'y en a que quelques-unes, mais nous en ajouterons d'autres). Ensuite, nous inclurons la bibliothèque CETEIcean, en ajoutant la ligne suivante après le lien vers la feuille de style&nbsp;:

```html
  <script src="js/CETEI.js"></script>
```

À ce stade, notre fichier `index.html` devrait avoir le contenu suivant&nbsp;:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
<!-- Lignes ajoutées -->
<link rel="stylesheet" href="css/tei.css">
<script src="js/CETEI.js"></script>
<!-- Lignes ajoutées -->
</head>
<body>

</body>
</html>
```

## Étape 2&nbsp;: Charger et prévisualiser le fichier TEI
Nous sommes maintenant prêts à charger le fichier TEI. Pour cela, nous devons ajouter une séquence de commandes informatiques communément appelée par son nom anglais [&laquo;&nbsp;script&nbsp;&raquo;](https://perma.cc/545L-WV2Z), qui nous permettra de récupérer le document TEI de *La Dernière Incarnation de Vautrin* dans notre fichier HTML (celui que nous sommes en train d'éditer). Copiez et collez les lignes de code suivantes après le dernier élément que nous avons ajouté (`<script src="js/CETEI.js"></script>`)&nbsp;:

```html
<script>
let c = new CETEI();
 c.getHTML5('balzac-42-splendeurs-miseres-courtisanes-presse-derniere-incarnation-vautrin.xml', function(data) {
   document.getElementsByTagName("body")[0].appendChild(data);
 });
</script>
```

Vous n'avez pas besoin d'être un expert en JavaScript pour utiliser CETEIcean, mais apprendre son fonctionnement de base peut être utile. Par ailleurs, si vous souhaitez inclure des fonctions avancées, vous devrez apprendre JavaScript. Sur le réseau pour développeurs de Mozilla, vous pouvez trouver un excellent [guide JavaScript](https://perma.cc/XLN5-DXBA) dans plusieurs langues, dont le français. Pour ce tutoriel, nous expliquons seulement quelques éléments&nbsp;:

- Premièrement, une variable `c` est définie comme un nouvel objet CETEI. Elle permet de charger et d'appliquer les styles à notre fichier source
- Deuxièmement, nous indiquerons à `c` de charger le fichier source et de le convertir en HTML ([Custom Elements](https://perma.cc/7VSF-L97H)), et nous lui donnerons également une fonction qui récupèrera les résultats et les insèrera dans le `<body>` de notre fichier `index.html`
- Troisièmement, dans la quatrième ligne du code, la fonction `getElementsByTagName('body')` recherche tous les éléments `<body>` et les renvoie sous la forme d'une liste ordonnée (une liste dans laquelle on peut accéder aux membres qui la composent à travers leur numéro d'index)
- Enfin, dans notre exemple, il n'y a qu'un seul élément `<body>`, nous obtiendrons donc une seule entrée dans notre liste, d'où le bout de code `('body')[0]`. Cet élément, qui est un élément HTML, reçoit comme enfant le contenu de notre document TEI fraichement converti

À ce stade, vous devriez pouvoir obtenir une prévisualisation du fichier HTML. Nous allons le prévisualiser avec l'extension que nous avons installée au début de ce tutoriel. Pour cela, faites un clic droit sur le fichier HTML et choisissez dans le menu déroulant l'option &laquo;&nbsp;*Open Preview*&nbsp;&raquo;&nbsp;:

{% include figure.html filename="fr-tr-publier-archives-tei-ceteicean-02.png"  alt="Capture d'écran qui montre l'option à choisir dans le menu déroulant qui s'ouvre en faisant un clic droit sur le fichier HTML." caption="Figure 2. Menu des options pour prévisualiser les fichiers en HTML dans VS Code." %}

{% include figure.html filename="fr-tr-publier-archives-tei-ceteicean-03.png"  alt="Capture d'écran qui montre comment trouver l'option pour changer les paramètres de sécurité de l'extension `HTML Preview` en cliquant sur le bouton 'Plus d'actions...' situé à droite." caption="Figure 3. Bouton pour changer les paramètres de sécurité de l'extension `HTML Preview` pour permettre l'exécution des scripts pour la prévisualisation des fichiers TEI avec CETEIcean" %}

{% include figure.html filename="fr-tr-publier-archives-tei-ceteicean-04.png"  alt="Capture d'écran qui indique qu'il faut choisir l'option 'Disable' pour pouvoir prévisualiser les fichiers TEI avec CETEIcean." caption="Figure 4. Option à choisir pour activer l'exécution des scripts pour la prévisualisation des fichiers TEI avec CETEIcean" %}

{% include figure.html filename="fr-tr-publier-archives-tei-ceteicean-05.png" alt="Capture d'écran montrant une première prévisualisation de notre fichier TEI avec CETEIcean. Le fichier HTML et la prévisualisation apparaissent côte à côte&nbsp;: le fichier HTML à gauche et la prévisualisation à droite." caption="Figure 5. Première prévisualisation de notre fichier TEI avec CETEIcean" %}

Si vous n'utilisez pas VS Code, vous pouvez faire la même chose en plaçant vos fichiers sur un serveur web. Si vous connaissez le fonctionnement de GitHub, vous pouvez utiliser GitHub Pages (voici un [tutoriel](https://perma.cc/2E68-D976) en français) et créer un dépôt. Si vous avez installé Python sur votre ordinateur, vous pouvez exécuter un serveur web simple dans le répertoire de ce tutoriel (dans notre cas, le dossier `tutoriel_fr`). À cette fin, vous devez ouvrir la console de commandes et vérifier que vous êtes dans le dossier souhaité (sinon, vous pouvez naviguer jusqu'à ce dossier avec la commande `cd + chemin/vers/le/dossier`, par exemple&nbsp;: `cd Documents/tutoriel_fr`) et entrer la commande&nbsp;:

```bash
python -m SimpleHTTPServer
```

Il est également possible que votre ordinateur ait déjà les programmes nécessaires pour exécuter un serveur web, ou vous pouvez installer [MAMP](https://www.mamp.info) ou un autre programme similaire. L'objectif de la création de ce serveur est de visualiser nos fichiers TEI dans le navigateur comme s'il s'agissait d'un contenu en ligne.

## Étape 3&nbsp;: Améliorer la visualisation de notre fichier
Cette première visualisation contiendra plusieurs erreurs que nous devrons corriger. Pour cela, nous reviendrons à notre travail dans VS Code. Nous commencerons par ajouter une feuille de style pour mettre en forme les éléments TEI dans notre fichier, puis nous ajouterons des fonctions de CETEIcean pour faire des modifications plus complexes. Si vous n'avez pas encore jeté un coup d'œil au fichier source XML, c'est le bon moment pour le faire, pour voir ce que CETEIcean fait déjà et ce qu'il ne fait pas. Nous pouvons observer que le contenu du `<teiHeader>` n'est pas affiché. Les éléments `<div>` et `<p>`, quant à eux, sont formatés comme des blocs et les notes apparaissent dans le corps du texte entre parenthèses. Dans le `<body>` de notre document source, il existe huit types d'éléments&nbsp;:

 * [div](https://perma.cc/LU2R-8599)
 * [head](https://perma.cc/JNM6-PWM4)
 * [note](https://perma.cc/YLY2-UD6N)
 * [p](https://perma.cc/MP29-UTYS)
 * [q](https://perma.cc/C35U-GJ6Q)
 * [hi](https://perma.cc/5H8Q-YD3M)
 * [pb](https://perma.cc/SBJ8-F76K)
 * [label](https://perma.cc/8KAK-Z2XT)

Certains de ces éléments peuvent ne pas nécessiter de styles ou de comportements spéciaux, mais d'autres en auront certainement besoin.
Jetez un coup d'œil au fichier `tei.css` du dossier `css/`. Comme vous pouvez le voir, il n'a que quelques règles pour l'instant&nbsp;:

```css
tei-div {
  display: block;
}
tei-p {
  display: block;
  margin-top: .5em;
  margin-bottom: .5em;
}
```

Remarquez que les noms des éléments dans nos sélecteurs CSS ont le préfixe `tei-`. Ceci est nécessaire pour que CETEIcean puisse convertir les éléments TEI en éléments HTML personnalisés ([Custom Elements](https://perma.cc/7VSF-L97H)). Ces règles établissent que les éléments `<div>` sont visualisés comme des blocs (ils commencent sur une nouvelle ligne et se terminent par un saut de ligne)&nbsp;; il en va de même pour les paragraphes, qui ont également des marges supérieures et inférieures.

Décider quels styles appliquer aux éléments qui n'en ont pas encore n'est pas une tâche aisée, mais nous pouvons commencer à en établir pour les cas les plus simples. Par exemple, dans notre document source, les entêtes des différentes sections sont signalés par l'élément `<head>`. Dans la visualisation HTML, nous souhaiterions probablement que ces entêtes se distinguent du corps du texte. Nous pouvons donc modifier la feuille de style CSS afin de leur donner un style particulier. Maintenant, vous devez ouvrir le fichier `tei.css` (que vous trouverez dans le dossier `css`) dans VS Code et à la fin du document, ajoutez les lignes suivantes&nbsp;:

```css
tei-head {
  font-size: 2em;
  font-weight: bold;
}
```

Vous verrez que ce n'est pas une solution parfaite, car nous avons différents niveaux d'éléments `<div>`, et il serait approprié que les entêtes de différents niveaux aient des tailles différentes pour les identifier. Étant donné que les éléments `<div>` de notre fichier TEI n'indiquent pas leur niveau d'imbrication, cela peut être difficile à réaliser avec CSS. Cependant, nous pouvons également utiliser les comportements (_behaviors_) de CETEIcean pour la mise en forme.

En HTML, la convention est de représenter les différents niveaux d'entête avec les éléments `<h1>`, `<h2>`, `<h3>`, etc. (jusqu'à `<h6>`). Nous pouvons y parvenir en utilisant un comportement. Pour cela, dans votre fichier `index.html`, ajoutez ce qui suit entre la première et la deuxième ligne du code qui se trouve entre les balises `<script></script>` (c'est-à-dire entre `"let c = new CETEI();"` et `"c.getHTML5('balzac-42-splendeurs-miseres-courtisanes-presse-derniere-incarnation-vautrin.xml'…"`):

```js
  let comportements = {
    "tei": {
      "head": function(e) {
        let niveau = document.evaluate("count(ancestor::tei-div)", e, null, XPathResult.NUMBER_TYPE, null);
        let resultat
        if (niveau.numberValue <= 6) {
          resultat = document.createElement("h" + niveau.numberValue);
        } else if (niveau.numberValue > 6) {
          resultat = document.createElement("h6"); // Les niveaux supérieurs à 6 sont tous rendus en h6
        }
        for (let n of Array.from(e.childNodes)) {
          resultat.appendChild(n.cloneNode());
        }
        return resultat;
      }    
    }
  };
  c.addBehaviors(comportements);
```

Cela créera un objet Javascript et lui assignera la variable `comportements`, que nous lierons ensuite à l'objet `CETEI` que nous avons créé auparavant, en utilisant la méthode `addBehaviors` (qui est déjà incluse dans CETEIcean). À l'intérieur de cet objet, nous avons une section étiquetée comme &laquo;&nbsp;tei&nbsp;&raquo; (qui est le préfixe pour tous nos éléments personnalisés), et à l'intérieur de celle-ci, les comportements pour les éléments sont définis. Lorsque CETEIcean trouve une correspondance pour le nom d'un élément, comme &laquo;&nbsp;head&nbsp;&raquo; (notez que le nom de TEI est utilisé sans le préfixe), il applique les comportements correspondants.

Ce nouveau comportement prend une fonction de JavaScript, de sorte que l'élément soit traité comme un paramètre (le `e`). Cela crée la variable `niveau`, qui contient le niveau d'imbrication de la `<tei-div>` parent du `<tei-head>`, crée ensuite un élément `<h[niveau]>` avec le niveau correspondant, et copie enfin le contenu de l'élément original dans le nouvel élément d'entête. CETEIcean affichera le contenu du nouvel élément d'entête, par exemple `<h2>`, au lieu de l'élément original `<tei-head>`. Notez que ce code inclut un bloc de conditions pour produire un élément d'entête `<h6>` si le niveau d'imbrication est supérieur à 6 afin d'éviter de produire un élément d'entête supérieur à la limite admise par HTML (par exemple, un élément `<h7>`). Notre document source n'a pas plus de deux niveaux d'imbrication, mais ce code peut être utile pour d'autres sources.

Si à ce stade, nous prévisualisons notre HTML dans VS Code, nous obtenons le résultat suivant&nbsp;:

{% include figure.html filename="fr-tr-publier-archives-tei-ceteicean-06.png" alt="Capture d'écran qui montre le fichier HTML sur le côté gauche et la prévisualisation de notre fichier TEI où on peut voir les titres en gras et en plus grande taille selon le niveau du titre sur le côté droit." caption="Figure 6. Prévisualisation de notre fichier TEI avec style pour les titres." %}

Avec cette prévisualisation, nous avons considérablement amélioré la présentation de notre document, mais les notes de l'édition rendent toujours la lecture du texte difficile. Pour résoudre ce problème, nous ajouterons un comportement supplémentaire à notre script. Cependant, pour atteindre cet objectif, nous devrons utiliser une séquence de commandes un peu plus longue et complexe que la précédente. Copiez et collez le texte suivant entre les lignes `"tei": {` et `"head": function(e) {` qui se trouvent dans le deuxième élément `<script>` de notre document `index.html`:

```js
    "note": function(e){
    if (!this.noteIndex){
      this["noteIndex"] = 1;
    } else {
      this.noteIndex++;
    }    
    /* Le premier bloc vérifie s'il y a des notes dans le texte et les numérote séquentiellement*/

    let id = "note" + this.noteIndex;
    let lien = document.createElement("a");
    lien.setAttribute("id", "src" + id);
    lien.setAttribute("href", "#" + id);
    //link.setAttribute("title", e.textContent); // Décommenter cette ligne pour ajouter le texte de la note en info-bulle
    lien.innerHTML = this.noteIndex;
    let contenu = document.createElement("sup");
    if (e.previousSibling.localName == "tei-note") {
      contenu.appendChild(document.createTextNode(","));
    }
    /* Le deuxième bloc ajoute un numéro à chaque note*/

    contenu.appendChild(lien);
    let notes = this.dom.querySelector("ol.notes");
    if (!notes) {
      notes = document.createElement("ol");
      notes.setAttribute("class", "notes");
      this.dom.appendChild(notes);
    }
    /* Le troisième bloc crée une section de notes à la fin du document */

    let note = document.createElement("li");
    note.id = id;
    note.innerHTML = "<a href=\"#src" + id + "\">^</a> " + e.innerHTML
    notes.appendChild(note);
    return contenu;
  },
    /* Enfin, le quatrième bloc crée une liste avec les notes et les lie avec les références dans le corps du texte */
```

Pour suivre ce tutoriel, il n'est pas nécessaire de comprendre le fonctionnement de chaque ligne de ce comportement. Cependant, si vous observez le résultat de la prévisualisation, vous remarquerez qu'en l'incluant, les notes apparaissent à la fin du texte, liées par hyperlien avec leurs références respectives&nbsp;:

{% include figure.html filename="fr-tr-publier-archives-tei-ceteicean-07.png" alt="Capture d'écran qui montre le fichier HTML sur le côté gauche et la prévisualisation de notre fichier TEI avec les numéros des notes sous forme de lien hypertexte sur le côté droit." caption="Figure 7. Prévisualisation de notre fichier TEI avec style pour les appels de notes." %}

## Étape 4&nbsp;: Pour continuer à travailler avec CETEIcean
CETEIcean possède un certain nombre de comportements intégrés que vous pouvez remplacer ou désactiver en leur assignant des valeurs. Si, par exemple, vous souhaitez afficher le contenu du `<teiHeader>` (qui est caché par défaut), vous pouvez ajouter la ligne suivante à notre `<script>` en dessous de `"tei": {`:

```js
  "teiHeader": null,
  // Exemple de comportement personnalisé pour les sauts de ligne (décommenter la ligne suivante pour activer)
  //"lb": function(e){let lb = document.createElement("br") ; return lb;},
```

Si vous faites cela, vous voudrez peut-être ajouter des styles CSS ou des comportements pour choisir la manière dont le contenu du TEI Header sera affiché dans le navigateur.

Dans ce tutoriel, nous n'avons pas épuisé toutes les possibilités pour la présentation de notre document source. Nous vous invitons à continuer à expérimenter par vous-même les différentes manières dont un balisage TEI peut être affiché dans un navigateur en utilisant CETEIcean. Vous pouvez trouver plus d'informations sur [CETEIcean](http://teic.github.io/CETEIcean/). Vous pouvez aussi trouver quelques lignes de code commentées dans cette leçon pour appliquer certains comportements supplémentaires qui pourront s'avérer utiles.

## Références bibliographiques

Balzac, Honoré. &laquo;&nbsp;La Dernière Incarnation de Vautrin&nbsp;&raquo;, dans *Splendeurs et misères des courtisanes*, La Presse (1847), édité par Tania Duclos, Maxime Perret, et Amélie Canu (ANR Phoebus e-Balzac, 2017). [https://www.ebalzac.com/edition/42-splendeurs-miseres-courtisanes/presse](https://perma.cc/TPW9-XABX).

Balzac, Honoré. &laquo;&nbsp;La Dernière Incarnation de Vautrin, paru en feuilleton dans La Presse du 13 avril au 17 mai 1847&nbsp;&raquo;, fichier XML 10.34847/nkl.4fb47i30. Avec Tania Duclos, Maxime Perret, et Amélie Canu (Nakala, 8 septembre 2021). XML. [https://doi.org/10.34847/NKL.4FB47I30](https://doi.org/10.34847/NKL.4FB47I30).

Bertrand, Lauranne. &laquo;&nbsp;Initiation XML-TEI&nbsp;&raquo;, (URFIST, BORDEAUX, 12 juillet 2016). [http://weburfist.univ-bordeaux.fr/wp-content/uploads/2016/12/20161209_BERTRAND-URFIST-TEI-1.pdf](https://perma.cc/H3SC-8J7D).

Sperberg-McQueen, C. M., et Lou Burnard. &laquo;&nbsp;La TEI Lite&nbsp;: Encoder Pour Échanger&nbsp;: Une Introduction à La TEI&nbsp;&raquo;, traduit par Sophie David. Consulté le 12 août 2025. [https://www.tei-c.org/release/doc/tei-p5-exemplars/html/tei_lite_fr.doc.html](https://perma.cc/4GLQ-B33D).

Vaughan, Nicolás. &laquo;&nbsp;Introduction au codage de textes en TEI (partie 1)&nbsp;&raquo;, *Programming Historian en español* 5 (2021). [https://doi.org/10.46430/phes0053](https://doi.org/10.46430/phes0053).

## Outils techniques

- Atom. Un éditeur de texte hackable pour le 21e siècle. [https://atom.io](https://atom.io)

- Cayless, Hugh et Viglianti, Raffaele. CETEIcean. [http://teic.github.io/CETEIcean/](http://teic.github.io/CETEIcean/)

- Jedit. Éditeur de texte pour programmeurs. Version stable&nbsp;: 5.6.0. [http://www.jedit.org/](http://www.jedit.org/)

- Oxygen. Éditeur XML. [https://www.oxygenxml.com/](https://www.oxygenxml.com/)

- Visual Studio Code. [https://code.visualstudio.com/](https://code.visualstudio.com/)
