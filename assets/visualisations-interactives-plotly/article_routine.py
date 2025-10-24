# BLOC 1 =======================================================================
# Imports 
import numpy as np
import pandas as pd
import plotly.express as px
# Importing for saving the html files
from images_interactives.save import save_html
# END BLOC 1 ===================================================================

# BLOC 2 =======================================================================
colonnes : list[str] = ["Année","Origine sociale","Nombre de personnes admises",
    "Proportion de personnes admises","Type de baccalauréat"]

df : pd.DataFrame = pd.read_csv("data_article.csv",usecols = colonnes)

# On raccourcit le nom de chaque colonne
nouvelles_colonnes = {
    "Année" : "annee",
    "Origine sociale" : "origine_sociale",
    "Nombre de personnes admises" : "n_admis",
    "Proportion de personnes admises" : "p_admis",
    "Type de baccalauréat" : "type"
}
df.rename(nouvelles_colonnes, axis = 1, inplace = True)

# On raccourcit le nom de certaines origines sociales pour alléger les visualisations
df["origine_sociale"] = df["origine_sociale"].replace({
    "Professions intermédiaires" : "P. intermédiaires",
    "Cadres, professions intellectuelles supérieures" : "Cadres",
    "Autres personnes sans activité professionnelle" : "Sans activité p.",
    "Artisans, commerçants, chefs d'entreprise" : "Indépendants",
    "Agriculteurs exploitants" : "Agriculteurs",
})

# On raccourcit le nom des types de bacs
df["type"] = df["type"].replace({
    "baccalaureat général" : "bac_g",
    "baccalauréat technologique" : "bac_t",
    "baccalauréat professionnel" : "bac_p",
    "baccalauréat" : "bac_tous",
})

# On supprime les lignes associées aux origines sociales que l'on souhaite écarter 
# pour cette leçon.
df.drop(df[
        (df["origine_sociale"] == "Ensemble") | \
        (df["origine_sociale"] == "Indéterminé") 
    ].index, inplace = True)
# END BLOC 2 ===================================================================

# BLOC 3 =======================================================================
# Création d'un nouveau DataFrame
num_admis_par_origine_sociale_2024 = df.loc[
    (df["annee"] == 2024)&(df["type"] == "bac_tous"), ["origine_sociale", "n_admis"]
]
print(num_admis_par_origine_sociale_2024)
# END BLOC 3 ===================================================================

# BLOC 4 =======================================================================
# Créer le diagramme en barres (bar chart) en utilisant la fonction .bar()
fig = px.bar(num_admis_par_origine_sociale_2024, x = "origine_sociale", y = "n_admis")

# Affiche la figure en utilisant la méthode .show()
# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-01.png")
save_html(fig, 1, "./images_interactives/fr-tr-visualisations-interactives-plotly-01.html")
# END BLOC 4 ===================================================================

# BLOC 5 =======================================================================
# Créer un diagramme en barres en utilisant la fonction .bar()
fig = px.bar(
    num_admis_par_origine_sociale_2024,
    x="origine_sociale",
    y="n_admis",
    title="Titre de votre choix",
    labels={"n_admis": "Nombre de personnes admises au baccalauréat"},

    # Notez que l'argument "color" prend une chaîne de caractères se référant à 
    # la colonne "origine_sociale" du jeu de données
    color="origine_sociale"
)

# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-02.png")
save_html(fig,2, "./images_interactives/fr-tr-visualisations-interactives-plotly-02.html")
# END BLOC 5 ===================================================================

# BLOC 6 =======================================================================
# Créer un nouveau DataFrame contenant le pourcentage d'admis au 
# baccalauréat (tous types confondus) par origine sociale et par année
prop_admis_par_origine_sociale_par_annee = df.loc[
    df["type"] == "bac_tous", ["annee", "origine_sociale", "p_admis"]
]
# END BLOC 6 ===================================================================

# BLOC 7 =======================================================================
# Créer des courbes avec la fonction px.line() et ajouter quelques éléments de 
# personnalisation
fig = px.line(
    prop_admis_par_origine_sociale_par_annee,
    x = "annee",
    y = "p_admis",
    # title = "Ajouter le titre de votre choix",
    labels = {"p_admis" : "Proportion de personnes admises au baccalauréat"},
    color = "origine_sociale"
)

# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-03.png")
save_html(fig,3, "./images_interactives/fr-tr-visualisations-interactives-plotly-03.html")
# END BLOC 7 ===================================================================

# BLOC 8 =======================================================================
fig.update_layout(
    font_family = "Courrier New",   # Modification de la police
    font_color = "blue",            # Modification de la couleur du texte
    legend_title_font_color = "red",# Modification de la couleur du titre de la légende
    title = "Un titre formaté"
)

# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-04.png")
save_html(fig,4, "./images_interactives/fr-tr-visualisations-interactives-plotly-04.html")
# END BLOC 8 ===================================================================

# BLOC 9 =======================================================================
num_admis_bac_t_bac_g = {
    "annee" : [], 
    "origine_sociale" : [],
    "n_admis_bac_g" : [],
    "n_admis_bac_t" : []
}

# Pour chaque combinaison d'année et origine sociale
for (annee, origine_sociale), _ in df.groupby(["annee", "origine_sociale"]):
    # On sauvegarde: l'année, l'origine sociale, le nombre de personnes admises 
    # au baccalauréat général et au baccalauréat technologique
    
    # Si l'origine sociale n'est pas dans la liste suivante, on passe à la prochaine.
    if origine_sociale not in ["Cadres", "Indépendants", "Ouvriers", "Agriculteurs"]:
        continue
    
    num_admis_bac_t_bac_g["annee"].append(annee)
    num_admis_bac_t_bac_g["origine_sociale"].append(origine_sociale)
    num_admis_bac_t_bac_g["n_admis_bac_g"].append(
        df.loc[
            (df["type"]=="bac_g")&\
            (df["annee"]==annee)&\
            (df["origine_sociale"]==origine_sociale),
            "n_admis"
        ].item()
    )
    num_admis_bac_t_bac_g["n_admis_bac_t"].append(
        df.loc[
            (df["type"]=="bac_t")&\
            (df["annee"]==annee)&\
            (df["origine_sociale"]==origine_sociale),
            "n_admis"
        ].item()
    )

# Transformons maintenant le dictionnaire en DataFrame.
num_admis_bac_t_bac_g = pd.DataFrame(num_admis_bac_t_bac_g)
print(num_admis_bac_t_bac_g)
# END BLOC 9 ===================================================================


# BLOC 10 ======================================================================
fig = px.scatter(
    num_admis_bac_t_bac_g,
    x="n_admis_bac_t",
    y="n_admis_bac_g",
    color = "origine_sociale"
    # title="Titre de votre choix",
)
# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-05.png")
save_html(fig,5, "./images_interactives/fr-tr-visualisations-interactives-plotly-05.html")
# END BLOC 10 ==================================================================

# BLOC 11 ======================================================================
lignes_bac_technologique_et_general_2024 = \
    ((df["type"] == "bac_t") | (df["type"] == "bac_g")) &\
    (df["annee"] == 2024) # (type = "bac_t" ou "bac_g") ET annee = 2024
type_bac_origine_sociales = df.\
    loc[lignes_bac_technologique_et_general_2024, :]

# Utiliser la fonction px.bar pour spécifier le type de représentation
fig = px.bar(
    type_bac_origine_sociales,
    x="origine_sociale",
    y="n_admis",
    # Utiliser le paramètre facet_col pour spécifier la colonne qui doit subdiviser
    facet_col="type", 
    color="origine_sociale",
    # title="Titre de votre choix",
)
# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-06.png")
save_html(fig,6, "./images_interactives/fr-tr-visualisations-interactives-plotly-06.html")
# END BLOC 11 ==================================================================

