# SCELLIDOC API - Backend Django

![CI](https://github.com/Gali14591/IDORA/actions/workflows/ci.yml/badge.svg)

**Note:** The CI workflow runs Django migrations and tests from the repository root using `python manage.py`.

## Structure du projet

```
scellidoc_api/
  manage.py
  requirements.txt
  scellidoc_api/
    __init__.py
    settings.py
    urls.py
    wsgi.py
  accounts/
    __init__.py
    apps.py
    models.py
    serializers.py
    views.py
    urls.py
  documents/
    __init__.py
    apps.py
    models.py
    serializers.py
    views.py
    urls.py
  sends/
    __init__.py
    apps.py
    models.py
    serializers.py
    views.py
    urls.py
  inbox/
    __init__.py
    apps.py
    models.py
    serializers.py
    views.py
    urls.py
  audit/
    __init__.py
    apps.py
    models.py
    serializers.py
    views.py
    urls.py
```

## Installation

1. Créer un environnement virtuel :
   ```bash
   python -m venv venv
   ```

2. Activer l'environnement virtuel :
   - Windows : `venv\Scripts\activate`
   - Mac/Linux : `source venv/bin/activate`

3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Créer les migrations :
   ```bash
   python manage.py makemigrations
   ```

5. Appliquer les migrations :
   ```bash
   python manage.py migrate
   ```

6. Lancer le serveur :
   ```bash
   python manage.py runserver
   ```

## Endpoints disponibles

- `POST /api/accounts/register/` - Inscription d'un nouvel utilisateur
- `POST /api/auth/token/` - Obtenir un token JWT (authentification)
- `POST /api/auth/token/refresh/` - Rafraîchir le token JWT
- `GET /api/documents/` - Liste des documents (authentifié)
- `POST /api/documents/` - Créer un document (authentifié)
- `GET /api/sends/` - Liste des envois (authentifié)
- `POST /api/sends/` - Créer un envoi (authentifié)
- `GET /api/inbox/` - Liste des messages reçus (authentifié)
- `GET /api/audit/` - Liste des logs d'audit (authentifié)

## Test de l'API

### 1. Inscription
```bash
POST http://127.0.0.1:8000/api/accounts/register/
Content-Type: application/json

{
  "phone": "+242060000000",
  "role": "citizen",
  "password": "1234",
  "password2": "1234"
}
```

### 2. Authentification
```bash
POST http://127.0.0.1:8000/api/auth/token/
Content-Type: application/json

{
  "username": "+242060000000",
  "password": "1234"
}
```

La réponse contiendra `access` et `refresh` tokens.

