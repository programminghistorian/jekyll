---
title: "L’édition critique en continu&nbsp;: publier au rythme de l’encodage (Partie 1)"
slug: edition-critique-continu-pt1
layout: lesson
collection: lessons
date: 2026-10-02
authors:
- Clément Godbarge
reviewers:
- Jasmin Macarios
- Elsa Van Kote
editors:
- Matthias Gille Levenson
- Daphné Mathelier
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/674
difficulty: 3
activity: transforming
topics: [metadata, website, data-management]
abstract: Cette leçon montre comment mettre en place une édition critique &laquo;&nbsp;en continu&nbsp;&raquo; d’un corpus TEI&nbsp; définir un ODD, générer un schéma RELAX NG, compléter la validation avec Schematron et produire des sorties (texte/HTML/Markdown) via XSLT 2.0. L’exemple s’appuie sur la correspondance de Filippo Cavriana.
avatar_alt: Illustration d'un motif textile tissé composé de bandes verticales foncées et de bandes horizontales plus claires.
doi: 10.46430/phfr0044
---

{% include toc.html %}

## Introduction

L’édition critique traditionnelle suit un modèle de publication en bloc. L’intégralité du texte est préparée puis publiée lorsque le travail est jugé &laquo;&nbsp;achevé&nbsp;&raquo;. Héritée de l’imprimé, cette logique persiste à l’ère numérique, alors même que celui-ci permettrait d’autres rythmes et modalités de publication. Parce que les opérations techniques (conversion, validation, mise en ligne) sont souvent confiées à des spécialistes en fin de chaîne, la flexibilité du numérique demeure sous-exploitée.

Ce modèle s’adapte mal à l’édition critique de sources primaires. Sa rigidité impose une tolérance à l’erreur quasi nulle, ce qui retarde la diffusion de résultats déjà exploitables par la communauté scientifique. Il dissuade aussi nombre de chercheurs et chercheuses de l’intégrer à leur stratégie de publication, car ce travail de longue haleine, bien qu’essentiel à la recherche, reste peu reconnu. Son rapport coût-bénéfice défavorable en fait souvent une variable d’ajustement.

Face à ces limites, l’édition continue offre une alternative intéressante. Par &laquo;&nbsp;édition continue&nbsp;&raquo;, on entend une publication par incréments. Plutôt que d’attendre la finalisation d’un projet éditorial, on diffuse progressivement les documents au fur et à mesure de leur encodage et de leur révision, tout en facilitant les mises à jour régulières du corpus à mesure que de nouvelles sources apparaissent.

