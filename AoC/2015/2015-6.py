#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

"""
DESCRIPTION

--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house
decorating contest year after year, you've decided to deploy one million
lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has
mailed you instructions on how to display the ideal lighting
configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the
lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The
instructions include whether to turn on, turn off, or toggle various
inclusive ranges given as coordinate pairs. Each coordinate pair
represents opposite corners of a rectangle, inclusive; a coordinate pair
like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The
lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your
lights by doing the instructions Santa sent you in order.

For example:

    - turn on 0,0 through 999,999 would turn on (or leave on) every light.

    - toggle 0,0 through 999,0 would toggle the first line of 1000
      lights, turning off the ones that were on, and turning on the ones
      that were off.

    - turn off 499,499 through 500,500 would turn off (or
      leave off) the middle four lights. After following the
      instructions, how many lights are lit?

STRATEGY:
    I'm just going to use a big dict, with keys like "0,499".
    Parse what kind of message it is:
        * toggle
        * turn on
        * turn off
    and just iterate over a couple of loops, then use a dict filter to
    apply a count function. Simple.

    Regular Expressions seem well suited here, but things are not really
    complex enough to warrant them. They are "nifty" and "handy" but
    also tend to be slow. I suppose this would be a good framework in
    which to measure the performance under an RE and non_RE solution.

    Just doing the non-RE solution for now...
    (I'm not competing against others on performance, otherwise I would
    want to optimize run time.)

DISCUSSION
    You'll have to check the git logs to beleive this, but I'm feeling
    pretty happy about seeing Part 2 after having solved Part I. The
    code change is almost trivial. I believe that is the benefit of
    having a decent design in the first place.
"""


import sys
import pdb  # http://pymotw.com/2/pdb/


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = '2015-6.input'
OP_VALUES = ['OFF', 'ON', 'TOGGLE']
OP_OFF, OP_ON, OP_TOGGLE = OP_VALUES
OP_PATTERNS = ["turn off ", "turn on ", "toggle "]


def getRowColBoundaries(text):
    p1, p2 = [s.strip() for s in text.split('through')]
    rs, cs = [s.strip() for s in p1.strip().split(',')]
    re, ce = [s.strip() for s in p2.strip().split(',')]
    return [int(s) for s in [rs, cs, re, ce]]


def iterate(op, onOff_d, row_start, col_start, row_end, col_end):
    for row_i in range(row_start, row_end + 1): 
        for col_i in range(col_start, col_end + 1): 
            key = f"{row_i},{col_i}"
            # print("key:", key)
            if op == OP_OFF:
                value = onOff_d[key]
                onOff_d[key] = value - 1 if value > 0 else 0
            elif op == OP_ON:
                onOff_d[key] += 1
            elif op == OP_TOGGLE:
                # Part 1: onOff_d[key] = not onOff_d[key]
                onOff_d[key] += 2


def main():
    # the lights On/Off dict: init OFF
    onOff_d = {}
    for r in range(1000):
        for c in range(1000):
            onOff_d[f"{r},{c}"] = 0  # OFF

    # read the data to process
    lines = open(INPUT_FILENAME, 'r').readlines()
    # this TEST line should turn on 4 bulbs
    # lines = ["toggle 499,499 through 500,500"]

    # process each line of input
    for line in lines:
        for i, pat in enumerate(OP_PATTERNS):
            if line.startswith(pat):
                op = OP_VALUES[i]
                rest  = line[len(pat):]
                # [rowStart, colStart, rowEnd, colEnd]
                rcArgs_l = getRowColBoundaries(rest)
                # print(rcArgs_l)
                iterate(op, onOff_d, *rcArgs_l)

    # count what's turned on
    onCount = sum([v for k,v in onOff_d.items() if v > 0])
    print(f"onCount is: {onCount}")

    # takes something like 15-20 sec
    # 400410 verfied as correct answer on 2022Jul25

    # Part 2: onCount is: 15343601  # verified correct @ 2022Jul25


if __name__ == '__main__':
    main()


# EOF

