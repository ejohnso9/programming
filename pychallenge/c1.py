#!/usr/bin/env python

"""
DESCRIPTION:
    Python challenge problem #1

    http://www.pythonchallenge.com/pc/def/274877906944.html
    (forwards to: http://www.pythonchallenge.com/pc/def/map.html)

HISTORY
    2019May20 Updating code for Python3.
"""

# this is the text cut from the web page:
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq
ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq
qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""


# str.translate() seems to me to be the logical thing to do here, but as
# the URL hint is strongly pushing towards map(), I'll use that in my
# solution.  Here's the function I'll use with map():

#-----------------------------------------------------------------------
def rot2(c):
    if 'a' <= c <= 'z':
        c = chr(ord(c) + 2)

    # NB: assignment above affects this clause
    if c > 'z':
        # roll back to beginning of alphabet
        c = chr(ord(c) - 26)

    return c
#-----------------------------------------------------------------------


#///////////////////////////////////////////////////////////////////////
# MAIN
if __name__ == '__main__':

    print(''.join(map(rot2, list(text))))

    result = """\
i hope you didnt translate it by hand. thats what computers
are for. doing it in by hand is inefficient and that's why this text is
so long. using string.maketrans() is recommended. now apply on the url.
"""


    # for reference...
    help = """
>>> help(string.maketrans)
Help on built-in function maketrans in module strop:

maketrans(...)
    maketrans(frm, to) -> string

    Return a translation table (a string of 256 bytes long)
    suitable for use in string.translate.  The strings frm and to
    must be of the same length.
    """

    print(''.join(map(rot2, list('map.html'))))
    # that would be 'ocr.jvon', which will actually get you a download
    # with text in it, implying we should go to an HTML page.

    # the step starts here:
    # http://www.pythonchallenge.com/pc/def/ocr.html 

# END MAIN
#///////////////////////////////////////////////////////////////////////
