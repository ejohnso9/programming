#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #131  (SPLIT THE NUMBER)
https://www.codeeval.com/open_challenges/131/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":

    out_lines = []
    for line in open(sys.argv[1], 'r'):
        line = line.rstrip()
        i_s, s = line.split()
        index = s.find('+')
        if index > 0:
            i = int(i_s[:index]) + int(i_s[index:])
        else:
            index = s.find('-')
            i = int(i_s[:index]) - int(i_s[index:])

        out_lines.append(str(i))
        
    print '\n'.join(out_lines)

