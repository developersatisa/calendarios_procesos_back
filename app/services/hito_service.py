from app.crud import hito as crud_hito

def crear(db, data):
    return crud_hito.create_hito(db, data)

def obtener_todos(db):
    return crud_hito.obtener_todos(db)

def obtener_por_id(db, id):
    return crud_hito.obtener_por_id(db, id)

def actualizar(db, id, data):
    return crud_hito.actualizar(db, id, data)

def eliminar(db, id):
    return crud_hito.eliminar(db, id)
