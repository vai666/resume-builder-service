# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

import uuid
from initializer import db


class AuthService():
    def __init__(self):
        pass

    def get_all(self, filter: dict) -> List[Resume]:
        pass

    def save(self, data: dict) -> dict:
        entity = Resume(name=data["name"], id=uuid.uuid4())
        db.session.add(entity)
        db.session.commit()
        return entity.to_dict()

    def update(self, data: dict) -> str:
        pass
