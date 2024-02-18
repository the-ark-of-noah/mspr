import pandas as pd

# Chemin du fichier
file_path = "../../data/raw/2021_niveau_de_vie.xlsx"

# Chargement du dataset
df = pd.read_excel(file_path, skiprows=3)

# Sélection des colonnes souhaitées
colonnes_a_garder = [
    'Code',
    'Nb de ménages fiscaux 2021',
    'Médiane du niveau de vie 2021',
    'Part des minima sociaux dans le rev. disp. 2021',
    'Part des prestations familiales dans le rev. disp. 2021',
    'Part des prestations sociales dans le rev. disp. 2021',
    'Part des prestations logement dans le rev. disp. 2021',
    'Part des indemnités de chômage dans le rev. disp. 2021'
]

# Filtrage du dataframe pour ne garder que les colonnes souhaitées
df_filtre = df[colonnes_a_garder]

# Suppression des lignes avec des valeurs manquantes
df_filtre = df_filtre.dropna()

# Suppresion des DROM-TOM
df_filtre = df_filtre[~df_filtre["Code"].isin(['971', '972', '973', '974', '976'])]

# Convertir et ajuster les numéros pour la Corse
df_filtre["Code"] = df_filtre["Code"].replace({'2A': "201", '2B': "202"})

print(df_filtre.dtypes)

# Sauvegarder le DataFrame combiné
output_path = "../../data/processed/niveau_de_vie_par_departement_2021.csv"
df_filtre.to_csv(output_path, index=False)

df_filtre.head()
