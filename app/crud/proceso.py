from app.models.proceso import Proceso

def create_proceso(db, data):
    nuevo = Proceso(**data)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_todos(db):
    return db.query(Proceso).all()

def obtener_por_id(db, id):
    return db.query(Proceso).filter(Proceso.id == id).first()

def actualizar(db, id, data):
    proceso = obtener_por_id(db, id)
    if not proceso:
        return None
    for key, value in data.items():
        setattr(proceso, key, value)
    db.commit()
    db.refresh(proceso)
    return proceso

def eliminar(db, id):
    proceso = obtener_por_id(db, id)
    if not proceso:
        return None
    db.delete(proceso)
    db.commit()
    return True
