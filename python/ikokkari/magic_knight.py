#!/usr/bin/env python
# file: magic_knight.py
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 textwidth=100:


# 19.The magic knight of Muhammad ibn Muhammad
def magic_knight(n: int, items: list[int]) -> list[tuple[int, int]]:
    """
    The problem description basically has up/down inverted from the way rows and columns would normally
    be rendered. That is, if you print a list-of-lists with element 0 first and then iterating rows upwards,
    the rows come out:
        row 1
        row 2
        ...
        row N

    If you say the upper-right (UR) corner is (n-1, n-1), this is essentially mathematical (X, Y) with X increasing
    upwards:
        row N
        ...
        row 2
        row 1

    I'm basically doing this in Excel coordinates with Row 1 at the top. It's the same thing, but my up/down is
    inverted from problem statement. Where the algorithm requires the knight to move "down 2 rows", I am still
    decreasing the row index by 2 but moving "up" 2 rows in the way one would normally iterate a printout of rows.

    The second thing to note is that in the expected result, what is given are (col, row) coordinates. This is also
    sort of challenging normal mathematical matrix indexing, but OK, you can think of that as (X, Y) in an X increases
    up, Y increases to right world. (I had assumed the given tuples were (row, col) as one would normally address
    a 2D matrix: but everything comes out "bass ackwards" when printing (row, col) tuples, of course.)

    SUGGESTION:
    A little discussion about notations and conventions in this problem I think would help students a lot.
    For me at least, I think this is more natural (matrix notation, list-of-lists, row printing ordering):

         0    1    2    3    4  cols ->
        --   --   --   --   --
    0 | .. | .. |  3 | .. | .. |
    1 |  5 | .. | .. | .. | .. |
    2 | .. | .. | .. |  2 | .. |
    3 | .. |  4 | .. | .. | .. |
    4 | .. | .. | .. | .. |  1 |   # move up 2, left 1
   rows
    |
    V

    Than this, mathematical axes:
    ^
    |
    X
    4 | .. | .. | .. | .. |  1 |   # move down 2, left 1
    3 | .. |  4 | .. | .. | .. |
    2 | .. | .. | .. |  2 | .. |
    1 |  5 | .. | .. | .. | .. |
    0 | .. | .. |  3 | .. | .. |
        --   --   --   --   --
         0    1    2    3    4  Y ->

    Making clear that the expected result is: (col, row) tuples and *NOT* (row, col) tuples
    will also help, but perhaps that was part of the intended lesson: to struggle with this
    a bit? I guess it becomes clear pretty quickly if you do a 5x5 by hand that element 10
    can't possibly be at (row=3, col=1) (4 is already there). After thinking on this a bit,
    maybe better to NOT say anything and let students figure this out on their own?
    """

    ROW, COL = 0, 1  # like symconsts for fields used in this func: tuple access

    # initialize grid (list of lists) and other stuff
    i = 1  # the integer we are putting into cells (also index of work being done)
    grid = [[0] * n for i in range(n)]
    work = []
    row_col = (n - 1, n - 1)  # start LR corner of "normal" grid

    def nextPosition(N: int, rc: tuple[int, int]) -> tuple[int, int]:
        """
        NB: refs outer 'grid', 'i' !!! (i.e., this is not strictly "functional")
        """

        while True:
            rc = (rc[ROW] - 2) % N, (rc[COL] - 1) % N  # 2 rows up, 1 col left
            if grid[rc[ROW]][rc[COL]] == 0:
                return rc
            else:
                # two steps left from occupied square
                return rc[ROW], (rc[COL] - 2) % N

    for i in range(n ** 2):
        idx_1 = i + 1
        grid[row_col[ROW]][row_col[COL]] = i + 1
        if idx_1 in items:
            work.append((row_col[COL], row_col[ROW]))
        row_col = nextPosition(n, row_col)

    return work

