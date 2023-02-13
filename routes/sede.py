from fastapi import APIRouter,Response , HTTPException, Path, Query, Request
#importando la conexion
from config.databases import conn ,Session, engine, Base
#importando el squema
from models.sede import sede as sedesModel
#PARA PEDIRLE
sede = APIRouter()
from typing import  List
from pydantic import BaseModel, Field
from schemas.sede import Sedes
# CREAR PETICIONES
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder
# incluyendo servicios
from services.sedes import SedeService

Base.metadata.create_all(bind=engine)

@sede.get("/sede",tags=['sede'],response_model=list[Sedes],status_code=200)
def get_sedes()->list[Sedes]:
    db=Session()
    result=SedeService(db).get_sedes()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@sede.get("/sede/{id}",tags=['sede'],response_model=Sedes,status_code=200)
def get_sede(id:int) -> Sedes:
    db=Session()
    result=SedeService(db).get_sede(id)
    if not result:
        return JSONResponse(status_code=404 ,content={"message":'no encontrado'})
    
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@sede.get("/sede/",tags=['sede'],response_model=list[Sedes],status_code=200)
def get_sedes_by_nombre(nombre:str)->list[Sedes] :
    db=Session()
    result=SedeService(db).get_sede_for_name(nombre)
    if not result:
        return JSONResponse(status_code=404,content={"message":'no encontrado'})
    return JSONResponse(status_code=202,content=jsonable_encoder(result))




@sede.post("/sede",tags=['sede'],response_model=dict,status_code=201)
def create_sede(sede:Sedes) ->dict:
    #platzi
    db =Session()
    SedeService(db).crate_sede(sede)
    return JSONResponse(status_code=201,content={"message":"se añadio registro"})

@sede.put('/sede/{id}',tags=['sede'],response_model=dict,status_code=200,)
def update_sedes(id:int ,sede:Sedes)->dict:
    db=Session()
    #filtrando por id
    result=SedeService(db).get_sede(id)
    if not result:
        return JSONResponse(status_code=404 ,content={"message":'no encontrado'})
    #introduciendo los valores de la clase se al resultado
    SedeService(db).update_sede(id,sede)
    return JSONResponse(status_code=200,content={"mensaje":"se ha modificado la sede"})

@sede.delete("/sede/{id}",tags=['sede'],response_model=dict,status_code=200)
def delete_sede(id:int)->dict:
    db=Session()
    result:sedesModel= db.query(sedesModel).filter(sedesModel.idSede==id).first()
    if not result:
        return JSONResponse(status_code=404,content={'message':"no encontrado"})
    SedeService(db).delete_sede(id)
    return JSONResponse(status_code=200,content=jsonable_encoder(result))
