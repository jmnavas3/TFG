from flask import Blueprint

from app.backend.src.firewall.infrastructure.controllers.get_blacklist_controller import GetBlacklistController
from app.backend.src.firewall.infrastructure.controllers.get_firewall_controller import GetFirewallController


firewall_page = Blueprint('firewall', __name__, url_prefix='firewall')

firewall_page.add_url_rule(rule='/rules', view_func=GetFirewallController.as_view('firewall_rules'))
firewall_page.add_url_rule(rule='/blacklist', view_func=GetBlacklistController.as_view('firewall_blacklist'))
