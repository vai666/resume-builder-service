""" import os to get environ from .env """
import os

class Development:
    """ Configuration for dev environment """
    DB_URI: str = os.environ.get("DEV_DB_URI")
    FIREBASE_API_KEY: str = os.environ.get("DEV_FIREBASE_API_KEY")
    FIREBASE_AUTH_DOMAIN: str = os.environ.get("DEV_FIREBASE_AUTH_DOMAIN")
    FIREBASE_PROJECT_ID: str = os.environ.get("DEV_FIREBASE_PROJECT_ID")
    FIREBASE_STORAGE_BUCKET: str = os.environ.get("DEV_FIREBASE_STORAGE_BUCKET")
    FIREBASE_MESSAGING_SENDER_ID: str = os.environ.get("DEV_FIREBASE_MESSAGING_SENDER_ID")
    FIREBASE_APP_ID: str = os.environ.get("DEV_FIREBASE_APP_ID")

class Test:
    """ Configuration for test environment """
    DB_URI: str = os.environ.get("TEST_DB_URI")
    DEBUG: bool = True
    SECRET_KEY: str = os.environ.get("TEST_SECRET_KEY")
    FIREBASE_API_KEY: str = os.environ.get("TEST_FIREBASE_API_KEY")
    FIREBASE_AUTH_DOMAIN: str = os.environ.get("TEST_FIREBASE_AUTH_DOMAIN")
    FIREBASE_PROJECT_ID: str = os.environ.get("TEST_FIREBASE_PROJECT_ID")
    FIREBASE_STORAGE_BUCKET: str = os.environ.get("TEST_FIREBASE_STORAGE_BUCKET")
    FIREBASE_MESSAGING_SENDER_ID: str = os.environ.get("TEST_FIREBASE_MESSAGING_SENDER_ID")
    FIREBASE_APP_ID: str = os.environ.get("TEST_FIREBASE_APP_ID")

class Production:
    """ Configuration for production environment """
    DB_URI: str = os.environ.get("DB_URI")
    DEBUG: bool = False
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    FIREBASE_API_KEY: str = os.environ.get("FIREBASE_API_KEY")
    FIREBASE_AUTH_DOMAIN: str = os.environ.get("FIREBASE_AUTH_DOMAIN")
    FIREBASE_PROJECT_ID: str = os.environ.get("FIREBASE_PROJECT_ID")
    FIREBASE_STORAGE_BUCKET: str = os.environ.get("FIREBASE_STORAGE_BUCKET")
    FIREBASE_MESSAGING_SENDER_ID: str = os.environ.get("FIREBASE_MESSAGING_SENDER_ID")
    FIREBASE_APP_ID: str = os.environ.get("FIREBASE_APP_ID")
