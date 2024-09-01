from flask import jsonify
from flask.views import MethodView
from injector import inject

from app.backend.src.rules.application.query.get_rules_query import GetRulesQuery
from app.backend.src.base.infrastructure.requests.validate_request_with_factory import validate_request_with_factory
from app.backend.src.rules.infrastructure.controllers.requests.get_rules_request import GetRulesRequest


class GetRulesController(MethodView):
    @inject
    def __init__(self, query: GetRulesQuery):
        self.query = query

    @validate_request_with_factory(GetRulesRequest, 'request', method='POST')
    def post(self, request, **kwargs):
        try:
            rule_list = self.query.execute(request)
            return jsonify(rule_list), 200
        except Exception as e:
            print(str(e))
            return "no se han podido obtener los datos", 500
