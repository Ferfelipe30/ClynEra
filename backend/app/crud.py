from sqlalchemy.orm import Session
from . import models, schemas
from typing import List
import datetime
import random
import string
import bcrypt

def get_paciente_by_documento(db: Session, documento: str) -> models.Paciente | None:
    return db.query(models.Paciente).filter(models.Paciente.documento == documento).first()

def get_paciente_by_id(db: Session, paciente_id: int) -> models.Paciente | None:
    return db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()

def get_pacientes(db: Session, skip: int = 0, limit: int = 100) -> List[models.Paciente]:
    return db.query(models.Paciente).offset(skip).limit(limit).all()

def create_paciente(db: Session, paciente: schemas.PacienteCreate):
    hashed = bcrypt.hashpw(paciente.contraseña.encode(), bcrypt.gensalt()).decode()
    paciente_dict = paciente.model_dump()
    paciente_dict['contraseña'] = hashed
    db_paciente = models.Paciente(**paciente_dict)
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def update_paciente(db: Session, paciente_id: int, paciente: schemas.PacienteCreate) -> models.Paciente | None:
    db_paciente = db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()
    if db_paciente:
        for key, value in paciente.model_dump().items():
            setattr(db_paciente, key, value)
        db.commit()
        db.refresh(db_paciente)
    return db_paciente

def delete_paciente(db: Session, paciente_id: int) -> bool:
    db_paciente = db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()
    if db_paciente:
        db.delete(db_paciente)
        db.commit()
        return True
    return False

# CRUD operations for exams
def get_examenes(db: Session, skip: int = 0, limit: int = 100) -> List[models.Examen]:
    return db.query(models.Examen).offset(skip).limit(limit).all()

def get_examen_by_id(db: Session, examen_id: int) -> models.Examen | None:
    return db.query(models.Examen).filter(models.Examen.id == examen_id).first()

def create_examen(db: Session, examen: schemas.ExamenBase) -> models.Examen:
    db_examen = models.Examen(**examen.model_dump())
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen

# CRUD operations for orders
def generate_order_number() -> str:
    """Generate a unique order number."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    random_suffix = ''.join(random.choices(string.digits, k=3))
    return f"{timestamp}-{random_suffix}"

def get_ordenes(db: Session, skip: int = 0, limit: int = 100) -> List[models.Orden]:
    return db.query(models.Orden).offset(skip).limit(limit).all()

def get_orden_by_id(db: Session, orden_id: int) -> models.Orden | None:
    return db.query(models.Orden).filter(models.Orden.id == orden_id).first()

def create_orden(db: Session, orden_data: dict) -> models.Orden:
    """Create a new order with exams."""
    # Generate order number
    numero_orden = generate_order_number()
    
    # Create the order
    db_orden = models.Orden(
        numero_orden=numero_orden,
        id_paciente=orden_data["paciente_id"],
        estado="Pendiente"
    )
    db.add(db_orden)
    db.commit()
    db.refresh(db_orden)
    
    # Add exams to the order
    for examen_id in orden_data["examen_ids"]:
        db_orden_examen = models.OrdenExamen(
            id_orden=db_orden.id,
            id_examen=examen_id
        )
        db.add(db_orden_examen)
    
    db.commit()
    db.refresh(db_orden)
    return db_orden

def update_orden(db: Session, orden_id: int, orden_data: dict) -> models.Orden | None:
    db_orden = db.query(models.Orden).filter(models.Orden.id == orden_id).first()
    if db_orden:
        for key, value in orden_data.items():
            if hasattr(db_orden, key):
                setattr(db_orden, key, value)
        db.commit()
        db.refresh(db_orden)
    return db_orden

def delete_orden(db: Session, orden_id: int) -> bool:
    db_orden = db.query(models.Orden).filter(models.Orden.id == orden_id).first()
    if db_orden:
        db.delete(db_orden)
        db.commit()
        return True
    return False