#!/usr/bin/env python
# file: labs109.py

"""
DESCRIPTION:
    Source file holding function definitions for Ilkka Kokarinen's
    problem set.

AUTHOR:
    Erik Johnson (of all but ryserson_letter_grade())
    ejohnso9@earthlink.net

HISTORY
    2025Nov25 DL repo & start
"""


# 1. Ryerson letter grade (pg 9)
def ryerson_letter_grade(n):
    """This is starting source provided by ikokkari"""

    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


# 2. Ascending list (pg 10)
def is_ascending(items: list[int]) -> bool:
    if len(items) in (0, 1):
        return True
    return all([items[i] < items[i + 1] for i in range(len(items) - 1)])


# 3. Riffle shuffle kerfuffle (pg 11)
def riffle(ls: list[int], out: int = True) -> list[int]:
    """perform a perfect riffle shuffle on each half of 'ls' list"""
    # set up range objects as iterators, then run them
    if not ls:
        return []
    n = len(ls)
    it1, it2 = iter(range(n//2)), iter(range(n//2, n + 1))
    if not out:
        it1, it2 = it2, it1  # swap the iterators around
    rv_ls = []
    for i in range(n//2):
        rv_ls.append(ls[next(it1)])
        rv_ls.append(ls[next(it2)])
    return rv_ls


# 4. Even the odds (pg 12)
def only_odd_digits(n: int) -> bool:
    """Problem 4: is every digit in n odd?"""
    return all([c in '13579' for c in str(n)])


# 5. Cyclops numbers (pg 13)
def is_cyclops(n: int) -> bool:
    # length has to be odd
    

# ENTRY POINT
if __name__ == '__main__':
    # ls = list(range(1, 9))
    ls = [0, 1]
    shuffled = riffle(ls)

    _ = 'STOP'


# EOF

