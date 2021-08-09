---
title: Une introduction aux Bots Twitter avec Tracery
doi: 10.46430/phfr0010
layout: lesson
slug: intro-aux-bots-twitter
authors:
- Shawn Graham
date: 2017-08-29
reviewers:
- Lee Skallerup Bessette
- Adam Crymble
- Nick Ruest
editors:
- Jessica Parr
translator:
- Géraldine Castel
translation-editor:
- Sofia Papastamkou
translation-reviewer:
- Antoine Courtin
- Sylvain Machefert
- Alix Chagué
translation_date: 2020-05-09
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/256
activity: presenting
topics: [api]
abstract: "Cette leçon explique comment créer de simples bots Twitter à l'aide de la grammaire Tracery et du service Cheap Bots Done Quick. Tracery est interopérable avec plusieurs langages de programmation et peut être intégrée dans des sites web, des jeux ou des bots."
original: intro-to-twitterbots
avatar_alt: Appareil à plusieurs mécanismes interconnectés

---

# Une introduction aux bots Twitter avec Tracery

Cette leçon explique comment créer des bots basiques sur Twitter à l’aide de la [grammaire générative Tracery](http://tracery.io) et du service [Cheap Bots Done Quick](http://cheapbotsdonequick.com/). Tracery est interopérable avec plusieurs langages de programmation et peut être intégrée dans des sites web, des jeux ou des bots. Vous pouvez en faire une copie (fork) sur github [ici](https://github.com/galaxykate/tracery/tree/tracery2).

## Pourquoi des bots?
Pour être exact, un bot Twitter est un logiciel permettant de contrôler automatiquement un compte Twitter. Lorsque des centaines de bots sont créés et tweetent plus ou moins le même message, ils peuvent façonner le discours sur Twitter, ce qui influence ensuite le discours d’autres médias. Des bots de ce type [peuvent même être perçus comme des sources crédibles d’information](http://www.sciencedirect.com/science/article/pii/S0747563213003129). Des projets tels que [Documenting the Now](http://www.docnow.io/) mettent au point des outils qui permettent aux chercheur(e)s de créer et d’interroger des archives de réseaux sociaux en ligne à propos d’événements récents qui comprennent très probablement un bon nombre de messages générés par des bots. Dans ce tutoriel, je veux montrer comment construire un bot Twitter basique afin que des historiens et des historiennes, ayant connaissance de leur fonctionnement, puissent plus facilement les repérer dans des archives et, peut-être, même les neutraliser grâce à leurs propres bots.

Mais je crois aussi qu’il y a de la place en histoire et dans les humanités numériques de façon plus large pour un travail créatif, expressif, voire artistique. Les historiens et les historiennes qui connaissent la programmation peuvent profiter des possibilités offertes par les médias numériques pour monter des créations, autrement impossibles à réaliser pour nous émouvoir, nous inspirer, nous interpeller. Il y a de la place pour de la satire, il y a de la place pour commenter. Comme Mark Sample, je crois qu’il y a besoin de &laquo; [bots de conviction](https://medium.com/@samplereality/a-protest-bot-is-a-bot-so-specific-you-cant-mistake-it-for-bullshit-90fe10b7fbaa)&raquo;.
Ce sont des bots de contestation, des bots si pointus et pertinents, qu’il devient impossible de les prendre pour autre chose par erreur. Selon Sample, il faudrait que de tels bots soient:

- **d’actualité**: &laquo; Ils traitent les informations du matin et les horreurs qui ne font pas la une des journaux &raquo;.

- **factuels**: &laquo; Ils s’appuient sur de la recherche, des statistiques, des tableurs, des bases de données. Les bots n’ont pas de subconscient. S’ils utilisent des images, elles sont à prendre au pied de la lettre &raquo;.

- **cumulatifs**: &laquo; La répétition s’auto-alimente, le bot reprend le même air encore et encore, imperturbable et inébranlable, empilant les débris sur nos écrans &raquo;.

- **partisans**: &laquo; Les bots de contestation sont engagés. La société étant ce qu’elle est, ce parti pris sera probablement mal vu, peut-être même déstabilisant &raquo;.

- **déroutants**:&laquo; La révélation de ce que nous voulions dissimuler &raquo;.

J'aimerais voir plus de bots de contestation, des bots nous plaçant face à des vérités implacables et qui, dans leur persévérance dépourvue d'humanité, réclament justice. [_Every 3 minutes_](https://twitter.com/Every3Minutes) de Caleb McDaniel nous fait honte en nous rappelant sans cesse que toutes les trois minutes, un être humain était vendu en esclavage dans le Sud des États-Unis avant la guerre civile.

{% include figure.html filename="bot-lesson-every3minutes.png" caption="Capture d'écran de la page Twitter du bot Every3Minutes" %}

_À lui tout seul, every3minutes justifie la création d’un bot en histoire_.

Pour entamer la réflexion, voici quelques suggestions de personnes qui m’ont répondu sur Twitter lorsque j’ai demandé à quoi pourraient ressembler des bots de conviction en histoire et archéologie:

> - un bot qui tweeterait des images en haute résolution issues du patrimoine culturel rendues inaccessibles par des visionneuses en mosaïque et des appropriations de droits d’auteur frauduleuses de la part des institutions où elles se trouvent ?
— Ryan Baumann (@ryanfb) 22 avril 2017

> - un bot qui tweeterait des images de lieux sacrés amérindiens profanés au nom de la cupidité des entreprises.
— Cory Taylor (@CoryTaylor_) 22 avril 2017

> - un bot qui référencerait les actifs historiques bénéficiant d’une exemption d’impôt sur la succession car supposés être « accessibles » au public
— Sarah Saunders (@Tick_Tax) 22 avril 2017

> - un bot qui tweeterait le nom d’esclaves ayant appartenu à des universités prestigieuses ou ayant participé à la construction de bâtiments gouvernementaux tels que la Maison blanche.
— Cory Taylor (@CoryTaylor_) 22 avril 2017

> - à chaque fois que quelqu’un dirait « depuis la nuit des temps, les humains ont », un bot qui répondrait automatiquement CONNERIES.
— Colleen Morgan (@clmorgan) 22 avril 2017

> - un bot qui imaginerait la réaction d’Afghans, d’Irakiens, de Syriens, de Yéménites lorsque des membres de leur famille sont tués dans des attaques de drones.
— Cory Taylor (@CoryTaylor_) 22 avril 2017

Dans la mesure où beaucoup de données historiques en ligne sont disponibles en format [JSON](http://json.org/), en cherchant un peu, vous devriez en trouver à utiliser avec votre bot.

Ma méthode est celle du bricoleur qui adapte et assemble des morceaux de code trouvés ici et là. En vérité, la programmation fonctionne en grande partie comme ça. Il existe beaucoup de logiciels pour interagir avec l’API (*Application Programming Interface* soit l'interface de programmation d'application) de Twitter. Dans cette leçon, il y aura peu de &laquo; programmation &raquo;: les bots ne seront pas écrits en Python, par exemple. Dans cette leçon d’introduction, je vais vous montrer comment construire un bot qui raconte des histoires, qui compose de la poésie, qui fait des choses merveilleuses à l’aide de [Tracery.io](http://tracery.io/) comme _grammaire générative_ et du service Cheap Bots Done Quick comme hébergeur du bot. Pour davantage de tutoriels pour apprendre à construire et héberger des bots Twitter sur d’autres services, voir [la liste de tutoriels de Botwiki](https://botwiki.org/tutorials/twitterbots/) (en anglais).

Celui de mes bots qui a connu le plus de succès est [@tinyarchae](http://twitter.com/tinyarchae), un bot qui tweete des scènes de dysfonctionnements au sein d’un horrible projet d’excavation archéologique. Tout projet archéologique est confronté à des problèmes de sexisme, d’insultes, de mauvaise foi. Ainsi, @tinyarchae prend tout ce qui se murmure dans les colloques et le pousse à l’extrême. C’est, en réalité, une caricature qui comporte une part de vérité embarrassante. D’autres bots que j’ai construits détournent de la [photographie archéologique](https://twitter.com/archaeoglitch); l’un est même utile puisqu’il [annonce la sortie de nouveaux articles de revues en archéologie](https://twitter.com/botarchaeo) et fait donc office d’assistant de recherche. Pour plus de réflexions sur le rôle joué par les bots en archéologie publique, voir ce [discours inaugural](https://electricarchaeology.ca/2017/04/27/bots-of-archaeology-machines-writing-public-archaeology/) tiré du [colloque Twitter sur l’archéologie publique](http://web.archive.org/web/20180131161516/https://publicarchaeologyconference.wordpress.com/)).

# Préparation : que fera votre bot ?

Commençons avec un bloc-notes et du papier. À l'école primaire, une activité que nous faisions souvent pour apprendre les bases de la grammaire anglaise s'appelait &laquo; mad-libs &raquo; (des improvisations un peu folles). L'enseignant en charge de l’activité demandait par exemple à la classe de donner un nom, puis un adverbe, puis un verbe, puis un autre adverbe. Puis, de l'autre côté de la feuille, il y avait une histoire avec des espaces vides du type :

"Susie la \_nom\_ était \_adverbe\_ mais elle \_verbe\_ \_adverbe\_."

et les élèves remplissaient les blancs comme demandé. C'était un peu bête et, surtout, c'était amusant. Les Twitterbots sont à ce type d'improvisation ce que les voitures de sport sont aux attelages de chevaux. Les blancs à remplir pourraient, par exemple, être des valeurs dans des graphiques vectoriels svg. Il pourrait s'agir de nombres dans des noms de fichiers numériques (et donc de liens aléatoires vers une base de données ouverte, par exemple). Cela pourrait même être des noms et des adverbes. Comme les bots Twitter vivent sur le web, les blocs de construction à assembler peuvent être autre chose que du texte, même si, pour l'instant, le texte est le plus facile à utiliser.

Nous allons commencer par esquisser une *grammaire de remplacement*. Cette grammaire s’appelle [Tracery.io](http://tracery.io) et ses conventions ont été développées par Kate Compton ([@galaxykate](https://twitter.com/galaxykate) sur Twitter). Elle s’utilise comme une bibliothèque [javascript](https://fr.wikipedia.org/wiki/JavaScript) dans des pages web, des jeux, et des bots. Une grammaire de remplacement fonctionne en grande partie comme les improvisations ci-dessus.

Afin de clarifier d'abord ce que fait la _grammaire_, nous n'allons _pas_ créer un bot en histoire pour l'instant. Νous allons plutôt construire quelque chose de surréaliste pour montrer comment cette grammaire fonctionne.
Imaginons que vous souhaitiez créer un bot qui parle avec la voix d'une plante en pot. Que pourrait-il bien dire ce bot que nous appelerons tout simplement _PlanteEnPot_? Notez quelques idées.

- Je suis une plante en pot. C’est vraiment ennuyeux !
- S'il vous plaît, arrosez-moi. Je vous en supplie.
- Ce pot. Il est si petit. Mes racines sont tellement à l'étroit !
- Je me suis tournée vers le soleil. Mais ce n'était qu'une ampoule.
- Je suis si seule. Où sont toutes les abeilles ?

Voyons maintenant comment ces phrases ont été construites. Nous allons remplacer les mots et les phrases par des variables, que nous appelerons des _symboles_, afin de pouvoir regénerer les phrases d’origine. Plusieurs phrases commencent par &laquo; je &raquo;, créons donc un _symbole_ "être" pour préciser un état ou une action pour le sujet:

```

"être": "suis une plante", "vous en supplie", "suis tellement seule", "me suis tournée"

```

Cette configuration nous dit que le symbole "être" peut correspondre aux expressions "suis une plante", "vous en supplie" et ainsi de suite.

Nous pouvons mélanger les symboles et du texte dans notre bot. Si nous configurons le bot de manière que les phrases commencent par le mot &laquo; je &raquo;  nous pouvons insérer le _symbole_ "être" après celui-ci et compléter ainsi la phrase par "suis une plante" ou "me suis tournée". La phrase reste ainsi _grammaticalement_ correcte. Construisons un autre symbole et appelons le, pourquoi pas, "endroit" :

```

" endroit ": "dans un pot", "sur le bord de la fenêtre", "vers le soleil"

```
("endroit" est le _symbole_ (notre variable) et "dans un pot" etc… sont les _règles_ (les valeurs de la variable) qui le remplacent)

Dans les phrases de notre brainstorming, nous n'avons jamais utilisé l'expression "sur le bord de la fenêtre", mais une fois que nous avons identifié "dans un pot", d'autres équivalences possibles surgissent. Notre bot va par la suite utiliser ces _symboles_ pour faire des phrases. Les symboles - dans notre cas: "être" et "endroit" - sont comme nos improvisations de type madlib où il fallait une liste de noms, d'adverbes et ainsi de suite. Imaginons alors transmettre à notre bot l’expression suivante :
```
"Je #être# #endroit#"

```

Les résultats possibles seront :

- Je me sens si seule sur le bord de la fenêtre.
- Je me sens si seule dans un pot.
- Je me suis tournée vers le soleil.

En bricolant, et en décomposant les unités d'expression en symboles plus petits et précis, on peut corriger toute maladresse d'expression - ou alors décider de les laisser pour rendre la voix du bot plus &laquo; authentique &raquo;.

## Prototypage à l’aide d’un éditeur Tracery
Un éditeur Tracery est disponible ici : [www.brightspiral.com/tracery/](http://www.brightspiral.com/tracery). Nous l'utiliserons pour rectifier les imperfections du bot _PlanteEnPot_. L'éditeur visualise la façon dont les symboles et les règles de la grammaire interagissent, à savoir la manière dont ils sont imbriqués et le type de résultats que votre grammaire va générer. Si vous ouvrez l'éditeur dans une nouvelle fenêtre, vous devriez voir ça :

{% include figure.html filename="bot-lesson-editor.png" caption="L'éditeur Tracery sur Brightspiral.com" %}

Le menu déroulant en haut à gauche, marqué `tinygrammar`, contient d'autres exemples de grammaires que l'on peut explorer ; ils montrent à quel point Tracery peut devenir complexe. Pour l'instant, conservez `tinygrammar`. L'un des avantages de cet éditeur est que vous pouvez appuyer sur le bouton `show colors` (*Afficher les couleurs*), qui va attribuer une couleur à chaque symbole et ses règles, en codant par couleur le texte généré afin que vous puissiez voir quel élément appartient à quel symbole.

Si vous double-cliquez sur un symbole dans la grammaire par défaut, par exemple `name` (*nom*) ou `occupation` (*profession*), et que vous appuyez sur la touche **Supprimer** de votre clavier, vous enlèverez ce symbole de la grammaire. Faites-le pour `name` (*nom*) et `occupation` (*profession*), en ne laissant que `origin`(*origine*). Maintenant, ajoutez un nouveau symbole en cliquant sur le bouton `new symbol`(*nouveau symbole*). Cliquez sur le titre (`symbol1`) et renommez-le `être`. Ensuite, cliquez sur le signe `+`et ajoutez certaines de nos règles ci-dessus. Répétez l'opération pour un nouveau symbole appelé `endroit`.

{% include figure.html filename="bot-lesson-plantbot-fr.png" caption="Construction de la grammaire pour le bot PlanteEnPot" %}

À ce moment-là, l'éditeur affichera un message d'erreur en haut à droite, `ERROR: symbol 'name' not found in tinygrammar`(*ERREUR : le symbole `name` n'a pas été trouvé dans tinygrammar*). C'est parce que nous avons déjà supprimé `name`, mais que ce symbole-là est aussi présent comme l'une une des règles du symbole `origin`! C'est intéressant, car cela nous montre que nous pouvons _imbriquer_ des symboles dans des règles. Nous pourrions par exemple avoir un symbole appelé `character`(*personnage*), combinant des sous-symboles nommés `first name` (*prénom*), `last name` (*nom de famille*) et `occupation` (*profession*), et chacun de ces sous-symboles contiendrait comme *règles* une liste de prénoms, noms et professions. Chaque fois que la grammaire serait exécutée, vous obtiendriez par exemple &laquo; Shawn Graham archéologue &raquo; stocké dans le symbole `character` (*personnage*).

Une autre chose intéressante ici, c'est que le symbole `origin` joue un rôle spécial, puisqu'il génère au final le texte (la grammaire est ici _aplatie_). Changeons donc les règles à l'intérieur de ce symbole pour que notre bot _PlanteEnPot_ puisse enfin parler. (Attention, lorsque vous utilisez d'autres symboles comme régles à l'intérieur d'un symbole donné, vous devez les entourer de croisillons `#`; ici donc vous obtiendrez: `#être# #endroit#`).

Toutefois, il manque encore quelque chose: le mot &laquo; je &raquo;. Vous savez qu'il est posible de combiner du texte ordinaire avec les règles, faites-le donc maintenant: appuyez sur le `+` à côté des règles à l'intérieur du symbole `origin` et insérez le mot *je*. Ainsi, le symbole `origin` affiche maintenant `Je #être# #endroit#`. Peut-être que votre bot parlerait même avec une diction plus poétique en utilisant la combinaison inverse `#endroit# #être#`.

Si vous appuyez sur `save`(*Enregistrer*) dans l'éditeur, votre grammaire sera horodatée et apparaîtra dans la liste déroulante des grammaires. Elle sera sauvegardée dans le cache de votre navigateur, sachant que, si vous videz le cache, vous la perdrez.

Avant de poursuivre, il y a une dernière chose à examiner. En cliquant sur le bouton `JSON`de l'éditeur, vous devriez voir quelque chose comme ça :

```JSON
{
	"origin": [
		"Je #être# #endroit#",
		""
	],
	"être": [
		"",
		"suis une plante",
		"vous en supplie",
		"suis tellement seule",
		"me suis tournée"
	],
	"endroit": [
		"",
		"dans un pot",
		"sur le bord de la fenêtre",
		"vers le soleil"
	]
}
```

Chaque grammaire Tracery est en réalité un objet [JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) composé de paires clé/valeur, ce que Tracery appelle de son côté symboles et règles. JSON est le format que nous utiliserons lorsque nous configurerons notre bot pour commencer à tweeter. Pour en savoir plus, vous pouvez consulter [ce tutoriel de Matthew Lincoln](/en/lessons/json-and-jq) (en anglais). Sachez que le format JSON est tatillon, notez donc bien que les symboles sont entourés de `"`, tout comme les règles, sauf que ces dernières sont en plus énumérées par des crochets `[` et `]`. Gardez à l'esprit ce schéma:

```JSON
{
  "symbole": ["règle","règle","règle"],
  "autresymbole": ["règle","règle","règle"],
}
```

Bien sûr, le nombre de symboles et de règles est sans importance, mais veillez à ce que les virgules soient placées correctement !

C'est une bonne pratique de copier ce JSON dans un éditeur de texte et d'enregistrer une copie dans un répertoire pérenne.

## Mais à quoi pourrait bien ressembler un bot historique ?

Maintenant, refaites l'exercice ci-dessus, mais réfléchissez bien à ce à quoi pourrait ressembler un bot en histoire étant donné les contraintes de Tracery. Construisez une grammaire simple pour exprimer cette idée et veillez à bien la sauvegarder. Voici d'autres éléments à prendre en compte lors de la conception de votre grammaire :

La sérendipité peut rendre les bots Twitter amusants, car les tweets se placent au hasard entre d’autres tweets sur un fil d’actualité (il vous faut suivre votre propre bot, pour garder un œil sur ce qu’il fait):


{% include figure.html filename="bot-lesson-maniacallaughbot.jpg" caption="Maniacallaughbot a encore gagné" %}


N'oubliez pas que votre bot apparaîtra sur le fil d'autres personnes. Le potentiel de juxtaposition du ou des messages de votre bot avec les tweets d'autres personnes influencera également le succès relatif du bot.


{% include figure.html filename="bot-lesson-interaction-with-tinyarchae.png" caption="Une interaction avec Tinyarchae occasionne des réflexions mélancoliques" %}


# Créez un compte Twitter pour votre bot et connectez-le à Cheap Bots Done Quick

Vous pouvez certes associer un bot à votre propre compte Twitter. Toutefois, si vous ne voulez pas qu'un bot tweete _en votre_nom_ ou _pour vous_, créez un nouveau compte Twitter. Pour ce faire, Twitter vous demande une adresse e-mail. Vous pouvez utiliser une nouvelle adresse ou, si vous avez un compte Gmail, vous pouvez utiliser l'astuce `+tag`, c'est-à-dire qu'au lieu de `nomdecompte` sur @gmail, vous utilisez `nomdecompte+twitterbot` sur @gmail. Twitter l’acceptera comme une adresse électronique distincte de votre adresse habituelle.

Normalement, quand on construit un bot Twitter, il faut créer [une application sur Twitter en tant que développeur ou développeuse](https://developer.twitter.com/)), obtenir les clés d'accès d'utilisateur/utilisatrice de l'API (Application Programming Interface, il s'agit de l'interface de programmation applicative), ainsi que le *token* (jeton). Ensuite, il faudrait programmer l'authentification pour que Twitter sache que le programme essayant d'accéder à la plate-forme est autorisé.

Heureusement, nous n'avons pas à faire tout cela, puisque George Buckenham a créé le site d'hébergement de bot [Cheap Bots Done Quick](http://cheapbotsdonequick.com/) (ce site web montre également la grammaire source en JSON pour un certain nombre de bots différents, ce qui peut vous donner des idées). Une fois que vous avez créé le compte Twitter de votre bot et que vous y êtes connecté, allez sur Cheap Bots Done Quick et cliquez sur le bouton `Sign in with Twitter`(*Connexion avec Twitter*). Le site vous redirigera vers Twitter pour approuver l'autorisation, puis vous ramènera à Cheap Bots Done Quick.

Le JSON qui décrit votre bot peut être rédigé ou collé dans la case blanche principale qui se trouve en bas. Copiez le script que vous avez préparé dans Tracery depuis votre éditeur de texte et collez-le dans la case blanche principale. S'il y a des erreurs dans votre JSON, la fenêtre de résultat en bas deviendra rouge et le site essaiera de vous indiquer ce qui pose problème. Dans la plupart des cas, ce sera à cause d'une virgule ou d'un guillemet erronés ou égarés. Si vous cliquez sur le bouton d'actualisation à droite de la fenêtre de résultat (attention, il n'est PAS question ici du bouton d'actualisation de votre navigateur!), le site va générer un nouveau texte à partir de votre grammaire.

{% include figure.html filename="bot-lesson-cbdq-fr.png" caption="L'interface du site Cheap Bots, Done Quick" %}

Sous la fenêtre blanche qui accueille notre JSON se trouvent quelques paramètres qui déterminent la fréquence à laquelle votre bot tweetera, s'il répondra ou non aux messages ou mentions le cas échéant, enfin si votre grammaire source sera visible pour les autres:

{% include figure.html filename="bot-lesson-settings-fr.png" caption="Les paramètres de votre bot" %}

Configurez ces paramètres selon vos préférences. Ensuite, c'est le moment de vérité! Appuyez sur le bouton `Tweet`, puis allez vérifier le flux Twitter de votre bot. Si tout se présente bien, cliquez sur `Save` (*Enregistrer*).

Félicitations, vous venez de configurer un bot Twitter!

## Code de bonne conduite

Cheap Bots Done Quick est un service fourni par George Buckenham dans un esprit de bonne volonté. N'utilisez donc pas ce service pour créer des bots offensants ou injurieux ou qui pourraient gâcher le service pour tout autre utilisateur. Comme le créateur du service l'écrit,

> Si vous créez un bot que je juge spammeux, injurieux ou désagréable d'une manière ou d'une autre (par exemple, en @mentionnant des personnes qui n'ont pas donné leur consentement, en publiant des insultes ou en proférant des calomnies), je le retirerai.

Darius Kazemi, l'un des grands artistes du bot, fournit davantage de conseils en matière de bonnes manières concernant les bots [ici](http://tinysubversions.com/2013/03/basic-twitter-bot-etiquette/).

# Aller plus loin avec Tracery
Ce que nous avons décrit ici est suffisant pour vous permettre de vous lancer. Toutefois, beaucoup de bots sont plus compliqués que cela et il est possible d'en créer qui sont étonnamment efficaces en utilisant Tracery.

## Changer des symboles

Tracery peut être configuré pour mettre les mots au pluriel ou en majuscules. Cela signifie, en réalité, que vous pouvez fournir le mot de base dans une règle, puis ajouter des modificateurs le cas échéant. Prenez par exemple:

```
"origin":["#size.capitalize# #creature.s# are nice"]
"size":["small","big","medium"]
"creature":["pig","cow","kangaroo"]
```
Les modificateurs `.capitalize` et `.s` sont ajoutés à l'intérieur du `#` du symbole qu'ils sont destinés à modifier. D'autres modificateurs sont `.ed`pour le passé, et `.a` pour a/an. Il y en a peut-être plus, car Tracery est en cours de développement.

*N.D.L.R.: Cet exemple est adapté à l'anglais, nous avons néanmoins opté pour le présenter tel quel afin de démontrer les possibilités de Tracery, dont les fonctionnalités peuvent être développées selon les besoins d'une langue. Pour l'instant, les fonctionnalités les plus subtiles sont développées dans des contextes anglophones, elles sont donc plus adaptées aux règles de grammaire et de syntaxe de l'anglais.*  

## Utiliser des emoji

Les emojis peuvent être utilisés avec beaucoup d'efficacité dans des bots Twitter. Vous pouvez copier et coller des emojis directement dans l'éditeur Cheap Bots Done Quick, en les plaçant chacun entre guillemets comme toute autre valeur qui vous sert de règle. Utilisez [cette liste](http://unicode.org/emoji/charts/full-emoji-list.html) pour repérer les emojis que vous souhaitez utiliser, en veillant à les copier/coller depuis la colonne Twitter pour vous assurer qu'ils vont bien s'afficher.

## Réutilisation de symboles générés avec la fonctionnalité action

Cette fonctionnalité ne serait probablement pas très utile dans le cas d'un bot Twitter, qui par définition produit du texte court. Mais lorsqu'il s'agit de générer du texte plus long, par exemple une histoire ou un poème, cette fonctionnalité peut être employée pour que Tracery retienne la première fois qu'une règle particulière a été affectée à un symbole. Ainsi, nous pourrions faire en sorte que la même valeur soit toujours utilisée lors de chaque appel suivant de `creature`. C'est ce que Tracery appelle une « action ». La convention est #[uneAction]unSymbole#. Toutefois, cette fonctionnalité reste en cours de développement et peut prêter à confusion. Vous pouvez néanmoins voir comment elle fonctionne, si vous copiez-collez le JSON ci-dessous dans cet éditeur Tracery de Beau Gunderson : [https://beaugunderson.com/tracery-writer/](https://beaugunderson.com/tracery-writer/) (veiller à sélectionner et à supprimer le texte qui s'affiche par défaut). L'éditeur Tracery utilisé précédemment ne gère pas très bien la sauvegarde des données, donc cette alternative-ci constitue un meilleur outil pour nos besoins actuels.


```JSON
{
	"taille": [
		"petit",
		"grand"
	],
	"créature": [
		"cochon",
		"veau",
		"kangourou"
	],
	"poème":["Mon animal préféré était un #animaldoudoutaille# #animaldoudou# en effet. Ce #animaldoudou# s'appelait Lucky"],
 	 "origin":["#[animaldoudou:#créature#][animaldoudoutaille:#taille#]poème#"]

}

```

Un autre exemple un peu plus complexe est le numéro 5 sur le site du tutoriel de Kate Compton à l'adresse [http://www.crystalcodepalace.com/traceryTut.html](http://www.crystalcodepalace.com/traceryTut.html) :

```JSON
{
	"name": ["Arjun","Yuuma","Darcy","Mia","Chiaki","Izzi","Azra","Lina"]
,	"animal": ["unicorn","raven","sparrow","scorpion","coyote","eagle","owl","lizard","zebra","duck","kitten"]
,	"mood": ["vexed","indignant","impassioned","wistful","astute","courteous"]
,	"story": ["#hero# traveled with her pet #heroPet#.  #hero# was never #mood#, for the #heroPet# was always too #mood#."]
,	"origin": ["#[hero:#name#][heroPet:#animal#]story#"]

}
```


Tracery lit le symbole `origin` (*N.D.L.R.: si vous travaillez sur un exemple en français, ce qui est tout à fait possible, veillez à ne pas traduire ce symbole; vous gardez donc bien `origin`, car sinon il ne sera pas reconnu et le code ne fonctionnera pas*), et avant d'arriver au symbole `story`, il voit une action appelée `hero` qu'il définit à partir du symbole `name`. Il fait la même chose pour `heroPet` à partir d'`animal`. Avec ces ensembles, il lit alors l’histoire définie dans la variable `story`. Dans `story` le symbole `hero` lit ce qui vient d'être défini par l'action, et retourne la même valeur à chaque fois. Donc, si 'Yuuma' a été sélectionné par l'action, l'histoire dira ```Yuuma traveled with her pet [nom d'animal] Yuuma was never [variable d'humeur]``` (*```Yuuma a voyagé avec son animal de compagnie.... Yuuma n'a jamais...```*). Si nous n'avions pas défini le nom du héros via l'action, alors l'histoire générée pourrait changer le nom du héros au milieu de l'histoire !


## Répondre à des mentions dans Cheap Bots Done Quick

[Cheap Bots Done Quick](http://cheapbotsdonequick.com/) possède une fonctionnalité bêta qui permet à votre robot de répondre aux mentions. Attention, si vous créez deux bots configurés pour que l'un mentionne l'autre, la « conversation » qui s'ensuit peut durer très longtemps. A noter qu'il y a 5% de chances dans tout échange que le bot ne réponde pas, interrompant ainsi la conversation.

Pour configurer un modèle de réponse, cliquez au bas de la page pour paramétrer le bouton pour répondre aux tweets (`Reply`). Dans la fenêtre de modification JSON qui apparaît, configurez le modèle pour les phrases auxquelles votre bot va répondre. Par exemple, voici ci-dessous une partie de ce que mon bot @tinyarchae détecte :

```JSON
{
	"hello":"hello there!",
	"What|what":"#whatanswer#",
	"Who|who":"#whoanswer#",
	"When|when":"#whenanswer#",
	"Where|where":"#whereanswer#.",
	"Why|why":"#whyanswer#",
	"How|how":"#howanswer#",
	"Should|should|Maybe|maybe|if|If":"#shouldanswer#"
}
```

Les symboles ici peuvent inclure des motifs d'expressions régulières (Regex) (pour en savoir plus, voir [cette leçon](/fr/lecons/comprendre-les-expressions-regulieres) sur les expressions régulières). Ainsi, dans l'exemple ci-dessus, le dernier symbole recherche *Should* " OU *should* OU  *Maybe* OU  *maybe* OU *if* OU *If*. Pour répondre à tout ce qui lui est adressé, le symbole serait le point : `.`. Les règles peuvent inclure du texte simple (comme dans la réponse à "hello") ou peuvent être un autre symbole. Les règles doivent être incluses dans votre grammaire principale dans la première case d'édition JSON de la page. Ainsi, `#shouldanswer#` est dans la case principale de l'éditeur de grammaire @tinyarchae sous la forme d'une ligne :

```JSON
"shouldanswer":["We asked #name#, who wrote 'An Archaeology of #verb.capitalize#'. The answer is #yesno#.","This isn't magic 8 ball, you know.","This is all very meta, isn't it.","#name# says to tell you, '42'."],
```

Tout en bas de la page, vous pouvez tester vos mentions en écrivant un exemple de tweet que votre bot va détecter. Si vous avez bien configuré les choses, vous devriez voir une réponse. S'il y a une erreur, la case `Response` (*Réponse*) devient rouge et vous indique où se trouve l'erreur.

{% include figure.html filename="bot-lesson-response.png" caption="Tester la réponse du bot" %}

## Graphiques SVG
Puisque le [SVG](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics) est un format de données qui décrit la géométrie d'un graphique vectoriel, Tracery peut être utilisé pour réaliser un travail plutôt artistique. Par exemple, il existe le bot [Tiny Space Adventure](https://twitter.com/TinyAdv) qui dessine un champ d'étoiles, un vaisseau spatial et un descriptif. Sa grammaire [peut être consultée ici](https://pastebin.com/YYtZnzZ0). Pour que le format SVG soit généré correctement, il est d'une importance capitale d'avoir paramétré correctement Tracery. N'hésitez donc pas de prendre comme modèle le code source du [bot softlandscapes](http://cheapbotsdonequick.com/source/softlandscapes) qui commence par définir le texte critique qui délimite le SVG :

```
"origin2": ["#preface##defs##bg##mountains##clouds##ending#"],
"preface":"{svg <svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" height=\"#baseh#\" width=\"#basew#\">"
```
et ensuite :

```
"ending":"</svg>}"
```

Travailler avec SVG peut être délicat, car des éléments comme les barres obliques inverses, les fins de ligne, les guillemets et ainsi de suite doivent être « échappés » pour que le script fonctionne correctement. Comme dit sur le site,

> La syntaxe ressemble à ceci : {svg <svg <svg ...> .... </svg>}. Les balises SVG devront spécifier un attribut de largeur et de hauteur (*width*, *height*). Notez que, dans celles-ci, les guillemets (`"`) et les croisillons (`#`) doivent être échappés en se faisant précéder par une double barre oblique inversée (antislash), comme ceci \\" et cela \\#. Par ailleurs, les accolades (`{` et `}`) doivent aussi être échappées en utilisant quatre barres obliques inversées, de la manière qui suit: \\\\{ et \\\\}.
Note : cette fonctionnalité est encore en développement, le bouton tweet sur cette page ne fonctionnera donc pas. Et les informations de débogage sont meilleures dans FF que dans d'autres navigateurs.

Les bots qui génèrent du SVG dépassent le cadre de cette leçon, mais une étude minutieuse des bots existants devrait pouvoir vous aider, si vous souhaitez approfondir cette question.

## Musique
À proprement parler, il ne s'agit plus de bots, mais comme la musique peut être écrite en texte, on peut utiliser Tracery pour composer de la musique et utiliser d'autres bibliothèques pour convertir cette notation en fichiers Midi. Pour aller plus loin, vous pouvez consulter [cet article-ci](http://www.codingblocks.net/videos/generating-music-in-javascript/) et mon [propre retour d'expérience](https://electricarchaeology.ca/2017/04/07/tracery-continues-to-be-awesome/).

# Autres tutoriels et ressources sur les bots
**En anglais:**

- Zach Whalen, [How to make a Twitter Bot with Google Spreadsheets](http://www.zachwhalen.net/posts/how-to-make-a-twitter-bot-with-google-spreadsheets-version-04/), site web de Zach Whalen, http://www.zachwhalen.net/, 7 mai 2015
- [Tracery & Twitterbots](http://cmuems.com/2015b/tracery-twitterbots/)
- Casey Bergman, [Keeping Up With the Scientific Literature using Twitterbots: The FlyPapers Experiment](https://caseybergman.wordpress.com/2014/02/24/keeping-up-with-the-scientific-literature-using-twitterbots-the-flypapers-experiment/) (et aussi [ce repository de Robert Lanfear sur Github](https://github.com/roblanf/phypapers)). Cette méthode consiste à collecter les flux RSS des articles de revues, puis à utiliser un service tel que [Dlvr.it](https://dlvrit.com/) pour rediriger les liens vers un compte Twitter.
- Abandonnée: Stefan Bohacek propose des modèles de code pour différents types de bots sur le site de remixage de code Glitch.com. Si vous vous rendez sur sa page, vous verrez une liste de différents types de bots. Séléctionnez-en un, cliquez sur le bouton `remix` puis étudiez attentivement la documentation `README.md` qui s'affiche sur la page. Glitch nécessite une identification (login) via un compte Github ou Facebook.
- Enfin, je suggère de rejoindre le groupe BotMakers Slack pour découvrir d'autres tutoriels, des personnes partageant les mêmes intérêts, et d'autres ressources : [Inscrivez-vous ici](https://botmakers.org).
- Le wiki des Botmakers' propose également une liste de [tutoriels sur des bots Twitter](https://botwiki.org/tutorials/twitterbots/).

Enfin, voici une liste de bots fonctionnant avec Tracery tenue à jour par Compton [ici]https://twitter.com/GalaxyKate/lists/tracery-bots). Amusez-vous bien ! Que vos bots déconcertent, divertissent, inspirent et déroutent.

**En français (N.D.L.R.: il s'agit de notes ajoutées à la version traduite):**

- Antoine Courtin, [#BotInfocom](https://medium.com/@seeksanusername/botinfocom-1a89605c0953), *Medium.com/@seeksanusername/*, 11 décembre 2016.

# Exemples de bots en français
**Avec un compte Twitter dédié**

- [Bot de sept lieues](https://www.cafedefaune.org/ougepro/bot-de-sept-lieues): un bot voyageur qui raconte ses découvertes faites dans des contrées imaginaires.
- [EnvoisdeRomeBot](https://twitter.com/envoisdeRomeBot): un bot de valorisation d'une base de données patrimoniales.
- [Le bot de 7 lieux](https://twitter.com/lebotde7lieux): un bot qui explore les données géolocalisées de Wikidata.
- [Mémoire de la guerre d'Espagne - Bot](https://twitter.com/memo_guerra_bot): un bot de mémoire sur la Guerre d'Espagne qui liste les noms recensés de ses victimes.

**Émis à partir du compte d'utilisateur du créateur du bot**

- Le [GallicaBot](https://twitter.com/search?q=GallicaBot&src=typed_query&f=live) d'Olivier Jacquot qui tweete les titres d'ouvrages en accès libre disponibles sur la bibliothèque [Gallica](https://gallica.bnf.fr/).
- Le [#BotInfoCom ](https://twitter.com/search?q=%23botInfocom&src=typd&f=live) d'Antoine Courtin, un bot qui simule des titres d'articles (imaginaires) en sciences de l'information et de la communication.

# Références
Compton, K., Kybartas, B., Mateas, M.: Tracery: « An author-focused generative text tool » dans *Proceedings of the 8th International Conference on Interactive Digital Storytelling*, pp. 154–161 (2015).
