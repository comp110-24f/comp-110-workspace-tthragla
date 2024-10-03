"""example of mutable lists"""

__author__ = "730698509"


def lessen(my_list: list[int]):
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] = my_list[idx] - 1
        idx += 1
    return msg


msg: list[int] = [4, 5, 6]
