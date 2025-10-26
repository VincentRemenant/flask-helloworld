# Utiliser l'image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements en premier (pour le cache Docker)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer le port (Railway injectera la variable PORT)
EXPOSE $PORT

# Commande pour démarrer l'application
CMD gunicorn --bind 0.0.0.0:$PORT app:app