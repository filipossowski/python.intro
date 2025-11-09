from app import bubble_sort
from app import insertion_sort
from app import fibonacci
from app import is_palindrome
from app import bmi
import unittest
#3.3
#testy funkcji bubble_sort, insertion_sort, fibonacci, is_palindrome oraz bmi. Sprawdzane są przypadki typowe.
def test_bubble_sort():
    assert bubble_sort([5,3,1,2]) == [1,2,3,5]
def test_insertion_sort():
    assert insertion_sort([5,3,1,2]) == [1,2,3,5]

def test_fibonacci():
    assert fibonacci(10) == 34

def test_is_palindrome():
    assert is_palindrome("Tenet") == True
    assert is_palindrome("Batman") == False

def test_bmi():
    assert bmi(50, 1.80) == "niedowaga"
    assert bmi(75, 1.85) == "norma"
    assert bmi(95, 1.87) == "nadwaga"
    assert bmi(120, 1.75) == "otyłość"

#3.4


class TestBubbleSort(unittest.TestCase):
# Testy funkcji bubble_sort z funkcją SetUp. Sprawdzane są przypadki typowe, przypadek z pustą listą oraz przypadek z jednym elementem w liście.

    def setUp(self):
        self.sample = [3,1,2]

    def test_typical(self):
        self.assertEqual(bubble_sort(self.sample.copy()), [1,2,3])

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_one_element(self):
        self.assertEqual(bubble_sort([42]), [42])

class TestInsertionSort(unittest.TestCase):
# Testy funkcji insertion_sort z funkcją SetUp. Sprawdzane są przypadki typowe, przypadek z pustą listą oraz przypadek z jednym elementem w liście.

    def setUp(self):
        self.sample = [5,3,4,1]

    def test_typical(self):
        self.assertEqual(insertion_sort(self.sample.copy()), [1,3,4,5])

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_one_element(self):
        self.assertEqual(insertion_sort([28]), [28])

class TestFibonacci(unittest.TestCase):
# Testy funkcji fibonacci. Sprawdzane są przypadki typowe, przypadki brzegowe oraz przypadki z niepoprawnymi danymi.
    def test_typical(self):
        self.assertEqual(fibonacci(10), 34)

    def test_edge_case(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_wrong_data(self):
        with self.assertRaises(ValueError):
            fibonacci(-3)

class TestIsPalindrome(unittest.TestCase):
# Testy funkcji is_palindrome. Sprawdzane są przypadki typowe, tzn. z faktycznymi palindromami,
# przypadki brzegowe, gdzie pojawia pojedyńcza litera lub ich całkowity brak oraz parametryzowane testy z różnymi palindromami.
    def test_typical(self):
        self.assertTrue(is_palindrome("tenet"), True)

    def test_edge_case(self):
        self.assertTrue(is_palindrome("a"), True)
        self.assertTrue(is_palindrome(""), True)    

    def test_wrong_data(self):
        self.assertFalse(is_palindrome("Interstellar"))

    def test_paremetrized(self):
        palindromes = ["kajak", "tenet", "oko"]
        for word in palindromes:
            self.assertTrue(is_palindrome(word))

class TestBMI(unittest.TestCase):
# Testy funkcji bmi. Sprawdzane są przypadki typowe, przypadki brzegowe oraz przypadki z niepoprawnymi danymi.

    def test_typical(self):
        self.assertEqual(bmi(50, 1.80), "niedowaga")
        self.assertEqual(bmi(75, 1.85), "norma")
        self.assertEqual(bmi(95, 1.87), "nadwaga")
        self.assertEqual(bmi(120, 1.75), "otyłość")

    def test_edge_case(self):

        self.assertEqual(bmi(59, 1.80), "niedowaga")   
        self.assertEqual(bmi(60, 1.80), "norma")    

    def test_wrong_data(self):
        with self.assertRaises(ZeroDivisionError):
            bmi(180, 0)
