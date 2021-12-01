---
title: Consignes aux auteur(e)s
layout: blank
original: author-guidelines
skip_validation: true
---

# Consignes aux auteur(e)s

<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />
<h2 class="noclear"> Étape 1: <a href="#étape-1-proposer-une-nouvelle-leçon">proposer une nouvelle leçon</a></h2>
<h2 class="noclear">Étape 2: <a href="#étape-2-rédaction-et-mise-en-forme">rédaction et mise en forme</a></h2>
<h2 class="noclear">Étape 3: <a href="#étape-3-soumettre-une-nouvelle-leçon">soumettre une nouvelle leçon</a></h2>  

Ces consignes ont été développées pour vous permettre de comprendre comment s'organise l'écriture d'un tutoriel pour le *Programming Historian en français*. Elles fournissent des détails pratiques, des informations sur la philosophie de la revue, ses workflows et l'évaluation ouverte par les pairs. Si pour quelque raison que ce soit elles nous vous paraissent pas claires, n'hésitez pas à contacter notre rédacteur/rédactrice en chef {% include managing-editor.html lang=page.lang %}.  

## Étape 1: proposer une nouvelle leçon

<div class="alert alert-success">
Nous vous invitons à nous soumettre des tutoriels pertinents pour les sciences humaines et sociales, qui portent sur une problématique de recherche ou un processus particulier, et qui sont adaptés à n'importe quel niveau de compétence et d'expérience technique. Les tutoriels ont vocation à être pérennes dans le long terme et doivent s'adresser à un public international.
La portée et la longueur du tutoriel doivent être appropriées à la complexité de la tâche qui y est expliquée. La longueur des tutoriels ne doit pas excéder 8000 mots (en incluant le code source) et nous encourageons la soumission de leçons plus courtes. Celles qui seraient plus longues sont susceptibles d'être divisées en plusieurs tutoriels.
</div>

Si vous avez une idée pour une nouvelle leçon, merci de compléter un [formulaire de proposition](/assets/forms/Formulaire.Tutoriel.txt) et contacter {% include managing-editor.html lang=page.lang %} pour discuter de votre idée.

