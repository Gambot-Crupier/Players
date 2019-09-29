from typing import List
from flask import Blueprint
from flask import jsonify
from flask import request
from project import db
from project.api.models import User
auth_blueprint = Blueprint('auth_blueprint', __name__)


"""
Nickname, email, password, password confirmation
"""
@auth_blueprint.route('/sign-up', methods=['POST'])
def sign_up_gateway():
    request_data = request.get_json()
    user_data = User(name = request_data[0]['name'], email = request_data[0]['email'], 
                     username = request_data[0]['username'], password = request_data[0]['password'])

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
        