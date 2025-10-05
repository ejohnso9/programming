#!/usr/bin/env python

"""
Python functions collected from various sources on the web.
"""

import sys

# source: http://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning
def partition(number, perms=False):
    """
    Slightly modified by ej to take 'perms' arg. Called w/ one arg,
    get all the possible additive partitions of 'number'. 

    Example: 

    partition(3) returns:  set([(1, 2), (1, 1, 1), (3,)]) 

    If you want to consider (1, 2) and (2, 1) as separate items, call:

    partition(3, True)
    """

    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x, perms):
            if perms: # all permutations
                answer.add((x, ) + y)
            else:
                answer.add(tuple(sorted((x, ) + y)))

    return answer


# all the factors of integer n
def factors(n):    
    """Returns a set of all the factors of n. For example:
    factors(42) gives: set([1, 2, 3, 6, 7, 14, 21, 42])
    """
    return set(reduce(list.__add__, 
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# Test primality of given integer
# http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
def isPrime(n):
    """Predicate for whether 'n' is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


if __name__ == '__main__':

    print("""
file not meant to be run as a stand-alone script.

Use: 

    from ej_lib import *

to access functions defined in this file
""")

# EOF

