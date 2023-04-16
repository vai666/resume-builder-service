# pylint: disable=missing-docstring

from injector import Binder, Module, singleton
from services.resume_service import ResumeService
from models.resume import Resume

class AppModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ResumeService, to=ResumeService(Resume()), scope=singleton)
