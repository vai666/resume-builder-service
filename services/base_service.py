# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.exc import OperationalError
from initializer import db


class BaseService(ABC):
    def __init__(self, model: db.Model):
        self.model = model

    def get_by_resume(self, resume_id: str, email: str, serialize=True) -> db.Model:
        try:
            entity = self.model.query.filter_by(resume_id=resume_id, email=email).first()
            if entity is None:
                return None
       
            if serialize:
                return entity.to_dict()
       
            return entity
        except OperationalError:
            return None
        
    def get(self, id: str, email: str, serialize: bool=True) -> db.Model:
        try:
            entity = self.model.query.filter_by(id=id, email=email).first()
            if entity is None:
                return None
       
            if serialize:
                return entity.to_dict()
       
            return entity
        except OperationalError:
            return None

    def delete(self, id: str, email: str) -> str:
        self.model.query.filter_by(id=id, email=email).delete()
        db.session.commit()
        return id

    @abstractmethod
    def get_all(self, filter: dict) -> List[db.Model]:
        pass

    @abstractmethod
    def save(self, data: dict) -> dict:
        pass

    @abstractmethod
    def update(self, data: dict) -> str:
        pass
