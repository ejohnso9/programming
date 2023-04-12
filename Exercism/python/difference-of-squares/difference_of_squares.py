#!/usr/bin/env python
# file: difference_of_squares.py  # developed under Python 3.7.3

r"""
DESCRIPTION
    Exercism exercise:
    https://exercism.org/tracks/python/exercises/difference_of_squares.py

AUTHOR
    Erik Johnson

DEV NOTES
    This can be tested on my local system via git bash shell:
    $ pytest -o markers=task

    # NB: command above appears to be testing under Python 3.7.3
    #     'python' command is mapped to Python 3.7.3
    #     'py' command is mapped to Python 3.8.10

    # I created pytest.ini according to info in HELP.md.
    # After that, I can simply run:
    $ pytest

    # To publish:
    $ exercism submit difference_of_squares.py


HISTORY
    2023Jan17  created
"""


def square_of_sum(n):
    return sum([i for i in range(1, n + 1)]) ** 2


def sum_of_squares(n):
    return sum([i ** 2 for i in range(1, n + 1)])


def difference_of_squares(n):
    return square_of_sum(n) - sum_of_squares(n)


if __name__ == '__main__':
    print(f"square_of_sum: {[square_of_sum(i) for i in range(1, 10)]}")
    print(f"sum_of_squares: {[sum_of_squares(i) for i in range(1, 10)]}")
    print()

# EOF
