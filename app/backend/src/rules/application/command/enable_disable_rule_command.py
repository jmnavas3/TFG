from app.backend.src.base.application.command.command_interface import CommandInterface
from attr import attrib, validators, frozen


@frozen
class EnableDisableRuleCommand(CommandInterface):
    sid = attrib(validator=[validators.instance_of(str)])
    action = attrib(validator=[validators.instance_of(str)])

    @staticmethod
    def generate(
            sid: str,
            action: str,
            **kwargs):
        try:
            return EnableDisableRuleCommand(
                sid=sid,
                action=action
            )
        except Exception as e:
            raise e