# BLOC 12 ======================================================================
num_admis_par_origine_sociale_par_annee = df.loc[
    df["type"] == "bac_tous", ["annee", "origine_sociale", "n_admis"]
]
# On utilise px.bar pour créer un diagramme en barres
fig = px.bar(
    num_admis_par_origine_sociale_par_annee,
    x="origine_sociale",
    y="n_admis",
    labels={"n_admis": "Nombre de personnes admises au baccalauréat"},
    range_y=[0,200_000],  # Le paramètre range_y permet de personnaliser l'intervalle de l'axe y 
    color="origine_sociale",
    # title="Titre de votre choix",
    # Utiliser le paramètre animation_frame pour spécfier l'axe d'évolution
    animation_frame="annee", 
)
# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-07.png")
save_html(fig,7, "./images_interactives/fr-tr-visualisations-interactives-plotly-07.html")
# END BLOC 12 ==================================================================

# BLOC 13 ======================================================================
fig = px.scatter(
    num_admis_bac_t_bac_g,
    x="n_admis_bac_t",
    y="n_admis_bac_g",
    color="origine_sociale", 
    # title="Titre de votre choix",
    labels = {
        "n_admis_bac_t" : "Nombre de personnes admises au baccalauréat technologique",
        "n_admis_bac_g" : "Nombre de personnes admises au baccalauréat général"
    }
)
# END BLOC 13 ==================================================================

