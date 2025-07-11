#!/usr/bin/env python3
"""
Script simple para probar la conexión a PostgreSQL sin SQLAlchemy.
"""

import psycopg2
import sys

def test_postgres_connection():
    """Prueba la conexión directa a PostgreSQL."""
    connection_params = {
        'host': 'localhost',
        'port': 5432,
        'database': 'laboratorio_clinico',
        'user': 'ferju',
        'password': '1003',
        'client_encoding': 'utf8'
    }
    
    try:
        print("🔍 Probando conexión directa a PostgreSQL...")
        print(f"📊 Parámetros: {connection_params['host']}:{connection_params['port']}/{connection_params['database']}")
        
        # Intentar conexión
        conn = psycopg2.connect(**connection_params)
        
        # Crear cursor y ejecutar query simple
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        
        print("✅ Conexión exitosa!")
        print(f"📋 Versión de PostgreSQL: {version[0]}")
        
        # Verificar si la base de datos existe
        cursor.execute("SELECT current_database();")
        db_name = cursor.fetchone()
        print(f"🗄️ Base de datos actual: {db_name[0]}")
        
        # Cerrar conexión
        cursor.close()
        conn.close()
        
        return True
        
    except psycopg2.OperationalError as e:
        print(f"❌ Error de conexión: {e}")
        print("\n💡 Posibles soluciones:")
        print("1. Verificar que PostgreSQL esté ejecutándose")
        print("2. Verificar que la base de datos 'laboratorio_clinico' exista")
        print("3. Verificar usuario y contraseña")
        print("4. Verificar que el puerto 5432 esté disponible")
        return False
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def create_database_if_not_exists():
    """Crea la base de datos si no existe."""
    try:
        print("\n🔍 Verificando si la base de datos existe...")
        
        # Conectar a postgres (base de datos por defecto)
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            database='postgres',
            user='ferju',
            password='1003',
            client_encoding='utf8'
        )
        
        cursor = conn.cursor()
        
        # Verificar si la base de datos existe
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'laboratorio_clinico';")
        exists = cursor.fetchone()
        
        if not exists:
            print("📝 Creando base de datos 'laboratorio_clinico'...")
            cursor.execute("CREATE DATABASE laboratorio_clinico;")
            conn.commit()
            print("✅ Base de datos creada exitosamente")
        else:
            print("✅ La base de datos 'laboratorio_clinico' ya existe")
        
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error al crear/verificar base de datos: {e}")
        return False

def main():
    """Función principal."""
    print("🧪 Iniciando pruebas de conexión a PostgreSQL...")
    
    # Primero intentar crear la base de datos si no existe
    if not create_database_if_not_exists():
        print("❌ No se pudo crear/verificar la base de datos")
        sys.exit(1)
    
    # Luego probar la conexión
    if not test_postgres_connection():
        print("❌ No se pudo conectar a la base de datos")
        sys.exit(1)
    
    print("\n🎉 Todas las pruebas de conexión pasaron!")
    print("🚀 Puedes iniciar el servidor backend ahora.")

if __name__ == "__main__":
    main() 