Cette approche repose sur des outils simples mais puissants de gestion de versions, tels que Git, qui permettent de suivre précisément chaque modification tout en favorisant une collaboration transparente. Des plateformes comme GitHub ou GitLab offrent en outre des solutions d’automatisation capables de transformer instantanément les fichiers encodés selon les standards de la *Text Encoding Initiative* ([TEI](https://perma.cc/WZG9-XZM7)) en ressources publiables sur le web et lisibles par des publics différents.

La clé de cette approche tient à une association entre travail éditorial et développement logiciel&nbsp;: représenter le texte encodé comme une donnée structurée et gérer son cycle de vie avec l’outillage de l’ingénierie logicielle. L’encodage TEI, fondé sur XML ([*eXtensible Markup Language*](https://perma.cc/L9PH-AHPY)), est après tout un code déclaratif&nbsp;: il se versionne, se valide et se transforme. Nous adaptons donc des pratiques éprouvées en programmation, notamment l’intégration et la livraison continues ([*Continuous Integration*, *Continuous Delivery*](https://perma.cc/29LZ-YA6Y)). Ces démarches automatisent le processus de préparation à la mise en ligne du texte. À chaque modification du corpus, la chaîne d’intégration exécute les contrôles de conformité. Puis, une chaîne de livraison prend le relais pour transformer le code en formats immédiatement exploitables. La distinction entre les deux termes tient au seuil de publication&nbsp;: la livraison continue produit à chaque mise à jour un livrable vérifié et prêt à publier, mais laisse le geste final à un humain&nbsp;; le déploiement continu franchit ce seuil et publie sans intervention. Sauf précision contraire, &laquo;&nbsp;livraison continue&nbsp;&raquo; désignera ici les deux étapes. Ainsi, l’ODD ([*One Document Does it all*](https://perma.cc/JT6L-87S8)) joue le rôle de spécification, RELAX NG ([*Regular Language for XML, Next Generation*](https://perma.cc/JF83-W7T3)) formalise les contraintes structurelles, [Schematron](https://perma.cc/GV8L-EYHU) les complète par des contraintes éditoriales spécifiques, tandis que les feuilles XSLT ([*eXtensible Stylesheet Language Transformations*](https://perma.cc/JBF9-5ZE8)) assurent la transformation du code en formats de sortie désirés ([HTML](https://perma.cc/TE4A-48CC), [Markdown](https://perma.cc/QM86-XMBG), etc.). Les plateformes telles que GitHub et GitLab permettent d’ajouter au dépôt de données une chaîne d’intégration et de déploiement continus ([CI/CD](https://perma.cc/5ZH5-5DWZ) - *Continuous Integration/Continuous Deployment*). Ainsi, chaque mise à jour du dépôt déclenche un contrôle de conformité et une transformation. Couplées à [Zenodo](https://perma.cc/Q2L3-NJXA), ces mêmes plateformes permettent aussi l’archivage à long terme de versions que l’on peut citer avec un identifiant numérique de type DOI ([*Digital Object Identifier*](https://perma.cc/36SB-FYDP)).

Le schéma ci-dessous résume les étapes de la chaîne de traitement complète, de l’encodage à la publication&nbsp;:

```text
ODD (spécification du projet)
├──▶ Schéma RELAX NG
├──▶ Règles Schematron
└──▶ Documentation d’encodage

Encodage TEI ──▶ Dépôt Git
                    │
                    ▼
            Chaîne CI/CD (déclenchée à chaque mise à jour)
            ├──▶ Validation RELAX NG (structure)
            ├──▶ Validation Schematron (logique éditoriale)
            ├──▶ Transformation XSLT (HTML, Markdown…)
            ├──▶ Publication (site web statique)
            └──▶ Archivage pérenne + DOI (Zenodo)
```

Cette leçon vous montre comment mettre en place une telle édition continue à partir d’un cas précis&nbsp;: la correspondance de Filippo Cavriana (1536-1606), médecin et espion italien à la cour de France et commentateur avisé des guerres de Religion, dont une édition numérique est [publiée en ligne](https://pantagrueliste.github.io/CavrianaCorr_FrontEnd/). Tous les outils mobilisés sont gratuits et compatibles avec tous les systèmes d’exploitation. La mise au point peut nécessiter une phase de débogage, mais cet effort en vaut la peine, car il accroît l’autonomie éditoriale, évite la dépendance à des solutions propriétaires et accélère la diffusion des résultats. 

La première partie couvre toutes les composantes de ce flux de travail éditorial. Vous y apprendrez les bases de la TEI, à définir un schéma adapté pour votre projet, à valider le code, et à le transformer localement. Connaître ces fondamentaux vous permettra d’éviter de nombreuses erreurs par la suite. La seconde partie se concentre sur l’infrastructure&nbsp;: gestion collaborative de versions, automatisations en intégration continue, publication sur site web statique et archivage de versions pérennes.

### Prérequis

- Connaissance basique du terminal/ligne de commande
- Notions de XML (balises, attributs)
- Un ordinateur sous Windows, macOS ou Linux
- Un terminal de type Unix&nbsp;: celui de macOS ou de Linux ou, sous Windows, celui que fournit WSL (voir ci-dessous)
- Droits d’administration pour l’installation par gestionnaire de paquets ou, à défaut, l’installation manuelle décrite plus bas
- Environnement d’Exécution Java ([JRE](https://perma.cc/WS78-W5SC)) installé
- Éditeur de texte (VS Code, Notepad++, Vim, Sublime Text, etc.)

### Organisation du projet

Avant de commencer, organisons notre espace de travail. Un projet d’édition TEI doit suivre une structure claire pour séparer les différents types de fichiers. À la racine du projet, créez quatre répertoires principaux&nbsp;:
- `letters/` contiendra les fichiers TEI-XML de la correspondance (une lettre par fichier)
- `templates/` regroupera vos fichiers de configuration personnalisés (ODD, schémas, XSLT) 
- `output/` recevra les résultats des transformations
- `common/` accueillera les feuilles de style TEI partagées, téléchargées plus bas

Pour les créer, une simple ligne de commande suffira:

```bash
mkdir -p letters templates common output
``` 

Cette leçon suppose un terminal POSIX et deux commandes disponibles dans celui-ci&nbsp;: `saxon` et `jing`. Les commandes sont données pour deux environnements, Ubuntu et macOS. Sous Windows, vous obtiendrez un terminal Ubuntu grâce à WSL, décrit juste après&nbsp;; sur une distribution Linux autre qu’Ubuntu, remplacez `apt` par votre gestionnaire de paquets. Trois chemins mènent au même résultat&nbsp;:

- L’installation par gestionnaire de paquets (APT ou Homebrew) est la plus simple, mais elle exige des droits d’administration
- L’installation manuelle des fichiers JAR dans votre répertoire personnel ne demande aucun privilège particulier
- Un environnement distant, par exemple un conteneur de développement, convient si vous ne pouvez rien installer sur votre machine

Une fois l’une de ces voies suivie, toutes les commandes de la leçon sont identiques.

Si vous utilisez Windows, la voie la plus simple est WSL (*Windows Subsystem for Linux*), qui installe [Ubuntu](https://fr.wikipedia.org/wiki/Ubuntu_(système_d%27exploitation)) par défaut et vous donne le même terminal que sous Linux. Son installation exige toutefois des droits d’administration, dont on ne dispose pas toujours sur une machine gérée par une institution. Dans ce cas, suivez l’installation manuelle décrite plus bas, qui ne demande aucun privilège particulier.

Sous WSL, placez votre projet dans le système de fichiers Linux (`~/cavriana`) plutôt que dans `/mnt/c/...`&nbsp;: les accès y sont nettement plus rapides, et vous éviterez qu’un éditeur Windows n’introduise des fins de ligne CRLF dans vos fichiers XML.

Si vous utilisez macOS, assurez-vous d’avoir installé au préalable Homebrew. Pour l’installer, exécutez cette commande sur le terminal&nbsp;: 

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Puis, vous pouvez l’exécuter pour installer les deux paquets&nbsp;:
```bash
brew install saxon
brew install jing-trang
```

Sur Ubuntu/WSL, APT est déjà installé mais requiert sudo&nbsp;; sur un système neuf, la liste des paquets doit être mise à jour une première fois&nbsp;:

```bash
sudo apt update
sudo apt install -y libsaxonhe-java jing
```

Sur macOS, les commandes `saxon` et `jing` sont directement disponibles après installation. Sur Ubuntu (et donc sous WSL), le paquet de Jing installe bien une commande `jing`, mais celui de Saxon dépose un JAR à l’emplacement fixe `/usr/share/java/Saxon-HE.jar`&nbsp;: il faut donc fabriquer un petit lanceur. Une installation de Saxon déjà présente sur la machine peut répondre à la place du lanceur et vous induire en erreur&nbsp;: veillez à ce que ce soit bien votre lanceur qui réponde.

> Les deux lanceurs iront dans `~/.local/bin`, le répertoire réservé aux exécutables de l’utilisateur. Créez-le s’il n’existe pas, avec `mkdir -p ~/.local/bin`. S’il ne figure pas déjà dans votre `PATH`, ajoutez-le avec `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc`, puis `source ~/.bashrc`. Sous macOS, où `zsh` est le shell par défaut depuis 2019, remplacez `~/.bashrc` par `~/.zshrc`. Si un Saxon préexistant se cachait sur votre machine, vérifiez que votre lanceur vient en tête&nbsp;: `command -v saxon` doit afficher `~/.local/bin/saxon`.

Créez un fichier `~/.local/bin/saxon` contenant ces deux lignes&nbsp;:

```bash
#!/bin/sh
exec java -jar /usr/share/java/Saxon-HE.jar "$@"
```

Rendez-le ensuite exécutable&nbsp;:

```bash
chmod +x ~/.local/bin/saxon
```

Pour `jing`, vérifiez qu’il est accessible (la commande affiche sa version et son usage, puis se termine avec un code d’erreur, ce qui est normal)&nbsp;:

```bash
jing
```

Si cette commande n’est pas trouvée, localisez le fichier `jing.jar` livré par le paquet avec `ls /usr/share/java/ | grep -i jing`, puis créez `~/.local/bin/jing` sur le même modèle, en adaptant le chemin au résultat obtenu&nbsp;:

```bash
#!/bin/sh
exec java -jar /usr/share/java/jing.jar "$@"
```

```bash
chmod +x ~/.local/bin/jing
```

Vérifiez enfin que les deux commandes répondent&nbsp;:

```bash
saxon
jing
```

Chacune doit afficher un message d’usage. Une réponse `command not found` signale que `~/.local/bin` ne figure pas dans votre `PATH`.

Ces deux programmes s’exécutent sur une machine virtuelle Java. Il faut donc installer un JRE avant de les utiliser. Nous recommandons OpenJDK 17 (LTS) ou plus récent&nbsp;: sous Linux, installez‑le avec `sudo apt install openjdk-17-jre`&nbsp;; sous **macOS** (Homebrew), utilisez `brew install openjdk`. Vérifiez ensuite l’installation avec `java -version`. Si la commande n’est pas trouvée, relancez votre terminal ou ajoutez le chemin d’OpenJDK à votre `PATH`.

Si vous ne disposez pas de droits d’administration, ou si vous préférez garder les outils auprès de votre projet, créez un répertoire `~/tools` et téléchargez-y les fichiers [JAR](https://fr.wikipedia.org/wiki/JAR_(format_de_fichier)) (*Java ARchive*) depuis [Saxonica](https://github.com/Saxonica/Saxon-HE/releases) et [Jing-Trang](https://github.com/relaxng/jing-trang/releases). Décompressez l’archive de Saxon **en entier** dans `~/tools`&nbsp;: Saxon exige que ses dépendances (répertoire `lib/`) restent à côté de son JAR, faute de quoi il refusera de démarrer. Aucune de ces étapes ne réclame de privilèges. Si `java -version` ne répond pas et que vous ne pouvez pas installer de paquet, décompressez dans votre répertoire personnel une archive de [Temurin](https://perma.cc/T6SQ-XYZE), puis ajoutez son sous-répertoire `bin` à votre `PATH`.

Créez ensuite les deux mêmes lanceurs, en pointant celui de Jing sur le JAR décompressé (par exemple `$HOME/tools/jing-20220510/bin/jing.jar`) et celui de Saxon sur le sien (par exemple `$HOME/tools/saxon-he-12.10.jar`).

Après cette configuration, `saxon` et `jing` s’utilisent de la même manière sous macOS et sous Ubuntu, donc aussi sous WSL. Toutes les commandes qui suivent sont identiques dans les deux environnements.

Vous pouvez aussi télécharger localement les feuilles de style TEI, ODD, et Schematron, ce qui vous permet de travailler sans vous soucier de votre connexion internet&nbsp;: 

```bash
mkdir -p templates common
cd templates

TEI=https://www.tei-c.org/release/xml/tei/stylesheet
SCH=https://raw.githubusercontent.com/Schematron/stf/master/iso-schematron-xslt2

# TEI ODD + dépendances nécessaires
for f in odd2odd odd2relax odd2html teiodds classatts RngToRnc; do
  curl -O "$TEI/odds/$f.xsl"
done

# Schematron
for f in iso_svrl_for_xslt2 iso_dsdl_include iso_abstract_expand \
         iso_schematron_skeleton_for_saxon; do
  curl -O "$SCH/$f.xsl"
done

# Dépendances communes TEI (référencées par odd2relax/teiodds)
for f in functions i18n common_param; do
  curl -o "../common/$f.xsl" "$TEI/common/$f.xsl"
done

cd ..

# Messages de la feuille odd2odd, résolus depuis la racine du projet
curl -O "$TEI/i18n.xml"
```

## Qu’est‑ce que la TEI&nbsp;?

La Text Encoding Initiative (TEI) constitue le standard international pour l’encodage de textes en humanités numériques. Née au milieu des années 1980 avec l’objectif d’un balisage commun en SGML ([*Standard Generalized Markup Language*](https://perma.cc/2HML-65WE)), la TEI évolue à partir des années 2000 et adopte le format XML, plus léger et accessible. Cette réforme en a grandement facilité l’adoption.

Aujourd’hui, la TEI propose un langage de balisage riche et modulaire pour décrire la structure et le contenu de documents de toute nature, des manuscrits médiévaux aux correspondances, pièces de théâtre, poèmes, inscriptions épigraphiques, corpus linguistiques, entretiens oraux ou documents multimédias. Le consortium TEI, qui réunit institutions et spécialistes du monde entier, maintient et développe continument ce standard pour répondre aux besoins de la recherche et de la conservation.

Contrairement à un traitement de texte centré sur l’apparence visuelle, la TEI se concentre sur la structuration et la sémantique du texte. Autrement dit, là où Word applique l’italique, la TEI distingue si cette italique signale le titre d’une œuvre `<title>`, un terme en langue étrangère `<foreign>` ou une emphase `<emph>`. Cette structuration sémantique permet à la machine de comprendre le texte et ses composantes.

Un avantage fondamental de la TEI est sa transparence et son interopérabilité. Les balises TEI s’insèrent directement dans le texte, sans nécessiter de logiciel propriétaire. N’importe quel éditeur de texte convient&nbsp;: Notepad, Vim, VS Code, voire même la commande `echo` dans un terminal.

L’adoption de la TEI garantit deux avantages cruciaux&nbsp;: la pérennité et la portabilité. La pérennité assure que le travail restera accessible et exploitable, indépendamment des évolutions techniques. Contrairement aux formats propriétaires, le format TEI-XML est un standard très répandu, lisible par l’homme comme par la machine, qu’elle soit récente ou qu’elle ait trente ans d’âge. La portabilité de la TEI découle de sa structuration sémantique&nbsp;: la machine comprend la structure du texte, ce qui permet des transformations automatiques vers d’autres formats, y compris ceux qui n’existent pas encore.

Pour la correspondance de Filippo Cavriana, la TEI permet d’encoder non seulement le texte des lettres, mais aussi leurs métadonnées (expéditeur, destinataire, date, lieu, etc.), leurs particularités matérielles (ratures, ajouts marginaux, etc.) et leurs références (personnes mentionnées, lieux évoqués, etc.). Chaque phénomène textuel reçoit un balisage spécifique qui en facilite le traitement automatique ainsi que l’analyse statistique.

Tout fichier TEI commence par des éléments récurrents. Concrètement, l’en‑tête d’un fichier XML déclare la version et l’encodage des caractères&nbsp;: `<?xml version="1.0" encoding="UTF-8"?>`. La racine `<TEI>` déclare l’espace de noms par défaut de la TEI&nbsp;: `xmlns="http://www.tei-c.org/ns/1.0"`. Ces deux lignes, qui établissent le cadre syntaxique et le vocabulaire TEI à employer, varient rarement.

Les lignes directrices de la TEI précisent que tous les documents se divisent en deux parties&nbsp;: l’en‑tête (`<teiHeader>`) et le corps (`<text>`). Le minimum requis par TEI P5 pour un en‑tête valide est un élément `<fileDesc>` comportant au moins un `<titleStmt>` avec un `<title>`, un `<publicationStmt>` qui décrit le mode de diffusion (même de manière succincte, par exemple dans un paragraphe `<p>`), et un `<sourceDesc>` qui décrit la ou les sources. Des sections complémentaires comme `<encodingDesc>`, `<profileDesc>` ou `<revisionDesc>` sont vivement recommandées, sans être obligatoires.

Voici un extrait d’une lettre de Filippo Cavriana encodée en TEI, tirée du corpus. Enregistrez-le sous `letters/1568-07-03.xml`&nbsp;:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
 <teiHeader>
  <fileDesc>
   <titleStmt>
    <title>Update on Nevers' condition - 3 July 1568</title>
    <author>Filippo Cavriana</author>
   </titleStmt>
   <publicationStmt>
    <p>Exemple minimal</p>
   </publicationStmt>
   <sourceDesc>
    <msDesc>
     <msIdentifier>
      <settlement>Mantua</settlement>
      <repository>Archivio di Stato di Mantova</repository>
      <collection>Archivio Gonzaga</collection>
      <idno>b654, fols. 924r-924v</idno>
     </msIdentifier>
    </msDesc>
   </sourceDesc>
  </fileDesc>
  <profileDesc>
   <correspDesc>
    <correspAction type="sent">
     <persName ref="#pers-cavriana-f">Filippo Cavriana</persName>
     <placeName ref="#place-nevers">Nevers</placeName>
     <date when="1568-07-03"/>
    </correspAction>
    <correspAction type="received">
     <persName ref="#pers-gonzaga-g">Guglielmo Gonzaga</persName>
     <placeName ref="#place-mantova">Mantova</placeName>
    </correspAction>
   </correspDesc>
  </profileDesc>
 </teiHeader>
 <text>
  <body>
   <div type="letter">
    <pb n="924r"/>
    <opener>
     <salute><choice><abbr>Ill.mo</abbr><expan>Illustrissimo</expan></choice> et <choice><abbr>Ecc.mo</abbr><expan>Eccellentissimo</expan></choice> 
     <choice><abbr>S.or</abbr><expan>Signor</expan></choice> mio <choice><abbr>oss.mo</abbr><expan>osservandissimo</expan></choice></salute>
    </opener>
    <p>Il <persName ref="#pers-gonzaga-l-nev">Duca</persName> mio padrone è così ben disposto della<lb/> 
    persona (Dio mercè) che non si potria desiderar<lb/> 
    meglio rispetto al tempi dove siamo, et alla in<lb break="no"/>fermità grave, che ha patito...</p>
    <closer>
     <dateline>Di <placeName ref="#place-nevers">Nevers</placeName>, il <date when="1568-07-03">3 di luglio 1568</date></dateline>
     <salute>Di <choice><abbr>V.E.</abbr><expan>Vostra Eccellenza</expan></choice></salute>
     <signed><choice><abbr>Humiliss.o</abbr><expan>Humilissimo</expan></choice> et <choice><abbr>devotiss.o</abbr><expan>devotissimo</expan></choice> servitore<lb/> 
     <persName ref="#pers-cavriana-f">Filippo Cavriana</persName></signed>
    </closer>
   </div>
  </body>
 </text>
</TEI>
```

Dans cet exemple, le `<teiHeader>` contient des métadonnées telles que l’identification du manuscrit conservé à Mantoue et la description de la correspondance (expéditeur, destinataire, lieu, date). Le corps du texte utilise plusieurs éléments structurels&nbsp;: `<opener>` et `<closer>` décrivent les formules d’ouverture et de clôture de la lettre, tandis que `<p>` signale les paragraphes. Comme la plupart des balises XML, ces éléments comportent une balise ouvrante et une balise fermante (ex&nbsp;: `<opener>...</opener>`). Certaines, toutefois, comme `<lb/>`, sont dites &laquo;&nbsp;vides&nbsp;&raquo;&nbsp;: elles ne contiennent aucun contenu textuel ni sous-élément, et se ferment donc immédiatement.

Les balises `<lb/>` signalent des sauts de ligne diplomatiques. Lorsqu’un saut de ligne coupe un mot en deux, l’attribut `break="no"` nous permet de préciser qu’il s’agit d’une contrainte de mise en forme et non d’une coupure du contenu. Cela est utile lors de la phase de transformation, car la machine saura alors quand recomposer le mot sans espace ni saut de ligne, se libérant si besoin de la mise en page originale.

Pour ce projet particulier, le choix éditorial est d’offrir au lecteur la forme développée des abréviations pour améliorer la lisibilité du texte. L’encodage TEI permet d’enregistrer simultanément les deux formes grâce à l’élément `<choice>` qui regroupe `<abbr>` (l’abréviation telle qu’elle apparaît dans le manuscrit original) et `<expan>` (sa forme développée). Cette double représentation présente un avantage majeur&nbsp;: elle maintient la fidélité à la source tout en offrant une flexibilité éditoriale. Lors de la transformation pour publication, on peut choisir d’afficher uniquement la version étendue pour faciliter la lecture, tout en préservant dans le fichier TEI une transcription diplomatique fidèle du texte original. Cette approche garantit que l’information paléographique reste accessible pour les chercheurs et chercheuses qui souhaiteraient étudier les pratiques d’écriture et d’abréviation du scriptorat, sans pour autant imposer cette complexité au lectorat général.

Le code TEI comprend aussi les éléments sémantiques `<persName>` et `<placeName>`, qui décrivent des entités nommées. Ils portent des attributs `@ref` renvoyant à un index de personnes et de lieux. Dans un corpus de correspondance, il est recommandé de centraliser ces informations dans des fichiers d’autorité séparés pour garantir la cohérence de l’ensemble. Selon les besoins du projet, elles peuvent aussi être intégrées dans l’en-tête du document.

En voici un exemple&nbsp;:

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
 <teiHeader>
  <fileDesc>
   <titleStmt><title>Entités Personnes</title></titleStmt>
   <publicationStmt><p>exemple minimal</p></publicationStmt>
   <sourceDesc><p>...</p></sourceDesc>
  </fileDesc>
  <profileDesc>
   <particDesc>
    <listPerson>
     <person xml:id="pers-cavriana-f">
      <persName>Filippo Cavriana</persName>
      <persName type="alias" xml:lang="it">Vincenzo da Castello</persName>
      <persName type="alias" xml:lang="it">Chi ella sà</persName>
      <sex value="1">male</sex>
      <occupation xml:lang="fr">Médecin et diplomate</occupation>
     </person>
     <person xml:id="pers-gonzaga-g">
      <persName>Guglielmo Gonzaga</persName>
      <sex value="1">male</sex>
      <roleName type="title" xml:lang="fr">Duc de Mantoue</roleName>
      <idno type="VIAF">51953916</idno>
      <birth when="1538-04-24"/>
      <death when="1587-08-14"/>
     </person>
    </listPerson>
   </particDesc>
  </profileDesc>
 </teiHeader>
 <text>
  <body/>
 </text>
</TEI>
```

La TEI étant très flexible, nous pouvons nourrir chaque entrée d’informations supplémentaires. On peut, par exemple, complémenter une entité de lieu avec des coordonnées géographiques ou des liens à des bases de données telles que le TGN ([*Getty Thesaurus of Geographic Names*](https://perma.cc/C2VV-ZWQL)). Dans l’exemple ci-dessus, nous avons choisi de référencer les personnages au VIAF ([*Virtual International Authority File*](https://perma.cc/4GT6-QWAR)) lorsque cela est possible. Ces informations peuvent être utiles, notamment pour faciliter l’interopérabilité entre différents projets numériques, permettre des recherches plus précises et enrichir l’analyse des données textuelles. Elles offrent également la possibilité d’enrichir la publication de ce texte avec des informations contextuelles supplémentaires.

Cet aperçu de la TEI est minimal. Pour découvrir les centaines d’éléments et attributs propres à cette convention, on se reportera à la documentation officielle, [*TEI&nbsp;: Recommandations pour l’encodage et l’échange de textes électroniques*](https://perma.cc/WRF8-ZEFJ), et au leçon de Nicolás Vaughan dans le _Programming Historian en français_&nbsp;: [_Introduction à l’encodage de texte TEI_](/fr/lecons/introduction-a-tei-1).

## Prévention des erreurs, conformité syntaxique et validité

Le XML est strict et ne pardonne pas&nbsp;: un guillemet manquant, un caractère mal placé ou un espace de trop peut rendre le document illisible par la machine. Pour limiter les problèmes, il faut d’abord encoder les fichiers en Unicode ([UTF-8](https://perma.cc/2DM5-GH7X)), un standard universel qui attribue une représentation numérique à chaque caractère. L’étape suivante consiste à normaliser ces caractères, afin d’assurer leur cohérence interne&nbsp;: en Unicode, un même signe accentué peut être représenté de plusieurs manières: sous une forme précomposée (par exemple&nbsp;: &laquo;&nbsp;é&nbsp;&raquo; = U+00E9) ou décomposée (U+0065 + U+0301, soit la lettre &laquo;&nbsp;e&nbsp;&raquo; suivie d’un accent combinant). Visuellement identiques, ces deux formes diffèrent sur le plan binaire. La normalisation NFC ([*Normalization Form C*](https://perma.cc/YRL6-QGBD)) privilégie la forme précomposée lorsqu’elle existe, garantissant la stabilité des recherches, des comparaisons et des transformations XSLT. Dans ce contexte, la normalisation désigne donc un traitement technique des caractères, à ne pas confondre avec la normalisation éditoriale qui consiste à développer ou régulariser des formes linguistiques pour la lisibilité. Comme le rappelle Chahan Vidal-Gorène dans sa leçon [_La reconnaissance automatique d'écriture à l'épreuve des langues peu dotées_](/fr/lecons/transcription-automatisee-graphies-non-latines), le choix d’une forme de normalisation Unicode (NFC, NFD, etc.) influe directement sur la reconnaissance automatique de l’écriture et sur la cohérence des corpus multilingues.

Certaines applications peuvent normaliser le texte en Unicode NFC pour vous. Dans Linux (et donc Ubuntu/WSL)&nbsp;:

```bash
sudo apt install -y icu-devtools
uconv -x any-nfc -o letters/1568-07-03-nfc.xml letters/1568-07-03.xml
```

Dans macOS&nbsp;:
```bash
brew install icu4c
$(brew --prefix icu4c)/bin/uconv -x any-nfc \
  -o letters/1568-07-03-nfc.xml letters/1568-07-03.xml
```

Sous Windows sans WSL (Git Bash), PowerShell fait de même&nbsp;:
```bash
powershell -Command '$t = Get-Content -Raw -Encoding UTF8 letters/1568-07-03.xml
  [IO.File]::WriteAllText("letters/1568-07-03-nfc.xml",
  $t.Normalize([Text.NormalizationForm]::FormC),
  (New-Object Text.UTF8Encoding $false))'
```

En XML (et donc en TEI), on distingue deux niveaux de conformité. Un document &laquo;&nbsp;bien formé&nbsp;&raquo; respecte les règles syntaxiques de base&nbsp;: les balises sont correctement imbriquées, les attributs sont entre guillemets, etc. Par exemple, `<p>Ceci est un paragraphe</p>` est &laquo;&nbsp;bien formé&nbsp;&raquo;, alors que `<p>Ceci est un paragraphe<p>` ne l’est pas. Un document &laquo;&nbsp;valide&nbsp;&raquo; va plus loin&nbsp;: non seulement il est &laquo;&nbsp;bien formé&nbsp;&raquo;, mais il respecte un schéma qui définit quels éléments sont autorisés, dans quel ordre, avec quels attributs et quelles contraintes. En TEI, un fichier peut être &laquo;&nbsp;bien formé&nbsp;&raquo; mais &laquo;&nbsp;pas valide&nbsp;&raquo; s’il emploie un élément qui n’existe pas dans la TEI (par exemple `<paragraph>`), s’il place un élément à un endroit non autorisé (par exemple une `<note>` directement sous `<teiHeader>`) ou s’il omet un attribut exigé par le schéma que nous avons défini au préalable (par exemple un `@ref` obligatoire sur `<persName>`).

Valider régulièrement le code garantit la cohérence des choix éditoriaux. Par exemple, imposer `@place="margin"` sur `<add>` (où @place indique l’emplacement matériel de l’ajout et margin signifie &laquo;&nbsp;écrit en marge, hors de la ligne&nbsp;&raquo;) aligne toutes les contributions sur la même convention, ce qui facilite la collaboration, l’interopérabilité avec d’autres corpus et la fiabilité des transformations XSLT.

## Créer un schéma de validation

Pour qu’un projet d’édition soit solide et cohérent, il est essentiel de définir un schéma de validation. Ce document énumère les éléments et attributs autorisés, décrit leur structure et précise les valeurs acceptées. Il agit comme une grammaire à respecter durant les phases d’édition et d’encodage&nbsp;: chaque fichier TEI est comparé à ce schéma pour que toute non-conformité soit signalée. Un tel mécanisme garantit que tous les textes encodés du projet respectent les mêmes conventions. Il prévient l’introduction d’éléments ou d’attributs imprévus, réduisant les incohérences d’encodage. En d’autres termes, le schéma de validation encadre la liberté laissée aux encodeurs&nbsp;: il impose une rigueur technique tout en formalisant les choix éditoriaux du projet.

Trois familles de schémas coexistent. La [DTD](https://perma.cc/B6W9-YD3M) (Document Type Definition), héritée du SGML, reste supportée mais n’est pratiquement plus utilisée. [XML Schema (XSD)](https://perma.cc/D5S6-QDGU) permet un typage fin et une validation détaillée, au prix d’une complexité importante. Cependant, la TEI préconise RELAX NG ([*REgular LAnguage for XML, Next Generation*](https://perma.cc/JF83-W7T3)), car sa flexibilité et sa concision en font le meilleur choix pour la plupart des éditions. C’est le format que nous utiliserons ici.

Un schéma RELAX NG pour la TEI définit précisément quels modules sont utilisés et comment ils sont personnalisés. Pour une correspondance comme celle de Cavriana, par exemple, on inclura les modules essentiels (`tei`, `core`, `header`, `textstructure`, `namesdates`, `transcr`, et `msdescription`) et l’on précisera des contraintes adaptées au projet. Ainsi, nous ne voulons pas de `<persName>` et `<placeName>` sans attribut `@ref`, car nous voulons nous assurer que ces éléments renvoient les entités nommées à leurs fiches correspondantes. De même, les balises `<correspAction>` seront toujours accompagnées d’un élément `<date>` portant l’attribut `@when`, de sorte que la machine puisse lire la date dans tous les documents du projet. Toujours dans `<correspAction>`, nous éviterons toute ambiguïté en restreignant l’attribut `@type` aux seules valeurs `sent` ou `received`. Pour chaque changement de page `<pb>`, l’attribut `@n` sera requis afin d’assurer la numérotation. Nous pouvons aussi limiter l’élément `<choice>` à la paire `<abbr>`/`<expan>` et préciser dans la documentation d’encodage qu’un `<msIdentifier>` complet (`settlement`, `repository`, `collection`, `idno`) est attendu dans `<msDesc>`. Un tel resserrement aligne le schéma sur notre pratique d’encodage et fiabilise les recherches ou transformations XSLT ultérieures.

Dans l’écosystème TEI, la manière la plus robuste de définir ce schéma consiste à écrire un ODD ([*One Document Does it all*](https://perma.cc/JT6L-87S8)), puis à en dériver automatiquement un schéma RELAX NG pour la validation et une documentation lisible pour les personnes en charge de l’encodage. L’ODD joue ainsi à la fois le rôle de manuel d’encodage et de spécification technique. Autrement dit, il ne s’agit pas seulement d’un document de référence destiné aux éditeurs, mais du point central à partir duquel la validation peut être automatisée. Le ODD étant codé en XML, on peut l’écrire à l’aide de n’importe quel éditeur. Cependant, on peut préférer utiliser l’application web gratuite [Roma](https://roma.tei-c.org), qui offre une interface visuelle plus intuitive. Pour une réflexion approfondie sur la notion de conformité TEI et le rôle central de l’ODD dans sa formalisation, on se reportera avec profit à l’article de Lou Burnard, &laquo;&nbsp;[What Is TEI Conformance, and Why Should You Care?](https://doi.org/10.4000/jtei.1777)&nbsp;&raquo;, *Journal of the Text Encoding Initiative*, 12 (2019).

L’extrait ci-dessous illustre les personnalisations essentielles de notre ODD&nbsp;: enregistré tel quel sous `templates/cavriana.odd`, il fonctionne directement, la chaîne de transformation allant chercher en ligne les sources TEI qui le complètent. Vous pouvez aussi le composer dans [Roma](https://roma.tei-c.org), l’interface visuelle du consortium, puis l’exporter au même endroit&nbsp;: la suite de la leçon ne change pas.

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0"
     xmlns:sch="http://purl.oclc.org/dsdl/schematron">
 <teiHeader>
  <fileDesc>
   <titleStmt><title>ODD Cavriana — Extrait pédagogique</title></titleStmt>
   <publicationStmt><p>Document de Travail</p></publicationStmt>
   <sourceDesc><p>Correspondance (XVIe siècle)</p></sourceDesc>
  </fileDesc>
 </teiHeader>

 <text>
  <body>
    <!-- =========================
      1) Modules TEI requis
      ========================= -->
  <schemaSpec ident="cavriana" start="TEI">
   <!-- Noyau et structures -->
   <moduleRef key="tei"/>
   <moduleRef key="core"/>
   <moduleRef key="header"/>
   <moduleRef key="textstructure"/>
   <!-- Noms et dates, transcription, description des manuscrits -->
   <moduleRef key="namesdates"/>
   <moduleRef key="transcr"/>
   <moduleRef key="msdescription"/>
   <!-- Dépendances requises par le module transcr -->
   <moduleRef key="analysis"/>
   <moduleRef key="linking"/>

   <!-- ==========================
      1) Resserrement RELAX NG
      ========================== -->
   
   <!-- '@ref' obligatoire sur les entités nommées -->
   <elementSpec ident="persName" mode="change">
    <attList><attDef ident="ref" mode="change" usage="req"/></attList>
   </elementSpec>
   <elementSpec ident="placeName" mode="change">
    <attList><attDef ident="ref" mode="change" usage="req"/></attList>
   </elementSpec>
   
   <!-- '@type' fermé sur 'correspAction' -->
   <elementSpec ident="correspAction" mode="change">
    <attList>
     <attDef ident="type" mode="change">
      <valList type="closed">
       <valItem ident="sent"/>
       <valItem ident="received"/>
      </valList>
     </attDef>
    </attList>
   </elementSpec>

   <!-- numéro de page requis -->
   <elementSpec ident="pb" mode="change">
    <attList><attDef ident="n" mode="change" usage="req"/></attList>
   </elementSpec>
   
   <!-- choice limité à 'abbr' et 'expan' -->
   <elementSpec ident="choice" mode="change">
    <content>
     <sequence>
      <elementRef key="abbr"/>
      <elementRef key="expan"/>
     </sequence>
    </content>
   </elementSpec>
  </schemaSpec>
 </body></text>
</TEI>
```
Ce premier ODD nous donne un schéma RELAX NG focalisé sur la grammaire du projet. Des vérifications plus &laquo;&nbsp;éditoriales&nbsp;&raquo; seront présentées dans la suite du leçon, lorsque nous aborderons le Schematron. La racine du fichier déclare déjà l’espace de noms Schematron (`xmlns:sch`)&nbsp;: il ne sert à rien pour l’instant, mais il évite une erreur fréquente au moment d’ajouter les règles, le processeur refusant tout préfixe `sch:` qui n’a pas été lié. Notez enfin l’attribut `mode="change"` porté par chaque `<attDef>`&nbsp;: il modifie l’attribut hérité de la TEI au lieu d’en ajouter un doublon, sous peine d’échec à la validation.

Une fois l’ODD défini, nous pouvons le transformer en RELAX NG pour qu’il soit utilisable par des outils de validation. Pour cela, on applique une feuille de transformation XSLT au fichier ODD, soit via l’interface Roma, soit en ligne de commande. 

L’exemple suivant montre comment effectuer cette conversion avec Saxon-HE (Home Edition), un processeur XSLT gratuit et open source développé par Saxonica. La conversion se fait en deux temps&nbsp;: la feuille `odd2odd.xsl` fusionne d’abord votre ODD avec les sources officielles de la TEI, téléchargées en ligne, puis `odd2relax.xsl` dérive le schéma RELAX NG de ce fichier fusionné. À la racine du projet, on exécute&nbsp;: 

```bash
saxon -s:templates/cavriana.odd -xsl:templates/odd2odd.xsl \
  -o:templates/cavriana-compile.odd
saxon -s:templates/cavriana-compile.odd -xsl:templates/odd2relax.xsl \
  -o:templates/schema-cavriana.rng \
  schemaBaseURL=https://www.tei-c.org/release/xml/tei/schema/relaxng/
```

Ici, `saxon` lance Saxon-HE, `-s` indique le fichier source, `-xsl` précise la feuille XSLT à appliquer et `-o` définit le fichier produit&nbsp;: d’abord `cavriana-compile.odd`, l’ODD fusionné, puis `schema-cavriana.rng`, le schéma de validation. Le paramètre `schemaBaseURL` complète `-xsl`&nbsp;: il indique à la feuille l’adresse des fragments RELAX NG officiels de la TEI, que le schéma généré référence lorsqu’il n’en redéfinit pas le contenu lui-même. Sans lui, ces références pointent vers une adresse locale fictive (`http://localhost/schema/relaxng/`) que le validateur ne peut pas résoudre. Sauter la première étape produirait un schéma en apparence valide mais vidé de votre personnalisation, et la seconde transformation ne pourrait pas vous en avertir. Ces transformations sont à effectuer lors de la mise en place initiale du projet puis à chaque modification de l’ODD, pour que le schéma de validation reflète toujours les règles éditoriales les plus récentes.


### Valider les documents localement

Dès lors que nous disposons de notre schéma de validation, nous pouvons vérifier les fichiers TEI localement avec un validateur RELAX NG comme Jing. Cette étape permet de détecter toute erreur de syntaxe introduite lors de l’encodage, avant tout envoi vers le dépôt ou tout déclenchement d’une chaîne d’intégration continue. La validation locale joue ainsi le rôle de premier garde-fou&nbsp;: elle garantit que les fichiers respectent les contraintes définies dans l’ODD, compilées en schéma RELAX NG. Des garde-fous, il en faut beaucoup, car l’expérience montre que de nombreuses coquilles peuvent s’introduire subrepticement à chaque étape de manipulation.

Pour valider un fichier unique à partir du schéma RELAX NG généré précédemment, il suffit de lancer cette commande&nbsp;:

```bash
jing templates/schema-cavriana.rng letters/1568-07-03.xml
```

Si le document est conforme au schéma, Jing ne produit aucune sortie. En cas d’erreur, il affiche un message de la forme&nbsp;:

```
fichier:ligne:colonne: error: description de l’erreur
```

Par exemple&nbsp;:

```
letters/1574-10-15.xml:45:12: error: element "persName" not closed
letters/1574-10-15.xml:32:8: error: attribute "type" not allowed here
```

Ces messages lapidaires intimident souvent les débutant&middot;es. Parfois cryptiques, ils ne signifient pourtant pas l’échec. Ils indiquent au contraire l’origine du problème et ouvrent des pistes de correction. À l’instar du mot d’ordre &laquo;&nbsp;lis tes ratures&nbsp;&raquo;, l’encodeur&middot;euse doit apprendre à lire ses erreurs.

Pour valider un ensemble de fichiers sous macOS ou Linux, on utilisera&nbsp;:

```bash
jing templates/schema-cavriana.rng letters/*.xml
```

Ce motif inclura le fichier normalisé créé plus haut, qui n’est pas une lettre du corpus&nbsp;; déplacez-le ou ajustez le motif pour l’en écarter.

Dans un flux de travail efficace, la validation locale est effectuée après chaque session d’encodage et avant tout envoi au dépôt, en complément des validations automatisées exécutées par la chaîne CI/CD que nous verrons dans la seconde partie de cette leçon.

Si la validation manuelle devient fastidieuse à mesure que le corpus s’étoffe, on peut automatiser cette étape à l’aide d’un script. Celui-ci parcourt les fichiers d’un répertoire, exécute la validation pour chacun, affiche un résumé clair des résultats et renvoie un code de sortie en cas d’erreurs. Ouvrez un fichier `valider.sh` à la racine du projet et copiez-y les lignes suivantes&nbsp;:

```bash
#!/bin/bash
SCHEMA="templates/schema-cavriana.rng"
LETTERS="letters/*.xml"
ERRORS=0

echo "Validation du corpus..."
for file in $LETTERS; do
 [ -f "$file" ] || continue
 if jing "$SCHEMA" "$file" 2>/dev/null; then
  echo "OK $(basename "$file")"
 else
  echo "ERR $(basename "$file")"
  jing "$SCHEMA" "$file"
  ERRORS=$((ERRORS+1))
 fi
done
exit $ERRORS
```

Lancez-le ensuite avec `bash valider.sh`, ce qui évite d’avoir à rendre le fichier exécutable. Le script appelle `jing` comme vous le feriez dans le terminal&nbsp;: c’est précisément l’intérêt d’un lanceur placé dans le `PATH` plutôt que d’un alias, ce dernier n’étant pas reconnu par les scripts.

Cette validation peut s’intégrer directement dans les environnements de développement modernes (Visual Studio Code, Sublime Text, Vim) pour un retour immédiat à chaque sauvegarde.

La validation RELAX NG vérifie que le document respecte à la fois la syntaxe XML et les contraintes structurelles définies dans l’ODD&nbsp;: types de données, règles de présence et de répétition des éléments et attributs. Mais certaines règles échappent à ce cadre purement déclaratif, comme les contraintes conditionnelles, les vérifications croisées entre parties du document, toute cette logique éditoriale qui dépasse la simple grammaire du schéma. C’est là qu’intervient Schematron, avec des assertions précises capables de capturer ces cas particuliers.

### Validation éditoriale avec Schematron

Comme vu précédemment, RELAX NG valide la forme. Pour exprimer des contraintes de logique éditoriale plus complexes, on ajoute Schematron. Par souci de clarté pédagogique, nous commençons ici par un schéma Schematron séparé (`.sch`). En production, ces règles sont souvent intégrées directement dans l’ODD, afin de conserver une source de vérité unique. 

Il est important de comprendre comment Schematron fonctionne. Contrairement à RELAX NG, qui est interprété directement par un validateur dédié comme Jing, Schematron passe par une étape intermédiaire&nbsp;: les règles `.sch` sont d’abord *compilées* en une feuille XSLT par Saxon, puis cette feuille compilée est *appliquée* au document TEI, toujours par Saxon, pour produire un rapport de validation (SVRL). Autrement dit, Saxon et le langage XSLT servent ici d’outil de *validation*, alors que nous les utiliserons plus loin comme outil de *transformation* (TEI vers HTML, Markdown, etc.). Cette apparente double fonction s’explique par la polyvalence d’XSLT, qui permet aussi bien de vérifier des contraintes que de générer des formats de sortie.

Par exemple, dans une correspondance, on peut exiger la présence conjointe d’une action d’envoi et d’une action de réception, et imposer qu’au moins une date lisible par machine accompagne l’action `sent`. Enregistrez ce schéma sous `templates/cavriana.sch`&nbsp;:

```xml
<schema xmlns="http://purl.oclc.org/dsdl/schematron"
    xmlns:tei="http://www.tei-c.org/ns/1.0">
 <ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>
 
 <!-- Règle 1 : correspDesc doit contenir sent + received + date machine‑lisible -->
 <pattern id="correspondance">
  <rule context="tei:teiHeader/tei:profileDesc/tei:correspDesc">
   <assert test="tei:correspAction[@type='sent'] and tei:correspAction[@type='received']">
    correspDesc doit contenir correspAction[@type='sent'] et correspAction[@type='received'].
   </assert>
   <assert test="tei:correspAction[@type='sent']/tei:date[@when or @from or @to or @notBefore or @notAfter]">
    L’action 'sent' doit comporter une date lisible par machine (@when|@from|@to|@notBefore|@notAfter).
   </assert>
  </rule>
 </pattern>

 <!-- Règle 2 : le premier div du corps doit être typé 'letter' -->
 <pattern id="structure-lettre">
  <rule context="tei:text/tei:body/tei:div[1]">
   <assert test="@type='letter'">
    Le premier &lt;div&gt; du corps doit avoir @type='letter'.
   </assert>
  </rule>
 </pattern>
 
 <!-- Règle 3 : msIdentifier doit être complet (settlement, repository, collection, idno) -->
 <pattern id="ms-identifier">
  <rule context="tei:msDesc/tei:msIdentifier">
   <assert test="tei:settlement and tei:repository and tei:collection and tei:idno">
    msIdentifier doit contenir settlement, repository, collection et idno.
   </assert>
  </rule>
 </pattern>

</schema>
```

On compile ensuite le schéma en XSLT en trois étapes successives&nbsp;: inclusion des modules externes, expansion des motifs abstraits, puis génération de la feuille XSLT de validation&nbsp;:

```bash
# Étape 1 : résoudre les inclusions
saxon -s:templates/cavriana.sch -xsl:templates/iso_dsdl_include.xsl \
  -o:templates/cavriana-step1.sch

# Étape 2 : expanser les motifs abstraits
saxon -s:templates/cavriana-step1.sch -xsl:templates/iso_abstract_expand.xsl \
  -o:templates/cavriana-step2.sch

# Étape 3 : générer la feuille XSLT de validation
saxon -s:templates/cavriana-step2.sch -xsl:templates/iso_svrl_for_xslt2.xsl \
  -o:templates/cavriana-schematron.xsl
```

Puis on l’applique aux documents&nbsp;:

```bash
saxon -s:letters/1568-07-03.xml -xsl:templates/cavriana-schematron.xsl \
  -o:output/rapport-schematron.svrl
```

Le rapport SVRL (*Schematron Validation Report Language*) consigne les règles déclenchées (`<svrl:active-pattern>`, `<svrl:fired-rule>`), puis, pour chacune, les assertions échouées (`<svrl:failed-assert>`). Notre lettre respecte les trois règles&nbsp;: son rapport ne contient aucun `failed-assert` et ce silence est le signe que tout va bien. Voici la sortie réelle, allégée des espaces de noms et du chemin absolu de l’attribut `document`, propre à votre machine&nbsp;:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<svrl:schematron-output xmlns:svrl="http://purl.oclc.org/dsdl/svrl" ...>
 <!-- Règle 1 : correspDesc -->
 <svrl:active-pattern document="..." id="correspondance"/>
 <svrl:fired-rule context="tei:teiHeader/tei:profileDesc/tei:correspDesc"/>
 <!-- Règle 2 : le premier div -->
 <svrl:active-pattern document="..." id="structure-lettre"/>
 <svrl:fired-rule context="tei:text/tei:body/tei:div[1]"/>
 <!-- Règle 3 : msIdentifier -->
 <svrl:active-pattern document="..." id="ms-identifier"/>
 <svrl:fired-rule context="tei:msDesc/tei:msIdentifier"/>
</svrl:schematron-output>
```

Pour voir un rapport d’échec, introduisez trois fautes dans une copie de la lettre&nbsp;: supprimez l’attribut `@when` de la date d’envoi, changez le `@type` du premier `div`, retirez l’élément `<collection>`. Relancez la même commande&nbsp;: le rapport contient exactement trois `failed-assert`, un par règle&nbsp;:

```xml
<!-- Règle 1 : la date machine-lisible manque -->
<svrl:failed-assert test="tei:correspAction[@type='sent']/tei:date[@when or @from or @to or @notBefore or @notAfter]"
                   location="/*[local-name()='TEI']/*[local-name()='teiHeader']/*[local-name()='profileDesc']/*[local-name()='correspDesc']">
 <svrl:text>
  L’action 'sent' doit comporter une date lisible par machine (@when|@from|@to|@notBefore|@notAfter).
 </svrl:text>
</svrl:failed-assert>
<!-- Règle 2 : le premier div n’est pas typé 'letter' -->
<svrl:failed-assert test="@type='letter'"
                   location="/*[local-name()='TEI']/*[local-name()='text']/*[local-name()='body']/*[local-name()='div']">
 <svrl:text>
  Le premier &lt;div&gt; du corps doit avoir @type='letter'.
 </svrl:text>
</svrl:failed-assert>
<!-- Règle 3 : collection manque dans msIdentifier -->
<svrl:failed-assert test="tei:settlement and tei:repository and tei:collection and tei:idno"
                   location="/*[local-name()='TEI']/*[local-name()='fileDesc']/*[local-name()='sourceDesc']/*[local-name()='msDesc']/*[local-name()='msIdentifier']">
 <svrl:text>
  msIdentifier doit contenir settlement, repository, collection et idno.
 </svrl:text>
</svrl:failed-assert>
```

Chaque `failed-assert` porte le test évalué (`@test`), la localisation du nœud fautif (`@location`, sous la forme `/*[local-name()='TEI']…`, propre au SVRL) et le message défini dans le schéma (`<svrl:text>`). Les règles satisfaites restent silencieuses. Ce contrôle complémentaire est particulièrement utile dans un projet collaboratif&nbsp;: il aide à repérer et corriger immédiatement les incohérences introduites par différentes contributions, avant qu’elles ne s’accumulent dans le corpus.

Les règles Schematron s’écrivent dans le fichier `templates/cavriana.odd`, aux côtés de la grammaire RELAX&nbsp;NG. C’est la raison pour laquelle sa racine déclare deux espaces de noms, celui de la TEI et celui du Schematron&nbsp;: si vous partez d’un ODD exporté depuis Roma, vérifiez que la deuxième déclaration est bien présente, faute de quoi la transformation échouera sur un message du type `The prefix "sch" for element "sch:rule" is not bound`.

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0"
   xmlns:sch="http://purl.oclc.org/dsdl/schematron">
``` 

Puis, à l’intérieur de l’ODD, on ajoute les règles Schematron au moyen de blocs `<constraintSpec>`. Conformément aux recommandations TEI, chaque `<constraintSpec>` est placé à l’intérieur de l’`<elementSpec>` auquel il se rapporte, de sorte que la contrainte reste associée à l’élément qu’elle concerne. Cette organisation par élément garantit la lisibilité de l’ODD et facilite sa maintenance&nbsp;: quand on modifie les règles d’un élément donné, on trouve au même endroit sa grammaire RELAX NG et sa logique Schematron.

Ajoutez les blocs suivants à l’intérieur de l’élément `<schemaSpec>` de `templates/cavriana.odd`, à la suite des `<elementSpec>` déjà définis&nbsp;:

```xml
  <!-- correspDesc : sent + received + date machine-lisible -->
  <elementSpec ident="correspDesc" mode="change">
   <constraintSpec ident="correspDesc-sent-received" scheme="schematron">
    <constraint>
     <sch:rule context="tei:correspDesc">
      <sch:assert test="tei:correspAction[@type='sent'] and tei:correspAction[@type='received']">
       correspDesc doit contenir correspAction[@type='sent'] et correspAction[@type='received'].
      </sch:assert>
      <sch:assert test="tei:correspAction[@type='sent']/tei:date[@when or @from or @to or @notBefore or @notAfter]">
       L’action 'sent' doit comporter une date lisible par machine (@when|@from|@to|@notBefore|@notAfter).
      </sch:assert>
     </sch:rule>
    </constraint>
   </constraintSpec>
  </elementSpec>

  <!-- div : le premier div du body doit être typé 'letter' -->
  <elementSpec ident="div" mode="change">
   <constraintSpec ident="div-type-letter" scheme="schematron">
    <constraint>
     <sch:rule context="tei:text/tei:body/tei:div[1]">
      <sch:assert test="@type='letter'">
       Le premier &lt;div&gt; du corps doit avoir @type='letter'.
      </sch:assert>
     </sch:rule>
    </constraint>
   </constraintSpec>
  </elementSpec>

  <!-- msIdentifier : settlement, repository, collection et idno requis -->
  <elementSpec ident="msIdentifier" mode="change">
   <constraintSpec ident="msIdentifier-complet" scheme="schematron">
    <constraint>
     <sch:rule context="tei:msDesc/tei:msIdentifier">
      <sch:assert test="tei:settlement and tei:repository and tei:collection and tei:idno">
       msIdentifier doit contenir settlement, repository, collection et idno.
      </sch:assert>
     </sch:rule>
    </constraint>
   </constraintSpec>
  </elementSpec>
```

On dérive ensuite deux artefacts à partir de cette source unique&nbsp;: le schéma RELAX&nbsp;NG pour `jing` et le Schematron compilé en XSLT pour produire le rapport SVRL.

Avec la validation terminée et le corpus conforme aux règles définies, on peut passer à une étape essentielle du flux éditorial continu&nbsp;: la transformation XSLT des fichiers TEI vers des formats exploitables aussi bien par les lecteur&middot;rices que par les systèmes de publication (HTML, Markdown, etc.).

### La transformation XSLT

La validation garantit la qualité de l’encodage, mais les fichiers TEI, malgré leur lisibilité pour les expert&middot;es, restent peu accessibles au grand public. Dans une édition continue, chaque document validé doit être immédiatement publiable. C’est ici qu’intervient XSLT (*eXtensible Stylesheet Language Transformations*), le pont entre l’encodage savant et la diffusion publique.

XSLT transforme le XML-TEI vers n’importe quel format de sortie&nbsp;: HTML pour le web, Markdown pour les générateurs de sites statiques comme Docusaurus ou Jekyll, LaTeX pour l’impression, ou même CSV pour l’analyse de données. Cette polyvalence est cruciale pour l’édition continue&nbsp;: une seule source TEI alimente automatiquement plusieurs canaux de publication.

Pour transformer un document, il faut d’abord pouvoir l’interroger. XPath ([*XML Path Language*](https://perma.cc/DMY7-82X2)) est un langage de requête conçu pour extraire des informations précises d’un document XML, comme SQL, qui interroge une base de données relationnelle. En informatique, XPath est omniprésent&nbsp;: les navigateurs web l’utilisent pour manipuler le DOM ([*Document Object Model*](https://perma.cc/8HJH-D4ZB)), les outils de test automatisé pour localiser des éléments d’interface, les systèmes de configuration pour extraire des paramètres. Dans notre contexte d’édition, XPath nous permet de cibler précisément les parties du document TEI à transformer.

Un document XML forme un arbre où chaque élément peut avoir des enfants, des attributs et du contenu textuel. XPath navigue dans cet arbre avec une syntaxe qui rappelle les chemins de fichiers d’un système d’exploitation, mais avec des capacités de recherche bien plus puissantes. Reprenons la lettre de Cavriana du 3 juillet 1568 pour visualiser sa structure&nbsp;:

```text
TEI
├── teiHeader
│  ├── fileDesc
│  │  ├── titleStmt
│  │  │  ├── title: "Update on Nevers' condition..."
│  │  │  └── author: "Filippo Cavriana"
│  │  └── sourceDesc
│  │    └── msDesc
│  │      └── msIdentifier
│  │        ├── settlement: "Mantua"
│  │        ├── repository: "Archivio di Stato..."
│  │        ├── collection: "Archivio Gonzaga"
│  │        └── idno: "b654, fols. 924r-924v"
│  └── profileDesc
│    └── correspDesc
│      ├── correspAction [@type="sent"]
│      │  ├── persName [@ref="#pers-cavriana-f"]: "Filippo Cavriana"
│      │  ├── placeName [@ref="#place-nevers"]: "Nevers"
│      │  └── date [@when="1568-07-03"]
│      └── correspAction [@type="received"]
│        ├── persName [@ref="#pers-gonzaga-g"]: "Guglielmo Gonzaga"
│        └── placeName [@ref="#place-mantova"]: "Mantova"
└── text
  └── body
    └── div [@type="letter"]
      ├── pb [@n="924r"]
      ├── opener
      │  └── salute
      │    └── choice (multiple)...
      ├── p
      │  ├── persName [@ref="#pers-gonzaga-l-nev"]: "Duca"
      │  ├── (texte)
      │  └── lb (multiple)
      └── closer
        ├── dateline
        │  ├── placeName [@ref="#place-nevers"]: "Nevers"
        │  └── date [@when="1568-07-03"]: "3 di luglio 1568"
        ├── salute
        └── signed
          └── persName [@ref="#pers-cavriana-f"]: "Filippo Cavriana"
```

Dans cet arbre, XPath agit comme un langage de requête. La barre oblique `/` représente la racine, la double barre oblique `//` permet de chercher à n’importe quelle profondeur, le point `.` désigne le nœud courant, deux points `..` remontent au parent, l’arobase `@` accède aux attributs, et les crochets `[]` filtrent selon une condition.

Prenons des exemples concrets. Pour trouver l’expéditeur de la lettre, on formule cette requête&nbsp;: chercher n’importe où dans le document (`//`) un élément `correspAction` dans l’espace de noms TEI (`tei:correspAction`), mais seulement celui qui a un attribut type égal à &laquo;&nbsp;sent&nbsp;&raquo; (`[@type='sent']`), puis descendre vers son enfant `persName` (`/tei:persName`). L’expression complète `//tei:correspAction[@type='sent']/tei:persName` nous donne &laquo;&nbsp;Filippo Cavriana&nbsp;&raquo;.

Pour trouver toutes les personnes mentionnées dans le corps de la lettre, on commence par chercher l’élément `body` n’importe où (`//tei:body`), puis on cherche tous les `persName` qu’il contient, peu importe leur profondeur (`//tei:persName`). L’expression `//tei:body//tei:persName` retourne &laquo;&nbsp;Duca&nbsp;&raquo; et &laquo;&nbsp;Filippo Cavriana&nbsp;&raquo; de la signature.

Si on veut extraire une date précise, on peut naviguer vers l’élément `date` et récupérer la valeur de son attribut `when` avec l’arobase&nbsp;: `//tei:date/@when` nous donne &laquo;&nbsp;1568-07-03&nbsp;&raquo;. On peut même être plus spécifique et demander uniquement la date d’envoi&nbsp;: `//tei:correspAction[@type='sent']/tei:date/@when`.

Ces requêtes XPath permettent à XSLT de cibler précisément les éléments à transformer. Sans XPath, XSLT serait aveugle, car XSLT est un langage déclaratif&nbsp;: on définit des règles indiquant comment transformer chaque partie du document identifiée par une expression XPath.

Commençons par extraire simplement le texte d’une lettre. Enregistrez cette feuille sous `templates/tei-to-text.xsl`&nbsp;:

```xml
<xsl:stylesheet version="2.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:tei="http://www.tei-c.org/ns/1.0"
 exclude-result-prefixes="tei">
 <xsl:output method="text" encoding="UTF-8"/>

 <!-- Règle racine : extraire les métadonnées puis le corps de la lettre -->
 <xsl:template match="/">
  <xsl:text>De : </xsl:text>
  <xsl:value-of select="//tei:correspAction[@type='sent']/tei:persName"/>
  <xsl:text>&#xA;À : </xsl:text>
  <xsl:value-of select="//tei:correspAction[@type='received']/tei:persName"/>
  <xsl:text>&#xA;Date : </xsl:text>
  <xsl:value-of select="//tei:correspAction[@type='sent']/tei:date/@when"/>
  <xsl:text>&#xA;&#xA;</xsl:text>
  <xsl:apply-templates select="//tei:body"/>
 </xsl:template>

 <!-- Paragraphes : restituer le texte suivi d’un saut de ligne double -->
 <xsl:template match="tei:p">
  <xsl:apply-templates/>
  <xsl:text>&#xA;&#xA;</xsl:text>
 </xsl:template>

 <!-- Entités nommées avec @ref : mettre en gras et afficher l’identifiant -->
 <xsl:template match="tei:persName[@ref]">
  <xsl:text>**</xsl:text><xsl:apply-templates/><xsl:text>** [</xsl:text>
  <xsl:value-of select="substring-after(@ref,'#')"/><xsl:text>]</xsl:text>
 </xsl:template>

 <!-- Entités nommées sans @ref : mettre en gras uniquement -->
 <xsl:template match="tei:persName[not(@ref)]">
    <xsl:text>**</xsl:text><xsl:apply-templates/><xsl:text>**</xsl:text>
</xsl:template>

</xsl:stylesheet>
```

Le processeur XSLT parcourt l’arbre XML. Quand il trouve un nœud correspondant à l’expression XPath dans `match`, il applique la transformation définie. L’instruction `apply-templates` poursuit le parcours dans les nœuds enfants.

Pour l’exécuter&nbsp;:

```bash
saxon -s:letters/1568-07-03.xml -xsl:templates/tei-to-text.xsl \
  -o:output/1568-07-03.txt
```

Enrichissons la transformation en naviguant plus précisément dans l’arbre. Enregistrez cette feuille sous `templates/tei-to-markdown.xsl`&nbsp;:

```xml
<xsl:stylesheet version="2.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:tei="http://www.tei-c.org/ns/1.0"
 exclude-result-prefixes="tei">

 <xsl:output method="text" encoding="UTF-8"/>

 <!-- Règle racine : normaliser les métadonnées et lancer le parcours du corps -->
 <xsl:template match="/">
  <xsl:text>De : </xsl:text>
  <xsl:value-of select="normalize-space(//tei:correspAction[@type='sent']/tei:persName)"/>
  <xsl:text>&#x0A;À : </xsl:text>
  <xsl:value-of select="normalize-space(//tei:correspAction[@type='received']/tei:persName)"/>
  <xsl:text>&#x0A;Date : </xsl:text>
  <xsl:value-of select="//tei:correspAction[@type='sent']/tei:date/@when"/>
  <xsl:text>&#x0A;&#x0A;</xsl:text>
  <xsl:apply-templates select="//tei:body"/>
 </xsl:template>

 <!-- Paragraphes : restituer le texte suivi d’un saut de ligne double -->
 <xsl:template match="tei:p">
  <xsl:apply-templates/>
  <xsl:text>&#x0A;&#x0A;</xsl:text>
 </xsl:template>

 <!-- Abréviations : afficher la forme développée si disponible -->
 <xsl:template match="tei:choice">
  <xsl:choose>
   <xsl:when test="tei:expan"><xsl:apply-templates select="tei:expan"/></xsl:when>
   <xsl:otherwise><xsl:apply-templates/></xsl:otherwise>
  </xsl:choose>
 </xsl:template>

 <!-- Sauts de ligne normaux : restituer le saut -->
 <xsl:template match="tei:lb[not(@break) or @break='yes']">
  <xsl:text>&#x0A;</xsl:text>
 </xsl:template>
 <!-- Sauts de ligne au milieu d’un mot : supprimer pour recomposer le mot -->
 <xsl:template match="tei:lb[@break='no']"/>

 <!-- Entités nommées avec @ref : mettre en gras et afficher l’identifiant -->
 <xsl:template match="tei:persName[@ref]">
  <xsl:text>**</xsl:text><xsl:apply-templates/><xsl:text>** [</xsl:text>
  <xsl:value-of select="substring-after(@ref,'#')"/><xsl:text>]</xsl:text>
 </xsl:template>
 <!-- Entités nommées sans @ref : mettre en gras uniquement -->
 <xsl:template match="tei:persName[not(@ref)]">
  <xsl:text>**</xsl:text><xsl:apply-templates/><xsl:text>**</xsl:text>
 </xsl:template>

</xsl:stylesheet>

```

Pour l’exécuter&nbsp;:

```bash
saxon -s:letters/1568-07-03.xml -xsl:templates/tei-to-markdown.xsl \
  -o:output/1568-07-03.md
```

Cette feuille extrait les métadonnées depuis le `teiHeader`, parcourt le `body` pour le contenu, et distingue les éléments selon leurs attributs. Le prédicat `[@ref]` cible les éléments dotés de cet attribut, tandis que `[not(@ref)]` sélectionne les autres. La fonction `substring-after(@ref, '#')` récupère l’identifiant interne.

Dans le flux d’édition continue, cette transformation s’exécutera automatiquement après chaque validation réussie, convertissant instantanément les nouvelles lettres encodées en format publiable.

## Conclusion

Cette leçon a posé le socle local de l’édition continue&nbsp;: personnalisation de la TEI via un ODD, génération d’un schéma RELAX NG, validation (RELAX NG et Schematron) et transformations XSLT vers Markdown et HTML. Ces pratiques assurent cohérence, interopérabilité et portabilité du corpus. Elles permettent déjà de produire localement une édition de qualité professionnelle.
En intégrant ces pratiques dans des chaînes d’automatisation (Git, CI/CD), la publication instantanée et l’archivage pérenne sont rendus possibles. Dans la seconde partie, nous brancherons ce socle sur une chaîne d’intégration et de déploiement continus&nbsp;: gestion de versions avec Git, automatisation (GitHub Actions/GitLab CI/CD), assignation d’un DOI à des instantanés sur Zenodo. L’objectif est que la moindre modification d’un fichier TEI déclenche automatiquement contrôle, transformation et mise en ligne, réalisant ainsi la promesse de l’édition continue.

## Références

- Adoptium. _Eclipse Temurin_ (environnements d’exécution Java). [https://adoptium.net/](https://perma.cc/T6SQ-XYZE).
- Burnard, Lou. &laquo;&nbsp;What Is TEI Conformance, and Why Should You Care?&nbsp;&raquo; _Journal of the Text Encoding Initiative_ 12 (2019). [https://doi.org/10.4000/jtei.1777](https://doi.org/10.4000/jtei.1777).
- CERN and OpenAIRE. _Zenodo_ (plateforme d’archivage et d’attribution de DOI). [https://zenodo.org](https://perma.cc/Q2L3-NJXA).
- Clark, James, dir. _Jing and Trang_ (validateur RELAX NG). [https://github.com/relaxng/jing-trang/releases](https://perma.cc/2Y3Z-ZZRR).
- Getty Research Institute. _Getty Thesaurus of Geographic Names (TGN)_. [https://www.getty.edu/research/tools/vocabularies/tgn/index.html](https://perma.cc/C2VV-ZWQL).
- Godbarge, Clément, éd. _Filippo Cavriana: The Secret Correspondence_. Édition numérique en cours. [https://pantagrueliste.github.io/CavrianaCorr_FrontEnd/](https://pantagrueliste.github.io/CavrianaCorr_FrontEnd/).
- Saxonica. _Saxon-HE_ (Home Edition). [https://github.com/Saxonica/Saxon-HE/releases](https://perma.cc/29UA-6GD8).
- Schematron stakeholders. _ISO Schematron XSLT2 implementation_. [https://github.com/Schematron/stf](https://perma.cc/6PQN-4XEB).
- TEI Consortium. _Getting Started with P5 ODDs_. [https://tei-c.org/guidelines/customization/getting-started-with-p5-odds/](https://perma.cc/JT6L-87S8).
- TEI Consortium. _RomaJS_. Version 1.3.3. n.d. GPL-3.0. [https://github.com/TEIC/romajs](https://perma.cc/JE26-2PHQ).
- TEI Consortium. _TEI P5&nbsp;: Recommandations pour l’encodage et l’échange de textes électroniques_. [https://tei-c.org/release/doc/tei-p5-doc/fr/html/index.html](https://perma.cc/WRF8-ZEFJ).
- Vaughan, Nicolás. &laquo;&nbsp;Introduction à l'encodage de texte TEI (partie 1)&nbsp;&raquo;. Traduction par Maritza Beatriz García Rodríguez. _Programming Historian en français_ 8 (2026). [https://doi.org/10.46430/phfr0040](https://doi.org/10.46430/phfr0040).
- Vidal-Gorène, Chahan. &laquo;&nbsp;La reconnaissance automatique d'écriture à l'épreuve des langues peu dotées&nbsp;&raquo;. _Programming Historian en français_ 5 (2023). [https://doi.org/10.46430/phfr0023](https://doi.org/10.46430/phfr0023).
- VIAF. _Virtual International Authority File_. [https://viaf.org/fr](https://perma.cc/4GT6-QWAR).