Vous pouvez avoir une meilleure idée de ce que nous publions en consultant nos [leçons en ligne](/fr/lecons/), en lisant nos [consignes aux évaluateurs et évaluatrices](/fr/consignes-evaluateurs), ou encore en parcourant les [leçons en cours de développement](https://github.com/programminghistorian/ph-submissions/issues). Merci de prendre aussi le temps de consulter notre table de [concordance des leçons](https://docs.google.com/spreadsheets/d/1vrvZTygZLfQRoQildD667Xcgzhf_reQC8Nq4OD-BRIA/edit#gid=0) afin de voir quelles méthodes ont déjà été traitées dans nos tutoriels publiés ou à venir.

Une fois que votre proposition est acceptée, nous allons créer un ticket &laquo;&#x202F;Proposition&#x202F;&raquo; dans notre [dépôt de soumissions](https://github.com/programminghistorian/ph-submissions/issues?q=is%3Aissue+is%3Aopen+label%3Aproposal) avec le titre provisoire de la leçon et les objectifs pédagogiques proposés. Ce ticket sert à signaler le travail en cours alors que vous êtes en train de rédiger votre leçon. Pour éviter d'accumuler les retards, nous vous demandons de soumettre votre leçon dans les 90 jours suivant l'acceptation de votre proposition. Pendant cette période, votre point de contact sera notre rédactrice en chef ou un autre membre de l'équipe désigné par celle-ci.

## Étape 2: rédaction et mise en forme

Ce guide de style présente notre approche et notre charte éditoriale à l'attention des auteur(e)s. En respectant ces principes, vous nous aidez à conserver la cohérence des contenus du *Programming Historian en français*.  

La section comprend trois parties, que nous vous remercions de lire avant d'écrire et après avoir achevé votre contribution&#x202F;:  

* A. Style de rédaction et public ciblé  
* B. Règles typographiques  
* C. Règles de mise en forme  

## A. Style de rédaction et public ciblé  
Cette partie aborde des questions générales de style pour vous aider à mieux répondre aux attentes de notre lectorat et de notre équipe éditoriale. Elle fournit des informations élémentaires sur le style et le ton à adopter lors de la rédaction, l'engagement en faveur du libre accès et des logiciels libres, la nécessité de s'adresser à un lectorat international, le besoin d'écrire un texte qui puisse durer dans le temps, et les choix à faire quant aux données mobilisées dans les leçons. Nous vous conseillons de bien lire cette partie lorsque vous vous projetez dans l'écriture d'une leçon puis de la relire avant de soumettre votre texte pour avoir la certitude que vous en avez tenu compte.    

### Langue et style  
*	Les tutoriels ne doivent pas excéder 8000 mots (y compris le code)
*	Veillez à garder un ton formel mais accessible
*	Nous vous conseillons d'utiliser la deuxième personne du pluriel (*vous*) pour vous adresser à votre lectorat 
*	Merci de veiller à ce que votre français soit compréhensible dans tout l'espace francophone 
*	Souvenez-vous que vous rédigez un tutoriel ou une leçon, mais pas un article académique

À tout moment, en cas de doute, vous pouvez vous adresser au membre de notre équipe qui assure le suivi éditorial de votre leçon pour obtenir plus de clarifications, si nécessaire.    

### Open source, libre accès
Le *Programming Historian en français* adhère aux principes de l’open source et du libre accès. Toutes les leçons doivent utiliser des langages de programmation et des logiciels à code source ouvert et libres dans la mesure du possible. Cela minimise les coûts pour toutes les parties impliquées dans la création et la réception des leçons et garantit leur utilisation la plus large possible.   

### Écrire pour un public international
Le lectorat du *Programming Historian* vient du monde entier et travaille au sein d'environnements culturels variés. Merci de garder à l'esprit que le *Programming Historian en français* s'adresse à tous les pays francophones et que, de plus, votre leçon est susceptible d'être traduite dans l'une des langues de nos différentes publications. C'est pourquoi les auteur(e)s doivent veiller à écrire leurs leçons de façon à ce qu'elles soient accessibles à un lectorat diversifié. Merci donc de faire preuve d'un esprit large et de faire attention aux conseils suivants&#x202F;:

- Soyez conscient(e) de la diversité de votre lectorat qui peut ne pas venir de votre pays ou partager les mêmes croyances que vous.
- **Termes techniques**&#x202F;: merci d'insérer un lien pointant à Wikipédia, à un dictionnaire fiable ou à un site web pérenne lorsque vous introduisez des termes techniques dans votre texte. Par &laquo;&#x202F;terme technique&#x202F;&raquo; nous entendons tout mot qu'un(e) citoyen(ne) non-initié(e) peut ne pas connaître ou comprendre.
- **Références culturelles**&#x202F;: les mentions de personnes ou d'organisations doivent toujours être accompagnées d'informations contextuelles. Ne prenez aucune connaissance générale ou référence populaire pour acquise et n'hésitez pas à ajouter des liens vers [Wikipédia](https://fr.wikipedia.org/) (par exemple, en parlant d'[Astérix](https://fr.wikipedia.org/wiki/Ast%C3%A9rix)). Faites de même pour les événements et informations historiques, sans oublier qu'il peut exister différentes perceptions et dénominations d'un pays à l'autre. Aussi, préférez les termes génériques aux marques de commerce [pour désigner certains produits ou services](https://fr.wikipedia.org/wiki/Nom_de_marque_lexicalis%C3%A9) (par exemple, *ruban adhésif* à la place de *scotch*).
- **Langage**&#x202F;: au cours de la rédaction, merci d'éviter les plaisanteries, les calembours, les jeux de mots, le sarcasme ou les émojis. Veillez aussi à ne pas utiliser une syntaxe qui serait plus compliquée que nécessaire.
- **Géographie**&#x202F;: lorsque vous faites référence à des lieux géographiques, merci de le faire avec précision et en énonçant clairement d'où vous parlez. La &laquo;&#x202F;côte atlantique&#x202F;&raquo;, est-elle celle de la France, du Sénégal ou du Canada&#x202F;? Parlez-vous des &laquo;&#x202F;Cantons de l'Est&#x202F;&raquo; de la Belgique ou de ceux du Québec&#x202F;? Veillez aussi à toujours écrire le nom complet d'une région lors de la première mention.  
- **Multilinguisme**&#x202F;: merci de vous assurer que votre choix de méthodes et d'outils tient compte des besoins d'un lectorat multilingue. Cela est particulièrement important pour les méthodes d'analyse de données textuelles, qui doivent être fonctionnelles pour des jeux de données utilisant des caractères codés (par exemple, caractères accentués, non latins, etc.) et pertinentes dans plus d'une langue. Dans la mesure du possible, votre choix de méthodes et d'outils doit se faire en fonction de l'existence d'une documentation multilingue ou de références bibliographiques disponibles dans plusieurs langues - ce qui peut faciliter la traduction de votre leçon.
- **Variantes du français**&#x202F;: en général, nous déconseillons l'utilisation d'expressions trop idiomatiques ou propres à un dialecte. Néanmoins, nous souhaitons aussi que les auteur(e)s puissent appliquer la variante linguistique du français avec laquelle ils et elles se sentent le plus à l'aise. Ces questions peuvent être discutées avec votre rédacteur ou rédactrice dans le ticket d'évaluation de votre leçon.       
- **Vocabulaire lié aux origines ethniques et culturelles**&#x202F;: en français, le terme &laquo;&#x202F;race&#x202F;&raquo; n'est pas considéré comme étant applicable à l'espèce humaine. Merci d'utiliser toute terminologie liée à l'appartenance ethnique et culturelle avec prudence, précision et en plaçant dans son contexte historique tout terme qui n'est plus pertinent ou qui peut être interprété de plusieurs manières. Il est préférable d'utiliser les termes raciaux comme des adjectifs et non comme des noms - des &laquo;&#x202F;personnes blanches&#x202F;&raquo; plutôt que des &laquo;&#x202F;Blancs&#x202F;&raquo;, une &laquo;&#x202F;femme asiatique&#x202F;&raquo; plutôt qu'une &laquo;&#x202F;Asiatique&#x202F;&raquo;. Sachez que les termes peuvent être compris différemment selon les pays et que ce que vous savez être acceptable ou, au contraire, inapproprié peut être culturellement spécifique à votre pays. En anglais, par exemple, les lecteurs du Royaume-Uni comprendront le terme &laquo;&#x202F;asiatique&#x202F;&raquo; (Inde, Pakistan, Bangladesh) différemment de ceux d'Amérique du Nord (Chine, Japon, Vietnam, Thaïlande).
- **Représentations visuelles**&#x202F;: quand, dans le cadre de votre leçon, vous choisissez des images et des sources primaires, lorsque vous produisez des illustrations ou quand vous faites des copies d'écran, pensez à la manière dont celles-ci vont être perçues par un public international.
- **Environnement technique et logiciel**&#x202F;: si votre leçon nécessite l'installation de plusieurs composantes logicielles ou l'utilisation de ressources considérables, merci d'en prévenir les lecteurs et lectrices au tout début de la leçon (après le sommaire). Merci de donner des indications précises en expliquant pourquoi, par exemple&#x202F;: &laquo;&#x202F;vous aurez besoin d'au moins 8GB de mémoire RAM disponibles pour achever cette leçon&#x202F;&raquo; ou &laquo;&#x202F;cette leçon utilise des fichiers volumineux de l'ordre de 2GB&#x202F;&raquo;. Précisez aussi, le cas échéant, si l'installation de logiciels nécessite de disposer des droits d'administration.     

### Écrire de manière durable  
Le *Programming Historian en français* s'efforce de publier des leçons qui restent utiles à notre lectorat sur le long terme. Pour assurer la création de leçons pérennes, nous vous demandons de garder à l'esprit un certain nombre de consignes lors de leur rédaction :

- **Rester à un niveau général le plus possible sans aller au-delà**&#x202F;: axez davantage votre leçon sur les méthodologies et sur une présentation plus générale des outils, plutôt qu'aux détails de l'utilisation de tel logiciel ou de telle interface. Il vaut mieux éviter de guider les lecteurs et les lectrices pour montrer comment cliquer sur tel ou tel bouton qui risque d'être obsolète dans de futures versions.
- **Réduire la dépendance d'éléments peu durables**&#x202F;: limitez l'usage d'images spécifiques à la version du logiciel présenté (par exemple, des captures d'écran) au minimum requis pour suivre votre leçon. Les interfaces des logiciels changent fréquemment et, le cas échéant, des images obsolètes peuvent semer la confusion chez les futurs lecteurs. De même, si vous mobilisez des liens externes, guidez-vous dans vos choix en vous projetant dans l'avenir. Pensez, par exemple, si le site web vers lequel votre lien pointe, change souvent ou encore s'il est susceptible d'exister d'ici dix ans.    
- **Préciser si la version d'un logiciel est un élément important**&#x202F;: fournissez toutes les informations dont vos lecteurs et lectrices ont besoin pour savoir si votre leçon est compatible avec toutes les versions des logiciels que vous mobilisez. Par exemple, est-elle exécutable seulement avec la version 4 de R ou avec n'importe quelle version&#x202F;? 
- **Renvoyer à la documentation**&#x202F;: si votre leçon peut tirer profit de la documentation d'un logiciel existant, dirigez votre lectorat vers cette documentation aussi souvent que cela est possible. Aussi, fournissez des conseils généraux sur la manière dont il est possible de trouver la documentation si de nouvelles versions sont susceptibles de paraître dans l'avenir.
- **Fournir des copies des jeux de données de la leçon**&#x202F;: toutes les données mobilisées dans une leçon doivent être disponibles, au moment de la publication de celle-ci, sur les serveurs du *Programming Historian*. Vous devez avoir le droit de redistribuer une copie de ces données et de les mettre à disposition dans un format ouvert.
Les auteur(e)s doivent consulter notre [politique de retrait des leçons]({{site.baseurl}}/fr/politique-retrait-lecons), qui décrit comment l'équipe éditoriale du *Programming Historian en français* gère les leçons qui sont devenues obsolètes. 


## B. Règles typographiques  

Cette partie se concentre davantage sur des conventions d'écriture à propos des dates, des nombres, des en-têtes, des listes, de l'usage des majuscules ou de la ponctuation, ainsi que de l'application de l'écriture inclusive. Vous pouvez vous y référer avant et après l'écriture de votre brouillon. 

### Dates et heures
* Les siècles doivent s'écrire en chiffres romains, si possible en petites capitales (vous pouvez utiliser le code HTML&#x202F;: ``` <span style="font-variant:small-caps;"> ```), avec le &laquo;&#x202F;&#x202F;e&#x202F;&raquo; final en exposant (code HTML&#x202F;: ``` <sup> ```), par exemple <span style="font-variant:small-caps;">XVIII</span><sup>e</sup> siècle.

