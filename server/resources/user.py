from ..models.db import db
from ..models.user import User
from ..models.team import Team
from ..models.player import Player
from ..models.user_team import user_teams
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import mapper
from sqlalchemy.orm import joinedload


class UserById(Resource):
    def get(self, user_id):
        user = User.query.options(joinedload(
            User.user_teams)).filter_by(id=user_id).first()
        teams = [t.json() for t in user.user_teams]
        players = [p.json() for p in user.user_players]
        return {
            **user.json(),
            "teams": teams,
            "players": players
        }

    def put(self, user_id):
        data = request.get_json()
        user = User.find_by_id(user_id)
        for key in data:
            setattr(user, key, data[key])
        db.session.commit()
        return user.json()

    def delete(self, user_id):
        user = User.find_by_id(user_id)
        if not user:
            return {"msg": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"msg": "User Deleted", "payload": user.json()}


class UserTeamsById(Resource):

    def get(self, user_id):
        user = User.find_by_id(user_id)
        teams = user.user_teams
        results = [t.json() for t in teams]
        return results


class UserPlayerById(Resource):

    def get(self, user_id):
        user = User.find_by_id(user_id)
        players = user.user_teams
        results = [p.json() for p in players]
        return results


class UserTeams(Resource):

    def post(self):
        data = request.get_json()
        user = User.find_by_id(data["user_id"])
        team = Team.find_by_id(data["team_id"])
        user.user_teams.append(team)
        db.session.commit()
        return {"user": user.json()["email"], "payload": team.json()}, 201

    def delete(self):
        data = request.get_json()
        user = User.find_by_id(data["user_id"])
        team = Team.find_by_id(data["team_id"])
        user.user_teams.remove(team)
        db.session.commit()
        return data, 201


class UserPlayers(Resource):

    def post(self):
        data = request.get_json()
        user = User.find_by_id(data["user_id"])
        player = Player.find_by_id(data["player_id"])
        user.user_players.append(player)
        db.session.commit()
        return {"user": user.json()["email"], "payload": player.json()}, 201

    def delete(self):
        data = request.get_json()
        user = User.find_by_id(data["user_id"])
        player = Player.find_by_id(data["player_id"])
        user.user_players.remove(player)
        db.session.commit()
        return data, 201
