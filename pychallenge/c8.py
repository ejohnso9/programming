#! /usr/bin/env python

"""
DESCRIPTION:
    A working solution for Python challenge problem #8, which starts at:
        http://www.pythonchallenge.com/pc/def/integrity.html

    The page has a linked image which takes you to a password protected
    area. The interesting part of the source seems to be:


<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->

    An encrypted or compressed string. The leading 'BZ' makes me think
    we want to look at the BZ lib module.

"""


# IMPORTS
#=======================================================================
import sys, zipfile, re
import bz2
# from pprint import pprint
# from urllib import urlopen

"""
>>> import bz2
>>> dir(bz2)
['BZ2Compressor', 'BZ2Decompressor', 'BZ2File', '__author__', '__doc__', '__file
__', '__name__', 'compress', 'decompress']
>>> un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M
\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
>>> bz2.decompress(un)
'huge'
>>> pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x
14\xe1BBP\x91\xf08'
>>> bz2.decompress(pw)
'file'

# Click on the bee and fill in the htaccess dialog with:
#   user: huge
#   pass: file

# Problem #9 starts at: http://www.pythonchallenge.com/pc/return/good.html
"""

import bz2

#///////////////////////////////////////////////////////////////////////
# MAIN
#
# PREREQUISITES:
#     oxygen.png assumed to be a local file

if __name__ == '__main__':

    un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

    print "user: " + bz2.decompress(un)

    pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    print "pass: " + bz2.decompress(pw)

    print "http://www.pythonchallenge.com/pc/return/good.html"

# END MAIN
#///////////////////////////////////////////////////////////////////////
