#!/usr/bin/env python
# file: exchange.py

"""
DESCRIPTION
    https://exercism.org/tracks/python/exercises/currency-exchange

HISTORY
    2023Jan05   ej  created

"""


def exchange_money(budget, exchange_rate):
    """
    See link for exercize.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Create the get_change() function, taking 2 parameters:

    budget : Amount of money before exchange.
    exchanging_value : Amount of money that is taken from the budget to be exchanged.
    This function should return the amount of money that is left from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    See link for exercize.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """
    See link for exercize.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def get_leftover_of_bills(budget, denomination):
    """
    See link for exercize.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget - (denomination * get_number_of_bills(budget, denomination))


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    See link for exercize.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    value = exchange_money(budget, (1.0 + 0.01 * spread) * exchange_rate)
    return denomination * get_number_of_bills(value, denomination)

# EOF
