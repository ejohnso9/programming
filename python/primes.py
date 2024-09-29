#!/usr/bin/env -S python

"""
Code to generate prime integers.

"""


import math


# let's just seed this with a few known primes, then procees from there.
_primes = [2, 3, 5, 7]


def nextPrime() -> int:
    last_prime = _primes[-1]
    n_sqrt_i = int(math.sqrt(last_prime))

    # add one more prime to our list
    while True:
        candidate = last_prime + 2
        for p in _primes:
            if candidate % p == 0:
                break
            if p >= n_sqrt_i:
                _primes.append(candidate)
                return candidate



"""True if n is prime, else False
def isPrime(n: int) -> bool:
    n_sqrt_i = int(math.sqrt(n))
    last_p = _primes[-1]

    # generate more primes if needed
    # while last_p < n_sqrt_i:
    #     last_p = nextPrime()

    # check remainder on the primes we have...
    for p in _primes:
        if n % p == 0:
            return False
        if p >= n_sqrt_i:
            return True

    # we don't have enough primes to work with...
    p = nextPrime()
"""


def main():
    for i in range(10):
        print(nextPrime())

    print(_primes)


if __name__ == '__main__':
    main()


# EOF

