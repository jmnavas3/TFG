import pytest

from app.backend.src.rules.domain.services.add_rule_file_service import AddRuleFileService
from app.backend.src.rules.infrastructure.scripts.add_rule_file_script import AddRuleFileScript
from app.backend.src.rules.infrastructure.scripts.convert_rule_to_csv_script import ConvertRuleToCsvScript
from app.backend.src.rules.infrastructure.services.import_rules_service import ImportRulesService


@pytest.fixture()
def add_rule_file_service(generate_database, test_config):
    return AddRuleFileService(
        repository=ImportRulesService(engine=generate_database['db'].get_engine(), csv=test_config["NEW_CSV_RULES"]),
        csv_script=ConvertRuleToCsvScript(),
        copy_script=AddRuleFileScript()
    )


def test_add_rule_file_service(add_rule_file_service, test_config):
    response = add_rule_file_service.manage_rule(test_config["NEW_RULES"],
                                                 test_config["RULES_FILE"],
                                                 test_config["NEW_CSV_RULES"])

    assert isinstance(response, dict)
    assert response["rule"] == test_config["NEW_RULES"]
    assert response["status"] == 1
