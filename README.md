[![CI](https://github.com/GraphiteTuff/incident-tracker-api/actions/workflows/ci.yml/badge.svg)](https://github.com/GraphiteTuff/incident-tracker-api/actions/workflows/ci.yml)

# Incident Tracker API

A production-style **FastAPI** service for creating and managing operational incidents, backed by **PostgreSQL** with **Alembic migrations**, **Docker Compose** local dev, and **GitHub Actions CI**.

This project is built to demonstrate real-world backend patterns recruiters look for: clean layering (routes/services/db), config management, migrations, testing, and containerized development.

---

## Highlights
- ✅ CRUD API for incidents with **severity/status** fields
- ✅ **OpenAPI / Swagger UI** at `/docs`
- ✅ PostgreSQL persistence + **Alembic** migrations
- ✅ Docker Compose (API + DB)
- ✅ Pytest tests + CI passing on GitHub Actions
- ✅ CI defaults to SQLite so tests run without provisioning Postgres

---

## Tech Stack
- **Python 3.11**, FastAPI
- SQLAlchemy 2.x
- PostgreSQL 16
- Alembic (schema migrations)
- Docker / Docker Compose
- Pytest + GitHub Actions

---

## Project Structure
```text
├─ app/
│  ├─ api/routes/            # HTTP endpoints (routers)
│  ├─ services/              # business logic layer
│  ├─ schemas/               # request/response validation (Pydantic)
│  ├─ db/                    # SQLAlchemy engine/session/models
│  ├─ core/                  # settings/config
│  └─ main.py                # FastAPI app entrypoint
├─ alembic/                  # migrations
├─ tests/                    # pytest tests
├─ docker-compose.yml
├─ Dockerfile
├─ requirements.txt
└─ pytest.ini
```
## Quickstart (Docker)

### Recommended: run with Docker so Postgres is available.

1) Create environment file
cp .env.example .env
2) Build + run the stack
docker compose up --build
3) Open
- Health: http://localhost:8000/health
- Docs: http://localhost:8000/docs

## API Overview
### Health

- GET /health → {"status":"ok"}

## Incidents

- POST /incidents → create
- GET /incidents → list (supports optional filters)
- query params: status, severity, service
- GET /incidents/{id} → fetch one
- PATCH /incidents/{id} → partial update
- DELETE /incidents/{id} → delete

## Example Requests
- Create an incident

curl -X POST "http://localhost:8000/incidents" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "API timeout in checkout",
    "service": "checkout",
    "severity": "SEV2",
    "status": "Investigating",
    "summary": "Timeouts observed from 10:02 UTC. Investigating upstream dependency."
  }'

## List incidents
- curl "http://localhost:8000/incidents"

## Filter incidents
- curl "http://localhost:8000/incidents?severity=SEV2&status=Investigating"

## Database Migrations (Alembic)
- Create a migration (after changing models)
- docker compose run --rm api alembic -c /app/alembic.ini revision --autogenerate -m "your message"

## Apply migrations
- docker compose run --rm api alembic -c /app/alembic.ini upgrade head

## Tests
- Run tests locally
- pytest -q

## Run tests in Docker
- docker compose run --rm api pytest -q

## CI

- GitHub Actions runs tests on every push and pull request:
- Workflow: .github/workflows/ci.yml

## Notes / Design Decisions
- Settings are environment-driven using pydantic-settings.
- CI defaults DATABASE_URL to SQLite so unit tests run without provisioning Postgres.
- Docker uses .env for Postgres connectivity via the db service.

## Roadmap

- Pagination + sorting for list endpoint
- Incident updates/timeline endpoint (/incidents/{id}/updates)
- Integration tests using Postgres service in CI
- Authentication (API key/JWT) + structured request logging
