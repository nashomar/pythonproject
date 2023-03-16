import unittest
from day_01_part_01 import calculate_fuel

class TestCalculateFuel(unittest.TestCase):

    def test_calculate_fuel(self):
        self.assertEqual(calculate_fuel(12), 2)
        self.assertEqual(calculate_fuel(14), 2)
        self.assertEqual(calculate_fuel(1969), 654)
        self.assertEqual(calculate_fuel(100756), 33583)
