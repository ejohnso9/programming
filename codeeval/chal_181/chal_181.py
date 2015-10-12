#!/usr/bin/env python

import sys, pdb

"""
Solution for codeeval challenge #181 (GRONSFELD CIPHER)
https://www.codeeval.com/open_challenges/181/

AUTHOR: Erik Johnson

DISCUSSION:
"""

DATA = ' !"#$%&' + "'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        dig, letters = line.strip().split(';')
        digits = [int(c) for c in dig]
        n = len(digits)
        word = []
        for i, c in enumerate(letters):
            index = DATA.find(c)
            new_i = index - digits[i % n]
            if new_i < 0:
                new_i += len(DATA)
            c2 = DATA[new_i]
            word.append(c2)

        lines_out.append(''.join(word))

    print '\n'.join(lines_out)
