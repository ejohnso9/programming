#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #88  (JUGGLE FEST)
https://www.codeeval.com/open_challenges/88/

AUTHOR: Erik Johnson

DISCUSSION:
    Maybe this one actually belongs in the hard category, though it
doesn't look too bad provided I am understanding what they are
saying about juggle assignments. That seems like the hard part to me.

    There is the juggler's circuit preference, but then also a
calculation of their "aptitude" for that circuit:

    Each participant will be on exactly one team and there will be a
    distinct circuit for each team to attempt. Each participant will
    rank in order of preference their top X circuits. Since we would
    like the audiences to enjoy the performances as much as possible,
    when assigning jugglers to circuits we also want to consider how
    well their skills match up to the circuit. In fact we want to match
    jugglers to circuits such that no juggler could switch to a circuit
    that they prefer more than the one they are assigned to and be a
    better fit for that circuit than one of the other jugglers assigned
    to it. 

So, a juggler is not necessarily assigned to the circuit he prefers
most, and not necessarily assigned to the circuit of their highest
aptitude. The constraint is that if there is a circuit a juggler
prefers more, his aptitude is less that all the jugglers already on that
circuit.

    Hmmm... have to think about that one.
"""

if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        # ignoring first two elements - not needed!
        codes = [s.strip() for s in line.split('|')][2]
        iList = [int(i) for i in codes.split()]
        space = min(iList)
        offset = space - 32  # 32 is ord(' ')
        print ''.join([chr(i - offset) for i in iList])

"""
NOTES:
   http://stackoverflow.com/questions/5919530/what-is-the-pythonic-way-to-calculate-dot-product 


My favorite Pythonic dot product is:

    sum([i*j for (i, j) in zip(list1, list2)])

So for your case we could do:

    sum([i*j for (i, j) in zip([K[0] for K in A], B)])
"""
