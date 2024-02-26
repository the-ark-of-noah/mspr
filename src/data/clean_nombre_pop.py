import pandas as pd

# Chemin vers le fichier source
file_path = "../../data/raw/1999_2023_population_departement.xlsx"

# Sauter les 3 premières lignes pour atteindre les données
df_nb_pop = pd.read_excel(file_path, skiprows=3)
df_nb_pop = df_nb_pop.rename(columns={'Unnamed: 0': 'Code_departement', 'Unnamed: 1': 'Nom_departement'})

# Suppresion des colonnes inutiles
df_nb_pop = df_nb_pop[~df_nb_pop["Code_departement"].isin(
    ['971', '972', '973', '974', '976', 'F', '(p) estimations provisoires'])]

# Supprime la dernière ligne
df_nb_pop = df_nb_pop.iloc[:-1]

# Convertir et ajuster les numéros pour la Corse
df_nb_pop["Code_departement"] = df_nb_pop["Code_departement"].replace(
    {'2A': "201", '2B': "202", 'M': 'Moyenne métropolitaine'})

print(df_nb_pop.dtypes)

df_nb_pop = df_nb_pop.rename(columns={'Code_departement': 'code_postal', 'Nom_departement': 'departement', '2023 (p)': '2023'})

df_nb_pop = df_nb_pop[~df_nb_pop['code_postal'].isin(['Moyenne métropolitaine'])]

df_nb_pop['code_postal'] = df_nb_pop['code_postal'].astype(int)

output_path = "../../data/processed/population_par_departement_1999_2023.csv"
df_nb_pop.to_csv(output_path, index=False)

print("Le fichier a été sauvegardé avec succès.")
