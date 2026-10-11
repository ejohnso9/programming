#!/usr/bin/env python
# file: count_unicolour_rectangles.py
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 textwidth=100:


"""
DESCRIPTION:
    module for 1 function: first_fit_bin_packing()


AUTHOR:
    Erik Johnson: ejohnso9@earthlink.net

HISTORY
    2026Oct08 
"""


# --------------------------------------------------------------------------------------------------
# Problem Set #2:  
# https://github.com/ikokkari/PythonProblems/blob/main/Additional%20Python%20Problems.pdf
# --------------------------------------------------------------------------------------------------
    
# 22. Count monochromatic rectangles
# NB: naming discrepancy here
def count_unicolour_rectangles(grid: list[str]) -> int:
    """
    Count of how many rectilinear rectangles have all 4 corners same color.
    """

    count: int = 0
    nrows, ncols = len(grid), len(grid[0])  # width, height

    # functional: no inner refs
    def findRowsBelow(grid: list[str], row_i: int, col_i: int) -> list[int]:
        """
        Let c be the color at grid[row_i][col_i]
        Build list of row indices below col_i that are same color, c, at (r, col_i), r > row_i

        :param row_i: 0-based row index
        :param col_i: 0-based column index
        :return: row indices > row_i with
        """

        c = grid[row_i][col_i]  # color @ UL corner
        return [r for r in range(row_i + 1, nrows) if grid(r, col_i) == c]

    # scan upper left corners from (0, 0) to (nrows - 2, ncols - 2)
    for r1 in range(nrows - 1):
        for c1 in range(ncols - 1):
            color = grid[r1][c1]  # color @ UL corner

            # scan down for row below UL corner w/ same color
            for r2 in range(r1 + 1, nrows):
                if grid[r2][c1] != color:
                    continue

                # scan to right for cols w/ same color
                for c2 in range(c1 + 1, ncols):
                    if grid[r1][c2] != color:
                        continue

                    # now, cell at: (r2, c2) either matches other 3 corners or not
                    if grid[r2][c2] == color:
                        count += 1
                        # print(f"({r1}, {c1}), ({r2}, {c1}), ({r1}, {c2}), ({r2}, {c2})")
                        # print(f"({row_i}, {col_i})", end=' ')

    return count


# ENTRY POINT
if __name__ == '__main__':

    # This module just defines one function (and tests 2nd example).

    # TEST DATA (from the problem statement)
    TEST_DATA = [
        # grid 1: count = 1
        (['aba',
          'ccc',
          'ada'], 1),

        # grid 2: count = 5
        (['bbbbccba',
          'cdacaabc',
          'acdcdcdc',
          'cddacdab',
          'cbaaaabd'], 5),
    ]

    f = count_unicolour_rectangles  # the function under test
    grid, exp = (TEST_DATA[1][i] for i in (0, 1))
    assert f(grid) == exp


# EOF
