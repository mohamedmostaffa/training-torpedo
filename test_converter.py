import unittest
from converter import *

class TestConverter(unittest.TestCase):
    def test_c_to_f(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)

    def test_f_to_c(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)

if __name__ == '__main__':
    unittest.main()