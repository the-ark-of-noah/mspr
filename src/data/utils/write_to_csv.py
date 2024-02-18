import pandas as pd
from pathlib import Path


def write_to_csv(data: pd.DataFrame, file_name: str, folder_path="../../../data/processed/"):
    folder_path = Path(folder_path)
    if not folder_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Directory created: {folder_path}")

    # Construire le chemin complet du fichier CSV
    file_path = folder_path / f"{file_name}.csv"

    # Écrire le DataFrame dans un fichier CSV
    data.to_csv(file_path, index=False)
    print(f"Data written to {file_path}")
