# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from flask import Blueprint, jsonify, request, Response
from injector import inject
from pyrebase import pyrebase
from services.experience_service import ExperienceService
from decorator import authenticate


experience_blueprint = Blueprint('Experience', __name__)

@inject
@experience_blueprint.route('/api/experience/<id>', methods=["GET"])
@authenticate
def get(id: str, service: ExperienceService, auth: pyrebase.Auth, user: dict) -> Response:
    entity = service.get(id, user["email"])
    return jsonify({"status": 200, "data": entity})

@inject
@experience_blueprint.route('/api/experience/<id>/resume', methods=["GET"])
@authenticate
def get_by_resume(id: str, service: ExperienceService, auth: pyrebase.Auth, user: dict) -> Response:
    entity = service.get_by_resume(id, user["email"])
    return jsonify({"status": 200, "data": entity})

@inject
@experience_blueprint.route('/api/experience', methods=["GET"])
@authenticate
def get_all(service: ExperienceService, auth: pyrebase.Auth, user: dict) -> Response:
    args = dict(request.args)
    args["email"] = user["email"]
    entities = service.get_all(args)
    return jsonify({"status": 200, "data": entities})

@inject
@experience_blueprint.route('/api/experience', methods=["POST"])
@authenticate
def save(service: ExperienceService, auth: pyrebase.Auth, user: dict) -> Response:
    data = request.json
    data["email"] = user["email"]
    entity = service.save(data)
    return jsonify({"status": 200, "data": entity})


@inject
@experience_blueprint.route('/api/experience/<id>', methods=["DELETE"])
@authenticate
def delete(id: str, service: ExperienceService, auth: pyrebase.Auth, user: dict) -> Response:
    deleted_id: str = service.delete(id, user["email"])
    return jsonify({"status": 200, "data": deleted_id})
