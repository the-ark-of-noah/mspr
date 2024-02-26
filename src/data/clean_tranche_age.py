import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('../../data/raw/2020_2023_tranche_age.csv', low_memory=False, delimiter=';')

# Renommer les colonnes
column_to_rename = {
    "Libellé": "departement",
    "Code": "code_departement",
    "Part des pers. âgées de 65 ans ou + 2020": "65-99_2020",
    "Estimations de population : part des 60 ans ou plus 2023": "60-99_2023",
    "Estimations de population : part des 25 à 59 ans 2023": "25-59_2023",
    "Estimations de population : part des 0 à 24 ans 2023": "0-24_2023",
    "Part des pers. âgées de - de 25 ans 2020": "0-25_2020",
    "Part des pers. âgées de 25 à 64 ans 2020": "25-64_2020"
}

# Renommer les colonnes
df = df.rename(columns=column_to_rename)

# Convertir et ajuster les numéros pour la Corse
df["code_departement"] = df["code_departement"].replace({'2A': "201", '2B': "202"})

# Supprimer la ligne ayant le code département 971
df = df[df['code_departement'] != 971]

# Sauvegarde
output_path = "../../data/processed/tranche_age_cleaned.csv"
df.to_csv(output_path, index=False)

print("Tranche d'age sauvegardé avec succès")