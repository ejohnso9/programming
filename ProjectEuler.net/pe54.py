#!/usr/bin/env python
# ProjectEuler.net Problem #54
# https://projecteuler.net/problem=54

"""
PURPOSE
    I am writing code in this solution without respect for running time.
    Like some other sites (e.g., Advent of Code), it's only about whether
    you get the answer, not how many milliseconds (or seconds or minutes)
    it took to get there.

    I am writing this code pretty much the same way I write production code
    to become part of my Company's projects. This code is being written with
    the idea that others may read, review, and judge it. I am trying to create
    code that is "decently" documented, well-organized, commented, understandable,
    flexible, and hopefully easy to understand and maintain (yet often still
    less than "perfect"). I'm not playing code golf and I'm not looking to try
    to beat out other competitors on run time.

DESCRIPTION
    In the card game poker, a hand consists of five cards and are
    ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

    If two players have the same ranked hands then the rank made up of
    the highest value wins; for example, a pair of eights beats a pair
    of fives (see example 1 below). But if two ranks tie, for example,
    both players have a pair of queens, then highest cards in each hand
    are compared (see example 4 below); if the highest cards tie then
    the next highest cards are compared, and so on.

    Consider the following five hands dealt to two players:

Hand    Player 1            Player 2            Winner
-----   --------------      --------------      --------
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD
        Pair of Fives       Pair of Eights      Player 2

2       5D 8C 9S JS AC      2C 5C 7D 8S QH
        Highest card Ace    Highest card Queen  Player 1

3       2D 9C AS AH AC      3D 6D 7D TD QD
        Three Aces          Flush with Diamonds Player 2

4       4D 6S 9H QH QC      3D 6D 7H QD QS
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven  Player 1

5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        Full House          Full House
        with Three Fours    with Three Threes   Player 1

The file, p054_poker.txt, contains one-thousand random hands dealt to two
players. Each line of the file contains ten cards (separated by a single
space): the first five are Player 1's cards and the last five are Player
2's cards. You can assume that all hands are valid (no invalid
characters or repeated cards), each player's hand is in no specific
order, and in each hand there is a clear winner.

How many hands does Player 1 win?


DISCUSSION / STRATEGY
    The instructions seem to overlook the fact that hands can tie.
    For example:
        KH KC 3D 8H JS  # pair of kings, J-high (followed by 8, 3)
        KS KD 3C 8S JD  # pair of kings, J-high (followed by 8, 3)

    I didn't know initially if any "full hand ties" actuall appear in
    the data file - apparently they do not. A more general solution
    would have to deal with that.

    The given table follows typical poker books, listing a "Royal
    Flush" as a kind of hand in its own right.  But it's really not,
    it's a straight flush. It happens to be the highest possible straight
    flush but is not a fundamentally different kind of hand. In the same
    vein, one might as well refer to 3 aces as "Royal Trips" or something,
    because aces are the highest you can have, but no poker players
    refer to a "Royal Full House" or "Royal Trips".

    In the ranking system I will implement, as far as rank is concerned,
    a Royal Flush is just a Straight Flush, ties between Straight Flushes
    being resolved by looking at the rank of the cards involved.

    Again, as it turns out (since the data file is random hands and not
    constructed hands), there aren't any Royal Flush, Stright Flush,
    nor Four of a Kind hands.

    My ranking values are:
        0 for high card,
        1 for a pair,
        2 for two pair,
        ...
        8 for straight flush

    I often just embed data files as text chunks within the code, then
    create functions to process that into some sort of structured data.
    Because this data file is rather long (1000 lines), I started using
    code to just pull it straight from the web on the fly, at each run
    but when I ran into problems and started looking for other
    solutions, they were reading local files so I switched to just read
    local data file. Loading from the internet was hardly a noticeable
    delay.

    I made a couple of errors in implementing this solution. One was
    that when you have two hands tied in one or two pairs, the other
    cards that you look at to resolve the tie have to be sorted in
    Reverse order, not forward order.

    The second was that when you have the ranks in sorted order, the
    high card being 4 more than the low card does not necessarily imply
    a straight. It does if you know you have 5 different ranks in the
    hand, which is what I was thinking because I build a dict with the
    sort of information and such a check is made in another place, but I
    made a mistake in implementing the isFlush evaluation.

    This raises the whole subject of software correctness, which I'm not
    going to get into here.

    The data file has no "Low Straight" hands: A2345. If one has
    remapped the value of Ace to be 14, A2345 should lose to 23456
    stright. But if you just look for the high card, code may well think
    that A2345 beats 23456. It does not. Yet you can get the right
    answer at ProjectEuler for Problem #54 without handling this case
    correctly, which leads me to mention "sufficiency" versus
    "over-engineering". PE #54 solutions don't need to solve ties on any
    hand ranks other than high card, one pair, and straight. That's not
    sufficient to implement a general poker solution. So, are PE #54
    solutions that ignore the low straight, don't resolve ties for two
    pair, three-of-a-kind, etc. "deficient"?

    I would argue that they are not. Instead the code should be
    documented to be sufficient for a particular purpose, (or documented
    to be insufficient as a general solution). The goal here is to find
    the correct answer for PE #54. Did I "cheat"? Well... sort of, from
    certain perspectives, I did. Yet being able to look around on the
    Internet and find code that addresses certain issues is also a
    valuable skill. The programmer that tries to solve everything from
    first principles is going to spend a lot of time re-solving problems
    that he could have just "stolen" some public code forums. That directly
    translates to more development time and more (often "crufty") code
    that has to be maintained in a project.

    I compared my own code against other's code to find where my error
    was and then fixed my own code. I did not plagiarize. My code was
    first giving 385 (which seems unusually low for random hands -
    that's pretty skewed toward Player 2 wins).  After one of the fixes
    I was getting 377, which is one off from the correct answer.

    I'm showing "The Dreamshire solution", and not claiming it is mine.
    My ranking code is my own. I think it's pretty good. It is not as
    short as the Dreamshire solution, which is impressive. It's also what
    Brian Kernighan would term "clever". (Look up Kernighan's Law. That
    may seem like a cute joke at first, but I have found that in
    practice, there is real wisdom there, especially for multi-person
    projects where others may be looking at a clever solution and
    misunderstand it, be tempted to "fix" or re-factor it, or simply
    re-implement something themselves because they are not sure the
    clever solution is correct or what it really does. Believe me, this
    is real - When that happens, it directly leads to code bloat as well
    as multiple alternatives for doing the same thing which may not be
    exactly identical. Which will then lead a third developer to ignore
    both solutions and create yet a third. (Again, I have actually seen
    this take place in real projects.) 

"""

