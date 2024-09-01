import pytest

from app.backend.src.rules.infrastructure.services.import_rules_service import ImportRulesService


@pytest.fixture()
def rule_csv_service(generate_database, test_config):
    return ImportRulesService(engine=generate_database['db'].get_engine(), csv=test_config["NEW_CSV_RULES"])


def test_import_csv(rule_csv_service, repository):
    new_rule_sid = "50200002"
    rule_csv_service.import_csv("replace")
    new_rule_exists = repository.rule_exists(new_rule_sid)
    assert new_rule_exists
