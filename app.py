from http import HTTPStatus
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! UNIPARKING"


types = [{'id': 1, 'nome': 'Funcionário'}, {'id': 2, 'nome': 'Professor'}]


@app.route("/types")
def list_types():
    return jsonify(types)


@app.route('/types/<int:type_id>')
def get_type(type_id):
    for current in types:
        if current['id'] == type_id:
            return jsonify(current)
    return '', HTTPStatus.NOT_FOUND


@app.route("/types", methods=['POST'])
def create_type():
    new_type = request.get_json()
    new_type['id'] = len(types) + 1
    types.append(new_type)
    return jsonify(new_type), HTTPStatus.CREATED


@app.route("/types/<int:type_id>", methods=['PUT'])
def update_type(type_id):
    for i, current in enumerate(types):
        if current['id'] == type_id:
            updated_type = request.get_json()
            updated_type['id'] = type_id
            types[i] = updated_type
            return '', HTTPStatus.NO_CONTENT
    return '', HTTPStatus.NOT_FOUND


@app.route("/types/<int:type_id>", methods=['DELETE'])
def delete_type(type_id):
    for current in types:
        if current['id'] == type_id:
            types.remove(current)
            return "", HTTPStatus.NO_CONTENT
    return "", HTTPStatus.NOT_FOUND
