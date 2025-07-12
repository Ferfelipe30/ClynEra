from fastapi import FastAPI, HTTPException
from typing import List
import datetime
import random
import string
from fastapi.middleware.cors import CORSMiddleware

# Importa los esquemas que creaste
from . import schemas
from .routers.patients import router as patients_router
from .database import engine, Base, SessionLocal
from . import models, crud

# Crea una instancia de la aplicación FastAPI
app = FastAPI(
    title="ClynEra API",
    description="API para la gestión de pacientes y órdenes de examen.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # Alternative dev port
        "http://127.0.0.1:5173",  # Alternative localhost
        "http://127.0.0.1:3000",  # Alternative localhost
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(patients_router)

# Create database tables with error handling
try:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")
except Exception as e:
    print(f"Warning: Could not create database tables: {e}")
    print("The application will continue but database operations may fail.")

@app.get("/")
def read_root():
    """
    Un endpoint raíz para confirmar que la API está funcionando.
    """
    return {"message": "Bienvenido a la API de ClynEra"}



# Endpoints for exams
@app.get("/examenes", response_model=List[schemas.Examen])
def get_examenes_endpoint(skip: int = 0, limit: int = 100):
    """
    Obtener lista de exámenes.
    """
    db = SessionLocal()
    try:
        examenes = crud.get_examenes(db, skip=skip, limit=limit)
        return examenes
    finally:
        db.close()

@app.post("/examenes", response_model=schemas.Examen, status_code=201)
def create_examen_endpoint(examen: schemas.ExamenBase):
    """
    Crear un nuevo examen.
    """
    db = SessionLocal()
    try:
        return crud.create_examen(db=db, examen=examen)
    finally:
        db.close()

# Endpoints for orders
@app.get("/ordenes", response_model=List[schemas.Orden])
def get_ordenes_endpoint(skip: int = 0, limit: int = 100):
    """
    Obtener lista de órdenes.
    """
    db = SessionLocal()
    try:
        ordenes = crud.get_ordenes(db, skip=skip, limit=limit)
        return ordenes
    finally:
        db.close()

@app.post("/ordenes", response_model=schemas.Orden, status_code=201)
def create_orden_endpoint(orden_data: dict):
    """
    Crear una nueva orden.
    """
    db = SessionLocal()
    try:
        # Validate required fields
        if "paciente_id" not in orden_data:
            raise HTTPException(status_code=400, detail="paciente_id is required")
        if "examen_ids" not in orden_data:
            raise HTTPException(status_code=400, detail="examen_ids is required")
        
        # Validate patient exists
        paciente = crud.get_paciente_by_id(db, orden_data["paciente_id"])
        if not paciente:
            raise HTTPException(status_code=404, detail="Patient not found")
        
        # Validate exams exist
        for examen_id in orden_data["examen_ids"]:
            examen = crud.get_examen_by_id(db, examen_id)
            if not examen:
                raise HTTPException(status_code=404, detail=f"Exam with id {examen_id} not found")
        
        return crud.create_orden(db=db, orden_data=orden_data)
    finally:
        db.close()

@app.get("/ordenes/{orden_id}", response_model=schemas.Orden)
def get_orden_endpoint(orden_id: int):
    """
    Obtener una orden por ID.
    """
    db = SessionLocal()
    try:
        orden = crud.get_orden_by_id(db, orden_id=orden_id)
        if orden is None:
            raise HTTPException(status_code=404, detail="Order not found")
        return orden
    finally:
        db.close()

@app.put("/ordenes/{orden_id}", response_model=schemas.Orden)
def update_orden_endpoint(orden_id: int, orden_data: dict):
    """
    Actualizar una orden existente.
    """
    db = SessionLocal()
    try:
        orden = crud.update_orden(db, orden_id=orden_id, orden_data=orden_data)
        if orden is None:
            raise HTTPException(status_code=404, detail="Order not found")
        return orden
    finally:
        db.close()

@app.delete("/ordenes/{orden_id}")
def delete_orden_endpoint(orden_id: int):
    """
    Eliminar una orden.
    """
    db = SessionLocal()
    try:
        success = crud.delete_orden(db, orden_id=orden_id)
        if not success:
            raise HTTPException(status_code=404, detail="Order not found")
        return {"message": "Order deleted successfully"}
    finally:
        db.close()