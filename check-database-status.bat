@echo off
echo ========================================
echo Verificando Estado de la Base de Datos
echo ========================================

echo.
echo 1. Verificando estado de Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker no está disponible
    echo Por favor, instala Docker Desktop
    pause
    exit /b 1
)

echo ✅ Docker está disponible

echo.
echo 2. Verificando contenedores de Docker...
docker ps -a --filter "name=clynera_mysql_container"

echo.
echo 3. Verificando si MySQL está ejecutándose...
docker ps --filter "name=clynera_mysql_container" --filter "status=running" | findstr "clynera_mysql_container" >nul
if %errorlevel% equ 0 (
    echo ✅ MySQL está ejecutándose
) else (
    echo ❌ MySQL no está ejecutándose
    echo.
    echo Para iniciar MySQL, ejecuta:
    echo setup-mysql-database.bat
    pause
    exit /b 1
)

echo.
echo 4. Verificando conexión a la base de datos...
python backend/test_mysql_connection.py

echo.
echo 5. Verificando tablas de la base de datos...
python -c "
import pymysql
try:
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root_password',
        database='laboratorio_clinico',
        charset='utf8mb4'
    )
    cursor = conn.cursor()
    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    print(f'✅ Tablas encontradas: {len(tables)}')
    for table in tables:
        print(f'   - {table[0]}')
    cursor.close()
    conn.close()
except Exception as e:
    print(f'❌ Error al verificar tablas: {e}')
"

echo.
echo ========================================
echo Verificación completada
echo ========================================
pause 