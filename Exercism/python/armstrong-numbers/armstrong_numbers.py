#!/usr/bin/env python
# file: armstrong_numbers.py  # dev under Python 3.7.3

"""
DESCRIPTION
    Exercism problem: https://exercism.org/tracks/python/exercises/armstrong-numbers

AUTHOR
    Erik P. Johnson

TESTING
    $ pytest

HISTORY
    2022Jan12  created
"""


def is_armstrong_number(x):
    n = len(str(x))
    digits = [int(c) for c in list(str(x))]
    return x == sum([i ** n for i in digits])


def main():
    # 0 *IS* an Armstrong number
    nums = [0, 8, 9, 10, 153, 154]
    for x in nums:
        print(f"{x}: {is_armstrong_number(x)}")


if __name__ == '__main__':
    main()

# EOF
