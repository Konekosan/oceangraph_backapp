from fastapi import FastAPI
from app.view import planche_api
from app.view import utilisateur_api
from app.database import engine
from app.database import Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Ajouter le middleware CORS pour autoriser votre frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Autoriser les requêtes venant de localhost:4200 (le frontend)
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les headers
)

Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return {'details': 'Hello world!'}

app.include_router(planche_api.planche_router, prefix='/planche', tags=['planche'])
app.include_router(utilisateur_api.utilisateur_router, prefix='/user', tags=['user'])