from sqlalchemy import Column, Integer, String, Date, ForeingKey, DateTime, Text
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Paciente(Base):
    __tablename__ = "paciente"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    documento = Column(String, unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(String, nullable=False)
    ordenes = relationship("Orden", back_populates="paciente")
    
class Examen(Base):
    __tablename__ = "examen"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    area = Column(String, nullable=False)
    
class Orden(Base):
    __tablename__ = "orden"
    id = Column(Integer, primary_key=True, index=True)
    numero_orden = Column (String, unique=True, nullable=False)
    fecha_creacion = Column (DateTime, default=datetime.datetime.utcnow)
    estado = Column (String, nullable=False)
    paciente_id = Column (Integer, ForeingKey("paciente.id"))
    paciente = relationship ("Paciente", back_populates="ordenes")
    examenes = relationship ("OrdenExamen", back_populates="orden")
    
class OrdenExamen(Base):
    __tablename__ = "orden_examen"
    id = Column(Integer, primary_key=True, index=True)
    id_orden = Column(Integer, ForeignKey("orden.id"))
    id_examen = Column(Integer, ForeignKey("examen.id"))
    resultado = Column(Text)
    fecha_resultado = Column(DateTime)
    orden = relationship("Orden", back_populates="examenes")
    examen = relationship("Examen")