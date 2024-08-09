from app.backend.src.base.application.command.command_interface import CommandInterface
from app.backend.src.base.application.command.handler_interface import HandlerInterface


class EnableDisableRuleHandler(HandlerInterface):

    def __init__(self, service):
        self._service = service

    def execute(self, command: CommandInterface):
        try:
            return self._service.manage_rule(command)
        except Exception as e:
            print(e)
