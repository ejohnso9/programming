#!/usr/bin/env python
# file: lists.py  # developed under Python 3.7.3

# This does not follow doc string conventions
# see: https://peps.python.org/pep-0257/
r"""
DESCRIPTION
    Exercism exercise:
        https://exercism.org/tracks/python/exercises/card-games

    Functions for tracking poker hands and assorted card tasks.

AUTHOR
    Erik Johnson

REFERENCE(S)
    Python list documentation: https://docs.python.org/3/tutorial/datastructures.html


DEV NOTES
    # I created pytest.ini file according to info in HELP.md.
    # with that in the tracks dir itself (e.g., 'python)...
    $ pytest  # or: $ pytest -x  # to stop on first error

    # To publish:
    $ exercism submit

HISTORY
    2023Jan24  created
"""

# IMHO, this idea that all strings need to use the same kind of
# quote character is just plain stupid.
# pylint: disable=W1405

def get_rounds(round_n):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    # IMO: 'i' is a great name to use here
    return [round_n + i for i in (0, 1, 2)]  # pylint: disable=C0104


def concatenate_rounds(rounds_1: list, rounds_2: list):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand) -> bool:
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    avg = card_average(hand)
    median = hand[len(hand) // 2]
    first_last = (hand[0] + hand[-1]) / 2.0

    return avg in [median, first_last]


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    # pylint: disable=C0104  # IMO: 'i' is a great name to use here
    n = len(hand)  # pylint: disable=C0104  # IMO: 'n' is a great name to use here
    evens = [hand[i] for i in range(0, n, 2)]  # indices: 0, 2, ...
    odds = [hand[i] for i in range(1, n, 2)]  # indices: 1, 3, ...

    return card_average(odds) == card_average(evens)


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    card = hand[-1]
    last_card = 22 if card == 11 else card
    return hand[:-1] + [last_card]


if __name__ == '__main__':

    f = approx_average_is_average
    input_vars = [
        [1, 2, 3, 4],
        [0, 1, 5],
        [3, 6, 9, 12, 150],
        [1, 2, 3, 5, 9],
        [2, 3, 4, 7, 8],
        [1, 2, 3],
        [2, 3, 4],
        [2, 3, 4, 8, 8],
        [1, 2, 4, 5, 8],
    ]
    exp_ls = [False] * 4 + [True] * 4

    # lists_test.py::CardGamesTest::test_average_even_is_average_odd
    f = average_even_is_average_odd
    input_vars = [[5, 6, 8], [1, 2, 3, 4], [1, 2, 3], [5, 6, 7], [1, 3, 5, 7, 9]]
    exp_ls = [False] * 2 + [True] * 3

    for _hand, exp in zip(input_vars, exp_ls):
        act_tf = f(_hand)
        if not act_tf == exp:
            print(f"act: {act_tf}, exp: {exp}")

# EOF
