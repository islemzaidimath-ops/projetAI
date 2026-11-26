
FROM python:3.11-slim

WORKDIR /app

# Installation des dependances
COPY requirements.txt .

RUN pip install --no-cache-dir --default-timeout=300 --retries=10 -r requirements.txt

# Copie du projet
COPY . .

# Entrainement automatique du modele
RUN python -m app.model.train

# Port de l'application
EXPOSE 8000

# Lancement de FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
