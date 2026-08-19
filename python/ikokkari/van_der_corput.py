#!/usr/bin/env python
# file: labs109.py
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 textwidth=100:


from fractions import Fraction


#===============================================================================
# UTILITY FUNCTIONS
def to_base(n: int, base: int) -> list[int]:
    if base < 2:
        raise ValueError("base must be at least 2")
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return [0]

    digits = []
    while n:
        n, digit = divmod(n, base)
        digits.append(digit)

    return digits[::-1]  # NB: most sig. first: to_base(123, 10) -> [1, 2, 3]
#===============================================================================



# 37. Van der Corput sequence
def van_der_corput(base: int, n: int) -> Fraction:
    """
    Problem #37:
    https://github.com/ikokkari/PythonProblems/blob/main/Additional%20Python%20Problems.pdf
    """

    # iterating 'ls' least-sig first!
    return sum([Fraction(el, base ** (i+1)) for i, el in enumerate(to_base(n, base)[::-1])])



# ENTRY POINT
if __name__ == '__main__':
    assert True


# EOF

