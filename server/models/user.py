from ..models.db import db
from datetime import datetime
from ..models.user_team import user_teams
from ..models.user_player import user_players


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_digest = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)
    user_teams = db.relationship('Team', secondary=user_teams, lazy='subquery',
                                 backref=db.backref('teams', lazy=True))
    user_players = db.relationship('Player', secondary=user_players, lazy='subquery',
                                   backref=db.backref('players', lazy=True))

    def __init__(self, name, email, password_digest):
        self.name = name
        self.email = email
        self.password_digest = password_digest

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password_digest": self.password_digest,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self.json()

    def create_user_team(self, team_id):
        self.user_teams.append({"user_id": self.id, "team_id": team_id})
        db.session.commit()
        return self.json()

    @classmethod
    def find_by_id(cls, user_id):
        return User.query.filter_by(id=user_id).first()

    @classmethod
    def find_one(cls, email):
        user = User.query.filter_by(email=email).first()
        return user
