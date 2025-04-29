import streamlit as st
import requests

st.title("🎬 Recommandations de films")
user_id = st.number_input("Entrez un ID utilisateur :", min_value=1, step=1)

if st.button("Obtenir des recommandations"):
    response = requests.get(f"http://backend:8000/recommend_movies/{user_id}")
    if response.status_code == 200:
        data = response.json()
        st.write(f"🎯 Recommandations pour l'utilisateur {user_id}")
        for movie in data['recommendations']:
            st.write(f"- {movie['title']} (Note prédite : {movie['rating_predicted']})")
    else:
        st.error("Erreur lors de la récupération des recommandations.")