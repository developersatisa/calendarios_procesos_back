# app/models/cliente_proceso_hito.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class ClienteProcesoHito(Base):
    __tablename__ = "cliente_proceso_hito"

    id = Column(Integer, primary_key=True, index=True)
    cliente_proceso_id = Column(Integer, ForeignKey("cliente_proceso.id"), nullable=False)
    hito_id = Column(Integer, ForeignKey("proceso_hito_maestro.id"), nullable=False)
    estado = Column(String(50), nullable=False, default="pendiente")
    fecha_estado = Column(DateTime, default=datetime.utcnow)

    cliente_proceso = relationship("ClienteProceso", back_populates="hitos")
    hito = relationship("ProcesoHitoMaestro")
