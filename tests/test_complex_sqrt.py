import unittest
import math
from domain import Complex

class TestComplexPow(unittest.TestCase):
    def test_natural_power(self):
        c = Complex(1, 1)  # (1 + 1i)
        result = c.pow(2)  # (1 + 1i)^2
        self.assertAlmostEqual(result.real, 0.0)
        self.assertAlmostEqual(result.imag, 2.0)

    def test_negative_power(self):
        c = Complex(1, 1)  # (1 + 1i)
        result = c.pow(-1)  # (1 + 1i)^-1
        expected_real = 0.5
        expected_imag = -0.5
        self.assertAlmostEqual(result.real, expected_real)
        self.assertAlmostEqual(result.imag, expected_imag)

    def test_fractional_power(self):
        c = Complex(1, 0)  # (1 + 0i)
        result = c.pow(0.5)  # (1 + 0i)^(1/2)
        self.assertAlmostEqual(result.real, 1.0)
        self.assertAlmostEqual(result.imag, 0.0)

    def test_zero_real(self):
        c = Complex(0, 1)  # (0 + 1i)
        result = c.pow(2)  # (0 + 1i)^2
        self.assertAlmostEqual(result.real, -1.0)
        self.assertAlmostEqual(result.imag, 0.0)

    def test_zero_imaginary(self):
        c = Complex(1, 0)  # (1 + 0i)
        result = c.pow(3)  # (1 + 0i)^3
        self.assertAlmostEqual(result.real, 1.0)
        self.assertAlmostEqual(result.imag, 0.0)

    def test_negative_power_zero_real(self):
        c = Complex(0, 1)  # (0 + 1i)
        result = c.pow(-2)  # (0 + 1i)^-2
        self.assertAlmostEqual(result.real, -1.0)
        self.assertAlmostEqual(result.imag, 0.0)

    def test_positive_power_large(self):
        c = Complex(1, 1)  # (1 + 1i)
        result = c.pow(10)  # (1 + 1i)^10
        expected_real = 0.0
        expected_imag = 32.0
        self.assertAlmostEqual(result.real, expected_real)
        self.assertAlmostEqual(result.imag, expected_imag)

if __name__ == "__main__":
    unittest.main()
