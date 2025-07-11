Write-Host "Starting ClynEra Database..." -ForegroundColor Green
docker-compose up -d db
Write-Host "Database started successfully!" -ForegroundColor Green
Write-Host "Database URL: postgresql://clynera_user:clynera_password@localhost:5432/clynera_db" -ForegroundColor Yellow 