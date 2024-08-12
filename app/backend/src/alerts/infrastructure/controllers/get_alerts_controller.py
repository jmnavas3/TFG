from flask import Blueprint
from flask.views import MethodView
from injector import inject

from app.backend.src.base.application.dto.pagination import OrderPagination
from app.backend.src.alerts.application.query.get_alerts_query import GetAlertsQuery
from app.backend.src.base.infrastructure.requests.validate_request_with_factory import validate_request_with_factory

get_alerts = Blueprint('get_alerts', __name__, url_prefix='/alerts/get_alerts')


class GetAlertsController(MethodView):
    @inject
    def __init__(self, query: GetAlertsQuery):
        self._query = query

    @validate_request_with_factory(OrderPagination, 'request', method='POST')
    def post(self, request, **kwargs):
        try:
            alert_list = self._query.execute(request)
            return alert_list, 200
        except Exception as e:
            print(str(e))
            return "no se han podido obtener los datos", 500


get_alerts.add_url_rule(rule="", view_func=GetAlertsController.as_view('get_alerts'))
