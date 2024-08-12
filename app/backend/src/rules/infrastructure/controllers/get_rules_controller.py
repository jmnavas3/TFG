from flask import Blueprint
from flask.views import MethodView
from injector import inject

from app.backend.src.rules.application.query.get_rules_query import GetRulesQuery
from app.backend.src.base.infrastructure.requests.validate_request_with_factory import validate_request_with_factory
from app.backend.src.rules.infrastructure.controllers.requests.get_rules_request import GetRulesRequest

get_rules = Blueprint('get_rules', __name__, url_prefix='/rules/get_rules')


class GetRulesController(MethodView):
    @inject
    def __init__(self, query: GetRulesQuery):
        self._query = query

    @validate_request_with_factory(GetRulesRequest, 'request', method='GET')
    def get(self, request, **kwargs):
        try:
            rule_list = self._query.execute(request.page)
            return rule_list, 200
        except Exception as e:
            print(str(e))
            return "no se han podido obtener los datos", 500


get_rules.add_url_rule(rule="/<page>", view_func=GetRulesController.as_view('get_rules'))
