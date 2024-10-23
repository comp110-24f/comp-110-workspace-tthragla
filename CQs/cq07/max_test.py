__author__ = "730697509"


from CQs.cq07.find_max import find_and_remove_max


def test_returns_value() -> None:
    a = [1, 2, 3, 4, 5, 5]
    result = find_and_remove_max(a)
    assert result == 5


def test_mutates() -> None:
    a = [1, 2, 3, 4, 5, 5]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 4]


def test_unconventianal_input() -> None:
    a = [2]
    result = find_and_remove_max(a)
    assert result == 2
