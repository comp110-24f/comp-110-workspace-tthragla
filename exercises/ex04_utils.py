"""Practice implementing past algorithms"""

__author__ = "730698509"


def all(a: list[int], b: int) -> bool:
    idx: int = 0
    if len(a) == 0:
        return False
    while idx < len(a):
        if a[idx] != b:
            return False
        idx += 1
    return True


# this function should return the largest value in the list
# so it should iterate over the list and compare values
# if val2 > val 1
# assign val 2 to a local variable
# else val 1 stays assigned to local variable


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    value: int = input[0]
    idx: int = 1
    while idx < len(input):
        if input[idx] > value:
            value = input[idx]
        idx += 1
    return value


def is_equal(aa: list[int], bb: list[int]) -> bool:
    idx: int = 0
    if len(aa) != len(bb):
        return False
    while idx < len(aa):
        if aa[idx] != bb[idx]:
            return False
        idx += 1
    return True


def extend(input1: list[int], input2: list[int]) -> None:
    idx: int = 0
    while idx < len(input2):
        input1.append(input2[idx])
        idx += 1
    print(input1)
