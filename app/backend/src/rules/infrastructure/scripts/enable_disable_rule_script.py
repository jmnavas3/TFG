from app.backend.src.base.infrastructure.scripts.base_script import BaseScript


class EnableDisableRuleScript(BaseScript):
    script_name = "enable_disable_rule.sh"

    def execute(self, sid: str, action: str):
        self.params = [action, sid]
        self.run()