from collections import Counter
import requests  # standard module under Python 3: https://pypi.org/project/requests/


# GLOBAL DATA
NL = '\n'
DATA_URL = "https://projecteuler.net/project/resources/p054_poker.txt"
RANK_REMAP = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, }

# INDEX into (rank, suit) 2-tuple by SYMCONST
RANK, SUIT = 0, 1

PLAYER_1 = 1  # SYMCONST for "Player 1"
PLAYER_2 = 2  # SYMCONST for "Player 2"

# where I am indexing two data structures, use 0, 1 instead of 1, 2
P1, P2 = 0, 1  # indices into Player 1 structure, Player 2 structure
PLAYERS = [P1, P2]  # both players

# we all know magic numbers are bad, right?
"""
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
"""
RANK_HIGH_CARD = 0
RANK_ONE_PAIR = 1
RANK_TWO_PAIR = 2
RANK_THREE_OF_A_KIND = 3
RANK_STRAIGHT = 4
RANK_FLUSH = 5
RANK_FULL_HOUSE = 6
RANK_FOUR_OF_A_KIND = 7
RANK_STRAIGHT_FLUSH = 8

RANK_NAMES = [
    'RANK_HIGH_CARD',
    'RANK_ONE_PAIR',
    'RANK_TWO_PAIR',
    'RANK_THREE_OF_A_KIND',
    'RANK_STRAIGHT',
    'RANK_FLUSH',
    'RANK_FULL_HOUSE',
    'RANK_FOUR_OF_A_KIND',
    'RANK_STRAIGHT_FLUSH',
]

RANK_TO_NAME_D = {i: name for i, name in enumerate(RANK_NAMES)}


def getHandRep(line):
    """
    Convert a line of 10 cards as read from the input data file into
    two 5-element lists of tuples for internal representation.

    :param line: text line from input file
    :return: [ [5-element list of 2-tuples], [5-element list of 2-tuples] ]
    """

    def repTuple(card):
        """
        Represent a card as: (int, str) where suit is 1-char str in list("SHDC")
        :param card: 2-char str, the data file representation (e.g., "TC" for ten of clubs)
        :return: (rank, suit)  # type: (int, str)
        """

        rank, suit = list(card)  # str, str
        rank = RANK_REMAP[rank] if rank in RANK_REMAP else int(rank)

        return rank, suit  # int, str

    cards = line.split()  # list of 2-char "cards" (e.g., ['TC', 'AS', '5D', ...])

    return [
        [repTuple(card) for card in cards[:5]],
        [repTuple(card) for card in cards[5:]],
    ]


