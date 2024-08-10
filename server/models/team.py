from datetime import datetime
from ..models.db import db


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255))
    api_id = db.Column(db.String(80))
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           nullable=False, onupdate=datetime.now())

    def __init__(self, name, image, api_id):
        self.name = name
        self.image = image
        self.api_id = api_id

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "api_id": self.api_id,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Team.query.all()

    @classmethod
    def find_by_id(cls, id):
        return Team.query.filter_by(id=id).first()

    @classmethod
    def find_by_api_id(cls, api_id):
        return Team.query.filter_by(api_id=api_id).first()
