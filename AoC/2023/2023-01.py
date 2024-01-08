#!/usr/bin/env python
# run on pythonanywhere.com @ Python version 3.9.5

r"""
Solution for: https://adventofcode.com/2023/day/1

DISCUSSION
    This problem seems like it should be nearly trivial.
In fact, it injects a rather nasty complication - surprising for a Day 1
problem. The issue is in overlap of characters of digit names -
somethign not covered in the examples.

This Reddit article basically says that values like "twone" should be
replaced with "21":
    https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2

I would call that poor problem design (or poor problem description, to
not specify the procedure to handle such overlaps). Once the procedure
for such name overlaps is known, I can just add it to my replacement
table.)

The Reddit article talks about the 'regex' module (which is outside the
Standard Python Library") taking a non-overlapping argument. My feeling
is:
    A) The 're' module *IS* within the Standard Python Library - why would
        you be using anything else?

    B) If you can solve a problem without involving regular expressions
        in the first place, that is likely to be a substantially more
        efficient solution (and less complicated, easier to understand,
        IMHO, generally).

Instead of replacements like: "85xtwone" -> "85xtw1"
others are suggsting things like: "85xtwone" -> "85xtwo1e"
Then you will still catch "two" if you are doing digit name replacements
in the order one, two, three, ... but then "two" needs to be replaced
with "t2o", etc. I dunno; this seems cutesy / cheesy / artificial to me.

I'm not sure if this overlap wrinkle was intentional to make Day 1
tough, but I suspect the issue was perfectly well known to Eric Wustl
since "xtwone3four" is actually in the example text, which perhaps
speaks to reading examples very, very closely and carefully, but it
still doesn't really spell out the expected procedure to handle such
overlapping text - one is left guessing at possible procedures to handle
such overlaps.

Before finding the Reddit article, I just searched my input puzzle text
for overlapping names:

possible overlaps:
    oneight:   *** several instances of this!
    threeight: NONE
    fiveight: NONE
    nineight: NONE
    twone:    *** several instances of this!
    sevenine: NONE
    eightwo:  *** several instances of this!
    eighthree: NONE

And then knew this was at the core of my unaccepted answer, but since I
wasn't solving this on same day of puzzle release, found the expected procedure
later (Jan 8th) via Google search.
Knowing that, I can simply replace: "twone" with "21", "eightwo" with "82", etc.
NB: those subs need to happen before single-digit subs!

I guess this is a very good lesson for dealing with overlapping string
patterns, but I still feel like that was unnecessarily evil for a Day 1
problem.
"""

# NB: I'm not playing code golf here. This is basically the opposite of
# code golf: it's bascially the way I would write production code
# (except perhaps a bit less documented, refactored, and polished than I
# would submit for final production code).


# Standard Python Library
import string
import sys


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = "2023-01.txt"
overlaps = ['oneight', 'twone', 'eightwo']
DIGIT_MAP = {
    'oneight': '18',
    'twone': '21',
    'eightwo': '82'
}
_ = "one two three four five six seven eight nine"
for i, name in enumerate(_.split()):
    DIGIT_MAP[name] = str(i + 1)


def words_to_digits(line):
    s = line
    for name, c in DIGIT_MAP.items():
        s = s.replace(name, c)
        
    return s


def getnum(line: str) -> int:
    f = words_to_digits
    digits = [c for c in list(f(line)) if c in string.digits]

    return int(digits[0] + digits[-1])


def main(filename):

    with open(filename, 'r') as fd:
        lines = [line.strip() for line in fd.readlines()]

    # I put an extra blank line on the end: strip it
    lines = lines[:1000]  # work with exactly 1000 lines
    data = [getnum(line) for line in lines]
    total1 = sum(data)

    # DEBUG cross-check
    total2 = 0
    for i, line in enumerate(lines):
        s = words_to_digits(lines[i])
        value = getnum(s)
        i_ls = [int(c) for c in list(s) if c in string.digits]
        d = data[i]  # value from the short way
        assert value == d
        if any([pat in line for pat in overlaps]):
            print(f'{i + 1}: total={total2}, {value}, "{line}", "{s}", {i_ls}')
        total2 += value

    print()
    print(f"for {len(lines)} lines, total1 = {total1}")
    print(f"total2 is: {total2}")
    # 55130 accepted for part 1 (2023Dec08)
    # 54495 rejected for part 2 (2024Jan08)
    # 54985 accepted for part 2 (2024Jan08)

    return 0  # normal exit code


# ENTRY POINT
if __name__ == '__main__':
    rc = main(INPUT_FILENAME)
    print(f"exit({rc})")

# EOF

