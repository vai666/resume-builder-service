# pylint: disable=missing-docstring
import os
from dotenv import load_dotenv


load_dotenv()

class Development:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG: bool = True
    FIREBASE_API_KEY: str = os.environ.get("DEV_FIREBASE_API_KEY")
    FIREBASE_AUTH_DOMAIN: str = os.environ.get("DEV_FIREBASE_AUTH_DOMAIN")
    FIREBASE_PROJECT_ID: str = os.environ.get("DEV_FIREBASE_PROJECT_ID")
    FIREBASE_STORAGE_BUCKET: str = os.environ.get("DEV_FIREBASE_STORAGE_BUCKET")
    FIREBASE_MESSAGING_SENDER_ID: str = os.environ.get("DEV_FIREBASE_MESSAGING_SENDER_ID")
    FIREBASE_APP_ID: str = os.environ.get("DEV_FIREBASE_APP_ID")

class Test:
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("TEST_DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG: bool = True
    SECRET_KEY: str = os.environ.get("TEST_SECRET_KEY")
    FIREBASE_API_KEY: str = os.environ.get("TEST_FIREBASE_API_KEY")
    FIREBASE_AUTH_DOMAIN: str = os.environ.get("TEST_FIREBASE_AUTH_DOMAIN")
    FIREBASE_PROJECT_ID: str = os.environ.get("TEST_FIREBASE_PROJECT_ID")
    FIREBASE_STORAGE_BUCKET: str = os.environ.get("TEST_FIREBASE_STORAGE_BUCKET")
    FIREBASE_MESSAGING_SENDER_ID: str = os.environ.get("TEST_FIREBASE_MESSAGING_SENDER_ID")
    FIREBASE_APP_ID: str = os.environ.get("TEST_FIREBASE_APP_ID")

class Production:
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG: bool = False
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    FIREBASE_API_KEY: str = os.environ.get("FIREBASE_API_KEY")
    FIREBASE_AUTH_DOMAIN: str = os.environ.get("FIREBASE_AUTH_DOMAIN")
    FIREBASE_PROJECT_ID: str = os.environ.get("FIREBASE_PROJECT_ID")
    FIREBASE_STORAGE_BUCKET: str = os.environ.get("FIREBASE_STORAGE_BUCKET")
    FIREBASE_MESSAGING_SENDER_ID: str = os.environ.get("FIREBASE_MESSAGING_SENDER_ID")
    FIREBASE_APP_ID: str = os.environ.get("FIREBASE_APP_ID")
