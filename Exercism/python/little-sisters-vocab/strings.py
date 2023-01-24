"""Functions for creating, transforming, and adding prefixes to strings."""


# pylint: disable=W1405


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return f"un{word}"


def make_word_groups(in_words):
    """Transform a list containing a prefix and words into a string with the
    prefix followed by the words with prefix prepended.

    :param in_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = in_words[0]
    return ' :: '.join([prefix] + [f"{prefix}{word}" for word in in_words[1:]])


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    if word.endswith('ness'):
        base = word[:-4]
        rv = f"{base[:-1]}y" if base.endswith('i') else base
    else:
        rv = word

    return rv


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    return sentence[:-1].split()[index] + "en"


def main():
    # local testing
    input_data = [
        'Look at the bright sky.',
        'His expression went dark.',
        'The bread got hard after sitting out.',
        'The butter got soft in the sun.',

        'Her eyes were light blue.',
        'The morning fog made everything damp with mist.',
        'He cut the fence pickets short by mistake.',
        'Charles made weak crying noises.',

        'The black oil got on the white dog.',
    ]

    index_data = [
        -2, -1, 3, 3,
        -2, -3, 5, 2,
        1,
    ]

    result_data = [
        'brighten', 'darken', 'harden', 'soften',
        'lighten', 'dampen', 'shorten', 'weaken',
        'blacken',
    ]

    for sentence, index, exp in zip(input_data, index_data, result_data):
        act = adjective_to_verb(sentence, index)
        if act != exp:
            raise RuntimeError(exp, act)


    # input_data = ['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture']
    # print(make_word_groups(input_data))


if __name__ == '__main__':
    main()

# EOF
