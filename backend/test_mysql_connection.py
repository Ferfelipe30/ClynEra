#!/usr/bin/env python3
"""
Script para probar la conexión a MySQL.
"""

import pymysql
import sys

def test_mysql_connection():
    """Prueba la conexión directa a MySQL."""
    connection_params = {
        'host': 'localhost',
        'port': 3307,
        'database': 'laboratorio_clinico',
        'user': 'root',
        'password': 'root_password',
        'charset': 'utf8mb4'
    }
    
    try:
        print("🔍 Probando conexión directa a MySQL...")
        print(f"📊 Parámetros: {connection_params['host']}:{connection_params['port']}/{connection_params['database']}")
        
        # Intentar conexión
        conn = pymysql.connect(**connection_params)
        
        # Crear cursor y ejecutar query simple
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        
        print("✅ Conexión exitosa!")
        if version is not None:
            print(f"📋 Versión de MySQL: {version[0]}")
        else:
            print("📋 No se pudo obtener la versión de MySQL.")
        
        # Verificar si la base de datos existe
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        if db_name and db_name[0]:
            print(f"🗄️ Base de datos actual: {db_name[0]}")
        else:
            print("🗄️ No se seleccionó ninguna base de datos.")

        # Verificar tablas existentes
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print(f"📋 Tablas encontradas: {len(tables)}")
        for table in tables:
            print(f"   - {table[0]}")
        
        # Cerrar conexión
        cursor.close()
        conn.close()
        
        return True
        
    except pymysql.Error as e:
        print(f"❌ Error de conexión: {e}")
        print("\n💡 Posibles soluciones:")
        print("1. Verificar que MySQL esté ejecutándose en Docker")
        print("2. Verificar que el puerto 3307 esté disponible")
        print("3. Verificar usuario y contraseña")
        print("4. Ejecutar: docker-compose up -d")
        return False
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def test_sqlalchemy_connection():
    """Prueba la conexión usando SQLAlchemy."""
    try:
        print("\n🔍 Probando conexión con SQLAlchemy...")
        
        from sqlalchemy import create_engine, text
        from app.database import SQLALCHEMY_DATABASE_URL
        
        print(f"📊 URL de conexión: {SQLALCHEMY_DATABASE_URL}")
        
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        
        with engine.connect() as connection:
            result = connection.execute(text("SELECT VERSION();"))
            version = result.fetchone()
            print(f"✅ Conexión SQLAlchemy exitosa!")
            if version and version[0]:
                print(f"📋 Versión de MySQL: {version[0]}")
            else:
                print("📋 No se pudo obtener la versión de MySQL.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en conexión SQLAlchemy: {e}")
        return False

def main():
    """Función principal."""
    print("🧪 Iniciando pruebas de conexión a MySQL...")
    
    # Probar conexión directa
    if not test_mysql_connection():
        print("❌ No se pudo conectar directamente a MySQL")
        sys.exit(1)
    
    # Probar conexión con SQLAlchemy
    if not test_sqlalchemy_connection():
        print("❌ No se pudo conectar con SQLAlchemy")
        sys.exit(1)
    
    print("\n🎉 Todas las pruebas de conexión pasaron!")
    print("🚀 Puedes iniciar el servidor backend ahora.")

if __name__ == "__main__":
    main() 