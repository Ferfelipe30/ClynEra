@echo off
echo Starting ClynEra Backend...
echo.
echo Checking database connection first...
cd backend
python test_connection.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️ Database connection failed!
    echo Please run setup-database.ps1 first to configure the database.
    echo.
    pause
    exit /b 1
)
echo.
echo ✅ Database connection successful!
echo Starting FastAPI server...
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 