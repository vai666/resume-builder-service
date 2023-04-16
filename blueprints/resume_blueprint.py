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
def get(id: str, service: ResumeService, auth: pyrebase.Auth):
    entity = service.get(id)
    return jsonify(entity)

@requires_auth
@inject
@resume_blueprint.route('/api/', methods=["GET"])
def get_all(service: ResumeService, auth: pyrebase.Auth):
    args = request.args
    entities = service.get_all(args)
    return jsonify(entities)

@requires_auth
@inject
@resume_blueprint.route('/api/', methods=["POST"])
def save(service: ResumeService, auth: pyrebase.Auth):
    data = request.json
    id = service.save(data)
    return jsonify(id)
