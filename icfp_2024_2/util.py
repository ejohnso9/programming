#!/usr/bin/env python
# CBV / COBV => "Cult of the Bound Variable"

"""
This module implements various support functions in Python for doing the
ICFP 2024 contest  (NB: I am doing it well after the contest has closed
for my own edification and entertainment.)
"""

#
# GLOBAL DATA
#

# base-94 decoding
STR_DATA = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!\"#$%&'()*+,-./:;<=>?@[\]^_`|~ \n")


def strEncode(ascii_txt: str) -> str:
    """
    Convert plain ASCII into COBV text (w/o 'S' op at front)
    """

    return 'S' + ''.join([chr_xlate(c) for c in ascii_txt])


def chr_xlate(c):
    return chr(STR_DATA.index(c) + 33) if c != '}' else ' '


def strDecode(cbv_str: str) -> str:
    """
    Convert CBV text into plain ASCII (w/o 'S' op at front)
    """

    assert cbv_str[0] == 'S'
    return ''.join([STR_DATA[ord(c) - 33] for c in cbv_str[1:]])


def runTests():
    """unit testing"""

    c = chr_xlate('H')

    # test 1
    hello = "Hello World!"
    cbv_hw = 'SB%,,/}Q/2,$_'  # 'S' + "Hello World!" from: https://icfpcontest2024.github.io/icfp.html
    decoded = strDecode(cbv_hw)
    assert decoded == hello
    print(f"PASS: strDecode('{cbv_hw}') is: '{decoded}'")

    # test2
    encoded = strEncode(hello)
    assert encoded == cbv_hw
    print(f"PASS: strEncode('{hello}') is: '{encoded}'")

    # test3
    txt = 'S\'%4}).$%8'
    decoded = strDecode(txt)  # "get index"
    print(f"PASS: strDecode('{txt}') is: '{decoded}'")


# ENTRY POINT
if __name__ == '__main__':
    runTests()

# EOF

