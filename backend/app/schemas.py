from pydantic import BaseModel, ConfigDict
from typing import List, Optional
import datetime

class PacienteBase(BaseModel):
    """Base properties for a Patient."""
    nombre_completo: str
    documento: str
    fecha_nacimiento: datetime.date
    genero: str

class PacienteCreate(PacienteBase):
    """Properties to receive via API on patient creation."""
    pass

class Paciente(PacienteBase):
    """Properties to return to client."""
    id: int
    model_config = ConfigDict(from_attributes=True)

class ExamenBase(BaseModel):
    """Base properties for an Exam."""
    nombre: str
    area: str

class Examen(ExamenBase):
    """Properties to return to client for an Exam."""
    id: int
    model_config = ConfigDict(from_attributes=True)

class OrdenExamenBase(BaseModel):
    """Base properties for an OrderExam."""
    id_examen: int

class OrdenExamenCreate(OrdenExamenBase):
    """Properties to receive on OrderExam creation, linked to an Order."""
    pass

class OrdenExamen(OrdenExamenBase):
    id: int
    id_orden: int
    id_examen: int
    resultado: str | None = None
    fecha_resultado: datetime.datetime | None = None
    examen: Examen | None

    class Config:
        orm_mode = True

class OrdenBase(BaseModel):
    id: int
    numero_orden: str
    fecha_creacion: datetime.datetime
    id_paciente: int
    estado: str
    paciente: Paciente | None
    examenes: List[OrdenExamen] = []

    class Config:
        orm_mode = True

class OrdenCreate(OrdenBase):
    """Properties to receive on Order creation."""
    examenes: List[OrdenExamenCreate]

class Orden(OrdenBase):
    """Properties to return to client for an Order."""
    id: int
    numero_orden: str
    fecha_creacion: datetime.datetime
    paciente: Paciente
    examenes: List[OrdenExamen]
    model_config = ConfigDict(from_attributes=True)