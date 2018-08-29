---
title: Consignes aux auteur(e)s
layout: blank
redirect_from: 
 - /nouvelle-leçon-workflow
 - /consignes-auteurs
---

# Consignes aux auteur(e)s

<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />
<h2 class="noclear"> Étape 1 : <a href="#proposer-une-nouvelle-leçon">Proposer une nouvelle leçon</a></h2>
<h2 class="noclear">Étape 2 : <a href="#écrire-une-nouvelle-leçon">Écrire et mettre en forme une nouvelle leçon</a></h2>
<h2 class="noclear">Étape 3 : <a href="#soumettre-une-nouvelle-leçon">Soumettre une nouvelle leçon</a></h2>

## Proposer une nouvelle leçon
Si vous avez une idée pour une nouvelle leçon, ou si vous avez déjà rédigé un tutoriel qui, selon vous, pourrait être adapté au *Programming Historian en français*, contactez [Jessica Parr] pour discuter de votre idée. En prenant contact avec l'équipe au tout début du processus, il vous sera plus facile d'élaborer votre leçon -- et plus particulièrement d'identifier le lectorat cible et le niveau de compétence attendu - et de vous associer à l'éditeur(trice) le(a) plus expérimenté(e) sur les thèmes que vous abordez.

<div class="alert alert-success">
Nous acceptons des tutoriels :

 - pertinents pour les humanités, 
 - adaptés à n'importe quel niveau de compétence et d'expérience technique, 
 - concernant un problème ou un processus particulier, 
 - pérennes dans le long terme, 
 - et s'adressant à un public international. 

La portée et la longueur du tutoriel doivent être appropriés à la complexité de la tâche qui y est expliquée. La longueur des tutoriels ne doit pas excéder 8,000 mots (en incluant le code source) à moins que l'éditeur(trice) n'en ait explicitement donné la permission. Celle-ci sera uniquement accordée dans des circonstances exceptionnelles. Nous demandons que la longueur des leçons soit en général comprise entre 4,000 et 6,000 mots. Les leçons plus longues pourront être divisées en plusieurs tutoriels.
</div>

Vous pouvez avoir une meilleure idée de ce que nous publions en consultant nos [leçons publiées], en lisant nos [consignes aux relecteur(trice)s] ou en parcourant les [leçons en cours de développement](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lecons). Nous vous encourageons à proposer des leçons sur des sujets déjà traités ou en en cours de développement, à condition que la nouvelle leçon apporte sa propre contribution originale au traitement d'un sujet donné.

Afin d'assurer la pérennité de nos leçons, les auteur(e)s doivent s'efforcer de soumettre des leçons qui ne sont pas complètement dépendantes de logiciels spécifiques ou d'interfaces utilisateurs. Ces leçons vont à coup sûr souffrir d'instabilité, et vont avoir besoin de révisions substantielles lorsque sort une nouvelle version du logiciel ou de l'interface. Enseigner des concepts, plutôt que demander de 'cliquer sur le bouton _x_', facilite la rédaction et la publication de tutoriels pérennes.

