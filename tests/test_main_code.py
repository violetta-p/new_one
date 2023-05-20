import pytest
from src.main_code import get_presentation
@pytest.fixture
def dict_fixture():
    return [{"id": 41428829, "date": "03.05.2018", "description": "Перевод организации"},
            {"id": 441945886, "date": "26.08.2019","description": "Перевод организации"}]


def test_get_presentation():
    data = ("date", "desc", "sender", "recip", "amount")
    assert get_presentation(data) == 'date desc\nsender -> recip\namount\n'

