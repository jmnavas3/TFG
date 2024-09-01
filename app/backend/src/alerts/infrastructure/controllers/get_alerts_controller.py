from flask import jsonify
from flask.views import MethodView
from injector import inject

from app.backend.src.base.application.dto.pagination import OrderPagination
from app.backend.src.alerts.application.query.get_alerts_query import GetAlertsQuery
from app.backend.src.base.infrastructure.requests.validate_request_with_factory import validate_request_with_factory


class GetAlertsController(MethodView):
    @inject
    def __init__(self, query: GetAlertsQuery):
        self.query = query

    @validate_request_with_factory(OrderPagination, 'request', method='POST')
    def post(self, request, **kwargs):
        try:
            alert_list = self.query.execute(request)
            return jsonify(alert_list), 200
        except Exception as e:
            print(str(e))
            return "no se han podido obtener los datos", 500
