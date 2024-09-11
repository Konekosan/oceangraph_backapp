from typing import Optional
from pydantic import BaseModel, Field

class UtilisateurSchema(BaseModel):
    id: Optional[int]=None
    nom: Optional[str]=None
    prenom: Optional[str]=None
    age: Optional[int]=None
    username: Optional[str]=None
    # hashed_pwd = Optional[str]=None
    # is_active = Optional[str]=None

    class Config:
        orm_mode = True


class RequestUtilisateurSchema(BaseModel):
    parameter: UtilisateurSchema = Field(...)
