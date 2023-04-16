# pylint: disable=missing-docstring

from datetime import datetime
from initializer import db
from models.base import Base

class Header(Base):
    __tablename__ = "headers"
    id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    resume_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("resume.id"))
    email = db.Column(db.String(150))
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    linkedin_url = db.Column(db.String(100), nullable=True)
    github_url = db.Column(db.String(100), nullable=True)
    custom_url = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

