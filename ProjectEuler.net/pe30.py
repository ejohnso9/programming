#!/usr/bin/env python
"""
developed under Python 3.7.3

Project Euler Problem #30
    https://projecteuler.net/problem=30

PROBLEM

    Surprisingly there are only three numbers that can be written as the sum of fourth
    powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of
    their digits.

DISCUSSION
    Writing the function of part A (below) seems simple enough. But the
    problem statement asserts there are only three such numbers for
    power of 4. They all happen to be 4 digit numbers. So, there are no
    such 2-digit numbers, 3-digit numbers, 5-digits number, 6, 7, ...
    First of all, is the above assertion true for the 2- through 5-digit
    numbers?
    How do you know when you have searched far enough?

    NB: range(1, 1e5 - 1) is up through the 5-digit numbers
        range(1, 1e6 - 1) is up through the 6-digit numbers, etc

    Searching up through 1e7 takes roughly 30 seconds(?), does not
    reveal any new numbers for power=4.

    Simply switching the power to 5 and running up through 1e6
    yields 1 plus:
        [4150, 4151, 54748, 92727, 93084, 194979]

    The sum of which is:

        >>> sum([4150, 4151, 54748, 92727, 93084, 194979])
        443839

    Indeed, 443839 accepted as correct answer.

    There are probably some arguments to be made about searching larget
    digit spaces, but I guess I am going to be pragmatic (at least for
    now) and call this problem done.

STRATEGY
    A. write a function that takes a number and returns whether the sum of
        it's digits to a power is the same as the input digit.

    B. run the loop over the range...  ummm, yeah, let's do the
        DISCUSSION part 

    C. A lot of multiplications can be avoided by pre-computing a list
        of the digits raised to the power. That's one minor
        optimization.

    * do part A)
        for power=4
            run this up through the 6-digit space, verify only those hits
            run over range(10, 99999 + 1)
            WHOA: for range(1, 10000) it finds 1, plus [1634, 8208, 9474]
                in just about 1/2 second
"""

import sys


# helper func for loop in __main__ branch
def f(i, digits_d, powers):
    """
    Is an integer number the same as the sum of the digits to some power
    (precomputed in 'powers')

    :param i: the integer to check
    :param digits_d: str to int conversion dict: {'0': 0, '1': 1, ..., '9': 9}
    :param digits_d: pre-computed powers: [0 ** p, 1 ** p, ..., 9 ** p]
    """

    digits = [digits_d[c] for c in list(str(i))]
    terms = [powers[d] for d in digits]

    return sum(terms) == i



# ENTRY POINT
if __name__ == '__main__':

    p = 5
    digits = {str(i): i for i in range(10)}
    powers = [i ** p for i in range(10)]

    for i in range(1, int(1e6) - 1):
        if f(i, digits, powers):
            print(i)

    # 443839 is correct answer.

# EOF

