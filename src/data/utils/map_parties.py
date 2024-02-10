def replace_candidate_names_with_parties(df, party_dict):
    # Remplace les noms des candidats par les noms de leurs partis dans un DataFrame.

    for candidate, party in party_dict.items():
        # Remplacer dans toutes les colonnes du DataFrame
        df = df.replace(candidate, party)

    return df
