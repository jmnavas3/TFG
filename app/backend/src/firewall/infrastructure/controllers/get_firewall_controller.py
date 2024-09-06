from flask import jsonify
from flask.views import MethodView
from injector import inject

from app.backend.src.base.application.dto.pagination import OrderPagination
from app.backend.src.firewall.application.query.get_firewall_query import GetFirewallQuery
from app.backend.src.base.infrastructure.requests.validate_request_with_factory import validate_request_with_factory


class GetFirewallController(MethodView):
    @inject
    def __init__(self, query: GetFirewallQuery):
        self.query = query

    @validate_request_with_factory(OrderPagination, 'request', method='POST')
    def post(self, request, **kwargs):
        try:
            rule_list = self.query.execute(request)
            if not rule_list:
                return jsonify({'Error': 'Router not connected'}), 400
            return jsonify(rule_list), 200
        except Exception as e:
            print(str(e))
            return "no se han podido obtener los datos", 500
