from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from ..models.db import db
import os

## import resources
from ..resources.user import UserTeams, UserTeamsById, UserById, UserPlayers
from ..resources.auth import Login, Register, Session, UpdatePassword
from ..resources.team import Teams, TeamDetails, TeamAPI
from ..resources.player import Players, PlayerDetails, PlayerAPI
from ..models.user import User
from ..models.team import Team
from ..models.player import Player
from ..models.user_team import user_teams
from ..models.user_player import user_players


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
DATABASE_URL = os.getenv('DATABASE_URL')
os.getenv('APP_SECRET')

if DATABASE_URL:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_ECHO'] = False
    app.env = 'production'
else:
    app.debug = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/sports_vue_db"
    app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return 'Api up!'

# Resources //
api.add_resource(Login, '/api/auth/login')
api.add_resource(Register, '/api/auth/register')
api.add_resource(Session, '/api/auth/session')
api.add_resource(UpdatePassword, '/api/auth/user/<int:user_id>')
api.add_resource(UserTeams, '/api/user/teams')
api.add_resource(UserPlayers, '/api/user/players')
api.add_resource(UserById, '/api/user/<int:user_id>')
api.add_resource(UserTeamsById, '/api/user/teams/<int:user_id>')
api.add_resource(Teams, '/api/teams')
api.add_resource(TeamDetails, '/api/teams/<int:team_id>')
api.add_resource(TeamAPI, '/api/teamapi/<string:api_id>')
api.add_resource(Players, '/api/players')
api.add_resource(PlayerDetails, '/api/players/<int:player_id>')
api.add_resource(PlayerAPI, '/api/playerapi/<string:api_id>')


if __name__ == '__main__':
    app.run()
