import unittest
from converter import *

class TestConverter(unittest.TestCase):
    def test_c_to_f(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)

    def test_f_to_c(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
    def test_c_to_k(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)

    def test_k_to_c(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)

    def test_f_to_k(self):
        self.assertAlmostEqual(fahrenheit_to_kelvin(32), 273.15)

    def test_k_to_f(self):
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32)

if __name__ == '__main__':
    unittest.main()