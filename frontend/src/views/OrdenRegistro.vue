<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const pacienteId = ref('')
const pacienteSearch = ref('')
const examenIds = ref([])
const clinicalNotes = ref('')
const selectedPriority = ref('Routine')

const pacientes = ref([])
const examenes = ref([])
const loading = ref(false)
const mensaje = ref('')
const hasError = ref(false)
const activeTab = ref('Hematología')

const examenesPorCategoria = computed(() => {
  const categorias = { Hematología: [], Química: [], Uroanálisis: [] }
  for (const ex of examenes.value) {
    if (categorias[ex.area]) categorias[ex.area].push(ex)
  }
  return categorias
})

const pacienteFiltrado = computed(() => {
  if (!pacienteSearch.value) return pacientes.value
  return pacientes.value.filter(p =>
    p.nombre_completo.toLowerCase().includes(pacienteSearch.value.toLowerCase()) ||
    (p.documento && p.documento.includes(pacienteSearch.value))
  )
})

const pacienteSeleccionado = computed(() => {
  return pacientes.value.find(p => p.id === pacienteId.value)
})

onMounted(async () => {
  try {
    const [pacientesRes, examenesRes] = await Promise.all([
      axios.get('http://localhost:8000/pacientes'),
      axios.get('http://localhost:8000/examenes'),
    ])
    pacientes.value = pacientesRes.data
    examenes.value = examenesRes.data
  } catch (error) {
    console.error('Error al cargar datos iniciales: ', error)
    mensaje.value = 'No se pudieron cargar los pacientes o examenes.'
    hasError.value = true
  }
})

const resetForm = () => {
  pacienteId.value = ''
  examenIds.value = []
  clinicalNotes.value = ''
  selectedPriority.value = 'Routine'
}

