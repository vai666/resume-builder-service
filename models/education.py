# pylint: disable=missing-docstring

from datetime import datetime
from initializer import db
from models.base import Base

class Education(Base):
    __tablename__ = "educations"
    id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    resume_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("resumes.id"))
    email = db.Column(db.String(150))
    major = db.Column(db.String, nullable=True)
    institution = db.Column(db.String(200), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    month = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
