#!/usr/bin/env python

"""
ProjectEuler problem #68
https://projecteuler.net/problem=68
"""

import sys, time
from itertools import permutations

#
# GLOBAL DATA
#

#      0
#       \
#        6    1
#      /   \ /
#     5     7
#    / \   /
#   4   9-8 - 2
#        \
#         3

# the arrangement of elements that need to be evaluated for equivalency
# in the magic 5-gon (i.e., list of indices where each tuple is
# one line of the arrangement above)
IDX = ( (0, 6, 7), (1, 7, 8), (2, 8, 9), (3, 9, 5), (4, 5, 6) )

# does the permutation meet the required spec?
def eval_perm(p):
    """is p a valid permutation?"""
    t0 = sum([p[0], p[6], p[7]]) # initial sum
    for (i,j,k) in IDX:
        if sum([p[i], p[j], p[k]]) != t0:
            return False  # p fails!

    return p  # p is valid!


def min_form(p):
    """Put p into preferred minimal form
    (i.e., smallest outside number at index 0)
    """
    # how many ccw rots do we need?
    n = p.index(min(p[:5]))

    # put min element at index 0
    return rot_ccw(p, n)


def rot_ccw(t, n):  # t: a tuple
    """rotate list l n moves counter-clockwise"""
    l = list(t) # make list so we can change it
    for i in range(n):
        l.insert(4, l.pop(0))  # rot front half
        l.append(l.pop(5))  # rot back half

    return l


def to_s(l):
    """convert permutation (as list) into a single string"""
    idx = l.index(10)
    l.pop(idx)
    l.insert(idx, 'X')

    return ''.join([str(x) for x in l])


def main():
    start_t = time.time()
    perm_gen = permutations(range(1, 11))
    found_l = []
    found_d = {} # dict of minimal permutations found

    # run through all the permutations
    i = 0
    while True:
        try:
            p = perm_gen.next()
            if eval_perm(p):
                l = min_form(p)
                s = to_s(l)
                if not found_d.has_key(s):
                    found_d[s] = True
                    print '%i:' % i, s
            i += 1
        except StopIteration:
            print "done"
            break
            

if __name__ == '__main__':
    main()


# POSTMORTEM COMMENTS
"""
    So, I did the last bit manually. The permutation library has the
    property that it goes through the list such that the first element
    will be inascending order. Here's the program output:

C:\Users\epjohn\SITS\Python>python pe68.py
10: 1234568X79
53050: 1357926X48
131804: 154327X869
309764: 197534X628
462130: 2468X15937
490808: 253691784X
511714: 2586934X17
666278: 296354871X
669260: 296851X437
718844: 2X86439517
2045410: 6789X13524
2177204: 6X98725314
done


'X' here represents 10. The last one in the list ought to be maximum.
So, now all you have to do is look at the diagram, and read off the
digits (taking 10 as two digits), in the IDX order to get the whole
string: 6531031914842725

I could, of course, write a function to do that. Maybe later (meaning
probably never, since this problem is done.)
"""


