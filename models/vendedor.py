from config.databases import Base
from sqlalchemy import Column,Integer,String ,DATE
from config.databases import meta

class Vendedor(Base):
    __tablename__="vendedor"
    idVendedor=Column(Integer,primary_key=True)
    nombre=Column(String(100))
    fechaNacimiento=Column(DATE)
    foto =Column(String)



