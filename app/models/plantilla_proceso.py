# app/models/plantilla_proceso.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class PlantillaProceso(Base):
    __tablename__ = "plantilla_proceso"

    id = Column(Integer, primary_key=True, index=True)
    plantilla_id = Column(Integer, ForeignKey("plantilla.id"), nullable=False)
    proceso_id = Column(Integer, ForeignKey("proceso.id"), nullable=False)
    plantilla = relationship("Plantilla", back_populates="procesos")
    proceso = relationship("Proceso")

