#!/usr/bin/env python3
"""
Script para inicializar la base de datos y verificar la conexión.
"""

import sys
import os
from sqlalchemy import text
from app.database import engine, SessionLocal
from app.models import Base

def test_database_connection():
    """Prueba la conexión a la base de datos."""
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ Conexión a la base de datos exitosa")
            return True
    except Exception as e:
        print(f"❌ Error de conexión a la base de datos: {e}")
        print("\n💡 Intentando conexión alternativa...")
        
        # Intentar conexión directa con psycopg2
        try:
            import psycopg2
            conn = psycopg2.connect(
                host='localhost',
                port=5432,
                database='laboratorio_clinico',
                user='ferju',
                password='1003',
                client_encoding='utf8'
            )
            conn.close()
            print("✅ Conexión alternativa exitosa")
            return True
        except Exception as e2:
            print(f"❌ Conexión alternativa también falló: {e2}")
            return False

def create_tables():
    """Crea las tablas en la base de datos."""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tablas creadas exitosamente")
        return True
    except Exception as e:
        print(f"❌ Error al crear las tablas: {e}")
        return False

def verify_tables():
    """Verifica que las tablas existan."""
    try:
        with engine.connect() as connection:
            # Verificar si la tabla paciente existe
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'paciente'
            """))
            if result.fetchone():
                print("✅ Tabla 'paciente' existe")
            else:
                print("❌ Tabla 'paciente' no existe")
                return False
            
            # Verificar si la tabla examen existe
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'examen'
            """))
            if result.fetchone():
                print("✅ Tabla 'examen' existe")
            else:
                print("❌ Tabla 'examen' no existe")
                return False
            
            # Verificar si la tabla orden existe
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'orden'
            """))
            if result.fetchone():
                print("✅ Tabla 'orden' existe")
            else:
                print("❌ Tabla 'orden' no existe")
                return False
            
            # Verificar si la tabla orden_examen existe
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'orden_examen'
            """))
            if result.fetchone():
                print("✅ Tabla 'orden_examen' existe")
            else:
                print("❌ Tabla 'orden_examen' no existe")
                return False
            
            return True
    except Exception as e:
        print(f"❌ Error al verificar las tablas: {e}")
        return False

def main():
    """Función principal."""
    print("🔍 Inicializando base de datos...")
    print(f"📊 URL de la base de datos: {engine.url}")
    
    # Probar conexión
    if not test_database_connection():
        sys.exit(1)
    
    # Crear tablas
    if not create_tables():
        sys.exit(1)
    
    # Verificar tablas
    if not verify_tables():
        sys.exit(1)
    
    print("\n🎉 Base de datos inicializada correctamente!")
    print("🚀 Puedes iniciar el servidor backend ahora.")

if __name__ == "__main__":
    main() 