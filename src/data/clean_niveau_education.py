import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('../../data/raw/2020_niveau_education.csv', low_memory=False)

# Drop columns
df.drop(columns=['Part des élèves du privé parmi les élèves du second degré 2021'], inplace=True)

# Rename columns
df.rename(columns={
    'Nb de pers. non scolarisées de 15 ans ou + 2020': 'Nombre de personne non scolarisé',
    'Part des diplômés d\'un BAC+5 ou plus dans la pop. non scolarisée de 15 ans ou + 2020': 'Part des diplômés d\'un BAC+5 ou plus dans la population non scolarisée',
    'Part des diplômés d\'un BAC+3  ou BAC+4 dans la pop. non scolarisée de 15 ans ou + 2020': 'Part des diplômés d\'un BAC+3 ou BAC+4 dans la population non scolarisée',
    'Part des diplômés d\'un BAC+2 dans la pop. non scolarisée de 15 ans ou + 2020': 'Part des diplômés d\'un BAC+2 dans la population non scolarisée',
    'Part des pers., dont le diplôme le plus élevé est le bac, dans la pop. non scolarisée de 15 ans ou + 2020': 'Part des personnes, dont le diplôme le plus élevé est le bac, dans la population non scolarisée',
    'Part des pers., dont le diplôme le plus élevé est un CAP ou un BEP, dans la pop. non scolarisée de 15 ans ou + 2020': 'Part des personne, dont le diplôme le plus élevé est un CAP ou un BEP, dans la population non scolarisée',
    'Code': 'code_postal',
    'Libellé': 'departement'
}, inplace=True)

# Supprimer les lignes avec les codes postaux 971 et 972
df = df[~df['code_postal'].isin(['971', '972', '973', '974', '976'])]

# Set age
df['Âge'] = '15-26'

new_rows = []

for index, row in df.iterrows():
    for col_name in df.columns[2:]:
        new_row = {
            'code_postal': row['code_postal'],
            'departement': row['departement'],
            'annee': 2020,
            'age': row['Âge'],
            'indicateur': col_name,
            'valeurs': row[col_name]
        }
        new_rows.append(new_row)

# Create new dataframe
new_df = pd.DataFrame(new_rows)

# Convertir les numéros pour la Corse
new_df["code_postal"] = new_df["code_postal"].replace(
    {'2A': "201", '2B': "202"})

new_df['code_postal'] = new_df['code_postal'].astype(int)

output_path = "../../data/processed/niveau_education.csv"
new_df.to_csv(output_path, index=False)

print("Le fichier niveau éducation a été sauvegardé avec succès.")
