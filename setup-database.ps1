Write-Host "🔧 Configurando base de datos PostgreSQL..." -ForegroundColor Green

# Verificar si PostgreSQL está ejecutándose
Write-Host "📊 Verificando si PostgreSQL está ejecutándose..." -ForegroundColor Yellow
try {
    $pgProcess = Get-Process -Name "postgres" -ErrorAction SilentlyContinue
    if ($pgProcess) {
        Write-Host "✅ PostgreSQL está ejecutándose" -ForegroundColor Green
    } else {
        Write-Host "⚠️ PostgreSQL no parece estar ejecutándose" -ForegroundColor Yellow
        Write-Host "💡 Asegúrate de que PostgreSQL esté instalado y ejecutándose" -ForegroundColor Cyan
    }
} catch {
    Write-Host "⚠️ No se pudo verificar el estado de PostgreSQL" -ForegroundColor Yellow
}

# Verificar si el puerto 5432 está en uso
Write-Host "🔌 Verificando puerto 5432..." -ForegroundColor Yellow
try {
    $portCheck = netstat -an | findstr ":5432"
    if ($portCheck) {
        Write-Host "✅ Puerto 5432 está en uso (probablemente PostgreSQL)" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Puerto 5432 no está en uso" -ForegroundColor Yellow
    }
} catch {
    Write-Host "⚠️ No se pudo verificar el puerto 5432" -ForegroundColor Yellow
}

Write-Host "`n🚀 Ejecutando script de prueba de conexión..." -ForegroundColor Green
cd backend
python test_connection.py

Write-Host "`n📋 Información de conexión:" -ForegroundColor Cyan
Write-Host "Host: localhost" -ForegroundColor White
Write-Host "Puerto: 5432" -ForegroundColor White
Write-Host "Base de datos: laboratorio_clinico" -ForegroundColor White
Write-Host "Usuario: ferju" -ForegroundColor White
Write-Host "Contraseña: 1003" -ForegroundColor White

Write-Host "`n💡 Si hay problemas de conexión:" -ForegroundColor Yellow
Write-Host "1. Verifica que PostgreSQL esté instalado y ejecutándose" -ForegroundColor White
Write-Host "2. Verifica que el usuario 'ferju' tenga permisos" -ForegroundColor White
Write-Host "3. Verifica que la base de datos 'laboratorio_clinico' exista" -ForegroundColor White
Write-Host "4. Verifica que el puerto 5432 esté disponible" -ForegroundColor White 