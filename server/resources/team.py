from ..models.db import db
from ..models.team import Team
from flask_restful import Resource
from flask import request


class Teams(Resource):
    def get(self):
        teams = Team.find_all()
        results = [t.json() for t in teams]
        return results

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        team = Team(**params)
        team.create()

        return team.json(), 201


class TeamDetails(Resource):
    def get(self, team_id):
        team = Team.find_by_id(team_id)
        return team.json()

    def delete(self, team_id):
        team = Team.find_by_id(team_id)
        if not team:
            return {"msg": "Team not found"}, 404
        db.session.delete(team)
        db.session.commit()
        return {"msg": "Team Deleted", "payload": team.json()}

    def put(self, team_id):
        data = request.get_json()
        team = Team.find_by_id(team_id)
        for key in data:
            setattr(team, key, data[key])
        db.session.commit()
        return team.json()


class TeamAPI(Resource):
    def get(self, api_id):
        team = Team.find_by_api_id(api_id)
        if team:
            return team.json()
        else:
            return team
