import logging

from sqlalchemy.orm import Session
from app.model.planche import Planche
from app.schema.planche_schema import PlancheSchema
from fastapi import HTTPException, status
from sqlalchemy import func, desc

loggers = logging.getLogger(__name__)

#Logger
def _print(text: str, log_level='info'):
    print(text)
    getattr(loggers, log_level)(text)

# Get all planches
def fetch_all_planches(db:Session, skipt:int=0, limit:int=100):
    return db.query(Planche).offset(skipt).limit(limit).all()

# Get planche by id
def fetch_planche_by_id(db:Session, planche_id: int):
    return db.query(Planche).filter(Planche.id == planche_id).first()

# Create planche
def add_planche(db:Session, planche: PlancheSchema):
    _planche = Planche(
                   name=planche.name, 
                   brand=planche.brand, 
                   shape=planche.shape)
    db.add(_planche)
    try:
        db.commit()
        db.refresh(_planche)
        _print('Planche ajouté avec succès !')
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de l'ajout",
        )
    return _planche

def delete_planche(db:Session, planche: PlancheSchema):
    _planche = fetch_planche_by_id(db, planche)

    try:
        db.delete(_planche)
        _print('Planche supprimée avec succès ! ')
        db.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la supression",
        )    