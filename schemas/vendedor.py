#la esquema de la tabla para ingresar datos mas rapido
from pydantic import BaseModel
from typing import Optional

class Vendedor(BaseModel):
    idVehiculo :Optional[int]
    nombre : str 
    fechaNacimiento : str 
    foto : str

