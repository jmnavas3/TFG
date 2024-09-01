from app.backend.src.base.infrastructure.scripts.base_script import BaseScript


class AddRuleFileScript(BaseScript):
    script_name = "add_rule_file.sh"

    def execute(self, new_file: str = "", rules_file: str = ""):
        self.params = [new_file, rules_file]
        script_response = self.run(output=True)

        if not script_response:
            raise SystemError("new rules file not found")

        if str(script_response) != "done":
            raise SystemError(f"Script failed: {script_response}")

        return str(script_response)
