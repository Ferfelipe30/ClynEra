# ClynEra - Patient Management System

A full-stack application for managing patients and medical orders, built with FastAPI (backend) and Vue.js (frontend).

## Prerequisites

- Python 3.8+
- Node.js 16+
- Docker and Docker Compose
- PostgreSQL (via Docker)

## Quick Start

### 1. Start the Database

```bash
docker-compose up -d db
```

This will start a PostgreSQL database with the following credentials:
- Host: localhost
- Port: 5432
- Database: clynera_db
- Username: clynera_user
- Password: clynera_password

### 2. Setup Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Setup Frontend

```bash
cd frontend
npm install
```

### 4. Setup Database

#### Option A: Using Docker (Recommended)
```bash
# Setup and start MySQL database
setup-mysql-database.bat
```

#### Option B: Manual Setup
```bash
# Start MySQL with Docker
docker-compose up -d db

# Wait for MySQL to be ready (about 10 seconds)
# Then initialize tables
python backend/init_mysql_db.py
```

#### Verify Database Status
```bash
# Check if database is running correctly
check-database-status.bat
```

### 5. Start the Application

#### Option A: Using the provided scripts (Windows)
```bash
# Start both Backend and Frontend with one command
start-app.bat

# Or start them separately:
# Terminal 1 - Start Backend
start-backend.bat

# Terminal 2 - Start Frontend  
start-frontend.bat
```

#### Option B: Using PowerShell
```powershell
# Start both Backend and Frontend with one command
.\start-app.ps1
```

#### Option C: Manual start
```bash
# Terminal 1 - Start Backend
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Start Frontend
cd frontend
npm run dev
```

### 6. Test the API (Optional)

```bash
# Probar que todos los endpoints funcionan correctamente
test-api.bat
```

## Access the Application

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Troubleshooting

### CORS Errors
If you encounter CORS errors, ensure:
1. The backend is running on port 8000
2. The frontend is running on port 5173
3. CORS is properly configured in `backend/app/main.py`
4. Check the API connection indicator in the frontend navbar

### API Connection Issues
- The frontend includes a visual indicator in the navbar showing API connection status
- Green dot: API connected ✅
- Red dot: API disconnected ❌
- Check the browser console for detailed error messages
- Verify both services are running on the correct ports

### Database Connection Errors
If you get database connection errors:

#### Option 1: Using Docker (Recommended)
```bash
# Setup and start MySQL database
setup-mysql-database.bat

# Or manually:
docker-compose up -d db
```

#### Option 2: Check Database Status
```bash
# Verify database status
check-database-status.bat
```

#### Common Issues:
- **Access denied error**: The database is configured to use MySQL with Docker
- **Database doesn't exist**: Run `setup-mysql-database.bat` to create it
- **Connection refused**: Ensure Docker is running and MySQL container is started
- **Authentication failed**: The default credentials are `root:root_password`
- **Port conflicts**: MySQL runs on port 3306 by default

### 500 Internal Server Error
If you get 500 errors when creating patients:
1. Check that the database is running and accessible
2. Verify the database tables were created (they should be created automatically)
3. Check the backend logs for specific error messages

## Project Structure

```
clynera/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI application
│   │   ├── database.py      # Database configuration
│   │   ├── models.py        # SQLAlchemy models
│   │   ├── schemas.py       # Pydantic schemas
│   │   ├── crud.py          # Database operations
│   │   ├── dependencies.py  # FastAPI dependencies
│   │   └── routers/
│   │       └── patients.py  # Patient endpoints
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   │   ├── PacienteRegistro.vue
│   │   │   └── ...
│   │   ├── services/
│   │   │   └── api.js       # API services
│   │   ├── composables/
│   │   │   └── useApi.js    # API composable
│   │   ├── config.js        # API configuration
│   │   └── main.js
│   └── package.json
├── start-app.bat            # Start both services (Windows)
├── start-app.ps1            # Start both services (PowerShell)
└── docker-compose.yml
```

## API Endpoints

### Pacientes
- `POST /pacientes/` - Crear un nuevo paciente
- `GET /pacientes/` - Obtener todos los pacientes
- `GET /pacientes/{id}` - Obtener paciente por ID
- `PUT /pacientes/{id}` - Actualizar paciente
- `DELETE /pacientes/{id}` - Eliminar paciente

### Frontend Routes
- `/` - Página principal con menú
- `/paciente` - Formulario de registro de pacientes
- `/pacientes` - Lista de pacientes registrados
- `/orden` - Crear orden de examen
- `/historial/{documento}` - Historial de paciente

## Development

### Backend Development
- The backend uses FastAPI with automatic API documentation
- Database models are defined in `models.py`
- API schemas are defined in `schemas.py`
- CRUD operations are in `crud.py`

### Frontend Development
- Built with Vue 3 and Vite
- Uses Vue Router for navigation
- Axios for API communication
- Modern CSS with scoped styles

## Environment Variables

The application uses the following environment variables:

### Backend (.env file in backend directory)
```
DATABASE_URL=mysql+pymysql://root:root_password@localhost:3306/laboratorio_clinico?charset=utf8mb4
```

### Frontend (.env file in frontend directory)
```
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_TITLE=ClynEra
VITE_APP_VERSION=1.0.0
```

## API Integration

The frontend and backend are fully integrated with:

- **Centralized API Services**: All API calls are managed through `frontend/src/services/api.js`
- **Global State Management**: API connection status is tracked globally
- **Error Handling**: Consistent error handling across all API calls
- **Loading States**: Automatic loading state management
- **CORS Configuration**: Properly configured for development and production

For detailed information about the API integration, see [FRONTEND_BACKEND_CONNECTION.md](FRONTEND_BACKEND_CONNECTION.md).
```
VITE_API_BASE_URL=http://localhost:8000
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request 