<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const pacienteId = ref('')
const examenIds = ref([])

const pacientes = ref([])
const examenes = ref([])

const loading = ref(false)
const mensaje = ref('')
const hasError = ref(false)

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
  <div class="form-container">
    <h2>Registro de Orden</h2>
    <form @submit.prevent="registrarOrden">
      <div class="form-group">
        <label for="paciente">Paciente</label>
        <select id="paciente" v-model="pacienteId" required>
          <option disabled value="">Seleccione un paciente</option>
          <option v-for="paciente in pacientes" :key="paciente.id" :value="paciente.id">
            {{ paciente.nombre }} ({{ paciente.documento }})
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Exámenes</label>
        <div class="examenes-list">
          <div v-for="examen in examenes" :key="examen.id" class="examen-item">
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

      <button type="submit" :disabled="loading">
        {{ loading ? 'Registrando...' : 'Registrar Orden' }}
      </button>

      <div v-if="mensaje" :class="['mensaje', { error: hasError, success: !hasError }]">
        {{ mensaje }}
      </div>
    </form>
  </div>
</template>

<style scoped>
.form-container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: var(--color-background-soft);
}
h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: var(--color-heading);
}
.form-group {
  margin-bottom: 1.5rem;
}
.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}
select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  background-color: var(--color-background);
  color: var(--color-text);
  font-size: 1rem;
}
select:focus {
  outline: none;
  border-color: var(--color-border-hover);
}
.examenes-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
  padding: 1rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  max-height: 250px;
  overflow-y: auto;
}
.examen-item {
  display: flex;
  align-items: center;
}
.examen-item input[type='checkbox'] {
  margin-right: 0.5rem;
  width: auto;
}
.examen-item label {
  margin-bottom: 0;
  font-weight: normal;
}
button {
  width: 100%;
  padding: 0.75rem;
  border: none;
  border-radius: 4px;
  background-color: hsla(160, 100%, 37%, 1);
  color: white;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}
button:hover {
  background-color: hsla(160, 100%, 30%, 1);
}
button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
.mensaje {
  margin-top: 1rem;
  padding: 0.75rem;
  border-radius: 4px;
  text-align: center;
}
.success {
  background-color: hsla(160, 100%, 37%, 0.2);
  color: var(--color-heading);
}
.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}
</style>