def rankHand(hand):
    """
    Given a hand, assign the numeric rank, basically just as table
    is given in the problem description:

        0: High Card: Highest value card.
        1: One Pair: Two cards of the same value.
        2: Two Pairs: Two different pairs.
        3: Three of a Kind: Three cards of the same value.
        4: Straight: All cards are consecutive values.
        5: Flush: All cards of the same suit.
        6: Full House: Three of a kind and a pair.
        7: Four of a Kind: Four cards of the same value.
        8: Straight Flush: All cards are consecutive values of same suit.

    :param hand: list of 2-tuples
    :return: int rank value
    """

    ranks = sorted([card[RANK] for card in hand])  # list of each rank value, ascending order
    rankSet = set([card[RANK] for card in hand])  # different ranks appearing in the hand
    rankCount_d = {rank: ranks.count(rank) for rank in rankSet}  # { rank: nCardsOfThatRank }

    # list of counts for the diff. ranks (e.g., 4-of-a-kind would be [4, 1] or [1, 4]):
    rankCounts = list(rankCount_d.values())

    isFlush = all([card[SUIT] == hand[0][SUIT] for card in hand])

    # special case for the A2345 straight
    lowStraight = all([r in ranks for r in [14, 2, 3, 4, 5]])

    # top card is 4 more than bottom card in a sequence
    maxRank = max(ranks)  # rank of the highest card in the hand
    straightRanks = list(range(maxRank - 4, maxRank + 1))
    isStraight = lowStraight or all([r in ranks for r in straightRanks])

    # return the rank value
    if isStraight and isFlush:
        rank = RANK_STRAIGHT_FLUSH
    elif isFlush:
        rank = RANK_FLUSH
    elif isStraight:
        rank = RANK_STRAIGHT
    elif len(rankCounts) == 2:
        # 5-0 not possible: we either have:
        #   4 of one rank and 1 of another
        #   OR: 3 of one rank and 2 of another
        rank = RANK_FOUR_OF_A_KIND if 4 in rankCounts else RANK_FULL_HOUSE
    elif 3 in rankCounts:
        rank = RANK_THREE_OF_A_KIND
    elif rankCounts.count(2) == 2:
        rank = RANK_TWO_PAIR
    elif rankCounts.count(2) == 1:
        rank = RANK_ONE_PAIR
    elif rankCounts.count(1) == 5:
        # 5 different ranks that's not straight or flush
        rank = RANK_HIGH_CARD
    else:
        raise RuntimeError("LOGIC PROBLEM")

    return rank


def determineWinner(hands, rank):
    """
    When the two hands are of the same rank, which hand is higher?

    NB: This implementation is sufficient for the given data file, but is
        NOT SUFFICIENT for poker hands in general!

    :param hands: list of the two hands (of same rank)
    :param rank: the rank of both hands
    :return: PLAYER_1 or PLAYER_2
    """

    hand1, hand2 = hands

    if rank == RANK_HIGH_CARD:
        # high-card hand ties can be ordered by natural list order
        lists = [sorted([card[RANK] for card in hand], reverse=True) for hand in hands]
        winner = PLAYER_1 if lists[0] > lists[1] else PLAYER_2

    # FORTUITOUS: this same branch actually works for both one pair and two pair comparisons!
    elif rank in [RANK_ONE_PAIR, RANK_TWO_PAIR]:
        ranks = [sorted([card[RANK] for card in hand]) for hand in hands]  # list of each rank value, ascending order
        rankSets = [set([card[RANK] for card in hand]) for hand in hands]  # different ranks appearing in the hand
        countDicts = [{rank: ranks[p].count(rank) for rank in rankSets[p]} for p in PLAYERS]  # { rank: nCardsOfThatRank }
        pairRanks = [sorted([rank for rank, count in countDicts[p].items() if count == 2]) for p in PLAYERS]

        if pairRanks[P1] != pairRanks[P2]:
            # natural sort order of the lists takes care of same top pair, or different top pair
            winner = PLAYER_1 if pairRanks[P1] > pairRanks[P2] else PLAYER_2
        else:
            # same one or two pair: have to look at the other 3 cards or 1 other card
            otherRanks = [sorted([rank for rank, count in countDicts[p].items() if count == 1], reverse=True)
                          for p in PLAYERS]
            winner = PLAYER_1 if otherRanks[P1] > otherRanks[P2] else PLAYER_2

    elif rank == RANK_STRAIGHT:
        # the only ties happen on non-tied high card
        highCard_l = [max([card[RANK] for card in hand]) for hand in hands]
        winner = PLAYER_1 if highCard_l[P1] > highCard_l[P2] else PLAYER_2

    else:
        raise NotImplemented

    return winner  # PLAYER_1 or PLAYER_2


