from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.incidents import IncidentCreate, IncidentUpdate, IncidentOut
from app.services.incidents_service import (
    create_incident, get_incident, list_incidents, update_incident, delete_incident
)

router = APIRouter(prefix="/incidents", tags=["incidents"])

@router.post("", response_model=IncidentOut, status_code=status.HTTP_201_CREATED)
def create(payload: IncidentCreate, db: Session = Depends(get_db)):
    return create_incident(db, payload)

@router.get("", response_model=list[IncidentOut])
def list_(
    status: str | None = None,
    severity: str | None = None,
    service: str | None = None,
    db: Session = Depends(get_db),
):
    return list_incidents(db, status=status, severity=severity, service=service)

@router.get("/{incident_id}", response_model=IncidentOut)
def get_one(incident_id: int, db: Session = Depends(get_db)):
    obj = get_incident(db, incident_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Incident not found")
    return obj

@router.patch("/{incident_id}", response_model=IncidentOut)
def patch(incident_id: int, payload: IncidentUpdate, db: Session = Depends(get_db)):
    obj = update_incident(db, incident_id, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Incident not found")
    return obj

@router.delete("/{incident_id}", status_code=204)
def remove(incident_id: int, db: Session = Depends(get_db)):
    ok = delete_incident(db, incident_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Incident not found")
    return None