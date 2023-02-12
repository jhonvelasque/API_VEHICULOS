#representa a  la tabla
from config.databases import Base 
from sqlalchemy import Column, Integer, String, Float,Date 
from config.databases import meta


class sede(Base):
    #el nombre  de la tabla debes estar iguala la que creaste
    __tablename__ = "sede"
    idSede = Column(Integer, primary_key = True)
    nombre = Column(String(250))
    ubicacion = Column(String)
    
