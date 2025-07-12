@echo off
echo ========================================
echo Reiniciando Backend ClynEra
echo ========================================

echo.
echo Deteniendo procesos existentes...
taskkill /f /im python.exe 2>nul
taskkill /f /im uvicorn.exe 2>nul

echo.
echo Esperando 2 segundos...
timeout /t 2 /nobreak > nul

echo.
echo Iniciando backend...
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

echo.
echo Presiona cualquier tecla para cerrar...
pause > nul 