# Health Calculator Service : 

Health Calculator Service est une application web permettant aux utilisateurs 
de calculer leur Indice de Masse Corporelle (BMI) et leur Métabolisme de Base (BMR). 
L'application est développée en Flask, conteneurisée avec Docker, et inclut 
une pipeline CI/CD pour les tests et le déploiement automatique sur Azure Web Apps.

  #  Fonctionnalités
 
- Calcul du BMI basé sur le poids et la taille.
- Calcul du BMR basé sur le poids, la taille, l'âge et le genre.
- Interface web simple et réactive pour tester les calculs.

  #  Structure du projet
  Stucture du Projet : 
  
```
/health-calculator-service
|-- app.py
|-- health_utils.py
|-- static
|   |-- index.html
|-- tests
|   |-- test_health.py
|-- requirements.txt
|-- Dockerfile
|-- Makefile
/.github
|-- workflows
|   |-- ci-cd.yml
.gitignore
README.md
``` 

  #  Pré-requis
  Prérequis:

    Python: 3.9+
    
    Docker: Requis
    
    Un compte Azure: Requis pour le déploiement

  #  Installation
 ### Étape 1️ Cloner le projet
  
        git clone https://github.com/yassin-alfa/health-calculator-service.git
        cd health-calculator-service
        make setenv
        source .env/bin/activate  # Linux/macOS
        venv\Scripts\activate     # Windows
        make init

  ### Étapes 2️ Lancer l'application
        make local
         L'application est accessible sur **http://localhost:8000**

  #  Docker
Cette section décrit les commandes Docker essentielles pour construire, exécuter et gérer l'application dans un conteneur.
Assurez-vous que Docker est installé et en cours d'exécution avant d'exécuter ces commandes.
commandes
```
      make build
      make run
      make stop
      make push
```

  #  CI/CD Pipeline (GitHub Actions)
 ### CI_CD_Pipeline:
  
      Le pipeline CI/CD est configuré via GitHub Actions et inclut :
      - Tests automatisés à chaque push sur `main`
      - Construction et push de l’image Docker vers GitHub Container Registry (GHCR)
      - Déploiement automatique sur Azure Web Apps
      
  ### Vérification: 
    
  Vérifier le statut du pipeline :
       
      1. Aller sur GitHub > Actions
      2. Vérifier l'exécution du dernier workflow

  #  Déploiement sur Azure
   
Pour déployer cette application sur Azure, suivez ces étapes :
1. Créer un groupe de ressources sur Azure.
2. Créer une Web App Service dans ce groupe de ressources.
3. Connecter la Web App Service à GitHub via le Deployment Center d'Azure.
4. Une fois connecté, GitHub Actions prendra en charge le déploiement automatique de l'application.

Note:

 Assurez-vous que votre Web App Service est configurée pour utiliser Docker et pointe vers l’image Docker correcte.
 Le déploiement commencera automatiquement après chaque push sur GitHub

  Accéder à l'application en ligne :
    
    https://health-calculator123.azurewebsites.net/

  #  Remerciements
  
Un immense merci au formateur pour son accompagnement et ses conseils précieux tout au long de ce projet.
 
  #  Message Final
  
Merci d'utiliser Health Calculator Service !
