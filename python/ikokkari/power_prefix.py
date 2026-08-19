#!/usr/bin/env python
# file: power_prefix.py
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 textwidth=100:


# 9. Power Prefix
def power_prefix(prefix: str) -> int:
    """
    Problem #9, "Additional Python Problems" (Set 2)
    https://github.com/ikokkari/PythonProblems/blob/main/109%20Python%20Problems%20for%20CCPS%20109.pdf
    Find the power of 2 that gives a number starting with 'prefix' where 'prefix'
    is a string with '*' wildcards in it.
    (e.g., power_prefix('*22*3720') -> 63)
    """

    # let's just handle the base case directly
    if prefix == '1':
        return 0

    def str_cmp(template: str, s: str) -> bool:
        """does given 's' match the template (w/ '*' wildcards)?"""
        # this is probably less efficient than more imperative stuff, but it's clean
        for i, c in enumerate(template):
            if c == '*':
                continue
            if template[i] != s[i]:
                return False

        return True

    two_n, power = 1, 0  # starting at: 2 ** 0 == 1
    while True:
        two_n <<= 1  # shift left (i.e., * 2), reassign
        s = str(two_n)
        power += 1  # keep track of which power we are at
        if len(s) < len(prefix):
            continue  # have to have enough digits in the computed number to cover the template comparison
        if str_cmp(prefix, str(two_n)):
            return power  # Found the first 2 ** power that matches

    raise RuntimeError("How did you get here?")

