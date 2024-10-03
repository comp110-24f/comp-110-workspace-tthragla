"""Mutating Functions."""

__author__ = "730698509"


def manual_append(a: list[int], b: int) -> None:
    a.append(b)


def double(a: list[int]) -> None:
    idx: int = 0
    while idx < len(a):
        a[idx] = a[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
