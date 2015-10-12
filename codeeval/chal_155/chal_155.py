#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #155  (ASCII DECRYPTION)
https://www.codeeval.com/open_challenges/155/

AUTHOR: Erik Johnson

DISCUSSION:
    Ummmm, well... all of the letters and even the punctuation is above
' ', ASCII char 32 (dec). Just look at the smallest value in the data,
that's your space character, now we have the offset. All that's left to
do is process the numbers back into a string. This whole idea of
repeated word and knowing the last character of that repeated word seems
like a complete red herring. If you don't have any spaces in the
message, then it's a one-word message and there can't be any repeated
word, right? So we must have a space character. Unless there are
embedded control characters in the message, this is trivial.

    Is the problem creator not aware of this issue, or is it a test to
see if I spend a bunch of resources flailing about trying to find two
instances of a 5-char word that ends in 's'? I guess I will soon know.

    I moved to the "Hard" problems, but this doesn't seem to be one of
them. :(
"""

if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        # ignoring first two elements - not needed!
        codes = [s.strip() for s in line.split('|')][2]
        iList = [int(i) for i in codes.split()]
        space = min(iList)
        offset = space - 32  # 32 is ord(' ')
        print ''.join([chr(i - offset) for i in iList])

