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
    return all(items[i] < items[i + 1] for i in range(len(items) - 1))


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
    """predicate: middle digit 0, no other 0 digits in n"""
    s = str(n)
    if len(s) % 2 != 1:
        return False
    i = len(s) // 2
    return s[i] == '0' and '0' not in s[:i] + s[i+1:]


    
#---------------------------------------------------------------------------------------------------
# Problem Set #3:  
# https://github.com/ikokkari/PythonProblems/blob/main/Third%20Python%20Problem%20Collection.pdf
#---------------------------------------------------------------------------------------------------

def baum_sweet(n: int) -> int:
    """
    1 if no odd-length 0 runs in the binary rep. of n, else 0
    NB: switching var names from problem statement: n -> num
    """

    count = 0
    rep = bin(n)[2:]  # the binary representation string: e.g., "100101"
    for i in range(len(rep)):
        if rep[i] == '0':
            count += 1
        elif rep[i] == '1': 
            # did we just switch back to '1's from an odd sequence of '0'?
            if count > 0 and count % 2:
                return 0  # False: not Baum-Sweet (i.e., has odd seq. of 0)
            count = 0

    return 1 if count % 2 == 0 else 0


# ENTRY POINT
if __name__ == '__main__':
    # ls = list(range(1, 9))
    # ls = [0, 1]
    # shuffled = riffle(ls)
    # _ = 'STOP'

    # TEST: 5. Cyclops numbers
    # n Expected result
    f = is_cyclops
    test_data = [
        (0, True),
        (101, True),
        (98053, True),
        (777888999, False),
        (1056, False),
        (675409820, False),
    ]
    for n, exp in test_data:
        print(f"f({n}) is {f(n)}")
        # assert f(n) == tf 


# EOF

