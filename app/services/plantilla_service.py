from app.crud import plantilla as crud_plantilla
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from app.models.plantilla import Plantilla
from app.models.plantilla_proceso import PlantillaProceso
from app.models.proceso import Proceso

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

def obtener_plantillas_con_procesos_y_hitos(db):
    plantillas = db.query(Plantilla).options(
        joinedload(Plantilla.procesos).joinedload(PlantillaProceso.proceso).joinedload(Proceso.hitos)
    ).all()

    result = []
    for plantilla in plantillas:
        result.append({
            "id": plantilla.id,
            "nombre": plantilla.nombre,
            "procesos": [
                {
                    "id": rel.proceso.id,
                    "nombre": rel.proceso.nombre,
                    "hitos": [h.hito.nombre for h in rel.proceso.hitos]
                } for rel in plantilla.procesos
            ]
        })
    return result