#!/usr/bin/env python
# https://projecteuler.net/problem=7
from itertools import count, islice
import time

def isPrime(n):
    if n < 2:
        return False
    return all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

t0 = time.time()
i = 3
n = 1 # how many primes found
while True:
    if isPrime(i):
        n += 1
        if n == 10001:
            break
    i += 2

print n, i # 10001, 104743
print "in %f sec" % (time.time() - t0) # ~0.6 sec
