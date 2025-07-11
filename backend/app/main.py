from fastapi import FastAPI, HTTPException
from typing import List
import datetime
import random
import string
from fastapi.middleware.cors import CORSMiddleware

# Importa los esquemas que creaste
from . import schemas
from .routers.patients import router as patients_router
from .database import engine
from . import models

# Crea una instancia de la aplicación FastAPI
app = FastAPI(
    title="ClynEra API",
    description="API para la gestión de pacientes y órdenes de examen.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patients_router)

# Create database tables with error handling
try:
    models.Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")
except Exception as e:
    print(f"⚠️ Warning: Could not create database tables: {e}")
    print("The application will continue but database operations may fail.")

@app.get("/")
def read_root():
    """
    Un endpoint raíz para confirmar que la API está funcionando.
    """
    return {"message": "Bienvenido a la API de ClynEra"}