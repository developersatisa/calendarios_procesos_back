from app.models.proceso_hito_maestro import ProcesoHitoMaestro

def create(db, data):
    nuevo = ProcesoHitoMaestro(**data)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_todos(db):
    return db.query(ProcesoHitoMaestro).all()

def obtener_por_id(db, id):
    return db.query(ProcesoHitoMaestro).filter(ProcesoHitoMaestro.id == id).first()

def actualizar(db, id, data):
    registro = obtener_por_id(db, id)
    if not registro:
        return None
    for key, value in data.items():
        setattr(registro, key, value)
    db.commit()
    db.refresh(registro)
    return registro

def eliminar(db, id):
    registro = obtener_por_id(db, id)
    if not registro:
        return None
    db.delete(registro)
    db.commit()
    return True
