from pydantic import BaseModel
from typing import List, Optional
import datetime

class PacienteBase(BaseModel):
    nombre: str
    documento: str
    fecha_nacimiento: datetime.date
    genero: str
    
class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id: int
    class Config:
        orm_mode = True
        
class ExamenBase(BaseModel):
    nombre: str
    area: str
    
class Examen(ExamenBase):
    id: int
    class Config:
        orm_mode = True
        
class OrdenExamenBase(BaseModel):
    id_examen: int
    
class OrdenExamenCreate(OrdenExamenBase):
    pass

class OrdenExamen(OrdenExamenBase):
    id: int
    resultados: Optional[str]
    fecha_resultado: Optional[datetime.datetime]
    examen: Examen
    class Config:
        orm_mode = True
        
class OrdenBase(BaseModel):
    estado: str
    paciente_id: int
    
class OrdenCreate(OrdenBase):
    examenes: List[OrdenExamenCreate]
    
class Orden(OrdenBase):
    id: int
    numero_orden: str
    fecha_creacion: datetime.datetime
    examenes: List[OrdenExamen]
    class Config:
        orm_mode = True