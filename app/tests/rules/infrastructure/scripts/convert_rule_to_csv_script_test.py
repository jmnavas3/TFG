from app.backend.src.rules.infrastructure.scripts.convert_rule_to_csv_script import ConvertRuleToCsvScript


def script_arguments(rules_file: str = "", csv_file: str = ""):
    return {
        "rules_file": rules_file,
        "csv_file": csv_file
    }


def test_convert_rule_file_to_csv(test_config):
    script_manager = ConvertRuleToCsvScript()
    result = int(script_manager.execute(**script_arguments(
        rules_file=test_config["RULES_FILE"],
        csv_file=test_config["NEW_CSV_RULES"]
    )))
    print(f"obtenidas {result-1} reglas")
    assert result > 0


def test_convert_single_rule_to_csv(test_config):
    script_manager = ConvertRuleToCsvScript()
    result = int(script_manager.execute(
        **script_arguments(rules_file=test_config["NEW_RULES"],
                           csv_file=test_config["NEW_CSV_RULES"])
    ))
    print(f"obtenidas {result-1} reglas")
    assert result > 0
