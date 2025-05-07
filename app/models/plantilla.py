from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Plantilla(Base):
    __tablename__ = "plantilla"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(1000), nullable=True)
    procesos = relationship("PlantillaProceso", back_populates="plantilla", cascade="all, delete-orphan")