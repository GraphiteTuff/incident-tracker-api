from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_incident_validation_fails():
    r = client.post("/incidents", json={"title": "x", "service": "", "severity": "SEV9"})
    assert r.status_code == 422