#!/usr/bin/env python

"""
DESCRIPTION
    solution to Kattis problem:
        https://open.kattis.com/problems/10kindsofpeople

THOUGHTS / DISCUSSION
    The solution rate on this problem is low, which is why I decided to try it.
    That probably stems from the fact that a straight recursive solution will
    eat up a bunch of memory and Python will quit (crash), even after this:

    sys.setrecursionlimit(100000)

    One can get the same effect by using a list like a data stack and
    simply iterating to process each argument put on our own "stack".
"""

import sys
from sys import stdin


def find(cur_row, cur_col, tgt_row, tgt_col, grid):
    stack = list()
    found = list()
    tgt_type = grid[tgt_row][tgt_col]
    stack.append((cur_row, cur_col))  # tuple

    # helper
    def look(row, col):
        if (row, col) not in found:
            found.append((row, col))
            stack.append((row, col))

    while stack:
        cur_row, cur_col = stack.pop()
        cur_type = grid[cur_row][cur_col]

        # is this the right cell type to continue search from?
        if cur_type != tgt_type:
            continue

        # did we find it?
        if cur_row == tgt_row and cur_col == tgt_col:
            return "decimal" if tgt_type == '1' else "binary"

        # look around (orthogonally)
        # TODO: AND (neighboring cell is of right type)
        left = cur_row - 1, cur_col
        if cur_row > 0:  # and isRightType(*left)
            look(*left)
        if cur_row < n_rows - 1:
            look(cur_row - 1, cur_col)
        if cur_col > 0:
            look(cur_row, cur_col - 1)
        if cur_col < n_cols - 1:
            look(cur_row, cur_col + 1)

    return "neither"


if __name__ == '__main__':
    rl = stdin.readline
    n_rows, n_cols = [int(w) for w in rl().split()]

    # load initial grid
    grid = [rl().strip() for i in range(n_rows)]
    for i in range(int(rl())):
        # use 0-based indices here
        r1, c1, r2, c2 = [int(w) - 1 for w in rl().split()]
        if grid[r1][c1] != grid[r2][c2]:
            print("neither")
        else:
            print(find(r1, c1, r2, c2, grid))
