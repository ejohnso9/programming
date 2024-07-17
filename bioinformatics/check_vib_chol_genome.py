#!/usr/bin/env python

"""
2024May18
----------

There are severals ways to try to do substring matching.

For the Pattern: 'CTTGATCAT', the problem at:
    https://cogniterra.org/lesson/30257/step/10?thread=solutions&unit=22334
states that the pattern is found in the genome at the following indices:

"""


def readGenomeFile(filename):
    with open(filename) as fd:
        s = fd.read()

    return s  # genome as single string


if __name__ == '__main__':
    filename = 'Vibrio_cholera.txt'
    genome = readGenomeFile(filename)  # length = 1108250
    pattern ='CTTGATCAT'
    n = len(pattern)
    hits = [60039, 98409, 129189, 152283, 152354, 152411, 163207, 197028, 200160,
        357976, 376771, 392723, 532935, 600085, 622755, 1065555]
    for idx, match in enumerate([genome[i:i+n] for i in hits]):
        print(f"{idx}: '{match}'")

# EOF

