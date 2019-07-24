---
title: Consignes aux traducteurs et aux traductrices
layout: blank
original: translator-guidelines
skip_validation: true
---

# Consignes aux traducteurs et aux traductrices
<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />
<h2 class="noclear">Étape 1: <a href="#proposer-traduction-lecon">Proposer la traduction d'une leçon </a></h2>
<h2 class="noclear">Étape 2: <a href="#writing-a-new-lesson">Traduire une leçon et la mettre en page</a></h2>
<h2 class="noclear">Étape 3: <a href="#submitting-a-new-lesson">Soumettre la leçon traduite</a></h2>

## Proposer la traduction d'une leçon 
Si vous désirez traduire une leçon publiée dans le *Programming Historian*, veuillez consulter la liste des traductions en cours et contacter {% include managing-editor.html lang=page.lang %} pour discuter de vos compétences langagières et de votre expérience de traduction. Nous cherchons des traducteurs et traductrices qui font preuve de rigueur, qui produisent des textes agréables à lire et qui sont sensibles aux besoins d'un public de lecteurs et de lectrices francophones.

Lorsque la traduction d'une leçon publiée a été assignée, un membre de notre équipe éditoriale crée un "Ticket de relecture de traduction" dans notre [dépôt Github](https://github.com/programminghistorian/ph-submissions) où la révision par les pairs aura lieu. Ce ticket inclut un forum de discussion qui servira à documenter la progression du processus de révision. Afin de minimiser les délais de publication, nous vous demandons de soumettre votre traduction dans les 90 jours suivant l'approbation de votre proposition par l'équipe éditoriale.

## Traduire une leçon et la mettre en page
Les principales étapes de la traduction d'une leçon sont les suivantes:
- la traduction du corps de texte de la leçon;
- la traduction des termes employés dans le code et dans les exemples, si possible;
- si la leçon utilise un logiciel dont l'interface est disponible en français, les termes techniques associés à ce logiciel et qui sont employés dans le texte (entrées de menus, étiquettes de boutons, etc.) doivent être traduits en conséquence;
- la traduction des titres et des sous-titres de figures. Dans certains cas, il faudra produire de nouvelles figures, par exemple lorsqu'un exercice fait appel à un logiciel dont l'interface est disponible en français;
- le remplacement des liens et des notes contenus dans le texte d'origine par des équivalents francophones, lorsque cela est possible; par exemple, des liens vers la version française de la documentation d'un logiciel, vers le contenu francophone de Wikipedia, etc.

Si vous décidez de traduire une leçon, veuillez tenir compte du fait que vous vous adressez à un auditoire international. En matière de style et de choix linguistiques, veuillez vous référer à nos [consignes aux auteurs]({{site.baseurl}}/fr/consignes-auteurs).

Veuillez aussi noter que toutes nos leçons doivent être rédigées en format Markdown et obéir à nos consignes techniques de mise en page, que vous pourrez également consulter dans nos [consignes aux auteurs]({{site.baseurl}}/fr/consignes-auteurs).

## Soumettre la leçon traduite
Lorsque le fichier contenant votre traduction a été préparé en suivant les spécifications ci-haut, il est temps de le soumettre à la révision par les pairs.

