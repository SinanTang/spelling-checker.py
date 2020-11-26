from .errors import UnsupportedLanguageError
from .helpers import (get_one_edits,
                      get_two_edits,
                      get_word_freq_dict,
                      get_total_word_count_in_dict,
                      get_known_words,
                      get_word_freq)


class SpellChecker:
    """The main class and entry point of package `spellingchecker`"""

    def __init__(self, lang):
        self.lang = self.__verify_language_support(lang)

    def __verify_language_support(self, lang):
        """
        The spelling check only supports English now.
        :raises UnsupportedLanguageError
        """
        if lang.lower() != 'en':
            raise UnsupportedLanguageError('Language {} is currently unsupported by SpellChecker!'.format(lang))
        else:
            return lang.lower()

    def correct(self, word):
        """
        Returns the most probably correction given a word.
        :param word: string, likely with a typo
        :return: a known word
        """
        return max(self.candidates(word), key=self.probability)

    def candidates(self, word):
        """
        Generates possible spelling corrections as a list for the given word.
        :param word: string
        :return:
        """
        return get_known_words([word]) \
               or get_known_words(get_one_edits(word)) \
               or get_known_words(get_two_edits(word)) \
               or [word]

    def probability(self, word,
                    total=get_total_word_count_in_dict(get_word_freq_dict())):
        """
        Returns the probability of the given word in the corpus.
        :param word: string
        :param total: total number of words in the corpus
        :return: probability as float
        """
        return get_word_freq(word) / total
