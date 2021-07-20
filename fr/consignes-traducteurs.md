---
title: Consignes aux traducteurs et aux traductrices
layout: blank
original: translator-guidelines
skip_validation: true
---

# Consignes aux traducteurs et aux traductrices
<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" alt="{{ site.data.snippets.write-a-lesson-image-alt[page.lang] }}"/>
<h2 class="noclear">Étape 1: <a href="#proposer-la-traduction-dune-leçon">Proposer la traduction d'une leçon </a></h2>
<h2 class="noclear">Étape 2: <a href="#traduire-une-leçon-et-la-mettre-en-page">Traduire une leçon et la mettre en page</a></h2>
<h2 class="noclear">Étape 3: <a href="#soumettre-la-leçon-traduite">Soumettre la leçon traduite</a></h2>

## Proposer la traduction d'une leçon 
Si vous désirez traduire en français une leçon publiée dans le *Programming Historian*, veuillez consulter la liste des traductions en cours et contacter {% include managing-editor.html lang=page.lang %} pour discuter de vos compétences langagières et de votre expérience en traduction. Nous cherchons des traducteurs et traductrices qui font preuve de rigueur, qui produisent des textes agréables à lire et qui comprennent les besoins spécifiques d'un public de lecteurs et de lectrices francophones.

Lorsqu'une leçon a été assignée à un traducteur ou à une traductrice, un membre de notre équipe de rédaction crée un "Ticket de relecture de traduction" dans notre [dépôt Github](https://github.com/programminghistorian/ph-submissions), où le processus d'évaluation par les pairs aura lieu. Ce ticket inclut un forum de discussion qui servira à documenter la progression du travail. Afin de minimiser les délais de publication, nous vous demandons de livrer votre traduction dans les 90 jours suivant l'approbation de votre proposition par l'équipe de rédaction.

## Traduire une leçon et la mettre en page
Les principales étapes de la traduction d'une leçon sont les suivantes:
- la traduction du corps de texte de la leçon;
- la traduction des termes employés dans le code et dans les exemples, si possible;
- si la leçon utilise un logiciel dont l'interface est disponible en français, les termes techniques associés à ce logiciel et qui sont employés dans le texte (entrées de menus, étiquettes de boutons, etc.) doivent être traduits en conséquence;
- la traduction des titres et des sous-titres de figures. Dans certains cas, il faudra produire de nouvelles figures, par exemple lorsqu'un exercice fait appel à un logiciel dont l'interface est disponible en français;
- le remplacement, lorsque cela est possible, des liens et des notes contenus dans le texte d'origine par des équivalents francophones; par exemple, des liens vers la version française de la documentation d'un logiciel, vers des articles de la version française de Wikipedia, etc.

Quand vous traduisez une leçon, veuillez tenir compte du fait que vous vous adressez à un auditoire international. En matière de style et de choix linguistiques, veuillez vous référer à nos [consignes aux auteurs]({{site.baseurl}}/fr/consignes-auteurs).

Veuillez aussi noter que toutes nos leçons doivent être rédigées en format Markdown et obéir à nos consignes techniques de mise en page, que vous pourrez également consulter dans nos [consignes aux auteurs]({{site.baseurl}}/fr/consignes-auteurs).

## Soumettre la leçon traduite
Une fois que votre traduction a été préparée en suivant les consignes données ci-dessus, il est temps d'organiser l'évaluation par les pairs.

Lorsque vous êtes prêt(e) à soumettre votre traduction, merci d'envoyer tous les fichiers (texte, images, données...) au rédacteur ou à la rédactrice en charge du suivi éditorial de celle-ci, qui les téléversera pour vous dans notre dépôt dédié à l'évaluation par les pairs sur [Github](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/fr/traductions). Voici comment procéder de votre côté:

