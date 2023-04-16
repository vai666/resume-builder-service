# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from abc import ABC, abstractmethod
from typing import List
from initializer import db


class BaseService(ABC):
    def __init__(self, model: db.Model):
        self.entity = model

    def get(self, id: str) -> db.Model:
        return self.entity.query.get(id)

    def delete(self, id: str) -> str:
        self.entity.query.filter_by(id=id).delete()
        db.session.commit()
        return id

    @abstractmethod
    def get_all(self, filter: dict) -> List[db.Model]:
        pass

    @abstractmethod
    def save(self, data: dict) -> str:
        pass

    @abstractmethod
    def update(self, data: dict) -> str:
        pass
