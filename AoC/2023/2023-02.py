#!/usr/bin/env python
#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# run on pythonanywhere.com @ Python version 3.9.5

r"""
Solution for: https://adventofcode.com/2023/day/2

DISCUSSION
    Nearly trivial: just some simple text parsing and a little bit 
    of aggregration.

STRATEGY
    N/A

# NB: I'm not playing code golf here (though documentation may be
# somewhat lacking). This is basically the way I write production code.
"""



# Standard Python Library
import string
import sys


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = "2023-02.txt"
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


def load_lines():
    """
    a simple helper to read the input file, return a list of
    strings as lines (stripped on end, but unchanged at front)
    """

    if len(sys.argv) > 1:
        filename = sys.argv[1] 
    else:
        filename = INPUT_FILENAME

    with open(filename, 'r') as fd:
        lines = [line.rstrip() for line in fd.readlines()]

    return lines


def main():

    lines = load_lines()
    print(f"loaded {len(lines)} lines")


    return 0  # normal exit code


# ENTRY POINT
if __name__ == '__main__':
    rc = main()
    print(f"exit({rc})")

# EOF

