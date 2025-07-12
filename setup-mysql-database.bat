@echo off
echo ========================================
echo Configurando Base de Datos MySQL
echo ========================================

echo.
echo 1. Verificando si Docker está ejecutándose...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker no está instalado o no está en el PATH
    echo Por favor, instala Docker Desktop y reinicia la terminal
    pause
    exit /b 1
)

echo ✅ Docker está disponible

echo.
echo 2. Deteniendo contenedores existentes...
docker-compose down

echo.
echo 3. Iniciando la base de datos MySQL...
docker-compose up -d db

echo.
echo 4. Esperando a que MySQL esté listo...
timeout /t 10 /nobreak > nul

echo.
echo 5. Verificando conexión a la base de datos...
python backend/test_mysql_connection.py

echo.
echo 6. Inicializando tablas de la base de datos...
python backend/init_mysql_db.py

echo.
echo ========================================
echo ✅ Base de datos configurada correctamente
echo ========================================
echo.
echo Ahora puedes iniciar el backend con:
echo start-backend.bat
echo.
echo O iniciar toda la aplicación con:
echo start-app.bat
echo.
pause 