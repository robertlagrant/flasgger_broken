from flask import Blueprint, request, jsonify
from flasgger import swag_from, validate


b = Blueprint('blue', __name__)


@b.route('/bar', methods=['POST'])
@swag_from(specs='swagger.yaml', validation=True)
def create_foo_auto():

    return jsonify({"message": "it worked!"})


@b.route('/bar_manual', methods=['POST'])
@swag_from(specs='swagger.yaml')
def create_foo():

    validate(request.json, 'Bar', 'swagger.yaml')

    return jsonify({"message": "it worked!"})
