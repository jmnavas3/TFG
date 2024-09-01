from app.backend.src.base.application.command.command_interface import CommandInterface
from app.backend.src.base.application.command.handler_interface import HandlerInterface
from app.backend.src.rules.domain.services.enable_disable_rule_service import EnableDisableRuleService


class EnableDisableRuleHandler(HandlerInterface):

    def __init__(self, service: EnableDisableRuleService):
        self.service = service

    def execute(self, command: CommandInterface):
        try:
            return self.service.manage_rule(command)
        except Exception as e:
            raise e
