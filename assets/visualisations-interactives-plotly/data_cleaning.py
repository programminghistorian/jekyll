"""
This file is cleaning data downloaded here : 
https://www.data.gouv.fr/fr/datasets/reussite-au-baccalaureat-selon-lorigine-sociale/
We first describe the errors and then correct them.
"""
# Imports
import pandas as pd
import numpy as np

# Open the dataset
raw_df : pd.DataFrame = pd.read_csv("data_baccalaureat_origine_sociale.csv",
                                    sep = ";")

# The unique origine_sociale are : 
print(raw_df["Origine sociale"].unique())
"""
>>> [
>>>     'Autres personnes sans activité professionnelle',
>>>     "Artisans, commerçants, chefs d'entreprise",
>>>     'Employés',
>>>     'Ensemble',
>>>     'Ouvriers',
>>>     'Agriculteurs exploitants',
>>>     'Retraités',
>>>     'Cadres, professions intellectuelles supérieures',
>>>     'Cadres, professions intellectuelles supérieures : professeurs et assimilés',
>>>     'Indéterminé',
>>>     'Professions intermédiaires : instituteurs et assimilés',
>>>     'Professions intermédiaires',
>>>     "Artisans, commerçants et chefs d'entreprise",
>>>     'Cadres et professions intellectuelles supérieures'
>>> ]
We can already spot some irregularities, such as "Cadres, professions 
intellectuelles supérieures" is appearing multiple times under different names. 
Same for "Professions intermédiaires"
"""

# The first objective is to merge the rows corresponding to the same year and 
# social background.
# We replace the names of the social backgrounds to get homogenous data.
origines_sociales_renommee = {
    'Employés' : "Employés",

    'Ensemble' : "Ensemble",
    
    'Ouvriers' : "Ouvriers",
    
    'Agriculteurs exploitants' : "Agriculteurs exploitants",
    
    'Retraités' : "Retraités",
    
    'Autres personnes sans activité professionnelle' : \
        "Autres personnes sans activité professionnelle",

    'Cadres, professions intellectuelles supérieures' : \
        "Cadres, professions intellectuelles supérieures",
    'Cadres, professions intellectuelles supérieures : professeurs et assimilés' :\
        "Cadres, professions intellectuelles supérieures",
    'Cadres et professions intellectuelles supérieures' : \
        "Cadres, professions intellectuelles supérieures",
    
    'Indéterminé' : "Indéterminé",

    'Professions intermédiaires : instituteurs et assimilés' :\
        "Professions intermédiaires",
    'Professions intermédiaires' : "Professions intermédiaires",

    "Artisans, commerçants et chefs d'entreprise" : \
        "Artisans, commerçants, chefs d'entreprise",
    "Artisans, commerçants, chefs d'entreprise" : \
        "Artisans, commerçants, chefs d'entreprise",
}
raw_df["Origine sociale"] = raw_df["Origine sociale"].replace(origines_sociales_renommee)

sizes = raw_df.groupby(["Origine sociale", "Année"]).size()
print(sizes[sizes != 1])
"""
>>> Origine sociale                                  Année
>>> Cadres, professions intellectuelles supérieures  1997     2
>>>                                                  1998     2
>>>                                                  1999     2
>>>                                                  2000     2
>>>                                                  2001     2
>>>                                                  2002     2
>>>                                                  2003     2
>>>                                                  2004     2
>>>                                                  2005     2
>>>                                                  2006     2
>>>                                                  2007     2
>>>                                                  2008     2
>>>                                                  2009     2
>>>                                                  2010     2
>>>                                                  2011     2
>>>                                                  2012     2
>>>                                                  2013     2
>>>                                                  2014     2
>>>                                                  2015     2
>>>                                                  2016     2
>>>                                                  2017     2
>>>                                                  2018     2
>>>                                                  2019     2
>>>                                                  2020     2
>>>                                                  2021     2
>>>                                                  2022     2
>>>                                                  2023     2
>>>                                                  2024     2
>>> Professions intermédiaires                       1997     2
>>>                                                  1998     2
>>>                                                  1999     2
>>>                                                  2000     2
>>>                                                  2001     2
>>>                                                  2002     2
>>>                                                  2003     2
>>>                                                  2004     2
>>>                                                  2005     2
>>>                                                  2006     2
>>>                                                  2007     2
>>>                                                  2008     2
>>>                                                  2009     2
>>>                                                  2010     2
>>>                                                  2011     2
>>>                                                  2012     2
>>>                                                  2013     2
>>>                                                  2014     2
>>>                                                  2015     2
>>>                                                  2016     2
>>>                                                  2017     2
>>>                                                  2018     2
>>>                                                  2019     2
>>>                                                  2020     2
>>>                                                  2021     2
>>>                                                  2022     2
>>>                                                  2023     2
>>>                                                  2024     2
"""

