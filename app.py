# pylint: disable=missing-docstring

import os
from flask import Flask, request, abort
from flask_injector import FlaskInjector
from initializer import create_app
from app_module import AppModule


env: str = os.environ.get("MODE") or 'development'
app: Flask = create_app(env)

from blueprints.auth_blueprint import auth_blueprint
from blueprints.resume_blueprint import resume_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(resume_blueprint)


if __name__ == "__main__":
    FlaskInjector(app=app, modules=[AppModule])
    app.run()
