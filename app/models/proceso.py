from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from app.db.database import Base

class Proceso(Base):
    __tablename__ = "proceso"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(1000), nullable=True)
    frecuencia = Column(Integer, nullable=False)
    temporalidad = Column(String(50), nullable=False)  # día, mes, año
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=True)
    inicia_dia_1 = Column(Boolean, default=False)
    hitos = relationship(
        "ProcesoHitoMaestro",
        back_populates="proceso",
        cascade="all, delete-orphan"
    )
    clientes = relationship("ClienteProceso", back_populates="proceso")
