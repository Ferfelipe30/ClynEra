@echo off
echo ========================================
echo Iniciando ClynEra - Backend y Frontend
echo ========================================

echo.
echo 1. Iniciando Backend...
start "ClynEra Backend" cmd /k "cd backend && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

echo.
echo 2. Esperando 3 segundos para que el backend se inicie...
timeout /t 3 /nobreak > nul

echo.
echo 3. Iniciando Frontend...
start "ClynEra Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo Aplicacion iniciada!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo ========================================
echo.
echo Presiona cualquier tecla para cerrar esta ventana...
pause > nul 