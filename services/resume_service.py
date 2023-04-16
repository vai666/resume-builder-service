# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from typing import List
from services.base_service import BaseService
from models.resume import Resume


class ResumeService(BaseService):
    def __init__(self, model: Resume):
        super().__init__(model)

    def get_all(self, filter: dict) -> List[Resume]:
        pass

    def save(self, data: dict) -> str:
        pass

    def update(self, data: dict) -> str:
        pass
