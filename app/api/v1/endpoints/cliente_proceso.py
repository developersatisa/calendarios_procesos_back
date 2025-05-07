from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import cliente_proceso_service
from app.utils.serializers import model_to_dict

router = APIRouter()

@router.post("/")
def crear(data: dict, db: Session = Depends(get_db)):
    cp = cliente_proceso_service.crear(db, data)
    return model_to_dict(cp)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return cliente_proceso_service.obtener_todos(db)

@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    registro = cliente_proceso_service.obtener_por_id(db, id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro

@router.put("/{id}")
def actualizar(id: int, data: dict, db: Session = Depends(get_db)):
    registro = cliente_proceso_service.actualizar(db, id, data)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    registro = cliente_proceso_service.eliminar(db, id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"message": "Cliente-Proceso eliminado correctamente"}
