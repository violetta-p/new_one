import pytest
from src.funcs import *


@pytest.fixture
def dict_fixture():
    return {
            "id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации", "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
            }


@pytest.fixture
def dict_fixture_miss():
    return {
            "id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "to": "Счет 64686473678894779589"
            }


def test_get_date(dict_fixture):
    assert get_date(dict_fixture["date"]) == "26.08.2019"


def test_get_sender(dict_fixture):
    assert get_sender(dict_fixture["from"]) == "Maestro 1596 83** **** 5199"


def test_get_recipient(dict_fixture):
    assert get_recipient(dict_fixture["to"]) == "Счет **9589"


def test_if_data_missing(dict_fixture_miss):
    assert get_sender(dict_fixture_miss.get("from", None)) == "No info about sender"
