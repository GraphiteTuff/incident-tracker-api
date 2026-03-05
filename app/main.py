from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.incidents import router as incidents_router

app = FastAPI(title=settings.app_name)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(incidents_router)