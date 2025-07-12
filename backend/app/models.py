from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Paciente(Base):
    __tablename__ = "paciente"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_completo = Column(String(100), nullable=False)
    documento = Column(String(20), unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(Enum('Masculino', 'Femenino', 'Otro'), nullable=False)
    contraseña = Column(String(128), nullable=False)
    ordenes = relationship("Orden", back_populates="paciente")
    
class Examen(Base):
    __tablename__ = "examen"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    area = Column(String(50), nullable=False)
    
class Orden(Base):
    __tablename__ = "orden"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numero_orden = Column(String(20), unique=True, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.datetime.utcnow)
    id_paciente = Column(Integer, ForeignKey("paciente.id"))
    estado = Column(Enum('Pendiente', 'En proceso', 'Completado'), default='Pendiente')
    paciente = relationship("Paciente", back_populates="ordenes")
    examenes = relationship("OrdenExamen", back_populates="orden")
    
class OrdenExamen(Base):
    __tablename__ = "orden_examen"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_orden = Column(Integer, ForeignKey("orden.id", ondelete="CASCADE"))
    id_examen = Column(Integer, ForeignKey("examen.id"))
    resultado = Column(Text)
    fecha_resultado = Column(DateTime)
    orden = relationship("Orden", back_populates="examenes")
    examen = relationship("Examen")