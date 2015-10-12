#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #167  (READ MORE)
https://www.codeeval.com/open_challenges/155/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":

    out_lines = []
    for line in open(sys.argv[1], 'r'):
        line = line.rstrip()
        n = len(line)
        if n > 55:
            line = line[:40]
            index = line.rfind(' ')
            if index != -1:
                line = line[:index]
            line += '... <Read More>'

        out_lines.append(line)
        
    print '\n'.join(out_lines)

