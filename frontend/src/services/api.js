import axios from 'axios'
import { config } from '../config.js'

// Crear instancia de axios con configuración base
const api = axios.create({
  baseURL: config.API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor para manejar errores globalmente
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response?.data || error.message)
    return Promise.reject(error)
  }
)

// Servicios para pacientes
export const pacientesService = {
  // Obtener todos los pacientes
  getPacientes: (skip = 0, limit = 100) => 
    api.get(`/pacientes/?skip=${skip}&limit=${limit}`),
  
  // Obtener paciente por ID
  getPacienteById: (id) => 
    api.get(`/pacientes/${id}`),
  
  // Crear nuevo paciente
  createPaciente: (pacienteData) => 
    api.post('/pacientes/', pacienteData),
  
  // Actualizar paciente
  updatePaciente: (id, pacienteData) => 
    api.put(`/pacientes/${id}`, pacienteData),
  
  // Eliminar paciente
  deletePaciente: (id) => 
    api.delete(`/pacientes/${id}`),
}

// Servicios para exámenes
export const examenesService = {
  // Obtener todos los exámenes
  getExamenes: (skip = 0, limit = 100) => 
    api.get(`/examenes?skip=${skip}&limit=${limit}`),
  
  // Obtener examen por ID
  getExamenById: (id) => 
    api.get(`/examenes/${id}`),
  
  // Crear nuevo examen
  createExamen: (examenData) => 
    api.post('/examenes', examenData),
  
  // Actualizar examen
  updateExamen: (id, examenData) => 
    api.put(`/examenes/${id}`, examenData),
  
  // Eliminar examen
  deleteExamen: (id) => 
    api.delete(`/examenes/${id}`),
}

// Servicios para órdenes
export const ordenesService = {
  // Obtener todas las órdenes
  getOrdenes: (skip = 0, limit = 100) => 
    api.get(`/ordenes?skip=${skip}&limit=${limit}`),
  
  // Obtener orden por ID
  getOrdenById: (id) => 
    api.get(`/ordenes/${id}`),
  
  // Crear nueva orden
  createOrden: (ordenData) => 
    api.post('/ordenes', ordenData),
  
  // Actualizar orden
  updateOrden: (id, ordenData) => 
    api.put(`/ordenes/${id}`, ordenData),
  
  // Eliminar orden
  deleteOrden: (id) => 
    api.delete(`/ordenes/${id}`),
}

// Servicio general para verificar conexión
export const healthService = {
  // Verificar si la API está funcionando
  checkHealth: () => 
    api.get('/'),
}

export default api 