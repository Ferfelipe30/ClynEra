#!/usr/bin/env python3
"""
Script para probar los endpoints de la API.
"""

import requests
import json
from datetime import date

# Configuración
BASE_URL = "http://localhost:8000"

def test_root_endpoint():
    """Prueba el endpoint raíz."""
    print("🔍 Probando endpoint raíz...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Endpoint raíz funcionando")
            print(f"   Respuesta: {response.json()}")
        else:
            print(f"❌ Error en endpoint raíz: {response.status_code}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

def test_create_patient():
    """Prueba crear un paciente."""
    print("\n🔍 Probando creación de paciente...")
    
    patient_data = {
        "nombre_completo": "Juan Pérez",
        "documento": "12345678",
        "fecha_nacimiento": "1990-05-15",
        "genero": "Masculino"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/paciente/", json=patient_data)
        if response.status_code == 201:
            print("✅ Paciente creado exitosamente")
            print(f"   Respuesta: {response.json()}")
            return response.json()["id"]
        else:
            print(f"❌ Error al crear paciente: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return None

def test_get_patients():
    """Prueba obtener la lista de pacientes."""
    print("\n🔍 Probando obtención de pacientes...")
    try:
        response = requests.get(f"{BASE_URL}/paciente/")
        if response.status_code == 200:
            patients = response.json()
            print(f"✅ Lista de pacientes obtenida: {len(patients)} pacientes")
            for patient in patients:
                print(f"   - {patient['nombre_completo']} (ID: {patient['id']})")
        else:
            print(f"❌ Error al obtener pacientes: {response.status_code}")
            print(f"   Respuesta: {response.text}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

def test_get_patient_by_id(patient_id):
    """Prueba obtener un paciente por ID."""
    if not patient_id:
        return
    
    print(f"\n🔍 Probando obtención de paciente por ID ({patient_id})...")
    try:
        response = requests.get(f"{BASE_URL}/paciente/{patient_id}")
        if response.status_code == 200:
            patient = response.json()
            print("✅ Paciente obtenido por ID")
            print(f"   Nombre: {patient['nombre_completo']}")
            print(f"   Documento: {patient['documento']}")
        else:
            print(f"❌ Error al obtener paciente por ID: {response.status_code}")
            print(f"   Respuesta: {response.text}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

def test_update_patient(patient_id):
    """Prueba actualizar un paciente."""
    if not patient_id:
        return
    
    print(f"\n🔍 Probando actualización de paciente (ID: {patient_id})...")
    
    update_data = {
        "nombre_completo": "Juan Carlos Pérez",
        "documento": "12345678",
        "fecha_nacimiento": "1990-05-15",
        "genero": "Masculino"
    }
    
    try:
        response = requests.put(f"{BASE_URL}/paciente/{patient_id}", json=update_data)
        if response.status_code == 200:
            patient = response.json()
            print("✅ Paciente actualizado exitosamente")
            print(f"   Nuevo nombre: {patient['nombre_completo']}")
        else:
            print(f"❌ Error al actualizar paciente: {response.status_code}")
            print(f"   Respuesta: {response.text}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

def test_delete_patient(patient_id):
    """Prueba eliminar un paciente."""
    if not patient_id:
        return
    
    print(f"\n🔍 Probando eliminación de paciente (ID: {patient_id})...")
    try:
        response = requests.delete(f"{BASE_URL}/paciente/{patient_id}")
        if response.status_code == 200:
            print("✅ Paciente eliminado exitosamente")
            print(f"   Respuesta: {response.json()}")
        else:
            print(f"❌ Error al eliminar paciente: {response.status_code}")
            print(f"   Respuesta: {response.text}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

def main():
    """Función principal."""
    print("🧪 Iniciando pruebas de la API...")
    print(f"📡 URL base: {BASE_URL}")
    
    # Probar endpoint raíz
    test_root_endpoint()
    
    # Probar creación de paciente
    patient_id = test_create_patient()
    
    # Probar obtención de pacientes
    test_get_patients()
    
    # Probar obtención por ID
    test_get_patient_by_id(patient_id)
    
    # Probar actualización
    test_update_patient(patient_id)
    
    # Probar eliminación
    test_delete_patient(patient_id)
    
    print("\n🎉 Pruebas completadas!")

if __name__ == "__main__":
    main() 