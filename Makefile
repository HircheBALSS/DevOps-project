# Nom du conteneur et de l'image
CONTAINER_NAME = flask-app-container
IMAGE_NAME = flask-app

# Cible par défaut (aide)
help:
	@echo "Makefile pour la gestion de l'application Flask avec Docker"
	@echo "  make init         - Crée et active l'environnement virtuel"
	@echo "  make create-image - Crée l'image Docker"
	@echo "  make build        - Crée l'image Docker sans utiliser le cache"
	@echo "  make run          - Lance le conteneur Docker"
	@echo "  make stop         - Arrête et supprime le conteneur Docker"
	@echo "  make clean        - Supprime l'image Docker"
	@echo "  make install      - installe les dépendances"
	@echo "  make test         - Exécute les tests unitaires"

init:
	python3 -m venv .venv
	@echo "Environnement virtuel créé. Activez-le avec : source .venv/bin/activate"

install:
	pip install -r requirements.txt
	@echo "Les dépendances ont été installées."

create-image:
	docker build -t $(IMAGE_NAME) .

build:
	docker build --no-cache -t $(IMAGE_NAME) .

run:
	docker run -p 5000:5000 --name $(CONTAINER_NAME) -d $(IMAGE_NAME)
	@echo "Le conteneur $(CONTAINER_NAME) est en cours d'exécution sur le port 5000."

stop:
	docker stop $(CONTAINER_NAME) 
	true
	docker rm $(CONTAINER_NAME) || true
	@echo "Le conteneur $(CONTAINER_NAME) a été arrêté et supprimé."

clean:
	docker rmi -f $(IMAGE_NAME)
	@echo "L'image Docker $(IMAGE_NAME) a été supprimée."

test:
	pytest test.py -v

