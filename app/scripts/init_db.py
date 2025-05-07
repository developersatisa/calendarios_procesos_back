# app/scripts/init_db.py

from app.db.database import Base, engine

# 👇 Importa TODOS los modelos para que SQLAlchemy los registre
from app.models import *  # Y con eso se registran todas


print("🔧 Verificando y creando tablas si no existen...")
Base.metadata.create_all(bind=engine)
print("✅ Tablas generadas (si no existían)")
