import pandas as pd

file_path = "../../data/raw/2021_2022_immigre_departement.xlsx"

# Charger les feuilles avec les corrections sur les noms de colonnes
df_immigres = pd.read_excel(file_path, sheet_name="Figure 1", skiprows=2, usecols=["Numéro du département", "Libellé du département", "Part d'immigrés "]) # Ajout d'un espace, car le nom n'est pas correct
df_descendants = pd.read_excel(file_path, sheet_name="Figure 2", skiprows=2, usecols=["Numéro du département", "Libellé du département", "Part de descendants d’immigrés"])

# Renommer les colonnes pour la clarté
df_immigres.rename(columns={"Part d'immigrés ": "Part_immigres"}, inplace=True)
df_descendants.rename(columns={"Part de descendants d’immigrés": "Part_descendants_immigres"}, inplace=True)

# Fusionner les DataFrames sur les colonnes communes
df_combined = pd.merge(df_immigres, df_descendants, on=["Numéro du département", "Libellé du département"])

# Renommer les colonnes pour la clarté
df_combined = df_combined.rename(columns={"Numéro du département": "Code_departement", "Libellé du département": "Nom_departement"})

# Suppresion des DROM-TOM
df_combined = df_combined[~df_combined["Code_departement"].isin(['971', '972', '973', '974', 'France hors Mayotte'])]

# Convertir et ajuster les numéros pour la Corse
df_combined["Code_departement"] = df_combined["Code_departement"].replace({'2A': "201", '2B': "202"})

print(df_combined.dtypes)

# Sauvegarder le DataFrame combiné
output_path = "../../data/processed/immigres_et_descendants_par_departement_2020_2021.csv"
df_combined.to_csv(output_path, index=False)

print("Les DROM-TOM ont été correctement exclus et le fichier a été sauvegardé avec succès.")
