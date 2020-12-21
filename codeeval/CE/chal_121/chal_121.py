#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #121 (LOST IN TRANSLATION)
https://www.codeeval.com/open_challenges/121/

AUTHOR: Erik Johnson
DATE: 2015-NOV-16
"""

"""
def build_map(lines):
    d = {} # rv
    for i in range(3):
        enc = lines[i].rstrip()
        dec = lines[i + 3].rstrip()
        assert len(enc) == len(dec)
        for j in xrange(len(enc)):
            if enc[j] != ' ':
                d[enc[j]] = dec[j]

    return d
"""

XLATE_D = {
    'a': 'y',  'g': 'v',  'm': 'l',  's': 'n',
    'b': 'h',  'h': 'x',  'n': 'b',  't': 'w',
    'c': 'e',  'i': 'd',  'o': 'k',  'u': 'j',
    'd': 's',  'j': 'u',  'p': 'r',  'v': 'p',
    'e': 'o',  'k': 'i',  'q': 'z',  'w': 'f',
    'f': 'c',  'l': 'g',  'r': 't',  'x': 'm',

    'y': 'a', 'z': 'q', ' ': ' ',
}

if __name__ == "__main__":

    lines_out = []
    for line in open(sys.argv[1], 'r'):
        line = line.rstrip()
        lines_out.append(
            ''.join([XLATE_D[c] for c in line]))

    print '\n'.join(lines_out)
    sys.stdout.flush()
