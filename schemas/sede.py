from pydantic import BaseModel
from typing import Optional

class Sedes(BaseModel):
    idSede :Optional[int]
    nombre : str 
    ubicacion : str 