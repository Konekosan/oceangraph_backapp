import logging

from fastapi import APIRouter, Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.controller import utilisateur_repository
from app.schema.utilisateur_schema import RequestUtilisateurSchema

loggers = logging.getLogger(__name__)

utilisateur_router = APIRouter()

# Fetch all planches
@utilisateur_router.get("/")
async def get(db:Session=Depends(get_db)):
    _utlisateurs = utilisateur_repository.fetch_all_utilisateur(db, 0, 100)
    return _utlisateurs, 200

# Creation d'une planche
@utilisateur_router.post("/add")
async def create(request: RequestUtilisateurSchema, db:Session=Depends(get_db)):
    _utlisateur = utilisateur_repository.add_planche(db, request.parameter)
    return _utlisateur, 200

# Delete usager by id
# @utilisateur_router.delete("/{id}")
# def delete(id: int, db:Session=Depends(get_db)):
#     utilisateur_repository.delete_planche(db, id)
#     message = 'Planche ' + str(id) + ' supprimée avec succès'
#     return {message, 200}