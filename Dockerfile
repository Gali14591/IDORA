FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app/scellidoc_api

EXPOSE 8000

# For development, using runserver (change to gunicorn for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]