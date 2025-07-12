// Configuration for the application
export const config = {
  API_BASE_URL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  APP_TITLE: import.meta.env.VITE_APP_TITLE || 'ClynEra',
  APP_VERSION: import.meta.env.VITE_APP_VERSION || '1.0.0',
  // Timeout para peticiones API (en milisegundos)
  API_TIMEOUT: 10000,
  // Configuración de reintentos
  API_RETRY_ATTEMPTS: 3,
  API_RETRY_DELAY: 1000,
} 