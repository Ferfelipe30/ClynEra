<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { config } from '../config.js'

const route = useRoute()
const ordenId = route.params.id
const orden = ref(null)
const mensaje = ref('')
const hasError = ref(false)

onMounted(async () => {
  try {
    const res = await axios.get(`${config.API_BASE_URL}/ordenes/${ordenId}`)
    orden.value = res.data
  } catch (e) {
    mensaje.value = 'No se pudo cargar el detalle de la orden.'
    hasError.value = true
  }
})
</script>

<template>
  <div class="detalle-orden">
    <h1>Detalle de la Orden</h1>
    <div v-if="orden">
      <p><strong>ID:</strong> {{ orden.id }}</p>
      <p><strong>Número de Orden:</strong> {{ orden.numero_orden }}</p>
      <p><strong>Paciente:</strong> {{ orden.paciente?.nombre_completo }}</p>
      <p><strong>Documento:</strong> {{ orden.paciente?.documento }}</p>
      <p><strong>Fecha de Creación:</strong> {{ new Date(orden.fecha_creacion).toLocaleString() }}</p>
      <p><strong>Estado:</strong> {{ orden.estado }}</p>
      <div>
        <strong>Exámenes:</strong>
        <ul>
          <li v-for="ex in orden.examenes" :key="ex.id">
            {{ ex.examen?.nombre }}
          </li>
        </ul>
      </div>
    </div>
    <div v-else-if="mensaje" :class="{ error: hasError }">{{ mensaje }}</div>
    <div v-else>Cargando...</div>
  </div>
</template>