# The problem is that now, for each year and social background, we have 2 entries
# Given that the entries are: proportion of people being accepted and number of 
# people who took the test, we need to first evaluate the number of people who passed 
# in order to sum the entries together and re-evaluate the proportion of people 
# who passed.

allTypesOfBaccalaureat = [
    "baccalaureat général", 
    "baccalauréat technologique",
    "baccalauréat professionnel", "baccalauréat"
]
for typeOfBaccalaureat in  allTypesOfBaccalaureat: 
    # Num ppl passed = Num ppl took / (% ppl passed / 100)
    raw_df[f"Nombre de candidats au {typeOfBaccalaureat}"] = round(
        raw_df[f"Nombre d'admis au {typeOfBaccalaureat}"] / 
        (raw_df[f"Pourcentage d'admis au {typeOfBaccalaureat}"] / 100)
    )

# Now, for each social background, year and baccalaureat, we need to sum the 
# columns "Nombre d'admis au {bac}" and "{Nombre de candidats au {bac}"

def all_columns_to_aggregate():
    """Generator holding all the columns that will be aggregated
    i.e. "Nombre d'admis au {bac}" and "{Nombre de candidats au {bac}" for all
    bac
    """
    for typeOfBaccalaureat in allTypesOfBaccalaureat:
        yield f"Nombre d'admis au {typeOfBaccalaureat}" 
    for typeOfBaccalaureat in allTypesOfBaccalaureat:
        yield f"Nombre de candidats au {typeOfBaccalaureat}" 

aggregated_df : pd.DataFrame = raw_df.\
    groupby(["Origine sociale", "Année"], as_index = False).\
    agg(**{key : (key, "sum")for key in all_columns_to_aggregate()})

sizes = aggregated_df.groupby(["Origine sociale", "Année"]).size()
print(sizes[sizes != 1])
"""
>>> Series([], dtype: int64)
"""
# Data has been aggregated, for each social background, year and baccalaureat, we
# have one entry with the number of people who passed and the number of people 
# who took the test.

# Retrieve the proportion of people who passed
for typeOfBaccalaureat in  allTypesOfBaccalaureat: 
    # % ppl passed = 100 * Num ppl passed / Num ppl took
    aggregated_df[f"Pourcentage d'admis au {typeOfBaccalaureat}"] = \
        100 * aggregated_df[f"Nombre d'admis au {typeOfBaccalaureat}"] / \
        aggregated_df[f"Nombre de candidats au {typeOfBaccalaureat}"]
print(aggregated_df)
"""
>>>               Origine sociale  Année  ...  Pourcentage d'admis au baccalauréat professionnel  Pourcentage d'admis au baccalauréat
>>> 0    Agriculteurs exploitants   1997  ...                                          82.992502                            80.901420
>>> 1    Agriculteurs exploitants   1998  ...                                          82.304038                            82.900403
>>> 2    Agriculteurs exploitants   1999  ...                                          82.500905                            82.900283
>>> 3    Agriculteurs exploitants   2000  ...                                          85.493297                            85.000703
>>> 4    Agriculteurs exploitants   2001  ...                                          84.495856                            84.500988
>>> ..                        ...    ...  ...                                                ...                                  ...
>>> 275                 Retraités   2020  ...                                          87.990894                            93.497646
>>> 276                 Retraités   2021  ...                                          84.308511                            92.202462
>>> 277                 Retraités   2022  ...                                          80.298073                            88.903143
>>> 278                 Retraités   2023  ...                                          81.512605                            89.001560
>>> 279                 Retraités   2024  ...                                          81.015358                            89.097524
>>> 
>>> [280 rows x 14 columns]
"""
# The next issue, is that the categorie "Ensemble", supposed to aggregate all the
# social backgrounds for a given year, is not right. 
# Let's print a table comparing the data in the "Ensemble" categorie with the 
# data summed for a given year

# Pretty header
header = f"|{'Année':^6}|{'Nombre c Ensembles':^20}|{'Somme c':^20}|{'Error (%)':^20}|"
hline = "+" + "-" * (len(header)-2) + "+"
print(hline, header, hline, sep = "\n")

