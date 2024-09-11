import logging

from sqlalchemy.orm import Session
from app.model.utilisateur import Utilisateur
from app.schema.utilisateur_schema import UtilisateurSchema
from fastapi import HTTPException, status
from sqlalchemy import func, desc

loggers = logging.getLogger(__name__)

#Logger
def _print(text: str, log_level='info'):
    print(text)
    getattr(loggers, log_level)(text)

# Get all utilisateurs
def fetch_all_utilisateur(db:Session, skipt:int=0, limit:int=100):
    return db.query(Utilisateur).offset(skipt).limit(limit).all()

# Get utlisateur by id
def fetch_utilisateur_by_id(db:Session, utilisateur_id: int):
    return db.query(Utilisateur).filter(Utilisateur.id == utilisateur_id).first()

# Create utlisateur
def add_utlisateur(db:Session, user: UtilisateurSchema):
    _user = Utilisateur(
                   nom=user.nom, 
                   prenom=user.prenom, 
                   age=user.age,
                   username=user.username, 
                   hashed_pwd=user.hashed_pwd, 
                   is_active=user.is_active
    )
    db.add(_user)
    try:
        db.commit()
        db.refresh(_user)
        _print('Planche ajouté avec succès !')
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de l'ajout",
        )
    return _user