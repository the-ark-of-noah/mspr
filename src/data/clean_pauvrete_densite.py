import pandas as pd

def renameColumnsAndCorseFix():
    filename =  "filosofi.csv"
    filepath = "../../datasets/"
    df = pd.read_csv(filepath + filename, delimiter=',')
    df = df.rename(columns={'codgeo': 'code_postal', 'libgeo': 'departement'})
    print(df.dtypes)
    df['code_postal'] = df['code_postal'].replace({'2A': 201, '2B': 202})
    df.to_csv(filepath + "modifie_" + filename)