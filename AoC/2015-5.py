
"""
DESCRIPTION

--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty
or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or
aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx,
abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part
of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels
(u...i...o...), a double letter (...dd...), and none of the disallowed
substrings.
aaa is nice because it has at least three vowels and a double letter,
even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
    Day 3 of 2015: https://adventofcode.com/2015/day/3
    Elf directing Santa to houses on 2D infinite grid.
    DATA was manually embedded in this file.

"""


import sys
import pdb  # http://pymotw.com/2/pdb/


# GLOBAL DATA
NL = '\n'
VOWELS = 'aeiou'
NAUGHTY_PATS = "ab cd pq xy".split()

INPUT_FILE = '2015-5.input'



def hasThreeOrMoreVowels(s):
    return 3 <= sum([1 for c in list(s) if c in VOWELS])


def hasDouble(s):
    return any([s[i] == s[i + 1] for i in range(len(s) - 1)])


def isNaughty(s):
    for pat in NAUGHTY_PATS:
        index = s.find(pat)
        if index > -1:
            return True

    return False


def isNice(s):
    if not hasThreeOrMoreVowels(s):
        return False

    if not hasDouble(s):
        return False

    if isNaughty(s):
        return False

    return True


def getListOfStrings(filename):
    with open(filename, 'r') as fd:
        lines = fd.read().split(NL)
    
    return lines[:-2]


def main():

    lines = getListOfStrings(INPUT_FILE)

    # init
    nice_total = sum([1 for s in lines if isNice(s)])
    print("nice total is: ", nice_total)  # 258 is correct!
        


if __name__ == '__main__':
    main()
