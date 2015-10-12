#!/usr/bin/env python

import sys, re, string

"""
Solution for codeeval challenge #205 (CLEAN UP THE WORDS)
https://www.codeeval.com/open_challenges/205/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":
    lines_out = []
    table = string.maketrans('1234567890_', ':' * 11)
    for line in open(sys.argv[1], 'r'):
        s = line.strip().translate(table)
        words = [w.lower() for w in re.findall(r'\w+', s)]
        lines_out.append(' '.join(words))

    print '\n'.join(lines_out)
    sys.stdout.flush()
