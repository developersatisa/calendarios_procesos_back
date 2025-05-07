from app.crud import proceso as crud_proceso
from app.utils import validators

def crear(db, data):
    validators.validar_proceso(data)
    return crud_proceso.create_proceso(db, data)

def obtener_todos(db):
    return crud_proceso.obtener_todos(db)

def obtener_por_id(db, id):
    return crud_proceso.obtener_por_id(db, id)

def actualizar(db, id, data):
    return crud_proceso.actualizar(db, id, data)

def eliminar(db, id):
    return crud_proceso.eliminar(db, id)
