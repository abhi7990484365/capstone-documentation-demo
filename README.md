# Capstone Documentation Demo API

A small Python REST API used as a sample repository for the ELITEA Automated Documentation Sync capstone.

## Purpose
This service exposes a health endpoint and a simple greeting endpoint. It is intended for documentation and workflow testing, not production use.

## Technology
- Python 3.11+
- FastAPI
- Uvicorn
- Pytest and FastAPI TestClient

## Run locally
```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the API documentation.

## Endpoints
- `GET /health` — returns service health.
- `GET /hello/{name}` — returns a greeting for the supplied name.

## Run tests
```bash
pytest
```

## Configuration
No secrets are required. `APP_ENV` is an optional environment variable and defaults to `development`.
