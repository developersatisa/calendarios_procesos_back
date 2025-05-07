from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime, date
from app.models.proceso import Proceso
from app.models.cliente_proceso import ClienteProceso

def validar_existencia(session: Session, model, id_value: int, nombre_modelo: str):
    objeto = session.query(model).get(id_value)
    if not objeto:
        raise HTTPException(status_code=404, detail=f"{nombre_modelo} con ID {id_value} no encontrado")
    return objeto

def validar_fk(session: Session, model, field_name: str, value, nombre_modelo: str):
    if not session.query(model).filter(getattr(model, field_name) == value).first():
        raise HTTPException(status_code=400, detail=f"{nombre_modelo} con valor {value} no existe")

def validar_fechas(fecha_inicio: date, fecha_fin: date):
    if fecha_fin and fecha_inicio > fecha_fin:
        raise HTTPException(
            status_code=400,
            detail="La fecha de inicio no puede ser posterior a la fecha de fin."
        )

def validar_creacion_proceso(data: dict):
    if 'frecuencia' in data and not isinstance(data['frecuencia'], int):
        raise HTTPException(status_code=400, detail="Frecuencia debe ser un número entero")
    if 'temporalidad' in data and data['temporalidad'] not in ['día', 'mes', 'año']:
        raise HTTPException(status_code=400, detail="Temporalidad debe ser: día, mes o año")
    if 'fecha_inicio' in data and 'fecha_fin' in data:
        validar_fechas(data['fecha_inicio'], data['fecha_fin'])

def validar_creacion_cliente_proceso(db: Session, data: dict):
    validar_fk(db, Proceso, 'id', data['id_proceso'], 'Proceso')
    if 'fecha_inicio' in data and 'fecha_fin' in data:
        validar_fechas(data['fecha_inicio'], data['fecha_fin'])
    if 'id_anterior' in data and data['id_anterior'] is not None:
        validar_fk(db, ClienteProceso, 'id', data['id_anterior'], 'ClienteProceso')

def validar_cliente_proceso(db: Session, data: dict):
    # Validar que el proceso existe
    proceso = db.query(Proceso).filter(Proceso.id == data.get("id_proceso")).first()
    if not proceso:
        raise HTTPException(status_code=400, detail=f"Proceso con id={data.get('id_proceso')} no existe.")

    # Validar que el cliente existe en SQL Server (tabla externa)
    try:
        stmt = text("SELECT 1 FROM dbo.clientes WHERE idcliente = :idcliente")
        result = db.execute(stmt, {"idcliente": data["idcliente"]})
        if not result.fetchone():
            raise HTTPException(status_code=400, detail=f"Cliente con idcliente={data['idcliente']} no existe.")
    except ValueError:
        raise HTTPException(status_code=500, detail="Error validando cliente externo")

    if 'fecha_inicio' in data and 'fecha_fin' in data:
        validar_fechas(data['fecha_inicio'], data['fecha_fin'])
        
    return True

def validar_proceso(data: dict):
    if 'nombre' in data and not isinstance(data['nombre'], str):
        raise HTTPException(status_code=400, detail="Nombre debe ser una cadena de texto")
    if 'descripcion' in data and not isinstance(data['descripcion'], str):
        raise HTTPException(status_code=400, detail="Descripción debe ser una cadena de texto")
    if 'frecuencia' in data and not isinstance(data['frecuencia'], int):
        raise HTTPException(status_code=400, detail="Frecuencia debe ser un número entero")
    if 'temporalidad' in data and data['temporalidad'] not in ['día', 'mes', 'año']:
        raise HTTPException(status_code=400, detail="Temporalidad debe ser: día, mes o año")
    try:
        if 'fecha_inicio' in data:
            if isinstance(data['fecha_inicio'], str):
                data['fecha_inicio'] = datetime.strptime(data['fecha_inicio'], "%Y-%m-%d").date()
            elif not isinstance(data['fecha_inicio'], date):
                raise ValueError
    except ValueError:
        raise HTTPException(status_code=400, detail="Fecha de inicio debe tener formato YYYY-MM-DD")