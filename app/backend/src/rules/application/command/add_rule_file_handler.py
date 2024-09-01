from app.backend.src.base.application.command.handler_interface import HandlerInterface


class AddRuleFileHandler(HandlerInterface):

    def __init__(self, add_rule_file_service):
        self.add_rule_file_service = add_rule_file_service

    def execute(self, file_path):
        try:
            return self.add_rule_file_service.manage_rule(file_path)
        except Exception as e:
            raise e
