from flask import Blueprint

from app.backend.src.rules.infrastructure.controllers.add_rule_file_controlller import AddRuleFileController
from app.backend.src.rules.infrastructure.controllers.enable_disable_rule_controller import EnableDisableRuleController
from app.backend.src.rules.infrastructure.controllers.get_rules_controller import GetRulesController

rules_page = Blueprint('rules', __name__, url_prefix='rules')

rules_page.add_url_rule(rule='/list', view_func=GetRulesController.as_view('list_rules'))
rules_page.add_url_rule(rule='/enable_disable', view_func=EnableDisableRuleController.as_view('enable_disable_rule'))
rules_page.add_url_rule(rule='/add_file', view_func=AddRuleFileController.as_view('add_file'))
