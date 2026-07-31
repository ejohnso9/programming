#!/usr/bin/env python
# file: labs109.py
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 textwidth=100:

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
def domino_cycle(ls: list) -> bool:
    """
    Does the list of dominoes (2-tuples) form a valid loop of matching ends?
    """
    if ls == []:
        return True  # Degenerate case documented in problem statement
    inner_tf = all(ls[i][1] == ls[i+1][0] for i in range(len(ls) - 1))
    return inner_tf and ls[0][0] == ls[-1][1]


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


# 7. Colour trio (pg 15)  // passing on 2025Dec31
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
    
# 4. Lowest common dominator
def lowest_common_dominator(beta: list[int], gamma: list[int]) -> list[int]:
    from itertools import accumulate as acc

    return [max(b, g) for b, g in zip(acc(beta), acc(gamma))]


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


# 25. Square lamplighter
def square_lamps(n: int, flips: list[int]) -> int:
    """
    grid starts w/ all rows and cols OFF (0)
    positive ints in flips are rows being toggled
    negative ints in flips are cols being toggled

    Small example to motivate and reason out a more general solution:

    8x8 example (N = 8)

    flip: [-3, -7, 2, 4, 5]

    Let C be number of columns that end up ON
    Let R be number of rows that end up ON
    R = 3, C = 2

            O   O
            N   N    +-- count of cells ON
            v   v    v
          00100010   2
    ON -> 11011101   6
          00100010   2
    ON -> 11011101   6
    ON -> 11011101   6
          00100010   2
          00100010   2
          00100010   2
                     total = 3 * 6 + 2 * 5 = 28

    a quick Vim check:
        visually select the 0/1 grid
        :s/1//gn
        confirms count of 28

    As the instructions direct, we don't want to actually flip cells on and off in
    a big square grid. In fact, we don't need to care about individual cells at all.
    If I reduce the 'flips' array to two sets that are only storing keys where the
    row or column was flipped to 1 (ON):

      rows: {2, 4, 5}
      cols: {3, 7}

    There are just two kinds of rows:
    a) rows flipped ON:
       these have N - C cells ON: = 8 - 2 = 6
       count of ON rows: R = 3

    b) rows set OFF (not flipped ON)
       these have C cells ON: = 2
       count of OFF rows: N - R = 8 - 3 = 5

    Total ON cells:
    ((N - C) * R) + (C * (N - R))
    ((8 - 2) * 3) + (2 * (8 - 3))
    (6 * 3)       + (2 * 5)
    18 + 10
    28
    """

    rows = set()
    cols = set()
    for i in flips:
        if i < 0:
            s = cols  # manipulate the cols set
            i = -i    # positive index (for both)
        else:
            s = rows  # manipulate the rows set

        # just manipulate the set to keep only ON indices
        if i in s:
            s.remove(i)  # was already ON: turn it OFF
        else:
            s.add(i)  # was OFF: turn it ON

    # evaluate that one expression: ((N - C) * R) + (C * (N - R))
    R, C = len(rows), len(cols)
    N = n  # upper-case name alias
    return (N - C) * R + (C * (N - R))


# 63. Markov distance
def markov_distance(t1: tuple[int, int, int], t2: tuple[int, int, int]) -> int:
    """
    Compute the Markov distance between two given tuples.
    (looks like the "parent" tuple is always (a, b, 3 * a * b - c))
    """

    # make sure input tuples are in sorted order
    ls1 = sorted(t1)  # NB: this actually becomes list[int] (no need for tuple)
    ls2 = sorted(t2)  # NB: this actually becomes list[int] (no need for tuple)
    dist = 0  # i.e., count of parent climbs
    while ls1 != ls2:
        # climb upward on the tree one step for the largest tuple, reassign 3rd element of biggest tuple
        ls = ls1 if ls1[2] > ls2[2] else ls2
        a, b, c = ls
        ls[2] = 3 * a * b - c  # <- always replacing 3rd element
        ls.sort()
        dist += 1

    return dist


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

