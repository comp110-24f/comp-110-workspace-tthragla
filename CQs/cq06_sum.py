"""Summing the elements of a list using different loops"""

__author__ = "730698509"


# in order to iterate through the list and return the total we need two local variables
# one that will iterate through the list
# and another that will hold the sum(new value)
def w_sum(vals: list[float]) -> float:
    """return sum of all values"""
    idx: int = 0
    count: float = 0.0
    if vals == []:
        return 0.0
    else:
        while idx < len(vals):
            count = count + vals[idx]
            idx += 1
    return count


# since we're using the for..in loop we only need one local variable
# the for in loop does the iteration for us
# we only need a local variable for the sum
def f_sum(vals: list[float]) -> float:
    """return sum of all values using for in loop"""
    count: float = 0.0
    for value in vals:
        count += value
    return count


def f_range_sum(vals: list[float]) -> float:
    """return sum of all values using range keyword"""
    count: float = 0.0
    for i in range(len(vals)):
        count += vals[i]
    return count
