#!/usr/bin/env python
# file: triangle.py  # developed under Python 3.7.3

r"""
DESCRIPTION
    Exercism exercise: https://exercism.org/tracks/python/exercises/triangle

AUTHOR
    Erik Johnson

DEV NOTES
    This can be tested on my local system via git bash shell:
    $ pytest  (with a pytest.ini file in track dir)

    # To publish:
    $ exercism submit

HISTORY
    2023Jan23  created
"""


def zero_check(sides):
    return all([s > 0 for s in sides])


def ineq_check(sides):
    a, b, c = sides
    return all([
        a + b >= c,
        b + c >= a,
        a + c >= b,
    ])


def check(sides):
    return ineq_check(sides) and zero_check(sides)


def side_count(sides):
    return len({s: True for s in sides})


def equilateral(sides):
    return check(sides) and side_count(sides) == 1


def isosceles(sides):
    return check(sides) and side_count(sides) in [1, 2]


def scalene(sides):
    return check(sides) and side_count(sides) == 3


if __name__ == '__main__':
    print(scalene([7, 3, 2]))


# EOF
