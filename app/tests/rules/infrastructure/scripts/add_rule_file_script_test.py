from app.backend.src.rules.infrastructure.scripts.add_rule_file_script import AddRuleFileScript


def script_arguments(new_file: str = "", rules_file: str = ""):
    return {
        "new_file": new_file,
        "rules_file": rules_file
    }


def test_copy_new_rules_to_active_rules(test_config):
    script_manager = AddRuleFileScript()
    result = script_manager.execute(**script_arguments(
        new_file=test_config["NEW_RULES"],
        rules_file=test_config["RULES_FILE"]
    ))
    assert result == "done"