* La mention des décennies, plus particulièrement usitée pour le <span style="font-variant:small-caps;">XX</span><sup>e</sup> siècle, peut se formaliser soit en toutes lettres (les années trente), soit en donnant tous les chiffres de l’année (les années 1930).

* N’abrégez pas les millésimes pour les intervalles de dates. Privilégiez donc l'écriture des intervalles sous la forme suivante&#x202F;: 1854-1864, 1967-1974, par exemple.

* Pour les dates écrites au format numérique, respecter la norme ISO 8601:2004 (AAAA-MM-JJ).

* Pour marquer les dates avant ou après Jésus-Christ, abréger sous la forme &laquo;&#x202F;av. J.-C.&#x202F;&raquo; ou &laquo;&#x202F;apr. J.-C.&#x202F;&raquo;.

* Pour les heures, deux options sont envisageables :
	* écrire toutes les mentions &laquo;&#x202F;heures&#x202F;&raquo; (h), &laquo;&#x202F;minutes&#x202F;&raquo; (min) et &laquo;&#x202F;secondes&#x202F;&raquo; (s) en abrégé (10&nbsp;h&nbsp;10&nbsp;min), avec une espace insécable (indiqué comme ceci en HTML : ``` &nbsp; ``` ou `&#x202F;`) entre l'abrévation et le chiffre
	* écrire au format numérique avec un double point précédé d'une espace insécable (16&nbsp;:10)

* Pour indiquer les durées, écrire les mentions &laquo;&#x202F;heures&#x202F;&raquo;, &laquo;&#x202F;minutes&#x202F;&raquo; et &laquo;&#x202F;secondes&#x202F;&raquo; en toutes lettres (10 heures 10 minutes).


