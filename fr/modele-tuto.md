# Modèle de leçon pour le Programming Historian en français

Vous pouvez utiliser ce fichier en tant que modèle pour écrire votre leçon. Il vous fournit des informations et des instructions de formatage sans pour autant remplacer les consignes aux auteur(e)s que nous vous remercions par avance de bien vouloir lire (/fr/consignes-auteurs). 

## Ne pas oublier:

*	La longueur des tutoriels ne doit pas excéder 8000 mots (en incluant le code source).
*	Veillez à garder un ton formel mais accessible
*	Nous conseillons l'utilisation de la deuxième personne du pluriel (*vous*) pour vous adresser à votre lectorat 
*	Merci de veiller à ce que votre français soit compréhensible dans tout l'espace francophone 
*	Souvenez-vous que vous rédigez un tutoriel ou une leçon, mais pas un article académique
*   Adhérez aux principes de l’open source et du libre accès
*   Écrivez pour un public international
*   Écrivez de manière durable 

## Métadonnées de la leçon

**Au moment de la soumission de votre leçon, merci d'effacer tout ce qui précède cette ligne**.

---
title: VOTRE TITRE  
collection: lessons  
layout: lesson  
authors:
- PRÉNOM NOM 1
- PRÉNOM NOM 2, etc
---

# Table de matières

Merci de ne pas oublier d'introduire au tout début du texte cette brève ligne de code qui génère automatiquement la table de matières de votre leçon: 

{% include toc.html %}

--

## Exemples des formatages les plus courants en Markdown:

### Titres

# Titre 1
## Titre 2
### Titre 3
#### Titre 4


### Mise en forme de caractères

**texte en gras**
*texte en italique*
`mots réservés` ou `noms_de_fichiers`

### Liens

Si vous souhaitez renvoyer à une autre leçon du *Programming Historian*, merci d'utiliser des liens relatifs, par exemple: 
- Pour aller plus loin, vous pouvez consulter [notre leçon sur la préservation des données de recherche](/fr/lecons/preserver-ses-donnees-de-recherche).  
Merci de faire en sorte que les phrases qui intégrent des liens soient parlantes, plutôt que d'utiliser des phrases comme "cliquer ici".

### Insérer des images

Merci de copier la brève ligne de code fournie ci-dessous, si vous souhaitez insérer une image. Remplacez les mots en majuscules avec les informations sur votre image (par exemple,  Figure1.jpg). Les légendes doivent annoncer les images de manière ordonnée (par exemple, "Figure 1: ..."). 

{% include figure.html filename="NOM-FICHIER-IMAGE" caption="LÉGENDE DE L'IMAGE" %}

### Alertes et messages importants

Si vous souhaitez attirer l'attention de votre lectorat sur un point précis, vous pouvez ajouter un bloc à part dans le texte:

```
<div class="alert alert-warning">
Attention à ces instructions, elles sont très importantes!
</div>
```

Le message sera encadré et dans une couleur différente, il servira ainsi à attirer l'attention à une mise en garde spécifique. 

### Comment formater une liste non ordonnée

* Voici un item
* Voici un autre item
* Voici un dernier item
	
### Comment formater une liste ordonnée

1. Voici un item
2. Voici un autre item
3. Voici un dernier item

###Comment formater un tableau

| en-tête 1 | en-tête 2 | en-tête 3 |
| --------- | --------- | --------- |
| ligne 1, colonne 1 | ligne 1, colonne 2 | ligne 1, colonne 3|
| ligne 2, colonne 1 | ligne 2, colonne 2 | ligne 2, colonne 3|
| ligne 3, colonne 1 | ligne 3, colonne 2 | ligne 3, colonne 3|
Tableau 1: Ce tableau contient...

### Références

*	Utiliser des hyperliens dans le texte plutôt que d'insérer des notes de fin peut convenir dans la plupart de cas.  
*	La phrase source d'un hyperlien doit être sémantique, éviter par conséquent des phrases du type "cliquer ici".
*	Utiliser des notes de fin pour renvoyer aux références bibliographiques académiques, qu'elles soient électroniques ou publiées sur papier.
*	Si votre tutoriel a vocation d'être un tutoriel d'analyse, vous devez vous référer à la littérature savante publiée du domaine. 
*	Pour signaler une note de fin, placer le chiffre en exposant (appel de note) à l'endroit souhaité sans espacement après le mot. Le cas échéant, veiller à ce qu'il précède un point de ponctuation et non pas qu'il le suive. Par exemple, pour insérer une note de fin imaginaire dans cette phrase, le chiffre en exposant doit se placer avant le point final comme ceci². Mais il ne peut pas être placé de cette manière.²
*   Pour les notes de fin, merci d'utiliser le style de citation [*The Chicago Manual of Style*, 17e édition](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html) en tenant compte des règles typographiques de la langue française.

#### Formatage du texte pour renvoyer à une note

Vous avez du texte ici[^1].
Et vous avez un peu plus de texte ici[^2].

##### Notes de fin
[^1]: Référence utilisant le style Chicago Manual 
[^2]: Référence utilisant le style Chicago Manual 


# Avez-vous plus de questions?

Votre rédacteur/rédactrice se fera un plaisir de répondre à toute question que vous pouvez avoir.
