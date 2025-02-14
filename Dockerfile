# Utiliser une image Python officielle comme base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Installer des versions spécifiques pour éviter les conflits
RUN pip install --no-cache-dir Flask==2.0.2 Werkzeug==2.0.3

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer l’application
CMD ["python", "app.py"]

# Copier les fichiers statiques pour le front
COPY static /app/static

