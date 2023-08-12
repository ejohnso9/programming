
"""
DESCRIPTION

--- Day 5: Doesn't He Have Intern-Elves For This? ---

PART I
=======
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


PART II
========
Realizing the error of his ways, Santa has switched to a better model of
determining whether a string is naughty or nice. None of the old rules
apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the
string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not
like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter
between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj)
and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that
repeats with one between, even though the letters used by each rule
overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat
with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one
between (odo), but no pair that appears twice.
How many strings are nice under these new rules?

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


def isNice1(s):
    if not hasThreeOrMoreVowels(s):
        return False

    if not hasDouble(s):
        return False

    if isNaughty(s):
        return False

    return True


def hasRepeatedPair(s):
    # print("s = '" + s + "'")
    for i in range(len(s) - 4 + 1):
        s2 = s[i: i + 2]
        # print("s2 = '" + s2 + "'")
        idx = s.find(s2, i + 2)
        if idx > -1:
            # print("found '%s' at index %d" % (s2, idx))
            # pdb.set_trace()
            return True

    return False


def hasOneThreeRepeat(s):
    return any([s[i] == s[i + 2] for i in range(len(s) - 2)])


def isNice2(s):
    # pdb.set_trace()
    if not hasRepeatedPair(s):
        return False

    if not hasOneThreeRepeat(s):
        return False

    return True


def getListOfStrings(filename):
    with open(filename, 'r') as fd:
        lines = fd.read().split(NL)
    
    return lines[:-2]


def main():

    lines = getListOfStrings(INPUT_FILE)

    # PART I
    nice_total = sum([1 for s in lines if isNice1(s)])
    print("PART I nice total is: ", nice_total)  # 258 is correct!

    # PART II
    nice_total = sum([1 for s in lines if isNice2(s)])
    print("PART II nice total is: ", nice_total)  # 53 is correct!
        


if __name__ == '__main__':
    main()
