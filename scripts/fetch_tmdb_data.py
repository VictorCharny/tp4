import requests
import pandas as pd

API_KEY = ""
url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=fr-FR&page=1"
response = requests.get(url)
data = response.json()

movies = []
for movie in data['results']:
    movies.append({
        "id": movie['id'],
        "title": movie['title'],
        "description": movie['overview'],
        "genres": ", ".join([str(g) for g in movie.get("genre_ids", [])]),
        "release_date": movie['release_date'],
        "vote_average": movie['vote_average'],
        "vote_count": movie['vote_count']
    })

df = pd.DataFrame(movies)
df.to_csv("data/movies_tmdb.csv", index=False)
