from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import cliente_proceso_hito_service as service

router = APIRouter()

@router.post("/")
def crear(data: dict, db: Session = Depends(get_db)):
    return service.crear(db, data)

@router.patch("/{id}/estado")
def actualizar_estado(id: int, estado: str, db: Session = Depends(get_db)):
    return service.actualizar_estado(db, id, estado)

@router.get("/cliente-proceso/{cliente_proceso_id}")
def listar(cliente_proceso_id: int, db: Session = Depends(get_db)):
    return service.listar_por_cliente_proceso(db, cliente_proceso_id)
