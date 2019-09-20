from typing import List
from flask import Blueprint
from flask import jsonify
from flask import request
from project import db
import requests

auth_blueprint = Blueprint('auth_blueprint', __name__)


"""
Nickname, email, password, password confirmation
"""
@auth_blueprint.route('/sign-up', methods=['POST'])
def sign_up_gateway():
    user_data = request.get_json()
    print(user_data)

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
        