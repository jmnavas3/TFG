import pytest

from app.backend.src.rules.infrastructure.scripts.enable_disable_rule_script import EnableDisableRuleScript


def script_arguments(action: str, sid: str = "2200030"):
    return {"sid": sid, "action": action, "file": "/app/tests/test_files/test_suricata.rules"}


def test_disable_rule():
    script_manager = EnableDisableRuleScript()
    result = script_manager.execute(**script_arguments("disable"))
    assert result == "disabled"


def test_enable_rule():
    script_manager = EnableDisableRuleScript()
    result = script_manager.execute(**script_arguments("enable"))
    assert result == "enabled"


def test_rule_not_exists():
    script_manager = EnableDisableRuleScript()
    with pytest.raises(ValueError):
        script_manager.execute(**script_arguments("enable", sid="2200050"))
