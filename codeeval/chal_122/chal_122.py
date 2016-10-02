#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #122 (HIDDEN DIGITS)
https://www.codeeval.com/open_challenges/122/

AUTHOR: Erik Johnson
DATE: 2016-May-24

APPROACH:
    There is the unix 'tr' equivalent in ''.translate(), but that takes
a mapping of 256 characters. I think this problem is actually simpler to
understand if we simply create a function that uses a dict (map) to
remap characters to other characters (strings) (including empty string).
Then I can just map() that func over the string elements, join() them
and dump them.
"""

# map setup
"""
>>> d = {}
>>> for i in range(10):
...     d[str(i)] = str(i)
...
>>> d
{'1': '1', '0': '0', '3': '3', '2': '2', '5': '5', '4': '4', '7': '7',
'6': '6', '9': '9', '8': '8'}
>>> s = 'abcdefghij'
>>> for i in range(10):
...     d[s[i]] = str(i)
...
>>> d
"""

C_MAP = {
    'a': '0', 'c': '2', 'b': '1', 'e': '4', 'd': '3', 'g': '6', 'f': '5',
    'i': '8', 'h': '7', 'j': '9', '1': '1', '0': '0', '3': '3', '2': '2',
    '5': '5', '4': '4', '7': '7', '6': '6', '9': '9', '8': '8'
}

def f(c):
    return C_MAP[c] if C_MAP.has_key(c) else ''

if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        s = line.rstrip()
        new_s = ''.join(map(f, list(s)))
        if not len(new_s):
            new_s = 'NONE'

        lines_out.append(new_s)

    print '\n'.join(lines_out)
    sys.stdout.flush()
