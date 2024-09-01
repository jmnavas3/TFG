<<<<<<< HEAD
from flask import Blueprint, current_app
from backend.database.database import Database


api_route = Blueprint('api', __name__)
readiness_route = Blueprint('readiness', __name__)

@api_route.route('', methods=['GET'])
def index():
    return "Hola Mundo!", 200

@readiness_route.route('', methods=['GET'])
def db_check():
    try:
        db = Database(current_app.config['SQLALCHEMY_DATABASE_URI'])
        with Database.session_factory(db=db)() as session:
            if session.is_active:
                return "OK", 200
            return "Active", 200
    except Exception as e:
        print(str(e))
        return "KO", 500
=======
from flask import Blueprint

from app.backend.routes.alerts import alerts_page
from app.backend.routes.firewall import firewall_page
from app.backend.routes.rules import rules_page

api_route = Blueprint('api', __name__)
api_route.register_blueprint(rules_page)
api_route.register_blueprint(alerts_page)
api_route.register_blueprint(firewall_page)


@api_route.route('', methods=['GET'])
def index():
    print("hola mundo!")
    return "Hola Mundo!", 200
>>>>>>> d21db116366befdb866ac9b45065c3c981d67324