Une fois que votre proposition est acceptée, un(e) éditeur(trice) va créer un ticket "Proposition" dans notre [dépôt de soumissions](https://github.com/programminghistorian/ph-submissions/issues) avec le titre provisoire de la leçon et les objectifs pédagogiques proposés. Ce ticket sert à signaler le travail en cours alors que vous êtes en train de rédiger votre leçon. Pour éviter d'accumuler les retards, nous vous demandons de soumettre votre leçon dans les 90 jours suivants l'acceptation de votre proposition.

-----

## Writing a New Lesson
Écrire une nouvelle leçon
Le *Programming Historian en français* est hébergé par [GitHub](http://github.com), qui est plateforme gratuite permettant de sauvegarder des fichiers et de suivre l'historique de leurs révisions. La plupart du temps, Github est utilisé pour stocker des fichiers de code de programmation, mais c'est aussi une excellente solution pour maintenir une ressource en libre accès comme le *Programming Historian en français*. Plus spécifiquement, notre site utilise [GitHub Pages] pour traiter un ensemble de fichiers de texte brut et les transformer en un site internet élégant.

Cela signifie que nous demandons aux auteur(e)s de respecter les consignes détaillées ci-dessous pour écrire leurs leçons. Celles-ci sont non seulement stylistiques, mais aussi nécessaires pour assurer le bon fonctionnement de notre plateforme de publication. Si nos exigences vous semble difficiles à respecter, **nous sommes là pour vous aider à vous familiariser avec le processus de publication, et à apprendre à utiliser, au fur et à mesure de vos avancées, les technologies nécessaires**.

Gardez à l'esprit que ce projet est basé sur le volontariat, et que nous avons donc besoin que vous fassiez bien attention à tous ces détails.

### Utilisez le texte brut
Parce que notre site est hébergé avec [GitHub Pages](https://pages.github.com), **votre leçon doit être écrite en texte brut**, en utilisant un éditeur de texte de votre choix. *Les éditeurs de texte se distinguent clairement des traitements de texte traditionnels comme Microsoft Word*. Nous recommandons d'utiliser [Atom](https://atom.io/), qui est disponible sous Mac ou Windows. Les utilisateurs de Mac peuvent également envisager d'utiliser [TextWrangler] ou TextEdit (qui est fourni avec macOS). Les utilisateurs de Windows peuvent envisager d'utiliser [Notepad++].

Si le choix de l'éditeur n'a pas vraiment d'importance, vous devriez toutefois écrire dès le départ votre leçon en texte brut pour éviter des frustrations dans le futur. Par exemple, les guillemets insérés automatiquement par Word crée des problèmes de formatage difficiles à débugger. 

### Format des notes de bas de page
Nous demandons aux auteur(e)s de bien vouloir utiliser le style [Chicago Manual of Style](https://fr.wikipedia.org/wiki/The_Chicago_Manual_of_Style) pour mettre en forme les notes de bas de page.

### Choisissez un nom facile à trouver
Appelez le fichier de votre nouvelle leçon en respectant les conseils suivants :

-   Utilisez des minuscules et choisissez un nom court mais parlant. Ce nom de fichier deviendra le [slug] de l'URL de la leçon quand elle sera publiée. Par exemple, le titre de la leçon intitulée "Débuter avec Markdown" a le slug suivant : `débuter-avec-markdown` et l'URL : `https://programminghistorian.org/en/lessons/débuter-avec-markdown`. Pensez à regarder des leçons existantes pour plus d'exemples concrets.
-   Votre "slug" sera référencé plus tard de la manière suivante LEÇON-SLUG. 
-   Pensez à la manière dont des lecteur(trice)s potentiel(le)s pourraient chercher quelque chose de similaire à votre leçon. Un "slug" riche de mots-clé est une bonne manière de capter le trafic des moteurs de recherche.
-   N'utilisez pas d'espaces ou de tirets bas `(_)` dans le nom du fichier ; utilisez plutôt les tirets haut `(-)`.
-   L'extension du nom du fichier doit être `.md` (markdown).


### AAjoutez des métadonnées
Notre plateforme de publication, [GitHub Pages], dépend d'en-têtes spéciales, qui doivent être insérées dans chaque fichier de leçon en texte brut. Ces en-têtes sont appelées blocs liminaires [YAML], et c'est grâce à elles que la leçon s'affiche correctement sur notre site internet. Ces blocs consistent en des champs (comme "titre" et "auteurs") appariés avec des valeurs (comme "Fouiller les données dans l'Internet Archive Collection" et "Caleb McDaniel"). Vous n'avez pas besoin de comprendre en quoi consiste YAML et comment cela fonctionne, mais **vous devez inclure un bloc YAML au début de votre leçon**.

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


### Écrivez en Markdown
**Toutes les nouvelles leçons doivent être écrites en Markdown.** Markdown est un langage de balisage que l'on écrit très facilement avec un éditeur de texte (comme expliqué ci-dessus, n'utilisez pas un traitement de texte comme Word ou Open Office).  Les [GitHub Pages] sont générées par [Jekyll](http://jekyllrb.com/), qui convertit automatiquement les fichiers Markdown dans des pages HTML que vous pouvez trouver sur le site Web. Cette page est elle-même écrite en Markdown, comme vous pouvez le voir en regardant [le texte brut sur Github].

Pour une introduction en douceur à Markdown, consultez:
- [Débuter avec Markdown]({{site.baseurl}}/leçons/débuter-avec-markdown), un tutoriel du *Programming Historian* écrit par Sarah Simpkin
- ou le guide [GitHub Guide to Markdown].

<div class="alert alert-warning">
  Avant de continuer, assurez vous que vous comprenez comment utiliser la syntaxe Markdown pour du formatage basique comme la mise en valeur des en-têtes, la mise en gras du texte, l'utilisation de l'italique, l'ajout de liens, la mise en forme des paragraphes, et la création de listes.
</div>

### Écrivez de manière durable
Le *Programming Historian en français* s'efforce de publier des leçons qui sont utiles à nos lecteur(trice)s dans l'immédiat. Les auteur(e)s doivent consulter notre [politique de retrait des leçons]({{site.baseurl}}/politique-retrait-leçons), qui décrit comment l'équipe éditoriale du *Programming Historian en français* gère les leçons qui sont devenues obsolètes. Pour assurer la création de leçons pérennes, nous vous demandons de garder à l'esprit un certain nombre de consignes lors de la rédaction :

- Au lieu de vous concentrer sur des logiciels en particulier, axez de préférence votre leçon sur les méthodologies, et sur une présentation plus générale des outils.
- Si votre leçon peut tirer profit de la documentation d'un logiciel existant, envisagez de diriger vos lecteur(trice)s vers cette documentation plutôt que de la répéter dans votre leçon. Et au lieu d'ajouter un lien vers les ressources concernant un logiciel développé par une entreprise - ressources qui, en général, changent très souvent -, vous pouvez fournir des conseils généraux sur la manière dont vos lecteur(rice)s peuvent trouver la documentation. 
- Limitez l'usage d'images spécifiques à la version du logiciel présenté, à moins que cela ne soit requis pour suivre votre leçon.
- Vérifiez tous les liens externes de façon à vous assurez qu'ils sont à jour.
- Les données nécessaires pour suivre une leçon doivent être hébergées avec notre site Internet.


### Écrivez pour un public international

Les lecteur(trice)s du *Programming Historian en français* viennent du monde entier, et travaillent au sein d'environnements culturels variés. Pour qu'un public international puisse être touché, un certain nombre de nos publications sont accessibles dans plus d'une langue depuis 2017. Nous avons également pour but de traduire tous nos tutoriels. **Comme nous reconnaissons que toutes les méthodes et outils ne sont pas pleinement accessibles à un public international**, les auteur(e)s peuvent et doivent écrire leurs leçons de façon à ce qu'elles soient accessibles à autant de personnes que possible. **Nous vous donc de bien vouloir respecter les conseils suivants lorsque vous écrivez votre tutoriel** :

- Lorsque vous choisissez vos méthodes et outils, essayez de les choisir en gardant à l'esprit que les tous les lecteurs et lectrices ne parlent pas tous et toutes la même langue. Cela est particulièrement important lorsque l'on travaille sur des méthodes d'analyse des textes, ou lorsque les utilisateur(trice)s souhaiteraient travailler avec des ensembles de caractères différents (par exemple, caractères accentués, non-latins, etc.).
- Quand vous choisissez des images et des sources primaires, quand vous produisez des illustrations, ou quand vous faites des copies d'écran, pensez à la manière dont ils vont être vus par un public international. 
- Au cours de la rédaction, évitez les plaisanteries, les références culturelles, les calembours, les jeux de mots, les expressions idiomatiques, le sarcasme, les emojis ou une syntaxe qui serait plus compliquée que nécessaire. Les mentions de personnes, d'organisations, ou de détails historiques doivent toujours être accompagnées d'informations contextuelles. Vous devez constamment penser au fait que vos lecteur(trice)s ne vivent pas toujours dans le même pays que vous, et qu'ils ne parlent pas la même langue.
- Dans les exemples de codes source ou les métadonnées, utilisez des formats standards, reconnus au niveau international, pour les dates et les heures ([ISO 8601:2004](https://www.iso.org/fr/standard/40874.html)). Dans votre texte, restez bien conscients des différences culturelles existantes dans la représentations des dates et des heures. Ces différence pourraient en effet causer de la confusion.
- Quand cela est possible, choisissez des méthodes et des outils qui disposent de documentation multilingue. Dans le cas contraire, essayez d'ajouter, autant que faire se peut, des références multilingues à la fin de votre tutoriel. 

Contactez votre éditeur(trice) si vous avez besoin de conseils sur n'importe quel de ces points. Les tutoriels qui ne peuvent pas respecter ces consignes ne seront pas traduits, mais ils sont les bienvenus afin d'être envisagés pour une publication en une seule langue.

### Utilisez des en-têtes pour marquer le début d'une section
Nous nous efforçons de publier des leçons faciles à suivre, grâce à l'utilisation systématique d'en-têtes de section dans le corps des textes. Au moment où vous créez votre leçon, les en-têtes de section vont vous aider à visualiser et à vérifier la structure de celle-ci. Éviter les longues sections de texte sans en-têtes ; celles-ci peuvent en effet devenir très difficiles à suivre.

**Ne rendez pas vos sections visibles** en mettant votre texte **en gras** ou en *italique*. Vous devez utilisez le niveau de titre approprié (que vous pouvez mettre en forme de manière systématique dans le corps du texte). À moins que votre leçon ne soit particulièrement courte, vous allez avoir besoin d'un moins 3 niveaux différents.

Bien qu'il y ait plusieurs manières de créer des en-têtes de section avec Markdown, nous vous demandons d'utiliser la notation `#` dans vos en-têtes. Le titre de premier niveau est indiqué avec \# ; le niveau de titre suivant avec \#\#, et ainsi de suite :

    # Titre 1
    ## Titre 2
    ### Titre 3
    #### Titre 4

Il apparaissent ainsi en ligne :
# Titre 1
## Titre 2
### Titre 3
#### Titre 4
Si vous utilisez les en-têtes de section de manière adéquate, vous allez aussi aider les éditeur(trice)s et les relecteur(trice)s à évaluer plus facilement la structure générale de votre leçon ou traduction.

### Alertes
Si vous voulez attirer l'attention sur quelque chose qui n'est pas essentiel pour suivre votre leçon, mais qui est suffisamment important pour être mentionné (ou qui peut être utile pour certain de vos lecteur(trice)s), vous pouvez le dissocier du texte principal de votre leçon en utilisant notre [mise en forme d'alerte](https://v4-alpha.getbootstrap.com/components/alerts/) (emprunté à Bootstrap).

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
Comme n'importe quel autre journal, le *Programming Historian en français* a lui aussi un style "maison" que les auteurs doivent suivre pour garantir la cohérence des leçons. Mais contrairement à d'autres journaux, ne pas respecter ces règles de mise en forme peut avoir pour conséquence que vos leçons ne s'affichent pas correctement sur notre site web, et qu'elles restent donc invisibles.

### Illustrations
Quels que soient leur longueur ou leur niveau de difficulté, toutes les leçons peuvent tirer avantage des images, particulièrement les copies d'écran qui illustrent ce que les lecteur(trice)s doivent voir au fur et à mesure de leur avancée dans le tutoriel. Les captures d'écran permettent non seulement de savoir si une leçon nous intéresse d'un simple coup d'œil, mais elles aident également les utilisateur(trice)s à savoir s'il(elle)s font la bonne chose. Et bien sûr les images peuvent vous éviter de multiplier les longues descriptions dans votre texte.


#### Créer un dossier
Tout d'abord, créez un dossier dans lequel vous allez stocker tous vos fichiers images. Le nom du dossier doit être le même que le `LEÇON-SLUG` que vous avez choisi pour le nom de votre fichier. L'éditeur(trice) assigné(e) à votre leçon peut vous assister en téléchargeant vos images dans le dépôt `ph-submissions` au moment où vous soumettez votre leçon.

#### Utilisez des noms de fichiers compréhensibles 
Il y a deux façons de nommer vos fichiers. Une option consiste à utiliser des noms de fichier cohérents, et sémantiquement signifiants, qui indiquent clairement ce sur quoi porte l'image. Une autre option consiste à les nommer de manière séquentielle, en utilisant le même "slug" de leçon (ou une abréviation si le "slug" est trop long), suivi par un chiffre indiquant de quelle illustration il s'agit. Par exemple :
`counting-frequencies-1.png`, `counting-frequencies-2.png`, et ainsi de suite.)

#### Utilisez des tailles et des formats standard
Assurez vous que les images sont des formats adaptés pour le Web, comme PNG ou JPEG, et dans des tailles appropriées (à la fois en termes de pixels et de bytes).

#### Inclure des images
À chaque fois que vous souhaitez insérer une image, utilisez la ligne de code suivante dans votre leçon :

{% raw %}
``` markdown
{% include figure.html filename="IMAGE-FILENAME" caption="Caption to image" %}
```
{% endraw %}

Vous allez avoir besoin de renseigner le `NOM-DU-FICHIER-IMAGE` et la `Légende de l'image` en fonction de votre leçon et de l'image. Vous pouvez également avoir besoin d'utiliser du balisage Markdown pour la légende, par exemple pour mettre le texte en gras ou en italique.

Quand le Markdown est traité par notre system, cette ligne va automatiquement produire du HTML qui va ressembler à ceci :

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
 Il est important de noter que lorsque les images sont encodées de cette manière, elles ne sont pas visibles dans la pré-visualisation sur Github ou dans d'autres programmes de pré-visualisation pour Markdown.
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
Une fois que votre leçon a été préparée en suivant les consignes données ci-dessus, vous êtes prêt(e) à la soumettre !

Nous avons une [page-projet pour le Programming Historian](https://github.com/programminghistorian) sur GitHub, où nous maintenons deux dépôts (un dépôt ou *repository* est un endroit destiné à stocker les fichiers et les dossiers reliés - on peut les voir comme les dossiers que vous avez sur votre ordinateur). L'un d'entre eux s'appelle [jekyll](https://github.com/programminghistorian/jekyll), et héberge le code source du site visible à cette adresse <http://programminghistorian.org/fr/>. L'autre dépôt s'appelle [ph-submissions].

Nous souhaitons que les auteurs soumettent directement les leçons en les ajoutant au dépôt [ph-submissions]. Grâce aux fonctionnalités offertes par Github, vous pouvez utiliser l'action *glisser-déposer* pour télécharger des fichiers. En tant que nouvel auteur, voilà les étapes que vous allez devoir suivre :

1. Créer un [compte gratuit sur Github](https://github.com/join). Cela prend environ 30 secondes.
2. Envoyez un message à votre éditeur(trice) avec votre nouveau nom d'utilisateur(trice) Github et le nom/slug du fichier de votre leçon (assurez vous d'avoir suivi les règles de nommage exposées ci-dessus). L'éditeur va ensuite vous ajouter comme **collaborateur(trice)** dans le dépôt [ph-submissions]. Une fois que vous avez accès au dépôt en tant que collaborateur(trice), vous allez alors pouvoir directement faire des changements dans le dépôt [ph-submissions], comme ajouter, éditer, supprimer ou renommer des fichiers. L'éditeur(trice) va également créer un dossier avec le même nom que votre leçon dans le dossier "images". (Si vous avez d'autres types de fichiers de données que vous souhaitez associer à votre tutoriel, parlez en à votre éditeur(trice).
3. Une fois que votre éditeur(trice) vous a informé que vous avez été ajouté(e) en tant que collaborateur(trice) au dépôt, rendez vous dans le [dossier des leçons](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons) du dépôt [ph-submissions]. Ensuite, faites un glisser-déposer avec votre fichier en Markdown depuis votre ordinateur vers la fenêtre de votre navigateur. (Si vous avez besoin d'aide, consultez les [instructions fournies par Github](https://help.github.com/articles/adding-a-file-to-a-repository/)). Maintenant cliquez sur le bouton vert "Commit Changes" ; vous n'avez pas besoin de changer le message qui s'affiche par défaut.
4. Vous avez probablement des images qui accompagnent votre leçon. Soyez sûr(e) que tous les fichiers images sont nommés de manière appropriée, en accord avec les conventions de nommage spécifiées ci-dessus. Rendez vous dans le [dossier des images](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images) dans le dépôt [ph-submissions]. Cliquez sur le dossier avec le même nom que votre leçon (que votre éditeur(trice) a dû créer pour vous ; si vous ne le voyez pas, prenez contact avec votre éditeur(trice) et attendez de recevoir ses instructions). Une fois que vous êtes dans le bon dossier, faites un glisser-déposer de tous vos fichiers images de votre ordinateur vers la fenêtre de votre navigateur, comme vous l'avez fait lors de l'étape 3. Vous ne pouvez pas déposer un dossier contenant vos images ; mais vous pouvez déposer plusieurs fichiers en une fois.
5. Vous pouvez avoir un aperçu de votre leçon en ligne ! Attendez quelques minutes (voire moins) pour que Github convertisse votre fichier Markdown en HTML et en fasse une page web visible en ligne. Ensuite, rendez vous à l'adresse suivante : `http://programminghistorian.github.io/ph-submissions/lessons/NOM-DE-VOTRE-LEÇON` (mais remplacez NOM-DE-VOTRE-LEÇON par le nom de votre fichier).
6. Faites savoir à votre éditeur(trice) que vous avez téléchargé les fichiers de votre leçon dans le dépôt [ph-submissions] (il(elle) devrait recevoir une notification l'en informant ; mais nous préférons nous assurer que rien ne peut être omis). 

<div class="alert alert-info">
  Si vous avez l'habitude d'utiliser git et Github en ligne de commande, vous pouvez également soumettre votre leçon et vos images comme une *pull request* au dépôt `ph-submission` et la fusionner vous-même après y avoir été ajouté en tant que collaborateur(trice) <b> Nous vous demandons de ne pas soumettre des leçons par  [pull request] au dépôt principal Jekyll</b> de manière à ce que nous puissions fournir des aperçus en ligne des leçons en cours de relecture.
</div>

## La leçon a été soumise ! Et maintenant ?
Pour savoir ce qui va arriver à votre leçon après sa soumission, sentez-vous libre de consulter nos [consignes aux relecteur(trice)s](/consignes-relecteur), qui détaillent notre processus de révision et de publication. Vous pouvez retrouver les étapes les plus importantes ci-dessous.

L'étape la plus immédiate consiste en la création par votre éditeur(trice) d'une [issue](https://github.com/programminghistorian/ph-submissions/issues) pour la leçon téléchargée dans le dépôt [ph-submissions], contenant un lien vers votre leçon (dont vous avez pu avoir un aperçu lors de l'étape 5). L'éditeur(trice) et au moins deux relecteur(trice)s invité(e)s par l'éditeur(trice) vont poster leurs commentaires pour cette "issue".

### Attendez les commentaires des relecteur(trice)s
Nous essayons de finaliser le processus de relecture dans un délai de quatre semaines ; mais il peut parfois arriver que nous prenions du retard, ou que les personnes impliquées dans le processus de relecture soient très occupées, et cela peut prendre plus de temps que prévu.

Afin de promouvoir l'évaluation ouverte par les pairs et le développement d'un environnement académique ouvert, nous encourageons les discussions à rester sur Github. Toutefois, nous souhaitons également que vous vous sentiez à l'aise avec le processus de relecture ; sentez vous libre d'[envoyer directement un message à votre éditeur(trice)](/équipe-projet), ou de contacter notre médiatrice dédiée, [Amanda Visconti](/équipe-projet)..


### Répondez aux commentaires
Votre éditeur(trice) et vos relecteur(trice)s vont très probablement vous suggérer des modifications sur "l'issue" concernant votre leçon. L'éditeur(trice) vous dira clairement quelles sont les modifications indispensables, quelles sont les modifications optionnelles, et quelles modifications peuvent être mises de côté.

Vous pouvez éditer vos fichiers sur Github, en suivant [ces instructions](https://help.github.com/articles/editing-files-in-your-repository/).

Vos révisions doivent être finalisées sous 4 semaines après avoir reçu les consignes de votre éditeur(trice) concernant les réponses à donner à la suite de l'évaluation par les pairs. Il s'agit de s'assurer ainsi que les leçons sont publiées dans un délai convenable et ne prennent pas du retard inutilement. Si vous pensez que vous allez avoir des difficultés à respecter ce délai, vous devez contacter votre éditeur(trice) pour choisir une date plus appropriée.

Si, à n'importe quel moment, vous n'êtes pas sûr(e) de votre rôle ou de ce que l'on attend de vous, sentez vous libre d'envoyer un message à votre éditeur(trice) ou, encore mieux, de poster votre question sur l'issue concernant votre leçon (un(e) autre éditeur(trice) peut la voir et vous répondre à la place de votre éditeur(trice)). Vous devez comprendre que nous pouvons prendre quelques jours pour vous répondre, mais nous espérons que les améliorations apportées à votre leçon sauront récompenser votre patience.

### Faites savoir à votre éditeur(trice) que vous avez terminé
Une fois que vous avez terminé de répondre aux commentaires, faites le savoir à votre éditeur(trice). Si vous ne l'avez pas déjà fait, envoyez 2 ou 3 lignes de biographie, qui apparaîtront à la fin de votre leçon, suivant ainsi le modèle des autres leçons.

Ensuite, le comité éditorial du *Programming Historian en français* va rapidement relire votre leçon et la déplacer du dépôt `ph-submissions` vers le dépôt `jekyll`, et mettre à jour notre répertoire des leçons.

Félicitations ! Vous avez publié une leçon pour le *Programming Historian en français*!


   [Jessica Parr]: mailto:jparr1129@gmail.com
  [page wiki des leçons en cours de développement]: https://github.com/programminghistorian/jekyll/wiki/Lesson-Pipeline
  [consignes aux relecteur(trice)s]: /consignes-relecteurs.html
  [leçons publiées]: /leçons
  [TextWrangler]: http://www.barebones.com/products/textwrangler/
  [Notepad++]: https://notepad-plus-plus.org/
  [équipe-projet]: /équipe-projet.html
  [slug]: https://en.wikipedia.org/wiki/Semantic_URL#Slug
  [YAML]: https://fr.wikipedia.org/wiki/YAML
  [Guide GitHub pour Markdown]: https://guides.github.com/features/mastering-markdown/
  [les bases de Markdown]: https://help.github.com/articles/markdown-basics
  [Github Flavored Markdown]: https://help.github.com/articles/github-flavored-markdown
  [le texte brut sur Github]: https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/author-guidelines.md
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
  [conventions de nommage décrites ci-dessus]: #choisissez-le-nom-de-vos-fichiers
  [pull requests en attente dans notre dépôt]: https://github.com/programminghistorian/jekyll/pulls
  [guides GitHub]: https://guides.github.com/activities/forking/
  [réaliser un fork]: https://help.github.com/articles/fork-a-repo/
  [tutoriels indépendants]: https://gun.io/blog/how-to-github-fork-branch-and-pull-request/
  [Git pour les philosophes]: https://github.com/rzach/git4phi
  [GitHub Pages]: https://pages.github.com
  [ph-submissions]: https://github.com/programminghistorian/ph-submissions

