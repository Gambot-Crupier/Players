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
    request_data = validate_signup_json(request.get_json())

    if not request_data['success']:
        return jsonify({
            'message': 'Invalid Data'
        }), 400

    json_data = request_data['user']
    user_data = User(name = json_data['name'], email = json_data['email'], 
                     username = json_data['username'], password = json_data['password'])

    if user_data is not None:
        db.session.add(user_data)
        db.session.commit()

        return jsonify({
            'message': 'User was created sucessfully'
        }), 200
    else:
        return jsonify({
            'message': 'An error occured, please try again'
        }), 400

@auth_blueprint.route('/sign-in', methods=['POST'])
def sign_in():
    request_data = validate_login_json(request.get_json())

    if not request_data['success']:
        return jsonify({
            'message': 'Invalid Data'
        }), 400
    
    json_data = request_data['user']
    user_data = User.query.filter_by(email = json_data['email']).first()

    if user_data is not None:
        if user_data.password == json_data['password']:
            return jsonify({
                'message': 'Login was made successfully'
            }), 200
        else:
            return jsonify({
                'message': 'Passwords do not match'
            }), 400
    else:
        return jsonify({
            'message': 'User not registered on database'
        }), 400