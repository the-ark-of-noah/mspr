import pandas as pd

# Try reading the file with ISO-8859-1 encoding
df = pd.read_csv('../../data/raw/2016_2023_delinquance.csv', low_memory=False, encoding='ISO-8859-1', decimal=',')

# Remove the columns that are not useful
columns_to_remove = [
    "Unnamed: 4",
    "millPOP",
    "millLOG",
    "POP",
    "LOG"
]
df = df.drop(columns=columns_to_remove)

# Rename the columns
df = df.rename(columns={"Unnamed: 2": "code_postal"})
df = df.rename(columns={"Unnamed: 3": "code_region"})
df = df.rename(columns={"tauxpourmille": "tauxpourcent"})

# Convert 'code_postal' to int
# Replace '2A' with 201 and '2B' with 202 for conversion to int
df['code_postal'] = df['code_postal'].replace({'2A': 201, '2B': 202})

# Fill NaN values with 0
df['code_postal'] = df['code_postal'].fillna(0)

# Convert 'code_postal' to int
df['code_postal'] = df['code_postal'].astype(int)

# Filter out 'code_postal' values greater than 95 and more than 0
df = df.loc[df['code_postal'] <= 95]
df = df.loc[df['code_postal'] > 0]

# Convert code_postal value to double digit
df['code_postal'] = df['code_postal'].astype(str).apply(lambda x: x.zfill(2))

output_path = "../../data/processed/delinquance_cleaned.csv"
df.to_csv(output_path, index=False)

print("Le fichier délinquance a été sauvegardé avec succès.")
