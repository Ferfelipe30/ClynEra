import { ref, reactive } from 'vue'
import { healthService } from '../services/api.js'

// Estado global de la API
export const apiState = reactive({
  isConnected: false,
  isLoading: false,
  error: null,
  lastCheck: null,
})

// Función para verificar la conexión con el backend
export const checkApiConnection = async () => {
  apiState.isLoading = true
  apiState.error = null
  
  try {
    const response = await healthService.checkHealth()
    apiState.isConnected = true
    apiState.lastCheck = new Date()
    console.log('✅ API conectada:', response.data)
    return true
  } catch (error) {
    apiState.isConnected = false
    apiState.error = error.message || 'Error de conexión con el backend'
    console.error('❌ Error de conexión con la API:', error)
    return false
  } finally {
    apiState.isLoading = false
  }
}

// Función para manejar errores de API de forma consistente
export const handleApiError = (error, customMessage = null) => {
  const message = customMessage || error.response?.data?.detail || error.message || 'Error desconocido'
  console.error('API Error:', message)
  
  // Aquí podrías agregar notificaciones toast o alertas
  alert(`Error: ${message}`)
  
  return {
    success: false,
    error: message,
    data: null
  }
}

// Función para manejar respuestas exitosas
export const handleApiSuccess = (data, message = null) => {
  if (message) {
    console.log('✅', message)
    // Aquí podrías agregar notificaciones toast
  }
  
  return {
    success: true,
    error: null,
    data
  }
}

// Composable principal para usar en componentes
export const useApi = () => {
  const loading = ref(false)
  const error = ref(null)
  
  const executeApiCall = async (apiFunction, successMessage = null) => {
    loading.value = true
    error.value = null
    
    try {
      const response = await apiFunction()
      const result = handleApiSuccess(response.data, successMessage)
      return result
    } catch (err) {
      const result = handleApiError(err)
      error.value = result.error
      return result
    } finally {
      loading.value = false
    }
  }
  
  return {
    loading,
    error,
    executeApiCall,
    apiState,
    checkApiConnection
  }
} 