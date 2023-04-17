# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from flask import Blueprint, jsonify, request, Response
from injector import inject
from pyrebase import pyrebase
from services.resume_service import ResumeService
from decorator import authenticate


resume_blueprint = Blueprint('Resume', __name__)

@inject
@resume_blueprint.route('/api/<id>', methods=["GET"])
@authenticate
def get(id: str, service: ResumeService, auth: pyrebase.Auth, user: dict) -> Response:
    entity = service.get(id, user["email"])
    return jsonify({"status": 200, "data": entity})

@inject
@resume_blueprint.route('/api/', methods=["GET"])
@authenticate
def get_all(service: ResumeService, auth: pyrebase.Auth, user: str) -> Response:
    args = dict(request.args)
    args["email"] = user["email"]
    entities = service.get_all(args)
    return jsonify({"status": 200, "data": entities})

@inject
@resume_blueprint.route('/api/', methods=["POST"])
@authenticate
def save(service: ResumeService, auth: pyrebase.Auth, user: str) -> Response:
    data = request.json
    data["email"] = user["email"]
    entity = service.save(data)
    return jsonify({"status": 200, "data": entity})


@inject
@resume_blueprint.route('/api/<id>', methods=["DELETE"])
@authenticate
def delete(id: str, service: ResumeService, auth: pyrebase.Auth, user: str) -> Response:
    deleted_id: str = service.delete(id, user["email"])
    return jsonify({"status": 200, "data": deleted_id})
