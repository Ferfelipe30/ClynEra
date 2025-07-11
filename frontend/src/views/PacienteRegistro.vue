<template>
    <div class="form-container">
        <h2>Registro de paciente</h2>
        <form @submit.prevent="registrarPaciente">
            <div class="form-group">
                <label for="nombre">Nombre Completo</label>
                <input id="nombre" v-model="nombre" placeholder="Nombre del paciente" required />
            </div>
            <div class="form-group">
                <label for="documento">Documento</label>
                <input id="documento" v-model="documento" placeholder="Número de documento" required />
            </div>
            <div class="form-group">
                <label for="fecha_nacimiento">Fecha de Nacimiento</label>
                <input id="fecha_nacimiento" type="date" v-model="fecha_nacimiento" required />
            </div>
            <div class="form-group">
                <label for="genero">Género</label>
                <select id="genero" v-model="genero" required>
                    <option value="">Seleccione una opción</option>
                    <option value="Masculino">Masculino</option>
                    <option value="Femenino">Femenino</option>
                </select>
            </div>
            <button type="submit" :disabled="loading">
                {{ loading ? 'Registrando...' : 'Registrar' }}
            </button>
            <div v-if="mensaje" :class="['mensaje', { error: hasError, success: !hasError }]">
                {{ mensaje }}
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const nombre = ref('')
const documento = ref('')
const fecha_nacimiento = ref('')
const genero = ref('')
const mensaje = ref('')
const loading = ref(false)
const hasError = ref(false)

const resetForm = () => {
    nombre.value = ''
    documento.value = ''
    fecha_nacimiento.value = ''
    genero.value = ''
}

async function registrarPaciente() {
    loading.value = true
    mensaje.value = ''
    hasError.value = false

    try {
        await axios.post('http://localhost:8000/pacientes', {
            nombre: nombre.value,
            documento: documento.value,
            fecha_nacimiento: fecha_nacimiento.value,
            genero: genero.value
        })
        mensaje.value = 'Paciente registrado correctamente'
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
            mensaje.value = `Error al registrar paciente: ${errorMessage}`
        } else {
            mensaje.value = 'Error al registrar paciente. Verifique la conexion con el servidor.'
        }
        console.error(e)
    } finally {
        loading.value = false
    }
}
</script>

<style scoped>
.form-container {
  max-width: 500px;
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
  margin-bottom: 1rem;
}
.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}
input,
select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  background-color: var(--color-background);
  color: var(--color-text);
  font-size: 1rem;
}
input:focus,
select:focus {
  outline: none;
  border-color: var(--color-border-hover);
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