# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from flask import Blueprint, request
from injector import inject
from pyrebase import pyrebase

auth_blueprint = Blueprint('Auth', __name__)

@inject
@auth_blueprint.route('/api/auth/signup', methods=["POST"])
def signup(auth: pyrebase.Auth):
    data = request.json
    email = data["email"]
    password = data["password"]
    auth = auth.create_user_with_email_and_password(email, password)
    return auth["idToken"]

@inject
@auth_blueprint.route('/api/auth/signin', methods=["POST"])
def signin(auth: pyrebase.Auth):
    data = request.json
    email = data["email"]
    password = data["password"]
    auth = auth.sign_in_with_email_and_password(email, password)
    return auth["idToken"]
