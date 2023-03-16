import unittest
from day_01_part_02 import calculate_fuel_for_module, calculate_total_fuel

class TestCalculateFuelForModule(unittest.TestCase):

    def test_calculate_fuel_for_module(self):
        self.assertEqual(calculate_fuel_for_module(14), 2)
        self.assertEqual(calculate_fuel_for_module(1969), 966)
        self.assertEqual(calculate_fuel_for_module(100756), 50346)

class TestCalculateTotalFuel(unittest.TestCase):

    def test_calculate_total_fuel(self):
        self.assertEqual(calculate_total_fuel([12, 14, 1969, 100756]), 51316)
