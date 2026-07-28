#!/usr/bin/env python
# file: labs109.py

# 🕊♡ In Memory of Michael Hedges 🎶 🎸


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

# My previous version from 2025
# 6. Domino cycle (pg 14) //passing on 2025Dec31
# def domino_cycle(ls: list) -> bool:
#     """
#     Does the list of dominoes (2-tuples) form a valid loop of matching ends?
#     """
#     if ls == []:
#         return True  # Degenerate case documented in problem statement
#     inner_tf = all(ls[i][1] == ls[i+1][0] for i in range(len(ls) - 1))
#     return inner_tf and ls[0][0] == ls[-1][1]

# 6. Domino cycle (pg 14)
def domino_cycle(tiles) -> bool:
    """dominoes (2-tuples) form a loop
    (0 tiles: True, 1 tile: if ends match)
    """

    # degenerate cases
    if tiles == []:
        return True  # empty list taken as a cycle

    if len(tiles) == 1:
        t = tiles[0]
        return t[0] == t[1]  # 1-tile cycle if ends match

    # check the ends: 1st LH end has to match last RH end
    if tiles[0][0] != tiles[-1][1]:
        return False

    # check all the inner pairings
    return all(tiles[i][1] == tiles[i+1][0] for i in range(len(tiles) - 1))


# 7. Colour trio (pg 15)  //passing on 2025Dec31
def colour_trio(colors: str) -> str:
    """pairwise reduction to string of size 1 by mix() function"""

    def mix(c1: str, c2: str) -> str:
        if c1 == c2:
            return c1
        for c in list('ryb'):
            if c not in [c1, c2]:
                return c

    def mixDown(ls: list) -> list:
        return ''.join([mix(ls[i], ls[i + 1]) for i in range(len(ls) - 1)])

    while len(colors) > 1:
        colors = mixDown(colors)

    return colors


#---------------------------------------------------------------------------------------------------
# Problem Set #2:  
# https://github.com/ikokkari/PythonProblems/blob/main/Additional%20Python%20Problems.pdf
#---------------------------------------------------------------------------------------------------
    
# 8. Word positions  (the whole function is the more "production-like" defn)
def word_positions(sentence: str, word: str) -> list[str]:
    """list of word indices matching 'word'

    As the challenge one-liner:
        def word_positions(sentence, word): return [i for i, w in enumerate(sentence.split()) if w == word]
    or maybe:
        word_positions = lambda s, wd: [i for i, w in enumerate(s.split()) if w == wd]
    """

    return [i for i, w in enumerate(sentence.split()) if w == word]


# 13. Powertrain
def powertrain(n: int) -> int:
    """John Conway's "power train" function:
    Iterate until n becomes a single digit number, raising each odd
    digit to the power of the following digit and multiplying each
    term together.

    Should n contain an odd number of digits, the power of the last
    digit can be taken as 0.

    For example, for the 5-digit number: abcde, this becomes
    a**b * c**d (times e**0, which is 1 => just ignore e)

    The value of this function is the number of iterations required to
    reduce n to a single-digit number.
    """

    import math


    count = 0  # number of loop iterations
    while n > 10:
        loi = [int(c) for c in str(n)]  # list of ints (in [0, 9])
        # NB: any odd digit just sort of "disappears" in the len(loi) // 2 operation
        n = math.prod([loi[2 * i] ** loi[2 * i + 1] for i in range(len(loi) // 2)])
        count += 1

    return count

    

#---------------------------------------------------------------------------------------------------
# Problem Set #3:  
# https://github.com/ikokkari/PythonProblems/blob/main/Third%20Python%20Problem%20Collection.pdf
#---------------------------------------------------------------------------------------------------

# 5. Baum-Sweet cycle
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

