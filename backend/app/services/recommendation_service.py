from surprise import Dataset, Reader, SVD
from .db import get_ratings, get_movies

# Charger les données
ratings_df = get_ratings()
movies_df = get_movies()

# Préparer les données pour surprise
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings_df[['user_id', 'film_id', 'rating']], reader)

# Entraîner le modèle SVD
trainset = data.build_full_trainset()
model = SVD()
model.fit(trainset)

def recommend_movies(user_id: int, n: int = 5):
    # Films non encore notés par l'utilisateur
    rated_movies = ratings_df[ratings_df['user_id'] == user_id]['film_id'].unique()
    not_rated_movies = movies_df[~movies_df['id'].isin(rated_movies)]

    # Prédire les notes
    predictions = []
    for idx, row in not_rated_movies.iterrows():
        pred = model.predict(user_id, row['id'])
        predictions.append((row['id'], row['title'], pred.est))

    # Trier par prédiction décroissante
    predictions.sort(key=lambda x: x[2], reverse=True)

    # Retourner les meilleurs
    return [{"id": id_, "title": title, "rating_predicted": round(rating, 2)} for id_, title, rating in predictions[:n]]
