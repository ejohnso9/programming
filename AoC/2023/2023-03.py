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

    After solving part 1, I decided I wanted to start to develop a library of functions that may be useful towards
this type of program (which is common both here and at other programming sites). So fro examplek, get a list of adjacent
cells given the (row, col) of some cell. Cells in the middle will have 8 neighbors, cells in corners only 3, and cells
on edges have 5. This is general pattern that comes up over and over again. It is functionality that can be implemented\
separate from whatever processing is specific to the adjacent cells.

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
__MATRIX__ = None  # inited in main()


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


def findChar(char_to_find: str, matrix=None) -> list:
    """
    Find all occurrences of 'char_to_find', return a list of tuples: ((row, col), value)
    """

    found_chars_l = list()  # RV
    m = matrix if matrix else __MATRIX__
    for row, line in enumerate(m):
        for col, c in enumerate(list(line)):
            if c == char_to_find:
                found_chars_l.append((row, col))

    return found_chars_l


def getAdjacencyList(row: int, col: int, values=False, matrix=None) -> list[tuple]:
    """
    Given row and col indices, return a list of (row, col) tuples that are adjacent (including diagonally), assuming
    we are talking about a square matrix of rows of columns (list-of-lists and list-of-strings work identically).

    TODO: add option for only orthogonally adjacent
    """

    ls = list()  # RV

    m = matrix if matrix else __MATRIX__
    n_rows = len(m)
    n_cols = len(m[0])

    # to aid debugging, these are built in LtoR, TOP to BOTTOM order
    if row > 0:  # we have a previous row
        r = row - 1

        # column to the left
        if col > 0:
            c = col - 1
            t = (r, c, m[r][c]) if values else (r, c)
            ls.append(t)

        # same column (cell above)
        ls.append((r, col, m[r][col]) if values else (r, col))

        # column to the right
        if col < n_cols - 1:
            c = col + 1
            t = (r, c, m[r][c]) if values else (r, c)
            ls.append(t)

    # always have same row
    r = row
    if col > 0:
        c = col - 1
        ls.append((r, c, m[r][c]) if values else (r, c))
    if col < n_cols - 1:
        c = col + 1
        ls.append((r, c, m[r][c]) if values else (r, c))

    # next row down
    if row < n_rows - 1:  # we have a next row
        r = row + 1

        # column to the left
        if col > 0:
            c = col - 1
            ls.append((r, c, m[r][c]) if values else (r, c))

        # same column
        c = col
        ls.append((r, c, m[r][c]) if values else (r, c))

        # column to the right
        if col < n_cols - 1:
            c = col + 1
            ls.append((r, c, m[r][c]) if values else (r, c))

    return ls  # cells adjacent to (row, col) as: [(r0, c0), (r1, c1), ... ]

def getIntAt(row, col, matrix=None) -> int:
    """
    Return the int where (row,col) is one of the cells within the string.
    """
    m = matrix if matrix else __MATRIX__
    line0 = m[0]
    c = m[row][col]
    if c not in string.digits:
        raise ValueError(f"char at ({row}, {col}), {c} is not a digit.")

    # scan left
    _col = col
    while 0 <= _col:
        if m[row][_col] not in string.digits:
            break
        _col -= 1
    left = _col + 1  # first index in the digit string

    # scan right
    _col = col
    while _col < len(line0):  # strictly less b/c of comparison directly to col count
        if m[row][_col] not in string.digits:
            break
        _col += 1
    right = _col - 1  # last index in the digit string

    return int(m[row][left:right + 1])


def isGear(row, col, matrix=None) -> int:
    """
    If there are 2 PNs adjacent to the arg (row, col), then I will return the gear ratio: one PN time the other.
    If there are not 2 adjacent PNs, I will return None.

    Implementation is a bit tricky here...
    There are a few ways digit strings can appear around a '*', some of which imply separate numbers, some
    of which do not. Examples:

    6 adjacent digits, 2 parts:    3 adjacent digits, but only 1 part
        .123.                          .123.
        ..*..                          ..*..
        .790.                          .....

    3 adjacent digits, 1 part:     2 adjacent digits, 1 part
        .123.                          123..
        ..*..                          ..*..
        .....                          .....

    * There are other arrangements not shown here...
    * I'm assuming there is never a case of more than two separate PNs adjacent to a gear.
    * If adjacent digits appear on more than one line, I'm assuming that's a gear.

    The other two valid cases would then be:
        XD.DX      .....
        ..*..      ..*..
        .....      XD.DX

    Where X is either a digit or not - I didn't analyze it, but I can see two digit part numbers and at least
    one instance of a one-digit part number.
    """

    m = matrix if matrix else __MATRIX__
    adj_cells = getAdjacencyList(row, col, values=True)
    adj_digits = [t for t in adj_cells if t[2] in string.digits]
    # should be digits on just 1 or 2

    # digits on more than one row?
    row_values = list(set(r for r, c, v in adj_digits))
    assert len(row_values) < 3  # just make sure my assumption is not wrong
    if len(row_values) > 1:
        # get the int for the first row value (using the first digits on that row)
        first_row = row_values[0]
        row, col, _ = [t for t in adj_digits if t[0] == first_row][0]  # one of the digits happens to be first
        i1 = getIntAt(row, col)
        second_row = row_values[1]
        row, col, _ = [t for t in adj_digits if t[0] == second_row][0]  # one of the digits, as above
        i2 = getIntAt(row, col)
        return i1 * i2

    # else: all the digits must be on the same row! (which we essentially know)
    # NB: could be left and right on same row as '*'!
    _row = row_values[0]
    # NB: the center must be '.' or the '*' itself to separate two numbers
    if m[_row][col] in '.*':
        # the left and right chars on the row
        c_left = m[_row][col - 1]
        c_right = m[_row][col + 1]
        if all([c in string.digits for c in (c_left, c_right)]):
            i1 = getIntAt(_row, col - 1)
            i2 = getIntAt(_row, col + 1)
            return i1 * i2

    return None  # arg (row, col) not actually a gear


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
    global __MATRIX__  # the default data structure other API will access (if not explicitly passed)
    __MATRIX__ = lines
    # print(f"loaded {len(lines)} lines")

    # DEBUG testing
    # adj_ls = getAdjacencyList(0, 0)
    # adj_ls = getAdjacencyList(1, 6, values=True)
    # stars = findChar('*')
    # i = getIntAt(12, 137)  # 515 @end of row 13 (text index)
    # i = getIntAt(9, 0)  # 379 @start of row 10 (text index)

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
    #   2.1 find all the stars ('*'),
    #   2.2 check each for actually being a gear (func return None when it is not),
    #   2.3 build a list of all the gear ratios
    stars = findChar('*')
    ratios = list()
    for row, col in stars:
        ratio = isGear(row, col)  # int ratio or None if that's not a gear
        if ratio:
            ratios.append(ratio)

    # OMG!!! I can hardly believe I hit this first try, too!
    # 84363105 accepted @ 2023Dec12T18:02
    print(f'Part 2: {sum(ratios)}')

    return 0  # normal exit code


# ENTRY POINT
if __name__ == '__main__':
    rc = main()
    print(f"exit({rc}).")

# EOF
