---
title: Consignes aux traducteurs et aux traductrices
layout: blank
original: translator-guidelines
skip_validation: true
---

# Consignes aux traducteurs et aux traductrices
<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />
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
Lorsque le fichier contenant votre traduction a été préparé en suivant les spécifications ci-haut, il est temps de le soumettre à la révision par les pairs.

La [page de projet du Programming Historian sur GitHub](https://github.com/programminghistorian) contient deux dépôts (un dépôt est un endroit où l'on entrepose des fichiers et des répertoires apparentés; un répertoire-racine, en quelque sorte). L'un de ces dépôts, nommé [jekyll], héberge le code de la version active du site que vous pouvez visiter au http://programminghistorian.org. L'autre dépôt se nomme [ph-submissions].

Nous préférons que les traducteurs et les traductrices soumettent les leçons en les ajoutant directement au dépôt [ph-submissions]. GitHub vous permet de le faire en téléversant vos fichiers à l'aide d'actions glisser-déposer avec lesquelles vous êtes probablement déjà à l'aise. En tant que nouveau traducteur ou nouvelle traductrice, voici les étapes à suivre:

1. Créez un [compte GitHub gratuit](https://github.com/join). Cela ne vous prendra pas plus de 30 secondes.
2. Envoyez à votre rédacteur ou à votre rédactrice un courriel contenant votre nom d'usager GitHub et le nom du fichier contenant votre traduction. Le rédacteur ou la rédactrice vous ajoutera ensuite à la liste des **collaborateurs** du dépôt [ph-submissions]. Une fois que vous aurez été ajouté(e) à la liste des collaborateurs, vous pourrez effectuer vous-même des changements au dépôt [ph-submissions], notamment y ajouter des fichiers, les modifer, les effacer ou les renommer. Le rédacteur ou la rédactrice créera aussi un sous-répertoire qui portera le même nom que votre leçon dans le répertoire des images. (Si votre leçon inclut des liens vers d'autres fichiers de données, demandez des instructions spécifiques à votre rédacteur ou à votre rédactrice.)
3. Une fois que vous êtes inscrit(e) à la liste des collaborateurs, naviguez jusqu'au répertoire des [traductions en français](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/fr/traductions) du dépôt [ph-submissions]. Puis, glissez et déposez le fichier Markdown contenant votre leçon traduite dans la fenêtre de votre navigateur Web. (Si vous avez besoin d'aide, vous pouvez consulter [le manuel de GitHub (en anglais)](https://help.github.com/articles/adding-a-file-to-a-repository/)). Puis, cliquez sur le bouton vert "Commit Changes"; il n'est pas nécessaire de changer le message par défaut qui vous est proposé.
4. Vous disposez peut-être d'images associées au texte de votre leçon. Assurez-vous que tous les fichiers contenant ces images sont nommés correctement, en fonction de nos normes de nomenclature. Puis, naviguez vers le [répertoire des images](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images) sur le dépôt [ph-submissions]. Cliquez sur le répertoire qui porte le même nom que votre leçon (votre rédacteur ou votre rédactrice devrait l'avoir créé pour vous; si vous ne le voyez pas, communiquez avec votre rédacteur ou votre rédactrice et attendez ses instructions). Lorsque vous avez atteint le bon répertoire, glissez et déposez tous les fichiers contenant vos images dans la fenêtre de votre navigateur Web, comme à l'étape 3. Notez que vous pourrez déposer plusieurs fichiers d'un seul coup si vous le désirez mais qu'il ne sera pas possible de déposer un *répertoire* contenant vos fichiers d'images.
5. Consultez l'aperçu de votre leçon! Attendez quelques minutes (souvent moins) pour que GitHub ait le temps de convertir votre fichier Markdown en HTML et d'en faire une page Web accessible. Puis, naviguez vers `http://programminghistorian.github.io/ph-submissions/lessons/` + `VOTRE-LECON` (mais remplacez VOTRE-LECON par le nom de votre fichier).
6. Prévenez votre rédacteur ou votre rédactrice du téléversement des fichiers de votre leçon sur le dépôt [ph-submissions]. (Il ou elle devrait normalement recevoir une notification automatique mais nous préférons nous assurer que votre dépôt ne passera pas inaperçu.)

<div class="alert alert-info">
  Si vous êtes déjà à l'aise avec GitHub et avec la version de git accessible par la ligne de commande de votre système d'exploitation, vous pouvez aussi soumettre votre traduction et les images qui l'accompagnent à l'aide d'une 'pull request' vers le dépôt `ph-submission`, puis fusionner celle-ci avec le dépôt principal lorsque vous ferez partie de la liste des collaborateurs. <b>Veuillez ne pas soumettre de leçons par 'pull request' au dépôt`jekyll`</b> pour que nous puissions offrir des aperçus visibles des leçons en cours de développement.
</div>

### Traduction soumise! Et maintenant?
Pour savoir ce qui se passera après que vous ayez soumis votre traduction, n'hésitez pas à consulter nos [consignes aux rédacteurs et aux rédactrices](https://programminghistorian.org/fr/consignes-redacteurs) qui décrivent notre processus éditorial en détail. En voici les grandes lignes.

L'étape la plus importante à court terme est la création d'un [ticket](https://github.com/programminghistorian/ph-submissions/issues) pour la nouvelle traduction dans le dépôt [ph-submissions], où l'on retrouvera notamment un lien vers l'aperçu de votre leçon que vous avez consulté à l'étape 5. Le rédacteur ou la rédactrice et au moins deux évaluateurs ou évaluatrices (invité(e)s par le rédacteur ou la rédactrice) publieront leurs commentaires au sujet de votre traduction sur ce ticket.

### En attendant les retours des relectures 
Nous tentons de compléter le processus de relecture en quatre semaines ou moins, mais il est possible que des délais imprévus ou un emploi du temps chargé entraînent des retards.

En accord avec les principes de la recherche publique et de l'évaluation ouverte par les pairs, nous souhaitons que la discussion demeure sur GitHub. Cependant, nous voulons aussi que tous les intervenants soient à l'aise avec le processus. Si vous ressentez le besoin de discuter d'un enjeu en privé, n'hésitez pas à contacter directement [votre rédacteur ou votre rédactrice par courriel](/project-team) ou à faire appel à notre médiateur francophone [François Dominic Laramée](/project-team).

### Répondre aux relectures reçues 
Le rédacteur ou la rédactrice qui assure le suivi éditorial de votre traduction et les évaluateurs et évaluatrices recommanderont fort probablement des améliorations à apporter à votre texte dans le "ticket" qui lui est associé. Le rédacteur ou la rédactrice devrait spécifier clairement quelles améliorations sont essentielles, lesquelles sont optionnelles et lesquelles peuvent être mises de côté. 

Vous pouvez modifier vos fichiers directement sur GitHub en suivant [ces instructions (en anglais)](https://help.github.com/articles/editing-files-in-your-repository/).

Afin d'assurer une publication rapide de votre traduction, nous demandons que vous produisiez une version révisée 4 semaines après la réception des instructions de votre rédacteur ou de votre rédactrice. Si vous prévoyez avoir du mal à respecter ce délai, veuillez contacter votre rédacteur ou votre rédactrice pour fixer une date plus appropriée.

Si, à quelque moment que ce soit, vous doutez de votre rôle ou de la procédure à suivre, n'hésitez pas à contacter votre rédacteur ou votre rédactrice par courriel ou, mieux encore, à publier une question sur le ticket de relecture de votre leçon (un autre membre de notre équipe éditoriale pourrait voir la question et être en mesure de vous répondre plus rapidement que votre rédacteur ou votre rédactrice). Vous comprendrez qu'il faut parfois quelques jours pour obtenir une réponse, mais nous espérons que la qualité des ajustements apportés à la version finale de votre traduction en vaudra la peine.

### Informer le rédacteur ou la rédactrice qui assure le suivi éditorial que vous avez fini
Lorsque vous aurez terminé de répondre aux recommandations issues de l'évaluation, prévenez votre rédacteur ou votre rédactrice. Si la traduction est jugée satisfaisante, le rédacteur ou la rédactrice en chef du *Programming Historian en français* effectuera une dernière lecture, déplacera les fichiers du dépôt `ph-submissions` vers le dépôt `jekyll` et mettra à jour notre répertoire des leçons. À ce moment, votre traduction sera publiée.
