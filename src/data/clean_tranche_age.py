import sys
import pandas as pd

def main():
    clean_data()


def clean_data():
    folder_path = "../../data/raw/"
    file = open(f"{folder_path}tranche_dage_2020-2023.csv", "rb")
    data = pd.read_csv(file, sep=";", header=2, encoding="utf-8")
    labels = data["Libellé"]
    n = 100

    # print(data.columns)

    # clean 2020 data
    data = data[data["Part des pers. âgées de - de 25 ans 2020"].apply(lambda x: is_float(x))]
    data = data[data["Part des pers. âgées de 25 à 64 ans 2020"].apply(lambda x: is_float(x))]
    data = data[data["Part des pers. âgées de 65 ans ou + 2020"].apply(lambda x: is_float(x))]

    # clean 2023 data
    pd.to_numeric(data["Estimations de population : part des 0 à 24 ans 2023"], errors="coerce")
    pd.to_numeric(data["Estimations de population : part des 25 à 59 ans 2023"], errors="coerce")
    pd.to_numeric(data["Estimations de population : part des 60 ans ou plus 2023"], errors="coerce")

    # encode label column correctly using utf-8
    data["Libellé"] = labels.str.encode("utf-8").str.decode("utf-8")


    # merge columns by age range
    # # data_less255 = data[["Part des pers. âgées de - de 25 ans 2020", "Estimations de population : part des 0 à 24 ans 2023"]]
    # data_less255 = data["Part des pers. âgées de - de 25 ans 2020"] + data["Estimations de population : part des 0 à 24 ans 2023"]



    print(data.columns)
    write_to_csv(data, "tranche_dage_2023")


def write_to_csv(data: pd.DataFrame, file_name: str):
    folder_path = "../../data/processed/"
    data.to_csv(f"{folder_path}{file_name}.csv", index=False, sep=";", encoding="utf-8")

def is_float(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    sys.exit(main())
