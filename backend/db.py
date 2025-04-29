import duckdb
import pandas as pd

DB_PATH = "/data/movies.duckdb"  
def get_ratings():
    conn = duckdb.connect(database=DB_PATH, read_only=True)
    df = conn.execute("SELECT user_id, film_id, rating FROM ratings").fetchdf()
    conn.close()
    return df

def get_movies():
    conn = duckdb.connect(database=DB_PATH, read_only=True)
    df = conn.execute("SELECT id, title FROM films").fetchdf()
    conn.close()
    return df
