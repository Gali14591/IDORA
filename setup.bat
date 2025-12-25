@echo off
echo Creation de l'environnement virtuel...
python -m venv venv
if errorlevel 1 (
    echo Erreur: Python n'est pas installe ou pas dans le PATH
    echo Essayez avec: py -m venv venv
    pause
    exit /b 1
)

echo Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo Installation des dependances...
pip install -r requirements.txt

echo Creation des migrations...
python manage.py makemigrations

echo Application des migrations...
python manage.py migrate

echo Serveur pret a demarrer!
echo Utilisez: python manage.py runserver
pause

