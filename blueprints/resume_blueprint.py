# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from flask import Blueprint, jsonify, request
from injector import inject
from pyrebase import pyrebase
from services.resume_service import ResumeService
from decorator import requires_auth


resume_blueprint = Blueprint('Resume', __name__)

@requires_auth
@inject
@resume_blueprint.route('/api/<id>', methods=["GET"])
def get(id: str, service: ResumeService, auth: pyrebase.Auth, email: str):
    entity = service.get(id, email)
    return jsonify(entity)


@inject
@requires_auth
@resume_blueprint.route('/api/', methods=["GET"])
def get_all(service: ResumeService, auth: pyrebase.Auth, email: str):
    args = dict(request.args)
    args["email"] = email
    entities = service.get_all(args)
    return jsonify(entities)

@requires_auth
@inject
@resume_blueprint.route('/api/', methods=["POST"])
def save(service: ResumeService, auth: pyrebase.Auth, email: str):
    data = request.json
    data["email"] = email
    entity = service.save(data)
    return jsonify(entity)
