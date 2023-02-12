from fastapi import APIRouter
from pydantic import  BaseModel
from typing import Optional
from fastapi.responses import  HTMLResponse ,JSONResponse
vehiculo=APIRouter()
class Vehiculos(BaseModel):
    idVehiculo: Optional[int] = None
    marcaVehiculo:str
    modelo :str
    tipo :str
    anio :int
vehiculos = [
    {
		"idVehiculo": 1,
		"marcaVehiculo": "HONDA",
		"modelo": "CIVIC",
		"tipo": "AUTO",
		"anio": 2020,
	},
    {
		"idVehiculo": 2,
		"marcaVehiculo": "MAZDA",
		"modelo": "CRV",
		"tipo": "AUTO",
		"anio": 2020,
	}
]



@vehiculo.get('/',tags=['home'])
def mensaje():
    return HTMLResponse(" </h1>VENTAS DE AUTOS</h1> ")

@vehiculo.get('/vehiculos',tags=['vehiculos'])
def bucarvehiculo():
    return vehiculos

@vehiculo.get('/vehiculos/{id}',tags=['vehiculos'])
def get_vehiculo(id:int):
    for vehiculo in vehiculos:
        if vehiculo["idVehiculo"] == id:
            return vehiculo
    return []

@vehiculo.get('/vehiculos/',tags=['vehiculos'])
def get_vehiculos(modelo: str):
    for vehiculo in vehiculos:
        if vehiculo['modelo']== modelo:
            return vehiculo


#estamos pidiendo los valores como objeto dict
@vehiculo.post('/vehiculos',tags=['vehiculos'])
def crear_vahiculo(vehiculo:Vehiculos):
    vehiculos.append(vehiculo)
    return vehiculos

@vehiculo.put('/vehiculos/{id}',tags=['vehiculos'])
def modificar_vahiculo(id:int ,vehiculo : Vehiculos):
    for valor in vehiculos:
        if valor['idVehiculo']== id:
            valor['marcaVehiculo']=vehiculo.marcaVehiculo
            valor['modelo']=vehiculo.modelo
            valor['tipo']=vehiculo.tipo
            valor['anio']=vehiculo.anio
    return vehiculos

@vehiculo.delete('/vehiculos/{id}', tags=['vehiculos'])
def delete_movie(id: int):
    for vehiculo in vehiculos:
        if vehiculo["idVehiculo"] == id:
            vehiculos.remove(vehiculo)
            return vehiculo