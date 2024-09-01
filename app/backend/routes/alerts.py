from flask import Blueprint

from app.backend.src.alerts.infrastructure.controllers.get_alerts_controller import GetAlertsController

alerts_page = Blueprint('alerts', __name__, url_prefix='alerts')

alerts_page.add_url_rule(rule='/list', view_func=GetAlertsController.as_view('list_alerts'))
