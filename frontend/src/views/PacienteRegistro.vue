<template>
  <div class="register-container">
    <div class="register-card">
      <h1 class="register-title">New Patient Registration</h1>
      <form class="register-form" @submit.prevent="registrarPaciente">
        <div class="form-group">
          <label>Nombre Completo</label>
          <input type="text" v-model="paciente.nombre_completo" placeholder="Nombre completo del paciente" required />
        </div>
        <div class="form-group">
          <label>Documento</label>
          <input type="text" v-model="paciente.documento" placeholder="Número de documento" required />
        </div>
        <div class="form-group">
          <label>Fecha de Nacimiento</label>
          <input type="date" v-model="paciente.fecha_nacimiento" required />
        </div>
        <div class="form-group">
          <label>Género</label>
          <select v-model="paciente.genero" required>
            <option disabled value="">Seleccione una opción</option>
            <option>Masculino</option>
            <option>Femenino</option>
            <option>Otro</option>
          </select>
        </div>
        <div class="form-actions">
          <button type="submit" :disabled="loading" class="submit-btn">
            {{ loading ? 'Registrando...' : 'Registrar Paciente' }}
          </button>
          <button type="button" @click="resetForm" class="reset-btn">
            Limpiar Formulario
          </button>
        </div>
        <div v-if="mensaje" :class="['mensaje', { error: hasError, success: !hasError }]">
          {{ mensaje }}
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { pacientesService } from '../services/api.js'
import { useApi } from '../composables/useApi.js'

const paciente = ref({
  nombre_completo: '',
  documento: '',
  fecha_nacimiento: '',
  genero: ''
})

const mensaje = ref('')
const hasError = ref(false)
const { loading, executeApiCall } = useApi()

const resetForm = () => {
  paciente.value = { nombre_completo: '', documento: '', fecha_nacimiento: '', genero: '' }
}

async function registrarPaciente() {
  mensaje.value = ''
  hasError.value = false
  
  // Validar datos antes de enviar
  if (!paciente.value.nombre_completo || !paciente.value.documento || !paciente.value.fecha_nacimiento || !paciente.value.genero) {
    mensaje.value = 'Por favor complete todos los campos requeridos.'
    hasError.value = true
    return
  }
  
  const result = await executeApiCall(
    () => pacientesService.createPaciente(paciente.value),
    'Paciente registrado correctamente'
  )
  
  if (result.success) {
    mensaje.value = 'Paciente registrado correctamente.'
    hasError.value = false
    resetForm()
  } else {
    mensaje.value = `Error al registrar paciente: ${result.error}`
    hasError.value = true
  }
}
</script>

<style scoped>
.register-container {
  min-height: 100vh;
  background: #f7f9fb;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding-top: 40px;
}

.register-card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.04);
  padding: 40px 32px 32px 32px;
  width: 100%;
  max-width: 480px;
}

.register-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 32px;
  color: #222;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-group label {
  font-size: 1rem;
  color: #222;
  font-weight: 500;
}

.form-group input[type="text"],
.form-group input[type="date"],
.form-group select {
  background: #e9f1f7;
  border: none;
  border-radius: 8px;
  padding: 12px 14px;
  font-size: 1rem;
  color: #222;
  outline: none;
  transition: box-shadow 0.2s;
}

.form-group input:focus,
.form-group select:focus {
  box-shadow: 0 0 0 2px #b6e0fe;
}

.form-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 18px;
}

.submit-btn {
  background: #2196f3;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.submit-btn:hover:not(:disabled) {
  background: #1769aa;
}

.submit-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.reset-btn {
  background: #6c757d;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.reset-btn:hover {
  background: #5a6268;
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