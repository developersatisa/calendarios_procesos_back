from app.crud import cliente_proceso_hito as crud

def crear(db, data: dict):
    return crud.create(db, data)

def actualizar_estado(db, id: int, estado: str):
    return crud.update_estado(db, id, estado)

def listar_por_cliente_proceso(db, cliente_proceso_id: int):
    return crud.get_by_cliente_proceso(db, cliente_proceso_id)
