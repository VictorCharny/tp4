from fastapi import FastAPI, HTTPException
from surprise import Dataset, Reader, SVD
import duckdb
import pandas as pd

app = FastAPI(
    title="Système de Recommandation de Films 🎬",
    version="1.0.0"
)

DB_PATH = "/data/moviesdb" 
model = None
ratings_df = None
movies_df = None

@app.on_event("startup")
def startup_event():
    global model, ratings_df, movies_df

    # Connexion à la base
    try:
        conn = duckdb.connect(database=DB_PATH, read_only=True)
        ratings_df = conn.execute("SELECT user_id, film_id, rating FROM ratings").fetchdf()
        movies_df = conn.execute("SELECT id, title FROM films").fetchdf()
        conn.close()
    except Exception as e:
        raise RuntimeError(f"Erreur de connexion DuckDB : {e}")

    # Entraînement du modèle SVD
    try:
        reader = Reader(rating_scale=(0.5, 5.0))
        data = Dataset.load_from_df(ratings_df[['user_id', 'film_id', 'rating']], reader)
        trainset = data.build_full_trainset()
        model = SVD()
        model.fit(trainset)
        print("✅ Modèle SVD entraîné au démarrage.")
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'entraînement du modèle : {e}")

=======
from app.routers.recommender import router as recommender_router

# Une seule instance FastAPI pour toute l'application
app = FastAPI(title="Movie Recommendation API", version="1.0.0")

# Inclure les routeurs pour la partie recommandation de films
app.include_router(recommender_router, prefix="/api", tags=["recommender"])

# Route racine
@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de recommandation de films 🎬"}

@app.get("/films/")
def get_all_movies():
    if movies_df is None:
        raise HTTPException(status_code=500, detail="Données non disponibles.")
    return movies_df.to_dict(orient="records")

@app.get("/recommend_movies/{user_id}")
def recommend_movies(user_id: int, n: int = 5):
    if model is None or ratings_df is None or movies_df is None:
        raise HTTPException(status_code=500, detail="Le modèle ou les données ne sont pas prêts.")

    # Films déjà notés par l'utilisateur
    user_rated = ratings_df[ratings_df['user_id'] == user_id]['film_id'].unique()
    not_rated_movies = movies_df[~movies_df['id'].isin(user_rated)]

    if not_rated_movies.empty:
        return {"user_id": user_id, "recommendations": []}

    # Prédictions
    predictions = []
    for _, row in not_rated_movies.iterrows():
        pred = model.predict(uid=user_id, iid=row['id'])
        predictions.append({
            "id": row['id'],
            "title": row['title'],
            "rating_predicted": round(pred.est, 2)
        })

    # Trier les recommandations par score décroissant
    predictions.sort(key=lambda x: x["rating_predicted"], reverse=True)

    return {
        "user_id": user_id,
        "title": row['title'],
        "recommendations": predictions[:n]
    }
def read_root():
    return {"message": "Bienvenue sur l'API de recommandation de films !"}

# Base de données utilisateurs
users = {
    1: {"id": 1, "name": "Vince"},
    2: {"id": 2, "name": "Victor"}
}

# Route pour obtenir les détails d'un utilisateur par ID
@app.get("/user/{user_id}/details")
def get_user_details(user_id: int):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"Utilisateur avec l'ID {user_id} non trouvé.")
    return user
