from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Hito(Base):
    __tablename__ = "hito"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(1000), nullable=True)
    frecuencia = Column(Integer, nullable=False)
    temporalidad = Column(String(50), nullable=False)  # día, mes, año
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=True)
    obligatorio = Column(Boolean, default=False)    
    procesos = relationship(
        "ProcesoHitoMaestro",
        back_populates="hito",
        cascade="all, delete-orphan"
    )
