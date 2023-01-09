#!/usr/bin/env python
# file: hello-world.py  # dev under Python 3.7.3

"""
DESCRIPTION
    https://exercism.org/tracks/python/exercises/two-fer

DEV NOTES
    NB: (a reminder, really) if you declare:

        def two_fer(name):

    then internally try to do something like:
        who = name or 'you'

    the test suite can't even call:

        two_fer()  # missing required arg

HISTORY
    2023Jan06   ej  created
"""


def two_fer(name="you"):
    return f"One for {name}, one for me."


# EOF
