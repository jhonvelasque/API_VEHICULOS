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
from fastapi.responses import HTMLResponse ,JSONResponse
from fastapi.encoders import jsonable_encoder
from cryptography.fernet import Fernet
#permite hacer unico los cifrados
key=Fernet.generate_key()
f= Fernet(key)

Base.metadata.create_all(bind=engine)

@sede.get("/sede",tags=['sede'],response_model=list[Sedes],status_code=200)
def get_sedes()->list[Sedes]:
    db=Session()
    result=db.query(sedesModel).all()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@sede.get("/sede/",tags=['sede'],response_model=list[Sedes],status_code=200)
def get_sedes_by_nombre(nombre:str)->list[Sedes] :
    db=Session()
    result=db.query(sedesModel).filter(sedesModel.nombre == nombre).first()
    if not result:
        return JSONResponse(status_code=404,content={"message":'no encontrado'})
    return JSONResponse(status_code=202,content=jsonable_encoder(result))


@sede.get("/sede/{id}",tags=['sede'],response_model=Sedes)
def get_sede(id:int)->Sedes:
    db=Session()
    result=db.query(sedesModel).filter(sedesModel.idSede == id).first()
    if not result:
        return JSONResponse(status_code=404 ,content={"message":'no encontrado'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@sede.post("/sede",tags=['sede'],response_model=dict,status_code=201)
def create_sede(sede:Sedes) ->dict:
    #platzi
    db =Session()
    new_sede=sedesModel(**sede.dict())
    db.add(new_sede)
    db.commit()
    return JSONResponse(status_code=201,content={"message":"se añadio registro"})

@sede.put('/sede/{id}',tags=['sede'],response_model=dict,status_code=200,)
def update_sedes(id:int ,sede:Sedes)->dict:
    db=Session()
    result=db.query(sedesModel).filter(sedesModel.idSede==id).first()
    if not result:
        return JSONResponse(status_code=404 ,content={"message":'no encontrado'})
    result.nombre=sede.nombre
    result.ubicacion=sede.ubicacion
    db.commit()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@sede.delete("/sede/{id}",tags=['sede'],response_model=dict,status_code=200)
def delete_sede(id:int)->dict:
    db=Session()
    result=db.query(sedesModel).filter(sedesModel.idSede==id).first()
    if not result:
        return JSONResponse(status_code=404,content={'message':"no encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))
