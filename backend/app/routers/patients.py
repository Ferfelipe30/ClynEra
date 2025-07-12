from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from typing import List
import bcrypt

from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/pacientes",
    tags=["pacientes"],
)

@router.post("/login")
def login_paciente(
    documento: str = Body(...), 
    contraseña: str = Body(...), 
    db: Session = Depends(get_db)
):
    paciente = crud.get_paciente_by_documento(db, documento=documento)
    if not paciente or not bcrypt.checkpw(contraseña.encode(), paciente.contraseña.encode()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return {"message": "Login exitoso", "paciente_id": paciente.id}

@router.post("/", response_model=schemas.Paciente, status_code=201)
def create_paciente_endpoint(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    db_paciente = crud.get_paciente_by_documento(db, documento=paciente.documento)
    if db_paciente:
        raise HTTPException(status_code=400, detail="El documento ya esta registrado")
    return crud.create_paciente(db=db, paciente=paciente)

@router.get("/", response_model=List[schemas.Paciente])
def get_pacientes_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pacientes = crud.get_pacientes(db, skip=skip, limit=limit)
    return pacientes

@router.get("/{paciente_id}", response_model=schemas.Paciente)
def get_paciente_endpoint(paciente_id: int, db: Session = Depends(get_db)):
    """
    Obtener un paciente por ID.
    """
    paciente = crud.get_paciente_by_id(db, paciente_id=paciente_id)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@router.put("/{paciente_id}", response_model=schemas.Paciente)
def update_paciente_endpoint(paciente_id: int, paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    """
    Actualizar un paciente existente.
    """
    db_paciente = crud.update_paciente(db, paciente_id=paciente_id, paciente=paciente)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_paciente

@router.delete("/{paciente_id}")
def delete_paciente_endpoint(paciente_id: int, db: Session = Depends(get_db)):
    """
    Eliminar un paciente.
    """
    success = crud.delete_paciente(db, paciente_id=paciente_id)
    if not success:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"message": "Paciente eliminado correctamente"}