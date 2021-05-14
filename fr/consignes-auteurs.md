---
title: Consignes aux auteur(e)s
layout: blank
original: author-guidelines
skip_validation: true
---

# Consignes aux auteur(e)s

<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />
<h2 class="noclear"> Étape 1 : <a href="#proposer-une-nouvelle-leçon">Proposer une nouvelle leçon</a></h2>
<h2 class="noclear">Étape 2 : <a href="#rédaction-et-mise-en-forme">Rédaction et mise en forme</a></h2>
<h2 class="noclear">Étape 3 : <a href="#soumettre-une-nouvelle-leçon">Soumettre une nouvelle leçon</a></h2>  


Ces consignes ont été développées pour vous permettre de comprendre comment s'organise l'écriture d'un tutoriel pour le *Programming Historian en français*. Elles fournissement des détails pratiques, des informations sur la philosophie de la revue, ses workflows et l'évaluation ouverte par les pairs. Si pour quelque raison que ce soit elle nous vous paraissent pas claires, n'hésitez pas à contacter le rédacteur ou la rédactrice en chef {% include managing-editor.html lang=page.lang %}.  

## Proposer une nouvelle leçon

<div class="alert alert-success">
Nous vous invitons à nous soumettre des tutoriels pertinents pour les sciences humaines et sociales, qui portent sur un problème de recherche ou un processus particulier, et qui sont adaptés à n'importe quel niveau de compétence et d'expérience technique. Les tutoriels ont vocation à être pérennes dans le long terme et doivent s'adresser à un public international.
La portée et la longueur du tutoriel doivent être appropriés à la complexité de la tâche qui y est expliquée. La longueur des tutoriels ne doit pas excéder 8000 mots (en incluant le code source) et nous encourageons la soumission de leçons plus courtes. Celles qui seraient plus longues sont susceptibles d'être divisées en plusieurs tutoriels.
</div>

Si vous avez une idée pour une nouvelle leçon, merci de compléter un [formulaire de proposition](/assets/forms/Formulaire.Tutoriel.txt) et contacter {% include managing-editor.html lang=page.lang %} pour discuter de votre idée.

