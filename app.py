# pylint: disable=missing-docstring

import os
from flask import Flask, jsonify, Response
from flask_injector import FlaskInjector
from initializer import create_app
from app_module import AppModule


env: str = os.environ.get("MODE") or 'development'
app: Flask = create_app(env)

from blueprints.auth_blueprint import auth_blueprint
from blueprints.resume_blueprint import resume_blueprint
from blueprints.experience_blueprint import experience_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(resume_blueprint)
app.register_blueprint(experience_blueprint)

@app.errorhandler(404)
def not_found(error) -> Response:
    return jsonify({ "status": 404, "error": str(error), "context": "API not found"})

@app.errorhandler(500)
def internal_server_error(error) -> Response:
    return jsonify({ "status": 500, "error": str(error), "context": "Something's wrong in backend :("})

FlaskInjector(app=app, modules=[AppModule])

if __name__ == "__main__":
    app.run()
