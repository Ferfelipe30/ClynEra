from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# Default database URL for MySQL (Docker)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:root_password@localhost:3307/laboratorio_clinico?charset=utf8mb4")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,  # Verificar conexión antes de usar
    pool_recycle=300,    # Reciclar conexiones cada 5 minutos
    echo=False           # No mostrar queries SQL en consola
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass