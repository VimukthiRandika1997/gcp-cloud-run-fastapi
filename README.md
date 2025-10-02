# FastAPI Deployment to GCP Cloud Run

## Overview

This project showcases how to securely build, test, containerize and deploy a Python FastAPI web API to GCP Cloud Run using Github Actions. This includes:

- CI/CD automation
- Security scanning
- Uptime monitoring


## Tech Stack

- **API Framework**: FastAPI
- **Containerization**: Docker
- **Security**: Docker Scout for vulnerability scanning
- **Container Registry**: Google Artifact Registry
- **Deployment**: GCP Cloud Run
- **Monitoring**: GCP Cloud Monitoring for uptime checks, logs
- **CI/CD**: Github Actions (triggered on `main` branch)