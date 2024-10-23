"""implement some list utility functions"""

__author__ = "730698509"


def only_evens(nums: list) -> list:
    """make a new list that has only even numbers"""
    even_numbers: list = []
    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """return a subset of the list"""
    if len(nums) == 0 or start >= len(nums) or end <= 0:
        return []
    if start < 0:
        start = 0
    if end > len(nums):
        end = len(nums)
    result: list[int] = []
    for i in range(start, end):
        result.append(nums[i])
    return result


def add_at_index(list: list[int], element: int, index: int) -> None:
    """Insert element at the given index, mutating the input list"""
    if index < 0 or index > len(list):
        raise IndexError("Index is out of bounds for the input list")
    list.append(0)
    for i in range(len(list) - 1, index, -1):
        list[i] = list[i - 1]
    list[index] = element
