import pandas as pd
from utils.constants import departement_dict

df = pd.read_csv('../../data/raw/PIB par habitant.csv', low_memory=False, decimal=',')

# Inverser le dictionnaire pour obtenir un mapping des codes aux noms de département
code_departement_dict = {v: k for k, v in departement_dict.items()}

# Renommer la colonne 'Département' en 'departement'
df = df.rename(columns={'Département': 'departement'})

# Créer une nouvelle colonne 'code_departement' en utilisant le dictionnaire de correspondance
df['code_departement'] = df['departement'].map(code_departement_dict)

# Convertir et ajuster les numéros pour la Corse
df["code_departement"] = df["code_departement"].replace({'2A': "201", '2B': "202"})

# Renommer les colonnes "Année 2022", "Année 2015", "Année 2005" et "Année 2000"
df = df.rename(columns={"Année 2022": "2022", "Année 2015": "2015", "Année 2005": "2005", "Année 2000": "2000"})

# Supprimer la colonne "2015"
df = df.drop(columns=["2015"])

# Sauvegarde
output_path = "../../data/processed/pib_par_habitant.csv"
df.to_csv(output_path, index=False)

print("PIB par habitant sauvegardé avec succès")