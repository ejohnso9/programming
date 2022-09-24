
"""
DESCRIPTION
    Let me try to paraphrase the problem statement succintly:
    generate all the possible diagonals of a square matrix of ints as a
    list of lists of int.

    For Example:

    M = [ [1, 2],
          [3, 4], ]

    The answer is essentially this (as a Set: element order in the
    top-level list is immaterial but element order within the sublists
    should be preserved (i.e., ordered by row top-to-bottom)):

    [ [ 1 ], [ 2, 3 ], [ 4 ], [ 2 ], [ 1, 4 ], [ 3 ] ]
"""

def diagonal(matrix, rc_start, n_el, direction):
    """
    Function to generate a list of elements representing one diagonal,
    starting at (rc_start[0], rc_start[1]) and extending either down-left
    or down-right for 'n_el' elements.

    :param matrix: the NxN matrix to build a diagonal for
    :param start: 2-tuple of ints: the starting (row, col) element
    :param n_el: how many elements should be in this diagonal?
    :param direction: LEFT to iterate down and left, RIGHT to iterate down and right
    :return:
    """
    d_col = 1 if direction == 'R' else -1
    row, col = rc_start

    return [matrix[row + i][col + d_col * i] for i in range(n_el)]


def diagonals(matrix):
    """Build all the possible diagonals for the given square 'matrix' """
    diags_l = []  # RV
    n = len(matrix)

    # special branches for degenerate cases
    # (NB: Test suite seems to have arbitrary interpretations of these.)
    if n == 0:
        return []
    elif n == 1:
        # Logically, I guess you would have the same 1-element list twice
        return [[matrix[0][0]]]

    # add LEFT and RIGHT diagonals across top row
    for i in range(n):
        diags_l.append(diagonal(matrix, (0, i), i + 1, 'L'))
        diags_l.append(diagonal(matrix, (0, i), n - i, 'R'))

    # add the both diagonals down left or right column
    for i in range(n - 1):
        diags_l.append(diagonal(matrix, (i + 1, n - 1), n - i - 1, 'L'))
        diags_l.append(diagonal(matrix, (i + 1, 0), n - i - 1, 'R'))

    return diags_l


def main():
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    return diagonals(M)


if __name__ == '__main__':
    diags = main()
    print(sorted(diags))