1. **Obtenir accès à notre dépôt d'évaluation**: pour cela il suffit de créer un [compte gratuit sur Github](https://github.com/join) et le communiquer à votre rédacteur ou rédactrice, qui va ensuite vous ajouter comme **collaborateur ou collaboratrice** dans le dépôt [ph-submissions](https://github.com/programminghistorian/ph-submissions). Ce n'est pas à vous de faire le téléversement initial des fichiers, mais l'accès au dépôt est nécessaire pour que vous puissiez par la suite apporter des modifications et des mises à jour. 
2. **Préparer ses fichiers**: vous avez probablement des images qui accompagnent votre leçon (si, par exemple, vous avez produit des images d'interfaces en français etc). Merci de vérifier que tous les fichiers images sont nommés de manière appropriée, en accord avec les conventions de nommage spécifiées dans les consignes aux auteur(e)s. Ces fichiers doivent nous parvenir dans un dossier unique compressé. Si vous avez en plus des fichiers de données, merci de nous envoyer ces fichiers aussi dans un dossier compressé distinct.
3. **Envoyer un message électronique**: informez votre rédacteur ou rédactrice que vous êtes prêt(e) à soumettre votre traduction, en joignant le fichier de celle-ci et, le cas échéant, les dossiers des fichiers images et données. 
4. **Participer à la discussion**: le rédacteur ou la rédactrice en charge du suivi éditorial de votre traduction déposera vos fichiers dans notre [dépôt de soumissions](https://github.com/programminghistorian/ph-submissions) en faisant quelques premières modifications si nécessaire (métadonnées, syntaxe Markdown etc). Ensuite, un ticket sera ouvert pour l'évaluation ouverte de votre traduction, pendant laquelle vous avez la possibilité d'échanger avec celles et ceux qui participent au processus.
5. **Apporter des modifications**: si le dépôt initial des fichiers est fait par votre rédacteur ou rédactrice assigné(e), le processus de la relecture peut néanmoins entraîner le besoin d'apporter des modifications supplémentaires de votre côté. Toutes les révisions se font directement par les traducteurs sur les fichiers versés dans notre dépôt pour avoir la certitude que vous travaillez sur la version la plus récente du fichier de la traduction.

## Le processus de l'évaluation ouverte par les pairs
Une fois que votre rédacteur ou rédactrice assigné(e) aura déposé et formaté vos fichiers de manière appropriée, vous recevrez un lien de prévisualisation de la leçon qui vous permettra de vérifier aussi de votre côté que tout se présente correctement; si ce n'est pas le cas, vous pouvez apporter des corrections. 

La relecture de votre traduction a lieu dans le cadre d'un [ticket](https://github.com/programminghistorian/ph-submissions/issues) Github qui prend ainsi la forme d'un forum de discussion ouverte. Merci de garder à l'esprit que l'évaluation par les pairs se fait publiquement et elle reste disponible à la consultation publique; le ticket en est l'enregistrement. Si pour quelque raison que ce soit vous n'êtes pas à l'aise ou souhaitez une évaluation par les pairs non publique, merci de prendre contact avec votre rédacteur ou rédactrice assigné(e). 

Concernant les traductions, l'évaluation doit être comprise comme relecture critique dont l'objectif est de se garantir la pertinence du texte pour un lectorat francophone. L'évaluation ouverte par les pairs du contenu de la leçon a, quant à elle, déjà eu lieu avant la publication dans la langue originale. Nous appliquons néanmoins les mêmes principes de base pour les relectures des traductions que pour le processus de l'évaluation ouverte par les pairs. 

Le processus de l'évaluation se passe habituellement en trois étapes:

1) Le rédacteur ou la rédactrice assigné(e) à votre traduction en fait une première lecture attentive. Vous êtes à ce stade susceptible de recevoir un premier retour qui pourrait solliciter votre réponse. L'objectif de ce premier retour est de se garantir la pertinence de votre traduction pour le lectorat du *Programming Historian en français* et qu'elle est fonctionnelle avant d'être proposée à l'évaluation externe ou interne. Vous avez normalement un mois pour répondre à cette première évaluation. 

2) Ensuite, votre rédacteur ou  rédactrice assigné(e) propose la leçon à l'évaluation formelle par les pairs. Cela implique l'invitation d'un ou deux évaluateurs ou évaluatrices externes ou internes, mais potentiellement aussi la participation d'une communauté plus large, car tout commentaire est bienvenu (pourvu que les règles de bonne conduite, explicités dans le ticket, soient observées). En général, nous accordons aux évaluateurs et évaluatrices un délai d'un mois pour fournir leurs commentaires, il peut néanmoins arriver que ce délai ne soit pas respecté pour des raisons indépendantes de la volonté des personnes impliquées au processus. Vous devez attendre l'ensemble des relectures et les instructions consécutives de votre rédacteur our rédactrice assigné(e) avant d'aller plus loin. Le plus souvent il s'agit de simples suggestions d'apporter certaines modifications. Afin d'assurer une publication rapide de votre traduction, nous demandons que vous produisiez une version révisée quatre semaines après la réception des instructions, mais le délai peut être revu si vous avez du mal à le respecter. Selon les commentaires et la nature des questions soulevées, il se peut que vous ayez à réviser le tutoriel plus qu'une fois. Toufois, votre rédacteur ou rédactrice assignée(e) veillera à ce que vous receviez une guidance claire pour que la traduction soit publiée. Par ailleurs, il est toujours possible de retirer votre traduction du processus de l'évaluation, si tel est votre choix. 

