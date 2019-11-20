from typing import List
from flask import Blueprint
from flask import jsonify
from flask import request
from project import db
from project.api.models import User
from project.api.schemas.user import validate_edit_json
import sys
from project.api.models import UserCommunication

comunication_blueprint = Blueprint('comunication_blueprint', __name__)

@comunication_blueprint.route('/post_player_id', methods=['POST'])
def post_player_id():
    try:
        player_id = request.args.get('player_id')
        data = UserCommunication(player_id=player_id)
        db.session.add(data)
        db.session.commit()

        return jsonify({'message': 'Id postado com sucesso.'}), 200
        
    except Exception as e:
        return jsonify({'message': 'Erro ao tentar reconhecer jogador.', 'error': e}), 500



@comunication_blueprint.route('/post_ignore_player', methods=['POST'])
def post_ignore_player():
    try:
        data = UserCommunication(player_id=None)
        db.session.add(data)
        db.session.commit()

        return jsonify({'message': 'Id postado com sucesso.'}), 200
        
    except Exception as e:
        return jsonify({'message': 'Erro ao tentar ignorar jogador.', 'error': e}), 500



@comunication_blueprint.route('/post_end_recognition', methods=['POST'])
def post_end_recognition():
    try:
        data = UserCommunication(player_id=-1)
        db.session.add(data)
        db.session.commit()

        return jsonify({'message': 'Id postado com sucesso.'}), 200
        
    except Exception as e:
        return jsonify({'message': 'Erro ao tentar finalzar o reconhecimento.', 'error': e}), 500



@comunication_blueprint.route('/get_player_id', methods=['GET'])
def get_player_id():
    try:
        player_data = UserCommunication.query.all()

        return jsonify({'player_id': str(player_data[-1].player_id)}), 200

    except Exception as e:
        return jsonify({'message': 'Erro ao tentar recuperar Id de jogador.', 'error': e}), 500
