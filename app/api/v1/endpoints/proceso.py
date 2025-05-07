from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import proceso_service

router = APIRouter()

@router.post("/")
def crear(data: dict, db: Session = Depends(get_db)):
    return proceso_service.crear(db, data)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return proceso_service.obtener_todos(db)

@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    proceso = proceso_service.obtener_por_id(db, id)
    if not proceso:
        raise HTTPException(status_code=404, detail="Proceso no encontrado")
    return proceso

@router.put("/{id}")
def actualizar(id: int, data: dict, db: Session = Depends(get_db)):
    proceso = proceso_service.actualizar(db, id, data)
    if not proceso:
        raise HTTPException(status_code=404, detail="Proceso no encontrado")
    return proceso

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    proceso = proceso_service.eliminar(db, id)
    if not proceso:
        raise HTTPException(status_code=404, detail="Proceso no encontrado")
    return {"message": "Proceso eliminado correctamente"}
