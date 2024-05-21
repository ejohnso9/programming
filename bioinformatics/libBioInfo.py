#!usr/bin/env python

"""
This library houses some bioinformatics functions and data that goes
with the Coursera course:
    "Biology Meets Programming: Bioinformatics for Beginners"
    (https://www.coursera.org/learn/bioinformatics/home/week/1
    but that seems to be implemented through a different site:
    Cogniterra: on 2024May12 I am at:
        https://cogniterra.org/lesson/30257/step/9?unit=22334)

NOTES
    I am generally changing the course functions to have
    PEP-8-named vars here
"""


import pdb  # pdb.set_trace()


# DATA / GLOBAL symconsts
DNA_BASES_COMP_MAP = {'A': 'T', 'T':'A', 'C': 'G', 'G': 'C'}


#
# Functions (try to keep in alphabetical order)
#

def Complement(pattern: str) -> str:
    """
    Complement of 'ACGT'* string.
    
    @Pattern input string of list("ACGT")
    @return complemented str (e.g. "ACGT" -> "TGCA")
    """
    
    return ''.join([DNA_BASES_COMP_MAP [c] for c in pattern])


def PatternMatching(pattern: str, genome: str) -> list[int]:
    """
    Given 'Pattern' and a string of ACGT* bases, return the
    (0-based) indices of 'Pattern' occurences (or [] if 'pattern'
    not found)
    """

    # TODO: redo this imp. using str.index()
    positions = []  # RV
    k = len(pattern)
    for i in range(len(genome) - k + 1):
        s = genome[i:i+k]
        if s == pattern:
            positions.append(i)

    return positions


def testPatternMatching():
    arg1, arg2 = 'ACTT', 'GATATATGCATATACTT'
    rv = PatternMatching(arg1, arg2)
    try:
        assert rv == [1, 3, 9]
    except AssertionError as ae_x:
        print(f"PatternMatching('{arg1}', '{arg2}') returned: {rv}")


def Reverse(Pattern: str) -> str:
    """a reversed copy of 'Pattern' (i.e., 'Pattern' read backwards)"""
    
    return ''.join(reversed(Pattern))


def ReverseComplement(Pattern: str) -> str:
    """
    # Input:  A DNA string Pattern
    # Output: The reverse complement of Pattern
    """
    
    return Reverse(Complement(Pattern))


# ENTRY POINT
if __name__ == '__main__':

    # print(f"This library module defines: {globals()}")

    testPatternMatching()

    # TODO: the whole genome is available as one big string right here:
    #    https://bioinformaticsalgorithms.com/data/realdatasets/Replication/Vibrio_cholerae.txt
    #    [ ] benchmark PatternMatching() with a list comprehension
    #       - [ ] as-is
    #       - [ ] using .index()
    #       - [ ] using .startswith()
    #       - [ ] any significant difference?

