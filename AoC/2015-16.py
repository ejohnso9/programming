#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
DESCRIPTION
    https://adventofcode.com/2015/day/16

--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her
a thank you card. However, there's a small problem: she signed it "From,
Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure
out which Aunt Sue (which you conveniently number 1 to 500, for sanity)
gave you the gift. You open the present and, as luck would have it, good
ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what
you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect
a few specific compounds in a given sample, as well as how many distinct
kinds of those compounds there are. According to the instructions, these
are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping
from the gift into the MFCSAM. It beeps inquisitively at you a few times
and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue.
Things missing from your list aren't zero - you simply don't remember
the value.

What is the number of the Sue that got you the gift?

DISCUSSION
    So, two general approaches occur to me:

    Strategy I:
    -----------
    Iterate the attributes given above and use each to filter a set of
    rows. The evaluation function needs to keep all rows where the
    attribute is not mentioned. But, for example, every row that gives a
    'children' value can be eliminated if it's value is not 3.

    After walking the 10 given attributes, there should be one Aunt left.

    Strategy II:
    ------------
    Iterate over aunt rows, check each of the 3 attributes from the row
    against the 10 given attributes (above). Most rows will 


    My input is below. This all seems pretty straighforward: every Aunt
    line has some subset of the properties above, with a value.
    Presumably, at most one row will match in all of the attributes.

STRATEGY
    By inspection, all of the Aunt Sue lines appear to have 3
    attributes. Parse those out and check whether each matches the
    MFCSAM dict given above. If a row matches in all three attributes,
    print it out.

AUTHOR
    Erik P. Johnson

HISTORY
    2022Aug05  Created.
