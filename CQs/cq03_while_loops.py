"""This program finds and tells you the amounf of times a char appears"""

__author__ = "730698509"


def num_instances(phrase: str, search_char: str) -> int:
    # while phrase[0]=search_char
    # it needs to go through the entire phrase
    # need a counter that counts number of instances
    count: int = 0
    track: int = 0
    while track < len(phrase):
        if phrase[track] == search_char:
            count += 1
        track += 1
    return count
