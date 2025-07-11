#!/usr/bin/env python3
"""
Script para inicializar la base de datos MySQL con las tablas necesarias.
"""

import pymysql
import sys

def create_database_and_tables():
    """Crea la base de datos y las tablas."""
    try:
        # Conectar a MySQL (sin especificar base de datos)
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        
        # Crear base de datos si no existe
        print("🔍 Creando base de datos 'laboratorio_clinico'...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS laboratorio_clinico CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✅ Base de datos creada/verificada exitosamente")
        
        # Usar la base de datos
        cursor.execute("USE laboratorio_clinico")
        
        # Crear tabla paciente
        print("📋 Creando tabla 'paciente'...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS paciente (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre_completo VARCHAR(100) NOT NULL,
                documento VARCHAR(20) NOT NULL UNIQUE,
                fecha_nacimiento DATE NOT NULL,
                genero ENUM('Masculino', 'Femenino', 'Otro') NOT NULL
            )
        """)
        
        # Crear tabla examen
        print("📋 Creando tabla 'examen'...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS examen (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                area VARCHAR(50) NOT NULL
            )
        """)
        
        # Crear tabla orden
        print("📋 Creando tabla 'orden'...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orden (
                id INT AUTO_INCREMENT PRIMARY KEY,
                numero_orden VARCHAR(20) NOT NULL UNIQUE,
                fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                id_paciente INT NOT NULL,
                estado ENUM('Pendiente', 'En proceso', 'Completado') DEFAULT 'Pendiente',
                FOREIGN KEY (id_paciente) REFERENCES paciente(id)
            )
        """)
        
        # Crear tabla orden_examen
        print("📋 Creando tabla 'orden_examen'...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orden_examen (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_orden INT NOT NULL,
                id_examen INT NOT NULL,
                resultado TEXT,
                fecha_resultado DATETIME,
                FOREIGN KEY (id_orden) REFERENCES orden(id) ON DELETE CASCADE,
                FOREIGN KEY (id_examen) REFERENCES examen(id)
            )
        """)
        
        # Insertar datos de prueba
        print("📝 Insertando datos de prueba...")
        
        # Verificar si ya hay datos
        cursor.execute("SELECT COUNT(*) FROM paciente")
        result = cursor.fetchone()
        if result is not None and result[0] == 0:
            # Insertar pacientes de prueba
            cursor.execute("""
                INSERT INTO paciente (nombre_completo, documento, fecha_nacimiento, genero) VALUES
                ('Laura Sánchez', '12345678', '1995-05-10', 'Femenino'),
                ('Carlos Méndez', '87654321', '1988-11-23', 'Masculino')
            """)
            
            # Insertar exámenes de prueba
            cursor.execute("""
                INSERT INTO examen (nombre, area) VALUES
                ('Hemograma', 'Hematología'),
                ('Glucosa', 'Química'),
                ('Perfil Lipídico', 'Química'),
                ('Orina Completa', 'Uroanálisis')
            """)
            
            # Insertar órdenes de prueba
            cursor.execute("""
                INSERT INTO orden (numero_orden, id_paciente, estado) VALUES
                ('20250708-001', 1, 'Pendiente'),
                ('20250708-002', 2, 'En proceso')
            """)
            
            # Insertar orden_examen de prueba
            cursor.execute("""
                INSERT INTO orden_examen (id_orden, id_examen, resultado, fecha_resultado) VALUES
                (1, 1, NULL, NULL),
                (1, 2, NULL, NULL),
                (2, 3, 'Colesterol Total: 200 mg/dL', '2025-07-08 09:00:00'),
                (2, 4, NULL, NULL)
            """)
            
            print("✅ Datos de prueba insertados exitosamente")
        else:
            print("ℹ️ Los datos de prueba ya existen")
        
        connection.commit()
        cursor.close()
        connection.close()
        
        print("\n🎉 Base de datos MySQL inicializada correctamente!")
        print("🚀 Puedes iniciar el servidor backend ahora.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al inicializar la base de datos: {e}")
        print("\n💡 Asegúrate de que:")
        print("1. MySQL esté instalado y ejecutándose")
        print("2. El usuario 'root' tenga permisos")
        print("3. El puerto 3306 esté disponible")
        return False

if __name__ == "__main__":
    print("🧪 Inicializando base de datos MySQL...")
    if create_database_and_tables():
        sys.exit(0)
    else:
        sys.exit(1) 