#!/usr/bin/env -S python
"""
Solution to ProjectEuler #46:
    https://projecteuler.net/problem=46
"""


import math


# seed this with a few known primes then let the code take care of the rest
_primes = [2, 3, 5, 7, 11]


def addAPrime() -> int:
    """add the next prime we don't already have to our list (_primes)"""

    candidate = _primes[-1]

    # search forward, two at a time from last prime we have
    while True:
        candidate += 2
        n_sqrt_i = int(math.sqrt(candidate))
        for p in _primes:
            if candidate % p == 0:
                break  # not prime: go to next candidate and restart checking the prime list
            if p > n_sqrt_i:
                # prime: none of the primes <= sqrt(n) are factors
                _primes.append(candidate)
                return candidate

    # some sort of mistake: you can't legitimately exit this way
    raise RuntimeException("programming error")


def isPrime(n: int) -> bool:
    """True if n is prime, else False"""

    # to make this simple (and avoid a sqrt operation), just store primes up to or exceeding n
    while _primes[-1] < n:
        addAPrime()  # NB: modifying _primes!!!

    # now, we've either listed n as a prime or not
    return n in _primes


def isGoldbach(n, p):
    """
    Check for the Goldbach condition for int n and a given prime, p
    True if: (n - p) / 2 is a (perfect) square, else False
    """

    np2 = (n - p) / 2
    if not np2.is_integer():
        return False  # sqrt of non-integers is never integer

    return math.sqrt(np2).is_integer()


def main():

    # starting on 5, find the first composite odd failing Goldbach's conjecture
    n = 3
    while True:
        n += 2
        if isPrime(n):
            continue  # not composite, try next one

        # else: check for a Golbach solution using all the primes
        goldbach = False  # flag used to break second loop
        for p in _primes:
            if p > n:
                break
            if isGoldbach(n, p):
                goldbach = True
                break

        if not goldbach:
            print(f"{n} fails the Goldbach conjecture")  # 5777 is the first failure
            break

    print("done.")

    # you can use this to generate primes up to or past n
    # n = 10001
    # print(f"isPrime({n}) is: {isPrime(n)}")
    # print(_primes)


if __name__ == '__main__':
    main()

# EOF

