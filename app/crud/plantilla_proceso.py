# app/crud/plantilla_proceso.py
from app.models.plantilla_proceso import PlantillaProceso

def create(db, data: dict):
    nuevo = PlantillaProceso(**data)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_all(db):
    return db.query(PlantillaProceso).all()
