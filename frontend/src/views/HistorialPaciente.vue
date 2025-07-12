<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { config } from '../config.js'
import axios from 'axios'

const route = useRoute()
const documento = route.params.documento

const paciente = ref(null)
const ordenes = ref([])
const searchDocumento = ref('')
const loading = ref(false)
const search = ref('')
const testType = ref('')
const selectedDate = ref(null)
const calendarMonth = ref(new Date().getMonth())
const calendarYear = ref(new Date().getFullYear())
const mensaje = ref('')
const hasError = ref(false)

const testTypes = ref([
  { value: '', label: 'All Types' },
  { value: 'CBC', label: 'Complete Blood Count (CBC)' },
  { value: 'Lipid', label: 'Lipid Panel' },
  { value: 'Thyroid', label: 'Thyroid Function Test' },
  { value: 'Urinalysis', label: 'Urinalysis' },
  { value: 'CMP', label: 'Comprehensive Metabolic Panel (CMP)' },
])

const ordenesFiltradas = computed(() => {
  if (!searchDocumento.value.trim()) return ordenes.value
  return ordenes.value.filter(o => 
    o.paciente?.documento?.includes(searchDocumento.value.trim())
  )
})

function setCalendar(month, year) {
  calendarMonth.value = month
  calendarYear.value = year
}

function selectDate(day) {
  selectedDate.value = `${calendarYear.value}-${String(calendarMonth.value+1).padStart(2,'0')}-${String(day).padStart(2,'0')}`
}

function clearFilters() {
  search.value = ''
  testType.value = ''
  selectedDate.value = null
}

onMounted(async () => {
  loading.value = true
  try {
    const res = await axios.get(`${config.API_BASE_URL}/ordenes`)
    ordenes.value = res.data       
  } catch (e) {
    mensaje.value = 'No se pudo cargar el historial.'
    hasError.value = true
  } finally {
    loading.value = false
  }
})

function prevMonth() {
  if (calendarMonth.value === 0) {
    calendarMonth.value = 11
    calendarYear.value--
  } else {
    calendarMonth.value--
  }
}
function nextMonth() {
  if (calendarMonth.value === 11) {
    calendarMonth.value = 0
    calendarYear.value++
  } else {
    calendarMonth.value++
  }
}
function daysInMonth(month, year) {
  return new Date(year, month + 1, 0).getDate()
}
</script>

<template>
  <div class="lab-history-layout">
    <h1 class="lab-history-title">Patient Lab History</h1>
    <div class="lab-history-subtitle">
      View and manage lab orders and results for patient: <b>{{ paciente?.nombre || documento }}</b>
    </div>
    <div class="lab-history-search">
      <input v-model="searchDocumento" class="search-input" placeholder="Filtrar por documento de paciente" />
    </div>
    <div class="lab-history-filters">
      <select v-model="testType" class="filter-select">
        <option v-for="t in testTypes" :key="t.value" :value="t.value">{{ t.label }}</option>
      </select>
      <div class="calendar-container">
        <div class="calendar-header">
          <button @click="prevMonth">&lt;</button>
          <span>{{ new Date(calendarYear, calendarMonth).toLocaleString('default', { month: 'long', year: 'numeric' }) }}</span>
          <button @click="nextMonth">&gt;</button>
        </div>
        <div class="calendar-grid">
          <div class="calendar-day" v-for="d in ['S','M','T','W','T','F','S']" :key="d">{{ d }}</div>
          <div v-for="n in new Date(calendarYear, calendarMonth, 1).getDay()" :key="'empty-'+n" class="calendar-empty"></div>
          <button v-for="day in daysInMonth(calendarMonth, calendarYear)" :key="day" :class="['calendar-date', {selected: selectedDate && selectedDate.endsWith('-'+String(day).padStart(2,'0'))}]" @click="selectDate(day)">{{ day }}</button>
        </div>
      </div>
      <button class="apply-btn" @click="clearFilters">Apply Filters</button>
    </div>
    <div class="lab-orders-table-container">
      <table class="lab-orders-table">
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Paciente</th>
            <th>Documento</th>
            <th>Fecha</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="orden in ordenesFiltradas" :key="orden.id">
            <td>{{ orden.id }}</td>
            <td>{{ orden.paciente?.nombre_completo }}</td>
            <td>{{ orden.paciente?.documento }}</td>
            <td>{{ new Date(orden.fecha_creacion).toLocaleDateString() }}</td>
            <td>{{ orden.estado }}</td>
          </tr>
        </tbody>
      </table>
      <div v-if="mensaje" :class="{ error: hasError }">{{ mensaje }}</div>
    </div>
  </div>
</template>

<style scoped>
.lab-history-layout {
  max-width: 1100px;
  margin: 40px auto;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.04);
  padding: 40px 32px 32px 32px;
}
.lab-history-title {
  font-size: 2rem;
  font-weight: 700;
  color: #222;
  margin-bottom: 8px;
}
.lab-history-subtitle {
  color: #666;
  font-size: 1.08rem;
  margin-bottom: 24px;
}
.lab-history-search {
  margin-bottom: 18px;
}
.search-input {
  width: 100%;
  padding: 14px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  font-size: 1rem;
  background: #f7f9fb;
}
.lab-history-filters {
  display: flex;
  align-items: flex-end;
  gap: 32px;
  margin-bottom: 32px;
}
.filter-select {
  padding: 12px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  font-size: 1rem;
  background: #f7f9fb;
}
.calendar-container {
  background: #f7f9fb;
  border-radius: 12px;
  padding: 18px 18px 12px 18px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
  min-width: 260px;
}
.calendar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
  font-weight: 600;
  color: #222;
}
.calendar-header button {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: #2196f3;
  padding: 2px 8px;
}
.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
}
.calendar-day {
  text-align: center;
  color: #888;
  font-size: 0.97rem;
  font-weight: 600;
  margin-bottom: 2px;
}
.calendar-empty {
  height: 28px;
}
.calendar-date {
  background: none;
  border: none;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  text-align: center;
  font-size: 1rem;
  color: #222;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
}
.calendar-date.selected, .calendar-date:hover {
  background: #2196f3;
  color: #fff;
}
.apply-btn {
  background: #2196f3;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  margin-left: 18px;
  transition: background 0.2s;
}
.apply-btn:hover {
  background: #1769aa;
}
.lab-orders-table-container {
  margin-top: 32px;
}
.lab-orders-table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}
.lab-orders-table th, .lab-orders-table td {
  padding: 14px 12px;
  text-align: left;
  font-size: 1rem;
}
.lab-orders-table th {
  background: #f7f9fb;
  color: #222;
  font-weight: 700;
}
.lab-orders-table tr {
  border-bottom: 1px solid #ececec;
}
.lab-orders-table tr:last-child {
  border-bottom: none;
}
.status-completed {
  background: #e6f9ec;
  color: #207544;
  border-radius: 8px;
  padding: 6px 16px;
  font-weight: 600;
  font-size: 0.98rem;
}
.order-date-link, .view-results-link {
  color: #2196f3;
  text-decoration: underline;
  cursor: pointer;
  font-weight: 500;
}
.no-orders {
  text-align: center;
  color: #888;
  margin-top: 18px;
  font-size: 1.1rem;
}
</style>