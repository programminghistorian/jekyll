---
title: Consignes aux auteur(e)s
layout: blank
original: author-guidelines
skip_validation: true
---

# Consignes aux auteur(e)s

<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" alt="{{ site.data.snippets.write-a-lesson-image-alt[page.lang] }}"/>
<h2 class="noclear"> Étape 1 : <a href="#proposer-une-nouvelle-leçon">Proposer une nouvelle leçon</a></h2>
<h2 class="noclear">Étape 2 : <a href="#écrire-une-nouvelle-leçon">Écrire et mettre en forme une nouvelle leçon</a></h2>
<h2 class="noclear">Étape 3 : <a href="#soumettre-une-nouvelle-leçon">Soumettre une nouvelle leçon</a></h2>

## Proposer une nouvelle leçon
Si vous avez une idée pour une nouvelle leçon ou si vous avez déjà rédigé un tutoriel qui, selon vous, pourrait être adapté au *Programming Historian en français*, merci de compléter un [formulaire de proposition](/assets/forms/Formulaire.Tutoriel.txt) et contacter {% include managing-editor.html lang=page.lang %} pour discuter de votre idée. En prenant contact avec l'équipe au tout début du processus, il vous sera plus facile d'élaborer votre leçon -- et plus particulièrement d'identifier le lectorat cible et le niveau de compétence attendu - et de vous associer au rédacteur ou à la rédactrice avec le plus d'expérience sur les thèmes que vous abordez.

<div class="alert alert-success">
Nous acceptons des tutoriels :
<ul>
<li>pertinents pour les humanités;</li>
<li>adaptés à n'importe quel niveau de compétence et d'expérience technique;</li>
<li>concernant un problème ou un processus particulier;</li>
<li>pérennes dans le long terme;</li>
<li>et s'adressant à un public international.</li>
</ul>
La portée et la longueur du tutoriel doivent être appropriés à la complexité de la tâche qui y est expliquée. La longueur des tutoriels ne doit pas excéder 8,000 mots (en incluant le code source) à moins que le rédacteur ou la rédactrice n'en ait explicitement donné la permission. Celle-ci sera uniquement accordée dans des circonstances exceptionnelles. Nous demandons que la longueur des leçons soit en général comprise entre 4,000 et 6,000 mots. Les leçons plus longues pourront être divisées en plusieurs tutoriels.
</div>

