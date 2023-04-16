# pylint: disable=missing-docstring

from datetime import datetime
from initializer import db
from models.base import Base

class Experience(Base):
    __tablename__ = "experiences"
    id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    resume_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("resumes.id"))
    email = db.Column(db.String(150))
    company_name = db.Column(db.String(100), nullable=True)
    job_desc = db.Column(db.String(100), nullable=True)
    month_from = db.Column(db.Integer, nullable=True)
    year_from = db.Column(db.Integer, nullable=True)
    month_to = db.Column(db.Integer, nullable=True)
    year_to = db.Column(db.Integer, nullable=True)
    additional_info = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    formatted = db.Column(db.Text, nullable=True)
    is_present = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

