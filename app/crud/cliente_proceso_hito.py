from app.models.cliente_proceso_hito import ClienteProcesoHito

def create(db, data: dict):
    nuevo = ClienteProcesoHito(**data)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_estado(db, id: int, nuevo_estado: str):
    hito = db.query(ClienteProcesoHito).get(id)
    if hito:
        hito.estado = nuevo_estado
        db.commit()
        db.refresh(hito)
    return hito

def get_by_cliente_proceso(db, cliente_proceso_id: int):
    return db.query(ClienteProcesoHito).filter_by(cliente_proceso_id=cliente_proceso_id).all()
