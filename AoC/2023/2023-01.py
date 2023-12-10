#!/usr/bin/env python
# run on pythonanywhere.com @ Python version 3.9.5

r"""
Solution for: https://adventofcode.com/2023/day/1

DISCUSSION
    This should be almost trivial.

STRATEGY
    Just need some basic string processing functions and a sum() call.
"""

# NB: I'm not playing code golf here (though documentation may be
# lacking). This is basically the way I write production code.


# Standard Python Library
import string
import sys


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = "2023-01_input.txt"
DIGIT_MAP = {
    word: str(i + 1)
    for i, word in enumerate("one two three four five six seven eight nine".split())
}


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
    for i in range(len(lines)):
        line = lines[i]
        s = words_to_digits(lines[i])
        value = getnum(s)
        i_ls = [int(c) for c in list(s) if c in string.digits]
        d = data[i]  # value from the short way
        assert value == d
        print(f'{i + 1}: total={total2}, {value}, "{line}", "{s}", {i_ls}')
        total2 += value

    print()
    print(f"for {len(lines)} lines, total1 = {total1}")
    print(f"total2 is: {total2}")
    # 55130 accepted for part 1 (2023Dec08)

    return 0  # normal exit code


# ENTRY POINT
if __name__ == '__main__':
    rc = main(INPUT_FILENAME)
    print(f"exit({rc})")

# EOF

