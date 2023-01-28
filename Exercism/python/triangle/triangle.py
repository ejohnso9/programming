#!/usr/bin/env python
# file: triangle.py  # developed under Python 3.7.3

# This is not following docstring conventions - it's more like
# UNIX man pages, but that's what I want here, for my own use.
# Like, when I come across this file 6 months or 3.5 years later,
# I want to answer:
#   * "What the hell is this?"
#   * "What's this Exercism thingy?"
#   * "How do you do it?"
r"""
DESCRIPTION
    Exercism exercise:
        https://exercism.org/tracks/python/exercises/triangle

AUTHOR
    Erik Johnson

REFERENCE(S)
    https://peps.python.org/pep-0257/
    https://docs.python.org/3/library/typing.html
    https://docs.python.org/3/library/typing.html#typing.Union
    Pycon 2022 talk: https://www.youtube.com/watch?v=wbohVjhqg7c
    https://docs.python.org/3/reference/expressions.html#generator-expressions
    "displays" (comprehensions): https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries

DEV NOTES
    This can be tested on my local system via git bash shell:
    $ pytest  # (with a pytest.ini file in track dir)

    # To publish:
    $ exercism submit

HISTORY
    2023Jan23  created
    2023Jan24  another iteration after great feedback from 'IsaacG'
    2023Jan25  Other iterations after discussions w/ 'IsaacG' (TYSM!)
"""


# Semi-modern type annotation (just because I can - a "working" example).
from typing import Union, List  # A big-el List! (Needed for my old Python 3.7.3)
Numeric = Union[int, float]  # not needed, OK, but I like the explicitness here
NumVector = List[Numeric]


def check(sides: NumVector) -> bool:
    """Basic problem statement requirements validation."""
    # all sides required to be non-zero
    if not all(side > 0 for side in sides):
        return False

    # check all 3 of the triangle inequality conditions
    a, b, c = sides  # unpack function args into nicer names
    rv = all(_a + _b >= _c for _a, _b, _c in [(a, b, c), (b, c, a), (a, c, b)])
    return rv


def side_count(sides: NumVector) -> int:
    """The number of distinct length values."""
    return len(set(sides))


def equilateral(sides: NumVector) -> bool:
    """Predicate for whether 'sides' represents an equilateral triangle."""
    return check(sides) and side_count(sides) == 1


def isosceles(sides: NumVector) -> bool:
    """Predicate for whether 'sides' represents an isosceles triangle."""
    return check(sides) and side_count(sides) <= 2


def scalene(sides: NumVector) -> bool:
    """Predicate for whether 'sides' represents a scalene triangle."""
    return check(sides) and side_count(sides) == 3


# [<EntryPoint>]  # (F# marker)
if __name__ == '__main__':
    # unit tests that were failing
    # print(scalene([7, 3, 2]))
    print(isosceles([1, 1, 3]))


# EOF
