from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine, Base
import uuid

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/pacientes/", response_model=schemas.Paciente)
def crear_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    db_paciente = models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@app.get("/pacientes/", response_model=list[schemas.Paciente])
def listar_pacientes(db: Session = Depends(get_db)):
    return db.query(models.Paciente).all()

@app.post("/ordenes/", response_model=schemas.Orden)
def crear_orden(orden: schemas.OrdenCreate, db: Session = Depends(get_db)):
    numero_orden = str(uuid.uuid4())[:8]
    db_orden = models.Orden(
        numero_orden=numero_orden,
        estado=orden.estado,
        paciente_id=orden.paciente_id
    )
    db.add(db_orden)
    db.commit()
    db.refresh(db_orden)
    for ex in orden.examenes:
        db_examen = models.OrdenExamen(
            id_orden=db_orden.id,
            id_examen=ex.id_examen
        )
        db.add(db_examen)
    db.commit()
    db.refresh(db_orden)
    return db_orden

@app.get("/ordenes/{documento}", response_model=list[schemas.Orden])
def listar_ordenes_por_documento(documento: str, db: Session = Depends(get_db)):
    paciente = db.query(models.Paciente).filter_by(documento=documento).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db.query(models.Orden).filter_by(paciente_id=paciente.id).all()

@app.get("/orden/{orden_id}", response_model=schemas.Orden)
def detalle_orden(orden_id: int, db: Session = Depends(get_db)):
    orden = db.query(models.Orden).filter_by(id=orden_id).first()
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return orden