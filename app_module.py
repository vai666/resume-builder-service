# pylint: disable=missing-docstring

import os
from injector import Binder, Module, singleton
from pyrebase import pyrebase
from initializer import get_config
from services.resume_service import Resume, ResumeService
from services.experience_service import Experience, ExperienceService
from services.header_service import Header, HeaderService
from services.summary_service import Summary, SummaryService
from services.expertise_service import Expertise, ExpertiseService
from services.education_service import Education, EducationService
from services.achievement_service import Achievement, AchievementService



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
        binder.bind(HeaderService, to=HeaderService(Header()), scope=singleton)
        binder.bind(SummaryService, to=SummaryService(Summary()), scope=singleton)
        binder.bind(ExpertiseService, to=ExpertiseService(Expertise()), scope=singleton)
        binder.bind(EducationService, to=EducationService(Education()), scope=singleton)
        binder.bind(AchievementService, to=AchievementService(Achievement()), scope=singleton)
        binder.bind(pyrebase.Auth, to=auth)
