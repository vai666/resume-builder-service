# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

import uuid
from typing import List
from services.base_service import BaseService
from models.summary import Summary
from initializer import db


class SummaryService(BaseService):
    def __init__(self, model: Summary):
        super().__init__(model)

    def get_all(self, filter: dict, serialize=True) -> List[Summary]:
        entities: List[Summary] = self.model.query.filter_by(email=filter["email"]).all()
        result = []

        for entity in entities:
            if serialize:
                result.append(entity.to_dict())
            else:
                result.append(entity)

        return result

    def save(self, data: dict) -> dict:
        entity = Summary(name=data["name"], id=uuid.uuid4(), email=data["email"])
        db.session.add(entity)
        db.session.commit()
        return entity.to_dict()

    def update(self, data: dict) -> str:
        pass
