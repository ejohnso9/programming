#!/usr/bin/env python
# file: bob.py  # developed under Python 3.7.3

r"""
DESCRIPTION
    Exercism exercise:
        https://exercism.org/tracks/python/exercises/bob

AUTHOR
    Erik Johnson

DEV NOTES
    Using type hints here (simply as an example of doing it).

    This can be tested on my local system via git bash shell:
    $ pytest -o markers=task

    # I created pytest.ini according to info in HELP.md.
    # It now sites in the 'python' track dir itself.
    # With that in place, test can be accomplished as simply:
    $ pytest

    # To publish:
    $ exercism submit

HISTORY
    2023Jan17  created
"""


import string


def is_question(hey_bob: str) -> bool:
    return hey_bob.strip().endswith('?')


def is_yelling(hey_bob: str) -> bool:
    letters = [c for c in list(hey_bob) if c in string.ascii_letters]
    return letters and all([c in string.ascii_uppercase for c in letters])


def response(hey_bob: str) -> str:
    _input = hey_bob.strip()
    if is_question(_input) and not is_yelling(_input):
        return "Sure."
    elif is_question(_input) and is_yelling(_input):
        return "Calm down, I know what I'm doing!"
    elif is_yelling(_input):
        return "Whoa, chill out!"
    elif not _input:
        return "Fine. Be that way!"
    else:
        return "Whatever."

# EOF
