from flask import Blueprint
from app.backend.src.rules.infrastructure.controllers.enable_disable_rule_controller import enable_disable

api_route = Blueprint('api', __name__)
api_route.register_blueprint(enable_disable)


@api_route.route('', methods=['GET'])
def index():
    print("hola mundo!")
    return "Hola Mundo!", 200
