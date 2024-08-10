from ..models.db import db

user_teams = db.Table('user_teams',
                      db.Column('user_id', db.Integer, db.ForeignKey(
                          'users.id'), primary_key=True),
                      db.Column('team_id', db.Integer, db.ForeignKey(
                          'teams.id'), primary_key=True)
                      )
