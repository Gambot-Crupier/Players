from typing import List
from flask import Blueprint
from flask import jsonify
from flask import request
from project import db
from project.api.models import User
from project.api.schemas.user import validate_edit_json
import sys

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/edit-user', methods=['PUT'])
def edit_user():
    request_data = validate_edit_json(request.get_json())

    if not request_data['success']:
        return jsonify({
            'message': 'Invalid Data'
        }), 400
    
    user_data = User.query.filter_by(email = json_data['email']).first()

    if user_data is not None:
        user_data.name = json_data['name']
        user_data.username = json_data['username']
        user_data.email = json_data['email']
        user_data.password = json_data['password']

        db.session.commit()

        return jsonify({
            'message': 'User data updated sucessfully'
        }), 200
    else:
        return jsonify({
            'message': 'User not registered on database'
        })


@user_blueprint.route('/get_user_by_id', methods=['GET'])
def get_user():
    try:
        user_id = request.args.get('user_id')
        user = User.query.filter_by(id=user_id).first()

        response = {
            "name": user.name,
        }

        return jsonify(response), 200
        
    except:
        return jsonify({"message": "Error retriving players"}), 500


