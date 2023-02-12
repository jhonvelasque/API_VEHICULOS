import os
from sqlalchemy import create_engine ,MetaData
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#sqlite_file_name = "../database.sqlite"
#base_dir = os.path.dirname(os.path.realpath(__file__))
#database_url = "mysql+pymysql://username:password@host:port/database"
database_url = "mysql+pymysql://root:@localhost:3306/venta_vehiculos"
#creando motor de base de datos

engine = create_engine(database_url, echo=True)
#conector 
conn=engine.connect()
meta=MetaData()
#conecotor a base de datos 
Session = sessionmaker(bind=engine)
Base = declarative_base()