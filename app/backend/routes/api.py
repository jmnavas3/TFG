from flask import Blueprint

from app.backend.src.alerts.infrastructure.controllers.get_alerts_controller import get_alerts
from app.backend.src.rules.infrastructure.controllers.enable_disable_rule_controller import enable_disable
from app.backend.src.rules.infrastructure.controllers.get_rules_controller import get_rules

api_route = Blueprint('api', __name__)
api_route.register_blueprint(enable_disable)
api_route.register_blueprint(get_rules)
api_route.register_blueprint(get_alerts)


@api_route.route('', methods=['GET'])
def index():
    print("hola mundo!")
    return "Hola Mundo!", 200