def pe54(lines):

    # The Dreamshire solution:
    #   https://blog.dreamshire.com/project-euler-54-solution/
    # filename = 'p054_poker.txt'  # the local hands data file
    # hands = (line.split() for line in open(filename))
    # values = {r: i for i, r in enumerate('23456789TJQKA', 2)}
    # straights = [(v, v - 1, v - 2, v - 3, v - 4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
    # ranks = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (), (), (3, 2), (4, 1)]

    # def hand_rank(hand):
    #     score = list(zip(*sorted(((v, values[k]) for
    #                          k, v in Counter(x[0] for x in hand).items()), reverse=True)))
    #     score[0] = ranks.index(score[0])

    #     if len(set(card[1] for card in hand)) == 1:
    #         score[0] = 5  # flush

    #     if score[1] in straights:
    #         score[0] = 8 if score[0] == 5 else 4  # str./str. flush

    #     return score

    # print("P1 wins", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands))
    # END Dreamshire solution


    playerCounts_d = {
        PLAYER_1: 0,
        PLAYER_2: 0,
    }

    # keep track of the ranks found (this is debugging support)
    rankStats_lol = [
        [0] * 9,  # Player 1: 1 count element for each possible rank
        [0] * 9,  # Player 2: 1 count element for each possible rank
    ]

    # for every 2 poker hands in the data file...
    for i, line in enumerate(lines):
        dsCards = line.split()
        hand1, hand2 = getHandRep(line)
        rank1, rank2 = [rankHand(hand) for hand in [hand1, hand2]]
        # dsRank1, dsRank2 = hand_rank(dsCards[:5]), hand_rank(dsCards[5:])

        # tabulate stats
        rankStats_lol[0][rank1] += 1
        rankStats_lol[1][rank2] += 1

        if rank1 != rank2:
            player = PLAYER_1 if rank1 > rank2 else PLAYER_2
        else:
            player = determineWinner([hand1, hand2], rank1)

        playerCounts_d[player] += 1

        # DEBUGGING
        # stop if my winning player not same as Dreamstate winning player
        # if (player == PLAYER_1 and dsRank2 > dsRank1) or (player == PLAYER_2 and dsRank2 < dsRank1):
        #     # no longer happening
        #     print("PROBLEM")

        # I was curious to have a look at tied hands, and quickly discovered that hands only
        # tie on 3 different ranks: high card, one pair, straight. And of the straights that tie,
        # there is only one such deal and the high card in the straights is not the same!
        # So, that is information specific to the given data file, and leads to an optimization of developer
        # time to get the right answer for PE #54. It also means that this code should not be used against
        # general data files of that form (i.e., anything other than the exact one given for PE #54).
        #
        # ignoreRanks = [RANK_HIGH_CARD, RANK_ONE_PAIR]
        # if rank1 == rank2 and rank1 not in ignoreRanks:
        #     print()
        #     print(f"hand1: {hand1}, rank: {RANK_TO_NAME_D[rank1]}")
        #     print(f"hand2: {hand2}, rank: {RANK_TO_NAME_D[rank2]}")

    return playerCounts_d


def main():
    filename = 'p054_poker.txt'  # the local hands data file

    # My solution (no longer fetching via Inet)
    # fetch the data off the web, print each player's winning count
    # resp = requests.get(DATA_URL)
    with open(filename, 'r') as fd:
        lines = fd.readlines()

    playerCounts = pe54(lines)
    for p in [PLAYER_1, PLAYER_2]:
        print(f"player {p}: {playerCounts[p]}")

    # 376 is the accepted answer - see discussion


if __name__ == '__main__':
    main()


# EOF

