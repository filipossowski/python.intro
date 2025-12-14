import unittest
from text_tools import (
    is_palindrome,
    delete_extra_spaces,
    remove_polish_letters,
    trim,
    word_count,
    contains,
)


class TestTextTools(unittest.TestCase):

    def test_is_palindrome(self):
        # przypadek normalny
        self.assertTrue(is_palindrome("Kajak"))
        # ignorowanie spacji i wielkości liter
        self.assertTrue(is_palindrome("Kobyła ma mały bok"))
        # niepalindrom
        self.assertFalse(is_palindrome("python"))
        # brzegowy: jeden znak
        self.assertTrue(is_palindrome("a"))
        # błędny: pusty string (jeśli w funkcji masz raise ValueError)
        with self.assertRaises(ValueError):
            is_palindrome("")

    def test_delete_extra_spaces(self):
        # wiele spacji pośrodku
        self.assertEqual(delete_extra_spaces("ala   ma   kota"), "ala ma kota")
        # spacje na początku i końcu
        self.assertEqual(delete_extra_spaces("   ala ma kota   "), "ala ma kota")
        # pojedyncze spacje – bez zmian
        self.assertEqual(delete_extra_spaces("ala ma kota"), "ala ma kota")
        # błędny: pusty tekst
        with self.assertRaises(ValueError):
            delete_extra_spaces("")

    def test_remove_polish_letters(self):
        # same polskie litery
        self.assertEqual(remove_polish_letters("ąęćłńóśźż"), "aeclnoszz")
        # mieszany tekst
        self.assertEqual(
            remove_polish_letters("Zażółć gęślą jaźń"),
            "zazolc gesla jazn",
        )
        # błędny: pusty tekst
        with self.assertRaises(ValueError):
            remove_polish_letters("")

    def test_trim(self):
        # zwykłe przycięcie
        self.assertEqual(trim("  ala ma kota  "), "ala ma kota")
        # bez białych znaków
        self.assertEqual(trim("ala"), "ala")
        # błędny: pusty
        with self.assertRaises(ValueError):
            trim("")

    def test_word_count(self):
        # normalny
        self.assertEqual(word_count("ala ma kota"), 3)
        # wiele spacji
        self.assertEqual(word_count("ala   ma   kota"), 3)
        # brzegowy: jedno słowo
        self.assertEqual(word_count("ala"), 1)
        # błędny: pusty
        with self.assertRaises(ValueError):
            word_count("")

    def test_contains(self):
        # normalny: zawiera
        self.assertTrue(contains("ala ma kota", "ma"))
        # normalny: nie zawiera
        self.assertFalse(contains("ala ma kota", "pies"))
        # brzegowy: podciąg równy całemu tekstowi
        self.assertTrue(contains("ala", "ala"))
        # błędne: pusty tekst lub pusty podciąg
        with self.assertRaises(ValueError):
            contains("", "a")
        with self.assertRaises(ValueError):
            contains("ala", "")