async function registrarOrden() {
  if (!pacienteId.value || examenIds.value.length === 0) {
    mensaje.value = 'Por favor, seleccione un paciente y al menos un examen.'
    hasError.value = true
    return
  }
  loading.value = true
  mensaje.value = ''
  hasError.value = false
  try {
    await axios.post('http://localhost:8000/ordenes', {
      paciente_id: pacienteId.value,
      examen_ids: examenIds.value,
      notas: clinicalNotes.value,
      prioridad: selectedPriority.value,
    })
    mensaje.value = 'Orden registrada exitosamente.'
    resetForm()
  } catch (e) {
    hasError.value = true
    if (e.response && e.response.data) {
      const errorData = e.response.data
      let errorMessage = 'Ocurrio un error.'
      if (typeof errorData === 'string') {
        errorMessage = errorData
      } else if (errorData.detail) {
        errorMessage = errorData.detail
      } else if (typeof errorData === 'object') {
        errorMessage = Object.entries(errorData)
          .map(([key, value]) => `${key}: ${value}`)
          .join(', ')
      }
      mensaje.value = `Error al registrar la orden: ${errorMessage}`
    } else {
      mensaje.value = 'Error al registrar la orden. Verifique la conexión con el servidor.'
    }
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="orden-layout">
    <!-- Columna principal -->
    <div class="orden-main">
      <h1 class="orden-title">Create New Order</h1>
      <div class="orden-section">
        <label class="orden-label">Patient Information</label>
        <div class="autocomplete-container">
          <input
            v-model="pacienteSearch"
            class="autocomplete-input"
            placeholder="Search by Name or ID"
            @input="pacienteId = ''"
          />
          <ul v-if="pacienteSearch && pacienteFiltrado.length" class="autocomplete-list">
            <li v-for="p in pacienteFiltrado" :key="p.id" @click="pacienteId = p.id; pacienteSearch = p.nombre_completo + (p.documento ? ' ('+p.documento+')' : '')">
              {{ p.nombre_completo }} <span v-if="p.documento">({{ p.documento }})</span>
            </li>
          </ul>
        </div>
      </div>
      <div class="orden-section">
        <label class="orden-label">Test Selection</label>
        <div class="tabs">
          <button v-for="tab in Object.keys(examenesPorCategoria)" :key="tab" :class="['tab', {active: activeTab === tab}]" @click="activeTab = tab">{{ tab }}</button>
        </div>
        <div class="tab-content">
          <div v-for="examen in examenesPorCategoria[activeTab]" :key="examen.id" class="examen-item">
            <input
              type="checkbox"
              :id="'examen-' + examen.id"
              :value="examen.id"
              v-model="examenIds"
            />
            <label :for="'examen-' + examen.id">{{ examen.nombre }}</label>
          </div>
        </div>
      </div>
      <div class="orden-section">
        <label class="orden-label">Clinical Notes</label>
        <textarea v-model="clinicalNotes" class="orden-notes" placeholder="Add any clinical notes or special instructions" rows="3"></textarea>
      </div>
    </div>
    <!-- Panel lateral de resumen -->
    <div class="orden-summary">
      <h2 class="summary-title">Order Summary</h2>
      <div class="summary-block">
        <div class="summary-label">Patient</div>
        <div v-if="pacienteSeleccionado">
          <div class="summary-patient-name">{{ pacienteSeleccionado.nombre_completo }}</div>
          <div class="summary-patient-id">ID: {{ pacienteSeleccionado.documento }}</div>
        </div>
        <div v-else class="summary-empty">No patient selected</div>
      </div>
      <div class="summary-block">
        <div class="summary-label">Priority</div>
        <div class="summary-priority">{{ selectedPriority }}</div>
      </div>
      <div class="summary-block">
        <div class="summary-label">Selected Tests</div>
        <ul class="summary-tests">
          <li v-for="id in examenIds" :key="id">
            {{ (examenes.find(e => e.id === id) || {}).nombre }}
          </li>
        </ul>
        <div v-if="!examenIds.length" class="summary-empty">None</div>
      </div>
      <div class="summary-block">
        <div class="summary-label">Clinical Notes</div>
        <div class="summary-notes">{{ clinicalNotes || 'None' }}</div>
      </div>
      <button class="orden-submit" :disabled="loading" @click="registrarOrden">
        {{ loading ? 'Submitting...' : 'Submit Order' }}
      </button>
      <div v-if="mensaje" :class="['mensaje', { error: hasError, success: !hasError }]">
        {{ mensaje }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.orden-layout {
  display: flex;
  gap: 40px;
  max-width: 1200px;
  margin: 40px auto;
  align-items: flex-start;
}
.orden-main {
  flex: 2;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
  padding: 32px 32px 24px 32px;
}
.orden-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 24px;
  color: #222;
}
.orden-section {
  margin-bottom: 32px;
}
.orden-label {
  font-weight: 600;
  color: #222;
  margin-bottom: 10px;
  display: block;
}
.autocomplete-container {
  position: relative;
  width: 100%;
}
.autocomplete-input {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  font-size: 1rem;
  background: #f7f9fb;
}
.autocomplete-list {
  position: absolute;
  left: 0;
  right: 0;
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 0 0 8px 8px;
  z-index: 10;
  max-height: 180px;
  overflow-y: auto;
  margin-top: 2px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.autocomplete-list li {
  padding: 10px 16px;
  cursor: pointer;
  transition: background 0.2s;
}
.autocomplete-list li:hover {
  background: #eaf3fa;
}
.tabs {
  display: flex;
  gap: 18px;
  margin-bottom: 12px;
}
.tab {
  background: none;
  border: none;
  font-weight: 600;
  font-size: 1rem;
  color: #888;
  padding: 8px 18px;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  transition: color 0.2s, border 0.2s;
}
.tab.active {
  color: #2196f3;
  border-bottom: 2px solid #2196f3;
}
.tab-content {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.examen-item {
  display: flex;
  align-items: center;
  gap: 8px;
}
.orden-notes {
  width: 100%;
  min-height: 60px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  padding: 12px;
  font-size: 1rem;
  background: #f7f9fb;
}
.orden-summary {
  flex: 1;
  background: #f7f9fb;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
  padding: 32px 24px 24px 24px;
  min-width: 320px;
  max-width: 350px;
  position: sticky;
  top: 40px;
  align-self: flex-start;
  display: flex;
  flex-direction: column;
  gap: 18px;
}
.summary-title {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 18px;
  color: #222;
}
.summary-block {
  margin-bottom: 16px;
}
.summary-label {
  font-size: 0.98rem;
  color: #888;
  font-weight: 600;
  margin-bottom: 4px;
}
.summary-patient-name {
  font-weight: 600;
  color: #222;
}
.summary-patient-id {
  color: #888;
  font-size: 0.97rem;
}
.summary-priority {
  color: #2196f3;
  font-weight: 600;
}
.summary-tests {
  list-style: none;
  padding: 0;
  margin: 0;
  color: #222;
  font-size: 0.97rem;
}
.summary-tests li {
  margin-bottom: 2px;
}
.summary-empty {
  color: #bbb;
  font-size: 0.97rem;
}
.summary-notes {
  color: #222;
  font-size: 0.97rem;
  white-space: pre-line;
}
.orden-submit {
  margin-top: 18px;
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: none;
  background: #2196f3;
  color: #fff;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s;
}
.orden-submit:disabled {
  background: #ccc;
  cursor: not-allowed;
}
.mensaje {
  margin-top: 1rem;
  padding: 0.75rem;
  border-radius: 4px;
  text-align: center;
}
.success {
  background-color: #e6f9ec;
  color: #207544;
}
.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}
</style>