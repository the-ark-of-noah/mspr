from sqlalchemy import create_engine
import pandas as pd

# Paramètres de connexion à la base de données PostgreSQL
database_url = "postgresql://admin:admin@localhost:15432/postgres"

engine = create_engine(database_url)


def query_db(query):
    """
    Exécute une requête SQL et retourne les résultats sous forme de DataFrame.
    Gère explicitement la création et la fermeture de la connexion à la base de données.
    """
    with engine.connect() as conn:
        return pd.read_sql_query(query, conn)
