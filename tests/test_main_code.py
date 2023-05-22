from src.main_code import get_presentation


def test_get_presentation():
    data = ("date", "desc", "sender", "recip", "amount")
    assert get_presentation(data) == 'date desc\nsender -> recip\namount\n'
