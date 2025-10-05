#!/usr/bin/env python

"""
DISCUSSION
    I thought I would add a few words on general approach...
At first I was thinking to use itertools.product() to just go over all
the possible 3-char lowercase keys: 'aaa', 'aab', ..., 'aaz', 'aba',
'abb', ..., 'abz', ..., 'zzz'.

    But the problem has basically already stated that an ASCII encoding
is being used, and crypt text is exclusively or-ed with the key. My
expectation is that the message is very likely to be exclusively
printable text, and nearly all characters. There might be a few
punctuation characters, parenthesis, braces, etc, but with the exception
of maybe CR and LF (ASCII chars 13 and 10 respectively), there probably
isn't going to be any chars in the control ranges (characters with
decimal code < 32).

    So, I can just look at every 3rd character and build a list of
letters that lead to either 0 or a minimal of characters decoded in
the < 32 range. This is not guaranteed to work, but seems like a
sensible starting point, noting that 3 * 26 is 78 while 26 ** 3 is
17576, a number more than 2 orders of magnitude greater.



# Frequency data from:
#   https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
#
#  E   11.1607%    56.88   M   3.0129% 15.36
#  A   8.4966%     43.31   H   3.0034% 15.31
#  R   7.5809%     38.64   G   2.4705% 12.59
#  I   7.5448%     38.45   B   2.0720% 10.56
#  O   7.1635%     36.51   F   1.8121% 9.24
#  T   6.9509%     35.43   Y   1.7779% 9.06
#  N   6.6544%     33.92   W   1.2899% 6.57
#  S   5.7351%     29.23   K   1.1016% 5.61
#  L   5.4893%     27.98   V   1.0074% 5.13
#  C   4.5388%     23.13   X   0.2902% 1.48
#  U   3.6308%     18.51   Z   0.2722% 1.39
#  D   3.3844%     17.25   J   0.1965% 1.00
#  P   3.1671%     16.14   Q   0.1962% (1)

"""


import sys


# GLOBAL DATA
HI_9 = 'EARIOTNSL'.split()  # the 9 most-common letters (in uppercase)

# custom codes character class encoding
CHARACTER_CLASS_DATA = [
    (97, 122, 'LC'),
    (65, 90, 'UC'),
    (60, 71, 'DIG'),
    (32, 32, 'SPACE'),
    # <32 is CTRL
    # else 'PUNCT'
]



def decode(loi: list[int], char_i: int, offset: int) -> list[int]:
    """
    TODO
    """

    n = len(loi)
    char_i
    i = 0
    rv_ls = list()
    while True:
        idx = i + offset
        if idx > n - 1:
            break
        if i % 3 == offset:
            value = loi[i] ^ char_i
            rv_ls.append(value)
        i += 1
        if i > n - 1:
            break

    return rv_ls


def countUnder32(loi: list[int]) -> int:
    """
    Count of the number of ints strictly less than 32
    """

    return sum(1 for i in loi if i < 32)



def hist(loi):
    """
    construct a dict of the counts of each int value, keyed by the
    int value
    """

    d = dict()

    for i in loi:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1

    return d


def make_str(loi):
    def f(i):
        return chr(i) if i != 80 else ' '

    return ''.join([f(i) for i in loi])


def freq_dict(ints: list[int]) -> dict:
    counts_d = {}

    for i in ints:
        # c = chr(i)
        try:
            counts_d[i] += 1
        except KeyError:
            counts_d[i] = 1

    return counts_d



def main(ints: list[int]):

    counts_d = freq_dict(ints)
    print()
    print('-' * 72)
    print(counts_d)
    print('-' * 72)
    print()

    n3 = len(ints) // 3
    _a = [ints[i] * 3 + 0 for i in range(n3)]
    _b = [ints[i] * 3 + 1 for i in range(n3)]
    _c = [ints[i] * 3 + 2 for i in range(n3)]

    # print(_a)
    # print(''.join([chr(c) for c in _a]))

    counts_d = freq_dict(_a)
    print(counts_d)
    tup_ls = sorted([(count, i) for i, count in counts_d.items()], reverse=True)
    for count, i in tup_ls[:12]:
        print(count, i)


    sys.exit()

    atoz = range(ord('a'), ord('z') + 1)  # 97 - 122 
    for key_i in atoz:
        ints = [key_i ^ _i for _i in _a]
        counts_d = freq_dict(ints)
        tup_ls = sorted([(count, k) for k, count in counts_d.items()], reverse=True)
        s = ''.join([t[1] for t in tup_ls][:10])
        # print(key_i, f"'{s}'")
        print(key_i, tup_ls)
        print()


    # convert the ints to string
    # loi = [int(s) for s in ints.split(sep=',')]
    # n = len(loi)
    # r = n % 3
    # print(f"{n} total ints to process")
    # print(f"{n} % 3 is: {r}")

    # d = hist(loi)
    # tups = [(k, v) for k, v in d.items()]
    # tups.sort(key=lambda t: t[1])
    # for t in tups:
    #     print(t)

    # print(make_str(loi))

    # lot = list()  # list of tuples
    # for c in range(ord('a'), ord('z') + 1):
    #     decoded_loi = decode(loi, c, 0)
    #     count = countUnder32(decoded_loi)
    #     # lot.append((chr(c), count))
    #     print(f"'{c}' = {count}")

    # print(lot)

    print("done.")
    return 0  # normal main() exit


# ENTRY POINT
if __name__ == '__main__':
    with open('pe59.txt', 'r') as fd:
        line = fd.readline()
    ints = [int(w) for w in line.split(sep=',')]
    # print(ints)

    main(ints) # list of ints


# EOF


