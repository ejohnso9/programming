#!/usr/bin/env python3

"""
DESCRIPTION
    https://open.kattis.com/contests/x4dmg8/problems/closingtheloop

AUTHOR
    Erik Johnson

HISTORY
    2020Dec19  Created
"""

import sys

# GLOBAL DATA
NL = '\n'


# Transpose
def T(lol):
    new_words = []
    for i in range(len(lol[0])):
        new_words.append(
            ''.join([w[i] for w in lol]))

    return new_words


def process(n_row, n_col, fd):

    lines = []
    for i in range(n_row):
        line = fd.readline().strip()
        lines.append(line)

    v_words = T(lines)
    # print(v_words)
    t_l = [(w.lower(), w) for w in v_words]
    t_l.sort()
    s_words = [t[1] for t in t_l]

    return T(s_words)


def output(answers):
    print(NL.join(
        [f'Case #{i+1}: {a}' for i, a in enumerate(answers)] ))


def main():
    fd = sys.stdin

    op_l = []
    while True:
        r, c = [int(s) for s in fd.readline().split()]
        if r == 0 and c == 0:
            break
        lol = process(r, c, fd)
        op_l.extend(lol)
        op_l.append('')

    # dump final output
    print(NL.join(op_l[:-1]))


if __name__ == '__main__':
    main()

