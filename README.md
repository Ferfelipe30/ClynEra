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

#### Option A: Using Docker
```bash
# Start PostgreSQL with Docker
docker-compose up -d db
```

#### Option B: Using Local PostgreSQL
```bash
# Setup and test database connection
setup-database.ps1
```

#### Initialize Tables
```bash
# Create database tables
init-database.bat
```

### 5. Start the Application

#### Option A: Using the provided scripts (Windows)
```bash
# Terminal 1 - Start Backend
start-backend.bat

# Terminal 2 - Start Frontend  
start-frontend.bat
```

#### Option B: Manual start
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

### Database Connection Errors
If you get database connection errors:

#### Option 1: Using Docker (if you have Docker installed)
```bash
# Start the database using Docker
docker-compose up -d db
```

#### Option 2: Using Local PostgreSQL
1. Ensure PostgreSQL is installed and running
2. Verify the database exists: `setup-database.ps1`
3. Test the connection: `test-connection.bat`
4. If the database doesn't exist, it will be created automatically

#### Common Issues:
- **UTF-8 Encoding Error**: The connection string now includes `client_encoding=utf8`
- **Database doesn't exist**: Run `setup-database.ps1` to create it
- **Connection refused**: Ensure PostgreSQL is running on port 5432
- **Authentication failed**: Verify username and password in `backend/app/database.py`

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
│   │   ├── config.js        # API configuration
│   │   └── main.js
│   └── package.json
└── docker-compose.yml
```

## API Endpoints

### Pacientes
- `POST /paciente/` - Crear un nuevo paciente
- `GET /paciente/` - Obtener todos los pacientes
- `GET /paciente/{id}` - Obtener paciente por ID
- `PUT /paciente/{id}` - Actualizar paciente
- `DELETE /paciente/{id}` - Eliminar paciente

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
DATABASE_URL=postgresql://clynera_user:clynera_password@localhost:5432/clynera_db
```

### Frontend (.env file in frontend directory)
```
VITE_API_BASE_URL=http://localhost:8000
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request 