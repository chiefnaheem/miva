# test_solution.py

import unittest
from solutions import plus_one, alternate_min_max

class TestSolution(unittest.TestCase):

    def test_plus_one_1(self):
        self.assertEqual(plus_one([1, 2, 3]), [1, 2, 4])

    def test_plus_one_2(self):
        self.assertEqual(plus_one([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_plus_one_3(self):
        self.assertEqual(plus_one([9]), [1, 0])

    def test_plus_one_4(self):
        self.assertEqual(plus_one([9, 9, 9]), [1, 0, 0, 0])

    def test_alternate_min_max_1(self):
        arr = [13, 7, 8, 3, 2, 10, 15, -1]
        expected = [-1, 15, 2, 13, 3, 10, 7, 8]
        self.assertEqual(alternate_min_max(arr), expected)

    def test_alternate_min_max_2(self):
        arr = [-5, -12, -1, 7, 14, -7, 3, 6]
        expected = [-12, 14, -7, 7, -5, 6, -1, 3]
        self.assertEqual(alternate_min_max(arr), expected)

    def test_alternate_min_max_3(self):
        arr = [3, 6, 9, -10, -5, -2, 0, 8]
        expected = [-10, 9, -5, 8, -2, 6, 0, 3]
        self.assertEqual(alternate_min_max(arr), expected)

    def test_alternate_min_max_empty(self):
        self.assertEqual(alternate_min_max([]), [])

if __name__ == "__main__":
    unittest.main()
