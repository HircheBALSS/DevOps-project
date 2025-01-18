
Voici le README.md complet pour votre projet. Vous pouvez copier-coller ce contenu dans un fichier nommé README.md à la racine de votre projet.

markdown
Copier
Modifier
# Python Web Application - Azure Deployment

This repository contains a Python web application for BMI and BMR calculations, developed using Flask and deployed to Microsoft Azure with Docker and GitHub Actions.

---

## Project Overview

- **Application Name**: `project-azure`
- **Description**: A web app that allows users to calculate BMI and BMR interactively.
- **Deployment**: Hosted on Microsoft Azure using App Service.
- **CI/CD Pipeline**: Automated using GitHub Actions.

---

## Features

- BMI (Body Mass Index) Calculator.
- BMR (Basal Metabolic Rate) Calculator.
- Interactive web interface using HTML and CSS.
- Containerized deployment using Docker.
- Automated CI/CD pipeline with testing and deployment workflows.

---

## Project Structure

project-azure/ ├── app.py # Main application file ├── health_utils.py # Utility functions for BMI and BMR calculations ├── templates/ # HTML templates for the web interface │ ├── index.html # Homepage │ ├── bmi.html # BMI calculation page │ ├── bmr.html # BMR calculation page ├── static/ # Static files (CSS, JS, images) │ └── styles.css # Stylesheet for the app ├── tests/ # Unit tests │ ├── test_app.py # Tests for app routes │ ├── test_health_utils.py # Tests for utility functions ├── requirements.txt # Python dependencies ├── Dockerfile # Docker build configuration ├── Makefile # Automation commands └── .github/workflows/ # CI/CD configuration └── azure.yml # GitHub Actions workflow for Azure

markdown
Copier
Modifier

---

## Prerequisites

1. **Local Development**:
   - Python 3.12 or higher installed.
   - Docker installed.
   - Virtual environment support (`venv`).

2. **Azure Deployment**:
   - An Azure account.
   - Azure App Service created for hosting.
   - Azure CLI installed (optional for manual testing).

3. **GitHub Secrets**:
   Add the following secrets to your repository for Azure deployment:
   - `AZUREAPPSERVICE_CLIENTID`
   - `AZUREAPPSERVICE_TENANTID`
   - `AZUREAPPSERVICE_SUBSCRIPTIONID`

---

## Installation and Setup

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/project-azure.git
   cd project-azure
Set up virtual environment:

bash
Copier
Modifier
make init
Run the app locally:

bash
Copier
Modifier
python app.py
Access the app: Open your browser and go to http://localhost:5000.

Testing
Run tests:

bash
Copier
Modifier
make test
Test coverage:

Tests are provided for both utility functions (health_utils) and app routes.
Deployment
This project uses GitHub Actions for CI/CD.

Workflow Triggers
Push to main branch: Automatically triggers the pipeline.
Manual Trigger: Via GitHub's Actions UI.
Deployment Steps
CI/CD Workflow File: The workflow file .github/workflows/azure.yml includes:

Building the Docker image.
Running tests.
Deploying the app to Azure App Service.
Build Commands:

Build Docker image:
bash
Copier
Modifier
make build
Run the container locally:
bash
Copier
Modifier
make run
Stop the container:
bash
Copier
Modifier
make stop
Azure Deployment: The app is deployed to Azure App Service. Ensure your secrets are configured in GitHub.

Makefile Commands
Command	Description
make init	Set up virtual environment and install dependencies.
make build	Build the Docker image for the app.
make run	Run the Docker container locally.
make stop	Stop the running Docker container.
make test	Run the test suite using pytest.
make clean	Clean up Docker images and containers.
Known Issues
Missing Dependencies: If you encounter ModuleNotFoundError, ensure the virtual environment is activated:
bash
Copier
Modifier
source .venv/bin/activate
Azure Deployment Failures: Verify secrets in GitHub and Azure App Service configurations.