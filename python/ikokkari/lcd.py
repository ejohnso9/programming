#!/usr/bin/env python
# file: lcd.py
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 textwidth=100:


#---------------------------------------------------------------------------------------------------
# Problem Set #2:  
# https://github.com/ikokkari/PythonProblems/blob/main/Additional%20Python%20Problems.pdf
#---------------------------------------------------------------------------------------------------
    

# 4. Lowest common dominator
def lowest_common_dominator(beta: list[int], gamma: list[int]) -> list[int]:
    from itertools import accumulate as acc

    return [max(b, g) for b, g in zip(acc(beta), acc(gamma))]

