import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from math_tools import fibonacci, bmi, mean, sum_list, is_even, absolute


class TestMathTools(unittest.TestCase):
    def test_fibonacci_edge_cases(self):
        #przypadki normalne
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        #przypadek błędny
        with self.assertRaises(ValueError):
            fibonacci(-1)
    
    def test_bmi(self):
        #przypadki normalne
        self.assertEqual(bmi(70, 1.75), "norma")
        self.assertEqual(bmi(45, 1.70), "niedowaga")   
        #przypadek błędny 
        with self.assertRaises(ValueError):
            bmi(70, 0)

    def test_mean(self):
        #przypadek typowy
        self.assertEqual(mean([1, 2, 3]), 2.0)
        #przypadek błędny
        with self.assertRaises(ValueError):
            mean([])
    
    def test_sum_list(self):
        #przypadek typowy
        self.assertEqual(sum_list([1, 2, 3]), 6.0)
        #przypadek błędny
        with self.assertRaises(ValueError):
            sum_list([])
    
    def test_is_even(self):
        #przypadki typowe dodatnie i ujemne
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(-3))   
    
    def test_absolute(self):
        #przypadek typowy 
        self.assertEqual(absolute(-5), 5.0)
        #przypadek brzegowy
        self.assertEqual(absolute(0), 0)