#!/usr/bin/env python
# file: lasagna.py  # developed under Python 3.7.3

r"""
DESCRIPTION
    Exercism exercise: https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna

AUTHOR
    Erik Johnson

EXERCISM MODULE DESCRIPTION
    Functions used in preparing Guido's gorgeous lasagna.
    Learn about Guido, the creator of the Python language:
        https://en.wikipedia.org/wiki/Guido_van_Rossum

DEV NOTES
    This can be tested on my local system via git bash shell:
    $ pytest -o markers=task

    # NB: command above appears to be testing under Python 3.7.3
    #     'python' command is mapped to Python 3.7.3
    #     'py' command is mapped to Python 3.8.10

    # I create pytest.ini according to info in HELP.md.
    # After that, I can simply run:

$ pytest
============================= test session starts =============================
platform win32 -- Python 3.7.3, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\ejohnson\src\git\programming\Exercism\python\guidos-gorgeous-lasagna, configfile: pytest.ini
collected 5 items

lasagna_test.py .....                                                    [100%]

============================== 5 passed in 0.03s ==============================

    # Then, to publish:

$ exercism submit lasagna.py

    Your solution has been submitted successfully.
    View it at:

    https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna


HISTORY
    2023Jan05  created
"""

# define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40  # minutes

# time it takes to prepare a single layer
PREPARATION_TIME = 2  # minutes per layer


def bake_time_remaining(elapsed_time):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_time


def preparation_time_in_minutes(n_layers):
    """
    How long to get ready to start baking.
    (More layers takes more time.)
    """

    return n_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers
    & the time already spent baking and calculates the total elapsed
    minutes spent cooking the lasagna.
    """

    return sum([
        preparation_time_in_minutes(number_of_layers),
        elapsed_bake_time,
    ])


# EOF
