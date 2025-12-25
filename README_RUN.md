# SCELLIDOC Backend (MVP)

![CI](https://github.com/Gali14591/IDORA/actions/workflows/ci.yml/badge.svg)
![Container](https://img.shields.io/container/v/Gali14591/idora?label=ghcr.io&logo=github)

## Setup
python -m venv venv
# Windows: venv\Scripts\activate
source venv/bin/activate

pip install -r requirements.txt

## Run (local)
cd scellidoc_api
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Run (Docker)
Pull the prebuilt container from GitHub Container Registry (GHCR):

```bash
# Replace OWNER with the repo owner (Gali14591)
docker pull ghcr.io/Gali14591/idora:latest

docker run -p 8000:8000 ghcr.io/Gali14591/idora:latest
```

To build locally:

```bash
docker build -t ghcr.io/Gali14591/idora:local .
docker run -p 8000:8000 ghcr.io/Gali14591/idora:local
```