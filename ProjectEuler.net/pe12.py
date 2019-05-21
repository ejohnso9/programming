#!/usr/bin/env python
"""
written for Python 2.x (2.7)

Project Euler Problem Template

DISCUSSION

STRATEGY

"""

import sys

# sample function
def factor(n):    
    return set(reduce(list.__add__, 
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# ENTRY POINT
if __name__ == '__main__':

    n = 1

    while True:
        factors = factor(n)
        if len(factors) >= 500:
            print n, factors
            sys.exit(0)
        n += i
