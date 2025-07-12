from pydantic import BaseModel, ConfigDict
from typing import List, Optional
import datetime

class PacienteBase(BaseModel):
    nombre_completo: str
    documento: str
    fecha_nacimiento: datetime.date
    genero: str

class PacienteCreate(PacienteBase):
    contraseña: str

class Paciente(PacienteBase):
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
    """Properties to return to client for an OrderExam."""
    id: int
    resultados: Optional[str]
    fecha_resultado: Optional[datetime.datetime]
    examen: Examen
    model_config = ConfigDict(from_attributes=True)

class OrdenBase(BaseModel):
    """Base properties for an Order."""
    estado: str
    paciente_id: int

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