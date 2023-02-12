from config.databases import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table
from config.databases import meta ,engine

sedes = Table("sede", meta, Column("idSede", Integer, primary_key=True),
             Column("nombre", String(255)),
             Column("ubicacion", String(255)))

meta.create_all(engine)
