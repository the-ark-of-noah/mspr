import pandas as pd

# Importing necessary functions from the project's modules
from src.data.utils.map_parties import replace_candidate_names_with_parties
from src.data.utils.write_to_csv import write_to_csv
from src.data.utils.constants import party_dict
from src.data.utils.constants import rename_election_columns


# Function to load data from a CSV file into a pandas DataFrame
def load_data(filepath):
    try:
        df = pd.read_csv(filepath, low_memory=False, sep=';', on_bad_lines='skip')
        print(f"Le fichier {filepath} a été chargé avec succès.")
        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {filepath}: {e}")
        return pd.DataFrame()  # Retourne un DataFrame vide en cas d'erreur


# Function to remove specified columns from the DataFrame
def remove_columns(df, columns):
    df = df.drop(columns=columns)
    return df


# Function to rename the columns of the DataFrame based on the provided dictionary
def rename_columns(df, rename_dict):
    df = df.rename(columns=rename_dict)
    return df


# Function to convert the postal codes in the DataFrame
def convert_code_postal(df):
    df['code_postal'] = df['code_postal'].replace({'2A': 201, '2B': 202})
    df['code_postal'] = df['code_postal'].astype(str).apply(lambda x: x.zfill(2))
    return df


# Cette fonction n'est pas utile car nous souhaitons conserver les 0 à gauche de ces colonnes
# def convert_col_to_int(df):
#     df['code_postal'] = df['code_postal'].astype(int)
#     df['Bureau de vote'] = df['Bureau de vote'].astype(int)
#     df['Code Insee'] = df['Code Insee'].astype(int)
#     return df

def custom_format(x):
    # Vérifie si la valeur est flottante en détectant la présence d'un point décimal dans la représentation en chaîne
    if "." in str(x):
        # Remplace par '0001' si c'est une valeur flottante
        return '0001'
    else:
        # Conserve la valeur telle quelle si ce n'est pas une valeur flottante
        return str(x)


# Retour les pourcentage en type float
def convert_col_to_float(df):
    columns_to_convert = ['% Abs/Ins', '% Vot/Ins', '% Blancs/Ins', '% Nuls/Vot',
                          '% Nuls/Ins', '% Exp/Vot', '% Exp/Ins', '% Voix/Ins 1', '% Voix/Exp 1']

    for col in columns_to_convert:
        # Vérifie si la colonne est de type object (ou string), sinon saute la conversion
        if df[col].dtype == 'object':
            df[col] = df[col].str.replace(',', '.').astype(float)
        else:
            # Optionnel : Afficher un message ou non si la colonne est déjà au bon format
            print(f"La colonne {col} est déjà au format numérique.")

    return df


# Function to exclude certain departments from the DataFrame based on the provided exclusion list
def exclude_departments(df, exclude_list, code_column='code_postal'):
    df_filtered = df[~df[code_column].isin(exclude_list)]
    return df_filtered


# Paths for both tour 1 and tour 2 files
filepaths = ["../../../data/raw/2017_resultats_par_burvot_tour_1.csv",
             "../../../data/raw/2017_resultats_par_burvot_tour_2.csv"]
columns_to_remove = ["Code de la circonscription", "Circonscription", "Code de la commune", "Adresse", "Code Postal",
                     'Coordonnées', 'Nom Bureau Vote', 'Ville', 'uniq_bdv']
exclude_drom_tom = ["ZA", "ZB", "ZC", "ZD", "ZM", "ZN", "ZP", "ZS", "ZW", "ZX", "ZZ"]


def main():
    for filepath in filepaths:
        # Load the data
        df = load_data(filepath)
        # Remove unnecessary columns
        df = remove_columns(df, columns_to_remove)
        # Rename columns
        df = rename_columns(df, rename_election_columns)
        # Exclude certain departments
        df = exclude_departments(df, exclude_drom_tom, "code_postal")
        # Convert postal codes
        df = convert_code_postal(df)

        # Replace candidate names with parties
        df = replace_candidate_names_with_parties(df, party_dict)

        df['Bureau de vote'] = df['Bureau de vote'].apply(custom_format)
        # Convert columns to float
        df = convert_col_to_float(df)
        # Get the file name from the file path
        file_name = filepath.split('/')[-1]

        print(df.dtypes)
        # Write the cleaned data to a CSV file
        write_to_csv(df, file_name.replace('2017_resultats_par_burvot', '2017_elections').replace('.csv', '_cleaned'))


if __name__ == "__main__":
    main()
