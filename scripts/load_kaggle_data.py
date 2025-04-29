import duckdb
import pandas as pd

ratings = pd.read_csv("data/ratings.csv")
con = duckdb.connect("data/base.duckdb")
con.execute("CREATE TABLE IF NOT EXISTS ratings AS SELECT * FROM ratings")