# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from flask import Blueprint, jsonify, request, Response
from injector import inject
from pyrebase import pyrebase
from services.experience_service import ExperienceService
from decorator import requires_auth


experience_blueprint = Blueprint('Experience', __name__)

@inject
@experience_blueprint.route('/api/experience/<id>', methods=["GET"])
@requires_auth
def get(id: str, service: ExperienceService, auth: pyrebase.Auth, email: str) -> Response:
    entity = service.get(id, email)
    return jsonify({"status": 200, "data": entity})

@inject
@experience_blueprint.route('/api/experience/<id>/resume', methods=["GET"])
@requires_auth
def get_by_resume(id: str, service: ExperienceService, auth: pyrebase.Auth, email: str) -> Response:
    entity = service.get_by_resume(id, email)
    return jsonify({"status": 200, "data": entity})

@inject
@experience_blueprint.route('/api/experience', methods=["GET"])
@requires_auth
def get_all(service: ExperienceService, auth: pyrebase.Auth, email: str) -> Response:
    args = dict(request.args)
    args["email"] = email
    entities = service.get_all(args)
    return jsonify({"status": 200, "data": entities})

@inject
@experience_blueprint.route('/api/experience', methods=["POST"])
@requires_auth
def save(service: ExperienceService, auth: pyrebase.Auth, email: str) -> Response:
    data = request.json
    data["email"] = email
    entity = service.save(data)
    return jsonify({"status": 200, "data": entity})


@inject
@experience_blueprint.route('/api/experience/<id>', methods=["DELETE"])
@requires_auth
def delete(id: str, service: ExperienceService, auth: pyrebase.Auth, email: str) -> Response:
    deleted_id: str = service.delete(id, email)
    return jsonify({"status": 200, "data": deleted_id})
