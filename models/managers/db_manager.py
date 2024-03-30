import psycopg2
from src.data.utils.constants import conn_params


def connect_to_bdd():
    try:
        conn = psycopg2.connect(
            host=str(conn_params["host"]),
            port=str(conn_params["port"]),
            database=str(conn_params["database"]),
            user=str(conn_params["user"]),
            password=str(conn_params["password"])
        )
        return conn

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à PostgreSQL:", error)
        return None