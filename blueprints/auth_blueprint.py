# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from flask import Blueprint, request, jsonify, Response
from injector import inject
from pyrebase import pyrebase
from decorator import authenticate

auth_blueprint = Blueprint('Auth', __name__)

@inject
@auth_blueprint.route('/api/auth/signup', methods=["POST"])
def signup(auth: pyrebase.Auth) -> Response:
    data = request.json
    email = data["email"]
    password = data["password"]
    auth = auth.create_user_with_email_and_password(email, password)
    return jsonify({ "status": 200, "data": email })

@inject
@auth_blueprint.route('/api/auth/signin', methods=["POST"])
def signin(auth: pyrebase.Auth) -> Response:
    data = request.json
    email = data["email"]
    password = data["password"]
    auth = auth.sign_in_with_email_and_password(email, password)
    return jsonify({ "status": 200, "data":
            { "idToken": auth["idToken"], "refreshToken": auth["refreshToken"] }
           })

@inject
@auth_blueprint.route('/api/auth/refresh-token', methods=["POST"])
@authenticate
def refresh_token(auth: pyrebase.Auth, user: dict) -> Response:
    data = request.json
    result = auth.refresh(data["refresh_token"])
    return jsonify({ "status": 200, "data": result })