for year, subDF in aggregated_df.groupby("Année") : 
    # For a given year, retrieve the number of candidates to all the baccalaureats
    nCandidatesEnsemble : int = int(
        subDF.\
            loc[subDF["Origine sociale"] == "Ensemble", 
                "Nombre de candidats au baccalauréat"].\
            sum()
        )
    # sum the number of candidates from all different social background
    sumCandidates : int = int(
        subDF.\
            loc[subDF["Origine sociale"] != "Ensemble", 
                "Nombre de candidats au baccalauréat"].\
            sum()
        )
    # Evaluate the error
    error : float = 100 * abs(nCandidatesEnsemble - sumCandidates) / sumCandidates
    sign : str = '+' if nCandidatesEnsemble > sumCandidates else '-'
    print((
        f"|{year:^6}"
        f"|{nCandidatesEnsemble:^20}"
        f"|{sumCandidates:^20}"
        f"|{'%s%.2f'%(sign,error):^20}"
        f"|"
    ))
print(hline)
"""
>>> +---------------------------------------------------------------------+
>>> |Année | Nombre c Ensembles |      Somme c       |     Error (%)      |
>>> +---------------------------------------------------------------------+
>>> | 1997 |       623283       |       657851       |       -5.25        |
>>> | 1998 |       635635       |       670376       |       -5.18        |
>>> | 1999 |       643275       |       676738       |       -4.94        |
>>> | 2000 |       649748       |       682091       |       -4.74        |
>>> | 2001 |       635150       |       665808       |       -4.60        |
>>> | 2002 |       628186       |       657726       |       -4.49        |
>>> | 2003 |       627554       |       656396       |       -4.39        |
>>> | 2004 |       625310       |       652503       |       -4.17        |
>>> | 2005 |       634053       |       661362       |       -4.13        |
>>> | 2006 |       638315       |       665770       |       -4.12        |
>>> | 2007 |       628673       |       654126       |       -3.89        |
>>> | 2008 |       621431       |       646467       |       -3.87        |
>>> | 2009 |       625397       |       650616       |       -3.88        |
>>> | 2010 |       621224       |       645642       |       -3.78        |
>>> | 2011 |       664359       |       689291       |       -3.62        |
>>> | 2012 |       721724       |       746618       |       -3.33        |
>>> | 2013 |       678262       |       703532       |       -3.59        |
>>> | 2014 |       710966       |       736761       |       -3.50        |
>>> | 2015 |       704032       |       730806       |       -3.66        |
>>> | 2016 |       715008       |       742965       |       -3.76        |
>>> | 2017 |       732391       |       762532       |       -3.95        |
>>> | 2018 |       767899       |       798280       |       -3.81        |
>>> | 2019 |       759481       |       789891       |       -3.85        |
>>> | 2020 |       761022       |       795057       |       -4.28        |
>>> | 2021 |       735348       |       768261       |       -4.28        |
>>> | 2022 |       732791       |       766550       |       -4.40        |
>>> | 2023 |       744147       |       778872       |       -4.46        |
>>> | 2024 |       753237       |       789435       |       -4.59        |
>>> +---------------------------------------------------------------------+
"""
# It seems like the data is off by 3-5% for each year.
# To fix this, we are going to re-evaluate the data for the "Ensemble" category.

for year, subDF in aggregated_df.groupby("Année") : 
    # For each year
    isEnsemble : list[bool] = subDF["Origine sociale"] == "Ensemble"
    notEnsemble : list[bool] = subDF["Origine sociale"] != "Ensemble"

    for typeOfBaccalaureat in allTypesOfBaccalaureat : 
        # For each baccalaureat
        # Evaluate the number of people who took the test
        subDF.loc[isEnsemble, f"Nombre de candidats au {typeOfBaccalaureat}"] = \
            subDF.loc[notEnsemble, f"Nombre de candidats au {typeOfBaccalaureat}"].sum()
        
        # Evaluate the number of people who passed the test
        subDF.loc[isEnsemble, f"Nombre d'admis au {typeOfBaccalaureat}"] = \
            subDF.loc[notEnsemble, f"Nombre d'admis au {typeOfBaccalaureat}"].sum() 
        
        # Evaluate the proportion of people who passed
        subDF.loc[isEnsemble, f"Pourcentage d'admis au {typeOfBaccalaureat}"] = \
            100 * subDF.loc[isEnsemble, f"Nombre d'admis au {typeOfBaccalaureat}"] / \
            subDF.loc[isEnsemble, f"Nombre de candidats au {typeOfBaccalaureat}"] 
    
    aggregated_df.loc[aggregated_df["Année"] == year, :] = subDF

# Let's verify that we actually fixed the problem by printing the same table as 
# before   

