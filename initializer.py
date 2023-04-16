# pylint: disable=missing-docstring

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from pyrebase import pyrebase
from config import Development, Test, Production

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()


def create_app(env: str) -> Flask:
    app: Flask = Flask(__name__)
    app_config: object = get_config(env)
    app.config.from_object(app_config)
    db.init_app(app)
    migrate.init_app(app, db)

    return app

def get_config(env: str) -> object:
    app_config: object = None

    if env == "development":
        app_config = Development
    elif env == "test":
        app_config = Test
    elif env == "production":
        app_config = Production
    else:
        raise ValueError(f"There is no env type for {env}")

    return app_config