La [page de projet du Programming Historian sur GitHub](https://github.com/programminghistorian) contient deux dépôts (un dépôt est un endroit où l'on entrepose des fichiers et des répertoires apparentés; un répertoire-racine, en quelque sorte). L'un de ces dépôts, nommé [jekyll], héberge le code de la version active du site que vous pouvez visiter au http://programminghistorian.org. L'autre dépôt se nomme [ph-submissions].

Nous préférons que les traducteurs soumettent leurs leçons en les ajoutant directement au dépôt [ph-submissions]. GitHub vous permet de le faire en téléversant vos fichiers à l'aide d'actions glisser-déposer avec lesquelles vous êtes probablement déjà à l'aise. En tant que nouveau traducteur ou nouvelle traductrice, voici les étapes à suivre:

1. Créez un [compte GitHub gratuit](https://github.com/join). Cela ne vous prendra pas plus de 30 secondes.
2. Envoyez à votre éditeur ou à votre éditrice un courriel contenant votre nom d'usager GitHub et le nom du fichier de votre traduction. L'éditeur ou l'éditrice vous ajoutera ensuite à la liste des **collaborateurs** du dépôt [ph-submissions]. Une fois que vous aurez été ajouté(e) à la liste des collaborateurs, vous pourrez effectuer vous-même des changements au dépôt [ph-submissions], notamment y ajouter des fichiers, les éditer, les effacer ou les renommer. L'éditeur ou l'éditrice créera aussi un sous-répertoire qui portera le même nom que votre leçon dans le répertoire des images. (Si votre leçon inclut des liens vers d'autres fichiers de données, demandez des instructions spécificiques à votre éditeur ou à votre éditrice.)
3. Lorsque votre éditeur ou votre éditrice vous a ajouté à la liste des collaborateurs, naviguez jusqu'au répertoire des [traductions en français](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/fr/traductions) sur le dépôt [ph-submissions]. Puis, glissez et déposez le fichier Markdown contenant votre leçon dans la fenêtre de votre navigateur Web. (Si vous avez besoin d'aide, vous pouvez consulter [le manuel de GitHub (en anglais)](https://help.github.com/articles/adding-a-file-to-a-repository/)). Puis, cliquez sur le bouton vert "Commit Changes"; il n'est pas nécessaire de changer le message par défaut qui vous est proposé.
4. Vous disposez peut-être d'images associées au texte de votre leçon. Assurez-vous que tous les fichiers contenant ces images sont nommés correctement, en fonction de nos normes de nomenclature. Puis, naviguez vers le [répertoire des images](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images) sur le dépôt [ph-submissions]. Cliquez sur le répertoire qui porte le même nom que votre leçon (votre éditeur ou votre éditrice devrait l'avoir créé pour vous; si vous ne le voyez pas, communiquez avec votre éditeur ou votre éditrice et attendez ses instructions). Lorsque vous avez atteint le bon répertoire, glissez et déposez tous vos fichiers d'images dans votre navigateur, comme à l'étape 3. Notez que vous ne pourrez pas déposer un répertoire d'images mais qu'il est possible de déposer plusieurs fichiers d'images d'un seul coup.
5. Consultez l'aperçu de votre leçon! Attendez quelques minutes (souvent moins) pour que GitHub ait le temps de convertir votre fichier Markdown en HTML et d'en faire une page Web accessible. Puis, naviguez vers `http://programminghistorian.github.io/ph-submissions/lessons/` + `VOTRE-LECON` (mais remplacez VOTRE-LECON par le nom de votre fichier).
6. Prévenez votre éditeur ou votre éditrice du téléversement des fichiers de votre leçon sur le dépôt [ph-submissions]. (Il ou elle devrait normalement recevoir une notification automatique mais nous préférons nous assurer que votre livraison ne passera pas inaperçue.)

<div class="alert alert-info">
  Si vous êtes déjà à l'aise avec GitHub et avec la version de git accessible par la ligne de commande de votre système d'exploitation, vous pouvez aussi soumettre votre traduction et les images qui l'accompagnent à l'aide d'une 'pull request' vers le dépôt `ph-submission`, puis fusionner celle-ci avec le dépôt principal après avoir été ajouté(e) à la liste des collaborateurs. <b>Veuillez ne pas soumettre de leçons par 'pull request' au dépôt Jekyll</b> pour que nous puissions offrir des aperçus visibles des leçons en cours de développement.
</div>

### Traduction soumise! Et maintenant?
Pour savoir ce qui se passera après que vous ayez soumis votre traduction, n'hésitez pas à consulter nos [consignes aux rédacteurs et aux rédactrices](https://programminghistorian.org/fr/consignes-redacteurs) qui décrivent notre processus éditorial en détail. En voici les grandes lignes:

L'étape la plus importante à court terme est la création d'un [ticket](https://github.com/programminghistorian/ph-submissions/issues) pour la nouvelle traduction dans le dépôt [ph-submissions], où l'on trouvera notamment un lien vers l'aperçu de votre leçon que vous avez consulté à l'étape 5. Le rédacteur ou la rédactrice et au moins deux évaluateurs (invités par le rédacteur ou la rédactrice) publieront leurs commentaires sur ce ticket.

### En attendant les retours des relectures 
Nous tentons de compléter le processus de révision en quatre semaines ou moins, mais il est possible que des délais imprévus ou un emploi du temps chargé entraînent des retards.

En accord avec les principes de la recherche publique et de la révision par les pairs ouverte, nous recommandons que la discussion demeure sur GitHub. Cependant, nous voulons aussi que tous les intervenants soient confortables avec le processus. Si vous ressentez le besoin de discuter d'un enjeu en privé, n'hésitez pas à contacter directement [votre rédacteur ou votre rédactrice par courriel](/project-team) ou à faire appel à nos médiateurs [Marie Puren et François Dominic Laramée](/project-team).

### Répondre aux relectures reçues 
Your editor and reviewers will most likely make some suggestions for improvements on the "issue" for your translation. The editor should clarify which suggestions are essential to address, which are optional, and which can be set aside.

You can edit your files on GitHub, following [these instructions](https://help.github.com/articles/editing-files-in-your-repository/).

Your revisions should be completed within 4 weeks of receiving guidance from the editor on how to respond to the peer review. This is to ensure that translations are published in a timely fashion and do not drag on unnecessarily. If you anticipate having trouble meeting the deadline, you should contact your editor to establish a more suitable due date.

If at any point you are unsure of your role or what to do next, feel free to email your editor or, better yet, to post a question to the issue (another editor might see it and can help you sooner than your own editor). You’ll understand that sometimes it will take us a few days to respond, but we hope the improvements to the finished lesson will be worth the wait.

### Informer le rédacteur ou la rédactrice qui assure le suivi éditorial que vous avez fini
Once you have finished responding to feedback, let your editor know. If they are satisfied with the lesson at this stage, the, *Programming Historian*'s Managing Editor will review your lesson, move it from the `ph-submissions` repository to the `jekyll` repository, and update our lessons directory where it will be published.
