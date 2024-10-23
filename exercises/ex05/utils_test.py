"""define unit test for utils function"""

__author__ = "730698509"


from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_returns_value() -> None:
    """tests to see if it returns onl evens"""
    nums = [1, 2, 3, 4]
    result = only_evens(nums)
    assert result == [2, 4]


def test_mutability() -> None:
    """tests to see if the original list is not mutated"""
    nums = [1, 2, 3, 4]
    only_evens(nums)
    assert nums == [1, 2, 3, 4]


def test_edge_case() -> None:
    """tests to see if it will return an empty list if input is empty list"""
    nums = []
    result = only_evens(nums)
    assert result == []


def test_returns_as_expected() -> None:
    """tests to see if it returns subset of original list"""
    nums = [
        1,
        2,
        3,
        4,
    ]
    start = 0
    end = 4
    result = sub(nums, start, end)
    assert result == [1, 2, 3, 4]


def test_if_mutates() -> None:
    """tests to see if the original list is mutated"""
    nums = [1, 2, 3, 4]
    start = 0
    end = 4
    sub(nums, start, end)
    assert nums == [1, 2, 3, 4]


def test_unexpected() -> None:
    """tests if it works when start is negative"""
    nums = []
    start = -1
    end = 4
    result = sub(nums, start, end)
    assert result == []


def test_returning_value() -> None:
    """tests to see if it returns as expected"""
    list = [10, 20, 30, 40]
    element = 25
    index = 2
    add_at_index(list, element, index)
    assert list == [10, 20, 25, 30, 40]


def test_if_one_value() -> None:
    """tests to see if it will return 0 if input is empty list"""
    list = [10]
    element = 25
    index = 1
    add_at_index(list, element, index)
    assert list == [10, 25]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index(list=[1, 2, 3, 4], element=4, index=-1)
        # an IndexError is raised for the case when the add_at_index is given an index
        # that is greater than the length of our <list_object>
