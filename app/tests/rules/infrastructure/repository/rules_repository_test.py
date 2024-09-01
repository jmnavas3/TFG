import pytest
from flask import jsonify

from app.backend.src.base.application.dto.pagination import OrderPagination


@pytest.fixture
def rule_sid():
    return "2200030"


def test_get_rule_by_sid(rule_sid, repository):
    expected_data = repository.get_rule_by_sid(rule_sid=rule_sid)
    print(expected_data)

    assert expected_data.get("id", None) == rule_sid


def test_get_rules_with_default_pagination(repository, pagination):
    order_pagination = OrderPagination(**pagination)
    expected_data = repository.get_rules(order_pagination)
    print(jsonify(expected_data).get_data())

    assert len(expected_data["data"]) == pagination["per_page"]
    assert expected_data["total"] > pagination["per_page"]
    assert expected_data["data"][0].get(order_pagination.field, False) > expected_data["data"][1].get(order_pagination.field, False)


def test_rule_exists(rule_sid, repository):
    rule_exists = repository.rule_exists(rule_sid)

    assert rule_exists


def test_update_status(rule_sid, repository):
    updated = repository.update_status(rule_sid, True)
    rule = repository.get_rule_by_sid(rule_sid)
    print(rule)

    assert updated
    assert rule.get("estado", "") == "activada"
