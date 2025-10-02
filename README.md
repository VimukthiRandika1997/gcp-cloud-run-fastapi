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

## Decision Choices

- **Cloud Run**

    - No server management
    - Integrated logging and monitoring
    - Auto-scaling based on HTTP traffic

- **Docker**

    - Isolated development and maintainance

- **Google Artifact Registry**

    -  This is for the holding Docker images

- **Github Actions**

    - Secret management
    - Flexible CI/CD pipeline configurations

- **GCP CLI: `gcloud`**

    - Simple command line tool to interact with GCP resources directly
    - This is best suited for quick setup, local development automation
    - Note:
        - If the application is lightweight, deployed in a single environment and designed for fast prototyping, then `gcloud` cli is preferred
        - Terraform is ideal for complex, multi-environmental setups where full infrastructure as code (IaC) is required


## How does CI/CD Pipeline run:

- The pipeline is triggered on a push to the `main` branch

- Steps:

    1. Checkout code
    2. Install dependencies
    3. Lint using `pylint`
    4. Test using `pytest`
    5. Build Docker the image
    6. Scan the image with Docker Scout
    7. Push the image to the GCP Artifact Registry
    8. Deploy to Cloud Run
    9. Fetch GCP Cloud Run URL where the web api is deployed
    10. Create Uptime Check
    11. Output deployed URL in job summary 


## About Uptime & Obervability

- `/healthcheck` endpoint is configured for basic service checks
- Created uptime check with:
    - Protocol: HTTPS
    - Endpoint: `/healthcheck`
    - Interval: 1 min

- Logs are collected automatically by Cloud Run and stored in Cloud Logging


## Cost Summary

- This architecture is highly cost-effective which is designed to operate within **Free Tier** offered by GCP. 
- This is ideal for:
    - Rapid Development
    - Testing
    - Low Traffic production environment

### Scaling

- If this application needs to scale for *latency-sensitive* workloads or high-traffic, then we have to set this up to handle cold starts.
- In this case, the cost may go up high
- Like setting up minimum instances to be run in the Cloud Run: `--min-instances=1`


## What is The Final Output

- **Deployed URL**: Captured & logged via Github Actions
- **Monitoring**:  Configurable alerts via Cloud Monitoring
- **Docker Image**: Built Docker images are available in Google Artifact Registry


## How to Run

