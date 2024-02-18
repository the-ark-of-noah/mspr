import pandas as pd

file_path = "../../data/raw/densite_population_depuis_1968.xlsx"

# Charger les feuilles avec les corrections sur les noms de colonnes
df_densite = pd.read_excel(file_path, skiprows=4)

# Renommer les colonnes pour la clarté
df_densite = df_densite.rename(columns={'codgeo': 'code_postal', 'libgeo': 'departement'})

print(df_densite.dtypes)

output_path = "../../data/processed/densite_population_depuis_1968.csv"
df_densite.to_csv(output_path, index=False)

print("Le fichier a été sauvegardé avec succès.")
