#!/usr/bin/env python

from math import sqrt
from itertools import count, islice
# import pdb

"""
https://projecteuler.net/problem=10
"""

def isPrime(n):
    if n < 2:
        return False

    return all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


i = 5
total = 5
primes = [2, 3]
n = 2 # how many primes found
# pdb.set_trace()
while i < 2000000:
    if isPrime(i):
        n += 1
        primes.append(i)
        total += i
    i += 2

print "%i primes:" % n
print "total", total
print "sum", sum(primes)
