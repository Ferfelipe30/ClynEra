# Conexión Frontend-Backend - ClynEra

## Descripción General

Este documento describe cómo está configurada la conexión entre el frontend (Vue.js) y el backend (FastAPI) en la aplicación ClynEra.

## Arquitectura

### Backend (FastAPI)
- **Puerto**: 8000
- **URL Base**: `http://localhost:8000`
- **Framework**: FastAPI con SQLAlchemy
- **Base de Datos**: MySQL

### Frontend (Vue.js)
- **Puerto**: 5173 (Vite dev server)
- **URL Base**: `http://localhost:5173`
- **Framework**: Vue 3 con Composition API
- **HTTP Client**: Axios

## Configuración CORS

El backend está configurado para permitir conexiones desde:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000` (Puerto alternativo)
- `http://127.0.0.1:5173` (Localhost alternativo)
- `http://127.0.0.1:3000` (Localhost alternativo)

## Estructura de Archivos

### Frontend

```
frontend/src/
├── services/
│   └── api.js              # Servicios API centralizados
├── composables/
│   └── useApi.js           # Composable para manejo de API
├── config.js               # Configuración de la aplicación
└── views/
    └── PacienteRegistro.vue # Ejemplo de uso de la API
```

### Backend

```
backend/app/
├── main.py                 # Aplicación FastAPI principal
├── database.py             # Configuración de base de datos
├── models.py               # Modelos SQLAlchemy
├── schemas.py              # Esquemas Pydantic
├── crud.py                 # Operaciones CRUD
└── routers/
    └── patients.py         # Rutas de pacientes
```

## Servicios API

### pacientesService
- `getPacientes(skip, limit)` - Obtener lista de pacientes
- `getPacienteById(id)` - Obtener paciente por ID
- `createPaciente(data)` - Crear nuevo paciente
- `updatePaciente(id, data)` - Actualizar paciente
- `deletePaciente(id)` - Eliminar paciente

### examenesService
- `getExamenes(skip, limit)` - Obtener lista de exámenes
- `getExamenById(id)` - Obtener examen por ID
- `createExamen(data)` - Crear nuevo examen
- `updateExamen(id, data)` - Actualizar examen
- `deleteExamen(id)` - Eliminar examen

### ordenesService
- `getOrdenes(skip, limit)` - Obtener lista de órdenes
- `getOrdenById(id)` - Obtener orden por ID
- `createOrden(data)` - Crear nueva orden
- `updateOrden(id, data)` - Actualizar orden
- `deleteOrden(id)` - Eliminar orden

### healthService
- `checkHealth()` - Verificar estado de la API

## Uso en Componentes

### Ejemplo Básico

```javascript
import { pacientesService } from '../services/api.js'
import { useApi } from '../composables/useApi.js'

const { loading, executeApiCall } = useApi()

const result = await executeApiCall(
  () => pacientesService.createPaciente(pacienteData),
  'Paciente registrado correctamente'
)

if (result.success) {
  // Manejar éxito
} else {
  // Manejar error
}
```

### Estado Global de la API

```javascript
import { apiState, checkApiConnection } from '../composables/useApi.js'

// Verificar conexión
await checkApiConnection()

// Estado disponible
console.log(apiState.isConnected)    // true/false
console.log(apiState.isLoading)      // true/false
console.log(apiState.error)          // mensaje de error
console.log(apiState.lastCheck)      // fecha de última verificación
```

## Scripts de Inicio

### Windows (Batch)
```bash
start-app.bat
```

### Windows (PowerShell)
```powershell
.\start-app.ps1
```

### Manual
```bash
# Terminal 1 - Backend
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Frontend
cd frontend
npm run dev
```

## Variables de Entorno

### Frontend (.env)
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_TITLE=ClynEra
VITE_APP_VERSION=1.0.0
```

### Backend (.env)
```env
DATABASE_URL=mysql+pymysql://root:1003@db:3306/laboratorio_clinico?charset=utf8mb4
```

## Manejo de Errores

### Interceptor Global
- Todos los errores de API se capturan automáticamente
- Se muestran en consola con formato consistente
- Se pueden personalizar las notificaciones

### Manejo en Componentes
```javascript
const result = await executeApiCall(apiFunction)

if (result.success) {
  // Éxito
  console.log(result.data)
} else {
  // Error
  console.error(result.error)
}
```

## Indicador de Estado

El frontend incluye un indicador visual en la barra de navegación que muestra:
- ✅ Verde: API conectada
- ❌ Rojo: API desconectada

## Endpoints Disponibles

### Pacientes
- `GET /pacientes` - Lista de pacientes
- `GET /pacientes/{id}` - Paciente por ID
- `POST /pacientes` - Crear paciente
- `PUT /pacientes/{id}` - Actualizar paciente
- `DELETE /pacientes/{id}` - Eliminar paciente

### Exámenes
- `GET /examenes` - Lista de exámenes
- `POST /examenes` - Crear examen

### Órdenes
- `GET /ordenes` - Lista de órdenes
- `GET /ordenes/{id}` - Orden por ID
- `POST /ordenes` - Crear orden
- `PUT /ordenes/{id}` - Actualizar orden
- `DELETE /ordenes/{id}` - Eliminar orden

### Health Check
- `GET /` - Estado de la API

## Troubleshooting

### Error 405 Method Not Allowed
Si recibes un error 405 al hacer POST a `/pacientes`:
1. Verificar que el router esté configurado correctamente en `backend/app/routers/patients.py`
2. Verificar que no haya endpoints duplicados en `backend/app/main.py`
3. Asegurarse de que el prefijo del router sea `/pacientes` (plural)
4. Verificar que los endpoints en el frontend usen la ruta correcta (`/pacientes/`)

### Error de CORS
- Verificar que el backend esté ejecutándose en el puerto 8000
- Verificar que el frontend esté ejecutándose en el puerto 5173
- Revisar la configuración CORS en `backend/app/main.py`

### Error de Conexión
- Verificar que la base de datos esté ejecutándose
- Verificar las variables de entorno
- Revisar los logs del backend

### Error de API
- Verificar que los endpoints existan en el backend
- Revisar el formato de los datos enviados
- Verificar la documentación de la API en `http://localhost:8000/docs`

### Scripts de Prueba
Para verificar que los endpoints funcionen correctamente:
```bash
# Probar endpoints
test-endpoints.bat

# Reiniciar backend si hay problemas
restart-backend.bat
``` 