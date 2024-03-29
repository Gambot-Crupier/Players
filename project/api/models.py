from sqlalchemy.dialects.mysql import TIME
from sqlalchemy.sql import func
from project import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    username = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    deviceId = db.Column(db.String(255), nullable = False)
    money = db.Column(db.Float)


class UserCommunication(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    player_id = db.Column(db.Integer)

    def __init__(self, player_id):
        self.player_id = player_id