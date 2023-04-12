#!/usr/bin/env python
# file: arcade_game.py  # developed under Python 3.7.3

r"""
DESCRIPTION
    Exercism exercise:
    https://exercism.org/tracks/python/exercises/ghost-gobble-arcade-game

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

$ exercism submit lasagna.py

    Your solution has been submitted successfully.
    View it at:

    https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna


HISTORY
    2023Jan17  created
"""


# Functions for implementing the rules of the classic arcade game Pac-Man.


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    """

    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """

    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """

    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """

    return has_eaten_all_dots and (
            not touching_ghost
            or eat_ghost(power_pellet_active, touching_ghost))
