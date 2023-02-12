from fastapi import APIRouter,Response 
#importando la conexion
from config.databases import conn 
#importando el squema
from models.sede import sedes as sedesModel
#PARA PEDIRLE
sede = APIRouter()
from schemas.sede import Sedes
# CREAR PETICIONES
from fastapi.responses import HTMLResponse ,JSONResponse
from cryptography.fernet import Fernet
#permite hacer unico los cifrados
key=Fernet.generate_key()
f= Fernet(key)
"""
@sede.get("/sede")
def get_users():
    return 'helo' #conn.execute(sede.select()).fetchall()
"""
@sede.get("/sede1/",tags=['sede'])
def get_sede():
    return print(conn.execute(sedesModel.select()).fetchall())

@sede.get("/sede/{id}",tags=['sede'])
def get_sede(id:str):
    print(conn.execute(sedesModel.select().where(sedesModel.c.idSede==id)).first())
    #return HTMLResponse(content=(conn.execute(sedes.select().where(sedes.c.idSede==id)).first()))
    #ver como mostrarlo en pantalla 
@sede.post("/sede",tags=['sede'],response_model=dict)
def create_sede(sede:Sedes) ->dict:
    """new_sede={"idSede":sede.idSede,
                "nombre":sede.nombre,
                "ubicacion":sede.ubicacion}
    #new_sede["idsede"]=f.encrypt(sede.password.encode("utf-8"))
    resultado=conn.execute(sedes.insert().values(new_sede))
    #sedes hace referencia al shema creado
    print ((conn.execute(sedes.select().where(sedes.c.idSede==resultado.lastrowid))).first())"""
    #platzi
    db =Se

@sede.delete("/sede/{id}",tags=['sede'])
def delete_sede(id:int):
    reult=conn.execute(sedes.delete().where(sedes.c.idSede==id))
    return Response(status_code=204)
