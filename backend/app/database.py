from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_DATABASE_URL = "mysql+pymysql://root:1003@localhost:3306/laboratorio_clinico?charset=utf8mb4"

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)

print(f"🔗 Conectando a la base de datos: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,  # Verificar conexión antes de usar
    pool_recycle=300,    # Reciclar conexiones cada 5 minutos
    echo=False           # No mostrar queries SQL en consola
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()