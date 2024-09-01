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
