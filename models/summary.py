# pylint: disable=missing-docstring

from datetime import datetime
from initializer import db
from models.base import Base

class Summary(Base):
    __tablename__ = "summaries"
    id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    resume_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("resumes.id"))
    email = db.Column(db.String(150))
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
