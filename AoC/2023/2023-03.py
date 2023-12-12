#!/usr/bin/env python

#                                                                                                  1         1         1
#        1         2         3         4         5         6         7         8         9         0         1         2
#23456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
# run on pythonanywhere.com @ Python version 3.9.5

r"""
Solution for: https://adventofcode.com/2023/day/3

DISCUSSION
    This is basically square matrix processing, except a "number" can span
several cells. Here's an arbitrarily-sized chunk from the upper LH corner
of my input file:

...........................775.651..
......240...................*.....-.
.485...+............437......906....
..........917.......&....146........
722...323.-................./...410.
.....*..........................*...
....370..$....639.748.......*...467.
........984....*.....*...782........
...............57..433.........390..
379..................../.........*..
...*..-......82.......167...936.17..

    So, for example, on line 1, scan (or .index()) down until you hit "775". That starts in the 28th column and
covers columns: 28 through 30. Once I see the '.' in column 31, I know the extent of the number. There's a "ring" of
cells around that, but in this case that "ring" doesn't extend onto the previous line, as it will for all other lines.
If there is a "symbol" in that ring, add the number to the list, else we're done processing "775".

STRATEGY
    There's a few special cases for processing numbers that are on the first or last line, and numbers that start
on the first column or end on the last column. Generally, read a list of strings, then process strings a line at
a time. Identify the bounds of a numeric run, then look for an adjacent symbol. If one is found, add the number to
a list. If not, skip the number and go on to find the bounds of the next numeric run. Continue through the last line,
then print the sum of the numbers in the list.

NB: I'm not playing code golf, here: some people want to show they are "clever" by doing various AoC problems as a
form of code golf. That's fine - it's good that they can do that. My goal here is to create working examples of
original code where organization, understandability, flexibility, changeability, and a reasonable balance of various
other "-ilities" far outweighs being "clever".

Performance is generally of little to no concern: squeezing a few milliseconds out of code by creating one run-on
block to avoid any function calls is of little or no benefit in this context (IMHO). Getting stuff organized into
small, understandable chunks (functions) is of great benefit (IMHO, a problem decomposed into small, well-named
functions in itself goes a long ways towards the sort of flexible, understandable solutions a company wants to
invest in and keep).

This is code written the same way I would (and do!) write production code for paying customers.
"""


# Standard Python Library
import string
import sys


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = "2023-03.txt"


def load_lines():
    """
    a simple helper to read the input file, return a list of strings as lines
    ('\n' (and any otehr whitespace) stripped from end, but unchanged at front)
    """

    if len(sys.argv) > 1:
        # NB: this is for IDE debug environment.
        # usually, 'python' will be in sys.argv[0]
        filename = sys.argv[0] 
    else:
        filename = INPUT_FILENAME

    with open(filename, 'r') as fd:
        lines = fd.readlines()

    return [line.rstrip() for line in lines]


def get_line_nums(line: str) -> list[tuple]:
    """
    Parse out where the numbers are (col index they start on start).

    @param lines: list of strings from input file
    @return: list of: (part_num, start_col)
        e.g., for 1st num on 1st line of example, the 1st list element would be:
            (775, 28)  # "775" found in col 28 (caller can see len("775") is 3)
            NB: "775" not yet an int, but run of digit chars
    """

    # TODO: this would probably also be a good candidate for using REGEXPs. This is the way I first thought about
    #   the problem; would be a good opportunity to measure how much slower REGEXP processing really is.

    pn_ls = list()  # RV: list of numbers seen on line w/ column index (list of 2-tuples)

    # walk the string, manipulate state for 4 cases:
    #   CASE 1: in_digit_run, next char is digit (continue in run)
    #   CASE 2: in_digit_run, next char is not digit (ending digit run)
    #   CASE 3: not in_digit_run, next char is digit (starting digit run)
    #   CASE 4: not in_digit_run, next char not digit (continue outside run)
    for i, c in enumerate(line):
        is_digit = c in string.digits
        if i == 0:  # init
            in_digit_run = line[0] in string.digits
            count = int(in_digit_run)
            col_start = 0
            continue

        # next char, being in a digit run
        if in_digit_run:
            if is_digit:  # CASE 1: continue in digit run
                count += 1
            else:
                # CASE 2: exiting a digit run
                s = line[col_start:col_start + count]
                pn_ls.append((s, col_start))
                count = 0
                in_digit_run = False

        # next char, NOT in a digit run
        else:
            if is_digit:  # CASE 3: start new digit run
                col_start = i
                count = 1
                in_digit_run = True
            # else: CASE 4: NOOP: continue (outside of a digit run)

    # special case for last char
    if in_digit_run:
        s = line[col_start:]
        pn_ls.append((s, col_start))

    # RV: list of numbers seen on line w/ column index (list of 2-tuples)
    return pn_ls  # (numeric string, col_index)


def is_engine_num(pn: str, col_i: int, line_no: int, lines: list[str], symbols: list[str]) -> bool:
    """

    @param pn: part number: a digit run found on a line (starting in column...)
    @param col_i: 0-based index of where 'pn' was found
    @param line_no:
    @param lines:
    @param symbols:
    @return:
    """

    line = lines[line_no]

    # slice start, end boundaries
    start = col_i - 1 if col_i > 0 else 0
    i = col_i + len(pn)  # provisional end slice index
    last_line_index = len(lines[line_no]) - 1
    end = i if i < last_line_index else i - 1

    # previous line: do we have a symbol in the range?
    if line_no > 0:
        prev_line = lines[line_no - 1]
        slice_s = prev_line[start:end + 1]
        if any([c in symbols for c in slice_s]):
            return True

    # on the line: symbol 1 char before hit index or 1 char after end of number?
    c_before, c_after = line[start], line[end]
    if any([c in symbols for c in [c_before, c_after]]):
        return True

    # special case for last line
    if line_no < len(lines) - 1:
        next_line = lines[line_no + 1]
        slice_s = next_line[start:end + 1]
        if any([c in symbols for c in slice_s]):
            return True

    return False


def process_lines(lines: list[str], symbols: list[str]) -> list[int]:
    engine_nums = list()
    for line_no, line in enumerate(lines):
        pns = get_line_nums(line)
        for pn, col_i in pns:
            if is_engine_num(pn, col_i, line_no, lines, symbols):
                engine_nums.append(int(pn))

    return engine_nums


def main():

    # read the data file
    lines = load_lines()
    # print(f"loaded {len(lines)} lines")

    # what are the symbols? (digits are not symbols, and neither is '.', the rest are)
    symbols = set()
    for line in lines:
        [symbols.update(c) for c in list(line)]

    # remove what's known to not be a "symbol"
    symbols.discard('.')
    for dig in string.digits:
        symbols.discard(dig)

    # DEBUG
    get_line_nums(lines[0])

    # get the list of part numbers (pns)
    engine_nums = process_lines(lines, symbols)

    # Part 1: Yay! 553079 accepted first try @ 2023Dec10T1724
    print(f"Part 1: {sum(engine_nums)}")

    # Part 2:
    print(f'Part 2: {"not implemented"}')

    return 0  # normal exit code


# ENTRY POINT
if __name__ == '__main__':
    rc = main()
    print(f"exit({rc}).")

# EOF
