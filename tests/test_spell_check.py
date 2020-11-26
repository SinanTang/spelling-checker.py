import unittest

from src.spelling_checker import SpellChecker
from src.spelling_checker.errors import UnsupportedLanguageError


class TestSpellCheck(unittest.TestCase):
    def test_it_raises_when_language_is_unsupported(self):
        unsupported_lang = 'de'
        self.assertRaises(UnsupportedLanguageError, SpellChecker, unsupported_lang)

    def test_spelling_correction_works_as_expected(self):
        checker = SpellChecker('en')

        self.assertEqual(checker.correct('speling'), 'spelling')
        self.assertEqual(checker.correct('inconvient'), 'inconvenient')
        self.assertEqual(checker.correct('peotry'), 'poetry')
        self.assertEqual(checker.correct('bycycle'), 'bicycle')
        self.assertEqual(checker.correct('word'), 'word')
