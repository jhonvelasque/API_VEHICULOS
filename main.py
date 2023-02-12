from fastapi import FastAPI ,Body ,APIRouter
from fastapi.responses import HTMLResponse
from routes.sede import sede
from routes.vehiculo import vehiculo
from routes.vendedor import vendedor
from middlewares.error import ErrorHander
#primer parametro http
app =FastAPI()
app.title="mi primera api"
app.version="0.0.1"
app.add_middleware(ErrorHander)
app.include_router(sede)
app.include_router(vehiculo)
app.include_router(vendedor)

#creacion de base de datos sino la tienes
#Base.metadata.create_all(bind=engine)