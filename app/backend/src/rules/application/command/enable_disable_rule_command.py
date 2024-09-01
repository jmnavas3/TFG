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
            if len(sid) < 7 or len(sid) > 9:
                raise ValueError("Sid must be 7 characters long")
            if not sid.isdecimal():
                raise ValueError("Sid must be entire decimal")
            if action != "enable" and action != "disable":
                raise ValueError("Action not valid")

            return EnableDisableRuleCommand(
                sid=sid,
                action=action
            )
        except Exception as e:
            raise e
