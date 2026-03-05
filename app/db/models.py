from sqlalchemy import Column, DateTime, Integer, String, Text, func
from app.db.base import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    service = Column(String(80), nullable=False)
    severity = Column(String(10), nullable=False)
    status = Column(String(20), nullable=False)
    summary = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )