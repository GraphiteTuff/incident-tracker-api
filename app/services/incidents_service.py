from sqlalchemy.orm import Session
from app.db.models import Incident
from app.schemas.incidents import IncidentCreate, IncidentUpdate

def create_incident(db: Session, payload: IncidentCreate) -> Incident:
    obj = Incident(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_incident(db: Session, incident_id: int) -> Incident | None:
    return db.query(Incident).filter(Incident.id == incident_id).first()

def list_incidents(db: Session, status: str | None, severity: str | None, service: str | None) -> list[Incident]:
    q = db.query(Incident)
    if status:
        q = q.filter(Incident.status == status)
    if severity:
        q = q.filter(Incident.severity == severity)
    if service:
        q = q.filter(Incident.service == service)
    return q.order_by(Incident.created_at.desc()).all()

def update_incident(db: Session, incident_id: int, payload: IncidentUpdate) -> Incident | None:
    obj = get_incident(db, incident_id)
    if not obj:
        return None

    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(obj, k, v)

    db.commit()
    db.refresh(obj)
    return obj

def delete_incident(db: Session, incident_id: int) -> bool:
    obj = get_incident(db, incident_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True