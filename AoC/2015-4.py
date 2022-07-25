#!/usr/bin/env python
# run at pythonanywhere.com under Python 3.9.5

"""
DESCRIPTION
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to
use as gifts for all the economically forward-thinking little girls and
boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start
with at least five zeroes. The input to the MD5 hash is some secret key
(your puzzle input, given below) followed by a number in decimal. To
mine AdventCoins, you must find Santa the lowest positive number (no
leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

    - If your secret key is abcdef, the answer is 609043, because the
      MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...),
      and it is the lowest such number to do so. 

    - If your secret key is pqrstuv, the lowest number it combines with
      to make an MD5 hash starting with five zeroes is 1048970; that is,
      the MD5 hash of pqrstuv1048970 looks like 000006136ef.... 

  Your puzzle input is yzbqklnj.

AUTHOR
    Erik Johnson

DISCUSSION
    md5 is implemented in standard python library 'hashlib'
    We just need a function to evaluate the md5 hash and decide if it is
    meeting the required conditions.
    Start with 1 and let the iteration rip, stop when you meet the
    condition.

    This code also has the remnants of using 'pdb', the interactive
    Python debugger.

HISTORY (see also: git log <filename>)
    2022Jul25 created
"""


import sys
from hashlib import md5
# import pdb



# GLOBAL DATA
NL = '\n'
PUZZ_INPUT = 'yzbqklnj'


def getHash(puzz_input, num_i):
    s = puzz_input + str(num_i)
    s_bytes = s.encode('utf-8')
    return md5(s_bytes).hexdigest()


def main():

    pat = '0' * 5
    i = 0  # i = 609000  # testing: start close to known solution
    key = PUZZ_INPUT  # key = 'abcdef' # test value
    while True:
        i += 1
        hash_val = getHash(key, i)
        if hash_val.startswith(pat):
            print(f"getHash('{key}', {i}) is: '{hash_val}'")
            break

    # 1st gold star:
    print("ej: 282749 was verified as correct answer on 2022Jul25")

if __name__ == '__main__':
    main()

# EOF

