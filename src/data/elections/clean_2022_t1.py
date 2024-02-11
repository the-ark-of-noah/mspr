import pandas as pd

# Importing necessary functions from the project's modules
from src.data.utils.map_parties import replace_candidate_names_with_parties
from src.data.utils.export_files import write_to_csv
from src.data.utils.constants import party_dict
from src.data.utils.constants import rename_election_columns


# Function to load data from a CSV file into a pandas DataFrame
def load_data(filepath):
    df = pd.read_csv(filepath, low_memory=False)
    return df


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
    df['code_postal'] = df['code_postal'].replace({'2A': 201, '2B': 202}).astype(int)
    df['code_postal'] = df['code_postal'].astype(str).apply(lambda x: x.zfill(2))
    return df


# Function to exclude certain departments from the DataFrame based on the provided exclusion list
def exclude_departments(df, exclude_list, code_column='code_postal'):
    df_filtered = df[~df[code_column].isin(exclude_list)]
    return df_filtered


# Function to rename unnamed columns in the DataFrame
def rename(df):
    new_column_names = [
        'N°Panneau',
        'Sexe',
        'Parti',
        'Prénom',
        'Voix',
        '% Voix/Ins',
        '% Voix/Exp'
    ]

    i = 28
    candidate_number = 2
    while i < 105:
        for new_name in new_column_names:
            old_name = "Unnamed: " + str(i)
            new_name_with_number = new_name + " " + str(candidate_number)
            df.rename(columns={old_name: new_name_with_number}, inplace=True)
            i += 1
        candidate_number += 1

    return df


# Function to remove columns that start with 'N°Panneau' from the DataFrame
def remove_column_by_name(df, column_name):
    columns_to_drop = [col for col in df.columns if col.startswith(column_name)]

    df = df.drop(columns=columns_to_drop)

    return df


# Main function that orchestrates the execution of the script
def main():
    # Paths for both tour 1 and tour 2 files
    filepaths = ["../../../data/raw/2022_resultats_par_burvot_tour_1.csv",
                 "../../../data/raw/2022_resultats_par_burvot_tour_2.csv"]
    columns_to_remove = ["Code de la circonscription", "Libellé de la circonscription", "Code de la commune"]
    exclude_drom_tom = ["ZA", "ZB", "ZC", "ZD", "ZM", "ZN", "ZP", "ZS", "ZW", "ZX", "ZZ"]

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
        # Rename unnamed columns
        df = rename(df)
        # Remove 'N°Panneau' columns
        df = remove_column_by_name(df, "N°Panneau")
        # Remove 'Prénom' columns
        df = remove_column_by_name(df, "Prénom")

        # Print the first few rows of the DataFrame to check the result
        print(df.head())

        # Get the file name from the file path
        file_name = filepath.split('/')[-1]

        # Write the cleaned data to a CSV file
        write_to_csv(df, file_name.replace('2022_resultats_par_burvot', '2022_elections').replace('.csv', '_cleaned'))


if __name__ == "__main__":
    main()
