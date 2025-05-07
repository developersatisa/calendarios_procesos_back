from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine
from app.models import *
from app.models.cliente_proceso import ClienteProceso
from app.models.cliente_proceso_hito import ClienteProcesoHito
from datetime import date

def poblar_datos_mockeados():
    db: Session = SessionLocal()

    # --- Limpieza previa opcional (solo para tests controlados) ---
    db.query(ClienteProcesoHito).delete()
    db.query(ClienteProceso).delete()
    db.query(ProcesoHitoMaestro).delete()
    db.query(Proceso).delete()
    db.query(Plantilla).delete()
    db.commit()

    # --- Plantilla de ejemplo ---
    plantilla = Plantilla(nombre="Plantilla Nómina", descripcion="Procesos de nómina y fiscales")
    db.add(plantilla)
    db.commit()
    db.refresh(plantilla)

    # --- Procesos ---
    proceso1 = Proceso(
        nombre="Contabilidad Mensual",
        descripcion="Proceso mensual de contabilidad",
        frecuencia=1,
        temporalidad="mes",
        fecha_inicio=date(2024, 1, 1),
        inicia_dia_1=True
    )
    proceso2 = Proceso(
        nombre="Modelo 190",
        descripcion="Generación y presentación del modelo",
        frecuencia=1,
        temporalidad="año",
        fecha_inicio=date(2024, 1, 1),
        inicia_dia_1=False
    )

    db.add_all([proceso1, proceso2])
    db.commit()

    relacion1 = PlantillaProceso(plantilla=plantilla, proceso=proceso1)
    relacion2 = PlantillaProceso(plantilla=plantilla, proceso=proceso2)
    db.add_all([relacion1, relacion2])

    # --- Crear los Hitos base (reutilizables) ---
    hito1 = Hito(nombre="Recibir Documentación", frecuencia=1, temporalidad="mes",fecha_inicio=date(2024, 1, 1))
    hito2 = Hito(nombre="Gestionar Contabilidad", frecuencia=2, temporalidad="mes",fecha_inicio=date(2024, 1, 1))
    hito3 = Hito(nombre="Calcular Modelo", frecuencia=1, temporalidad="mes",fecha_inicio=date(2024, 1, 1))
    hito4 = Hito(nombre="Presentar Modelo", frecuencia=2, temporalidad="mes",fecha_inicio=date(2024, 1, 1))
    db.add_all([hito1, hito2, hito3, hito4])
    db.commit()
    db.refresh(hito1)
    db.refresh(hito2)
    db.refresh(hito3)
    db.refresh(hito4)

    # --- Asociarlos como maestros a los procesos ---
    asoc1 = ProcesoHitoMaestro(id_proceso=proceso1.id, id_hito=hito1.id)
    asoc2 = ProcesoHitoMaestro(id_proceso=proceso1.id, id_hito=hito2.id)
    asoc3 = ProcesoHitoMaestro(id_proceso=proceso2.id, id_hito=hito3.id)
    asoc4 = ProcesoHitoMaestro(id_proceso=proceso2.id, id_hito=hito4.id)
    db.add_all([asoc1, asoc2, asoc3, asoc4])

    # --- ClienteProceso + hitos duplicados (para cliente "123456789") ---
    cliente_proceso = ClienteProceso(
        idcliente="123456789",
        id_proceso=proceso1.id,
        fecha_inicio=date(2024, 5, 1),
        fecha_fin=date(2024, 12, 31),
        mes=5,
        anio=2024,
    )
    db.add(cliente_proceso)
    db.commit()
    db.refresh(cliente_proceso)

    # --- Clonación de hitos maestros para ese ClienteProceso ---
    hitos_maestro = db.query(ProcesoHitoMaestro).filter_by(id_proceso=proceso1.id).all()
    for h in hitos_maestro:
        hito_cliente = ClienteProcesoHito(
            cliente_proceso_id=cliente_proceso.id,
            hito_id=h.id,
            estado="pendiente"
        )
        db.add(hito_cliente)

    db.commit()
    db.close()

    print("✅ Datos mockeados insertados correctamente.")

# Llamada directa
if __name__ == "__main__":
    poblar_datos_mockeados()
