from fastapi import APIRouter
from .endpoints import plantilla,proceso,hito,proceso_hito_maestro,cliente_proceso,ping

api_router = APIRouter()
api_router.include_router(plantilla.router, prefix="/plantillas", tags=["Plantillas"])
api_router.include_router(proceso.router, prefix="/procesos", tags=["Procesos"])
api_router.include_router(hito.router, prefix="/hitos", tags=["Hitos"])
api_router.include_router(proceso_hito_maestro.router, prefix="/proceso-hitos", tags=["Asociaciones"])
api_router.include_router(cliente_proceso.router, prefix="/cliente-procesos", tags=["Clientes Procesos"])
api_router.include_router(ping.router, prefix="/ping", tags=["ping"])