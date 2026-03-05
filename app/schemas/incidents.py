from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

Severity = Literal["SEV1", "SEV2", "SEV3"]
Status = Literal["Open", "Investigating", "Monitoring", "Resolved"]

class IncidentCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=120)
    service: str = Field(..., min_length=2, max_length=80)
    severity: Severity
    status: Status = "Open"
    summary: Optional[str] = Field(None, max_length=2000)

class IncidentUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=5, max_length=120)
    service: Optional[str] = Field(None, min_length=2, max_length=80)
    severity: Optional[Severity] = None
    status: Optional[Status] = None
    summary: Optional[str] = Field(None, max_length=2000)

class IncidentOut(BaseModel):
    id: int
    title: str
    service: str
    severity: Severity
    status: Status
    summary: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True