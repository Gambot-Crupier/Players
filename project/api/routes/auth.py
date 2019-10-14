from typing import List
from flask import Blueprint
from flask import jsonify
from flask import request
from project import db
from project.api.models import User
from project.api.schemas.auth import validate_signup_json, validate_login_json
auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/sign-up', methods=['POST'])
def sign_up():
    validate_data = request.get_json()
    request_data = validate_signup_json(validate_data['user'])

    if not request_data['success']:
        return jsonify({
            'message': 'Dados inválidos',
        }), 400

    json_data = request_data['user']
    user_data = User(name = json_data['name'], email = json_data['email'], 
                     username = json_data['username'], password = json_data['password'])

    if user_data is not None:
        db.session.add(user_data)
        db.session.commit()

        return jsonify({
            'message': 'Usuário criado com sucesso!'
        }), 200
    else:
        return jsonify({
            'message': 'Um erro ocorreu, tente novamente!'
        }), 400

@auth_blueprint.route('/sign-in', methods=['POST'])
def sign_in():
    validate_data = request.get_json()
    request_data = validate_login_json(validate_data['user'])

    if not request_data['success']:
        return jsonify({
            'message': 'Dados inválidos'
        }), 400
    
    json_data = request_data['user']
    user_data = User.query.filter_by(email = json_data['email']).first()

    if user_data is not None:
        if user_data.password == json_data['password']:
            return jsonify({
                'message': 'Login feito com sucesso.'
            }), 200
        else:
            return jsonify({
                'message': 'Senhas incompatíveis.'
            }), 400
    else:
        return jsonify({
            'message': 'Usuário não registrado no sistema.'
        }), 400