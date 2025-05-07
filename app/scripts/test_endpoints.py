import requests
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine
from app.models import *
from app.models.cliente_proceso import ClienteProceso
from app.models.cliente_proceso_hito import ClienteProcesoHito

BASE_URL = "http://localhost:8000/v1"  # Cambia esto según tu entorno

def test_health():
    r = requests.get(f"{BASE_URL}/ping")
    assert r.status_code == 200
    print("✅ API UP")

def crear_plantilla():
    payload = {
        "nombre": "Test Plantilla",
        "descripcion": "Plantilla de prueba"
    }
    r = requests.post(f"{BASE_URL}/plantillas", json=payload)
    print(f"POST /plantillas: {r.status_code} → {r.json()}")
    return r.json()["id"]

def crear_proceso():
    payload = {
        "nombre": "Test Proceso",
        "descripcion": "Proceso de test",
        "frecuencia": 1,
        "temporalidad": "mes",
        "fecha_inicio": "2024-01-01",
        "fecha_fin": "2024-12-31",
        "inicia_dia_1": True
    }
    r = requests.post(f"{BASE_URL}/procesos", json=payload)
    print(f"POST /procesos: {r.status_code} → {r.json()}")
    return r.json()["id"]

def crear_hito(id_proceso):
    payload = {        
        "nombre": "Hito de test",
        "frecuencia": 1,
        "temporalidad": "mes",
        "fecha_inicio": "2024-01-01",
    }
    r = requests.post(f"{BASE_URL}/hitos", json=payload)
    print(f"POST /hitos: {r.status_code} → {r.json()}")
    return r.json()["id"]

def asociar_proceso_hito_maestro(id_proceso, id_hito):
    payload = {
        "id_proceso": id_proceso,
        "id_hito": id_hito
    }
    r = requests.post(f"{BASE_URL}/proceso-hitos", json=payload)
    print(f"POST /proceso-hitos: {r.status_code} → {r.json()}")

def asignar_proceso_plantilla(id_plantilla, id_proceso):
    payload = {
        "id_proceso": id_proceso
    }
    r = requests.post(f"{BASE_URL}/plantillas/{id_plantilla}/procesos", json=payload)
    print(f"POST /plantillas/{id_plantilla}/procesos: {r.status_code} → {r.json()}")

def crear_cliente_proceso(id_proceso):
    payload = {
        "idcliente": "1",
        "id_proceso": id_proceso,
        "fecha_inicio": "2024-05-01",
        "fecha_fin": "2024-12-31",
        "mes": 5,
        "anio": 2024,
        "id_anterior": None
    }
    r = requests.post(f"{BASE_URL}/cliente-procesos", json=payload)
    print(f"POST /cliente-procesos: {r.status_code} → {r.json()}")
    return r.json()["id"]

def limpiar():
    db: Session = SessionLocal()

    # --- Limpieza previa opcional (solo para tests controlados) ---
    db.query(ClienteProcesoHito).delete()
    db.query(ClienteProceso).delete()
    db.query(ProcesoHitoMaestro).delete()
    db.query(PlantillaProceso).delete()
    db.query(Hito).delete()
    db.query(Proceso).delete()
    db.query(Plantilla).delete()
    db.commit()

def main():
    test_health()
    limpiar()  # Limpia la base de datos antes de crear nuevos registros
    print("✅ FIN LIMPIEZA")
    id_plantilla = crear_plantilla()
    id_proceso = crear_proceso()
    id_hito = crear_hito(id_proceso)
    asociar_proceso_hito_maestro(id_proceso, id_hito)
    asignar_proceso_plantilla(id_plantilla, id_proceso)
    crear_cliente_proceso(id_proceso)
    print("✅ FIN TEST OK ✅")

if __name__ == "__main__":
    main()
