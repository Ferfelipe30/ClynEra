#!/usr/bin/env python3
"""
Script para probar los endpoints de la API ClynEra
"""

import requests
import json
from datetime import date

# Configuración
BASE_URL = "http://localhost:8000"

def test_health_check():
    """Probar el endpoint de health check"""
    print("🔍 Probando health check...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Health check: {response.status_code} - {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Error en health check: {e}")
        return False

def test_create_paciente():
    """Probar la creación de un paciente"""
    print("\n🔍 Probando creación de paciente...")
    
    paciente_data = {
        "nombre_completo": "Juan Pérez Test",
        "documento": "12345678",
        "fecha_nacimiento": "1990-01-01",
        "genero": "Masculino"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/pacientes/",
            json=paciente_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"📊 Status Code: {response.status_code}")
        print(f"📊 Headers: {dict(response.headers)}")
        
        if response.status_code == 201:
            print(f"✅ Paciente creado exitosamente: {response.json()}")
            return response.json()
        else:
            print(f"❌ Error al crear paciente: {response.status_code}")
            print(f"📄 Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error en la petición: {e}")
        return None

def test_get_pacientes():
    """Probar la obtención de pacientes"""
    print("\n🔍 Probando obtención de pacientes...")
    
    try:
        response = requests.get(f"{BASE_URL}/pacientes/")
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            pacientes = response.json()
            print(f"✅ Pacientes obtenidos: {len(pacientes)} pacientes")
            for paciente in pacientes:
                print(f"  - {paciente['nombre_completo']} ({paciente['documento']})")
            return pacientes
        else:
            print(f"❌ Error al obtener pacientes: {response.status_code}")
            print(f"📄 Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error en la petición: {e}")
        return None

def test_get_paciente_by_id(paciente_id):
    """Probar la obtención de un paciente por ID"""
    print(f"\n🔍 Probando obtención de paciente ID {paciente_id}...")
    
    try:
        response = requests.get(f"{BASE_URL}/pacientes/{paciente_id}")
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            paciente = response.json()
            print(f"✅ Paciente obtenido: {paciente['nombre_completo']}")
            return paciente
        else:
            print(f"❌ Error al obtener paciente: {response.status_code}")
            print(f"📄 Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error en la petición: {e}")
        return None

def main():
    """Función principal de pruebas"""
    print("🚀 Iniciando pruebas de endpoints de ClynEra API")
    print("=" * 50)
    
    # Probar health check
    if not test_health_check():
        print("❌ El servidor no está respondiendo. Asegúrate de que esté ejecutándose.")
        return
    
    # Probar creación de paciente
    paciente_creado = test_create_paciente()
    
    if paciente_creado:
        paciente_id = paciente_creado['id']
        
        # Probar obtención de pacientes
        test_get_pacientes()
        
        # Probar obtención de paciente por ID
        test_get_paciente_by_id(paciente_id)
    
    print("\n" + "=" * 50)
    print("🏁 Pruebas completadas")

if __name__ == "__main__":
    main() 