from app.backend.src.base.infrastructure.scripts.base_script import BaseScript


class ConvertRuleToCsvScript(BaseScript):
    script_name = "convert_rule_to_csv.sh"

    def execute(self, rules_file: str = "", csv_file: str = ""):
        self.params = [rules_file, csv_file]
        result = self.run(output=True)

        if not result:
            raise SystemError("Csv file not created")

        if not str(result).isdecimal():
            raise SystemError(f"Script error: {str(result)}")

        return result if result else None
