__author__ = "730697509"


def find_and_remove_max(a: list[int]) -> int:
    idx: int = 0
    if a == []:
        return -1
    max_value = a[0]
    for val in a:
        if val > max_value:
            max_value = val
    while idx < len(a):
        if a[idx] == max_value:
            a.pop(idx)
        else:
            idx += 1
    return max_value
