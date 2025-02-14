
.PHONY: init run test build clean

# Installation des dépendances Python
init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Lancer l'application Flask directement (sans Docker)
run:
	@echo "Running the Flask app locally..."
	python3 app.py

# Exécuter les tests unitaires
test:
	@echo "Running tests..."
	pytest tests/

# Construire l'image Docker
build:
	@echo "Building the Docker image..."
	docker build -t health-calculator .

# Nettoyer les fichiers inutiles
clean:
	@echo "Cleaning up..."
	rm -rf __pycache__ .pytest_cache
