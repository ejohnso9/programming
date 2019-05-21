#!/usr/bin/env python
"""
Solution for CodeEval challenge #169 (FILENAME PATTERN)
https://www.codeeval.com/open_challenges/169/

AUTHOR: Erik Johnson
DATE: 2016-Oct-02

DISCUSSION:
"""

import sys, re

SUBS = [
    # turn file globbing pattern into REGEXP
    ('.', '\\.'),
    ('?', '.{1}'),
    ('*', '.*'),
]

def filter_files(line):
    """filter words[1:] by regex of words[0]"""

    files_l = []
    words = line.split()
    pat = words[0]
    for t in SUBS:
        pat = pat.replace(t[0], t[1])

    pat += '$' # end needs to be anchored

    for fname in words[1:]:
        if re.match(pat, fname):
            files_l.append(fname)

    return ' '.join(files_l) if files_l else '-'


if __name__ == "__main__":
    lines_out = []

    for line in open(sys.argv[1], 'r'):
        lines_out.append(filter_files(line.rstrip()))

    print '\n'.join(lines_out)
    sys.stdout.flush()
