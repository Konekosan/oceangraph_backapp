from typing import Optional
from pydantic import BaseModel, Field

class PlancheSchema(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    brand: Optional[str]=None
    shape: Optional[str]=None

    class Config:
        orm_mode = True


class RequestPlancheSchema(BaseModel):
    parameter: PlancheSchema = Field(...)