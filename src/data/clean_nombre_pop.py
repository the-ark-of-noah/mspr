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

# Liste des colonnes à convertir en entier car elles sont numériques, et nous parlons du nombre de personnes
colonnes_a_convertir = ['2023 (p)', '2020', '2015', '2010', '1999']

# Conversion des colonnes
for colonne in colonnes_a_convertir:
    # Convertir en int après avoir remplacé les valeurs NaN pour éviter les erreurs
    df_nb_pop[colonne] = pd.to_numeric(df_nb_pop[colonne], errors='coerce').fillna(0).astype(int)

# Afficher les types pour vérification
print(df_nb_pop.dtypes)


output_path = "../../data/processed/population_par_departement_1999_2023.csv"
df_nb_pop.to_csv(output_path, index=False)

print("Le fichier a été sauvegardé avec succès.")
