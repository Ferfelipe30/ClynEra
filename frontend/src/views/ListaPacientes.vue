<template>
  <div class="patients-container">
    <div class="patients-header">
      <h1 class="patients-title">Lista de Pacientes</h1>
      <div class="header-actions">
        <div class="search-container">
          <input 
            type="text" 
            v-model="searchTerm" 
            placeholder="Buscar por nombre o documento..." 
            class="search-input"
            @input="filterPacientes"
          />
        </div>
        <button @click="cargarPacientes" :disabled="loading" class="refresh-btn">
          {{ loading ? 'Cargando...' : 'Actualizar' }}
        </button>
      </div>
    </div>
    
    <div v-if="mensaje" :class="['mensaje', { error: hasError, success: !hasError }]">
      {{ mensaje }}
    </div>
    
    <div v-if="pacientes.length > 0" class="patients-stats">
      <p>Mostrando {{ filteredPacientes.length }} de {{ pacientes.length }} pacientes</p>
    </div>
    
    <div v-if="pacientes.length === 0 && !loading" class="no-patients">
      <p>No hay pacientes registrados.</p>
    </div>
    
    <div v-else-if="filteredPacientes.length === 0 && pacientes.length > 0 && !loading" class="no-patients">
      <p>No se encontraron pacientes que coincidan con la búsqueda.</p>
    </div>
    
    <div v-else-if="loading" class="loading">
      <p>Cargando pacientes...</p>
    </div>
    
    <div v-else class="patients-grid">
      <div v-for="paciente in filteredPacientes" :key="paciente.id" class="patient-card">
        <div class="patient-info">
          <h3 class="patient-name">{{ paciente.nombre_completo }}</h3>
          <p class="patient-document">Documento: {{ paciente.documento }}</p>
          <p class="patient-birth">Fecha de Nacimiento: {{ formatDate(paciente.fecha_nacimiento) }}</p>
          <p class="patient-gender">Género: {{ paciente.genero }}</p>
        </div>
        <div class="patient-actions">
          <button @click="verDetalles(paciente)" class="view-btn">Ver Detalles</button>
          <button @click="editarPaciente(paciente)" class="edit-btn">Editar</button>
          <button @click="eliminarPaciente(paciente.id)" class="delete-btn">Eliminar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { config } from '../config.js'

const pacientes = ref([])
const filteredPacientes = ref([])
const searchTerm = ref('')
const loading = ref(false)
const mensaje = ref('')
const hasError = ref(false)

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('es-ES')
}

const filterPacientes = () => {
  if (!searchTerm.value.trim()) {
    filteredPacientes.value = pacientes.value
    return
  }
  
  const term = searchTerm.value.toLowerCase().trim()
  filteredPacientes.value = pacientes.value.filter(paciente => 
    paciente.nombre_completo.toLowerCase().includes(term) ||
    paciente.documento.toLowerCase().includes(term)
  )
}

const cargarPacientes = async () => {
  loading.value = true
  mensaje.value = ''
  hasError.value = false
  
  try {
    console.log('Cargando pacientes desde:', `${config.API_BASE_URL}/pacientes/`)
    const response = await axios.get(`${config.API_BASE_URL}/pacientes/`)
    console.log('Pacientes cargados:', response.data)
    pacientes.value = response.data
    filteredPacientes.value = response.data
  } catch (e) {
    console.error('Error al cargar pacientes:', e)
    hasError.value = true
    
    if (e.response) {
      mensaje.value = `Error al cargar pacientes: ${e.response.data.detail || 'Error del servidor'}`
    } else if (e.request) {
      mensaje.value = 'No se pudo conectar con el servidor. Verifique que el backend esté ejecutándose.'
    } else {
      mensaje.value = 'Error al configurar la petición.'
    }
  } finally {
    loading.value = false
  }
}

const verDetalles = (paciente) => {
  alert(`Detalles del paciente:\n\nNombre: ${paciente.nombre_completo}\nDocumento: ${paciente.documento}\nFecha de Nacimiento: ${formatDate(paciente.fecha_nacimiento)}\nGénero: ${paciente.genero}`)
}

const editarPaciente = (paciente) => {
  // TODO: Implementar edición de paciente
  console.log('Editar paciente:', paciente)
  alert(`Función de edición para paciente: ${paciente.nombre_completo}`)
}

const eliminarPaciente = async (pacienteId) => {
  if (!confirm('¿Está seguro de que desea eliminar este paciente?')) {
    return
  }
  
  try {
    await axios.delete(`${config.API_BASE_URL}/pacientes/${pacienteId}`)
    mensaje.value = 'Paciente eliminado correctamente.'
    hasError.value = false
    await cargarPacientes() // Recargar la lista
    filterPacientes() // Reaplicar filtros
  } catch (e) {
    console.error('Error al eliminar paciente:', e)
    hasError.value = true
    
    if (e.response) {
      mensaje.value = `Error al eliminar paciente: ${e.response.data.detail || 'Error del servidor'}`
    } else {
      mensaje.value = 'Error al eliminar paciente.'
    }
  }
}

onMounted(() => {
  cargarPacientes()
})
</script>

<style scoped>
.patients-container {
  min-height: 100vh;
  background: #f7f9fb;
  padding: 40px 20px;
}

.patients-header {
  max-width: 1200px;
  margin: 0 auto 32px auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-actions {
  display: flex;
  gap: 16px;
  align-items: center;
}

.search-container {
  position: relative;
}

.search-input {
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 10px 16px;
  font-size: 1rem;
  width: 300px;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.search-input:focus {
  border-color: #2196f3;
  box-shadow: 0 0 0 2px rgba(33, 150, 243, 0.1);
}

.patients-title {
  font-size: 2rem;
  font-weight: 700;
  color: #222;
  margin: 0;
}

.refresh-btn {
  background: #2196f3;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 10px 20px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.refresh-btn:hover:not(:disabled) {
  background: #1769aa;
}

.refresh-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.mensaje {
  max-width: 1200px;
  margin: 0 auto 20px auto;
  padding: 12px;
  border-radius: 8px;
  text-align: center;
}

.success {
  background-color: #e6f9ec;
  color: #207544;
  border: 1px solid #c3e6cb;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.patients-stats {
  max-width: 1200px;
  margin: 0 auto 20px auto;
  text-align: right;
  color: #666;
  font-size: 0.9rem;
}

.no-patients, .loading {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
  padding: 40px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.04);
}

.patients-grid {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
}

.patient-card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.04);
  padding: 24px;
  transition: transform 0.2s, box-shadow 0.2s;
}

.patient-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 24px rgba(0,0,0,0.08);
}

.patient-info {
  margin-bottom: 20px;
}

.patient-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: #222;
  margin: 0 0 12px 0;
}

.patient-document,
.patient-birth,
.patient-gender {
  margin: 6px 0;
  color: #666;
  font-size: 0.9rem;
}

.patient-actions {
  display: flex;
  gap: 12px;
}

.view-btn,
.edit-btn,
.delete-btn {
  flex: 1;
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s;
}

.view-btn {
  background: #17a2b8;
  color: #fff;
}

.view-btn:hover {
  background: #138496;
}

.edit-btn {
  background: #ffc107;
  color: #000;
}

.edit-btn:hover {
  background: #e0a800;
}

.delete-btn {
  background: #dc3545;
  color: #fff;
}

.delete-btn:hover {
  background: #c82333;
}
</style> 