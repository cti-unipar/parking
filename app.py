from http import HTTPStatus
from flask import Flask, request
from model import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! UNIPARKING"


@app.route("/types", methods=["GET"])
def list_types():
    return Types.objects().to_json()


@app.route("/types/<string:type_id>", methods=['GET'])
def get_type(type_id):
    try:
        type = Types.objects.get(id=type_id)
        return type.to_json()
    except DoesNotExist:
        return '', HTTPStatus.NOT_FOUND


@app.route("/types", methods=['POST'])
def create_type():
    data = request.get_json()
    new_type = Types(**data)
    new_type.save()
    return new_type.to_json(), HTTPStatus.CREATED


@app.route("/types/<string:type_id>", methods=['PUT'])
def update_type(type_id):
    data = request.get_json()
    try:
        type = Types.objects.get(id=type_id)
        type.update(**data)
        return '', HTTPStatus.ACCEPTED
    except DoesNotExist:
        return '', HTTPStatus.NOT_FOUND


@app.route("/types/<string:type_id>", methods=['DELETE'])
def delete_type(type_id):
    try:
        type = Types.objects.get(id=type_id)
        type.delete()
        return "", HTTPStatus.NO_CONTENT
    except DoesNotExist:
        return "", HTTPStatus.NOT_FOUND

