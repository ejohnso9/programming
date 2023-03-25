"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


# pylint: disable=W1405
# pylint: disable=W0105
"'A foolish consistency is the hobgoblin of little minds.'"
'   --GvR'


# GLOBAL DATA
ROYALTY = 'JQK'  # single-char card values of value 10 (int)


# I think I generally support the idea of putting in type annotations.
# That said, I've not done it to this code (which is all pretty simple).
# I think if Exercism wants to steer learners towards that (which seems
# like a sound idea to me), they should start by including it in their
# code boilerplate from the "get-go".
def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card == 'A':
        return 1

    if card in ROYALTY:
        return 10

    return int(card)


def higher_card(c1, c2):
    """Determine which card has a higher value in the hand.

    :param c1, c2: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # pylint: disable=invalid-name

    v1, v2 = [value_of_card(c) for c in (c1, c2)]
    if v1 == v2:
        return c1, c2

    if v1 > v2:
        return c1

    return c2


def value_of_ace(c1, c2):  # pylint: disable=invalid-name
    """Calculate the most advantageous value for the ace card.

    :param c1, c2: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    # If it weren't for the fixed unit tests, I would probably modify value_of_card()
    # to take an 'ace_low' argument instead of define this. As the unit-test code
    # is not under my control, I defined this alternate func to value_of_card().
    def card_value(card):
        if card == 'A':
            return 11

        if card in ROYALTY:
            return 10

        return int(card)

    hand_total = sum(card_value(card) for card in [c1, c2])
    return 11 if hand_total <= 10 else 1


def is_blackjack(c1, c2):  # pylint: disable=invalid-name
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param c1, c2: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if 'A' not in (c1, c2):
        return False  # can't have a natural BJ w/o an 'A'
    # assert: one of the two cards *is* an 'A'!
    non_ace = c2 if c1 == 'A' else c1

    # Yes, I like the idea just testing: in str
    # ORIG: return non_ace in list('JQK') + ['10']
    # But have to be careful b/c this is not valid syntax:
    #   return non_ace in JQK + ['10']
    return non_ace in list(ROYALTY) + ['10']


def can_split_pairs(c1, c2):  # pylint: disable=invalid-name
    """Determine if a player can split their hand into two hands.

    :param c1, c2: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    # NB: the following pylint disable applies to just the next line
    #   and the one in the function def applies to just that line
    #   but in can_double_down(), the disable applies to the block!
    f = value_of_card  # pylint: disable=invalid-name
    return f(c1) == f(c2)


def can_double_down(c1, c2):
    """Determine if a blackjack player can place a double down bet.

    :param c1, c2: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    # pylint: disable=invalid-name,line-too-long

    # this alternate implementation is 1 line instead of 3:
    #
    #    return sum(value_of_card(c) for c in [c1, c2]) in [9, 10, 11]
    #
    # Is that better? Well, it's one line. Is that clearer overall? I'm not sure.
    #
    # I'm often trying to write for the future me or some other poor sod that got assigned to maintain my
    # code after I have moved on to greener pastures. If someone came in here cold, after 6 months, 3.5 years
    # (effectively first time ever), how can I best communicate what is going on here?
    # When I make a local alias like:
    #   f = value_of_card  # I'm saying: "First of all, NB: I'm going to be using this function."
    # And then I see something like: sum(f(c) for c in ...)
    # I immediately think: """
    #   Oh! I see where that 'f' you mentioned is getting called:
    #       f => some function
    #       f(c) => return value of that 'f' function called with some 'c' arg.
    #   Oh, I see: this code is adding up the functional values on some 'c's (cees): sum(f(c) ...
    #       I see, the cees are: [c1, c2]
    #   It's kinda like map(), but explicitly calling 'f' and using a comprehension instead of map().
    # """
    #  https://docs.python.org/3/reference/expressions.html#generator-expressions
    #  https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    #
    # Not that there isn't anything described above that isn't available in the 1-liner...
    #   it's all there as well, but it's more dense, there's no: "total" or "f(c)" hints.
    #
    # As you said, it may be splitting hairs: sometimes I feel like making a declaration like:
    #   f = value_of_card
    # makes code below much easier to read.
    # Other days, I read code I have written (or one of my co-workers has written) as below and I think:
    # """Why the hell don't you just put 'value_of_card' in at the one-and-only-place it is used?!?
    #  That would be one line instead of two! (Like... DUH!)"""
    # I think it depends on what day of the week it is. ;)
    # (Or how broadly or narrowly I am thinking right at that very moment, when I read it.
    # Which may well be different from how broadly I (or someone else) was thinking at the moment it got written.)
    #

    f = value_of_card                    # NB1: The function of interest being employed here is: 'value_of_card'
    total = sum(f(c) for c in [c1, c2])  # NB2: See how I sum up the functional value of some things: f(c) for ...
                                         #      [c1, c2] to be specific, but note: sum(f(c) <for-clause>)
    return total in [9, 10, 11]          # NB3: logical value of *this* function is whether 'total' is one of ...
                                         # could also be:
                                         # return 9 >= total >= 11
                                         # Is that clearer? Maybe, but note 'total' is a discreet int, not float.

# EOF
