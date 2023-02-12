from models.sede import sede as sedesModel
#from fastapi import Query
from schemas.sede import Sedes 
class SedeService():
    def __init__(self,db)->None:
        self.db=db
    def get_sedes(self):
        result=self.db.query(sedesModel).all()
        return result
    #nota este metodo no debe ser iguala la funcion creada 
    def get_sede(self,id):
        resultado=self.db.query(sedesModel).filter(sedesModel.idSede == id).first()
        return resultado
    #nota cuidado que repitas los metodos
    def get_sede_for_name(self,nombre):
        result=self.db.query(sedesModel).filter(sedesModel.nombre==nombre).first()
        return result

    def crate_sede(self,sede:Sedes):
        new_sede=sedesModel(**sede.dict())
        self.db.add(new_sede)
        self.db.commit()
        return "se logro"
        
    def update_sede(self,id:int, data:Sedes):
        sede=self.db.query(sedesModel).filter(sedesModel.idSede == id).first()
        sede.nombre = data.nombre
        sede.ubicacion=data.ubicacion
        self.db.commit()
        return  
