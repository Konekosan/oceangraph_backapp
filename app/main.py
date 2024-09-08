from fastapi import FastAPI
from app.view import planche_api
from app.model import planche
from app.database import engine
from app.database import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return {'details': 'Hello world!'}

app.include_router(planche_api.planche_router, prefix='/planche', tags=['planche'])