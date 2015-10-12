#!/usr/bin/env python

# Python
# ProjectEuler.net Problem #5
# https://projecteuler.net/problem=5
# Find first integer that is a multiple of (1..20)

import operator

# The probelm states that 2520 is the first that is a multiple of
# 1..10, so we can start our search there.
def pe5():

    # n = 2520
    # n = int(7e7 + 9) # already checked up to 70 mil
    # n = 232788000
    loopCount = 0
    maxDiv = 20 # biggest divisor to search up to
    found = False

    # added after orig answer found
    pFactors = [2, 3, 5, 7, 11, 13, 17, 19]
    inc = reduce(operator.mul, pFactors)
    print "inc is:", inc
    n = inc # 9,699,690

    while not found:
        for i in xrange(2, maxDiv + 1):
            if n % i != 0:
                break

        if i == maxDiv:
            found = True
        else:
            n += inc # has to be multiple of 19, which is prime

        loopCount += 1
        print loopCount, n

    return n;  # 232792560


answer = pe5()
print "final answer is:",  answer

"""
POSTMORTEM
    So, one can check the factorization of this at Wolfram Alpha:

    http://www.wolframalpha.com/input/?i=prime+factors+of+232792560

prime factors are: 2^4, 3^2, 5, 7, 11, 13, 17, 19 

I was originally incrementing by 19. That is a substantial improvement
over incrementing by 1, but I probably should have seen that the number
has to at least be a multiple of the product of its prime factors (which
is 9699690) and is a far cry over 19.

With that in place, this will solve in just 24 loop iterations (2^3 * 3,
the other missing prime factors that are not obvious).

Note that the answer (232792560), is *MUCH* less than 20!

>>> import math
>>> math.factorial(20)
2432902008176640000

"""

