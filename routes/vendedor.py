from fastapi import APIRouter,Query
from typing import List
from models.vendedor import Vendedor as vendedorModel
from config.databases import Session,engine,Base
from schemas.vendedor import Vendedor 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.vendedor import VendedorService
vendedor=APIRouter()

@vendedor.get('/vendedor',tags=['vendedor'],response_model=List[Vendedor])
#mostrando todos los vendedores
def get_vendedor()->list[Vendedor]:
    db=Session()
    resultado=db.query(vendedorModel).all()
    return JSONResponse(content=jsonable_encoder(resultado))

@vendedor.get('/vendedor/',tags=['vendedor'],response_model=List[Vendedor])
def buscar_fecha(nombre:str)->list[Vendedor]:
    db=Session()
    result= VendedorService(db).buscar_nombre(str)
    if not result:
        return JSONResponse(status_code=404 ,content={"message":'no encontrado'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))
    
