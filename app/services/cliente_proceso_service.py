from app.crud import cliente_proceso as crud
from app.crud import cliente_proceso_hito as crud_cliente_proceso_hito
from app.models.proceso_hito_maestro import ProcesoHitoMaestro
from app.utils import validators


def crear(db, data):
    validators.validar_cliente_proceso(db, data)    
    cliente_proceso = crud.create(db, data)
    # 👇 Lógica para duplicar hitos del proceso al cliente_proceso
    hitos_maestro = db.query(ProcesoHitoMaestro).filter_by(id_proceso=data["id_proceso"]).all()

    for hito in hitos_maestro:
        hito_data = {
            "cliente_proceso_id": cliente_proceso.id,
            "hito_id": hito.id,
            "estado": "pendiente"
        }
        crud_cliente_proceso_hito.create(db, hito_data)

    return cliente_proceso

def obtener_todos(db):
    return crud.obtener_todos(db)

def obtener_por_id(db, id):
    return crud.obtener_por_id(db, id)

def actualizar(db, id, data):
    return crud.actualizar(db, id, data)

def eliminar(db, id):
    return crud.eliminar(db, id)
