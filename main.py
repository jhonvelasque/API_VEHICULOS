from fastapi import FastAPI ,Body ,APIRouter
from fastapi.responses import HTMLResponse
from pydantic import  BaseModel
from typing import Optional

from routes.sede import sede
#primer parametro http
app =FastAPI()
app.title="mi primera api"
app.version="0.0.1"
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

app.include_router(sede)

@app.get('/',tags=['home'])
def mensaje():
    return HTMLResponse(" </h1>VENTAS DE AUTOS</h1> ")

@app.get('/vehiculos',tags=['vehiculos'])
def bucarvehiculo():
    return vehiculos

@app.get('/vehiculos/{id}',tags=['vehiculos'])
def get_vehiculo(id:int):
    for vehiculo in vehiculos:
        if vehiculo["idVehiculo"] == id:
            return vehiculo
    return []

@app.get('/vehiculos/',tags=['vehiculos'])
def get_vehiculos(modelo: str):
    for vehiculo in vehiculos:
        if vehiculo['modelo']== modelo:
            return vehiculo


#estamos pidiendo los valores como objeto dict
@app.post('/vehiculos',tags=['vehiculos'])
def crear_vahiculo(vehiculo:Vehiculos):
    vehiculos.append(vehiculo)
    return vehiculos

@app.put('/vehiculos/{id}',tags=['vehiculos'])
def modificar_vahiculo(id:int ,vehiculo : Vehiculos):
    for valor in vehiculos:
        if valor['idVehiculo']== id:
            valor['marcaVehiculo']=vehiculo.marcaVehiculo
            valor['modelo']=vehiculo.modelo
            valor['tipo']=vehiculo.tipo
            valor['anio']=vehiculo.anio
    return vehiculos

@app.delete('/vehiculos/{id}', tags=['vehiculos'])
def delete_movie(id: int):
    for vehiculo in vehiculos:
        if vehiculo["idVehiculo"] == id:
            vehiculos.remove(vehiculo)
            return vehiculo