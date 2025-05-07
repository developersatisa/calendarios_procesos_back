from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import proceso_hito_maestro_service

router = APIRouter()

@router.post("/")
def crear(data: dict, db: Session = Depends(get_db)):
    return proceso_hito_maestro_service.crear(db, data)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return proceso_hito_maestro_service.obtener_todos(db)

@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    registro = proceso_hito_maestro_service.obtener_por_id(db, id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro

@router.put("/{id}")
def actualizar(id: int, data: dict, db: Session = Depends(get_db)):
    registro = proceso_hito_maestro_service.actualizar(db, id, data)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    registro = proceso_hito_maestro_service.eliminar(db, id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"message": "Asociación eliminada correctamente"}
