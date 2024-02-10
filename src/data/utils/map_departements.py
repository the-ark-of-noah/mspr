from .constants import departement_dict


# Remplace les codes des départements par leurs noms dans un DataFrame.

def map_departement_code_to_name(df, code_column='code_postal'):
    df[code_column] = df[code_column].apply(lambda x: departement_dict.get(str(x), "Code inconnu"))
    return df
