# pylint: disable=missing-docstring

from datetime import datetime
from initializer import db
from models.base import Base

class Expertise(Base):
    __tablename__ = "expertises"
    id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    resume_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("resume.id"))
    email = db.Column(db.String(150))
    expertise = db.Column(db.String, nullable=True)
    level = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)


