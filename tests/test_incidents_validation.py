from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_incident_validation_fails():
    r = client.post("/incidents", json={"title": "x", "service": "", "severity": "SEV9"})
    assert r.status_code == 422

def test_create_incident_rejects_blank_text_fields():
    title_response = client.post(
        "/incidents",
        json={"title": "     ", "service": "api", "severity": "SEV2"},
    )
    assert title_response.status_code == 422

    service_response = client.post(
        "/incidents",
        json={"title": "Valid title", "service": "   ", "severity": "SEV2"},
    )
    assert service_response.status_code == 422
