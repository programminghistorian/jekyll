---
title: "La reconnaissance automatique d'écriture à l'épreuve des langues peu dotées"
collection: lessons
layout: lesson
slug: transcription-automatisee-graphies-non-latines
date: 2023-01-30
authors:
- Chahan Vidal-Gorène
reviewers:
- Julien Philip
- Ariane Pinche
editors:
- Matthias Gille Levenson
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/421
difficulty: 3
activity: acquiring
topics: [machine-learning, data-manipulation]
abstract: Les systèmes de reconnaissance de texte manuscrit (*Handwritten Text Recognition* ou HTR) et imprimés (*Optical Character Recognition* ou OCR) atteignent des résultats de plus en plus précis dans tous les domaines, en particulier sur les manuscrits et documents historiques tapuscrits, malgré leurs disparités et leur absence de normalisation, grâce à l'intelligence artificielle. Ces systèmes ont besoin de données propres, en grand nombre et annotées correctement pour être entraînés efficacement et pour traiter de grandes bases de données. Construire des ensembles de données pertinents est une tâche qui prend du temps, même avec l'aide de plateformes dédiées. Le tutoriel a pour but de décrire les bonnes pratiques pour la création d'ensembles de données et la spécialisation des modèles en fonction d'un projet HTR ou OCR sur des documents qui n'utilisent pas l'alphabet latin et donc pour lesquels il n'existe pas ou très peu de données d'entraînement déjà disponibles. Le tutoriel a ainsi pour but de montrer des approches de *minimal computing* (ou d'investissement technique minimal) pour l'analyse de collections numériques à grande échelle pour des langues peu dotées. Notre tutoriel se concentrera sur un exemple en grec ancien, puis proposera une ouverture sur le traitement d'écritures arabes maghrébines manuscrites.
avatar_alt: Une initiale d'imprimerie représentant en son centre une figure écrivant à la main
mathjax: true
lesson-partners: [Jisc, The National Archives]
partnership-url: /jisc-tna-partnership
doi: 10.46430/phfr0023
---

{% include toc.html %}


## Cadre d'étude et objectifs de la leçon

Ce tutoriel présente des stratégies et bonnes pratiques pour constituer des données pertinentes et en quantité suffisantes pour reconnaître des écritures généralement peu ciblées dans les projets de reconnaissance de caractères. Le tutoriel est appliqué au traitement d'un imprimé, la Patrologie Grecque (PG), et propose une ouverture sur le traitement d'un document manuscrit de la [Bibliothèque universitaire des langues et civilisations (BULAC)](https://perma.cc/D9WP-TPPU) en écriture arabe maghrébine. Ces deux exemples sont très spécifiques mais la stratégie globale présentée, ainsi que les outils et approches introduits, sont adaptés au traitement de tout type de document numérisé, en particulier sur des langues peu dotées pour lesquelles une approche reposant sur la masse est difficilement applicable.

La PG est une collection de réimpressions de textes patristiques, théologiques et historiographiques publiée à Paris par Jacques-Paul Migne (1800-1875) entre 1857 et 1866. La PG compte 161 volumes et réunit des textes produits entre le I<sup>er</sup> et le XV<sup>e</sup> siècle, en commençant par les écrits de Clément de Rome --&nbsp;«&nbsp;pape&nbsp;» de 92 à 99&nbsp;-- pour se clôturer par ceux du cardinal Jean Bessarion (1403-1472). La PG ne contient pas que des textes théologiques –&nbsp;loin de là&nbsp;–, mais aussi de nombreux textes exégétiques, historiques, hagiographiques, législatifs, encyclopédiques, poétiques et même romanesques. En réalité, on y trouve la plus grande part de la littérature byzantine, qui fait la synthèse entre la culture grecque et l'héritage chrétien. Malgré leur intérêt incontestable pour la recherche, une partie de ces textes n'a plus été rééditée depuis la fin du XIX<sup>e</sup> siècle ou n'est toujours pas accessible dans une version numérique[^1]. Le projet Calfa GRE*g*ORI Patrologia Graeca (CGPG) a été créé pour combler cette lacune. L'association Calfa et le projet GRE*g*ORI, sous la responsabilité académique du professeur Jean-Marie Auwers (université catholique de Louvain) ont entrepris de rendre ces textes accessibles en ligne et d'en augmenter leurs contenus, dans un format interopérable, via des approches automatiques d'OCR et d'analyses lexicale et morphosyntaxique[^2].

<table>
<tr>
<td>
{% include figure.html filename="figure0_PG_125_625-626.jpg" alt="Exemple de pages en grec et en latin de la PG" caption="Figure&nbsp;0&nbsp;: Exemple de la PG (PG 125, c. 625-626)" width="200" %}</td>
<td>
{% include figure.html filename="figure0_PG_125_1103-1104.jpg" alt="Exemple de pages en grec et en latin de la PG" caption="Figure&nbsp;0&nbsp;: Exemple de la PG (PG 125, c. 1103-1104)" width="200" %}
</td>
</tr>
</table>
<!-- <p style="text-align:center;">
  <img src="figure0_PG_125_625-626.jpg" width="200" />
  <img src="figure0_PG_125_1103-1104.jpg" width="200" />
</p> -->

À l'issue de cette leçon, le lecteur ou la lectrice sera en mesure d'établir une stratégie et un cahier des charges adapté à la reconnaissance de caractères de documents actuellement non couverts par les modèles standards d'OCR (reconnaissance optique de caractères) et de HTR (reconnaissance de l'écriture manuscrite) généralement disponibles. Cette stratégie pourra se développer au sein de projets collaboratifs. La leçon initie également au fonctionnement d'une plateforme d'annotation de documents, Calfa Vision, sans toutefois exclure les autres plateformes. Le lectorat trouvera donc ici des méthodologies transposables. Enfin, la leçon introduit par l'exemple à des notions d'apprentissage machine. Elle ne nécessite pas de pré-requis particulier&nbsp;: quelques exemples en python et en XML sont présentés mais ils sont ajoutés à cette leçon en guise d'illustration. De même, les principes sous-jacents d'apprentissage machine sont introduits de zéro, parfois vulgarisés, et ne nécessitent pas de connaissances préalables. Néanmoins, il est recommandé de se renseigner sur les notions de base pour l'entraînement de réseaux de neurones --&nbsp;notions de jeux de données, d'ensemble d'apprentissage et de test&nbsp;-- afin de tirer profit au mieux de la leçon[^3].


## Introduction

### La reconnaissance de caractères

La transcription automatique de documents est désormais une étape courante des projets d'humanités numériques ou de valorisation des collections au sein de bibliothèques numériques. Celle-ci s'inscrit dans une large dynamique internationale de numérisation des documents, facilitée par le *framework* IIIF (*International Image Interoperability Framework*[^4]) qui permet l'échange, la comparaison et l'étude d'images au travers d'un unique protocole mis en place entre les bibliothèques et les interfaces compatibles. Si cette dynamique donne un accès privilégié et instantané à des fonds jusqu'ici en accès restreint, la masse de données bouleverse les approches que nous pouvons avoir des documents textuels. Traiter cette masse manuellement est difficilement envisageable, et c'est la raison pour laquelle de nombreuses approches en humanités numériques ont vu le jour ces dernières années. Outre la reconnaissance de caractères, peuvent s'envisager à grande échelle la reconnaissance de motifs enluminés[^5], la classification automatique de page de manuscrits[^6] ou encore des tâches codicologiques telles que l'identification d'une main, la datation d'un manuscrit ou son origine de production[^7], pour ne mentionner que les exemples les plus évidents. En reconnaissance de caractères comme en philologie computationnelle, de nombreuses approches et méthodologies produisent des résultats déjà très exploitables, sous réserve de disposer de données de qualité pour entraîner les systèmes.

<div class="alert alert-info">
On appelle reconnaissance de caractères la tâche qui permet le passage automatique d'un document numérisé au format texte interrogeable. On distingue classiquement l'OCR (<i>Optical Character Recognition</i>), pour les documents imprimés, de l'HTR (<i>Handwritten Text Recognition</i>), pour les documents manuscrits.
</div>

La leçon présente une approche reposant sur de l'apprentissage profond (ou *deep learning*), largement utilisé en intelligence artificielle. Dans notre cas, elle consiste *simplement* à fournir à un réseau de neurones un large échantillon d'exemples de textes transcrits afin d'entraîner et d'habituer le réseau à la reconnaissance d'une écriture. L'apprentissage, dit supervisé dans notre cas puisque nous fournissons au système toutes les informations nécessaires à son entraînement --&nbsp;c'est-à-dire une description complète des résultats attendus&nbsp;--, est réalisé par l'exemple et la fréquence.

Il est donc aujourd'hui possible d'entraîner des réseaux de neurones pour analyser une mise en page très spécifique ou traiter un ensemble de documents très particulier, en fournissant des exemples d'attendus à ces réseaux. Ainsi, il *suffira* d'apporter à un réseau de neurones l'exacte transcription d'une page de manuscrit ou la précise localisation des zones d'intérêts dans un document pour que le réseau reproduise cette tâche (voir figure&nbsp;1).

Il existe dans l'état de l'art une grande variété d'architectures et d'approches utilisables. Cependant, pour être efficaces et robustes, ces réseaux de neurones doivent être entraînés avec de grands ensembles de données. Il faut donc annoter, souvent manuellement, des documents similaires à ceux que l'on souhaite reconnaître --&nbsp;ce que nous appelons classiquement la création de «&nbsp;[vérité terrain](https://perma.cc/5FBF-24W2)&nbsp;» ou *ground truth*.

{% include figure.html filename="figure1_pipeline_training_1.jpg" alt="Schéma des étapes classiques pour l'entraînement d'un modèle OCR (de l'annotation des données à l'application du modèle)" caption="Figure&nbsp;1&nbsp;: Détail des étapes classiques pour l'entraînement d'un modèle OCR ou HTR" %}

<div class="alert alert-info">
Dans la pratique, la reconnaissance de caractères ne représente qu'un simple problème de classification en vision par ordinateur. Quelle que soit l'étape, détection des contenus et reconnaissance du texte proprement dite, les modèles tenteront de classifier les informations rencontrées et de les répartir dans les classes connues : par exemple une zone de texte à considérer comme titre, ou une forme à transcrire en la lettre A. Cette approche, complètement supervisée, est très largement dépendante des choix et des besoins identifiés et que nous abordons dans la partie <a href="#définition-des-besoins">Définition des besoins</a>.
</div>

### Le cas des langues et systèmes graphiques peu dotés

Annoter manuellement des documents, choisir une architecture neuronale adaptée à son besoin, suivre/évaluer l'apprentissage d'un réseau de neurones pour créer un modèle pertinent, etc., sont des activités coûteuses et chronophages, qui nécessitent souvent des investissements et une expérience en apprentissage machine (ou *machine learning*), conditions peu adaptées à un traitement massif et rapide de documents. L'apprentissage profond est donc une approche qui nécessite intrinsèquement la constitution d'un corpus d'entraînement conséquent, corpus qu'il n'est pas toujours aisé de constituer malgré la multiplicité des plateformes dédiées (voir *infra*). D'autres stratégies doivent donc être mises en place, en particulier dans le cas des langues dites peu dotées.

En effet, si la masse critique de données pour du traitement de manuscrits ou documents imprimés en alphabet latin semble pouvoir être atteinte[^8], avec une variété de formes, polices d'écritures et mises en page représentées et représentatives des besoins classiques des institutions en matière d'HTR et d'OCR[^9], cela est beaucoup moins évident pour les autres alphabets. Nous nous retrouvons donc dans la situation où des institutions patrimoniales numérisent et rendent disponibles des copies numériques des documents, mais où ces derniers restent «&nbsp;dormants&nbsp;» car pas ou peu interrogeables par des systèmes automatiques. Par exemple, de nombreuses institutions, comme la Bibliothèque nationale de France (BnF) au travers de son interface [Gallica](https://perma.cc/Y4DT-PBLD), proposent des versions textes des documents écrits majoritairement avec l'alphabet latin en vue de permettre la recherche en plein texte, fonctionnalité qui malheureusement est indisponible pour les documents en arabe.

Aujourd'hui, une langue ou un système graphique peuvent être considérés comme peu dotés à plusieurs niveaux&nbsp;:

* Un **manque de disponibilité ou d'existence des données**. Il s'agit du point le plus évident, de nombreux systèmes graphiques ne sont tout simplement pas représentés numériquement, au sens de données exploitables, même si des réseaux institutionnels se forment pour intégrer ces langues dans cette transition numérique[^10].

* Une **trop grande spécialisation d'un jeu de données ou *dataset***. *A contrario*, s'il peut exister des données pour une langue ciblée, celles-ci peuvent être trop spécialisées sur l'objectif poursuivi par l'équipe qui les ont produites --&nbsp;modernisation de l'orthographe d'une graphie ancienne ou utilisation d'une notion de ligne spécifique par exemple&nbsp;--, limitant sa reproductibilité et son exploitation dans un nouveau projet. Par conséquent, s'il existe des modèles gratuits et ouverts (voir *infra*) pour une langue ou un document, ceux-ci peuvent ne pas convenir immédiatement aux besoins du nouveau projet.

* Un **nombre potentiellement réduit de spécialistes** en mesure de transcrire et d'annoter des données rapidement. Si des initiatives participatives --&nbsp;dites de *crowdsourcing*&nbsp;-- sont souvent mises en place pour les alphabets latins[^11], elles sont plus difficilement applicables pour des écritures anciennes ou non latines qui nécessitent une haute expertise, souvent paléographique, limitant considérablement le nombre de personnes pouvant produire les données.

* Une **sur-spécialisation des technologies** existantes pour l'alphabet latin, résultant en des approches moins adaptées pour d'autres systèmes graphiques. Par exemple, les écritures arabes tireront intuitivement profit d'une reconnaissance globale des mots plutôt que de chercher à reconnaître chaque caractère indépendamment.

* La **nécessité de disposer de connaissances en apprentissage machine** pour exploiter au mieux les outils de reconnaissance automatique des écritures proposés actuellement.

Ces limites sont illustrées dans la figure&nbsp;2 qui met en évidence les composantes essentielles pour le traitement efficace d'un système graphique ou d'une langue, et dont sont dépourvues, en partie, les langues peu dotées.

{% include figure.html filename="figure2_composantes.jpg" alt="Détail des composantes nécessaires pour la création de modèles OCR : expertise, temps, compétences et données." caption="Figure&nbsp;2&nbsp;: Les composantes essentielles pour le traitement efficace d'une écriture (à gauche) et desquelles les langues peu dotées sont dépourvues (à droite quelques exemples classiquement traités sur Calfa Vision)" %}

Rien d'insurmontable pour autant. Si le *pipeline* (ou la chaîne de traitement) classique qui consiste donc à apporter *massivement* des *données* (manuellement) *annotées* à une *architecture* neuronale s'avère manifestement peu adapté au traitement de certaines langues, plusieurs plateformes ont été implémentées pour faciliter l'accès aux OCR et HTR ces dernières années. Chacune d'elles essaie de jongler avec les composantes de la figure&nbsp;2, en intégrant par exemple des modèles pré-entraînés pour avancer le travail de transcription[^12]. L'objectif de ces plateformes consiste à compenser l'une des composantes manquantes afin de permettre le traitement de la langue/écriture cible.

La plateforme la plus connue est [Transkribus](https://perma.cc/3D3V-YWW5) (READ-COOP), utilisée sur un très large spectre de langues, écritures et types de documents. Il existe également des plateformes institutionnelles comme [eScriptorium](https://perma.cc/CTV2-ZRE8) (université Paris Sciences & Lettres) dédiée aux documents historiques, et [OCR4all](https://perma.cc/9ADK-T4SB) (université de Wurtzbourg) particulièrement adaptée aux documents imprimés anciens. Enfin, des plateformes privées comme [Calfa Vision](https://vision.calfa.fr/) (Calfa) complètent ces dernières par une multiplicité d’architectures. Cette dernière intègre une approche de spécialisation itérative pour surmonter les écueils mentionnés pour le traitement d'écritures peu dotées, à partir de petits échantillons[^13].

<div class="alert alert-info">
Dans la suite du tutoriel, c'est la plateforme Calfa Vision que nous utiliserons, notamment car elle a été spécifiquement construite pour surmonter les problèmes liés aux documents et systèmes graphiques peu dotés, qui sont notre cible du jour. Le suivi du tutoriel nécessite la création (gratuite) d'un compte sur la plateforme. Néanmoins, l'intégralité du tutoriel et le type d'annotation choisi ici s'applique et est compatible avec les autres plateformes mentionnées.
</div>

L'objectif méthodologique est de tirer profit des fonctionnalités de spécialisation de la plateforme d'annotation Calfa Vision. Celle-ci intègre différentes architectures neuronales selon la langue ciblée afin de minimiser l'investissement en données, sans attendre des utilisateurs et utilisatrices une compétence particulière en apprentissage machine pour évaluer les modèles (voir *infra*). L'enjeu est donc de surmonter l'écueil du manque de données par des stratégies de spécialisation et de définition des besoins.


## Des données oui, mais pour quoi faire&#x202F;?

La reconnaissance automatique des écritures n'est possible qu'en associant l'expertise humaine à la capacité de calcul de l'ordinateur. Un important travail scientifique reste à notre charge pour définir les objectifs et les sorties d'une transcription automatique. Plusieurs questions se posent donc au moment de se lancer dans l'annotation de nos documents&nbsp;:

1. Créer des données. Quel volume possible, pour quels *besoins*, quel public et quelle compatibilité&#x202F;?
2. Créateur et créatrice de données. Par qui et dans quelle temporalité&#x202F;?
3. Approche généraliste ou approche spécialisée
4. Approche quantitative ou qualitative

Notre objectif est ici de réussir à transcrire automatiquement un ensemble homogène de documents, tout en minimisant l'investissement humain pour la création de modèles. Nous souhaitons créer un modèle spécialisé --&nbsp;et non généraliste&nbsp;-- pour surmonter les spécificités de notre document. Ces spécificités peuvent être de plusieurs ordres et peuvent justifier la création d'un modèle spécialisé&nbsp;: nouvelle main, nouveau font, état variable de conservation du document, mise en page inédite, besoin d'un contenu spécifique, etc.

### *Pipeline* classique d'un OCR/HTR

#### Étapes de reconnaissance

Le travail d'un OCR ou d'un HTR se décompose en plusieurs étapes&nbsp;: analyse et compréhension d'une mise en page, reconnaissance du texte et formatage du résultat. La figure&nbsp;3 reprend l'essentiel des tâches classiquement présentes et sur lesquelles un utilisateur ou une utilisatrice a la main pour adapter un modèle à son besoin. L'intégralité de ces fonctionnalités est entraînable sur la plateforme Calfa Vision, ce qui nous assure un contrôle complet du *pipeline* de reconnaissance.

{% include figure.html filename="figure3_pipeline-htr.jpeg" alt="Schéma de la décomposition du travail d'un OCR : analyse de la mise en page, reconnaissance du texte et formatage" caption="Figure&nbsp;3&nbsp;: *Pipeline* classique d'un traitement OCR/HTR. Les étapes 2 et 3 sont spécialisables aux besoins d'un projet, et l'étape 3 intègre des approches spécifiques à une langue/écriture pour maximiser les résultats en minimisant l'investissement." %}

La figure&nbsp;3 met en évidence l'une des grandes oubliées de la reconnaissance de caractères&nbsp;: l'analyse de la mise en page, qui peut être spécialisée pour ne reconnaître qu'une ou plusieurs régions d'intérêt dans le document et concentrer l'extraction des lignes dans ces régions. La construction d'un modèle d'analyse de la mise en page performant est l'un des enjeux majeurs pour le traitement de nouvelles collections (voir *infra*).

#### La spécialisation des modèles (ou *fine-tuning*)

<div class="alert alert-info">
Dans la suite de la leçon, nous utiliserons le terme anglais <i>fine-tuning</i>, davantage usité dans le champ disciplinaire de l'intelligence artificielle.
</div>

Le *fine-tuning* d'un modèle consiste à affiner et adapter les paramètres d'un modèle pré-entraîné sur une tâche similaire à notre problématique. Cette approche permet de limiter considérablement le nombre de données nécessaires, par opposition à la création d'un modèle de zéro (*from scratch*), l'essentiel du modèle étant déjà construit. Par exemple, nous pourrons partir d'un modèle entraîné sur le latin —&nbsp;langue pour laquelle nous disposons d'un grand nombre de données&nbsp;— pour obtenir rapidement un modèle pour le moyen-français —&nbsp;pour lequel les jeux de données sont plus limités. Ces deux langues partageant un grand nombre de représentations graphiques, ce travail de spécialisation permettra d'aboutir à des modèles OCR/HTR rapidement exploitables[^14].

La différence entre un modèle entraîné de zéro et une stratégie de *fine-tuning* est décrite en figures 4 et 5.

{% include figure.html filename="figure1_pipeline_training_1.jpg" alt="Schéma des étapes classiques pour l'entraînement d'un modèle OCR (de l'annotation des données à l'application du modèle)" caption="Figure&nbsp;4&nbsp;: Entraînement d'un modèle OCR/HTR de zéro" %}
{% include figure.html filename="figure5_pipeline_training_2.jpg" alt="Schéma de fonctionnement du fine-tuning d'un modèle en intelligence artificielle" caption="Figure&nbsp;5&nbsp;: *Fine-tuning* d'un modèle OCR/HTR pré-entraîné" %}

La stratégie de *fine-tuning* est largement développée et utilisée dans les projets faisant appel à la reconnaissance de caractères[^15].

#### Le *fine-tuning* itératif des modèles sur Calfa Vision

Dans la pratique, il est difficile d'anticiper le volume de données nécessaire au *fine-tuning* ou à l'entraînement de zéro d'un modèle (voir *infra*). Entraîner, évaluer, ré-annoter des documents, et ainsi de suite jusqu'à l'obtention d'un modèle satisfaisant est non seulement chronophage mais requiert de plus une solide formation en apprentissage machine. Afin de surmonter cet écueil, la plateforme Calfa Vision intègre nativement une stratégie de *fine-tuning* itératif autonome (voir figure&nbsp;6) au fur et à mesure des corrections de l'utilisateur ou de l'utilisatrice.

{% include figure.html filename="figure6_pipeline_training_3.jpg" alt="Schéma de fonctionnement du fine-tuning d'un modèle sur la plateforme Calfa Vision" caption="Figure&nbsp;6&nbsp;: Stratégie de *fine-tuning* itératif sur Calfa Vision" %}

La plateforme propose en effet un grand nombre de modèles pré-entraînés sur diverses tâches --&nbsp;étude de documents imprimés, analyse de documents manuscrits orientaux, lecture de documents xylographiés chinois, etc.&nbsp;-- qui sont prêts à être spécialisés sur les tâches ciblées par l'utilisateur ou l'utilisatrice, au niveau de la mise en page et de la reconnaissance de texte.

<div class="alert alert-warning">
Un modèle peut ne pas être pertinent immédiatement pour la tâche souhaitée, en raison d'un jeu de données utilisé en entraînement très éloigné des documents cibles. Néanmoins, les expériences réalisées sur la plateforme montrent une spécialisation très rapide des modèles après correction d'un nombre limité de pages (voir <i>infra</i> pour un exemple sur la PG).
</div>

### Définition des besoins

Si aujourd'hui nous pouvons tout à fait considérer la reconnaissance de caractères comme un problème largement résolu pour les écritures latines, ou les documents unilingues, et une mise en page simple, avec des taux d'erreur inférieurs à 2&nbsp;%[^16], le résultat final peut ne pas être exploitable du tout (voir figure&nbsp;7).

{% include figure.html filename="figure7_CER-layout.jpg" alt="Exemples de résultats produits par un OCR / HTR, avec ou sans normalisation du texte" caption="Figure&nbsp;7&nbsp;: Reconnaissance de caractères et du texte. BER ms or. quart. 304, 101v, Staatsbibliothek zu Berlin" %}

La figure&nbsp;7 met en lumière ce phénomène&nbsp;: en entraînant une architecture de reconnaissance spécialisée sur les caractères, nous obtenons ici un CER (*Character Error Rate*) de 0&nbsp;%, soit une reconnaissance parfaite. En revanche&nbsp;:

1. La mise en page par colonnes n'ayant pas été correctement détectée, nous nous retrouvons avec un seul bloc de texte
2. La *scriptio continua* du manuscrit, bien respectée par l'HTR, aboutit à un texte dépourvu d'espace difficilement accessible pour l'être humain
3. Le texte, en arménien classique, comporte un grand nombre d'**abréviations** qui ne sont pas développées dans le résultat final. Si le texte produit correspond bien à l'image du manuscrit, la recherche en plein texte demeure *de facto* limitée.

<div class="alert alert-warning">
Avant toute entreprise de transcription automatique, il convient donc de définir les attendus des modèles&nbsp;: mise en page à prendre en compte, zones d'intérêts, cahier des charges de la transcription, format des données, etc.
</div>

#### Zones d'intérêts

Dans le cadre du traitement de la PG, nous ne sommes intéressés que par le texte grec des PDF à notre disposition (en rouge dans les figures 8a et 8b). Malheureusement, nous sommes confrontés à une mise en page relativement dense et complexe, avec une alternance de colonnes en grec et en latin, des textes parfois à cheval sur les deux colonnes (ici en bleu), des titres courants, des notes de bas de page ainsi que des repères de paragraphes.


{% include figure.html filename="figure8_PG_123_359-360.jpg" alt="Exemple de mise en page de la PG, avec détail des zones de textes" caption="Figure&nbsp;8a&nbsp;: Mise en page de la PG (PG 123, c. 359-360)" width="200" %}
{% include figure.html filename="figure8_PG_125_625-626.jpg" alt="Exemple de mise en page de la PG, avec détail des zones de textes" caption="Figure&nbsp;8b&nbsp;: Mise en page de la PG (PG 125, c. 625-626)" width="200" %}

Cette mise en page ne poserait pas de problème majeur si nous ne nous intéressions pas à la question de la discrimination des zones de texte. Nous ne sommes néanmoins pas concernés par le texte latin et souhaitons obtenir un résultat aussi propre que possible, sans mélange des langues ou confusion probable dans le modèle. Nous identifions donc ici un besoin d'un **modèle de mise en page** spécialisé.

#### Choix de transcription et encodage

Nous sommes tout à fait libres de choisir une transcription qui ne corresponde pas tout à fait au contenu de l'image. Des expérimentations sur le latin manuscrit ont par exemple montré que des architectures de reconnaissance au mot (dites *word-based*)[^17], comme celles intégrées sur Calfa Vision, réussissent à développer des formes abrégées avec un taux d'erreur inférieur à 3&nbsp;%[^18].

Ici, nous travaillons avec du grec ancien, comportant de nombreux diacritiques.

<div class="table-wrapper" markdown="block">
<caption>Tableau&nbsp;1&nbsp;: Exemple de diacritiques rencontrés en grec </caption> 
 
|               | Signes | Codes  | Noms anglais         |
|---------------|--------|--------|----------------------|
| **Esprits**   |        |        |                      |
| Esprit doux   | ᾿      | U+1FBF | Greek Psili          |
| Esprit rude   | ῾      | U+1FFE | Greek Daseia          |
| **Accents**   |        |        |                      |
| Oxyton        | ´      | U+1FFD | Greek Oxeia           |
| Baryton       | `      | U+1FEF | Greek Vareia          |
| Périspomène   | ῀      | U+1FC0 | Greek Perispomeni    |
| **Autres**    |        |        |                      |
| Tréma         | ¨      | U+00A8 | Greek Dialytika      |
| Iota souscrit | ι      | U+1FBE | Greek Hypogegrammeni |
| Coronis       | ᾽      | U+1FBD | Greek Koronis        |
| ...           |        |        |                      |
 
</div>



Les diacritiques se combinent au-dessus des voyelles --&nbsp;ou juste devant les voyelles majuscules comme Ἄ, Ἆ. Les esprits peuvent de plus apparaître au-dessus de la consonne ρ (rho)&nbsp;: ῤ, ῥ et Ῥ. Le iota souscrit se place sous les voyelles α (alpha), η (êta), ω (oméga) -- &nbsp;ᾆ, ῃ, ῷ, etc.&nbsp;--, surmontées ou non des autres diacritiques. En tenant compte des combinaisons possibles de ces diacritiques et du changement de casse des lettres de l'alphabet grec, la lettre α (alpha) peut regrouper jusqu'à 44 glyphes&nbsp;: Α, α, Ἀ, ἀ, Ἁ, ἁ, Ἂ, ἂ, Ἃ, ἃ, Ἄ, ἄ, Ἅ, ἅ, Ἆ, ἆ, Ἇ, ἇ, Ὰ, ὰ, Ά, ά, ᾈ, ᾀ, ᾉ, ᾁ, ᾊ, ᾂ, ᾋ, ᾃ, ᾌ, ᾄ, ᾍ, ᾅ, ᾎ, ᾆ, ᾏ, ᾇ, ᾲ, ᾼ, ᾳ, ᾴ, ᾶ et ᾷ ([table complète de l'Unicode du grec ancien](https://perma.cc/959E-6QEX)).

Conséquence&nbsp;: selon la [normalisation Unicode](https://perma.cc/BF7R-ZJEZ) considérée, un caractère grec peut avoir plusieurs valeurs différentes, ce dont on peut se convaincre très facilement en python.

```python
char1 = "ᾧ"
char1
>>> ᾧ

len(char1)
>>> 1

char2 = "\u03C9\u0314\u0342\u0345" # Le même caractère mais avec les diacritiques explicitement décrits en Unicode.
char2
>>> ᾧ

len(char2)
>>> 4

char1 == char2
>>> False
```

Dès lors, le problème de reconnaissance de caractères n'est plus le même selon la normalisation appliquée. Dans un cas, nous n'aurons qu'une seule classe à reconnaître, le caractère Unicode ᾧ, tandis que dans l'autre nous devrons en reconnaître quatre --&nbsp;ω + ̔ +  ͂ +  ͅ &nbsp;-- comme nous pouvons le voir ci-après.

```python
print(u'\u03C9', u'\u0314', u'\u0342', u'\u0345')
>>> ω ̔ ͂ ͅ
```

Il existe plusieurs types de normalisation Unicode&nbsp;: NFC (*Normalization Form Canonical Composition*), NFD (*Normalization Form Canonical Decomposition*), NFKC (*Normalization Form Compatibility Composition*) et NFKD (*Normalization Form Compatibility Decomposition*), dont on peut voir les effets avec le code ci-dessous&nbsp;:

```python
from unicodedata import normalize, decomposition

len(normalize("NFC", char1))
>>> 1

len(normalize("NFD", char1))
>>> 4

len(normalize("NFC", char2))
>>> 1

normalize("NFC", char1) == normalize("NFC", char2)
>>> True

## Ce qui nous donne dans le détail :

decomposition(char1)
>>> '1F67 0345'

print(u'\u1F67')
>>> ὧ

decomposition(u'\u1F67')
>>> '1F61 0342'

print(u'\u1F61')
>>> ὡ

decomposition(u'\u1F61')
>>> '03C9 0314'

print(u'\u03C9')
>>> ω
```

Dans notre exemple, il apparaît que la normalisation NFC --&nbsp;et NFKC&nbsp;-- permet de recombiner un caractère en un seul caractère Unicode, tandis que la normalisation NFD --&nbsp;et NFKD&nbsp;-- réalise la décomposition inverse[^19]. L'avantage de ces dernières normalisations est de regrouper toutes les matérialisations d'une lettre sous un seul sigle afin de traiter la variété seulement au niveau des diacritiques.

Et donc, quelle normalisation choisir ici&#x202F;?

Au-delà de l'aspect technique sur un caractère isolé, l'approche du problème est sensiblement différente selon le choix.

```python
phrase = "ἀδιαίρετος καὶ ἀσχημάτιστος. Συνάπτεται δὲ ἀσυγ-"
len(normalize("NFC", phrase))
>>> 48
len(normalize("NFD", phrase))
>>> 56
```

Les impressions de la PG présentent une qualité très variable, allant de caractères lisibles à des caractères pratiquement entièrement effacés ou *a contrario* très empâtés (voir figure&nbsp;9 et tableau&nbsp;2). Il y a également présence de bruit résiduel, parfois ambigu avec les diacritiques ou ponctuations du grec.

{% include figure.html filename="figure9_exemples-PG.png" alt="Différents états de conservation ou d'impression dans la PG" caption="Figure&nbsp;9&nbsp;: Exemples d'impression de la PG" %}

Envisager une normalisation NFD ou NFKD permettrait de regrouper chaque caractère sous une méta-classe --&nbsp;par exemple α pour ά ᾶ ὰ&nbsp;-- et ainsi lisser la grande variété dans la qualité des images. Il nous semble toutefois ambitieux de vouloir envisager de reconnaître chaque diacritique séparément, au regard de la grande difficulté à les distinguer ne serait-ce que par nous-même. Notre choix est donc largement conditionné par (i) la qualité de la typographie, parfois médiocre, de la PG et (ii) la qualité de la numérisation, comme le montre le tableau&nbsp;2.

<div class="table-wrapper" markdown="block">
<table>
<caption>Tableau&nbsp;2&nbsp;: Lecture des variations du α dans la PG </caption>
<colgroup>
<col width="60%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Image</th>
<th>Transcription</th>
<th>Variation du α</th>
</tr>
</thead>
<tbody>
<tr>
<td>{% include figure.html filename="tableau_alpha/image1.png" alt="Impression du mot ἀληθινῷ dans la PG" caption="" %}</td>
<td markdown="span">**ἀ**ληθινῷ</td>
<td markdown="span">**ἀ**</td>
</tr>
<tr>
<td>{% include figure.html filename="tableau_alpha/image2.png" alt="Impression du mot ἁμαρτίας dans la PG" caption="" %}</td>
<td markdown="span">**ἁ**μαρτίας</td>
<td markdown="span">**ἁ**</td>
</tr>
<tr>
<td>{% include figure.html filename="tableau_alpha/image3.png" alt="Impression du mot μεταφράσαντος dans la PG" caption="" %}</td>
<td markdown="span">μεταφρ**ά**σαντος</td>
<td markdown="span">**ά**</td>
</tr>
<tr>
<td>{% include figure.html filename="tableau_alpha/image4.png" alt="Impression du mot μετὰ dans la PG" caption="" %}</td>
<td markdown="span">μετ**ὰ**</td>
<td markdown="span">**ὰ**</td>
</tr>
<tr>
<td>{% include figure.html filename="tableau_alpha/image5.png" alt="Impression du mot ἡμᾶς dans la PG" caption="" %}</td>
<td markdown="span">ἡμ**ᾶ**ς</td>
<td markdown="span">**ᾶ**</td>
</tr>
<tr>
<td>{% include figure.html filename="tableau_alpha/image6.png" alt="Impression du mot ἄχρι dans la PG" caption="" %}</td>
<td markdown="span">**ἄ**χρι</td>
<td markdown="span">**ἄ**</td>
</tr>
<tr>
<td>{% include figure.html filename="tableau_alpha/image7.png" alt="Impression du mot ἅπαντες dans la PG" caption="" %}</td>
<td markdown="span">**ἅ**παντες</td>
<td markdown="span">**ἅ**</td>
</tr>
</tbody>
</table>
</div>

Le tableau&nbsp;2 met en évidence la forte ambiguïté présente dans la PG. Les lignes 1 et 2 semblent par exemple, à tort, comporter la lettre α surmontée du même esprit. Il en est de même pour les lignes 3 et 4, et les lignes 6 et 7. Il apparaît difficile, avec peu de données, d’arriver à reconnaître ces esprits sans erreur indépendamment de la lettre. *A contrario*, la reconnaissance directe de la lettre accentuée pourra être facilitée par son contexte d’apparition.

Nous choisissons donc une normalisation de type NFC, qui aura pour conséquence de démultiplier le nombre de classes. Ce choix entraînera peut-être la nécessité de transcrire davantage de lignes[^20].

Par ailleurs, nous ne sommes pas intéressés par les appels de note présents dans le texte (voir figure&nbsp;9), et ceux-ci ne sont donc pas présents dans la transcription. Cela créera une ambiguïté supplémentaire dans le modèle OCR, puisqu'à une forme graphique dans l'image ne correspondra aucune transcription. Nous identifions ici un besoin d'un **modèle d'OCR spécialisé**[^21].

<div class="alert alert-warning">
Attention, le choix de la normalisation constitue un tournant dans la création du modèle OCR/HTR. Dans une situation comme celle de la PG, où nous ne disposons que de peu de données, le choix d'une normalisation plutôt que d'une autre peut démultiplier le nombre de caractères à prédire et conduire à la situation où nous ne disposons pas assez d'échantillons pour chaque caractère à reconnaître -&nbsp;c'est-à-dire pour chaque classe à reconnaître. La présente leçon ne traite pas de cette situation. Le lectorat devra mettre en place une stratégie pour augmenter artificiellement ses données, par exemple, ou alors envisager un travail de transcription un peu plus long en augmentant le nombre d'itérations du <i>fine-tuning</i> sur Calfa Vision.
</div>

#### Approches architecturales et compatibilité des données

À ce stade, nous avons identifié deux besoins qui conditionnent la qualité escomptée des modèles, le travail d'annotation et les résultats attendus. En termes d'OCR du grec ancien, nous ne partons pas non plus tout à fait de zéro puisqu'il existe déjà des images qui ont été transcrites et rendues disponibles[^22], pour un total de 5100 lignes. Un *dataset* plus récent, ```GT4HistComment```[^23], est également disponible, avec des imprimés de 1835-1894 et des mises en page plus proches de la PG. Le format de données est le même que pour les *datasets* précédents (voir *infra*). Nous ne retenons pas ce *dataset* en raison du mélange d'alphabets présent dans la vérité terrain (voir tableau&nbsp;3, ligne ```GT4HistComment```).

<div class="table-wrapper" markdown="block">
<table>
<caption>Tableau&nbsp;3&nbsp;: Exemples de vérités terrain disponibles pour le grec ancien</caption>
<colgroup>
<col width="25%" />
<col width="75%" />
</colgroup>
<thead>
<tr class="header">
<th>Source</th>
<th><i>Data</i></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>greek_cursive</code></td>
<td>{% include figure.html filename="cursive/000005.png" alt="Exemple de ligne de texte dans le dataset greek_cursive" caption="" %}</td>
</tr>
<tr style="border-bottom:2px solid black">
<td>Vérité terrain</td>
<td>Αλῶς ἡμῖν καὶ σοφῶς ἡ προηγησαμένη γλῶσσα τοῦ σταυροῦ τὰς ἀκτῖ-</td>
</tr>
<tr>
<td><code>gaza-iliad</code></td>
<td>{% include figure.html filename="gaza/000014.png" alt="Exemple de ligne de texte dans le dataset gaza-iliad" caption="" %}</td>
</tr>
<tr style="border-bottom:2px solid black">
<td>Vérité terrain</td>
<td>Τρῳσὶ, ποτὲ δὲ παρὰ τὸν Σιμοῦντα ποταμὸν, τρέχων</td>
</tr>
<tr>
<td><code>voulgaris-aeneid</code></td>
<td>{% include figure.html filename="voulgaris/000007.png" alt="Exemple de ligne de texte dans le dataset voulgaris-aeneid" caption="" %}</td>
</tr>
<tr style="border-bottom:2px solid black">
<td>Vérité terrain</td>
<td>θὺς συνεῤῥύη ἀνδρῶντε καὶ γυναικῶν τῶν ὁμοπατρίων, καὶ ἄλ-</td>
</tr>
<tr>
<td><code>GT4HistComment</code></td>
<td>{% include figure.html filename="gtcommantaries/cu31924087948174_0063_70.png" alt="Exemple de ligne de texte dans le dataset GT4HistComment" caption="" %}</td>
</tr>
<tr style="border-bottom:2px solid black">
<td>Vérité terrain</td>
<td>νώπαν θυμόν), yet αἴθων, which directly </td>
</tr>
</tbody>
</table>
</div>


Les données du tableau&nbsp;3 montrent une nette différence de qualité et de police entre ces données et la PG (voir tableau&nbsp;2). Les données ```greek_cursive``` présentent des formes graphiques très éloignées des formes de la PG, tandis que les autres documents sont beaucoup plus «&nbsp;propres&nbsp;». Néanmoins, cela apporte un complément lexical qui pourra peut-être s'avérer utile par la suite. L'intégration et l'évaluation de ces données sur Calfa Vision donnent un modèle avec un taux d'erreur de 2,24&nbsp;%[^24] dans un test *in-domain*, modèle sur lequel se basera le *fine-tuning* pour le modèle de PG. Néanmoins, il s'avère indispensable d'envisager un modèle spécialisé sur la PG afin de gérer les difficultés mises en évidence en figure&nbsp;9.

Les données sont disponibles dans le format originellement proposé par OCRopus[^25], c'est-à-dire une paire composée d'une image de ligne et de sa transcription (voir tableau&nbsp;3).

```
├── dataset
│   ├── 000001.gt.txt
│   ├── 000001.png
│   ├── 000002.gt.txt
│   ├── 000002.png
│   ├── 000003.gt.txt
│   └── 000003.png
```

Il s'agit d'un format ancien, la ligne de texte étant contenue dans un rectangle englobant (ou *bounding box*) parfaitement adapté aux documents sans courbure, ce qui n'est pas tout à fait le cas de la PG, dont les *scans* sont parfois courbés sur les tranches (voir figure&nbsp;10). Ces données ne permettront pas non plus d'entraîner un modèle d'analyse de la mise en page, puisque ne sont proposées que les images des lignes sans précision sur la localisation dans le document.

{% include figure.html filename="figure10_PG_123_202.jpg" alt="Exemple de détections de la courbure des lignes, avec baseline et polygones" caption="Figure&nbsp;10&nbsp;: Gestion de la courbure des lignes sur Calfa Vision" %}

Une approche par *baselines* (en rouge sur la figure&nbsp;10, il s'agit de la ligne de base de l'écriture) est ici justifiée puisqu'elle permet de prendre en compte cette courbure, afin d'extraire la ligne de texte avec un polygone encadrant (en bleu sur les figures 8a et 8b) et non plus une simple *bounding box*[^26]. Cette fois-ci les données ne sont plus exportées explicitement en tant que fichiers de lignes, mais l'information est contenue dans un XML contenant les coordonnées de chaque ligne. Cette approche est aujourd'hui universellement utilisée par tous les outils d'annotation de documents textuels&nbsp;: elle est donc applicable ailleurs.

```xml
<?xml version="1.0" ?>
<PcGts xmlns="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15 http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15/pagecontent.xsd">
  <Metadata>
    <Creator>Calfa</Creator>
    <Created>2022-08-23T14:48:18+00:00</Created>
  </Metadata>
  <Page imageFilename="grc_grna_or_409.jpg" imageHeight="3506" imageWidth="1686">
    <TextRegion id="52467" custom="structure {type:col_greek;}">
      <Coords points="193,225 147,667 171,3259 1525,3269 1505,246"/>
      <TextLine id="629162">
        <Coords points="241,264 241,317 239,331 1465,344 1469,329 1467,278 241,264"/>
        <Baseline points="243,319 1471,331"/>
        <TextEquiv>
          <Unicode>Βʹ. Καὶ ἵνα γε καθ´ ὁδὸν ὁ λόγος ἡμῖν προΐῃ, περὶ</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="629163">
        <Coords points="1479,407 1479,368 1036,348 1034,348 185,354 185,395 183,401 1475,412 1479,407"/>
        <Baseline points="187,396 1480,409"/>
        <TextEquiv>
          <Unicode>τῆς δειλίας προτέρας οὔσης καὶ διαλέξομαι· οὐδὲ γὰρ</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="629164">
        <Coords points="194,420 194,469 192,484 1477,490 1481,484 1481,446 194,420"/>
        <Baseline points="196,470 1482,485"/>
        <TextEquiv>
          <Unicode>ἀνέχομαι πλήττεσθαί τινας ἐν ἐμοὶ τῶν πάντα τη-</Unicode>
        </TextEquiv>
      </TextLine>
```
Exemple de structure du format [PAGE (XML)](https://perma.cc/YYB7-TD5X), décrivant l'ensemble de l'arborescence des annotations --&nbsp;la région de texte et son type, les coordonnées de la ligne, la *baseline* et la transcription. D'autres formats du même type existent, comme le format [ALTO (XML)](https://perma.cc/VX9N-M46X).

Le mélange des formats aboutit en général, dans les OCR disponibles, à une perte de qualité, en raison d'une gestion de l'information différente selon le format. Nous observons ainsi sur la figure&nbsp;11 que non seulement une *bounding box* ne peut pas appréhender convenablement la courbure du texte et chevauche la ligne supérieure, mais aussi que les données polygonales ne sont par défaut pas compatibles avec les données de type ```bounding-box``` en raison de la présence du masque. Il est néanmoins possible de les combiner sur Calfa Vision afin d'extraire non pas un polygone mais une *bounding box* à partir de la *baseline*. Cette fonctionnalité a été précisément mise en place afin de convertir des *datasets* habituellement incompatibles pour exploiter des données plus anciennes et assurer une continuité dans la création de données[^27].

{% include figure.html filename="figure11_bbox_polygon.jpeg" alt="Différents masques appliqués à une image de ligne selon l'outil utilisé" caption="Figure&nbsp;11&nbsp;: Différence de visualisation d'une ligne entre une *bounding-box*, un masque polygonal, et un polygone extrait de Calfa Vision" %}

Et maintenant&#x202F;?

En résumé, à l'issue de cette étape de description des besoins, il en résulte que&nbsp;:

1. **Zones de texte**. Nous souhaitons concentrer la détection et la reconnaissance du texte sur les colonnes principales en grec, en excluant le texte latin, les titres courants, les notes inter-colonnes, l'apparat critique et toute note marginale.
2. **Lignes de texte**. Nous avons à prendre en compte des lignes courbes et choisissons donc une approche par *baseline*.
3. **Modèle de base**. Un modèle de base est disponible mais entraîné avec des données plus anciennes. Nous utiliserons une approche combinant *baseline* et *bounding box* pour tirer profit au maximum des données existantes.
4. **Choix de transcription**. Nous partons sur une transcription avec normalisation de type NFC, sans intégrer les signes d'édition éventuels et les appels de note. La complexité offerte par la PG laisse supposer qu'un jeu de données important devra être produit. Nous verrons dans la partie suivante comment limiter les données nécessaires en considérant une architecture dédiée et non générique.

<div class="alert alert-info">
À ce stade, nous avons donc clairement identifié les besoins de notre projet OCR&nbsp;: afin de traiter efficacement l'intégralité des PDF de la PG non encore disponibles, nous devons créer un modèle de mise en page spécialisé et un modèle OCR propre à nos contraintes éditoriales.
</div>

#### Petit aparté sur les métriques

Pour appréhender les résultats proposés par l'OCR/HTR, tant au niveau de la mise en page que de la reconnaissance de caractères, nous devons définir quelques métriques couramment utilisées pour quantifier l'erreur de ces modèles.

*CER*

Nous avons déjà abordé discrètement le CER (*Character Error Rate*), qui donne le taux d'erreur au niveau du caractère dans la prédiction d'un texte. Le CER se calcule simplement en comptant le nombre d'opérations nécessaires pour passer de la prédiction au texte attendu. Le CER utilise la [distance de Levenshtein](https://perma.cc/R9HY-8LJ6). Il est donné par la formule suivante&nbsp;:

$$ CER = \frac{S+D+I}{N} $$

où S = le nombre de substitutions, D = le nombre de délétions, I = le nombre d'additions, et N = le nombre total de caractères à prédire.

Par exemple, si mon OCR prédit le mot ```Programm*m*ingHisto*y*an``` à la place de ```ProgrammingHistorian```, autrement dit&nbsp;:
* Un m superfétatoire a été ajouté
* Le i a été substitué par un y
* Le r n'a pas été reconnu

Nous avons donc les valeurs suivantes&nbsp;: S = 1, I = 1 D = 1 et N = 20.

$$ CER = \frac{1+1+1}{20} = 0,15 $$

Autrement dit, nous obtenons un taux d'erreur au niveau du caractère de 15&nbsp;%.

Il existe une variante applicable au mot, le WER (ou *Word Error Rate*), dont le fonctionnement est totalement similaire.
Le CER et le WER sont très pratiques et intuitifs pour quantifier le pourcentage d'erreur dans une prédiction. Toutefois, selon le cahier des charges adopté, ces métriques pourront se révéler moins pertinentes voire ambiguës. L'exemple le plus évident est celui d'une lecture automatique des abréviations où il ne serait pas pertinent de comptabiliser les additions et les substitutions --&nbsp;```par exemple``` à la place de ```p. ex.```[^28].

*Précision et rappel*

La précision (*precision*) et le rappel (*recall*) sont des métriques incontournables pour évaluer l'adéquation et la finesse des prédictions. Elles seront notamment utilisées lors de l'analyse de la mise en page.
La précision correspond au nombre total de résultats pertinents trouvés parmi tous les résultats obtenus. Le rappel correspond au nombre total de résultats pertinents trouvés parmi tous les résultats pertinents attendus.

Étudions ces deux métriques sur la tâche de détection des lignes (voir figure&nbsp;12, où les lignes correctement détectées sont en rouge et les lignes incorrectement détectées, c'est-à-dire avec des erreurs de détection et des lignes omises, sont en vert).

{% include figure.html filename="figure12_Precision_rappel.jpeg" alt="Trois exemples de détection de lignes dans un manuscrit" caption="Figure&nbsp;12&nbsp;: Comparaison de la précision et du rappel sur le manuscrit BULAC.MS.ARA.1947, image 178658 (RASAM)" %}

GT (*ground truth*)&nbsp;: nous souhaitons détecter 23 *baselines* --&nbsp;nous décidons d'ignorer les gloses interlinéaires.

Dans le cas 1, nous détectons 37 *baselines*. Parmi les 37 *baselines*, les 23 *baselines* attendues sont bien présentes. Le modèle propose donc des **résultats pertinents** mais est globalement **peu précis**. Cela se traduit par un **rappel élevé**, mais une **précision basse**. Dans le détail&nbsp;:

$$ Précision = \frac{23}{37} = 0,62 $$

$$ Rappel = \frac{23}{23} = 1 $$

Dans le cas 2, nous détectons 21 *baselines*, dont 10 sont correctes. Le modèle est à la fois **peu précis** et **assez peu pertinent**, puisqu'il manque plus de 50&nbsp;% des lignes souhaitées. Cela se traduit par un **rappel bas** et une **précision basse**. Dans le détail&nbsp;:

$$ Précision = \frac{10}{21} = 0,47 $$

$$ Rappel = \frac{10}{23} = 0,43 $$

Dans le cas 3, nous détectons douze *baselines*, qui sont toutes bonnes. Le modèle est **assez peu pertinent**, puisque la moitié seulement des lignes a été détectée, mais **très précis** car les lignes trouvées sont effectivement bonnes. Cela se traduit par une **précision haute** et un **rappel bas**. Dans le détail&nbsp;:


$$ Précision = \frac{12}{12} = 1 $$

$$ Rappel = \frac{12}{23} = 0,52 $$


La précision et le rappel sont souvent résumés avec le F1-score, qui correspond à leur [moyenne harmonique](https://perma.cc/FC5Z-E2QX) --&nbsp;l'objectif étant d'être le plus près possible de 1.


*Intersection sur l'Union (*Intersection over Union *ou IoU)*


Cette métrique s'applique à la détection d'objets dans un document, autrement dit elle est utilisée pour mesurer la qualité de l'analyse et de la compréhension de la mise en page&nbsp;: identification des titres, des numéros de page, des colonnes de texte, etc. Dans la pratique, nous mesurons le nombre de pixels communs à la vérité terrain et à la prédiction, divisés par le nombre total de pixels.

$$ IoU = \frac{GT \cap Prediction}{GT \cup Prediction} $$

Cette métrique est calculée séparément pour chaque classe à détecter, et une moyenne générale (en anglais *mean*) de toutes les classes est calculée pour fournir un score global, le ***mean*** **IoU**.

Une IoU de 0,5 est généralement considérée comme un bon score, car cela signifie qu’au moins la moitié des pixels ont été attribués à la bonne classe, ce qui est généralement suffisant pour identifier correctement un objet. Une IoU de 1 signifie que la prédiction et la vérité terrain se chevauchent complètement, une IoU de 0 signifie qu’aucun pixel n’est commun à la prédiction et à la vérité terrain.


## Chaîne de traitement&nbsp;: production du jeu de données et traitement des documents

### Méthodologie technique

Calfa Vision est une plateforme qui intègre un grand nombre de modèles pré-entraînés pour différentes tâches manuscrites et imprimées, dans plusieurs systèmes graphiques non latins[^29]&nbsp;: détection et classification de zones de textes, détection et extraction des lignes, reconnaissance de texte --&nbsp;arménien, géorgien, syriaque, écritures arabes, grec ancien, etc[^30]. Les travaux d'annotation et de transcription peuvent être menés en collaboration avec plusieurs membres d'une équipe et la plateforme prend en charge différents types de format. Une liste non exhaustive des modèles pré-entraînés disponibles est proposée dans le tableau&nbsp;4. La langue associée à chaque nom correspond à la langue dominante et au cas classique d'utilisation, sans pour autant exclure toute autre langue. Les projets spécialisés peuvent être développés et mis à disposition par les utilisateurs et utilisatrices de la plateforme, au bénéfice de toute la communauté, comme c'est le cas pour le projet ```Arabic manuscripts (Zijlawi)```.

<div class="alert alert-warning">
Par défaut, les projets et modèles proposent une approche par <i>baseline</i>, comme celle présentée jusqu'à présent. Ce choix permet d'assurer l'interopérabilité avec les autres plateformes mentionnées précédemment. Néanmoins, d'autres structures d'annotation sont proposées, mais sur demande uniquement.
</div>

<div class="table-wrapper" markdown="block">
<caption>Tableau&nbsp;4&nbsp;: Exemple de types de projets disponibles gratuitement et prêts à l'emploi sur la plateforme Calfa Vision (v1.9, 06/2022). Liste non exhaustive.</caption>
 
| Type de projet                             | Description                                                                                                                                                                                                                                                                         |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Projets génériques**                        |                                                                                                                                                                                                                                                                                     |
| Arabic manuscripts (default)               | Modèles de mise en page génériques pour une grande variété de manuscrits historiques arabes, simples et complexes, avec nombreux contenus marginaux courbes et endommagés.                                                                                                         |
| Armenian archives                          | Modèles de mise en page génériques pour des documents d'archives, principalement en langue arménienne --&nbsp;mises en page simples à très complexes, notamment des lettres&nbsp;--, avec classification sémantique des contenus --&nbsp;destinataire, signataire, date, contenu, marges, etc.          |
| Chinese printed                            | Modèles de mise en page génériques pour le traitement de textes verticaux imprimés anciens, avec mises en page simples à très denses.                                                                                                                                              |
| Default                                    | Modèles de mise en page génériques entraînés sur une très large variété de documents anciens et modernes, imprimés et manuscrits, avec classification sémantique des contenus. Capables d'une très grande polyvalence et d'une spécialisation rapide dans un grand nombre de cas. |
| Ethiopian archives                         | Modèles de mise en page génériques pour des documents d'archives extrêmement denses, avec grande variété de mises en page, avec classification sémantique des contenus.                                                                                                           |
| Newspaper                                  | Modèles de mise en page génériques pour l'analyse, la compréhension et la segmentation de journaux anciens et nouveaux. Classification sémantique des contenus pour l'arménien et l'arabe.                                                                                          |
| Printed documents                          | Modèles de mise en page génériques pour le traitement de documents imprimés anciens, modernes et contemporains, avec une grande variété de mises en page et de langues.                                                                                                            |
| **Projets spécialisés (liste non exhaustive)** |                                                                                                                                                                                                                                                                                     |
| Arabic manuscripts (Zijlawi)               | Modèles de mise en page spécialisés pour les manuscrits Zijlawi --&nbsp;arabe, mise en page complexe avec un texte très dense et des *marginalia* verticaux. Mis à disposition par un utilisateur de la plateforme.                                                                         |
| Greek printed (*Patrologia Graeca*)          | Modèles de mise en page spécialisés pour la PG --&nbsp;détection d'informations grecques dans des documents multilingues. Type de modèle utilisé dans la leçon pour *Programming Historian*.                                                                                 |

</div>

Ces modèles, en mesure de traiter un large spectre non exhaustif de documents, peuvent ne pas être parfaitement adaptés à notre chantier d'annotation de la PG. En revanche, la plateforme, qui repose donc sur le *fine-tuning* itératif de ses modèles en fonction des annotations des utilisateurs et utilisatrices, doit pouvoir rapidement se spécialiser sur un nouveau cas. Ainsi, partant par exemple d'un modèle de base pour la mise en page, nos relectures et précisions vont progressivement être intégrées dans le modèle afin de correspondre aux besoins de notre projet. Les différentes plateformes mentionnées précédemment intègrent des approches plus ou moins similaires pour le *fine-tuning* de leurs modèles, le lecteur ou la lectrice pourra donc réaliser un travail similaire sur ces plateformes. Calfa Vision a ici l'avantage de limiter l'engagement de chacun(e) à l'analyse de ses besoins, le *fine-tuning* étant réalisé de façon autonome au fil des annotations.

{% include figure.html filename="figure13_defaultLayout.jpeg" alt="Deux exemples d'analyse de la mise en page de la PG sur Calfa Vision" caption="Figure&nbsp;13&nbsp;: Calfa Vision - Analyse automatique de la mise en page sur deux exemples de la PG. En haut, le modèle détecte bien les multiples zones de texte, sans distinction, et l'ordre de lecture est le bon. En bas, la compréhension du document n'est pas satisfaisante et a entraîné une fusion des différentes colonnes et lignes." %}

Nous observons sur la figure&nbsp;13 que le modèle pré-entraîné à partir du modèle issu des projets ```Printed documents``` de la plateforme donne des résultats allant de très satisfaisants (en haut) à plus mitigés (en bas). Outre la mise sur le même plan de tous les types de régions, catégorisées en ```paragraph```, le modèle ne réussit pas toujours à comprendre la disposition en colonne. En revanche, malgré une fusion de toutes les lignes dans le second cas, l'ensemble des zones et des lignes est correctement détecté, il n'y a pas d'informations perdues. Nous pouvons donc supposer que la création d'un nouveau modèle spécialisé pour la PG sera rapide.

#### Quelles annotations de mise en page réaliser&#x202F;?

Pour les pages où la segmentation des zones est satisfaisante, nous devons préciser à quel type chaque zone de texte correspond, en spécifiant ce qui relève d'un texte en grec (en rouge sur les figures 8a et 8b) et ce qui relève d'un texte en latin (en bleu), et supprimer tout autre contenu jugé inutile dans notre traitement.
Pour les pages non satisfaisantes, nous devrons corriger les annotations erronées.

Concernant la transcription du texte, le modèle construit précédemment donne un taux d'erreur au niveau du caractère de 68,13&nbsp;% sur la PG --&nbsp;test hors domaine[^31]&nbsp;--, autrement dit il est inexploitable en l'état au regard de la grande différence qui existe entre les données d'entraînement et les documents ciblés. Nous nous retrouvons bien dans un scénario d'écriture peu dotée en raison de l'extrême particularité des impressions de la PG.

Au regard des difficultés identifiées en figure&nbsp;9 et de la grande dégradation du document, une architecture au niveau du caractère pourrait ne pas être la plus adaptée. Nous pouvons supposer l'existence d'un vocabulaire récurrent, au moins à l'échelle d'un volume de la PG. Le problème de reconnaissance pourrait ainsi être simplifié avec un apprentissage au mot plutôt qu'au caractère. Il existe une grande variété d'architectures neuronales qui sont implémentées dans les diverses plateformes de l'état de l'art[^32]. Elles présentent toutes leurs avantages et inconvénients en termes de polyvalence et de volume de données nécessaires. Néanmoins, une architecture unique pour tout type de problème peut conduire à un investissement beaucoup plus important que nécessaire. Dans ce contexte, la plateforme que nous utilisons opère un choix entre des architectures au caractère ou au mot, afin de simplifier la reconnaissance en donnant un poids plus important au contexte d'apparition du caractère et du mot. Il s'agit d'une approche qui a montré de bons résultats pour la lecture des abréviations du latin --&nbsp;à une forme graphique abrégée dans un manuscrit on transcrit un mot entier[^33]&nbsp;-- ou la reconnaissance des écritures arabes maghrébines --&nbsp;gestion d'un vocabulaire avec diacritiques ambigus et ligatures importantes[^34].

<div class="alert alert-info">
Le modèle d'analyse de la mise en page semble donc aisément <i>fine-tunable</i>. La reconnaissance de texte, malgré un modèle de grec déjà disponible, s'annonce plus compliquée. Un nouveau choix architectural s'avèrera peut-être pertinent.
</div>

#### Quel volume de données&#x202F;?

Il est très difficile d'anticiper le nombre de données nécessaire pour le *fine-tuning* des modèles. Une évaluation de la plateforme montre une adaptation pertinente de l'analyse de la mise en page et de la classification des zones de texte dès 50 pages pour des mises en page complexes sur des manuscrits arabes[^35]. Le problème est ici plus simple --&nbsp;moins de variabilité du contenu. Pour la détection des lignes, 25 pages suffisent[^36]. Il n'est toutefois pas nécessaire d'atteindre ces seuils pour mesurer le gain dans l'analyse et la détection.

Au niveau de la transcription, l'état de l'art met en évidence un besoin minimal de 2000 lignes pour entraîner un modèle OCR/HTR[^37], ce qui peut correspondre à une moyenne entre 75 et 100 pages pour des documents manuscrits sur les *scripta* non latines. Pour la PG, au regard de la densité particulière du texte, cela correspond à une moyenne de 50 pages.

Ströbel et al.[^38] montrent par ailleurs qu'au-delà de 100 pages il n'existe pas de grande différence entre les modèles pour un problème spécifique donné. L'important n'est donc pas de miser sur un gros volume de données, mais au contraire de concentrer l'attention sur la qualité des données produites et leur adéquation avec l'objectif recherché.

Toutefois, ces volumes correspondent aux besoins de modèles entraînés de zéro. Dans un cas de *fine-tuning*, les volumes sont bien inférieurs. Via la plateforme Calfa Vision, nous avons montré une réduction de 2,2&nbsp;% du CER pour de l'arménien manuscrit[^39] avec seulement trois pages transcrites, passant de 5,42&nbsp;% à 3,22&nbsp;% pour un nouveau cahier des charges de transcription, ou encore un CER de 9,17&nbsp;% atteint après 20 pages transcrites en arabe maghrébin pour un nouveau modèle --&nbsp;réduction de 90,83&nbsp;% du volume de données nécessaire par rapport à un modèle entraîné depuis zéro[^40].

Les dernières expériences montrent une spécialisation pertinente des modèles après seulement dix pages transcrites.

<div class="alert alert-info">
En règle générale, une bonne stratégie consiste à concentrer l'attention sur les pages les plus problématiques, et l'objectif de ces plateformes d'annotation consiste donc à permettre leur rapide correction.
</div>

#### Introduction à la plateforme d'annotation

Le détail des principales étapes sur la plateforme Calfa Vision est donné en figures&nbsp;14 et 15. L'accent est tout d'abord mis sur la gestion de projets, qui permet à un utilisateur ou une utilisatrice de créer, de gérer et de superviser des projets d'annotation, seul(e) ou en équipe. La figure&nbsp;14 illustre la procédure de création d'un nouveau projet, en particulier la sélection d'un type de projet, et d'ajout de nouvelles images.

{% include figure.html filename="figure14_Steps_CalfaVision_1.jpg" alt="Liste des étapes pour la création d'un projet OCR sur Calfa Vision" caption="Figure&nbsp;14&nbsp;: Calfa Vision - Résumé de l'interface et des étapes de création de projets" %}

La figure&nbsp;15 résume les étapes essentielles pour l'annotation automatique d'une image. Le détail est donné dans la suite de cette leçon à travers l'application sur la PG. Chacun(e) est libre d'utiliser les modèles d'analyse de la mise en page et de génération des lignes, sans limite en volume, tandis que la reconnaissance du texte est quant à elle conditionnée au type de profil.

{% include figure.html filename="figure15_Steps_CalfaVision_2.jpg" alt="Liste des étapes pour l'annotation de documents sur Calfa Vision" caption="Figure&nbsp;15&nbsp;: Calfa Vision - Résumé de l'interface et des étapes d'annotation de documents" %}

Un [tutoriel complet](https://vision.calfa.fr/app/guide) de chaque étape est proposé sur la plateforme; il est disponible après connexion. Le lectorat y trouvera des détails sur les formats d'import et d'export, les scripts automatiques, la gestion de projet, l'ajout de collaborateurs et collaboratrices ainsi que de nombreuses autres fonctionnalités propres à la plateforme qu'il n'est pas possible d'aborder dans cette leçon plus générale. La démarche classique consiste à&nbsp;:
1. Créer un compte sur la plateforme
2. Créer un projet pour chaque document cible
3. Importer ses images, et ses annotations si l'on en dispose déjà, et lancer les scripts d'analyse automatique
4. Vérifier les prédictions obtenues


<div class="alert alert-info">
La plateforme Calfa Vision propose gratuitement et sans limite l'utilisation et la spécialisation automatique des modèles de mise en page. La reconnaissance de caractères et la création de modèles sur-mesure est proposée dans le cadre d'un <a href="https://calfa.fr/ocr">forfait Recherche</a>, ainsi qu'aux partenaires, avec suivi du projet par les équipes de Calfa. Calfa s'engage également en proposant <a href="https://calfa.fr/contact-openocr">ce service gratuitement</a> pour un corpus limité dans le cadre d'une recherche.
</div>

### Étapes d'annotation

*Nous avons construit un premier* dataset *composé de 30 pages représentatives de différents volumes de la PG. Ces 30 pages nous servent d'ensemble de test pour évaluer précisément les modèles tout au long de l'annotation. Les annotations produites dans la suite de cette partie constituent l'ensemble d'apprentissage (voir figures&nbsp;5 et 6).*

{% include figure.html filename="figure16_projet.jpg" alt="Liste des images dans un projet sur Calfa Vision" caption="Figure&nbsp;16&nbsp;: Calfa Vision - Liste des images d'un projet de transcription" %}

#### Gestion du projet d'annotation

Après avoir créé un projet *Patrologia Graeca* de type ```Printed documents``` (v1.9 06/2022), nous ajoutons les documents que nous souhaitons annoter au niveau de la mise en page et du texte. L'import peut être réalisé avec une image, un fichier ZIP d'images, avec un manifeste IIIF --&nbsp;fichier ```JSON``` mis à disposition par les bibliothèques compatibles IIIF, contenant les métadonnées du document et les liens vers chaque image&nbsp;-- ou, dans notre cas, en important un fichier PDF. La figure&nbsp;16 montre l'interface utilisateur avec les images en attente d'annotation.

Une fois devant l'interface de transcription d'une image (voir figure&nbsp;15), nous disposons de plusieurs actions pour réaliser des analyses automatiques de nos documents&nbsp;:
1. ```Layout Analysis``` qui va détecter et classifier des zones et lignes de texte
2. ```Generate Polygons``` qui va extraire des lignes détectées la ligne entière à transcrire --&nbsp;détection de la *bounding box* ou du polygone encadrant, sous réserve de lignes détectées
3. ```Text Recognition``` qui va procéder à la reconnaissance des lignes détectées et extraites

Les trois étapes sont dissociées afin de laisser à chacun(e) le contrôle complet du *pipeline* de reconnaissance, avec notamment la possibilité de corriger toute prédiction incomplète ou erronée. Nous procédons à ce stade à l'analyse de la mise en page, massivement sur l'ensemble des images du projet.

#### Annotation de la mise en page

En accédant à l'interface d'annotation, les prédictions sont prêtes à être relues. Nous avons trois niveaux d'annotation dans le cadre de ce projet&nbsp;:

```
├── La région de texte (en vert), avec un type associé
│   └── La ligne de texte, composée
|       ├── D'une baseline (en rouge)
|       └── D'un polygone ou d'une bounding box (en bleu)
|           └── La transcription
```

{% include figure.html filename="figure17_layout2.jpg" alt="Exemple d'annotation d'une page sur Calfa Vision" caption="Figure&nbsp;17&nbsp;: Calfa Vision - Interface d'annotation et mise en page" %}

Il n'est pas nécessaire de pré-traiter les images et d'en réaliser une quelconque amélioration -&nbsp;redressement, nettoyage, etc.

Chaque objet --&nbsp;région, ligne et texte&nbsp;-- peut être manuellement modifié, déplacé, supprimé, etc. en fonction de l'objectif poursuivi. Ici, nous nous assurons de ne conserver que les zones que nous souhaitons reconnaître, à savoir ```col_greek``` et ```col_latin```, auxquelles nous ajoutons cette information sémantique. C'est l'occasion également de contrôler que les lignes ont bien été détectées, notamment pour les pages qui posent problème.

Nous réalisons ce contrôle sur 10, 30 et 50 pages pour mesurer l'impact sur la détection de ces régions de texte.

<div class="table-wrapper" markdown="block">
<caption>Tableau&nbsp;5&nbsp;: Évolution de la distinction des colonnes latines et grecques</caption>
 
| *mean* IoU    | 0 image | 10 images | 30 images | 50 images |
|-----------|---------|-----------|-----------|-----------|
| Paragraph | 0.94    | -         | -         | -         |
| Col_greek | -       | 0.86      | 0.91      | 0.95      |
| Col_latin | -       | 0.78      | 0.88      | 0.93      |

</div>


Nous observons dans le tableau&nbsp;5 que la distinction des zones de texte s'opère correctement dès dix images annotées, au niveau des régions. Dès 50 images, le modèle classifie à 95&nbsp;% les colonnes grecques et à 93&nbsp;% les colonnes latines. Les erreurs sont localisées sur les textes traversants, et sur la détection superfétatoire de notes de bas de page, respectivement en grec et en latin. Pour ce dernier cas de figure, il ne s'agit donc pas à proprement parler d'erreurs, même si cela entraîne un contenu non souhaité dans le résultat.

{% include figure.html filename="figure18_pred_PG.jpeg" alt="Évolution de la détection des zones et lignes de textes après 10, 30 et 50 images annotées" caption="Figure&nbsp;18&nbsp;: Évolution de la détection des zones et lignes de textes" %}

Avec ce nouveau modèle, l'annotation de la mise en page est donc beaucoup plus rapide. La correction progressive de nouvelles images permettra de surmonter les erreurs observées.

<div class="table-wrapper" markdown="block">
<caption>Tableau&nbsp;6&nbsp;: Évolution de la détection des <i>baselines</i></caption>

|           | F1-score |
|-----------|----------|
| 0 image   |  0.976   |
| 10 images |  0.982   |
| 30 images |  0.981   |
| 50 images |  0.981   |

</div>


Nous n'allons pas développer davantage sur la métrique utilisée ici[^41]. Concernant la détection des lignes, contrairement à ce que nous pouvions observer avec la détection des régions (figure 18), ici dix images suffisent à obtenir immédiatement un modèle très performant. L'absence d'annotation des notes de base de page conduit en particulier à créer une ambiguïté dans le modèle, d'où la stagnation des scores obtenus, pour lesquels on observe une précision «&nbsp;basse&nbsp;» --&nbsp;toutes les lignes détectées&nbsp;-- mais un rappel élevé --&nbsp;toutes les lignes souhaitées détectées. En revanche, cela n'a pas d'incidence sur le traitement des pages pour la suite, puisque seul le contenu des régions ciblées est pris en compte.

#### Annotation du texte

{% include figure.html filename="figure19_text.jpg" alt="L'interface de transcription sur Calfa Vision" caption="Figure&nbsp;19&nbsp;: Calfa Vision - Transcription du texte" %}

La transcription est réalisée ligne à ligne pour correspondre à la vérité terrain dont nous disposons déjà (voir *supra*). Cette transcription peut être réalisée entièrement manuellement, ou être assistée par l'OCR intégré, ou encore provenir d'une transcription existante et importée. Les lignes 1 et 7 mettent en évidence l'absence de transcription des chiffres dans cet exercice. Les données sont exportées dans un format compatible avec les données précédentes, paire image-texte, sans distorsion des images.

<div class="alert alert-warning">
L'export est réalisé en allant sur la page des informations de l'image --&nbsp;bouton <code>Info</code>&nbsp;-- et en choisissant le format d'export qui convient. Comme détaillé précédemment, afin de bénéficier des données pré-existantes pour renforcer notre apprentissage, nous choisissons l'export par paire image-texte. Aucune distorsion de la <i>baseline</i> n'est appliquée, celle-ci, lorsqu'elle est réalisée, pouvant entraîner une complexité supplémentaire à surmonter, nécessitant davantage de données.
</div>

Nous allons donc ici transcrire une, puis deux, puis cinq et enfin dix images, en profitant itérativement d'un nouveau modèle de transcription automatique.

<div class="table-wrapper" markdown="block">
<caption>Tableau&nbsp;7&nbsp;: Évolution du CER en fonction du nombre d'images transcrites</caption>
 
|         | 0     | 1     | 2    | 5    | 10   |
|---------|-------|-------|------|------|------|
| CER (%) | 68,13 | 38,45 | 6,97 | 5,42 | 4,19 |

</div>

Deux images suffisent à obtenir un CER inférieur à 7&nbsp;% et une transcription automatique exploitable. Le modèle n'est bien sûr pas encore très polyvalent à toute la variété de la PG mais la transcription de nouvelles pages s'en trouve accélérée. Dans les simulations réalisées à plus grande échelle, en conservant cette approche itérative, nous aboutissons à un CER de 1,1&nbsp;% après 50 pages transcrites.


{% include figure.html filename="figure20_PG-result.jpeg" alt="Exemple d'OCR de la PG avec le modèle final" caption="Figure&nbsp;20&nbsp;: Résultat final sur la PG" %}


## Ouverture sur le manuscrit et conclusion

La transcription de documents manuscrits --&nbsp;mais aussi celle de manuscrits anciens, d'archives modernes, etc.&nbsp;-- répond tout à fait à la même logique et aux mêmes enjeux&nbsp;: partir de modèles existants, que l'on va spécialiser aux besoins d'un objectif, selon un certain cahier des charges.

La plateforme a ainsi été éprouvée sur un nouvel ensemble graphique, celui des écritures maghrébines, écritures arabes qui représentent classiquement un écueil majeur pour les HTR. L'approche itérative qui a été appliquée a permis d'aboutir à la transcription de 300 images, constituant le *dataset* RASAM[^42], sous la supervision du [Groupement d'Intérêt Scientifique Moyen-Orient et mondes musulmans (GIS MOMM)](https://perma.cc/8DJM-HC9E), de la [BULAC](https://perma.cc/B79M-SGZV) et Calfa. En partant de zéro pour les écritures maghrébines, cette approche de *fine-tuning* à l'aide d'une interface de transcription comme celle présentée dans ce tutoriel a démontré sa pertinence&nbsp;: le temps nécessaire à la transcription est ainsi réduit de plus de 42&nbsp;% en moyenne (voir figure&nbsp;21).

{% include figure.html filename="figure21_time_saved_transcription.png" alt="Courbe d'évolution du gain de temps dans l'annotation avec un outil d'annotation et de transcription automatisé" caption="Figure&nbsp;21&nbsp;: RASAM Dataset, Springer 2021 - Évolution du CER et du temps de relecture" %}

Dans ce tutoriel, nous avons décrit les bonnes pratiques pour la transcription rapide de documents en systèmes graphiques ou en langues peu dotés via la plateforme Calfa Vision. La qualification de «&nbsp;peu dotée&nbsp;» peut concerner un grand nombre et une large variété de documents, y compris, comme ce fut le cas ici, dans des langues pour lesquelles il existe pourtant déjà des données. La qualité des données ne doit pas être négligée par rapport à la quantité, et l'utilisateur ou l'utilisatrice pourra dès lors envisager une transcription, y compris pour des documents inédits.


<div class="alert alert-info">
La stratégie de <i>fine-tuning</i> s'avère très pertinente dans les situations où il n'est pas possible de constituer un jeu de données suffisant, quelque soit le document ou la langue. Néanmoins, il faut prendre garde au fait que les modèles ainsi créés sont dès lors sur-spécialisés sur la problématique cible, en raison de tous les choix éditoriaux présentés. Cette stratégie n'est par ailleurs pas unique&nbsp;: il existe par exemple en apprentissage machine des stratégies reposant sur l'<a href="https://perma.cc/D6F4-G5PG">augmentation des données</a>.
</div>

Des questions plus techniques peuvent se poser selon la plateforme utilisée et un accompagnement dans les projets de transcription peut alors être proposé. Définir précisément les besoins d'un traitement OCR/HTR est essentiel au regard des enjeux, la transcription automatique étant une porte d'entrée à tout projet de valorisation et de traitement de collections.

Les données générées pour cet article et dans le cadre du projet CGPG sont disponibles sur Zenodo ([https://doi.org/10.5281/zenodo.7296539](https://doi.org/10.5281/zenodo.7296539)). La rédaction de cet article a été réalisée en utilisant la version 1.0.0 du jeu de données. Le modèle d'analyse de la mise en page reste disponible sur Calfa Vision sous l'appellation ```Greek printed (Patrologia Graeca)```, modèle régulièrement renforcé.



## Notes de fin

[^1]: Les volumes de la PG sont disponibles au format PDF, par exemple sous les adresses [https://patristica.net/graeca](https://patristica.net/graeca) et [https://www.roger-pearse.com/weblog/patrologia-graeca-pg-pdfs](https://perma.cc/9QR4-2PVU). Mais une partie seulement de la PG est encodée sous un format «&nbsp;textes&nbsp;», par exemple dans le corpus du [Thesaurus Linguae Graecae](https://perma.cc/LV3A-GL66).

[^2]: L'association Calfa (Paris, France) et le projet GRE*g*ORI (université catholique de Louvain, Louvain-la-Neuve, Belgique) développent conjointement des systèmes de reconnaissance de caractères et des systèmes d'analyse automatique des textes&nbsp;: lemmatisation, étiquetage morphosyntaxique, *POS_tagging*. Ces développements ont déjà été adaptés, testés et utilisés pour traiter des textes en arménien, en géorgien et en syriaque. Le projet CGPG poursuit ces développements dans le domaine du grec en proposant un traitement complet --&nbsp;OCR et analyse&nbsp;-- de textes édités dans la PG. Pour des exemples de traitement morphosyntaxique du grec ancien menés conjointement&nbsp;: Kindt, Bastien, Chahan Vidal-Gorène, et Saulo Delle Donne. «&nbsp;Analyse automatique du grec ancien par réseau de neurones. Évaluation sur le corpus De Thessalonica Capta&nbsp;». *BABELAO* 10-11 (2022), 525-550. [https://doi.org/10.14428/babelao.vol1011.2022.65073](https://doi.org/10.14428/babelao.vol1011.2022.65073).

[^3]: Voir par exemple Alex Graves et Jürgen Schmidhuber. (2008). «&nbsp;Offline Handwriting Recognition with Multidimensional Recurrent Neural Networks&nbsp;». In *Advances in Neural Information Processing Systems* 21 (NIPS 2008), dirigé par Daphne Koller *et al.* (S.l.&nbsp;: Curran Associates, 2009) [https://papers.nips.cc/paper/2008/file/66368270ffd51418ec58bd793f2d9b1b-Paper.pdf](https://perma.cc/N9N7-BB6R).

[^4]: Stuart Snydman, Robert Sanderson, et Tom Cramer. «&nbsp;The International Image Interoperability Framework (IIIF)&nbsp;: A community & technology approach for web-based images&nbsp;». *Archiving Conference*, 2015, 16‑21.

[^5]: Ryad Kaoua, Xi Shen, Alexandra Durr, Stavros Lazaris, David Picard, et Mathieu Aubry. «&nbsp;Image Collation&nbsp;: Matching Illustrations in Manuscripts&nbsp;». In *Document Analysis and Recognition – ICDAR 2021*, dirigé par Josep Lladós, Daniel Lopresti, et Seiichi Uchida. Lecture Notes in Computer Science, vol. 12824. Cham&nbsp;: Springer, 2021, 351‑66. [https://doi.org/10.1007/978-3-030-86337-1_24](https://doi.org/10.1007/978-3-030-86337-1_24).

[^6]: Emanuela Boros, Alexis Toumi, Erwan Rouchet, Bastien Abadie, Dominique Stutzmann, et Christopher Kermorvant. «&nbsp;Automatic Page Classification in a Large Collection of Manuscripts Based on the International Image Interoperability Framework&nbsp;». In *Document Analysis and Recognition - ICDAR 2019*, 2019, 756‑62, [https://doi.org/10.1109/ICDAR.2019.00126](https://doi.org/10.1109/ICDAR.2019.00126).

[^7]: Mathias Seuret, Anguelos Nicolaou, Dalia Rodríguez-Salas, Nikolaus Weichselbaumer, Dominique Stutzmann, Martin Mayr, Andreas Maier, et Vincent Christlein. «&nbsp;ICDAR 2021 Competition on Historical Document Classification&nbsp;». In *Document Analysis and Recognition – ICDAR 2021*, dirigé par Josep Lladós, Daniel Lopresti, et Seiichi Uchida. Lecture Notes in Computer Science, vol 12824. Cham&nbsp;: Springer, 2021, 618‑34. [https://doi.org/10.1007/978-3-030-86337-1_41](https://doi.org/10.1007/978-3-030-86337-1_41).

[^8]: Il existe une grande variété de jeux de données (ou *datasets*) existants réalisés dans divers cadres de recherche, les personnes intéressées et à la recherche de données pourront notamment trouver un grand nombre de données disponibles dans le cadre de l'[initiative HTR United](https://perma.cc/59X7-PGL6). Alix Chagué, Thibault Clérice, et Laurent Romary. «&nbsp;HTR-United&nbsp;: Mutualisons la vérité de terrain&#x202F;!&nbsp;», *DHNord2021 - Publier, partager, réutiliser les données de la recherche&nbsp;: les data papers et leurs enjeux*, Lille, MESHS, 2021. [https://hal.archives-ouvertes.fr/hal-03398740](https://perma.cc/4YL8-56C8).

[^9]: En particulier, le lectorat pourra trouver un grand nombre de données pour le français médiéval homogènes dans le cadre du projet CREMMA (Consortium pour la Reconnaissance d’Écriture Manuscrite des Matériaux Anciens). Ariane Pinche. «&nbsp;HTR Models and genericity for Medieval Manuscripts&nbsp;». 2022. [https://hal.archives-ouvertes.fr/hal-03736532/](https://perma.cc/93T5-8622).

[^10]: Nous pouvons par exemple citer le programme «&nbsp;[Scripta-PSL. Histoire et pratiques de l'écrit](https://perma.cc/LV5F-WMYY)&nbsp;» qui vise notamment à intégrer dans les humanités numériques une grande variété de langues et écritures anciennes et rares&#x202F;; l'[Ottoman Text Recognition Network](https://perma.cc/XG3X-FDMM) pour le traitement des graphies utilisées lors de la période ottomane&#x202F;; ou encore le [Groupement d'Intérêt Scientifique Moyen-Orient et mondes musulmans (GIS MOMM)](https://perma.cc/8DJM-HC9E) qui, en partenariat avec la [BULAC](https://perma.cc/B79M-SGZV) et [Calfa](https://perma.cc/VK4M-P3HH), produit des jeux de données pour le [traitement des graphies arabes maghrébines](https://perma.cc/G7RW-3LPL).

[^11]: Le *crowdsourcing* peut prendre la forme d'ateliers dédiés avec un public restreint, mais est aussi largement ouvert à tout public bénévole qui souhaite occasionnellement transcrire des documents, comme le propose la [plateforme Transcrire](https://perma.cc/F9TP-949U) déployée par Huma-Num.

[^12]: Christian Reul, Dennis Christ, Alexander Hartelt, Nico Balbach, Maximilian Wehner, Uwe Springmann, Christoph Wick, Christine Grundig, Andreas Büttner, et Frank Puppe. «&nbsp;OCR4all—An open-source tool providing a (semi-)automatic OCR workflow for historical printings&nbsp;». *Applied Sciences* 9, nᵒ 22 (2019)&nbsp;: 4853.

[^13]: Chahan Vidal-Gorène, Boris Dupin, Aliénor Decours-Perez, et Thomas Riccioli. «&nbsp;A modular and automated annotation platform for handwritings&nbsp;: evaluation on under-resourced languages&nbsp;». In *International Conference on Document Analysis and Recognition - ICDAR 2021*, dirigé par Josep Lladós, Daniel Lopresti, et Seiichi Uchida. 507-522. Lecture Notes in Computer Science, vol. 12823. Cham&nbsp;: Springer, 2021. [https://doi.org/10.1007/978-3-030-86334-0_33](https://doi.org/10.1007/978-3-030-86334-0_33).

[^14]: Jean-Baptiste Camps, Chahan Vidal-Gorène, Dominique Stutzmann, Marguerite Vernet, et Ariane Pinche, «&nbsp;Data Diversity in handwritten text recognition, Challenge or opportunity?&nbsp;», article présenté lors de la conférence *Digital Humanities 2022* (DH 2022), Tokyo, 27 juillet 2022.

[^15]: Pour un exemple de stratégie de *fine-tuning* appliquée à des graphies arabes manuscrites. Bulac Bibliothèque, Maxime Ruscio, Muriel Roiland, Sarah Maloberti, Lucas Noëmie, Antoine Perrier, et Chahan Vidal-Gorène. «&nbsp;Les collections de manuscrits maghrébins en France (2/2)&nbsp;», Mai 2022, HAL, [https://medihal.archives-ouvertes.fr/hal-03660889](https://perma.cc/NEU3-7TH3).

[^16]: Jean-Baptiste Camps. «&nbsp;Introduction à la philologie computationnelle. Science des données et science des textes&nbsp;: De l'acquisition du texte à l'analyse&nbsp;», présenté dans le cadre de la formation en ligne *Étudier et publier les textes arabes avec le numérique*, 7 décembre 2020, YouTube, [https://youtu.be/DK7oxn-v0YU](https://youtu.be/DK7oxn-v0YU).

[^17]: Dans une architecture *word-based*, chaque mot constitue une classe à part entière. Si cela entraîne mécaniquement une démultiplication du nombre de classes, le vocabulaire d'un texte est en réalité suffisamment homogène et réduit pour envisager cette approche. Elle n'est pas incompatible avec une architecture *character-based* complémentaire.

[^18]: Jean-Baptiste Camps, Chahan Vidal-Gorène, et Marguerite Vernet. «&nbsp;Handling Heavily Abbreviated Manuscripts: HTR engines vs text normalisation approaches&nbsp;». In *International Conference on Document Analysis and Recognition - ICDAR 2021*, dirigé par Elisa H. Barney Smith, Umapada Pal. Lecture Notes in Computer Science, vol. 12917. Cham&nbsp;: Springer, 2021, 507-522. [https://doi.org/10.1007/978-3-030-86159-9_21](https://doi.org/10.1007/978-3-030-86159-9_21).

[^19]: Pour davantage de manipulations Unicode en grec ancien&nbsp;: [https://jktauber.com/articles/python-unicode-ancient-greek/](https://perma.cc/7U33-XFC7) [consulté le 12 février 2022].

[^20]: À titre d'exemple, concernant la normalisation, avec NFD, nous obtenons un CER (voir plus loin) de 22,91&nbsp;% avec dix pages contre 4,19&nbsp;% avec la normalisation NFC.

[^21]: Par défaut, Calfa Vision va procéder au choix de normalisation le plus adapté au regard du jeu de données fourni, afin de simplifier la tâche de reconnaissance, sans qu'il soit nécessaire d'intervenir manuellement. La normalisation est toutefois paramétrable avant ou après le chargement des données sur la plateforme.

[^22]: Pour accéder aux jeux de données mentionnés&nbsp;: [greek_cursive](https://perma.cc/52BW-L7GT), [gaza-iliad](https://perma.cc/L783-BFVG) et [voulgaris-aeneid](https://perma.cc/JN4Z-Y4UQ).

[^23]: Matteo Romanello, Sven Najem-Meyer, et Bruce Robertson. «&nbsp;Optical Character Recognition of 19th Century Classical Commentaries: the Current State of Affairs&nbsp;».  In *The 6th International Workshop on Historical Document Imaging and Processing* (2021): 1-6. *Dataset* également [disponible sur Github](https://perma.cc/9G7W-H5R5).

[^24]: Le modèle n'est pas évalué sur la PG à ce stade. Le taux d'erreur est obtenu sur un ensemble de test extrait de ces trois *datasets*.

[^25]: Thomas M. Breuel. «&nbsp;The OCRopus open source OCR system&nbsp;». In *Document recognition and retrieval XV*, (2008): 6815-6850. International Society for Optics and Photonics.

[^26]: La co-existence de données de type *bounding box* et de type *baseline* correspond à une évolution technique et chronologique. Le système OCR OCRopy, pionnier dans les OCR par réseaux de neurones, utilise des *bounding box*, excluant de fait tout document courbé. Ce système nécessite le pré-traitement des images avant d'envisager toute reconnaissance.

[^27]: Vidal-Gorène, Dupin, Decours-Perez, Riccioli. «&nbsp;A modular and automated annotation platform for handwritings: evaluation on under-resourced languages&nbsp;», 507-522.

[^28]: Camps, Vidal-Gorène, et Vernet. «&nbsp;Handling Heavily Abbreviated Manuscripts: HTR engines vs text normalisation approaches&nbsp;», 507-522.

[^29]: Vidal-Gorène, Dupin, Decours-Perez, Riccioli. «&nbsp;A modular and automated annotation platform for handwritings: evaluation on under-resourced languages&nbsp;», 507-522.

[^30]: L'étape de reconnaissance de texte, OCR ou HTR, est proposée sur demande et dans le cadre de projets dédiés ou partenaires. Les deux premières étapes du traitement sont quant à elles gratuites et utilisables sans limite.

[^31]: On distingue généralement deux types d’évaluation d’un modèle OCR/HTR&nbsp;: une évaluation *in-domain*, c’est à dire que l’ensemble de test est similaire aux données d’entraînement, et une évaluation *out-of-domain*, avec des données complètement nouvelles pour le modèle. Classiquement, un test *in-domain* donne des résultats élevés car le modèle est très spécifiquement entraîné sur la tâche évaluée, même si les données d’entraînement et de test sont bien sûr disjointes. Ce test permet notamment d’évaluer la pertinence d’un modèle spécialisé. Un test *out-of-domain* donne des informations sur la polyvalence et la «&nbsp;généralité&nbsp;» d’un modèle, car celui-ci est évalué sur des données absentes et inconnues de ses données d’entraînement --&nbsp;par exemple une nouvelle main ou un nouveau type d’écriture.

[^32]: Francesco Lombardi, et Simone Marinai. «&nbsp;Deep Learning for Historical Document Analysis and Recognition—A Survey&nbsp;». *J. Imaging* 2020, 6(10), 110. [https://doi.org/10.3390/jimaging6100110](https://doi.org/10.3390/jimaging6100110).

[^33]: Camps, Vidal-Gorène, et Vernet. «&nbsp;Handling Heavily Abbreviated Manuscripts: HTR engines vs text normalisation approaches&nbsp;», 507-522.

[^34]: Chahan Vidal-Gorène, Noëmie Lucas, Clément Salah, Aliénor Decours-Perez, et Boris Dupin. «&nbsp;RASAM–A Dataset for the Recognition and Analysis of Scripts in Arabic Maghrebi&nbsp;». In *International Conference on Document Analysis and Recognition - ICDAR 2021*, dirigé par Elisa H. Barney Smith, Umapada Pal. Lecture Notes in Computer Science, vol. 12916. Cham&nbsp;: Springer, 2021, 265-281. [https://doi.org/10.1007/978-3-030-86198-8_19](https://doi.org/10.1007/978-3-030-86198-8_19).

[^35]: *Ibid.*

[^36]: Vidal-Gorène, Dupin, Decours-Perez, Riccioli. «&nbsp;A modular and automated annotation platform for handwritings: evaluation on under-resourced languages&nbsp;», 507-522.

[^37]: Phillip Benjamin Ströbel, Simon Clematide, et Martin Volk. «&nbsp;How Much Data Do You Need? About the Creation of a Ground Truth for Black Letter and the Effectiveness of Neural OCR&nbsp;». In *Proceedings of the 12th Language Resources and Evaluation Conference*, 3551-3559. Marseille: ACL Anthology, 2020. [https://aclanthology.org/2020.lrec-1.436.pdf](https://perma.cc/YW4D-2D3L).

[^38]: *Ibid.*

[^39]: Bastien Kindt et Vidal-Gorène Chahan, «&nbsp;From Manuscript to Tagged Corpora. An Automated Process for Ancient Armenian or Other Under-Resourced Languages of the Christian East&nbsp;». *Armeniaca. International Journal of Armenian Studies* 1, 73-96, 2022. [http://doi.org/10.30687/arm/9372-8175/2022/01/005]( http://doi.org/10.30687/arm/9372-8175/2022/01/005)

[^40]: Vidal-Gorène, Lucas, Salah, Decours-Perez, et Dupin. «&nbsp;RASAM–A Dataset for the Recognition and Analysis of Scripts in Arabic Maghrebi&nbsp;», 265-281.

[^41]: Vidal-Gorène, Dupin, Decours-Perez, Riccioli. «&nbsp;A modular and automated annotation platform for handwritings: evaluation on under-resourced languages&nbsp;», 507-522.

[^42]: Le *dataset* RASAM est disponible au format PAGE (XML) sur [Github](https://perma.cc/UT9Y-A4GA). Il est le résultat d'un hackathon participatif ayant regroupé quatorze personnes organisé par le GIS MOMM, la BULAC, Calfa, avec le soutien du ministère français de l'enseignement supérieur et de la recherche.
