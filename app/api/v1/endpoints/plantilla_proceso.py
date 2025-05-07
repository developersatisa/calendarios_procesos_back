# app/api/v1/endpoints/plantilla_proceso.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import plantilla_proceso_service as service

router = APIRouter()

@router.post("/")
def crear(data: dict, db: Session = Depends(get_db)):
    return service.crear(db, data)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return service.listar(db)
