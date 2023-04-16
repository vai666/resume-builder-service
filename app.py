# pylint: disable=missing-docstring
import os
from flask_injector import FlaskInjector
from flask import Flask
from initializer import create_app, AppModule

env: str = os.environ.get("MODE") or 'development'

app: Flask = create_app(env)

FlaskInjector(app=app, modules=[AppModule()])

if __name__ == "__main__":
    app.run()
