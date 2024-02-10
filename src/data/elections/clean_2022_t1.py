import pandas as pd

from src.data.utils.map_departements import map_departement_code_to_name
from src.data.utils.map_parties import replace_candidate_names_with_parties
from src.data.utils.export_files import write_to_csv
from src.data.utils.constants import party_dict


def load_data(filepath):
    df = pd.read_csv(filepath, low_memory=False)
    print("Data loaded:", df.shape)
    return df


def remove_columns(df, columns):
    df = df.drop(columns=columns)
    print("Columns removed:", columns)
    return df


def rename_columns(df, rename_dict):
    df = df.rename(columns=rename_dict)
    print("Columns renamed:", list(rename_dict.values()))
    return df


def convert_code_postal(df):
    df['code_postal'] = df['code_postal'].replace({'2A': 201, '2B': 202}).astype(int)
    print("Postal codes converted.")
    return df


def exclude_departments(df, exclude_list, code_column='code_postal'):
    df_filtered = df[~df[code_column].isin(exclude_list)]
    print(f"Departments excluded. Remaining rows: {df_filtered.shape[0]}")
    return df_filtered


def main():
    filepath = "../../../data/raw/2022_resultats_par_burvot_tour_1.csv"
    columns_to_remove = ["Code de la circonscription", "Libellé de la circonscription", "Code de la commune"]
    exclude_drom_tom = ["ZA", "ZB", "ZC", "ZD", "ZM", "ZN", "ZP", "ZS", "ZW", "ZX", "ZZ"]
    rename_dict = {
        "Code du département": "code_postal",
        "Libellé du département": "departement"
    }

    df = load_data(filepath)
    df = remove_columns(df, columns_to_remove)
    df = rename_columns(df, rename_dict)
    # Assurez-vous d'exclure les départements d'outre-mer avant de convertir les codes postaux
    df = exclude_departments(df, exclude_drom_tom, "code_postal")
    df = convert_code_postal(df)
    df = map_departement_code_to_name(df)  # Mappage des codes de département
    df = replace_candidate_names_with_parties(df, party_dict)  # Mappage des noms de candidats

    print(df.head())  # Affiche les premières lignes pour vérifier le résultat
    write_to_csv(df, "2022_elections_t1_cleaned")


if __name__ == "__main__":
    main()