3) Au bout de ce processus, si tous les critères sont remplis, votre rédacteur ou rédactrice assignée(e) donne le feu vert pour la publication. C'est ensuite au rédacteur ou à la rédactrice en chef de relire la traduction pour s'assurer de sa conformité aux consignes aux traducteurs et traductrices et aux standards du *Programming Historian*. Parfois des révisions et des corrections supplémentaires peuvent être nécessaires à ce stade pour que la traduction puisse être publiée. Une fois que le rédacteur ou la rédactrice en chef juge la version révisée satisfaisante, la traduction peut être publiée. Votre rédacteur ou rédactrice assigné(e) vous fournira toute information nécessaire à ce stade. 

Il serait utile de consulter nos [consignes aux évaluateurs et évaluatrices](/fr/consignes-evaluateurs) qui détaillent notre processus de révision et de publication.

Si jamais vous êtes dans l'incertitude sur comment procéder, n'hésitez pas à poster votre question sur le ticket d'évaluation, un membre de notre équipe vous apportera des réponses dans les délais les plus brefs possible. Nous faisons de notre mieux pour répondre au bout de quelques jours.

### Demandez nous des comptes

Notre équipe de bénévoles fait de son possible pour se garantir l'évaluation rigoureuse, collégiale et efficace des auteur(e)s par les pairs. Toutefois, il peut y avoir des failles, c'est pourquoi nous souhaitons que les auteur(e)s nous aident à maintenir un haut niveau de service. Si, pour quelque raison que ce soit, vous estimez ne pas avoir été traité(e) correctement, ou ne comprenez pas trop quel est votre rôle ou ce qu’on attend de vous, ou encore vous considérez que l'évaluation présente des retards injustifiés ou que quelqu'un a été rude avec vous, enfin, pour quelque souci que ce soit, n'hésitez pas à nous en tenir informés afin de pouvoir agir. 

Exprimer des réserves n'a AUCUN impact négatif sur le processus et le résultat de l'évaluation par les pairs. 

Pour ce faire, vous avez plusieurs points d'entrée et sentez-vous libre de contacter la personne avec laquelle vous êtes le plus à l'aise: 

* votre rédacteur ou rédactrice assigné(e); 
* le rédacteur ou la rédactrice en chef;
* notre médiatrice indépendante ([Dr Hélène Huet](mailto:hhuet@ufl.edu)).

Nous oeuvrons pour que tout se passe au mieux pour vous, mais si jamais vous estimez vous trouver dans une situation peu confortable, nous vous remercions de nous aider à y remédier et à améliorer les choses. 

### Nous interpeller

Notre équipe de bénévoles fait de son possible pour se garantir l'évaluation rigoureuse, collégiale et efficace des traductions par les pairs. Toutefois, il peut y avoir des failles, c'est pourquoi nous souhaitons que vous nous aidiez à maintenir un haut niveau de service. Si, pour quelque raison que ce soit, vous estimez ne pas avoir été traité(e) correctement, ou ne comprenez pas trop quel est votre rôle ou ce qu’on attend de vous, ou encore vous considérez que l'évaluation présente des retards injustifiés ou que quelqu'un a été rude avec vous, enfin, pour quelque souci que ce soit, n'hésitez pas à nous en tenir informés afin de pouvoir agir. 

Exprimer des réserves n'a AUCUN impact négatif sur le processus et le résultat de l'évaluation par les pairs. 

Pour ce faire, vous avez plusieurs points d'entrée et sentez-vous libre de contacter la personne avec laquelle vous êtes le plus à l'aise: 

* votre rédacteur ou rédactrice assigné(e); 
* le rédacteur ou la rédactrice en chef;
* notre médiatrice indépendante ([Dr Hélène Huet](mailto:hhuet@ufl.edu)).

Nous oeuvrons pour que tout se passe au mieux pour vous, mais si jamais vous estimez vous trouver dans une situation peu confortable, nous vous remercions de nous aider à y remédier et à améliorer les choses. 
