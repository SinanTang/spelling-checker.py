import unittest

from src.spelling_checker.helpers import get_words, get_known_words


class TestHelpers(unittest.TestCase):
    def test_get_words_returns_words_in_text(self):
        text = 'To Sherlock Holmes she is always the woman.'

        expected_word_list = ['to', 'sherlock', 'holmes', 'she', 'is', 'always', 'the', 'woman']
        actual_word_list = get_words(text)

        self.assertEqual(expected_word_list, actual_word_list)

    def test_it_returns_known_words(self):
        dictionary = {'the': 10, 'you': 7, 'me': 5, 'she': 6}
        words = ['teh', 'you', 'she']

        expected_known_words = {'you', 'she'}
        actual_known_words = get_known_words(words, dictionary)

        self.assertEqual(expected_known_words, actual_known_words)
