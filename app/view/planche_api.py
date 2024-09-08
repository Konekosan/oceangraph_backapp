from fastapi import APIRouter, Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.controller import planche_repository
from app.schema.planche_schema import RequestPlancheSchema

planche_router = APIRouter()

# Fetch all planches
@planche_router.get("/")
async def get(db:Session=Depends(get_db)):
    # _planches = 'coucou'
    _planches = planche_repository.get_planches(db, 0, 100)
    return _planches, 200

# Creation d'une planche
@planche_router.post("/add")
async def create(request: RequestPlancheSchema, db:Session=Depends(get_db)):

    print('aaaaaaaaaa')
    print(request.parameter)
    _planche = planche_repository.add_planche(db, request.parameter)
    return _planche, 200