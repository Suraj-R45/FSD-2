# Experiment 20: CI/CD Pipeline for Application Deployment

This experiment implements a CI/CD pipeline using Github Actions for the backend (Python) and frontend (Node.js) applications.

## Structure
- `backend/`: Python backend application with Dockerfile
- `frontend/`: Node.js frontend application with Dockerfile
- `.github/workflows/deploy.yml`: Github Actions workflow for CI/CD

## Docker Setup

### Backend
Navigate to `backend/` directory:
```
cd backend
docker build -t backend-app .
docker run -d -p 5000:5000 --name backend-container backend-app
```

### Frontend
Navigate to `frontend/` directory:
```
cd frontend
docker build -t frontend-app .
docker run -d -p 3000:3000 --name frontend-container frontend-app
```

## CI/CD Pipeline
The Github Actions workflow is in `.github/workflows/deploy.yml`. It triggers on push and pull requests to the main branch, building Docker images for both backend and frontend, and running the containers.

## Screenshots Required
- Docker image build and running container in CLI
- Github Actions workflow execution
