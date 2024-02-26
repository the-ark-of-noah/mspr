import pandas as pd

df = pd.read_csv('../../data/raw/2020_taux_de_pauvrete.csv', low_memory=False, encoding='utf-8')

df = df.rename(columns={'codgeo': 'code_postal', 'libgeo': 'departement', 'tx_pauv_60': 'taux'})

# Supprimer les lignes ayant les codes postaux 971, 972 et 973
df = df[~df['code_postal'].isin(['971', '972', '973', '974', '976'])]

# Convertir la colonne 'an' en int
df['an'] = df['an'].astype(int)

df['code_postal'] = df['code_postal'].replace({'2A': 201, '2B': 202})

output_path = "../../data/processed/pauvreté_cleaned.csv"
df.to_csv(output_path, index=False)

print("Le fichier pauvreté a été sauvegardé avec succès.")
