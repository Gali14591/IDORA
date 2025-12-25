# Script PowerShell pour démarrer le serveur Django

Write-Host "=== SCELLIDOC API - Démarrage du serveur ===" -ForegroundColor Green

# Vérifier si l'environnement virtuel existe
if (-not (Test-Path "venv")) {
    Write-Host "Création de l'environnement virtuel..." -ForegroundColor Yellow
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Erreur: Python n'est pas installé ou pas dans le PATH" -ForegroundColor Red
        Write-Host "Veuillez installer Python depuis https://www.python.org/" -ForegroundColor Red
        exit 1
    }
}

# Activer l'environnement virtuel
Write-Host "Activation de l'environnement virtuel..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

# Installer les dépendances si nécessaire
if (-not (Test-Path "venv\Lib\site-packages\django")) {
    Write-Host "Installation des dépendances..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

# Créer les migrations
Write-Host "Création des migrations..." -ForegroundColor Yellow
python manage.py makemigrations
if ($LASTEXITCODE -ne 0) {
    Write-Host "Erreur lors de la création des migrations" -ForegroundColor Red
    exit 1
}

# Appliquer les migrations
Write-Host "Application des migrations..." -ForegroundColor Yellow
python manage.py migrate
if ($LASTEXITCODE -ne 0) {
    Write-Host "Erreur lors de l'application des migrations" -ForegroundColor Red
    exit 1
}

# Démarrer le serveur
Write-Host "`n=== Démarrage du serveur Django ===" -ForegroundColor Green
Write-Host "Le serveur sera accessible sur: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "Appuyez sur Ctrl+C pour arrêter le serveur`n" -ForegroundColor Yellow

python manage.py runserver

