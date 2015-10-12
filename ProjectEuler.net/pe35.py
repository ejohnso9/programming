#!/usr/bin/env python

from math import log, ceil
from prime import is_prime
import pdb

# ProjectEuler.net Problem #35
# https://projecteuler.net/problem=35
# 

def is_circular_prime(n):
    """Returns true if n and all rotations of n are also prime
    Note that a number like 333 does not have 3 rotations!
    """

    # pdb.set_trace()
    s = str(n)
    for i in xrange(len(s)):
        if not is_prime(n):
            return False
        s = s[1:] + s[0]
        n = int(s)

    return True

    
def pe35(N, returnList):

    cpList = [2]
    count = 1  # for 2
    n = 3

    while n < N:
        if is_circular_prime(n):
            count += 1
            cpList.append(n)
        n += 2

    if returnList:
        return cpList
    else:
        return count


if __name__ == '__main__':
    N = int(1e6)
    cpList = pe35(N, True);
    print cpList
    print "count of circular primes under", N, "is", len(cpList)

