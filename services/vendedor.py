from models.vendedor import Vendedor as vendedorModel
from fastapi import Query
from sqlalchemy import extract,text
class VendedorService():
    def __init__(self,db)->None:
        self.db=db
    #veindo como implementar
    def buscar_fecha(self,anio:int):
        result=self.db.query(vendedorModel.idVendedor,
        vendedorModel.nombre, 
        vendedorModel.foto,
        extract('year', vendedorModel.fechaNacimiento).label("year_of_birth")).filter(text("extract(year from fechaNacimiento) = :value").bindparams(value=anio)).all()
        for nombre, year in result:
            print(nombre, year)
        #return result

    def buscar_nombre(self,nombre:str) :
        result=self.db.query(vendedorModel).filter(vendedorModel.nombre==nombre).first()
        return result
