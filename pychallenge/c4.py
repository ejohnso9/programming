#! /usr/bin/env python

"""
DESCRIPTION:
    Python challenge problem #4 at:

        http://www.pythonchallenge.com/pc/def/linkedlist.html  (.php)

        start at: linkedlist.php?nothing=12345

    Clue page states:

    <!-- urllib may help. don't try ALL nothings, since it will never 
    end. 400 times is enough. -->

RESULT
    http://www.pythonchallenge.com/pc/def/peak.html

HISTORY
    2019May20  updating for Python3
"""

import re
import pdb
from urllib.request import urlopen


#-----------------------------------------------------------------------
def follow(start_i):
    """
    DESCRIPTION:
        Follows a chain of URL's matching a quick and dirty pattern of
        pat = r'and the next nothing is \d+'

    PARAMETERS:
        i - int: an integer number

    RETURN VALUE:
        None
    """

    i = 0

    # argument checking
    assert type(start_i) is int
    

    pat = r'and the next nothing is \d+'
    base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    url = base_url + '?nothing=%i' % start_i

    # follow the chain...
    while 1:
        # get HTML output as string
        fd = urlopen(url)
        text = fd.read().decode('utf-8')
        # pdb.set_trace()
        fd.close()

        # try to find the pattern
        l = re.findall(pat, text)
        try:
            assert len(l) == 1
        except AssertionError:
            print(text)
            break

        match = l[0]                # e.g., '92512'
        n = match.split()[-1]
        print('[{}] {} '.format(i, match)); i += 1;

        # NOTE: such things can be expressed in fewer statements.
        # Dennis Ritchey advises: "Don't be clever - clever kills."
        # n = re.findall(pat, html)[0].split('=')[1]
        # (i.e., shorter but not more understandable)

        # next URL
        url = base_url + '?nothing=' + n

    return None
#-----------------------------------------------------------------------


#///////////////////////////////////////////////////////////////////////
# MAIN
if __name__ == '__main__':

    #follow(12345)

    # I had the loop defined in follow() as my main body. When the chain
    # ended on 92118, stating 'Yes. Divide by two and keep going.' I
    # didn't know how many such glitches I might hit and made the
    # while-loop into a function. As it turns out, there is only 1
    # such glitch, before the chain continues to 'peak.html'.

    # follow(int(92118 / 2))  # numbers not always the same
    # ends on 'peak.html'
    follow(8022)

    print("http://www.pythonchallenge.com/pc/def/peak.html")

# END MAIN
#///////////////////////////////////////////////////////////////////////
