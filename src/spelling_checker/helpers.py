import string
from collections import Counter
from pathlib import Path

import regex


def get_words(text):
    """
    Returns all words in lowercase from the given text in a list.
    :param text: string
    :return: list of strings
    """
    return regex.findall(r'\w+', text.lower())


def get_project_root():
    return Path(__file__).parent


# TODO store the default word frequency list as file instead of computing it every time.
def get_word_freq_dict():
    """
    Returns the default {word:raw_freq} dictionary, e.g.
    {'the': 11, 'project': 5, 'gutenberg': 5, ...}
    :return: dict (Counter)
    """
    default_corpus_filepath = str(get_project_root()) + '/data/bigtext.txt'
    return Counter(get_words(open(default_corpus_filepath, 'r').read()))


def get_word_freq(word):
    """
    If the given word exists in the dictionary, it returns the raw frequency count for it;
    otherwise returns 0.
    :param word: string
    :return: int
    """
    d = get_word_freq_dict()
    try:
        return d[word]
    except KeyError:
        return 0


def get_total_word_count_in_dict(d):
    """
    :param d: a word freq dict
    :return: int
    """
    return sum(d.values())


def get_known_words(words, dict=get_word_freq_dict()):
    """
    Returns a subset of given words which appear in the dictionary / corpus.
    :param words: list of strings
    :param dict: a dict of known words, defaults to using the project corpus
    :return: a set of strings
    """
    return set(w for w in words if w in dict)


def get_one_edits(word):
    """
    Returns a set containing unique strings one-edit distance (Damerau–Levenshtein distance)
    away from the given word.
    :param word: string
    :return: set of strings
    """
    LETTERS = string.ascii_lowercase

    # e.g. 'word' -> [('', 'word'), ('w', 'ord'), ('wo', 'rd'), ('wor', 'd'), ('word', '')]
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

    # -> ['ord', 'wrd', 'wod', 'wor']
    deletes    = [L + R[1:]               for L, R in splits if R]
    # -> ['owrd', 'wrod', 'wodr']
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    # -> ['aord', 'bord', 'cord', ... 'ward', 'wbrd', 'wcrd' ...]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in LETTERS]
    # -> ['aword', 'bword', 'cword', ... 'waord', 'wbord', 'wcord' ...]
    inserts    = [L + c + R               for L, R in splits for c in LETTERS]

    return set(deletes + transposes + replaces + inserts)


def get_two_edits(word):
    """
    Returns a set containing unique strings two-edit distance away from the given word.
    :param word: string
    :return: set of strings
    """
    return set(e2 for e1 in get_one_edits(word) for e2 in get_one_edits(e1))
