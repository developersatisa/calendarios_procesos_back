# app/services/plantilla_proceso_service.py
from app.crud import plantilla_proceso as crud

def crear(db, data: dict):
    return crud.create(db, data)

def listar(db):
    return crud.get_all(db)
