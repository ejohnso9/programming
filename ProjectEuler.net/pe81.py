#!/usr/bin/env python
# file: pe81.py

"""
# sample data: '_' indicates min path: 2427
DATA = [
    [_131,  673,  234,  103, 1566],
    [_201, _ 96, _342,  965, 1548],
    [ 630,  803, _746, _422, 1398],
    [ 537,  699,  497, _121, 1287],
    [ 805,  732,  524, _ 37, _331],
]

DISCUSSION
    My first throughts were to try to generate all the possible paths.
To get from top row to bottom row I will have to go down 4 times.
To get from left column to right, I will have to go right 4 times.

    For a 5x5 matrix that basically amounts to all the permutations of
"DDDDRRRR", where 'D' means go down, 'R' means go right. "DDDDRRRR" is
the path going down the left hand side, then across bottom row.

    Generating all possible strings of 4 'D' and 4 'R' is parhaps a bit
tricky. I had figured out how to do it by generating permutations of the
integers 0 - (N-1), using itertools.permutations, then referencing my
array of half 'D', half 'R'.

    The problem with that is that a list of the permutations of '01234'
is 5! long. That's 120. Sure, no problem. 80! is a 117-digit monster. We
cannot visit such permutations even for a microsecond - that problem is
completely intractable. Iterating 1000 permutations per microsecond, if
I could, doesn't change the intractability at all.

    That's when I knew that generating paths cannot be the approach.
So, what it a path cost? Well, from upper left corner, it's 131 plus 201
if I go down, or 131 + 673 if I go right. So, why not just record those
values?  Then the cost at M[1][1] is the cost of itself plus the smaller
of: cell above it, or the cell to the left.

    The top row cells for index > 0 are themselves plus the sum of the
cells to the left, and similarly the cells down the left side are
themselves plus the sum of the cells above them.

    We can proceed doing this on the second row and second column (row
index = 1, column index = 1), and so on. After this has been done on N-1
rows and columns, the cost of the lower right cell is itself, plus the
minimum of: (M[N-1][N-2], M[N-2][N-1]). (That is, in the 5x5 example,
cost(M[4][4]) is min(cost(M[4][3]), cost(M[3][4])), the two cells above
and left of the lower-right corner.)

    This is something like: 2 * (79 + 78 + 77 + ... + 1)
or 6320 iterations: something on the order of 10^4 instead of 10^117.
That's doable "in the blink of an eye".
"""


from copy import copy
from pathlib import Path
import sys


# sample data given in the problem: min path should be: 2427
N = 5
DATA = [
    [131, 673, 234, 103, 1566],
    [201,  96, 342, 965, 1548],
    [630, 803, 746, 422, 1398],
    [537, 699, 497, 121, 1287],
    [805, 732, 524,  37,  331],
]


def transformMatrix(M: list) -> None:
    """walk through the cells, setting path values"""

    # special loop for top row, left column
    for i in range(1, N):
        M[0][i] += M[0][i-1]  # top row
        M[i][0] += M[i-1][0]  # left column

    for i in range(1, N):
        # top row
        row = i
        for col in range(i, N):
            M[row][col] += min(M[row][col-1], M[row-1][col])

        # left column
        col = i
        for row in range(i + 1, N):
            M[row][col] += min(M[row][col-1], M[row-1][col])

    return


def main(input_file: str) -> int:
    # DEBUG
    # path_values = [131, 201, 96, 342, 746, 422, 121, 37, 331]
    # print(f"sum(path_values) = {sum(path_values)}")  # 2427

    # read in data file
    in_path = Path(input_file)
    assert in_path.is_file()
    with open(in_path, 'r') as fd:
        lines = fd.readlines()

    matrix = []
    for line in lines:
        loi = [int(w) for w in line.split(',')]
        matrix.append(loi)
    global N
    N = len(matrix)

    # print(matrix)
    # M = DATA
    M = copy(matrix)

    # do the computing
    transformMatrix(M)
    # print(M)

    # solved:
    answer = M[N-1][N-1]
    print(f"M[{N-1}][{N-1}] = {answer}")  # 427337

    # on 2024Jul31:
    """
    Congratulations, the answer you gave to problem 81 is correct.

    You are the 36962nd person to have solved this problem.

    This problem has a difficulty rating of 10%. The highest difficulty rating you have solved so far is 25%.
    """

    return 0  # normal main() exit



if __name__ == '__main__':

    # read input data file
    filename = 'pe81_matrix.txt'

    rc = main(filename)
    print("done.")
    print(f"sys.exit({rc})")
    sys.exit(rc)

# EOF
