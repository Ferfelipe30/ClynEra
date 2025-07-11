<template>
    <form @submit.prevent="registrarPaciente">
        <input v-model="nombre" placeholder="Nombre" required/>
        <input v-model="documento" placeholder="Documento" required/>
        <input v-model="fecha_nacimiento" type="date" required/>
        <select v-model="genero" required>
            <option value="M">Masculino</option>
            <option value="F">Femenino</option>
        </select>
        <button type="submit">Registrar</button>
        <div v-if="mensaje">{{ mensaje }}</div>
    </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const nombre = ref('')
const documento = ref('')
const fecha_nacimiento = ref('')
const genero = ref('')
const mensaje = ref('')

async function registrarPaciente() {
    try {
        await axios.post('http://localhost:8000/pacientes/', {
            nombre: nombre.value,
            documento: documento.value,
            fecha_nacimiento: fecha_nacimiento.value,
            genero: genero.value
        })
        mensaje.value = 'Paciente registrado correctamente'
    } catch (e) {
        mensaje.value = 'Error al registrar paciente'
    }
}
</script>