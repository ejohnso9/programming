#!/usr/bin/env python
# file: grains.py  # dev under Python 3.7.3

"""
DESCRIPTION
    Exercism problem: https://exercism.org/tracks/python/exercises/grains

AUTHOR
    Erik P. Johnson

TESTING
    $ pytest

HISTORY
    2022Jan12  created
"""


def square(number):
    ERR_MSG = "square must be between 1 and 64"
    if number not in range(1, 65):  # better, maybe?
        raise ValueError(ERR_MSG)

    return 2 ** (number - 1)


def total():
    # this could more functionally (but substantially less efficiently)
    # be implemented as a sum of square() calls)
    # return sum([square(i) for i in range(1, 65)])
    return (2 ** 64) - 1


def main():
    print(f"total is: {total()}")


if __name__ == '__main__':
    main()

# EOF
