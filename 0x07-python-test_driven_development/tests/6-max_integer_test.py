#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This class defines the unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test the ordered list of the integers."""
        ordered = [1, 2, 3, 7]
        self.assertEqual(max_integer(ordered), 7)

    def test_unordered_list(self):
        """Test the unordered list of integers."""
        unordered = [1, 2, 7, 3]
        self.assertEqual(max_integer(unordered), 7)

    
    def test_max_at_begginning(self):
        """Test the list with the beginning max value."""
        max_at_beginning = [7, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 7)
    
    def test_empty_list(self):
        """Test the empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)


if __name__ == '__main__':
    unittest.main()