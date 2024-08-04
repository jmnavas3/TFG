from flask import Blueprint, current_app
from backend.database.database import Database


api_route = Blueprint('api', __name__)
readiness_route = Blueprint('readiness', __name__)

@api_route.route('', methods=['GET'])
def index():
    print("hola mundo!")
    return "Hola Mundo!", 200

@readiness_route.route('', methods=['GET'])
def db_check():
    try:
        db = Database(current_app.config['SQLALCHEMY_DATABASE_URI'])
        with Database.session_factory(db=db)() as session:
            if session.is_active:
                print("sesion activa")
                return "OK", 200
            return "Active", 200
    except Exception as e:
        print(str(e))
        return "KO", 500
