from project import db


class Player(db.Model):
    __tablename__ = 'player'
    id             = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    name           = db.Column(db.String(128),  nullable=False)


    def __init__(self, name):
        self.name     = name