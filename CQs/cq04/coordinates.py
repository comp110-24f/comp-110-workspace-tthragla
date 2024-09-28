"""return coordinate pairs from input"""

__author__ = "730698509"


def get_coords(xs: str, ys: str) -> None:
    count = 0
    while count < len(xs):
        idx = 0
        while idx < len(ys):
            print("(" + xs[count] + ", " + ys[idx] + ")")
            idx += 1
        count += 1
    return None