### Nombres 
 * Écrire les nombres en lettres de 1 à 16 (un à seize) et en chiffres les nombres supérieurs. 
 * Écrire le(s) nombre(s) commençant une phrase en toutes lettres. Toutes les variétés de la langue française sont acceptées (par exemple, *septante* ou *soixante-dix* pour 70). 
 * Si deux nombres sont cités dans une phrase, dont l'un devrait s'écrire en lettres et l'autre en chiffres, écrire tous les deux préférablement en chiffres ou, si le contexte oblige, tous les deux en lettres (par exemple, *nous avons fusionné 3 des 26 colonnes de notre tableau*; ou *Trois des vingt-six colonnes de notre tableau ont été fusionnées*. Il faut donc éviter de mélanger les formes dans une même phrase. Le plus important est de se fixer une règle et de s'y tenir.  
 *	Écrire les nombres en chiffres dans les tableaux et les formules statistiques et techniques du texte.
 *	Utiliser l'espace insécable pour séparer les nombres en tranches de trois chiffres, lorsqu'il s'agit de grands nombres, tant dans la partie des entiers que dans celle des décimales (par exemple, *31&#x202F;589*, *4,321&#x202F;078*). Pour les nombres composés de quatre chiffres, cela est facultatif et il vaut mieux préférer la formule sans espace insécable (*3200* plutôt que *3&#x202F;200*). En revanche, les numéros, les dates et tout autre chiffre ayant une fonction de numérotation ne se séparent pas.  
 *	Écrire les nombres en chiffres pour indiquer les versions (*version 5* ou *v.5*), les poids et mesures, les pourcentages, les fractions et nombres décimaux, les sommes (par exemple, 55&#x202F;%, 17 °C, 200 €).
 *	Pour exprimer le pourcentage, écrire le nombre accompagné du signe % séparés par une espace insécable; écrire le pourcentage en toutes lettres (*pour cent*) seulement au début d'une phrase. 
 *	Écrire les formules mathématiques en syntaxe [LaTeX](https://fr.wikibooks.org/wiki/LaTeX/%C3%89crire_des_math%C3%A9matiques).
   

### En-têtes 
Les en-têtes ne doivent pas faire appel à des polices de caractères spécifiques ou à des propriétés telles que *l'italique* ou **le gras**.

Les titres doivent immédiatement précéder le corps du texte de l'en-tête.

Ne pas faire suivre un titre d’une mise en garde ou d’un autre titre sans un court texte introductif ou descriptif.


### Listes     
Nous utilisons les listes à puces ou à nombres. Les items de listes doivent être limités à une phrase. Ils sont traités comme des entités séparées et ne doivent pas être enchaînés avec de la ponctuation et des conjonctions. 

Ne pas écrire:

* Voici un item, et
* voici un autre item; et
* voici le dernier item.

Écrire:

* Voici un item
* Voici un autre item
* Voici un dernier item
	
Ou bien écrire:

1. Voici un item
2. Voici un autre item
3. Voici un dernier item


### Ponctuation   
* **Abréviations**&#x202F;: concernant les [abréviations proprement dites](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?Th=1&Th_id=153&niveau=), merci d'en limiter l'utilisation pour éviter de rendre le texte difficilement compréhensible. Pour des abréviations spécifiques, tels [les sigles et les acronymes](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?Th=1&Th_id=157&niveau=), commencer par donner la signification lors du premier emploi dans le texte et la faire suivre par l'abréviation entre parenthèses&#x202F;; par la suite, utiliser uniquement la forme abrégée. Par exemple, après avoir évoqué l'Union européenne (UE) une première fois, écrire par la suite seulement l'UE. Privilégier l'écriture des sigles sans points abréviatifs et en majuscules non accentués&#x202F;: OCDE pour Organisation de coopération et de développement économique, CNRS pour Centre national de la recherche scientifique... 
* **Esperluette ou perluète**&#x202F;: ne pas l'utiliser comme conjonction de coordination à la place de &laquo;&#x202F;et&#x202F;&raquo; pour joindre deux noms communs, mais seulement lorsque référence est faite à des [noms d’entreprises entre deux patronymes, prénoms ou initiales](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?id=3330). 
* **Parenthèses / crochets**&#x202F;: pour éviter de décharger du texte accessoire entre parenthèses, tels les commentaires, les précisions etc., il vaut mieux utiliser des virgules ou des tirets. Utiliser néanmoins systématiquement les parenthèses pour apporter des précisions sur des termes techniques en anglais, par exemple des éléments de l'interface d'un logiciel ou de code, lorsque vous fournissez la traduction en français dans le texte.  
* **Deux-points**&#x202F;: l'utiliser pour introduire des listes, du texte explicatif, des définitions, des citations, du discours direct, sans attribuer le majuscule au premier mot de la phrase qui suit le deux-points. Ce signe est précédé d'une espace insécable fine. Voici quelques exemples : 
    *  Cette incertitude résulte de la combinaison des différentes sources d’erreur au sein du laboratoire&#x202F;: il s’agit d’une incertitude aléatoire inhérente à la mesure.
    *  Nous sommes d'accord avec Tim Berners-Lee pour dire : &laquo;&#x202F;We want raw data now&#x202F;!&#x202F;&raquo;
    *  La conservation des données de la recherche dans un format numérique a clairement des avantages par rapport au précédent format physique&#x202F;: elles peuvent être parcourues et fouillées, hébergées d’une façon qui permette un accès depuis de nombreux endroits, fusionnées ou croisées avec d’autres données de la recherche.
* **Virgule**&#x202F;: s'en servir pour juxtaposer des mots qui ont la même fonction, séparer des phrases, ou encore pour encadrer du texte qu'il serait possible de soustraire, à la place des parenthèses. Voici quelques exemples&#x202F;: 
    * Trois méthodes sont abordées&#x202F;: les courbes caractéristiques de composition de Mendenhall, la méthode du khi carré de Kilgariff et, enfin, la méthode du Delta de John Burrows.
    * Si vous ne voulez pas inclure une option de tri, vous pouvez l’ignorer.
    * Les expressions régulières, ou regex pour faire court, sont une façon de définir un motif qui peut s’appliquer à une séquence d’éléments.   
* **Tiret**&#x202F;: utiliser une paire de tirets pour introduire une précision, un commentaire etc., comme il est possible de faire avec des parenthèses ou des virgules. Préférer les tirets lorsqu'il s'agit de mettre en valeur la partie en question. Au milieu du texte, utiliser une paire de tirets, en revanche, si la précision intervient à la fin d'une phrase, elle est introduite par un tiret et suivie par un point. Espacer avant et après le tiret.
* **Points de suspension**, soit les trois points alignés l'un après l'autre sans espace entre eux. Leur usage marque en général l'inaccompli, une phrase laissée en suspens ou encore le silence. Les utiliser pour condenser une phrase trop longue ou pour éviter d'énumérer plusieurs éléments l'un après l'autre. Vous pouvez consulter des exemples d'emploi des points de suspension [ici](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?id=3396).  
* **Point d'exclamation**&#x202F;: l'utiliser pour marquer une exclamation, une interjection, une interpellation, par exemple&#x202F;: 
	* &laquo;&#x202F;Je suis une plante en pot. C’est vraiment ennuyeux&#x202F;!&#x202F;&raquo; 
	* Assurez-vous d’avoir une liste complète de fichiers&#x202F;!  

L'utilisation d'une espace insécable fine avant le point d'exclamation est recommandée en France, au Québec et en Suisse, mais sa suppression est tolérée dans les deux derniers pays, enfin, en Belgique il n'y a pas d'espacement. Merci de consulter la partie spéciale sur l'espacement à la fin de cette section.   
*  **Point**&#x202F;: Ne pas hésiter à l'utiliser fréquemment pour construire des phrases courtes et pertinentes, plutôt que des phrases longues et compliquées. Cela permet d'obtenir un texte percutant et facile à comprendre. Vous pouvez employer le point pour marquer la fin d'une phrase (point final), mais aussi pour abréger un mot (point abréviatif), pour écrire, par exemple, &laquo;&#x202F;fig. 1&#x202F;&raquo; à la place de &laquo;&#x202F;figure 1&#x202F;&raquo;. En revanche, n'utilisez pas le point abréviatif dans l'écriture de sigles&#x202F;: &laquo;&#x202F;les données statistiques de l'Insee&#x202F;&raquo;, &laquo;&#x202F;Bibliothèque et Archives nationales du Québec (BAnQ) conserve le patrimoine documentaire québécois&#x202F;&raquo;, &laquo;&#x202F;la base de données de recherche du Fonds national suisse (FNS)&#x202F;&raquo;.  
* **Trait d'union**&#x202F;: Il s'agit d'un tiret court qui n'est ni précédé ni suivi par un espace, sauf il s'agit d'exprimer des horaires. Ne pas confondre son usage avec celui du tiret. Le trait d'union est employé pour joindre de différents mots et créer ainsi de nouvelles unités, notamment des mots composés. Il peut aussi servir de liaison grammaticale lors de l'inversion pronominale. 
    *  Mots composés&#x202F;: le trait d'union sert de lien qui joint deux ou plusieurs mots pour en créer un nouveau (chef-lieu, mot-valise, petit-dejeuner, tête-à-tête...). Pour les mots composés d'une préposition ou d'un adverbe (contre, entre, hors, mal, non, par, quasi, sous), merci de consulter [le tableau synthétique de l'Office québécois de la langue française](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?Th=2&t1=&id=4337).
    *  Toponymes&#x202F;: dans une dénomination composée, tous les éléments sauf l’article initial sont liés entre eux par des traits d’union. Pensez à la ville de La-Roche-en-Ardenne en Belgique ou encore au quartier Val-Bélair de la ville de Québec, appartenant à l'arrondissement de La Haute-Saint-Charles.   
    * Noms de personnes&#x202F;: le trait d'union s'emploie pour lier des prénoms ou des noms composés tels Jean-Paul Benzécri, Brigitte Escofier-Cordier...    
    * Points cardinaux&#x202F;: les points cardinaux composés sont liés par un trait d'union, comme par exemple, pour indiquer une orientation nord-ouest ou encore le Sud-Est des États-Unis etc.
    *  Écriture des nombres&#x202F;: dans les nombres composés, tous les numéraux, adjectifs et noms, ainsi que la conjonction &laquo;&#x202F;et&#x202F;&raquo;, sont reliés par un trait d'union. Par exemple, trois-mille-dix-sept, quarante-et-un, sept-cent-soixante-et-un. 
    *  Écriture des fractions&#x202F;: elle suit, naturellement, l'écriture valable pour les nombres et l'utilisation du trait d'union a aussi le mérité de désambiguïser. Ainsi, écrire trente-et-un tiers renvoie à 31/3, tandis que trente et un tiers à 30 + 1/3.
    * Inversion pronominale&#x202F;: lors de l'inversion du verbe et du pronom dans une phrase interrogative ou impérative, le trait d'union marque le lien entre ces deux éléments. Voici quelques exemples tirés de nos tutoriels: 
        * Assurez-vous de rester dans ce répertoire de travail courant et d’y sauvegarder tout le travail que vous réaliserez en suivant le tutoriel. 
        * Rappelez-vous, encore une fois, que la construction de corpus est un sous-domaine à part entière.
        * Essayez d’appuyer sur le bouton jaune *Trier*. Que se passe-t-il maintenant ?
* **Guillemets français**&#x202F;: ils sont utilisés pour entourer un discours rapporté (citation, discours direct) ou pour indiquer de manière distincte un ou plusieurs mots (par exemple, un terme ou une phrase dans une autre langue). Une espace insécable suit le guillemet ouvrant et précéde le guillemet fermant &laquo;&#x202F;comme ici&#x202F;&raquo;. Des phrases entre guillemets peuvent s'imbriquer&#x202F;; dans ce cas, la première est placée entre guillemets français, la deuxième entre guillemets anglais doubles (doubles apostrophes), la troisième entre guillemets anglais simples (une paire d'apostrophes). Il est à noter que les guillemets anglais sont accolés aux mots qu'ils entourent.

#### Règles d'espacement avant/après les principaux signes de ponctuation et autres symboles
Les règles typographiques ne coïncident pas toujours entièrement entre les différents pays francophones, bien qu'elles se recoupent dans leurs grandes lignes. Merci de retenir que nous conseillons l'utilisation de l'espace insécable avec les guillemets français, devant le symbole de pourcentage et devant le deux-points. Aussi, d'insérer si possible l'espace insécable fine devant le point-virgule, le point d’exclamation et le point d’interrogation, si votre éditeur de texte le permet ou à l'aide des codes suivants&#x202F;:
* `&nbsp;` ou `&#x00A0;` pour l'espace insécable
* `&#x202F;` pour l'espace insécable fine

Merci de vous référer aux [recommandations sur l'espacement](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?t1=1&id=2039) de l'Office québécois de la langue française. 

### Usage des majuscules  
Les majuscules, à utiliser avec parcimonie dans la prose courante, peuvent se diviser en trois catégories&#x202F;:

* Les majuscules de position (en début de phrase ou à chaque alinéa dans une liste énumérative)
* Les majuscules de signification pour supprimer une ambiguïté
* Les majuscules elliptiques pour distinguer les noms propres des noms communs

Les majuscules sont aussi concernées par les accents, le tréma ou la cédille, même dans le cas des abréviations, mais pas pour les sigles et les acronymes. Les différents cas décrits ci-dessous résument les particularités dans l'usage des majuscules en français. 

* Le cas des **titres** :
	* Si le titre ne débute pas par un article défini (le, la, les), seul le mot initial prend la majuscule (exemple : *Une saison en enfer*).
	* Si le titre débute par un article défini (le, la, les), ou bien seul l’article prend une majuscule, ou bien l'article et le premier substantif, ainsi que les adjectifs et adverbes qui précèdent le substantif (exemple : *Les Liaisons dangereuses*). Si le titre contient une comparaison ou une symétrie, l'article défini prend une majuscule ainsi que chaque terme mis en symétrie (exemple : *La Belle et la Bête*).
	* Si nous sommes face à des titres doubles séparés par la conjonction &laquo;&#x202F;ou&raquo;&#x202F;, les règles ci-des&laquo;&#x202F;us s'appliquent à chacune des deux parties du titre. Cependant, l'article défini débutant la seconde partie perd la majuscule (exemple&#x202F;: *Le Mariage de Figaro ou la Folle Journée*).

* Les cas toujours en majuscule :
	* Les **noms propres**
	* Les **cérémonies et festivités** (exemple&#x202F;: la Semaine Sainte)
	* Les **évènements historiques**, car ils sont assimilés à des noms propres (exemple&#x202F;: la Fronde)
	* Les **livres sacrés**. Les mots Bible, Écriture et Évangile prennent une majuscule s’ils désignent le recueil de textes religieux, ainsi que les mots Ancien Testament, Nouveau Testament ou Coran. Le mot &laquo;&#x202F;bible&raquo;&#x202F; perd toutefois sa majuscule quand il désigne un livre faisant autorité.

* Les cas partiellement en majuscule :
	
	* Les **organisations artistiques, culturelles ou gouvernementales**, les **institutions et établissements** :
		* Pour les organismes d’État uniques, la majuscule s'applique au premier mot nécessaire à l’identification, et à l’adjectif qui précède (exemple&#x202F;: le Conseil constitutionnel). 
		* Pour les organismes d’État non uniques, conserver les minuscules, sauf lorsque les substantifs et les éventuels adjectifs qui les précédent font office de nom propre (exemple&#x202F;: le ministère des Affaires étrangères).
		* Pour les régimes politiques, s'ils désignent implicitement un pays ou une époque, ils prennent une majuscule, ainsi que l'adjectif qui précède (exemple&#x202F;: la Restauration). Ils conservent toutefois une minsucule quand ils désignent directement un type de régime politique (exemple : rétablir la république), ou bien quand ils sont accompagnés d'un nom propre (exemple&#x202F;: la république de Weimar).
		* Les mots Secrétariat et Département prennent une majuscule (exemple&#x202F;: le Département d’économie de Sciences Po).
		* Pour les établissements d’enseignement, s'ils sont d’importance nationale, on met une majuscule au premier substantif et à l'éventuel adjectif qui le précède (exemple&#x202F;: le Collège de France). S'il est d’importance régionale ou locale, les noms communs s'écrivent en minuscules, et on ajoute une majuscule aux noms propres qui l'identifie (exemple&#x202F;: université Paris-Descartes).
		* Le mot faculté ne prend la majuscule initiale que lorsqu'il désigne le corps médical. De même, le mot université ne prend la majuscule initiale que lorsqu'il désigne le corps enseignant. Les disciplines ne prennent pas de majuscule (exemple&#x202F;: la faculté des lettres et sciences humaines).
		* Pour les agences, commissions, établissements publics, organisme non-gouvernemental, la majuscule est placée sur le terme générique par lequel commence le nom officiel d’une institution, d’une administration, d’un service de l’État ou d’un organisme international, de même qu’à l’adjectif qui le précède (exemple&#x202F;: l’Union postale universelle).

	* Les **lieux** : 
		* Les noms de pays, provinces, régions, ou villes prennent une majuscule, mais pas les adjectifs adjoints aux noms propres (exemple : l'Italie méridioniale), sauf s’ils font office de noms propres (exemple : le Grand Nord).
		* Les noms communs d’entités géographiques restent en minuscules (exemple&#x202F;: la mer). Si les noms communs d’entités géographiques sont suivis par un nom qualifiant, seul ce dernier a une majuscule (exemple&#x202F;: le golfe du Lion). De même pour les monuments ou les jardins (exemple&#x202F;: la tour Eiffel).
		* Les lieux désignant un produit connu devenu nom commun ne prennent pas de majuscules (exemple&#x202F;: un bourgogne).
		* Les planètes, les étoiles et les signes du zodiaque prennent toujours une majuscule.

	* En ce qui concerne les mots relevant de la **religion**, on met une majuscule quand on désigne l’institution ou l’ensemble des fidèles (exemple&#x202F;: Église, Ouma), mais le bâtiment religieux s'écrit avec une minuscule. On met une majuscule pour les mots Dieu, Jésus et leurs synonymes et équivalents comme le Verbe, le Créateur, Allah, Bouddha, etc. Le mot &laquo;&#x202F;saint&#x202F;&raquo; ne prend pas de majuscule quand il désigne un personnage (exemple: saint François d'Assises), mais il faut en mettre une quand il fait partie d'un nom propre (exemple&#x202F;: Saint Louis) ou d'un nom propre composé (exemple&#x202F; l’île Saint-Louis).

	* Dans le cas de métiers, les **noms des fonctions, de charges ou de titres civils ou militaires** ne prennent pas de majuscules, sauf pour :
		* Les titres ayant eu un seul détenteur assimilable à un nom propre (exemple&#x202F;: le Duce).
		* La désignation d’une personne précise, auquel cas il faut éviter de créer une ambiguïté dans le texte pour l'antonomase (exemple&#x202F;: le Général pour désigner le général de Gaulle).
		* Les titres honorifiques (exemple&#x202F;: Sa Majesté).

	* Pour les **comités, rapports et enquêtes**, on met une majuscule au terme (Programme, Projet, Plan, ...) suivi d’un adjectif ou d’un complément quand il est compris dans le nom officiel d’une activité (exemple&#x202F;: le Plan vert). Il prend toutefois une minuscule quand le nom officiel de l’activité est placé en apposition (exemple&#x202F;: le plan Marshall).

* Les cas toujours en minuscule&#x202F;: 

	* Les noms de **doctrines**, qu'elles soient religieuses, philosophiques, artistiques ou politiques (exemple&#x202F;: l'existentialisme) ; de même pour ceux qui s’en réclament (exemple&#x202F;: les hindous), mais la majuscule est de mise pour ceux devenus des noms propres (exemple&#x202F;: la Nouvelle Vague)
	* Les **saisons** (exemple&#x202F;: le printemps)
	* Les **monnaies** (exemple&#x202F;: trois livres tournois)

Pour plus de précisions, vous pouvez consulter la banque de dépannage linguistique de l'Office québécois de la langue française, avec une liste de l'emploi de la majuscule pour des [types de dénominations](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?th=1&th_id=280) et une autre pour les [noms particuliers](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?th=1&th_id=281).  

### Références bibliographiques  
*   Pour les notes de fin, merci d'utiliser le style de citation [*The Chicago Manual of Style*, 17e édition](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html) adapté aux règles typographiques de la langue française.
*   Mobiliser des hyperliens dans le texte plutôt que d'insérer des notes de fin peut convenir dans la plupart de cas.   
*   La phrase source d'un hyperlien doit être sémantique, éviter par conséquent des phrases du type &laquo;&#x202F;cliquer ici&#x202F;&raquo;.
*   Utiliser des notes de fin pour renvoyer aux références bibliographiques académiques, qu'elles soient électroniques ou publiées sur papier. 
*   Si votre tutoriel a vocation à être un tutoriel d'analyse (cf. [l'index des leçons](https://programminghistorian.org/fr/lecons/?activity=analyzing)), vous devez vous référer à la littérature savante publiée du domaine. 
*   Pour signaler une note de fin, placer le chiffre en exposant (appel de note) à l'endroit souhaité sans espacement après le mot. Le cas échéant, veiller à ce qu'il précède un point de ponctuation et non pas qu'il le suive. Par exemple, pour insérer une note de fin imaginaire dans cette phrase, le chiffre en exposant doit se placer avant le point final comme ceci². Mais il ne peut pas être placé de cette manière.²
*  Lorsque vous mentionnez un travail publié dans le texte, fournissez le nom complet de l'auteur(e) la première fois que vous le faites. Par exemple:
    * Vous pouvez trouver plus d'informations sur ce sujet dans _Histoire et linguistique_ de Régine Robin.
    * Pour en savoir plus, merci de consulter l'ouvrage de Régine Robin _Histoire et linguistique_. 
Si vous vous référez à nouveau au même ouvrage, vous pouvez par la suite fournir seulement le titre de l'ouvrage. Veillez à ne pas vous référer à un auteur avec son seul nom de famille que si vous renvoyez à ses travaux de manière répétée.  
*  Les notes de fin doivent fournir une référence complète et non pas renvoyer seulement à une URL&#x202F;:
    * Marine Riguet et Mohamed Amine Boukhaled, «&#x202F;La correspondance de motifs, un outil pour l’analyse du discours&#x202F;?&#x202F;», *Humanités numériques*, no. 1 (2020), https://doi.org/10.4000/revuehn.312 (note complète) 
    * Voir https://doi.org/10.4000/revuehn.312 (note incomplète) 
* Pour citer un logiciel, suivant les [recommandations](https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-software) du projet [Software Heritage](https://www.softwareheritage.org/), merci de fournir toute information disponible parmi les suivantes&#x202F;: auteur, titre, version, module, fragment de code (par exemple un algorithme spécifique dans un programme), année de parution, licence d'utilisation, URL d'entrepôt. Voici un exemple formatté selon le style *Chicago Manual*, 17e édition&#x202F;: 
    * Julien Barnier *et al.*. *Scatterd3*, version 1.0.1 (2021). GPL. https://cran.r-project.org/web/packages/scatterD3/index.html (en note de fin)
	* Barnier, Julien, Kent Russell, Mike Bostock, Susie Lu, Speros Kokenes, Evan Wang. *Scatterd3* (version 1.0.1). GPL. 2021.  https://cran.r-project.org/web/packages/scatterD3/index.html (en référence bibliographique)

### Écriture inclusive  
Nous appliquons l'écriture inclusive suivant les consignes de l'Office québécois de la langue française sur la [formation des noms féminins](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?Th=1&Th_id=358&niveau=) et la [rédaction épicène](http://bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?Th=2&t1=&id=3912), mises en place en 2002, ainsi que du [Guide d’aide à la féminisation des noms de métiers, titres, grades et fonctions](https://www.vie-publique.fr/sites/default/files/rapport/pdf/994001174.pdf), publié par l'Institut national de la langue française en 1999. Ces deux textes se recoupent largement et constituent des guides de base pour l'équipe du _Programming Historian en français_. En revanche, nous n'avons pas recours à l'utilisation du point médian (ou point milieu) ou de tirets. Ainsi, nous évitons d'écrire &laquo;&#x202F;les historien·ne·s&#x202F;&raquo; ou &laquo;&#x202F;les historien-ne-s&#x202F;&raquo;; nous privilégions à la place &laquo;&#x202F;les historiens et historiennes&#x202F;&raquo; ou encore &laquo;&#x202F;les historien(ne)s&#x202F;&raquo;, pour éviter d'alourdir le texte. De même, nous pouvons faire recours à l'emploi d'un nom collectif, en parlant, par exemple, du lectorat du *Programming Historian* plutôt que des lecteurs et des lectrices ou des utilisateurs et des utilisatrices.    

## C. Mise en forme
Cette section finale couvre les questions de mise en forme nécessaires pour soumettre une leçon. Merci de la lire attentivement aussi bien avant de vous lancer dans l'écriture qu'après avoir achevé votre première version. En cas d'erreur, vous pouvez toujours apporter des corrections au début du processus d'évaluation par les pairs à l'aide d'une prévisualisation de votre leçon.  

### Écrire en Markdown 
Toutes les leçons doivent être écrites en [Markdown](https://fr.wikipedia.org/wiki/Markdown). Nous fournissons [un modèle que vous pouvez utiliser pour écrire votre leçon]({{site.baseurl}}/fr/modele-tuto.md).  

Markdown est un langage de balisage. Vous pouvez l'écrire facilement en utilisant un éditeur de texte de votre choix. Attention, Microsoft Word et Open Office, qui ne sont pas des éditeurs mais des traitements de texte, sont à éviter. Nous recommandons plutôt l'utilisation des éditeurs suivants&#x202F;: [Atom](https://atom.io/), [TextWrangler](https://www.barebones.com/products/textwrangler/), [TextEdit](https://fr.wikipedia.org/wiki/TextEdit), [MacDown](https://macdown.uranusjr.com/) ou [Notepad++](https://notepad-plus-plus.org/downloads/). Si besoin, vous pouvez consulter notre leçon introductive [Débuter avec Markdown](/fr/lecons/debuter-avec-markdown).

Votre leçon doit être sauvegardée dans un fichier en format .md. Le nom de fichier définit l'URL de la leçon publiée, c'est pourquoi vous devez le nommer&#x202F;:
- En choisissant un nom descriptif court, en minuscules, qui indique clairement le contenu de la leçon (par exemple, debuter-avec-markdown.md)
- Sans utiliser des espaces ou des tirets bas, mais seulement des tirets
- En utilisant des mots-clés qui indiquent les technologies ou les méthodes mobilisées (par exemple, Python ou réutilisation de texte)

### Caractères en gras, italique et surlignés

#### Caractères en gras 
- Les caractères en gras ne sont utilisés qu'exceptionnellement. 
- La mise en gras se produit en utilisant **des paires doubles d'astérisques**.

#### Caractères en italique
- Les italiques sont utilisés pour indiquer des titres, des films, des émissions de télévision, des peintures, des chansons, des albums, des sites web. 
- Ne jamais utiliser les italiques pour indiquer les noms d'entreprises (par exemple, Facebook, Twitter...).
- La mise en italique se produit en utilisant *des paires d'astérisques*. 

#### Caractères surlignés 
Les caractères surlignés ne sont pas utilisés. 

### Alertes, messages importants
Si vous souhaitez attirer l'attention des lecteurs, vous pouvez ajouter un bloc à part dans le texte&#x202F;:

```
<div class="alert alert-warning">
 Attention à ces instructions, elles sont très importantes&#x202F;!
</div>
```
### Figures et images
Les images doivent pouvoir aider votre lectorat à mieux comprendre les étapes de votre leçon, elles ne doivent pas être purement illustratives. Si vous souhaitez en fournir avec votre leçon, nommez-les de manière ordonnée NOM-DE-LEÇON1.jpg, NOM-DE-LEÇON2.jpg, etc. puis, dans le texte, rappelez-les en tant que figure 1, figure 2... Toutes les figures doivent être accompagnées d'une brève légende et, le cas échéant, de notes. Vous devez disposer du droit de publier toute image que vous fournissez. 

Veillez à utiliser un format adapté à la publication web tel .png or .jpg et à réduire les grandes images à un maximum de 840px sur la longueur. Cela est important pour les lecteurs et les lectrices qui disposent des connexions internet à bas débit. 

Les images doivent être fournies dans un répertoire qui porte le même nom que votre fichier .md de leçon. Le rédacteur ou la rédactrice en charge du suivi éditorial de votre leçon peut vous aider à téléverser les images lorsque vous soumettez la leçon. 

Vous pouvez insérer une image dans votre texte à l'aide de cette syntaxe&#x202F;: 

{% raw %}
``` markdown
{% include figure.html filename="IMAGE-FILENAME" caption="VOTRE TITRE, AVEC \"CODE D'ÉCHAPPEMENT\" POUR LES GUILLEMETS" %}
```
{% endraw %}

N'oubliez pas que les guillemets à l'intérieur des titres des figures doivent être échappés à l'aide d'une barre oblique inverse, comme dans l'exemple ci-dessus. Il est important de noter que, lorsque les images sont encodées de cette manière, elles ne sont pas visibles dans la prévisualisation de votre leçon, mais votre rédacteur ou rédactrice s'assurera qu'elles soient affichées correctement lorsque la leçon sera publiée.

### Blocs de code
Si vous voulez inclure des lignes de code dans une leçon, il faut les distinguer clairement de la prose&#x202F;: 
* Les lignes de code ne doivent pas dépasser les 80 caractères 
* Les blocs de code multilignes doivent être entourés de paires de trois \`\`\`accents graves\`\`\`
* Le code sur la même ligne, à la suite du texte qui précède, doit être entouré d'une paire \`d'accents simples\` et il est rarement utilisé. 

```
Un bloc de code multilignes s'affiche de cette manière
```
` et le code sur la même ligne s'affiche ainsi`.

--
Merci de suivre les bonnes pratiques pour écrire votre code&#x202F;:

*	**Noms de variables et de fonctions**&#x202F;: préférez l'utilisation de noms pour nommer les variables (par exemple, counter ou compteur) et de verbes pour nommer les fonctions (par exemple, createFile ou creerFichier). Veillez à ne pas utiliser des signes diacritiques ou tout autre caractère qui, selon le langage que vous utilisez, pourrait provoquer des ambivalences dans la phase d'analyse syntaxique du programme. Choisissez des noms concis et signifiants sans diacritiques. Vous pouvez utiliser la convention de nommage de votre préférence, [snake_case](https://fr.wikipedia.org/wiki/Snake_case) ou [camelCase](https://fr.wikipedia.org/wiki/Camel_case), mais veillez à appliquer la même du début à la fin.
*	**Commande utilisateur**&#x202F;: lorsque vous souhaitez que vos lecteurs renseignent avec leurs propres informations une portion de texte, utilisez des MAJUSCULES entourés d'une paire `d'accents graves`, par exemple \`NOM D'UTILISATEUR ICI\`.
*	**Noms de fichiers**&#x202F;: les noms de fichiers que vous demandez aux utilisateurs de créer ou d'utiliser doivent être entourés d'une paire `d'accents graves` dans le texte et écrits avec leur extension. Choisissez des noms de fichiers concis et signifiants sans diacritiques. Vous pouvez utiliser la convention de nommage de votre préférence, [snake_case](https://fr.wikipedia.org/wiki/Snake_case) ou [camelCase](https://fr.wikipedia.org/wiki/Camel_case), mais veillez à appliquer la même du début à la fin, par exemple `donnees.txt`, `nettoyerDonnees.py` etc).
*	**Mots réservés**&#x202F;: les [mots réservés](https://fr.wikibooks.org/wiki/Cat%C3%A9gorie:Mots_r%C3%A9serv%C3%A9s) d'un langage de programmation doivent toujours être balisés comme du `code` dans un texte en utilisant une paire `d'accents graves`. Ci-dessous une liste des mots réservés de langages de programmation courants&#x202F;:

#### JavaScript:

`abstract`, `arguments`, `await`, `Boolean`, `break`, `byte`, `case`, `catch`, `char`, `class`, `const`, `continue`, `debugger`, `default`, `delete`, `do`, `double`, `else`, `enum`, `eval`, `export`, `extends`, `false`, `final`, `finally`, `float`, `for`, `function`, `goto`, `if`, `implements`, `import`, `in`, `instanceof`, `int`, `interface`, `let`, `long`, `native`, `new`, `null`, `package`, `private`, `protected`, `public`, `return`, `short`, `static`, `super`, `switch`, `synchronized`, `this`, `throw`, `throws`, `transient`, `true`, `try`, `typeof`, `var`, `void`, `volatile`, `while`, `with`, `yield`.

#### Python 2:
`and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `exec`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `not`, `or`, `pass`, `print`, `raise`, `return`, `try`, `while`, `with`, `yield`.

#### Python 3:
`and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `False`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `None`, `not`, `or`, `pass`, `raise`, `return`, `True`, `try`, `while`, `with`, `yield`.

#### R:
`break`, `else`, `for`, `FALSE`, `function`, `if`, `in`, `Inf`, `NA`, `NA_character_`, `NA_complex_`, `NA_integer_`, `NA_real_`, `NaN`, `next`, `NULL`, `repeat`, `TRUE`, `while`.


## Étape 3: soumettre une nouvelle leçon

Une fois que vous avez vérifié que votre leçon a été préparée en suivant les consignes données ci-dessus, nous vous conseillons de la faire relire et éventuellement d'apporter des corrections pour l'améliorer. Ainsi, l'évaluation ouverte par les pairs que nous allons organiser par la suite pourra se concentrer sur le fond, plutôt que sur la forme, afin de vous aider à produire la version la plus solide possible de votre leçon.   

Lorsque vous êtes prêt(e) à la soumettre, merci d'envoyer tous les fichiers (texte, images, données...) au rédacteur ou à la rédactrice en charge du suivi éditorial de votre leçon, qui les téléversera pour vous dans notre dépôt dédié à l'évaluation par les pairs sur [Github](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/fr/lecons). Voici comment procéder de votre côté: 

1. **Obtenir accès à notre dépôt d'évaluation**: pour cela il suffit de créer un [compte gratuit sur Github](https://github.com/join) et de le communiquer à votre rédacteur ou rédactrice, qui va ensuite vous ajouter comme **collaborateur ou collaboratrice** dans le dépôt [ph-submissions]. Ce n'est pas à vous de faire le téléversement initial des fichiers, mais l'accès au dépôt est nécessaire pour que vous puissiez par la suite apporter des modifications et des mises à jour. 
2. **Préparer vos fichiers**: vous avez probablement des images qui accompagnent votre leçon. Merci de vérifier que tous les fichiers images sont nommés de manière appropriée, en accord avec les [conventions de nommage spécifiées ci-dessus]. Ces fichiers doivent nous parvenir dans un dossier unique compressé. Si vous avez en plus des fichiers de données, merci de nous envoyer ces fichiers aussi dans un dossier compressé distinct.
3. **Envoyer un message électronique**: informez votre rédacteur ou rédactrice que vous êtes prêt(e) à soumettre votre leçon, en joignant le fichier de celle-ci et, le cas échéant, les dossiers des fichiers images et données. 
4. **Participer à la discussion**: le rédacteur ou la rédactrice en charge du suivi éditorial de votre leçon déposera vos fichiers dans notre [dépôt de soumissions](https://github.com/programminghistorian/ph-submissions) en faisant quelques premières modifications si nécessaire (métadonnées, syntaxe Markdown etc). Ensuite, un ticket sera ouvert pour l'évaluation ouverte de votre leçon, pendant laquelle vous avez la possibilité d'échanger avec celles et ceux qui participent au processus.
5. **Apporter des modifications**: si le dépôt initial des fichiers est fait par votre rédacteur ou rédactrice assigné(e), le processus éditorial peut néanmoins entraîner le besoin d'apporter des modifications supplémentaires de votre côté. Toutes les révisions se font directement par les auteur(e)s sur les fichiers versés dans notre dépôt pour avoir la certitude que vous travaillez sur la version la plus récente du fichier de la leçon.


## Le processus de l'évaluation ouverte par les pairs

Une fois que votre rédacteur ou rédactrice assigné(e) aura déposé et formaté vos fichiers de manière appropriée, vous recevrez un lien de prévisualisation de la leçon qui vous permettra de vérifier aussi de votre côté que tout se présente correctement&#x202F;; si ce n'est pas le cas, vous pouvez apporter des corrections. 

L'évaluation par les pairs a lieu dans le cadre d'un [ticket](https://github.com/programminghistorian/ph-submissions/issues) Github qui prend ainsi la forme d'un forum de discussion ouverte. Merci de garder à l'esprit que l'évaluation par les pairs se fait publiquement et qu'elle reste disponible à la consultation publique&#x202F;; le ticket en est l'enregistrement. Si pour quelque raison que ce soit vous n'êtes pas à l'aise ou souhaitez une évaluation par les pairs non publique, merci de prendre contact avec votre rédacteur ou rédactrice assigné(e). 

Le processus de l'évaluation se passe habituellement en trois étapes&#x202F;:

1) Le rédacteur ou la rédactrice assigné(e) à votre leçon en fait une première lecture attentive en testant les manipulations proposées. Vous êtes à ce stade susceptible de recevoir un premier retour qui pourrait solliciter votre réponse. L'objectif de ce premier retour est de se garantir la pertinence de votre leçon pour le lectorat du *Programming Historian en français* et qu'elle est fonctionnelle avant d'être proposée à l'évaluation externe. Vous avez normalement un mois pour répondre à cette première évaluation. 

2) Ensuite, votre rédacteur ou  rédactrice assigné(e) propose la leçon à l'évaluation formelle par les pairs. Cela implique l'invitation d'au moins deux évaluateurs ou évaluatrices externes, mais potentiellement aussi la participation d'une communauté plus large, car tout commentaire est bienvenu (pourvu que les règles de bonne conduite, explicitées dans le ticket, soient observées). En général, nous accordons aux évaluateurs et évaluatrices un délai d'un mois pour fournir leurs commentaires, il peut néanmoins arriver que ce délai ne soit pas respecté pour des raisons indépendantes de la volonté des personnes impliquées au processus. Vous devez attendre l'ensemble des relectures et les instructions consécutives de votre rédacteur our rédactrice assigné(e) avant d'aller plus loin. Parfois, il peut s'agir de simples suggestions d'apporter certaines modifications, mais il peut aussi être question de révisions majeures ou de repenser la leçon. Selon les évaluations des pairs et la nature des questions soulevées, il se peut que vous ayez à réviser le tutoriel plus qu'une fois. Toufois, votre rédacteur ou rédactrice assignée(e) veillera à ce que vous receviez une ligne directrice claire pour que la leçon soit publiée. Par ailleurs, il est toujours possible de retirer votre leçon du processus de l'évaluation, si tel est votre choix.   

3) Au bout de ce processus, si tous les critères sont remplis, votre rédacteur ou rédactrice assignée(e) donne le feu vert pour la publication. C'est ensuite au rédacteur ou à la rédactrice en chef de relire la leçon pour s'assurer de sa conformité aux consignes aux auteur(e)s et aux standards du *Programming Historian*. Parfois des révisions et des corrections supplémentaires peuvent être nécessaires à ce stade pour que la leçon puisse être publiée. Une fois que le rédacteur ou la rédactrice en chef juge la version révisée satisfaisante, la leçon peut être mise en ligne. Votre rédacteur ou rédactrice assigné(e) vous fournira toute information nécessaire à ce stade. 

N'hésitez pas à consulter nos [consignes aux évaluateurs et évaluatrices](/fr/consignes-evaluateurs) afin de vous familiariser avec notre processus de révision et de publication.

Si jamais vous êtes dans l'incertitude sur comment procéder, n'hésitez pas à poster votre question sur le ticket d'évaluation, un membre de notre équipe vous apportera des réponses dans les délais les plus brefs possible. Nous faisons de notre mieux pour répondre au bout de quelques jours.


### Que se passe-t-il une fois votre leçon publiée ?

Il nous arrive de recevoir des retours de notre lectorat nous signalant des erreurs dans nos leçons. Le cas échéant, notre assistante éditoriale va ouvrir un ticket sur GitHub pour confirmer si l'erreur signalée est due à une mauvaise manipulation de l'utilisateur ou de l'utilisatrice (modification du code, du jeu de données...) ou à un problème de la leçon. Dans ce dernier cas, notre assistante éditoriale va tester à nouveau la leçon et chercher une solution. Dans le cadre de ce processus de maintenance de nos leçons, nous pouvons être amenés à vous contacter aussi pour solliciter votre avis. Si une solution est impossible à trouver, nous proposerons de faire afficher un avertissement expliquant que certain(e)s de nos utilisateurs et utilisatrices pourraient rencontrer des problèmes. Lorsque cela est possible, l'avertissement devrait inclure des liens vers des ressources qui pourraient permettre aux utilisateurs et utilisatrices de trouver une solution.


### Nous interpeller

Notre équipe de bénévoles fait de son possible pour garantir l'évaluation rigoureuse, collégiale et efficace des auteur(e)s par les pairs. Toutefois, il peut y avoir des failles, c'est pourquoi nous souhaitons que les auteur(e)s nous aident à maintenir un haut niveau de service. Si, pour quelque raison que ce soit, vous estimez ne pas avoir été traité(e) correctement, ou ne comprenez pas trop quel est votre rôle ou ce qu’on attend de vous, ou encore si vous considérez que l'évaluation présente des retards injustifiés ou que quelqu'un a été incorrect(e) avec vous, enfin, pour quel autre souci que ce soit, n'hésitez pas à nous en tenir informés afin que nous puissions agir. 

Exprimer des réserves n'a AUCUN impact négatif sur le processus et le résultat de l'évaluation par les pairs. 

Pour ce faire, vous avez plusieurs points d'entrée - sentez-vous libre de contacter la personne avec laquelle vous êtes le plus à l'aise&#x202F;: 

* votre rédacteur ou rédactrice assigné(e) 
* le rédacteur ou la rédactrice en chef
* notre médiatrice indépendante ([Hélène Huet](mailto:hhuet@ufl.edu))

Nous œuvrons pour que tout se passe au mieux pour vous, mais si jamais vous estimez vous trouver dans une situation peu confortable, nous vous remercions de nous aider à y remédier et à améliorer les choses. 
