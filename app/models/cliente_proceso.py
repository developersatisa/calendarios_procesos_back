from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class ClienteProceso(Base):
    __tablename__ = "cliente_proceso"

    id = Column(Integer, primary_key=True, index=True)
    idcliente = Column(String(9), nullable=False)  # FK LÓGICA a la tabla externa "clientes"
    id_proceso = Column(Integer, ForeignKey("proceso.id"), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=True)
    mes = Column(Integer, nullable=True)
    anio = Column(Integer, nullable=True)
    id_anterior = Column(Integer, ForeignKey("cliente_proceso.id"), nullable=True)
    proceso = relationship("Proceso", back_populates="clientes")
    hitos = relationship("ClienteProcesoHito", back_populates="cliente_proceso", cascade="all, delete-orphan")
