# 🎬 API de Recommandation de Films

Projet API REST construite avec **FastAPI** pour recommander des films à partir d'une base de données PostgreSQL.

Le projet utilise **Docker** et **Docker Compose** pour orchestrer tous les services.

---

## 🚀 Lancer le projet

### Prérequis 

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

### Commandes

1. Cloner le dépôt :
   ```bash
   git clone <URL_DU_REPO>
   cd <nom_du_dossier>
   ```

2. Construire et démarrer les services :
   ```bash
   docker-compose up --build
   ```

3. Accéder à l'API :
   - Page principale : [http://localhost:8000/](http://localhost:8000/)
   - Documentation Swagger : [http://localhost:8000/docs](http://localhost:8000/docs)
   - Documentation Redoc : [http://localhost:8000/redoc](http://localhost:8000/redoc)

4. Arrêter les services :
   - Dans le terminal : `Ctrl + C`
   - Puis :
     ```bash
     docker-compose down
     ```

---

## 🛠 Technologies utilisées

- FastAPI
- PostgreSQL
- Docker & Docker Compose
