from sqlalchemy.orm import Session
from app.models.plantilla import Plantilla

def create_plantilla(db:Session, data:dict):
    nueva = Plantilla(**data)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def get_plantilla(db:Session, id:int):
    return db.query(Plantilla).filter(Plantilla.id == id).first()  

def get_plantillas(db:Session):
    return db.query(Plantilla).all()

def update_plantilla(db:Session, id:int, data:dict):
    plantilla = get_plantilla(db, id)
    if plantilla:
        for key, value in data.items():
            setattr(plantilla, key, value)
        db.commit()
        db.refresh(plantilla)        
    return plantilla

def delete_plantilla(db:Session, id:int):
    plantilla = get_plantilla(db, id)
    if plantilla:
        db.delete(plantilla)
        db.commit()
    return plantilla