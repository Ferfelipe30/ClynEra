Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Configurando Base de Datos MySQL" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Write-Host ""
Write-Host "1. Verificando si Docker está ejecutándose..." -ForegroundColor Yellow
try {
    docker --version | Out-Null
    Write-Host "✅ Docker está disponible" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker no está instalado o no está en el PATH" -ForegroundColor Red
    Write-Host "Por favor, instala Docker Desktop y reinicia la terminal" -ForegroundColor Yellow
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host ""
Write-Host "2. Deteniendo contenedores existentes..." -ForegroundColor Yellow
docker-compose down

Write-Host ""
Write-Host "3. Iniciando la base de datos MySQL..." -ForegroundColor Yellow
docker-compose up -d db

Write-Host ""
Write-Host "4. Esperando a que MySQL esté listo..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

Write-Host ""
Write-Host "5. Verificando conexión a la base de datos..." -ForegroundColor Yellow
python backend/test_mysql_connection.py

Write-Host ""
Write-Host "6. Inicializando tablas de la base de datos..." -ForegroundColor Yellow
python backend/init_mysql_db.py

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "✅ Base de datos configurada correctamente" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Ahora puedes iniciar el backend con:" -ForegroundColor Yellow
Write-Host "start-backend.bat" -ForegroundColor White
Write-Host ""
Write-Host "O iniciar toda la aplicación con:" -ForegroundColor Yellow
Write-Host "start-app.bat" -ForegroundColor White
Write-Host ""
Read-Host "Presiona Enter para continuar" 