Vous pouvez avoir une meilleure idée de ce que nous publions en consultant nos [leçons en ligne](/fr/lecons/), en lisant nos [consignes aux évaluateurs et évaluatrices](/fr/consignes-evaluateurs), ou encore en parcourant les [leçons en cours de développement](https://github.com/programminghistorian/ph-submissions/issues).
<!--
Afin d'assurer la pérennité de nos leçons, les auteur(e)s doivent s'efforcer de soumettre des leçons qui ne sont pas complètement dépendantes de logiciels spécifiques ou d'interfaces utilisateurs. Ces leçons vont à coup sûr souffrir d'instabilité et vont avoir besoin de révisions substantielles lorsque sort une nouvelle version du logiciel ou de l'interface. Enseigner des concepts, plutôt que demander de "cliquer sur le bouton _x_", facilite la rédaction et la publication de tutoriels pérennes.-->

Une fois que votre proposition est acceptée, nous allons créer un ticket "Proposition" dans notre [dépôt de soumissions](https://github.com/programminghistorian/ph-submissions/issues) avec le titre provisoire de la leçon et les objectifs pédagogiques proposés. Ce ticket sert à signaler le travail en cours alors que vous êtes en train de rédiger votre leçon. Pour éviter d'accumuler les retards, nous vous demandons de soumettre votre leçon dans les 90 jours suivant l'acceptation de votre proposition.

## Rédaction et mise en forme
Cette section présente notre charte éditoriale. En en respectant les principes, vous nous aidez à conserver la cohérence des contenus du *Programming Historian en français*.  

Elle comprend trois parties:  

* Règles de rédaction  
* Règles typographiques  
* Règles de mise en forme  

### Règles de rédaction  
<!--dans cette partie j'ai changé le niveau d'arborescence en comparaison avec la page en EN, cela faisait bizarre de maintenir cette partie au niveau 2, car elle dépend d'une partie niveau 2 aussi)-->  
Cette partie aborde des questions générales de style pour vous aider à mieux répondre aux attentes de notre lectorat et de notre équipe éditoriale. Elle fournit des informations élémentaires sur le style et le ton à adopter lors de la rédaction, les valeurs de libre accès et de logiciel libre, la nécessité de s'adresser à un lectorat international, l'enjeu d'une écriture durable, et les choix à faire quant aux données mobilisées dans les leçons. Nous vous conseillons de bien lire cette partie lorsque vous vous projettez dans l'écriture d'une leçon puis de la relire avant de soumettre votre texte pour avoir la certitude que voous en avez tenu compte.    

#### Language and Style  

#### Open Source, Open Access  

#### Write for a Global Audience  

<!--(plusieurs éléments ici reprennent la partie Ecrire pour un public international, cf. ci-dessous en la réorganisant. Il va falloir la concevoir avec à l'esprit un lectorat francophone) -->  

<!--### Écrire pour un public international

Les lecteurs et les lectrices du *Programming Historian en français* viennent du monde entier et travaillent au sein d'environnements culturels variés. Pour qu'un public international puisse être touché, un certain nombre de nos publications sont accessibles dans plus d'une langue depuis 2017. Nous avons également pour but de traduire tous nos tutoriels. **Comme nous reconnaissons que toutes les méthodes et outils ne sont pas pleinement accessibles à un public international**, les auteur(e)s peuvent et doivent écrire leurs leçons de façon à ce qu'elles soient accessibles à autant de personnes que possible. **Nous vous prions donc de bien vouloir respecter les conseils suivants lorsque vous écrivez votre tutoriel** :

- Lorsque vous choisissez vos méthodes et outils, essayez de les choisir en gardant à l'esprit que les tous les lecteurs et toutes les lectrices ne parlent pas tous et toutes la même langue. Cela est particulièrement important lorsque l'on travaille sur des méthodes d'analyse des textes, ou lorsque les utilisateurs et les utilisatrices souhaiteraient travailler avec des ensembles de caractères différents (par exemple, caractères accentués, non-latins, etc.).
- Quand vous choisissez des images et des sources primaires, quand vous produisez des illustrations, ou quand vous faites des copies d'écran, pensez à la manière dont celles-ci vont être vues par un public international.
- Au cours de la rédaction, évitez les plaisanteries, les références culturelles, les calembours, les jeux de mots, les expressions idiomatiques, le sarcasme, les emojis ou une syntaxe qui serait plus compliquée que nécessaire. Les mentions de personnes, d'organisations, ou de détails historiques doivent toujours être accompagnées d'informations contextuelles. Vous devez constamment penser au fait que vos lecteurs et lectrices ne vivent pas toujours dans le même pays que vous et qu'ils ne parlent pas la même langue.
- Dans les exemples de codes source ou les métadonnées, utilisez des formats standards, reconnus au niveau international, pour les dates et les heures ([ISO 8601:2004](https://www.iso.org/fr/standard/40874.html)). Dans votre texte, restez bien conscient(e) des différences culturelles existantes dans la représentations des dates et des heures. Ces différence pourraient en effet causer de la confusion.
- Quand cela est possible, choisissez des méthodes et des outils qui disposent de documentation multilingue. Dans le cas contraire, essayez d'ajouter, autant que faire se peut, des références multilingues à la fin de votre tutoriel.

Contactez le rédacteur ou la rédactrice en charge du suivi éditorial si vous avez besoin de conseils sur n'importe quel de ces points. Les tutoriels qui ne peuvent pas respecter ces consignes ne seront pas traduits, mais ils sont les bienvenus afin d'être envisagés pour une publication en une seule langue. -->   

#### Écrire de manière durable  
<!-- La partie correspondante en anglais a été remaniée: il faudrait comparer et voir s'il est pertinent de modifier celle-ci--> 
Le *Programming Historian en français* s'efforce de publier des leçons qui sont utiles à notre lectorat dans l'immédiat. Les auteur(e)s doivent consulter notre [politique de retrait des leçons]({{site.baseurl}}/fr/politique-retrait-lecons), qui décrit comment l'équipe éditoriale du *Programming Historian en français* gère les leçons qui sont devenues obsolètes. Pour assurer la création de leçons pérennes, nous vous demandons de garder à l'esprit un certain nombre de consignes lors de leur rédaction :

- Au lieu de vous concentrer sur des logiciels en particulier, axez de préférence votre leçon sur les méthodologies, et sur une présentation plus générale des outils.
- Si votre leçon peut tirer profit de la documentation d'un logiciel existant, envisagez de diriger votre lectorat vers cette documentation plutôt que de la répéter dans votre leçon. Et, au lieu d'ajouter un lien vers les ressources concernant un logiciel développé par une entreprise - ressources qui, en général, changent très souvent -, vous pouvez fournir des conseils généraux sur la manière dont vos lecteurs et lectrices peuvent trouver la documentation.
- Limitez l'usage d'images spécifiques à la version du logiciel présenté, à moins que cela ne soit requis pour suivre votre leçon.
- Vérifiez tous les liens externes de façon à vous assurer qu'ils sont à jour.
- Les données nécessaires pour suivre une leçon doivent être hébergées avec notre site Internet.  

### Règles typographiques  
<!-- Ici il y a du texte en EN, à voir si pertinent de le traduite ou de mettre une accroche spécifique-->
#### Dates et heures
<!--Gwen-->   
* Les siècles doivent s'écrire en chiffres romains, si possible en petites capitales, avec le "e" final en exposant, par exemple <span style="font-variant:small-caps;">XVIII</span><sup>e</sup> siècle.

* La mention des décennies, plus particulièrement usitée pour le <span style="font-variant:small-caps;">XX</span><sup>e</sup> siècle, peuvent s'écrire soit en toutes lettres (les années trente), soit en donnant tous les chiffres de l’année (les années 1930).

* On n’abrège pas les millésimes pour les intervalles de dates. On privilègie donc l'écriture des intervalles sous la forme "1854-1864".

* Pour les dates écrites au format numérique, repecter la norme ISO 8601:2004 (AAAA-MM-JJ).

* Pour marquer les dates avant ou après Jésus-Christ, abréger sous la forme "av. J.-C." ou "apr. J.-C.".

* Pour les heures, deux options sont possibles :
	* écrire toutes les mentions "heures" (h), minutes" (min) et "secondes" (s) en abrégé (10&nbsp;h&nbsp;10 min), avec un espace insécable (indiqué comme ceci en HTML : ``` &nbsp; ```) entre l'abrévation et le chiffre
	* écrire au format numérique avec un double point précédé d'un espace insécable (16 :10)

* Pour indiquer les durées, écrire les mentions "heures", minutes" et "secondes" en toutes lettres (10 heures 10 minutes).


#### Les nombres 
<!--Sofia--> 
 * Écrire les nombres en lettres de 1 à 16 (un à seize) et en chiffres les nombres supérieurs. 
 * Écrire le(s) nombre(s) commençant une phrase en toutes lettres; toutes les variétés de la langue française sont acceptées (par exemple, *septante* ou *soixante-dix* pour 70) 
 * Si deux nombres sont cités dans une phrase, dont l'un devrait s'écrire en lettres et l'autre en chiffres, écrire tous les deux préférablement en chiffres ou, si le contexte oblige, tous les deux en lettres (par exemple, *nous avons fusionné 3 des 26 colonnes de notre tableau*; ou *Trois des vingt-six colonnes de notre tableau ont été fusionnées*; nous éviterons donc de mélanger les formes dans une même phrase. Le plus important est de se fixer une règle et de s'y tenir.  
 *	Écrire les nombres en chiffres dans les tableaux et les formules statistiques et techniques du texte.
 *	Utiliser l'espace insécable pour séparer les nombres en tranches de trois chiffres, lorsqu'il s'agit de grands nombres, tant dans la partie des entiers que dans celle des décimales (par exemple, *31 589*, *4,321 078*). Pour les nombres composés de quatre chiffres, cela est facultatif et nous préférerons la formule sans espace insécable (*3200* plutôt que *3 200*). En revanche, les numéros, les dates et tout autre chiffre ayant une fonction de numérotation ne se séparent pas.  
 *	Écrire les nombres en chiffres pour indiquer les versions (*version 5* ou *v.5*), les poids et mesures, les pourcentages, les fractions et nombres décimaux, les sommes (par exemple, 55 %, 17 °C, 200 €).
 *	Pour exprimer le pourcentage, écrire le nombre accompagné du signe % séparés par un espace insécable; écrire le pourcentage en toutes lettres (*pour cent*) seulement au début d'une phrase. 
 *	Écrire les formules mathématiques en syntaxe [LaTeX](https://fr.wikibooks.org/wiki/LaTeX/%C3%89crire_des_math%C3%A9matiques).
   

#### En-têtes
<!--Gwen--> 
Les en-têtes ne doivent pas faire appel à des polices de caractères spécifiques ou à des propriétés telles que l'italique ou le gras.

Les titres doivent immédiatement précéder le corps du texte de l'en-tête.

Ne pas faire suivre un titre d’une mise en garde ou d’un autre titre sans un court texte introductif ou descriptif.


#### Listes   
<!--Gwen-->  
Nous utilisons les listes à puces ou à nombres. Les items de listes doivent être limités à une phrase. Ils sont traités comme des entités séparées et ne doivent pas être enchaînées avec de la ponctuation et des conjonctions. 

Ne pas écrire:

* Voici un item, et
* voici un autre item; et
* voici le derner item.

Écrire:

* Voici un item
* Voici un autre item
* Voici un dernier item
	
Ou bien écrire:

1. Voici un item
2. Voici un autre item
3. Voici un dernier item


#### Ponctuation  
<!--Sofia--> 

#### Usage des majuscules 
<!--Gwen-->  
Les majuscules, à utiliser avec parcimonie dans la prose courante, peuvent se diviser en trois catégories :

* Les majuscules de position (en début de phrase ou à chaque alinéa dans une liste énumérative)
* Les majuscules de signification pour supprimer une ambiguïté
* Les majuscules elliptiques pour distinguer les noms propres des noms communs

Les majuscules sont aussi concernées par les accents, le tréma ou la cédille, même dans le cas des abréviations, mais pas pour les sigles et les acronymes. Les différents cas décrits ci-dessous résument les particularités dans l'usage des majuscules en français. 

* Les titres :
	* Si le titre ne débute pas par un article défini (le, la, les), seul le mot initial prend la majuscule (exemple : *Une saison en enfer*).
	* Si le titre débute par un article défini (le, la, les), ou bien seul l’article prend une majuscule, ou bien l'article et le premier substantif, ainsi que les adjectifs et adverbes qui précèdent le substantif (exemple : *Les Liaisons dangereuses*). Si le titre contient une comparaison ou une symétrie, l'article défini prend une majuscule ainsi que chaque terme mis en symétrie (exemple : *La Belle et la Bête*).
	* Si nous sommes confrontés à des titres doubles séparés par la conjonction "ou", les règles ci-dessus s'appliquent à chacune des deux parties du titre. Cependant, l'article défini débutant la seconde partie perd la majuscule (exemple : *Le Mariage de Figaro ou la Folle Journée*).

* Les noms propres

* Les organisations artistiques, culturelles ou gouvernementales, les institutions et établissements :
	* Pour les organismes d’État uniques, la majuscule s'applique au permier mot nécessaire à l’identification, et à l’adjectif qui précède (exemple : "le Conseil constitutionnel"). 
	* Pour les organismes d’État non-uniques, conserver les minuscules, sauf lorsque les substantifs et les éventuels adjectifs qui les précédent font office de nom propre (exemple : "le ministère des Affaires étrangères").
	* Pour les régimes politiques, s'ils désignent implicitement un pays ou une époque, ils prennent une majuscule, ainsi que l'adjectif qui précède (exemple : "la Restauration"). Ils conservent toutefois une minsucule quand ils désignent directement un type de régime politique (exemple : "rétablir la république"), ou bien quand ils sont accompagnés d'un nom propre (exemple : la république de Weimar).
	* Les mots "Secrétariat" et "Département" prennent une majuscule (exemple : "le Département d’économie de Sciences Po").
	* Pour les établissements d’enseignement, s'ils sont d’importance nationale, on met une majuscule au premier substantif et à l'éventuel adjectif qui le précède (exemple : "le Collège de France"). S'il est d’importance régionale ou locale, les noms communs s'écrivent en minuscules, et on ajoute une majuscule aux noms propres qui l'identifie (exemple : "université Paris-Descartes").
	* Le mot faculté ne prend la majuscule initiale que lorsqu'il désigne le corps médical. De même, le mot université ne prend la majuscule initiale que lorsqu'il désigne le corps enseignant. Les disciplines ne prennent pas de majuscule (exemple : "la faculté des lettres et sciences humaines").
	* Pour les agences, commissions, établissements publics, organisme non-gouvernemental, la majuscule est placé sur le terme générique par lequel commence le nom officiel d’une institution, d’une administration, d’un service de l’État ou d’un organisme international, de même qu’à l’adjectif qui le précède (exemple : "l’Union postale universelle").

* Les cérémonies et festivités prennent une majuscule (exemple : "la Semaine Sainte"). 

* Différentes règles s'appliquent pour les lieux : 
	- Les noms de pays, provinces, régions, ou villes prennent une majsucule, mais pas les adjectifs adjoints aux noms propres (exemple : "l'Italie méridioniale"), sauf s’ils font office de noms propres (exemple : "le Grand Nord").
	- Les noms communs d’entités géographiques restent en minuscules (exemple : la mer). Si les noms communs d’entités géographiques sont suivis par un nom qualifiant, seul ce dernier a une majuscule (exemple : "le golfe du Lion"). De même pour les monuments ou les jardins (exemple : "la tour Eiffel").
	-  Les lieux désignant un produit connu devenu nom commun ne prennent pas de majuscules (exemple : "un bourgogne").
	-  Les planètes, les étoiles et les signes du zodiaque prennent toujours une majuscule.

* Les évènements historiques prennent une majuscule car ils sont assimilés à des noms propres (exemple : "la Fronde").

* Les noms de doctrines, qu'elles soient religieuses, philosophiques, artistiques ou politiques, restent en minuscules (exemple : "l'existentialisme"), de même que ceux qui s’en réclament (exemple : "les hindous"), mais la majuscule est de mise pour ceux devenus des noms propres (exemple : "la Nouvelle Vague").

* En ce qui concerne la religion, on met une majuscule quand on désigne l’institution ou l’ensemble des fidèles (exemple : "Église", "Ouma"), mais le bâtiment religieux s'écrit avec uen minuscule. On met une majuscule pour les mots "Dieu", "Jésus" et leurs synonymes et équivalents comme "le Verbe", "le Créateur", "Allah", "Bouddha". Le mot "saint" ne prend pas de majuscule quand il désigne un personnage (exemple : "saint François d'Assises"), mais il faut en mettre une quand il fait partie d'un nom propre (exemple : "Saint Louis") ou d'un nom propre composé (exemple "l’île Saint-Louis").

* Pour les livres sacrés, les mots "Bible", "Écriture" et "Évangile" prennent une majuscule s’ils désignent le recueil de textes religieux, ainsi que les mots « Ancien Testament », « Nouveau Testament » et « Coran ». Le mot "bible" perd toutefois sa majuscule quand il désigne un livre faisant autorité.

* Dans le cas de métiers, les noms des fonctions, de charges ou de titres civils ou militaires ne prennent pas de majuscules, sauf pour :
	* Les titre ayant eu un seul détenteur assimilable à un nom propre (exemple : "le Duce").
	* La désignation d’une personne précise, auquel cas pas il faut éviter de créer une ambiguïté dans le texte pour l'antonomase (exemple : "le Général" pour le général de Gaulle).
	* Les titres honorifiques (exemple : "Sa Majesté").

* Pour les comités, rapports et enquêtes, on met une majuscule au terme (Programme, Projet, Plan, ...) suivi d’un adjectif ou d’un complément quand il est compris dans le nom officiel d’une activité (exemple : "le Plan vert"). Il prend toutefois une minuscule quand le nom officiel de l’activité est placé en apposition (exemple : "le plan Marshall").

* Les saisons s'écrivent en minuscules.

* Les monnaies ne prennent pas de majuscules. 


#### Écriture inclusive  
Nous appliquons l'écriture inclusive suivant les consignes de l'Office québécois de la langue française sur la [formation des noms féminins](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?Th=1&Th_id=358&niveau=) et la [rédaction épicène](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?Th=2&t1=&id=3912), mises en place en 2002, ainsi que du [Guide d’aide à la féminisation des noms de métiers, titres, grades et fonctions](https://www.vie-publique.fr/sites/default/files/rapport/pdf/994001174.pdf), publié par l'Institut national de la langue française en 1999. Ces deux textes quasi-officiels se recoupent largement et constituent des guides de base pour l'équipe du _Programming Historian en français_. En revanche, nous ne faisons pas recours à l'utilisation du point médian (ou point milieu) ou de tirets. Ainsi, nous éviterons d'écrire "les historien·ne· s" ou "les historien-ne-s"; nous privilégions à la place "les historiens et historiennes" ou encore "les historien(ne)s", pour éviter la répétition de "et".  

#### Challenging Words Explained 
<!--- à voir si une telle partie est utile en français; cela peut rassembler tout et rien-->    

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

