from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import plantilla_service

router = APIRouter()


@router.post("/")
def crear(data: dict, db: Session = Depends(get_db)):
    return plantilla_service.crear(db, data)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return plantilla_service.obtener_todas(db)

@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    plantilla = plantilla_service.obtener_por_id(db, id)
    if not plantilla:
        raise HTTPException(status_code=404, detail="Plantilla no encontrada")
    return plantilla

@router.put("/{id}")
def actualizar(id: int, data: dict, db: Session = Depends(get_db)):
    plantilla = plantilla_service.actualizar(db, id, data)
    if not plantilla:
        raise HTTPException(status_code=404, detail="Plantilla no encontrada")
    return plantilla

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    plantilla = plantilla_service.eliminar(db, id)
    if not plantilla:
        raise HTTPException(status_code=404, detail="Plantilla no encontrada")
    return {"message": "Plantilla eliminada correctamente"}