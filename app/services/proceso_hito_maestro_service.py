from app.crud import proceso_hito_maestro as crud

def crear(db, data):
    return crud.create(db, data)

def obtener_todos(db):
    return crud.obtener_todos(db)

def obtener_por_id(db, id):
    return crud.obtener_por_id(db, id)

def actualizar(db, id, data):
    return crud.actualizar(db, id, data)

def eliminar(db, id):
    return crud.eliminar(db, id)
