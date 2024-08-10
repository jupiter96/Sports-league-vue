from ..models.db import db
from ..models.player import Player
from flask_restful import Resource
from flask import request


class Players(Resource):
    def get(self):
        players = Player.find_all()
        results = [p.json() for p in players]
        return results

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        players = Player(**params)
        players.create()
        return players.json(), 201


class PlayerDetails(Resource):
    def get(self, player_id):
        player = Player.find_by_id(player_id)
        return player.json()

    def delete(self, player_id):
        player = Player.find_by_id(player_id)
        if not player:
            return {"msg": "Player not found"}, 404
        db.session.delete(player)
        db.session.commit()
        return {"msg": "Player Deleted", "payload": player.json()}

    def put(self, player_id):
        data = request.get_json()
        player = Player.find_by_id(player_id)
        for key in data:
            setattr(player, key, data[key])
        db.session.commit()
        return player.json()


class PlayerAPI(Resource):
    def get(self, api_id):
        player = Player.find_by_api_id(api_id)
        if player:
            return player.json()
        else:
            return player
