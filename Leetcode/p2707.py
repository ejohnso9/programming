#!/usr/bin/env python3


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        # words = sorted(dictionary, key=lambda w: len(w), reverse=True)
        for w in dictionary:
            i = s.find(w)
            while -1 < i:
                n = len(w)
                s = s[:i] + '_' * n + s[i+n:]
                i = s.find(w, i + n)

        return len([c for c in list(s) if c != '_'])


if __name__ == '__main__':
    solution = Solution()
    rv = solution.minExtraChar(
        s="rkmsilizktprllwoimafyuqmeqrujxdzgp",
        dictionary=[
            "afy", "lyso", "ymdt", "uqm", "cfybt", "lwoim", "hdzeg", "th", "rkmsi", "d", "e", "tp", "r", "jx", "tofxe",
            "etjx", "llqs", "cpir", "p", "ncz", "ofeyx", "eqru", "l", "demij", "tjky", "jgodm", "y", "ernt", "jfns",
            "akjtl", "wt", "tk", "zg", "lxoi", "kt",
        ])
    print(rv)
