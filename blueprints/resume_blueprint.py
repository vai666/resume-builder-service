# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from flask import Blueprint, jsonify, request, Response
from injector import inject
from pyrebase import pyrebase
from services.resume_service import ResumeService
from decorator import requires_auth


resume_blueprint = Blueprint('Resume', __name__)

@inject
@resume_blueprint.route('/api/<id>', methods=["GET"])
@requires_auth
def get(id: str, service: ResumeService, auth: pyrebase.Auth, email: str) -> Response:
    entity = service.get(id, email)
    return jsonify({"status": 200, "data": entity})

@inject
@resume_blueprint.route('/api/', methods=["GET"])
@requires_auth
def get_all(service: ResumeService, auth: pyrebase.Auth, email: str) -> Response:
    args = dict(request.args)
    args["email"] = email
    entities = service.get_all(args)
    return jsonify({"status": 200, "data": entities})

@inject
@resume_blueprint.route('/api/', methods=["POST"])
@requires_auth
def save(service: ResumeService, auth: pyrebase.Auth, email: str) -> Response:
    data = request.json
    data["email"] = email
    entity = service.save(data)
    return jsonify({"status": 200, "data": entity})


@inject
@resume_blueprint.route('/api/<id>', methods=["DELETE"])
@requires_auth
def delete(id: str, service: ResumeService, auth: pyrebase.Auth, email: str) -> Response:
    deleted_id: str = service.delete(id, email)
    return jsonify({"status": 200, "data": deleted_id})
