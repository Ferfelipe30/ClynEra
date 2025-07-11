from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def get_paciente_by_documento(db: Session, documento: str) -> models.Paciente | None:
    return db.query(models.Paciente).filter(models.Paciente.documento == documento).first()

def get_paciente_by_id(db: Session, paciente_id: int) -> models.Paciente | None:
    return db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()

def get_pacientes(db: Session, skip: int = 0, limit: int = 100) -> List[models.Paciente]:
    return db.query(models.Paciente).offset(skip).limit(limit).all()

def create_paciente(db: Session, paciente: schemas.PacienteCreate) -> models.Paciente:
    db_paciente = models.Paciente(**paciente.model_dump())
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