import unittest
from sort_tools import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    is_sorted,
    reverse_list,
    swap,
)


class TestSortTools(unittest.TestCase):

    def test_bubble_sort(self):
        # przypadek normalny
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])
        # już posortowana
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])
        # duplikaty
        self.assertEqual(bubble_sort([5, 5, 1]), [1, 5, 5])
        # brzeg: jedna wartość
        self.assertEqual(bubble_sort([1]), [1])
        # brzeg/błędny: pusta lista (jeśli w funkcji masz raise)
        with self.assertRaises(ValueError):
            bubble_sort([])

    def test_insertion_sort(self):
        # normalny
        self.assertEqual(insertion_sort([4, 2, 3, 1]), [1, 2, 3, 4])
        # duplikaty
        self.assertEqual(insertion_sort([3, 3, 1, 2]), [1, 2, 3, 3])
        # jedna wartość
        self.assertEqual(insertion_sort([1]), [1])
        # błędny: pusta lista
        with self.assertRaises(ValueError):
            insertion_sort([])

    def test_selection_sort(self):
        # normalny
        self.assertEqual(selection_sort([3, 3, 2, 1]), [1, 2, 3, 3])
        # już posortowana
        self.assertEqual(selection_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        # jedna wartość
        self.assertEqual(selection_sort([1]), [1])
        # błędny: pusta lista
        with self.assertRaises(ValueError):
            selection_sort([])

    def test_is_sorted(self):
        # posortowana
        self.assertTrue(is_sorted([1, 2, 3, 4]))
        # nieposortowana
        self.assertFalse(is_sorted([2, 1, 3]))
        # brzeg: jedna wartość
        self.assertTrue(is_sorted([1]))
        # błędny: pusta lista (jeśli w funkcji masz raise)
        with self.assertRaises(ValueError):
            is_sorted([])

    def test_reverse_list(self):
        # normalny
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        # brzeg: jedna wartość
        self.assertEqual(reverse_list([1]), [1])
        # błędny: pusta lista
        with self.assertRaises(ValueError):
            reverse_list([])

    def test_swap(self):
        # normalny
        data = [1, 2, 3]
        swap(data, 0, 2)
        self.assertEqual(data, [3, 2, 1])
        # błędne indeksy
        with self.assertRaises(ValueError):
            swap(data, -1, 2)
        with self.assertRaises(ValueError):
            swap(data, 0, 3)
