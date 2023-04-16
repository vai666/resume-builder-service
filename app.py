# pylint: disable=missing-docstring
import os
from flask import Flask
from initializer import create_app

env: str = os.environ.get("MODE") or 'development'

app: Flask = create_app(env)


if __name__ == "__main__":
    app.run()
