#!/usr/bin/env python

import sys, re
import pdb

"""
Solution for codeeval challenge #36 (MESSAGE DECODING)
https://www.codeeval.com/open_challenges/36/

AUTHOR: Erik Johnson
"""

out_lines = []
pat = r'([01]+)$' # the binary message part

# build the ordered binary representations that will be mapped to characters in 's'
# BOOL_VEC = [all([bool(int(c)) for c in bin(i)[2:]]) for i in range(2**7)]
BINREP = []
for p2 in range(1, 8):
    l = []
    for i in xrange(2 ** p2 - 1):
        rep = bin(i)[2:]
        n_rep = len(rep)
        if n_rep < p2:
            rep = '0' * (p2 - n_rep) + rep
        l.append(rep)

    BINREP.extend(l)

def build_dict(s):
    d = {}
    for i, c in enumerate(s):
        d[BINREP[i]] = c
    return d

def decode_segment(s):
    n = int(s[:3], 2) # word length this segment
    if n == 0:
        return True, None, None

    i = 0
    c_l = [] # list of chars in this segment
    s = s[3:]
    seg_end = '1' * n

    while True:
        key = s[i * n : (i * n) + n]
        i += 1
        if key == seg_end:
            break
        c_l.append(decode_dict[key])

    return False, ''.join(c_l), s[i * n:]

# MAIN
for line in open(sys.argv[1], 'r'):
    line = line.rstrip()

    # set up the decode dict
    match = re.search(pat, line)
    msg = match.group(0)
    start = match.start()
    decode_dict = build_dict(line[:start])

    # walk the segments, look up the binary words, record the translation
    dec_segs = [] # decoded segments
    done = False
    rest = line[start:]
    while not done:
        done, dec_seg, rest = decode_segment(rest)
        if not done:
            dec_segs.append(dec_seg)

    out_lines.append(''.join(dec_segs))
    
print '\n'.join(out_lines)

