# pylint: disable=missing-docstring

from datetime import datetime
from initializer import db
from models.base import Base

class Resume(Base):
    __tablename__ = "resumes"
    id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
