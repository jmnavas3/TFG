from attr import attrib, frozen, validators

from app.backend.src.base.application.command.command_interface import CommandInterface


@frozen
class GetRulesRequest(CommandInterface):
    page = attrib(validator=[validators.instance_of(int)])

    @staticmethod
    def generate(page: str, **kwargs):
        return GetRulesRequest(page=int(page))
