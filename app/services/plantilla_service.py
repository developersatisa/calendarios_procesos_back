from app.crud import plantilla as crud_plantilla
from sqlalchemy.orm import Session


def crear(db: Session, data: dict):    
    return crud_plantilla.create_plantilla(db, data)

def obtener_todas(db: Session):
    return crud_plantilla.get_plantillas(db)

def obtener_por_id(db: Session, id: int):
    return crud_plantilla.get_plantilla(db, id)

def actualizar(db: Session, id: int, data: dict):
    return crud_plantilla.update_plantilla(db, id, data)

def eliminar(db: Session, id: int):
    return crud_plantilla.delete_plantilla(db, id)