Vous pouvez avoir une meilleure idée de ce que nous publions en consultant nos [leçons en ligne](/fr/lecons/), en lisant nos [consignes aux évaluateurs et évaluatrices](/fr/consignes-evaluateurs), ou encore en parcourant les [leçons en cours de développement](https://github.com/programminghistorian/ph-submissions/issues). Nous vous encourageons à proposer des leçons sur des sujets déjà traités ou en en cours de développement, à condition que la nouvelle leçon apporte sa propre contribution originale au traitement d'un sujet donné.

Afin d'assurer la pérennité de nos leçons, les auteur(e)s doivent s'efforcer de soumettre des leçons qui ne sont pas complètement dépendantes de logiciels spécifiques ou d'interfaces utilisateurs. Ces leçons vont à coup sûr souffrir d'instabilité et vont avoir besoin de révisions substantielles lorsque sort une nouvelle version du logiciel ou de l'interface. Enseigner des concepts, plutôt que demander de "cliquer sur le bouton _x_", facilite la rédaction et la publication de tutoriels pérennes.

Une fois que votre proposition est acceptée, un rédacteur ou une rédactrice va créer un ticket "Proposition" dans notre [dépôt de soumissions](https://github.com/programminghistorian/ph-submissions/issues) avec le titre provisoire de la leçon et les objectifs pédagogiques proposés. Ce ticket sert à signaler le travail en cours alors que vous êtes en train de rédiger votre leçon. Pour éviter d'accumuler les retards, nous vous demandons de soumettre votre leçon dans les 90 jours suivant l'acceptation de votre proposition.

-----

## Écrire une nouvelle leçon
Le *Programming Historian en français* est hébergé par [GitHub](http://github.com), qui est une plateforme gratuite permettant de sauvegarder des fichiers et de suivre l'historique de leurs révisions. La plupart du temps, Github est utilisé pour stocker des fichiers de code de programmation, mais c'est aussi une excellente solution pour maintenir une ressource en libre accès comme le *Programming Historian en français*. Plus spécifiquement, notre site utilise [GitHub Pages] pour traiter un ensemble de fichiers de texte brut et les transformer en un site internet élégant.

Cela signifie que nous demandons aux auteur(e)s de respecter les consignes détaillées ci-dessous pour écrire leurs leçons. Celles-ci sont non seulement stylistiques, mais aussi nécessaires pour assurer le bon fonctionnement de notre plateforme de publication. Si nos exigences vous semblent difficiles à respecter, **nous sommes là pour vous aider à vous familiariser avec le processus de publication et à apprendre à utiliser, au fur et à mesure de vos avancées, les technologies nécessaires**.

Gardez à l'esprit que ce projet est basé sur le volontariat, et que nous avons donc besoin que vous fassiez bien attention à tous ces détails.

### Utiliser le texte brut
Parce que notre site est hébergé avec [GitHub Pages](https://pages.github.com), **votre leçon doit être écrite en texte brut**, en utilisant un éditeur de texte de votre choix. *Les éditeurs de texte se distinguent clairement des traitements de texte traditionnels comme Microsoft Word*. Nous recommandons d'utiliser [Atom](https://atom.io/), qui est disponible sous Mac ou Windows. Les utilisateurs de Mac peuvent également envisager d'utiliser [TextWrangler] ou TextEdit (qui est fourni avec macOS). Les utilisateurs de Windows peuvent envisager d'utiliser [Notepad++].

Que vous choisissiez un éditeur de texte ou un autre - cela n'a pas vraiment d'importance -, vous devriez toutefois envisager d'écrire dès le départ votre leçon en texte brut pour éviter de futures frustrations. Par exemple, les guillemets insérés automatiquement par Word crée des problèmes de formatage difficiles à débugger.

### Mettre en forme les notes de bas de page
Nous vous demandons de bien vouloir utiliser le style [Chicago Manual of Style](https://fr.wikipedia.org/wiki/The_Chicago_Manual_of_Style) pour mettre en forme les notes de bas de page.

### Nommer le fichier
Nommez le fichier de votre nouvelle leçon en respectant les conseils suivants :

-   Utilisez des minuscules et choisissez un nom court mais parlant. Ce nom de fichier deviendra le [slug] de l'URL de la leçon quand elle sera publiée. Par exemple, le titre de la leçon intitulée "Débuter avec Markdown" a le slug suivant : `debuter-avec-markdown` et l'URL : `https://programminghistorian.org/en/lessons/debuter-avec-markdown`. Pensez à regarder des leçons existantes pour plus d'exemples concrets.
-   Votre "slug" sera référencé plus tard de la manière suivante : LEÇON-SLUG.
-   Pensez à la manière dont des lecteur(trice)s potentiel(le)s pourraient chercher quelque chose de similaire à votre leçon. Un "slug" riche de mots-clés est une bonne manière de capter le trafic des moteurs de recherche.
-   N'utilisez pas d'espaces ou de tirets bas `(_)` dans le nom du fichier ; utilisez plutôt les traits d'union `(-)`.
-   L'extension du nom du fichier doit être `.md` (markdown).


### Ajouter des métadonnées
Notre plateforme de publication, [GitHub Pages], dépend d'en-têtes spéciales, qui doivent être insérées dans chaque fichier de leçon en texte brut. Ces en-têtes sont appelées blocs liminaires [YAML], et c'est grâce à ces dernières que la leçon s'affiche correctement sur notre site internet. Ces blocs consistent en des champs (comme "titre" et "auteurs") appariés avec des valeurs (comme "Fouiller les données dans l'Internet Archive Collection" et "Caleb McDaniel"). Vous n'avez pas besoin de comprendre en quoi consiste YAML et comment cela fonctionne, mais **vous devez inclure un bloc YAML au début de votre leçon**.

Pour créer le bloc YAML pour votre leçon, vous devez **copier et coller le texte suivant dans votre fichier texte**, et changer les métadonnées correspondantes. Il doit apparaître au tout début de votre fichier, et *doit être suivi d'une ligne vide*. Laissez vide le champ "reviewers" pour l'instant.

     ---
    title: |
       Débuter avec le Topic-Modelling et MALLET
    authors:
    - Ian Milligan
    - Shawn Graham
    - Scott Weingart
    date: 2014-03-03
    reviewers:
    layout: lesson
    ---

<div class="alert alert-danger">
  <h4 class="alert heading">Notes importantes concernant YAML</h4>
  <ul>
    <li>Conservez \| dans le champ titre comme indiqué ; indentez le titre avec une tabulation sur la ligne suivante </li>
    <li> Utilisez le format "liste" indiqué ci-dessus pour le champ auteur, même s'il n'y a qu'un seul auteur</li>
    <li>Assurez-vous qu'il n'y a pas d'espaces superflus dans votre en-tête</li>
    <li> Le bloc YAML doit être suivi par une ligne vide après les trois tirets <code>---</code></li>
  </ul>
</div>


### Écrire en Markdown
**Toutes les nouvelles leçons doivent être écrites en Markdown.** Markdown est un langage de balisage que l'on écrit très facilement avec un éditeur de texte (comme expliqué ci-dessus, n'utilisez pas un traitement de texte comme Word ou Open Office).  Les [GitHub Pages] sont générées par [Jekyll](http://jekyllrb.com/), qui convertit automatiquement les fichiers Markdown dans des pages HTML que vous pouvez trouver sur le site Web. Cette page est elle-même écrite en Markdown, comme vous pouvez le voir en regardant [le texte brut sur Github].

Pour une introduction en douceur à Markdown, consultez:
- [Débuter avec Markdown]({{site.baseurl}}/fr/lecons/debuter-avec-markdown), un tutoriel du *Programming Historian* écrit par Sarah Simpkin
- ou le [guide de GitHub sur Markdown].

<div class="alert alert-warning">
  Avant de continuer, assurez vous que vous comprenez comment utiliser la syntaxe Markdown pour du formatage basique comme la mise en valeur des en-têtes, la mise en gras du texte, l'utilisation de l'italique, l'ajout de liens, la mise en forme des paragraphes, et la création de listes.
</div>

### Écrire de manière durable
Le *Programming Historian en français* s'efforce de publier des leçons qui sont utiles à notre lectorat dans l'immédiat. Les auteur(e)s doivent consulter notre [politique de retrait des leçons]({{site.baseurl}}/fr/politique-retrait-lecons), qui décrit comment l'équipe éditoriale du *Programming Historian en français* gère les leçons qui sont devenues obsolètes. Pour assurer la création de leçons pérennes, nous vous demandons de garder à l'esprit un certain nombre de consignes lors de leur rédaction :

- Au lieu de vous concentrer sur des logiciels en particulier, axez de préférence votre leçon sur les méthodologies, et sur une présentation plus générale des outils.
- Si votre leçon peut tirer profit de la documentation d'un logiciel existant, envisagez de diriger votre lectorat vers cette documentation plutôt que de la répéter dans votre leçon. Et, au lieu d'ajouter un lien vers les ressources concernant un logiciel développé par une entreprise - ressources qui, en général, changent très souvent -, vous pouvez fournir des conseils généraux sur la manière dont vos lecteurs et lectrices peuvent trouver la documentation.
- Limitez l'usage d'images spécifiques à la version du logiciel présenté, à moins que cela ne soit requis pour suivre votre leçon.
- Vérifiez tous les liens externes de façon à vous assurer qu'ils sont à jour.
- Les données nécessaires pour suivre une leçon doivent être hébergées avec notre site Internet.


### Écrire pour un public international

Les lecteurs et les lectrices du *Programming Historian en français* viennent du monde entier et travaillent au sein d'environnements culturels variés. Pour qu'un public international puisse être touché, un certain nombre de nos publications sont accessibles dans plus d'une langue depuis 2017. Nous avons également pour but de traduire tous nos tutoriels. **Comme nous reconnaissons que toutes les méthodes et outils ne sont pas pleinement accessibles à un public international**, les auteur(e)s peuvent et doivent écrire leurs leçons de façon à ce qu'elles soient accessibles à autant de personnes que possible. **Nous vous prions donc de bien vouloir respecter les conseils suivants lorsque vous écrivez votre tutoriel** :

- Lorsque vous choisissez vos méthodes et outils, essayez de les choisir en gardant à l'esprit que les tous les lecteurs et toutes les lectrices ne parlent pas tous et toutes la même langue. Cela est particulièrement important lorsque l'on travaille sur des méthodes d'analyse des textes, ou lorsque les utilisateurs et les utilisatrices souhaiteraient travailler avec des ensembles de caractères différents (par exemple, caractères accentués, non-latins, etc.).
- Quand vous choisissez des images et des sources primaires, quand vous produisez des illustrations, ou quand vous faites des copies d'écran, pensez à la manière dont celles-ci vont être vues par un public international.
- Au cours de la rédaction, évitez les plaisanteries, les références culturelles, les calembours, les jeux de mots, les expressions idiomatiques, le sarcasme, les emojis ou une syntaxe qui serait plus compliquée que nécessaire. Les mentions de personnes, d'organisations, ou de détails historiques doivent toujours être accompagnées d'informations contextuelles. Vous devez constamment penser au fait que vos lecteurs et lectrices ne vivent pas toujours dans le même pays que vous et qu'ils ne parlent pas la même langue.
- Dans les exemples de codes source ou les métadonnées, utilisez des formats standards, reconnus au niveau international, pour les dates et les heures ([ISO 8601:2004](https://www.iso.org/fr/standard/40874.html)). Dans votre texte, restez bien conscient(e) des différences culturelles existantes dans la représentations des dates et des heures. Ces différence pourraient en effet causer de la confusion.
- Quand cela est possible, choisissez des méthodes et des outils qui disposent de documentation multilingue. Dans le cas contraire, essayez d'ajouter, autant que faire se peut, des références multilingues à la fin de votre tutoriel.

Contactez le rédacteur ou la rédactrice en charge du suivi éditorial si vous avez besoin de conseils sur n'importe quel de ces points. Les tutoriels qui ne peuvent pas respecter ces consignes ne seront pas traduits, mais ils sont les bienvenus afin d'être envisagés pour une publication en une seule langue.

### Utiliser des en-têtes pour marquer le début d'une section
Nous nous efforçons de publier des leçons faciles à suivre, grâce à l'utilisation systématique d'en-têtes de section dans le corps des textes. Au moment où vous créez votre leçon, les en-têtes de section vont vous aider à visualiser et à vérifier la structure de cette dernière. Évitez les longues sections de texte sans en-têtes, celles-ci peuvent en effet devenir très difficiles à suivre.

**Ne rendez pas vos sections visibles** en mettant votre texte **en gras** ou en *italique*. Vous devez utilisez le niveau de titre approprié (que vous pouvez mettre en forme de manière systématique dans le corps du texte). À moins que votre leçon ne soit particulièrement courte, vous allez avoir besoin d'un moins 3 niveaux différents.

Bien qu'il y ait plusieurs manières de créer des en-têtes de section avec Markdown, nous vous demandons d'utiliser la notation `#` dans vos en-têtes. Le titre de premier niveau est indiqué avec \# ; le niveau de titre suivant avec \#\#, et ainsi de suite :

    # Titre 1
    ## Titre 2
    ### Titre 3
    #### Titre 4

Il apparaissent ainsi sur le site Internet :
# Titre 1
## Titre 2
### Titre 3
#### Titre 4
Si vous utilisez les en-têtes de section de manière adéquate, vous allez aussi aider les personnes chargées du suivi éditorial et de la relecture de votre leçon à en évaluer plus facilement la structure générale.

### Alertes
Si vous voulez attirer l'attention sur quelque chose qui n'est pas essentiel pour suivre votre leçon, mais qui est suffisamment important pour être mentionné (ou qui peut être utile pour une partie de votre lectorat), vous pouvez le dissocier du texte principal de votre leçon en utilisant notre [mise en forme d'alerte](https://v4-alpha.getbootstrap.com/components/alerts/) (emprunté à Bootstrap).

Pour ce faire, vous avez besoin d'utiliser du langage HTML de la façon suivante :

``` html
<div class="alert alert-warning">
  Assurez vous de suivre attentivement les consignes !
</div>
```
Sur le site web, le texte va se présenter ainsi :

<div class="alert alert-warning">
 Assurez vous de suivre attentivement les consignes !
</div>

### Règles de mise en forme spéciales
Comme n'importe quelle autre revue, le *Programming Historian en français* a lui aussi un style "maison" que les auteur(e)s doivent suivre pour garantir la cohérence des leçons. Mais, contrairement à d'autres revues, ne pas respecter ces règles de mise en forme peut avoir pour conséquence que vos leçons ne s'affichent pas correctement sur notre site web et qu'elles restent donc invisibles.

### Illustrations
Quels que soient leur longueur ou leur niveau de difficulté, toutes les leçons peuvent tirer avantage des images, particulièrement les copies d'écran qui illustrent ce que les lecteurs et lectrices doivent voir au fur et à mesure de leur avancée dans le tutoriel. Les captures d'écran permettent non seulement de savoir si une leçon nous intéresse d'un simple coup d'œil, mais elles servent également à rassurer les utilisateurs et les utilisatrices. Et, bien sûr, les images peuvent vous éviter de multiplier les longues descriptions dans votre texte.


#### Créer un dossier
Tout d'abord, créez un dossier dans lequel vous allez stocker tous vos fichiers images. Le nom du dossier doit être le même que le `SLUG-DE-LA-LEÇON` que vous avez choisi pour le nom de votre fichier. Le rédacteur ou la rédactrice responsable de votre leçon peut vous assister en téléchargeant vos images dans le dépôt `ph-submissions` au moment où vous soumettez votre leçon.

#### Utiliser des noms de fichiers compréhensibles
Il y a deux façons de nommer vos fichiers. Une option consiste à utiliser des noms de fichier cohérents, et sémantiquement signifiants, qui indiquent clairement ce sur quoi porte l'image. Une autre option consiste à les nommer de manière séquentielle, en utilisant le même "slug" de leçon (ou une abréviation si le "slug" est trop long), suivi par un chiffre indiquant de quelle illustration il s'agit. Par exemple :
`counting-frequencies-1.png`, `counting-frequencies-2.png`, et ainsi de suite.)

#### Utilisez des tailles et des formats standard
Assurez vous que les images sont des formats adaptés pour le Web, comme PNG ou JPEG, et dans des tailles appropriées (à la fois en termes de pixels et de bytes).

#### Inclure des images
À chaque fois que vous souhaitez insérer une image, utilisez la ligne de code suivante dans votre leçon :

{% raw %}
``` markdown
{% include figure.html filename="IMAGE-FILENAME" caption="VOTRE TITRE, AVEC \"CODE D'ÉCHAPPEMENT\" POUR LES GUILLEMETS" %}
```
{% endraw %}

Vous allez avoir besoin de renseigner le `NOM-DU-FICHIER-IMAGE` et la `Légende de l'image` en fonction de votre leçon et de l'image. Vous pouvez également avoir besoin d'utiliser du balisage Markdown pour la légende, par exemple pour mettre le texte en gras ou en italique.

Quand le Markdown est traité par notre système, cette ligne va automatiquement produire du HTML qui va ressembler à ceci :

``` html
<figure>
    <a href="/images/LEÇON-SLUG/NOM-DU-FICHIER-IMAGE">
       <img src="/images/LEÇON-SLUG/NOM-DU-FICHIER-IMAGE" alt="Légende de l'image">
    </a>
<figcaption>
    Légende de l'image
</figcaption>
</figure>
```

<div class="alert alert-warning">
 N'oubliez pas que les guillemets à l'intérieur des titres des figures doivent être échappés à l'aide d'une barre oblique inverse, comme dans l'exemple ci-dessus. Il est important de noter que, lorsque les images sont encodées de cette manière, elles ne sont pas visibles dans la pré-visualisation sur Github ou dans d'autres programmes de pré-visualisation pour Markdown mais que votre éditeur s'assurera qu'elles soient affichées correctement lorsque la leçon sera publiée.
</div>


### Notes de bas de page
Pour ajouter des notes de bas de page à votre texte, ajoutez un marqueur de la note dans le corps du texte de la façon suivante :

	Voilà du texte. [^1]Encore du texte. [^note de bas de page]

Comme vous pouvez le voir, le marqueur est entre crochets, et peut être composé de chiffres ou de lettres, du moment qu'il débute par le signe diacritique "accent circonflexe" (`^`)

Ensuite, vous devez préciser quel texte correspond au marqueur de la note, idéalement à la fin de votre fichier. Pour définir une note de bas de page, vous allez reproduire la syntaxe du marqueur, ajouter les deux-points, et taper la note de bas de page :

    [^1]: Une définition *idote* de la note

    [^endnote]: Regarde, j'ai fait une note de bas de page !

Pour en savoir plus sur la manière dont fonctionne cette syntaxe, regardez les [instructions complètes](http://kramdown.gettalong.org/syntax.html#footnotes) pour la fonctionnalité "note de bas de page".


### Blocs de code
Si vous voulez inclure du code source dans une leçon, ou si vous voulez montrer le résultat d'un programme informatique, utilisez ce que l'on appelle un *bloc de code*. Sur une nouvelle ligne, utilisez 3 accents graves (`` ` ``) pour ouvrir un bloc de code, suivi du langage de votre code (par exemple  `python` ou `html`). Ensuite collez votre code source, et quand vous avez terminé, fermez le bloc de code avec 3 accents graves.

	``` python
	print 'hello world'
	```
Le code sera visible en ligne de la façon suivante :
``` python
print 'hello world'
```

### Mettre en avant des parties du texte
Essayez d'utiliser les accents graves (`` ` `` ) pour afficher des lignes de codes dans le corps du texte et dans les noms de fichiers. Pour mettre en valeur d'autres types d'information, utilisez 2 astérisques (`* `) comme dans `*client*`, `*protocole*`, `*Le Old Bailey
Online*`).

-----

## Soumettre une nouvelle leçon
Une fois que votre leçon a été préparée en suivant les consignes données ci-dessus, nous vous conseillons de la faire relire et éventuellement d'apporter des corrections pour l'améliorer. Ainsi, l'évaluation ouverte par les pairs que nous allons organiser par la suite pourra se concentrer sur le fond, plutôt que sur la forme, afin de vous aider à produire la version la plus solide possible de votre leçon.   

Lorsque vous êtes prêt(e) à la soumettre, merci d'envoyer tous les fichiers (texte, images, données...) au rédacteur ou à la rédactrice en charge du suivi éditorial de votre leçon, qui les téléversera pour vous dans notre dépôt dédié à l'évaluation par les pairs sur [Github](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/fr/lecons). Voici comment procéder de votre côté: 

1. **Obtenir accès à notre dépôt d'évaluation**: pour cela il suffit de créer un [compte gratuit sur Github](https://github.com/join) et le communiquer à votre rédacteur ou rédactrice, qui va ensuite vous ajouter comme **collaborateur ou collaboratrice** dans le dépôt [ph-submissions]. Ce n'est pas à vous de faire le téléversement initial des fichiers, mais l'accès au dépôt est nécessaire pour que vous puissiez par la suite apporter des modifications et des mises à jour. 
2. **Préparer ses fichiers**: vous avez probablement des images qui accompagnent votre leçon. Merci de vérifier que tous les fichiers images sont nommés de manière appropriée, en accord avec les [conventions de nommage spécifiées ci-dessus]. Ces fichiers doivent nous parvenir dans un dossier unique compressé. Si vous avez en plus des fichiers de données, merci de nous envoyer ces fichiers aussi dans un dossier compressé distinct.
3. **Envoyer un message électronique**: informez votre rédacteur ou rédactrice que vous êtes prêt(e) à soumettre votre leçon, en joignant le fichier de celle-ci et, le cas échéant, les dossiers des fichiers images et données. 
4. **Participer à la discussion**: le rédacteur ou la rédactrice en charge du suivi éditorial de votre leçon déposera vos fichiers dans notre [dépôt de soumissions](https://github.com/programminghistorian/ph-submissions) en faisant quelques premières modifications si nécessaire (métadonnées, syntaxe Markdown etc). Ensuite, un ticket sera ouvert pour l'évaluation ouverte de votre leçon, pendant laquelle vous avez la possibilité d'échanger avec celles et ceux qui participent au processus.
5. **Apporter des modifications**: si le dépôt initial des fichiers est fait par votre rédacteur ou rédactrice assigné(e), le processus éditorial peut néanmoins entraîner le besoin d'apporter des modifications supplémentaires de votre côté. Toutes les révisions se font directement par les auteur(e)s sur les fichiers versés dans notre dépôt pour avoir la certitude que vous travaillez sur la version la plus récente du fichier de la leçon.


## Le processus de l'évaluation ouverte par les pairs
Une fois que votre rédacteur ou rédactrice assigné(e) aura déposé et formaté vos fichiers de manière appropriée, vous recevrez un lien de prévisualisation de la leçon qui vous permettra de vérifier aussi de votre côté que tout se présente correctement; si ce n'est pas le cas, vous pouvez apporter des corrections. 

L'évaluation par les pairs a lieu dans le cadre d'un [ticket](https://github.com/programminghistorian/ph-submissions/issues) Github qui prend ainsi la forme d'un forum de discussion ouverte. Merci de garder à l'esprit que l'évaluation par les pairs se fait publiquement et qu'elle reste disponible à la consultation publique; le ticket en est l'enregistrement. Si pour quelque raison que ce soit vous n'êtes pas à l'aise ou souhaitez une évaluation par les pairs non publique, merci de prendre contact avec votre rédacteur ou rédactrice assigné(e). 

Le processus de l'évaluation se passe habituellement en trois étapes:

1) Le rédacteur ou la rédactrice assigné(e) à votre leçon en fait une première lecture attentive en en testant les manipulations proposées. Vous êtes à ce stade susceptible de recevoir un premier retour qui pourrait solliciter votre réponse. L'objectif de ce premier retour est de se garantir la pertinence de votre leçon pour le lectorat du *Programming Historian en français* et qu'elle est fonctionnelle avant d'être proposée à l'évaluation externe. Vous avez normalement un mois pour répondre à cette première évaluation. 

2) Ensuite, votre rédacteur ou  rédactrice assigné(e) propose la leçon à l'évaluation formelle par les pairs. Cela implique l'invitation d'au moins deux évaluateurs ou évaluatrices externes, mais potentiellement aussi la participation d'une communauté plus large, car tout commentaire est bienvenu (pourvu que les règles de bonne conduite, explicités dans le ticket, soient observées). En général, nous accordons aux évaluateurs et évaluatrices un délai d'un mois pour fournir leurs commentaires, il peut néanmoins arriver que ce délai ne soit pas respecté pour des raisons indépendantes de la volonté des personnes impliquées au processus. Vous devez attendre l'ensemble des relectures et les instructions consécutives de votre rédacteur our rédactrice assigné(e) avant d'aller plus loin. Parfois il peut s'agir de simples suggestions d'apporter certaines modifications, mais il peut aussi être question de révisions majeures ou de repenser la leçon. Selon les évaluations des pairs et la nature des questions soulevées, il se peut que vous ayez à réviser le tutoriel plus qu'une fois. Toufois, votre rédacteur ou rédactrice assignée(e) veillera à ce que vous receviez une ligne directrice claire pour que la leçon soit publiée. Par ailleurs, il est toujours possible de retirer votre leçon du processus de l'évaluation, si tel est votre choix.   

3) Au bout de ce processus, si tous les critères sont remplis, votre rédacteur ou rédactrice assignée(e) donne le feu vert pour la publication. C'est ensuite au rédacteur ou à la rédactrice en chef de relire la leçon pour s'assurer de sa conformité aux consignes aux auteur(e)s et aux standards du *Programming Historian*. Parfois des révisions et des corrections supplémentaires peuvent être nécessaires à ce stade pour que la leçon puisse être publiée. Une fois que le rédacteur ou la rédactrice en chef juge la version révisée satisfaisante, la leçon peut être publiée. Votre rédacteur ou rédactrice assigné(e) vous fournira toute information nécessaire à ce stade. 

N'hésitez pas à consulter nos [consignes aux évaluateurs et évaluatrices](/fr/consignes-evaluateurs) afin de vous familiariser avec notre processus de révision et de publication.

Si jamais vous êtes dans l'incertitude sur comment procéder, n'hésitez pas à poster votre question sur le ticket d'évaluation, un membre de notre équipe vous apportera des réponses dans les délais les plus brefs possible. Nous faisons de notre mieux pour répondre au bout de quelques jours.


### Que se passe-t-il une fois votre leçon publiée?

Il nous arrive de recevoir des retours de notre lectorat nous signalant des erreurs dans nos leçons. Le cas échéant, notre assistante éditoriale va ouvrir un ticket sur GitHub pour confirmer si l'erreur signalée est due à une mauvaise manipulation de l'utilisateur ou de l'utilisatrice (modification du code, du jeu de données...) ou à un problème de la leçon. Dans ce dernier cas, notre assistante éditoriale va tester à nouveau la leçon et chercher une solution. Dans le cadre de ce processus de maintenance de nos leçons, nous pouvons être amenés à vous contacter aussi pour solliciter votre avis. Si une solution est impossible à trouver, nous proposerons de faire afficher un avertissement expliquant que certain(e)s de nos utilisateurs et utilisatrices pourraient rencontrer des problèmes. Lorsque cela est possible, l'avertissement devrait inclure des liens vers des ressources qui pourraient permettre aux utilisateurs et utilisatrices de trouver une solution.


### Nous interpeller

Notre équipe de bénévoles fait de son possible pour garantir l'évaluation rigoureuse, collégiale et efficace des auteur(e)s par les pairs. Toutefois, il peut y avoir des failles, c'est pourquoi nous souhaitons que les auteur(e)s nous aident à maintenir un haut niveau de service. Si, pour quelque raison que ce soit, vous estimez ne pas avoir été traité(e) correctement, ou ne comprenez pas trop quel est votre rôle ou ce qu’on attend de vous, ou encore si vous considérez que l'évaluation présente des retards injustifiés ou que quelqu'un a été rude avec vous, enfin, pour quel autre souci que ce soit, n'hésitez pas à nous en tenir informés afin que nous puissions agir. 

Exprimer des réserves n'a AUCUN impact négatif sur le processus et le résultat de l'évaluation par les pairs. 

Pour ce faire, vous avez plusieurs points d'entrée - sentez-vous libre de contacter la personne avec laquelle vous êtes le plus à l'aise: 

* votre rédacteur ou rédactrice assigné(e); 
* le rédacteur ou la rédactrice en chef;
* notre médiatrice indépendante ([Hélène Huet](mailto:hhuet@ufl.edu).

Nous oeuvrons pour que tout se passe au mieux pour vous, mais si jamais vous estimez vous trouver dans une situation peu confortable, nous vous remercions de nous aider à y remédier et à améliorer les choses. 





  [consignes aux évaluateurs et évaluatrices]: /fr/consignes-evaluateurs.html
  [leçons publiées]: /fr/lecons
  [TextWrangler]: http://www.barebones.com/products/textwrangler/
  [Notepad++]: https://notepad-plus-plus.org/
  [équipe-projet]: /fr/equipe-projet.html
  [slug]: https://en.wikipedia.org/wiki/Semantic_URL#Slug
  [YAML]: https://fr.wikipedia.org/wiki/YAML
  [guide de GitHub sur Markdown]: https://guides.github.com/features/mastering-markdown/
  [les bases de Markdown]: https://help.github.com/articles/markdown-basics
  [Github Flavored Markdown]: https://help.github.com/articles/github-flavored-markdown
  [le texte brut sur Github]: https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/en/author-guidelines.md
  [éléments fournis par HTML5]: http://html5doctor.com/the-figure-figcaption-elements/
  [exemple de pré-visualisation avec images ici]: https://github.com/programminghistorian/jekyll/commit/476f6d466d7dc4c36048954d2e1f309a597a4b87#diff-f61eee270fe5a122a0163ebf0e2f8725L28
  [version "live" ici]: /lessons/automated-downloading-with-wget#lesson-goals
  [tableau de syntaxe étendu]: http://kramdown.gettalong.org/syntax.html#tables
  [pandoc]: http://johnmacfarlane.net/pandoc/
  [fenced code blocks]: https://help.github.com/articles/github-flavored-markdown/#fenced-code-blocks
  [pull request]: https://help.github.com/articles/using-pull-requests/
  [GitHub pour Mac]: https://mac.github.com/
  [GitHub pour Windows]: https://windows.github.com/
  [créer un compte sur Github]: https://help.github.com/articles/signing-up-for-a-new-github-account/
  [conventions de nommage spécifiées ci-dessus]: #nommer-le-fichier
  [pull requests en attente dans notre dépôt]: https://github.com/programminghistorian/jekyll/pulls
  [guides GitHub]: https://guides.github.com/activities/forking/
  [réaliser un fork]: https://help.github.com/articles/fork-a-repo/
  [tutoriels indépendants]: https://gun.io/blog/how-to-github-fork-branch-and-pull-request/
  [Git pour les philosophes]: https://github.com/rzach/git4phi
  [GitHub Pages]: https://pages.github.com
  [ph-submissions]: https://github.com/programminghistorian/ph-submissions

  {% comment %}Anchor in line 306: Needs to be checked for: a) slug: does not seem to correspond to a subtitle, in the text there is only "Utilisez des noms de fichiers compréhensibles" b) where it is/will be inserted in the text{% endcomment %}
  {% comment %}Hopefully resolved after some changes. Sofia, 12/12/20{% endcomment %}

