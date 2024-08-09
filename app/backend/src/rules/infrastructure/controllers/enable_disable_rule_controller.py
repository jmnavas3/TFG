from flask import Blueprint
from flask.views import MethodView
from injector import inject

from app.backend.src.rules.application.command.enable_disable_rule_handler import EnableDisableRuleHandler
from app.backend.src.rules.application.command.enable_disable_rule_command import EnableDisableRuleCommand
from app.backend.src.base.infrastructure.requests.validate_request_with_factory import validate_request_with_factory

enable_disable = Blueprint('rules', __name__, url_prefix='/rules/enable_disable')


class EnableDisableRuleController(MethodView):
    @inject
    def __init__(self, handler: EnableDisableRuleHandler):
        self._handler = handler

    @validate_request_with_factory(EnableDisableRuleCommand, 'command', method='POST')
    def post(self, command, **kwargs):
        try:
            self._handler.execute(command)
            return "Hola Mundo!", 200
        except Exception as e:
            print(str(e))
            return str(e), 500


enable_disable.add_url_rule(rule="", view_func=EnableDisableRuleController.as_view('enable_disable_rule'))
