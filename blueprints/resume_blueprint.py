# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

from flask import Blueprint, jsonify, request
from injector import inject
from services.resume_service import ResumeService


resume_blueprint = Blueprint('', __name__)

@inject
@resume_blueprint.route('/api/<id>', methods=["GET"])
def get(id: str, service: ResumeService):
    entity = service.get(id)
    return jsonify(entity)

@inject
@resume_blueprint.route('/api/', methods=["POST"])
def save(service: ResumeService):
    data = request.json
    id = service.save(data)
    return jsonify(id)