# BLOC 14 ======================================================================
# Nous utilisons la méthode .update_layout pour ajouter le menu déroulant
fig.update_layout(
    updatemenus = [dict(
        buttons = [
            # Création de la liste de dictionaires pour chaque bouton du menu déroulant.
            dict(
                label = "Toutes les origines sociales", # Nom pour la première vue
                method = "update",
                args = [
                    # Cette vue montre les 4 origines sociales
                    {"visible" : [True, True, True, True]},
                    {
                        "title" : "Toutes les origines sociales",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                            }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
            dict(
                label = "Agriculteurs", # Nom pour la deuxième vue
                method = "update",
                args = [
                    # Cette vue montre seulement la première origine sociale
                    {"visible" : [True, False, False, False]}, 
                    {
                        "title" : "Agriculteurs",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                            }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
            dict(
                label = "Cadres", # Nom pour la troisième vue
                method = "update",
                args = [
                    # Cette vue montre uniquement la deuxième origine sociale
                    {"visible" : [False, True, False, False]}, 
                    {
                        "title" : "Cadres",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                            }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
            dict(
                label = "Indépendants", # Nom pour la quatrième vue
                method = "update",
                args = [
                    # Cette vue montre la 3è origine sociale
                    {"visible" : [False, False, True, False]},
                    {
                        "title" : "Indépendants",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                                }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
            dict(
                label = "Ouvriers", # Nom pour la cinquième vue
                method = "update",
                args = [
                    # Cette vue montre la 4è origine sociale
                    {"visible" : [False, False, False, True]},
                    {
                        "title" : "Ouvriers",
                        "xaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat technologique")
                            }
                        },
                        "yaxis" : {
                            "title" : {
                                "text" : ("Nombre de personnes admises au"
                                              " baccalauréat général")
                            }
                        }
                    }
                ]
            ),
        ]
    )]
)

# fig.show()
fig.update_layout(width = 1000,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-08.png")
save_html(fig,8, "./images_interactives/fr-tr-visualisations-interactives-plotly-08.html")
# END BLOC 14 ==================================================================

# BLOC 15 ======================================================================
import plotly.graph_objects as go 
# END BLOC 15 ==================================================================

# BLOC 16 ======================================================================
# Résultat du type de la figure
print(type(fig))
# END BLOC 16 ==================================================================

# BLOC 17 ======================================================================
print(fig.to_json(pretty = True)[0:500] + "\n...")
# END BLOC 17 ==================================================================

# BLOC 18 ======================================================================
num_admis_par_origine_sociale_2024 = df.loc[
    (df["annee"] == 2024)&(df["type"] == "bac_tous"), ["origine_sociale", "n_admis"]
]
# END BLOC 18 ==================================================================

# BLOC 19 ======================================================================
fig = go.Figure(
    # Utiliser go.Bar() pour spécifier le type de représentation à créer
    go.Bar(
        x = num_admis_par_origine_sociale_2024["n_admis"], 
        y = num_admis_par_origine_sociale_2024["origine_sociale"],
        orientation = "h",
        # Nous devons formatter le "hover text" alors que c'est automatique avec plotly.px
        hovertemplate = ("Origine Sociale : %{y}<br>"
                         "Nombre de personnes admises : %{x}"
                         "<extra></extra>"  )
    ),
    # layout = {"title" : "Ajouter le titre de votre choix"},
)

fig.update_layout(
    # Nous devons modifier le layout pour les titres d'axes alors que c'est automatique avec plotly.px
    xaxis = {"title" : ("Nombre de personnes admises au baccalauréat (tous "
                        "types confondus)")},
    yaxis = {"title" : "Origine Sociale"}
)

# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-09.png")
save_html(fig,9, "./images_interactives/fr-tr-visualisations-interactives-plotly-09.html")
# END BLOC 19 ==================================================================

# BLOC 20 ======================================================================
fig = px.bar(
    num_admis_par_origine_sociale_2024,
    x = "n_admis", y = "origine_sociale",
    orientation = "h",
    #title = "Titre de votre choix",
    labels = {"n_admis" : ("Nombre de personnes admises au baccalauréat (tous "
                           "types confondus)")}
)
# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-10.png")
save_html(fig,10, "./images_interactives/fr-tr-visualisations-interactives-plotly-10.html")
# END BLOC 20 ==================================================================

# BLOC 21 ======================================================================
fig = go.Figure(
    data = [
        go.Table(
            header = {
                "values" : df.columns,
                "fill_color" : "paleturquoise",
                "align" : "left"
            },
            cells = {
                "values" : df.transpose().values.tolist(),
                "fill_color" : "lavender",
                "align" : "left"
            }
        )
    ]
)

# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-11.png")
save_html(fig,11, "./images_interactives/fr-tr-visualisations-interactives-plotly-11.html")
# END BLOC 21 ==================================================================

# BLOC 22 ======================================================================
# Importer make_subplots
from plotly.subplots import make_subplots

# Préparation des données
num_admis_par_origine_sociale = df.\
    groupby(["type", "annee"]).\
    get_group(("bac_tous", 2024))

# On ne garde que 4 origines sociales pour alléger le graphe
selection_origines_sociales = np.isin(
    df["origine_sociale"], 
    ["Cadres", "Indépendants", "Ouvriers", "Agriculteurs"]
)
prop_admis_par_origine_sociale_par_annee = df.\
    loc[selection_origines_sociales, :].\
    groupby("type").get_group("bac_tous")

pourcentage_reussite_par_type_de_bac = df.\
    loc[df["type"] != "bac_tous",["type", "p_admis"]].\
    groupby("type")
# END BLOC 22 ==================================================================

# BLOC 23 ======================================================================
# 1 ligne, 3 colonnes
fig = make_subplots(rows = 1, cols = 3)
# END BLOC 23 ==================================================================

# BLOC 24 ======================================================================
fig.add_trace(
    # Utiliser go.Bar() pour spécifier le type de représentation
    go.Bar(
        x = num_admis_par_origine_sociale["n_admis"],
        y = num_admis_par_origine_sociale["origine_sociale"],
        orientation = "h",
        name = "Nombre de personnes admises au baccalauréat",
        hovertemplate = ("<b>Origine sociale :</b> %{y}<br><b>Nombre de personnes "
                        "ayant obtenu le bac</b> : %{x}<extra></extra>")
    ),
    # Les paramètres row et col permettent de positionner la figure dans la bonne case
    row = 1, col = 1 
)

fig.update_layout(width = 1200,height = 400)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-12.png")
save_html(fig,12, "./images_interactives/fr-tr-visualisations-interactives-plotly-12.html")
# END BLOC 24 ==================================================================

# BLOC 25 ======================================================================
# Pour chaque origine sociale il faut créer un objet go.Scatter différent afin de créer 
# les différentes courbes. 
# Pour se faire, on divise notre DataFrame par origine sociale et on procède comme 
# précédemment en ne travaillant qu'avec les sous-dataset
for origine_sociale, df_origine_sociale in prop_admis_par_origine_sociale_par_annee.\
                                    groupby("origine_sociale") :
    fig.add_trace(
        # Utiliser go.Scatter() pour spécifier le type de représentation
        go.Scatter(
            x = df_origine_sociale["annee"],
            y = df_origine_sociale["p_admis"],
            name = origine_sociale,
            mode = "markers+lines",
            hovertemplate = (f"<b>Origine sociale :</b> {origine_sociale}<br>"
                             "<b>Année :</b> %{x}<br>"
                             "<b>Proportion de personnes admises :</b> %{y}")  

        ),
        # Les paramètres row et col permettent de positionner la figure dans la bonne case
        row = 1, col = 2 
    )

# fig.show()
fig.update_layout(width = 1200,height = 400)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-13.png")
save_html(fig,13, "./images_interactives/fr-tr-visualisations-interactives-plotly-13.html")
# END BLOC 25 ==================================================================

# BLOC 26 ======================================================================
fig.add_trace(
    # Utiliser go.Box() pour spécifier le type de représentation
    go.Box(
        y = pourcentage_reussite_par_type_de_bac.\
            get_group("bac_g")["p_admis"],
        name = "Baccalauréat général"),
        row = 1, col = 3 # puisque c'est la troisième, on le met sur la 3è colonne
)

# On ajoute le deuxième et troisiéme diagramme en boîte puisqu'on a 3 groupes 
# distincts pour chaque type de baccalauréat
fig.add_trace(
    go.Box(
        y = pourcentage_reussite_par_type_de_bac.\
            get_group("bac_t")["p_admis"],
        name = "Baccalauréat technologique"),
        row = 1, col = 3 # puisque c'est la troisième, on le met sur la 3è colonne
)

fig.add_trace(
    go.Box(
        y = pourcentage_reussite_par_type_de_bac.\
            get_group("bac_p")["p_admis"],
        name = "Baccalauréat professionnel"),
        row = 1, col = 3 # puisque c'est la troisième, on le met sur la 3è colonne
)

fig.update_layout(width = 1200,height = 400)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-14.png")
save_html(fig,14, "./images_interactives/fr-tr-visualisations-interactives-plotly-14.html")
# END BLOC 26 ==================================================================

# BLOC 27 ======================================================================
fig.update_layout(
    # Changement de la police d'écriture pour toute la figure
    font_family = "Times New Roman", 
    # Changement de la police d'écriture pour les notes hover
    hoverlabel_font_family = "Times New Roman", 
    # changement de la taille d'écriture pour les notes hover
    hoverlabel_font_size = 16, 
    # title_text = "Ajouter un titre ici", # Titre principal
    # Positionnement du titre principal au centre de la visualisation 
    # (note : le paramètre title_x ne prend que des entiers (integers) 
    # ou des réels (floats))
    # title_x = 0.5 
    # ajout d'un titre d'axe pour l'absisse de la première figure
    xaxis1_title_text = ("Nombre de personnes admises au baccalauréat <br>(tous "
                         "types confondus) en 2024"),
    # ajout d'un titre d'axe pour les ordonnées de la première figure
    yaxis1_title_text = "Origine sociale", 
    yaxis2_title_text = ("Part de personnes admises au baccalauréat (tous types"
                         " confondus)"),
    xaxis2_title_text = "Année",
    yaxis3_title_text = "Distribution du pourcentage d'admission au baccalauréat",
    showlegend = False, # Retire la légende
    # Ajuste la taille de la visualisation  - pas toujours nécessaire mais peut 
    # s'avérer utile si les figures sont publiées sur internet
    height = 650
)

fig.update_layout(width = 1200)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-15.png")
save_html(fig,15, "./images_interactives/fr-tr-visualisations-interactives-plotly-15.html")
# END BLOC 27 ==================================================================

# BLOC 28 ======================================================================
fig.update_layout(
    # annotations reçoit une liste de disctionnaires, un dictionnaire = une annotation
    annotations = [
        # Notre première annotation sera pour identifier l'origine sociale "Agriculteurs"
        dict(
            # coordonnées du points de référence de l'annotation
            x = 2000, y = 85,
            # Spécifie dans quel référentiel on se place, ici comme on annote la
            # figure n°2 on donne comme référence x2, y2
            xref = "x2", yref = "y2",
            # Permet de spécifier la longueur de la flèche, et donc le décalage du 
            # texte par rapport au point
            ax = 0, ay = -100,
            text = "Agriculteurs",
            showarrow = True, # Utilisez False si vous ne voulez pas de la tête
            # de flèche dans l'annotation
            arrowhead = 1, # change la taille de la tête de flèche
        ),
        # Notre deuxième annotation sera pour identifier l'origine sociale "Indépendants"
        dict(
            x = 2001, y = 78.99,
            xref = "x2", yref = "y2",ax = 130, ay = 30,
            text = "Indépendants",showarrow = True, arrowhead = 1, 
        ),
        # Notre troisième annotation sera pour identifier l'origine sociale "Ouvriers"
        dict(
            x = 2019, y = 85.40,
            xref = "x2", yref = "y2",ax = 10, ay = 50,
            text = "Ouvriers",showarrow = True, arrowhead = 1, 
        ),
        # Notre quatrième annotation sera pour identifier l'origine sociale "Cadres"
        dict(
            x = 2020, y = 98.25,
            xref = "x2", yref = "y2",ax = -100, ay = 0,
            text = "Cadres",showarrow = True, arrowhead = 1, 
        ),
    ]
)

fig.update_layout(width = 1200,height = 650)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-16.png")
save_html(fig,16, "./images_interactives/fr-tr-visualisations-interactives-plotly-16.html")
# END BLOC 28 ==================================================================

# BLOC 29 ======================================================================
fig.add_annotation(
    dict(
        font=dict(color="black", size=15),  # Change la police d'écriture
        x=0.5,  # Utilise x et y pour la position de l'annotation
        y=-0.4,
        showarrow=False,
        text=(
            "Nombre de personnes admises au baccalauréat (tous types confondus)"
            " en 2024 et par origine sociale (gauche); <br>"
            "Proportion de personnes admises au baccalauréat (tous types"
            " confondus) à travers les années et par origine sociale (centre);<br>"
            "Distribution du pourcentage d'admission pour le baccalauréat général,"
            " technologique et professionnel (droite)."),
        # Option pour changer l'orientation de l'écriture, utile pour la gestion de l'espace
        textangle=0,  
        xanchor="center",
        # Régler xref et yref à 'paper' pour que les valeurs de x et y soient 
        # des coordonées absolues
        xref="paper",  
        yref="paper",
    )
)
# On ajoute une marge pour que laisser la place aux annotations
fig.update_layout(margin = {"b" : 200})

fig.update_layout(width = 1200,height = 650)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-17.png")
save_html(fig,17, "./images_interactives/fr-tr-visualisations-interactives-plotly-17.html")
# END BLOC 29 ==================================================================

# BLOC 30 ======================================================================
fig = px.line(
    prop_admis_par_origine_sociale_par_annee,
    x = "annee",
    y = "p_admis",
    # title = "Ajouter le titre de votre choix",
    labels = {"p_admis" : "Proportion de personnes admises au baccalauréat"},
    color = "origine_sociale"
)
# END BLOC 30 ==================================================================

# BLOC 31 ======================================================================
# fig.show()
fig.update_layout(width = 800,height = 600)
fig.write_image("./images_statiques/fr-tr-visualisations-interactives-plotly-18.png")
save_html(fig,18, "./images_interactives/fr-tr-visualisations-interactives-plotly-18.html")
# END BLOC 31 ==================================================================

# BLOC 32 ======================================================================
# Sauvegarde de la visualisation en format HTML
# fig.write_html("nom_visualisation.html")
# END BLOC 32 ==================================================================

# BLOC 33 ======================================================================
# Export en images classiques (raster):
# fig.write_image("nom_visualisation.png")
# fig.write_image("nom_visualisation.jpeg")

# Export en images vectorielles :
# fig.write_image("nom_visualisation.svg")
# fig.write_image("nom_visualisation.pdf")
# END BLOC 33 ==================================================================