# Pretty header
header = f"|{'Année':^6}|{'Nombre c Ensembles':^20}|{'Somme c':^20}|{'Error (%)':^20}|"
hline = "+" + "-" * (len(header)-2) + "+"
print(hline, header, hline, sep = "\n")

for year, subDF in aggregated_df.groupby("Année") : 
    # For a given year, retrieve the number of candidates to all the baccalaureats
    nCandidatesEnsemble : int = int(
        subDF.\
            loc[subDF["Origine sociale"] == "Ensemble", 
                "Nombre de candidats au baccalauréat"].\
            sum()
        )
    # sum the number of candidates from all different social background
    sumCandidates : int = int(
        subDF.\
            loc[subDF["Origine sociale"] != "Ensemble", 
                "Nombre de candidats au baccalauréat"].\
            sum()
        )
    # Evaluate the error
    error : float = 100 * abs(nCandidatesEnsemble - sumCandidates) / sumCandidates
    sign : str = '+' if nCandidatesEnsemble > sumCandidates else '-'
    print((
        f"|{year:^6}"
        f"|{nCandidatesEnsemble:^20}"
        f"|{sumCandidates:^20}"
        f"|{'%s%.2f'%(sign,error):^20}"
        f"|"
    ))
print(hline)
"""
>>> +---------------------------------------------------------------------+
>>> |Année | Nombre c Ensembles |      Somme c       |     Error (%)      |
>>> +---------------------------------------------------------------------+
>>> | 1997 |       657851       |       657851       |       -0.00        |
>>> | 1998 |       670376       |       670376       |       -0.00        |
>>> | 1999 |       676738       |       676738       |       -0.00        |
>>> | 2000 |       682091       |       682091       |       -0.00        |
>>> | 2001 |       665808       |       665808       |       -0.00        |
>>> | 2002 |       657726       |       657726       |       -0.00        |
>>> | 2003 |       656396       |       656396       |       -0.00        |
>>> | 2004 |       652503       |       652503       |       -0.00        |
>>> | 2005 |       661362       |       661362       |       -0.00        |
>>> | 2006 |       665770       |       665770       |       -0.00        |
>>> | 2007 |       654126       |       654126       |       -0.00        |
>>> | 2008 |       646467       |       646467       |       -0.00        |
>>> | 2009 |       650616       |       650616       |       -0.00        |
>>> | 2010 |       645642       |       645642       |       -0.00        |
>>> | 2011 |       689291       |       689291       |       -0.00        |
>>> | 2012 |       746618       |       746618       |       -0.00        |
>>> | 2013 |       703532       |       703532       |       -0.00        |
>>> | 2014 |       736761       |       736761       |       -0.00        |
>>> | 2015 |       730806       |       730806       |       -0.00        |
>>> | 2016 |       742965       |       742965       |       -0.00        |
>>> | 2017 |       762532       |       762532       |       -0.00        |
>>> | 2018 |       798280       |       798280       |       -0.00        |
>>> | 2019 |       789891       |       789891       |       -0.00        |
>>> | 2020 |       795057       |       795057       |       -0.00        |
>>> | 2021 |       768261       |       768261       |       -0.00        |
>>> | 2022 |       766550       |       766550       |       -0.00        |
>>> | 2023 |       778872       |       778872       |       -0.00        |
>>> | 2024 |       789435       |       789435       |       -0.00        |
>>> +---------------------------------------------------------------------+
"""

# We are going to reshape the table that is short and wide to a long and thin
# table. 
final_df = {
    "Année" : [],
    "Origine sociale" : [],
    "Nombre de personnes admises" : [],
    "Proportion de personnes admises" : [],
    "Type de baccalauréat" : []
}

# Puis pour chaque colonne, on y entre les données
for typeOfBaccalaureat in allTypesOfBaccalaureat: 
    final_df["Année"] +=  aggregated_df["Année"].to_list()
    final_df["Origine sociale"] +=  aggregated_df["Origine sociale"].to_list()
    final_df["Nombre de personnes admises"] +=  \
        aggregated_df[f"Nombre d'admis au {typeOfBaccalaureat}"].to_list()
    final_df["Proportion de personnes admises"] +=  \
        aggregated_df[f"Pourcentage d'admis au {typeOfBaccalaureat}"].to_list()
    # On ajoute un indicateur "type" pour repérer le type de baccalauréat
    final_df["Type de baccalauréat"] += [typeOfBaccalaureat] * len(aggregated_df)

final_df = pd.DataFrame(final_df)

# Save file 
final_df.to_csv("2025-07-16-data_article.csv", index = False)