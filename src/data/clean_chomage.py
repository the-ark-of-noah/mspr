import sys
import pandas as pd


def main():
    clean_data()


def clean_data():
    folder_path = "../../data/raw/"
    file = open(f"{folder_path}taux_de_chomage.xls", "rb")
    data = pd.read_excel(file, sheet_name="Département", header=3)
    years = range(1982, 2024)

    # Convertit en majuscules et supprime les espaces
    data["Libellé"] = data["Libellé"].str.upper().str.strip()

    # Supprime les colonnes inutiles, dont les DROM-TOM
    data = data.iloc[:-8]

    # Préparation du DataFrame résultant
    result = pd.DataFrame(data=data["Libellé"].rename("departement"))

    for year in years:
        avg = calculate_avg(data, year)
        result[f"avg_{year}"] = avg

    print(result.dtypes)
    write_to_csv(result, "moyenne_taux_chomage_par_departement_1982_2023")


def calculate_avg(data: pd.DataFrame, year):
    df = pd.DataFrame()
    for i in range(1, 5):
        column = f"T{i}_{year}"
        if column in data.columns:
            df[column] = data[column]

    avg = df.mean(axis=1)  # Moyenne pour les 4 trimestres
    return round(avg, 2)


def write_to_csv(data: pd.DataFrame, file_name: str):
    folder_path = "../../data/processed/"
    data.to_csv(f"{folder_path}{file_name}.csv", index=False)


if __name__ == '__main__':
    sys.exit(main())
