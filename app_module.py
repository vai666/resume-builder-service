# pylint: disable=missing-docstring

import os
from injector import Binder, Module, singleton
from pyrebase import pyrebase
from initializer import get_config
from services.resume_service import ResumeService
from models.resume import Resume
from services.experience_service import ExperienceService
from models.experience import Experience


class AppModule(Module):
    def create_firebase(self) -> pyrebase.Firebase: 
        env: str = os.environ.get("MODE") or 'development'
        config: object = get_config(env)
        firebase: pyrebase.Firebase = pyrebase.initialize_app({
            "apiKey": config.FIREBASE_API_KEY,
            "authDomain": config.FIREBASE_AUTH_DOMAIN,
            "databaseURL": "",
            "projectId": config.FIREBASE_PROJECT_ID,
            "storageBucket": config.FIREBASE_STORAGE_BUCKET,
            "messagingSenderId": config.FIREBASE_MESSAGING_SENDER_ID,
            "appId": config.FIREBASE_APP_ID
        })
        return firebase

    def configure(self, binder: Binder):
        firebase: pyrebase.Firebase = self.create_firebase()
        auth: pyrebase.Auth = firebase.auth()

        binder.bind(ResumeService, to=ResumeService(Resume()), scope=singleton)
        binder.bind(ExperienceService, to=ExperienceService(Experience()), scope=singleton)
        binder.bind(pyrebase.Auth, to=auth)
