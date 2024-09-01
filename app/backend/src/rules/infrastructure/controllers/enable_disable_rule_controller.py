from flask import jsonify
from flask.views import MethodView
from injector import inject

from app.backend.src.rules.application.command.enable_disable_rule_handler import EnableDisableRuleHandler
from app.backend.src.rules.application.command.enable_disable_rule_command import EnableDisableRuleCommand
from app.backend.src.base.infrastructure.requests.validate_request_with_factory import validate_request_with_factory


class EnableDisableRuleController(MethodView):
    @inject
    def __init__(self, handler: EnableDisableRuleHandler):
        self._handler = handler

    @validate_request_with_factory(EnableDisableRuleCommand, 'command', method='POST')
    def post(self, command, **kwargs):
        try:
            response = self._handler.execute(command)
            return jsonify(response), 200
        except Exception as e:
            print(str(e))
            return str(e), 500
