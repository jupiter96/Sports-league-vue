from ..models.db import db

user_players = db.Table('user_players',
                        db.Column('user_id', db.Integer, db.ForeignKey(
                            'users.id'), primary_key=True),
                        db.Column('players_id', db.Integer, db.ForeignKey(
                            'players.id'), primary_key=True)
                        )