"""


# import pdb  # http://pymotw.com/2/pdb/

# GLOBAL DATA
NL = '\n'

# the 500 Aunts Sue:
DATA = """\
Sue 1: cars: 9, akitas: 3, goldfish: 0
Sue 2: akitas: 9, children: 3, samoyeds: 9
Sue 3: trees: 6, cars: 6, children: 4
Sue 4: trees: 4, vizslas: 4, goldfish: 9
Sue 5: akitas: 9, vizslas: 7, cars: 5
Sue 6: vizslas: 6, goldfish: 6, akitas: 3
Sue 7: pomeranians: 5, samoyeds: 0, perfumes: 10
Sue 8: cars: 10, pomeranians: 7, goldfish: 8
Sue 9: trees: 2, vizslas: 7, samoyeds: 6
Sue 10: perfumes: 5, pomeranians: 4, children: 9
Sue 11: vizslas: 5, perfumes: 8, cars: 10
Sue 12: children: 10, cars: 6, perfumes: 5
Sue 13: cats: 4, samoyeds: 7, pomeranians: 8
Sue 14: perfumes: 6, goldfish: 10, children: 7
Sue 15: perfumes: 4, pomeranians: 3, cars: 6
Sue 16: perfumes: 7, cars: 9, pomeranians: 6
Sue 17: goldfish: 3, cars: 6, vizslas: 7
Sue 18: perfumes: 6, cars: 7, goldfish: 3
Sue 19: trees: 0, akitas: 3, pomeranians: 8
Sue 20: goldfish: 6, trees: 2, akitas: 6
Sue 21: pomeranians: 9, akitas: 9, samoyeds: 9
Sue 22: vizslas: 2, cars: 9, perfumes: 5
Sue 23: goldfish: 10, samoyeds: 8, children: 9
Sue 24: akitas: 4, goldfish: 1, vizslas: 5
Sue 25: goldfish: 10, trees: 8, perfumes: 6
Sue 26: vizslas: 5, akitas: 8, trees: 1
Sue 27: trees: 3, cars: 6, perfumes: 2
Sue 28: goldfish: 8, trees: 7, akitas: 10
Sue 29: children: 5, trees: 1, goldfish: 10
Sue 30: vizslas: 3, perfumes: 8, akitas: 3
Sue 31: cars: 6, children: 10, perfumes: 7
Sue 32: cars: 10, perfumes: 3, goldfish: 10
Sue 33: perfumes: 9, vizslas: 3, akitas: 4
Sue 34: perfumes: 10, vizslas: 7, children: 8
Sue 35: cars: 5, perfumes: 5, vizslas: 9
Sue 36: trees: 9, cars: 9, akitas: 7
Sue 37: samoyeds: 9, perfumes: 2, cars: 10
Sue 38: akitas: 7, cars: 5, trees: 5
Sue 39: goldfish: 8, trees: 9, cars: 10
Sue 40: trees: 0, cats: 1, pomeranians: 1
Sue 41: pomeranians: 6, perfumes: 9, samoyeds: 1
Sue 42: vizslas: 6, akitas: 3, pomeranians: 1
Sue 43: vizslas: 2, perfumes: 3, pomeranians: 6
Sue 44: akitas: 5, pomeranians: 0, vizslas: 10
Sue 45: vizslas: 4, goldfish: 1, cars: 5
Sue 46: cars: 4, vizslas: 8, cats: 0
Sue 47: cats: 5, children: 8, pomeranians: 2
Sue 48: vizslas: 3, perfumes: 6, cats: 0
Sue 49: akitas: 7, perfumes: 0, trees: 7
Sue 50: trees: 4, akitas: 10, vizslas: 2
Sue 51: goldfish: 10, cars: 9, trees: 4
Sue 52: cars: 5, children: 9, perfumes: 0
Sue 53: vizslas: 5, cars: 3, cats: 8
Sue 54: cars: 5, akitas: 1, goldfish: 10
Sue 55: akitas: 10, vizslas: 2, cars: 6
Sue 56: cats: 6, trees: 0, cars: 4
Sue 57: vizslas: 1, akitas: 1, samoyeds: 7
Sue 58: samoyeds: 6, vizslas: 1, akitas: 7
Sue 59: akitas: 9, cars: 8, vizslas: 1
Sue 60: cars: 6, vizslas: 7, goldfish: 0
Sue 61: pomeranians: 5, akitas: 6, vizslas: 2
Sue 62: samoyeds: 2, cats: 8, goldfish: 7
Sue 63: vizslas: 10, goldfish: 7, samoyeds: 9
Sue 64: perfumes: 2, trees: 1, akitas: 6
Sue 65: cars: 8, perfumes: 10, vizslas: 9
Sue 66: akitas: 8, vizslas: 8, perfumes: 8
Sue 67: goldfish: 7, cars: 9, samoyeds: 9
Sue 68: perfumes: 2, children: 7, akitas: 1
Sue 69: perfumes: 7, vizslas: 9, akitas: 1
Sue 70: samoyeds: 3, vizslas: 1, trees: 1
Sue 71: vizslas: 8, goldfish: 7, trees: 9
Sue 72: goldfish: 8, cars: 6, trees: 9
Sue 73: perfumes: 5, cars: 10, samoyeds: 7
Sue 74: pomeranians: 4, perfumes: 3, cars: 5
Sue 75: samoyeds: 1, perfumes: 1, pomeranians: 1
Sue 76: goldfish: 4, cats: 6, akitas: 7
Sue 77: perfumes: 5, akitas: 4, vizslas: 8
Sue 78: perfumes: 4, cats: 3, children: 4
Sue 79: vizslas: 5, pomeranians: 9, samoyeds: 7
Sue 80: cars: 3, samoyeds: 5, pomeranians: 7
Sue 81: vizslas: 2, samoyeds: 4, perfumes: 2
Sue 82: trees: 1, akitas: 10, vizslas: 9
Sue 83: vizslas: 0, akitas: 2, samoyeds: 5
Sue 84: perfumes: 5, vizslas: 7, children: 8
Sue 85: cats: 3, children: 2, trees: 0
Sue 86: cars: 3, perfumes: 2, goldfish: 2
Sue 87: trees: 1, akitas: 7, vizslas: 0
Sue 88: trees: 1, akitas: 2, samoyeds: 1
Sue 89: cars: 4, vizslas: 8, akitas: 1
Sue 90: perfumes: 5, cats: 3, vizslas: 0
Sue 91: samoyeds: 7, cats: 6, goldfish: 8
Sue 92: samoyeds: 10, cats: 0, cars: 7
Sue 93: cars: 6, akitas: 7, samoyeds: 2
Sue 94: perfumes: 0, goldfish: 6, trees: 9
Sue 95: cars: 6, pomeranians: 2, samoyeds: 8
Sue 96: cars: 2, trees: 9, samoyeds: 4
Sue 97: goldfish: 5, trees: 1, children: 0
Sue 98: akitas: 9, goldfish: 7, children: 6
Sue 99: goldfish: 9, akitas: 0, pomeranians: 0
Sue 100: samoyeds: 6, children: 8, vizslas: 5
Sue 101: vizslas: 6, cars: 5, goldfish: 4
Sue 102: vizslas: 6, akitas: 2, perfumes: 6
Sue 103: samoyeds: 3, akitas: 7, children: 4
Sue 104: cars: 3, perfumes: 10, cats: 6
Sue 105: vizslas: 9, pomeranians: 0, cars: 1
Sue 106: cats: 6, samoyeds: 8, pomeranians: 5
Sue 107: cars: 7, trees: 4, akitas: 10
Sue 108: perfumes: 3, vizslas: 1, goldfish: 9
Sue 109: trees: 6, cars: 8, goldfish: 5
Sue 110: pomeranians: 2, children: 1, vizslas: 7
Sue 111: akitas: 0, vizslas: 8, cars: 0
Sue 112: goldfish: 3, vizslas: 6, akitas: 2
Sue 113: akitas: 10, pomeranians: 7, perfumes: 7
Sue 114: cars: 10, cats: 2, vizslas: 8
Sue 115: akitas: 8, trees: 1, vizslas: 2
Sue 116: vizslas: 2, akitas: 7, perfumes: 1
Sue 117: goldfish: 0, vizslas: 10, trees: 9
Sue 118: trees: 3, cars: 0, goldfish: 0
Sue 119: perfumes: 7, goldfish: 5, trees: 9
Sue 120: children: 9, vizslas: 3, trees: 5
Sue 121: vizslas: 1, goldfish: 7, akitas: 10
Sue 122: perfumes: 1, cars: 6, trees: 1
Sue 123: akitas: 2, vizslas: 0, goldfish: 7
Sue 124: vizslas: 10, pomeranians: 7, akitas: 0
Sue 125: perfumes: 4, cats: 5, vizslas: 2
Sue 126: cars: 6, samoyeds: 8, akitas: 3
Sue 127: trees: 9, goldfish: 7, akitas: 9
Sue 128: cars: 8, trees: 0, perfumes: 2
Sue 129: pomeranians: 7, vizslas: 2, perfumes: 6
Sue 130: vizslas: 9, pomeranians: 3, trees: 6
Sue 131: vizslas: 7, cars: 9, perfumes: 1
Sue 132: akitas: 2, pomeranians: 9, vizslas: 7
Sue 133: trees: 9, pomeranians: 10, samoyeds: 0
Sue 134: children: 4, akitas: 10, perfumes: 4
Sue 135: vizslas: 1, cats: 1, trees: 8
Sue 136: samoyeds: 7, cars: 8, goldfish: 5
Sue 137: perfumes: 0, children: 1, pomeranians: 10
Sue 138: vizslas: 4, perfumes: 5, cars: 5
Sue 139: trees: 2, perfumes: 8, goldfish: 0
Sue 140: cars: 10, akitas: 5, goldfish: 7
Sue 141: children: 4, trees: 3, goldfish: 8
Sue 142: cars: 8, perfumes: 6, trees: 7
Sue 143: akitas: 6, goldfish: 0, trees: 10
Sue 144: akitas: 7, pomeranians: 10, perfumes: 10
Sue 145: trees: 10, vizslas: 3, goldfish: 4
Sue 146: samoyeds: 4, akitas: 3, perfumes: 6
Sue 147: akitas: 8, perfumes: 2, pomeranians: 10
Sue 148: cars: 2, perfumes: 0, goldfish: 8
Sue 149: goldfish: 6, akitas: 7, perfumes: 6
Sue 150: cars: 2, pomeranians: 5, perfumes: 4
Sue 151: goldfish: 1, cars: 5, trees: 0
Sue 152: pomeranians: 4, cars: 7, children: 1
Sue 153: goldfish: 8, cars: 1, children: 10
Sue 154: cars: 6, perfumes: 8, trees: 1
Sue 155: akitas: 4, perfumes: 6, pomeranians: 2
Sue 156: pomeranians: 5, cars: 4, akitas: 1
Sue 157: cats: 5, cars: 9, goldfish: 8
Sue 158: vizslas: 5, samoyeds: 1, children: 7
Sue 159: vizslas: 1, perfumes: 3, akitas: 1
Sue 160: goldfish: 10, pomeranians: 9, perfumes: 5
Sue 161: samoyeds: 3, trees: 7, cars: 2
Sue 162: cars: 2, pomeranians: 1, vizslas: 6
Sue 163: vizslas: 3, perfumes: 5, akitas: 6
Sue 164: vizslas: 1, trees: 0, akitas: 5
Sue 165: vizslas: 5, cars: 6, pomeranians: 8
Sue 166: cars: 10, perfumes: 2, trees: 9
Sue 167: cars: 10, pomeranians: 6, perfumes: 4
Sue 168: akitas: 7, trees: 10, goldfish: 7
Sue 169: akitas: 1, perfumes: 10, cars: 10
Sue 170: akitas: 5, samoyeds: 8, vizslas: 6
Sue 171: children: 3, akitas: 2, vizslas: 3
Sue 172: goldfish: 5, vizslas: 5, perfumes: 9
Sue 173: perfumes: 5, goldfish: 10, trees: 5
Sue 174: akitas: 5, vizslas: 2, children: 7
Sue 175: perfumes: 5, cars: 7, samoyeds: 2
Sue 176: cars: 8, vizslas: 10, akitas: 7
Sue 177: perfumes: 7, children: 8, goldfish: 7
Sue 178: cars: 1, pomeranians: 9, samoyeds: 0
Sue 179: perfumes: 6, cars: 2, trees: 6
Sue 180: trees: 3, vizslas: 7, children: 3
Sue 181: vizslas: 8, samoyeds: 2, trees: 9
Sue 182: perfumes: 3, cats: 1, children: 5
Sue 183: akitas: 9, cats: 6, children: 3
Sue 184: pomeranians: 9, cars: 6, perfumes: 8
Sue 185: vizslas: 9, trees: 0, akitas: 9
Sue 186: perfumes: 6, cars: 5, goldfish: 5
Sue 187: perfumes: 4, cats: 7, vizslas: 2
Sue 188: akitas: 7, cars: 4, children: 10
Sue 189: akitas: 0, goldfish: 7, vizslas: 5
Sue 190: akitas: 5, cars: 5, cats: 6
Sue 191: cars: 6, children: 0, perfumes: 3
Sue 192: cats: 2, perfumes: 10, goldfish: 7
Sue 193: trees: 1, perfumes: 0, cars: 8
Sue 194: perfumes: 9, children: 4, cats: 6
Sue 195: akitas: 7, trees: 3, goldfish: 6
Sue 196: goldfish: 8, cars: 8, samoyeds: 0
Sue 197: cats: 0, akitas: 10, vizslas: 0
Sue 198: goldfish: 1, perfumes: 3, cars: 8
Sue 199: akitas: 10, vizslas: 5, samoyeds: 6
Sue 200: pomeranians: 9, goldfish: 9, samoyeds: 7
Sue 201: samoyeds: 0, goldfish: 7, akitas: 6
Sue 202: vizslas: 0, goldfish: 2, akitas: 1
Sue 203: goldfish: 3, children: 0, vizslas: 8
Sue 204: cars: 8, trees: 2, perfumes: 2
Sue 205: cars: 4, perfumes: 5, goldfish: 8
Sue 206: vizslas: 3, trees: 2, akitas: 1
Sue 207: cars: 7, goldfish: 5, trees: 1
Sue 208: goldfish: 1, cars: 6, vizslas: 8
Sue 209: cats: 4, trees: 1, children: 0
Sue 210: cats: 10, children: 0, perfumes: 0
Sue 211: cars: 4, pomeranians: 7, samoyeds: 5
Sue 212: cars: 2, pomeranians: 10, trees: 1
Sue 213: trees: 10, cats: 5, cars: 10
Sue 214: perfumes: 5, trees: 1, vizslas: 1
Sue 215: akitas: 10, vizslas: 8, samoyeds: 8
Sue 216: vizslas: 2, cats: 5, pomeranians: 3
Sue 217: akitas: 10, perfumes: 0, cats: 10
Sue 218: trees: 8, cats: 5, vizslas: 2
Sue 219: goldfish: 10, perfumes: 8, children: 2
Sue 220: samoyeds: 9, trees: 8, vizslas: 7
Sue 221: children: 7, trees: 6, cars: 6
Sue 222: cats: 4, akitas: 5, pomeranians: 0
Sue 223: trees: 8, goldfish: 2, perfumes: 8
Sue 224: pomeranians: 9, cars: 8, akitas: 5
Sue 225: akitas: 10, vizslas: 0, trees: 2
Sue 226: akitas: 8, cats: 6, cars: 7
Sue 227: trees: 1, akitas: 3, goldfish: 4
Sue 228: pomeranians: 6, cats: 3, goldfish: 3
Sue 229: trees: 10, perfumes: 3, vizslas: 7
Sue 230: perfumes: 8, cars: 7, akitas: 0
Sue 231: perfumes: 10, goldfish: 4, cars: 6
Sue 232: goldfish: 7, trees: 3, cats: 2
Sue 233: perfumes: 6, trees: 4, akitas: 4
Sue 234: goldfish: 9, cats: 4, cars: 7
Sue 235: pomeranians: 6, vizslas: 0, akitas: 6
Sue 236: samoyeds: 5, cars: 5, children: 4
Sue 237: vizslas: 10, cars: 4, goldfish: 4
Sue 238: goldfish: 3, samoyeds: 7, akitas: 2
Sue 239: cats: 8, children: 2, vizslas: 7
Sue 240: cars: 9, perfumes: 4, trees: 9
Sue 241: trees: 8, vizslas: 2, goldfish: 5
Sue 242: cars: 6, trees: 3, vizslas: 3
Sue 243: cats: 6, children: 7, cars: 4
Sue 244: cats: 10, perfumes: 2, goldfish: 7
Sue 245: akitas: 8, cats: 10, perfumes: 8
Sue 246: vizslas: 8, akitas: 5, perfumes: 10
Sue 247: goldfish: 2, vizslas: 5, akitas: 7
Sue 248: akitas: 3, perfumes: 0, trees: 10
Sue 249: cats: 4, vizslas: 5, pomeranians: 6
Sue 250: children: 3, vizslas: 7, perfumes: 2
Sue 251: cars: 0, pomeranians: 10, perfumes: 0
Sue 252: akitas: 0, goldfish: 9, cars: 6
Sue 253: perfumes: 7, cars: 4, samoyeds: 5
Sue 254: akitas: 9, trees: 10, cars: 4
Sue 255: samoyeds: 10, children: 6, akitas: 7
Sue 256: trees: 8, goldfish: 8, perfumes: 8
Sue 257: goldfish: 3, akitas: 2, perfumes: 6
Sue 258: cats: 7, trees: 0, vizslas: 1
Sue 259: perfumes: 7, cars: 7, akitas: 7
Sue 260: goldfish: 0, vizslas: 0, samoyeds: 2
Sue 261: vizslas: 2, children: 2, cats: 3
Sue 262: vizslas: 2, pomeranians: 9, samoyeds: 3
Sue 263: cats: 1, akitas: 3, vizslas: 1
Sue 264: pomeranians: 10, trees: 2, goldfish: 7
Sue 265: samoyeds: 5, trees: 7, perfumes: 4
Sue 266: perfumes: 10, cars: 1, pomeranians: 3
Sue 267: trees: 6, goldfish: 1, cars: 0
Sue 268: cars: 6, samoyeds: 4, pomeranians: 5
Sue 269: goldfish: 3, vizslas: 3, akitas: 3
Sue 270: children: 5, cats: 0, cars: 4
Sue 271: goldfish: 3, perfumes: 8, pomeranians: 7
Sue 272: samoyeds: 6, cars: 7, perfumes: 10
Sue 273: trees: 4, cars: 2, vizslas: 7
Sue 274: samoyeds: 10, perfumes: 9, goldfish: 6
Sue 275: cars: 4, trees: 2, perfumes: 7
Sue 276: akitas: 3, perfumes: 9, cars: 9
Sue 277: akitas: 8, vizslas: 2, cats: 6
Sue 278: trees: 5, goldfish: 7, akitas: 3
Sue 279: perfumes: 9, cars: 8, vizslas: 2
Sue 280: trees: 3, vizslas: 0, children: 0
Sue 281: cars: 7, trees: 2, cats: 5
Sue 282: vizslas: 4, cars: 10, cats: 3
Sue 283: akitas: 10, cats: 3, samoyeds: 9
Sue 284: trees: 7, children: 5, goldfish: 6
Sue 285: cars: 2, perfumes: 5, cats: 7
Sue 286: samoyeds: 5, trees: 10, goldfish: 6
Sue 287: goldfish: 10, perfumes: 4, trees: 7
Sue 288: vizslas: 9, trees: 9, perfumes: 0
Sue 289: trees: 4, goldfish: 9, vizslas: 8
Sue 290: vizslas: 3, cars: 3, trees: 2
Sue 291: goldfish: 2, akitas: 2, trees: 2
Sue 292: children: 1, cars: 0, vizslas: 5
Sue 293: trees: 5, akitas: 4, goldfish: 6
Sue 294: akitas: 3, vizslas: 7, pomeranians: 5
Sue 295: goldfish: 10, vizslas: 3, trees: 1
Sue 296: cars: 2, trees: 1, akitas: 0
Sue 297: akitas: 10, vizslas: 6, samoyeds: 2
Sue 298: children: 5, trees: 1, samoyeds: 9
Sue 299: perfumes: 9, trees: 6, vizslas: 1
Sue 300: akitas: 7, pomeranians: 6, vizslas: 6
Sue 301: cats: 7, children: 6, vizslas: 7
Sue 302: trees: 2, vizslas: 7, samoyeds: 4
Sue 303: goldfish: 0, samoyeds: 10, cars: 4
Sue 304: pomeranians: 9, children: 3, vizslas: 5
Sue 305: akitas: 8, vizslas: 4, cars: 5
Sue 306: akitas: 0, perfumes: 2, pomeranians: 10
Sue 307: akitas: 9, cars: 0, trees: 2
Sue 308: vizslas: 10, goldfish: 8, akitas: 6
Sue 309: trees: 0, cats: 6, perfumes: 2
Sue 310: vizslas: 10, cars: 1, trees: 4
Sue 311: goldfish: 8, perfumes: 6, cats: 3
Sue 312: goldfish: 0, children: 1, akitas: 2
Sue 313: pomeranians: 10, trees: 6, samoyeds: 6
Sue 314: vizslas: 5, akitas: 4, pomeranians: 2
Sue 315: goldfish: 7, trees: 0, akitas: 5
Sue 316: goldfish: 4, vizslas: 5, cars: 7
Sue 317: perfumes: 7, cats: 10, cars: 4
Sue 318: samoyeds: 10, cars: 9, trees: 7
Sue 319: pomeranians: 8, vizslas: 6, cars: 3
Sue 320: cars: 4, cats: 9, akitas: 4
Sue 321: cars: 6, trees: 2, perfumes: 6
Sue 322: goldfish: 1, cats: 2, perfumes: 4
Sue 323: akitas: 6, cats: 5, cars: 8
Sue 324: cats: 4, vizslas: 9, akitas: 0
Sue 325: children: 8, samoyeds: 9, trees: 4
Sue 326: vizslas: 2, samoyeds: 10, perfumes: 7
Sue 327: goldfish: 7, pomeranians: 4, akitas: 10
Sue 328: perfumes: 8, cats: 4, akitas: 10
Sue 329: trees: 0, cars: 9, goldfish: 3
Sue 330: trees: 5, samoyeds: 7, perfumes: 8
Sue 331: cars: 4, perfumes: 2, goldfish: 0
Sue 332: vizslas: 4, pomeranians: 7, akitas: 1
Sue 333: akitas: 4, goldfish: 3, perfumes: 0
Sue 334: samoyeds: 3, akitas: 10, vizslas: 0
Sue 335: goldfish: 1, akitas: 7, vizslas: 6
Sue 336: perfumes: 1, goldfish: 1, pomeranians: 8
Sue 337: children: 5, cars: 4, cats: 4
Sue 338: vizslas: 5, cars: 10, cats: 3
Sue 339: trees: 2, goldfish: 3, cars: 1
Sue 340: trees: 10, goldfish: 6, perfumes: 2
Sue 341: akitas: 5, trees: 6, cats: 3
Sue 342: cars: 10, children: 8, goldfish: 0
Sue 343: cats: 2, akitas: 0, pomeranians: 4
Sue 344: perfumes: 1, vizslas: 3, cars: 3
Sue 345: samoyeds: 8, cats: 5, perfumes: 8
Sue 346: cars: 5, akitas: 10, trees: 2
Sue 347: vizslas: 9, akitas: 9, cars: 3
Sue 348: cars: 3, perfumes: 1, pomeranians: 9
Sue 349: akitas: 1, cars: 4, perfumes: 0
Sue 350: perfumes: 8, vizslas: 2, trees: 6
Sue 351: pomeranians: 5, akitas: 9, cats: 8
Sue 352: pomeranians: 8, vizslas: 3, goldfish: 10
Sue 353: trees: 2, pomeranians: 0, goldfish: 6
Sue 354: cats: 5, akitas: 7, goldfish: 6
Sue 355: goldfish: 6, children: 4, trees: 10
Sue 356: children: 1, trees: 3, akitas: 7
Sue 357: trees: 2, samoyeds: 10, goldfish: 3
Sue 358: samoyeds: 10, cats: 0, goldfish: 0
Sue 359: perfumes: 3, children: 6, pomeranians: 1
Sue 360: cars: 10, pomeranians: 1, samoyeds: 5
Sue 361: samoyeds: 9, pomeranians: 7, perfumes: 6
Sue 362: goldfish: 6, trees: 8, perfumes: 9
Sue 363: samoyeds: 10, pomeranians: 9, children: 10
Sue 364: perfumes: 3, goldfish: 7, cars: 9
Sue 365: cats: 3, children: 4, samoyeds: 8
Sue 366: trees: 0, cars: 10, vizslas: 10
Sue 367: pomeranians: 10, children: 8, perfumes: 2
Sue 368: cars: 5, vizslas: 0, samoyeds: 3
Sue 369: trees: 1, goldfish: 8, cars: 8
Sue 370: vizslas: 0, cars: 2, perfumes: 5
Sue 371: trees: 2, cars: 3, vizslas: 8
Sue 372: trees: 10, children: 9, cats: 1
Sue 373: pomeranians: 3, perfumes: 1, vizslas: 0
Sue 374: vizslas: 0, perfumes: 6, trees: 0
Sue 375: vizslas: 7, pomeranians: 1, akitas: 10
Sue 376: vizslas: 8, trees: 2, cars: 10
Sue 377: perfumes: 9, cats: 5, goldfish: 5
Sue 378: cats: 0, akitas: 10, perfumes: 9
Sue 379: cars: 4, akitas: 1, trees: 1
Sue 380: cars: 4, perfumes: 5, trees: 3
Sue 381: goldfish: 3, akitas: 5, samoyeds: 9
Sue 382: goldfish: 7, perfumes: 5, trees: 5
Sue 383: akitas: 4, cats: 6, cars: 8
Sue 384: children: 6, goldfish: 10, akitas: 7
Sue 385: akitas: 7, vizslas: 5, perfumes: 10
Sue 386: children: 7, vizslas: 10, akitas: 10
Sue 387: goldfish: 6, akitas: 7, trees: 2
Sue 388: vizslas: 6, trees: 1, akitas: 2
Sue 389: cars: 5, vizslas: 3, akitas: 7
Sue 390: vizslas: 4, cats: 8, perfumes: 7
Sue 391: akitas: 3, trees: 0, children: 2
Sue 392: cats: 7, cars: 3, children: 9
Sue 393: trees: 10, vizslas: 3, goldfish: 7
Sue 394: perfumes: 0, goldfish: 7, akitas: 4
Sue 395: cats: 6, cars: 7, vizslas: 0
Sue 396: vizslas: 4, perfumes: 6, goldfish: 5
Sue 397: pomeranians: 8, trees: 1, akitas: 9
Sue 398: goldfish: 7, pomeranians: 6, samoyeds: 9
Sue 399: perfumes: 10, cars: 1, trees: 8
Sue 400: trees: 0, goldfish: 9, children: 6
Sue 401: trees: 1, cars: 6, pomeranians: 8
Sue 402: perfumes: 9, cars: 0, vizslas: 10
Sue 403: samoyeds: 4, akitas: 1, vizslas: 9
Sue 404: perfumes: 0, trees: 2, cars: 4
Sue 405: akitas: 0, perfumes: 5, samoyeds: 4
Sue 406: akitas: 8, vizslas: 6, children: 2
Sue 407: children: 1, trees: 8, goldfish: 10
Sue 408: pomeranians: 4, trees: 10, cars: 9
Sue 409: perfumes: 5, vizslas: 5, akitas: 4
Sue 410: trees: 1, akitas: 10, vizslas: 6
Sue 411: samoyeds: 0, goldfish: 9, perfumes: 7
Sue 412: goldfish: 7, samoyeds: 10, trees: 1
Sue 413: samoyeds: 0, pomeranians: 10, vizslas: 6
Sue 414: children: 2, cars: 10, samoyeds: 2
Sue 415: trees: 2, goldfish: 8, cars: 0
Sue 416: samoyeds: 4, goldfish: 9, trees: 2
Sue 417: trees: 8, akitas: 10, perfumes: 3
Sue 418: samoyeds: 9, goldfish: 2, cars: 1
Sue 419: akitas: 2, perfumes: 8, trees: 2
Sue 420: children: 3, goldfish: 6, perfumes: 5
Sue 421: akitas: 8, perfumes: 2, samoyeds: 6
Sue 422: vizslas: 10, akitas: 4, pomeranians: 3
Sue 423: cats: 8, perfumes: 3, trees: 4
Sue 424: cars: 2, children: 4, pomeranians: 8
Sue 425: pomeranians: 4, samoyeds: 2, goldfish: 4
Sue 426: perfumes: 6, cars: 4, goldfish: 4
Sue 427: akitas: 0, goldfish: 7, perfumes: 5
Sue 428: perfumes: 4, cars: 3, akitas: 5
Sue 429: trees: 0, vizslas: 0, goldfish: 1
Sue 430: perfumes: 4, vizslas: 2, cars: 7
Sue 431: goldfish: 7, pomeranians: 8, trees: 0
Sue 432: goldfish: 7, children: 9, trees: 3
Sue 433: akitas: 1, vizslas: 10, trees: 2
Sue 434: perfumes: 2, cars: 4, goldfish: 10
Sue 435: pomeranians: 6, vizslas: 9, trees: 1
Sue 436: cars: 9, trees: 0, goldfish: 0
Sue 437: trees: 1, goldfish: 1, vizslas: 8
Sue 438: goldfish: 7, samoyeds: 8, children: 2
Sue 439: children: 1, cats: 7, vizslas: 8
Sue 440: cats: 2, pomeranians: 6, goldfish: 4
Sue 441: perfumes: 7, cats: 3, vizslas: 6
Sue 442: akitas: 4, samoyeds: 5, cars: 2
Sue 443: akitas: 3, perfumes: 3, cats: 9
Sue 444: perfumes: 10, akitas: 6, trees: 0
Sue 445: cars: 5, children: 9, perfumes: 8
Sue 446: vizslas: 10, cars: 3, perfumes: 5
Sue 447: children: 9, perfumes: 1, cars: 10
Sue 448: akitas: 0, goldfish: 8, trees: 3
Sue 449: cars: 7, akitas: 8, children: 3
Sue 450: cars: 4, akitas: 9, cats: 0
Sue 451: perfumes: 4, samoyeds: 5, goldfish: 6
Sue 452: perfumes: 10, akitas: 1, cars: 7
Sue 453: trees: 1, goldfish: 3, vizslas: 6
Sue 454: goldfish: 8, pomeranians: 6, trees: 10
Sue 455: akitas: 5, vizslas: 8, goldfish: 10
Sue 456: cats: 5, trees: 4, samoyeds: 0
Sue 457: perfumes: 8, cars: 0, cats: 3
Sue 458: akitas: 1, trees: 10, vizslas: 2
Sue 459: vizslas: 6, akitas: 3, children: 10
Sue 460: perfumes: 7, trees: 9, goldfish: 8
Sue 461: children: 6, vizslas: 4, perfumes: 5
Sue 462: vizslas: 6, akitas: 8, perfumes: 9
Sue 463: goldfish: 8, cars: 4, trees: 10
Sue 464: pomeranians: 8, cars: 5, vizslas: 0
Sue 465: cats: 10, goldfish: 7, akitas: 1
Sue 466: cats: 2, children: 1, cars: 6
Sue 467: perfumes: 3, samoyeds: 6, cars: 0
Sue 468: samoyeds: 10, pomeranians: 6, trees: 2
Sue 469: children: 2, perfumes: 2, pomeranians: 4
Sue 470: cats: 1, perfumes: 5, vizslas: 9
Sue 471: vizslas: 5, perfumes: 2, akitas: 7
Sue 472: samoyeds: 8, goldfish: 6, cats: 1
Sue 473: goldfish: 10, perfumes: 9, cars: 4
Sue 474: samoyeds: 0, cars: 4, vizslas: 4
Sue 475: trees: 2, cars: 7, akitas: 8
Sue 476: vizslas: 3, perfumes: 5, goldfish: 1
Sue 477: cats: 7, cars: 4, trees: 1
Sue 478: vizslas: 8, akitas: 3, goldfish: 0
Sue 479: cars: 6, cats: 3, perfumes: 2
Sue 480: goldfish: 1, children: 9, vizslas: 3
Sue 481: pomeranians: 5, vizslas: 1, cars: 10
Sue 482: children: 5, perfumes: 5, cats: 1
Sue 483: perfumes: 2, goldfish: 7, trees: 6
Sue 484: akitas: 2, goldfish: 4, perfumes: 10
Sue 485: samoyeds: 3, goldfish: 0, akitas: 1
Sue 486: trees: 8, vizslas: 9, goldfish: 0
Sue 487: goldfish: 8, samoyeds: 0, trees: 0
Sue 488: perfumes: 7, cars: 5, trees: 0
Sue 489: vizslas: 3, pomeranians: 2, perfumes: 5
Sue 490: cars: 5, perfumes: 5, akitas: 5
Sue 491: children: 8, trees: 1, pomeranians: 4
Sue 492: pomeranians: 0, akitas: 1, vizslas: 8
Sue 493: akitas: 10, perfumes: 10, samoyeds: 8
Sue 494: perfumes: 6, vizslas: 4, cats: 6
Sue 495: children: 6, pomeranians: 5, samoyeds: 4
Sue 496: vizslas: 1, trees: 5, akitas: 1
Sue 497: vizslas: 10, perfumes: 10, pomeranians: 3
Sue 498: samoyeds: 3, trees: 2, cars: 5
Sue 499: cats: 6, children: 3, perfumes: 0
Sue 500: pomeranians: 10, cats: 3, vizslas: 5
"""

def checkSue(known, line):
    """
    :param known: the known dict of attribes given in problem statement
    :param line: a DATA lines (from above)
    """

    # words, with trailing char stripped on all but last
    words = line.split()
    w = [word[:-1] for word in words[2:-1]
    cand = {}
    for i in [0, 2, 4]:
        cand[w[i]] = int(w[i + 1])
    }

    for key in candidateSue_d:
        if known[key] != cand[key]
            return False

    return True


def main():

    knownSue_d = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }



if __name__ == '__main__':
    main()

# EOF

