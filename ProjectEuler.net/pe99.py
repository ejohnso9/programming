#!/usr/bin/env python
# file: pe99.py
# ProjectEuler.net Problem #99
# https://projecteuler.net/problem=99

# NB: I removed the data file. You can re-fetch it from here:
# https://projecteuler.net/resources/documents/0099_base_exp.txt

r"""
PROBLEM STATEMENT
------------------
Python operator: ** is exponentiation

Comparing two numbers written in index form like 2**11 and 3**7
is not difficult, as any calculator would confirm that
 2**11 = 2048 < 3**7 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much
more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K
text file containing one thousand lines with a base/exponent pair on
each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.



DISCUSSION
-----------
Just browsing over the file, most of the bases and exponent are 6-digit
numbers, with a few 4- and 5-digit numbers thrown in.

Taking a base 10 logarithim of a number is one way to reduce a numbers
size without really losing information. Manipulating only the base,
the relative size of two numbers treated the same will not change.

I *THINK* that's also true if I took the log of both the base and the
exponent.

I could also reduce these numbers by a constant.
For example, 519432 ** 525806
could be: 
    (1e-5 * 519432) ** (1e-5 * 525806)
    equivalently: 5.19432 ** 5.25806

    Mathematically, I'm not entirely confident this holds, but I *THINK*
it does, and a reasonable approach is to simply assume that it does,
find the maximum-value row, and submit that answer.

    If it is correct, I'm comfortable continuing to think that scaling
both base and exponent by a constant factor doesn't change the relative
ordering of (base ** exponent) numbers treated equivalently.


PLANNING / DESIGN
------------------
    Not much to it: iterate over the data, do the computation, keep
track of the row number we were on for a (base, exponent), compare each
row to the biggest seen.
    Print out the biggest row at the end.

"""


import sys

#
# GLOBAL DATA
#



def main(in_filename: str) -> int:

    # read in data
    with open(in_filename, 'r') as fd:
        lines = fd.readlines()

    max_line = 0
    max_value = 0
    for i, line in enumerate(lines):
        line_no = i + 1
        base, exp = [int(n) for n in line.split(',')]
        f = base ** exp
        if f > max_value:
            max_value = f
            max_line = line_no

    print(f"PE99 largest row is: {len(solutions)}")


# ENTRY POINT
if __name__ == '__main__':
    rc = main('0099_base_exp.txt')
    print("done.")
    print(f"sys.exit({rc})")
    sys.exit(rc)

# EOF
