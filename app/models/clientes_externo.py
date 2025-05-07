from sqlalchemy import Column, String
from app.db.database import Base

class ClienteExterno(Base):
    __tablename__ = "clientes"
    __table_args__ = {'extend_existing': True}

    idcliente = Column(String(9), primary_key=True, index=True)
    cif = Column(String(15))
    cif_empresa = Column(String(15))
    razsoc = Column(String(100))
    direccion = Column(String(100))
    localidad = Column(String(100))
    provincia = Column(String(50))
    cpostal = Column(String(5))
    codigop = Column(String(10))
    pais = Column(String(4))
    cif_factura = Column(String(15))
