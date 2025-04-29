from fastapi import FastAPI, HTTPException
from app.routers.recommender import router as recommender_router

# Une seule instance FastAPI pour toute l'application
app = FastAPI(title="Movie Recommendation API", version="1.0.0")

# Inclure les routeurs pour la partie recommandation de films
app.include_router(recommender_router, prefix="/api", tags=["recommender"])

# Route racine
@app.get("/")
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