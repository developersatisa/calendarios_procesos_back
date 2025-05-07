from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import hito_service

router = APIRouter()

@router.post("/")
def crear(data: dict, db: Session = Depends(get_db)):
    return hito_service.crear(db, data)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return hito_service.obtener_todos(db)

@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    hito = hito_service.obtener_por_id(db, id)
    if not hito:
        raise HTTPException(status_code=404, detail="Hito no encontrado")
    return hito

@router.put("/{id}")
def actualizar(id: int, data: dict, db: Session = Depends(get_db)):
    hito = hito_service.actualizar(db, id, data)
    if not hito:
        raise HTTPException(status_code=404, detail="Hito no encontrado")
    return hito

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    hito = hito_service.eliminar(db, id)
    if not hito:
        raise HTTPException(status_code=404, detail="Hito no encontrado")
    return {"message": "Hito eliminado correctamente"}
