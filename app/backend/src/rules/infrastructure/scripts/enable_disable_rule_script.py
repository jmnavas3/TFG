from app.backend.src.base.infrastructure.scripts.base_script import BaseScript


class EnableDisableRuleScript(BaseScript):
    script_name = "enable_disable_rule.sh"

    def execute(self, sid: str, action: str, file: str = ""):
        self.params = [action, sid, file]
        script_response = self.run(output=True)

        if not script_response:
            raise ValueError("rule not found or already disabled")

        if script_response != "enabled" and script_response != "disabled":
            raise SystemError(f"Script failed: {script_response}")

        return script_response
