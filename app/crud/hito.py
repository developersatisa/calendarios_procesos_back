from app.models.hito import Hito

def create_hito(db, data):
    nuevo = Hito(**data)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_todos(db):
    return db.query(Hito).all()

def obtener_por_id(db, id):
    return db.query(Hito).filter(Hito.id == id).first()

def actualizar(db, id, data):
    hito = obtener_por_id(db, id)
    if not hito:
        return None
    for key, value in data.items():
        setattr(hito, key, value)
    db.commit()
    db.refresh(hito)
    return hito

def eliminar(db, id):
    hito = obtener_por_id(db, id)
    if not hito:
        return None
    db.delete(hito)
    db.commit()
    return True
