from flask import jsonify
from flask.views import MethodView
from injector import inject

from app.backend.src.base.application.dto.pagination import OrderPagination
from app.backend.src.firewall.application.query.get_blacklist_query import GetBlacklistQuery
from app.backend.src.base.infrastructure.requests.validate_request_with_factory import validate_request_with_factory


class GetBlacklistController(MethodView):
    @inject
    def __init__(self, query: GetBlacklistQuery):
        self.query = query

    @validate_request_with_factory(OrderPagination, 'request', method='POST')
    def post(self, request, **kwargs):
        try:
            blacklist = self.query.execute(request)
            if not blacklist:
                return jsonify({'Error': 'Router not connected'}), 400
            return jsonify(blacklist), 200
        except Exception as e:
            print(str(e))
            return "no se han podido obtener los datos", 500
