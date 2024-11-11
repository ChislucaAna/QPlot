import unittest
import math
from domain import Complex

#teste pentru operatii intre 2 instante de tip complex

class TestComplex(unittest.TestCase):

    def setUp(self): # numerele folosite in cadrul testelor
        """Set up test cases."""
        self.c1 = Complex(3, 4)   # 3 + 4i
        self.c2 = Complex(1, -2)  # 1 - 2i
        self.c3 = Complex(0, 0)   # 0 + 0i
        self.c4 = Complex(-1, 1)  # -1 + 1i

    #functiile de tipul self.assertEqual verifica validitatea operatiilor pe baza functiei __eq__ definita din clasa

    def test_add(self):
        """Test addition of complex numbers."""
        result = self.c1 + self.c2
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imag, 2)

    def test_subtract(self):
        """Test subtraction of complex numbers."""
        result = self.c1 - self.c2
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imag, 6)

    def test_multiply(self):
        """Test multiplication of complex numbers."""
        result = self.c1 * self.c2
        self.assertEqual(result.real, 11)  # (3*1 - 4*(-2)) = 3 + 8 = 11
        self.assertEqual(result.imag, -2)  # (3*(-2) + 4*1) = -6 + 4 = -2

    def test_divide(self):
        """Test division of complex numbers."""
        result = self.c1 / self.c2
        self.assertAlmostEqual(result.real, -1.0)  # (3*1 + 4*(-2)) / (1^2 + (-2)^2) = -5 / 5 = -1
        self.assertAlmostEqual(result.imag, 2.0)  # (4*1 - 3*(-2)) / (1^2 + (-2)^2) = 4 + 6 / 5 = 2

    def test_divide_by_zero(self):
        """Test division by zero exception."""
        with self.assertRaises(ZeroDivisionError):
            result = self.c1 / Complex(0, 0)

    def test_abs(self):
        """Test absolute value of complex numbers."""
        self.assertAlmostEqual(abs(self.c1), 5.0)  # sqrt(3^2 + 4^2) = 5
        self.assertAlmostEqual(abs(self.c2), math.sqrt(5))  # sqrt(1^2 + (-2)^2) = sqrt(5)
        self.assertAlmostEqual(abs(self.c3), 0.0)  # sqrt(0^2 + 0^2) = 0
        self.assertAlmostEqual(abs(self.c4), math.sqrt(2))  # sqrt((-1)^2 + 1^2) = sqrt(2)

    def test_equality(self):
        """Test equality of complex numbers."""
        self.assertTrue(self.c1 == Complex(3, 4))
        self.assertFalse(self.c1 == self.c2)
        self.assertFalse(self.c1 == Complex(4, 4))

    def test_str(self):
        """Test string representation of complex numbers."""
        self.assertEqual(str(self.c1), "3 + 4i")
        self.assertEqual(str(self.c2), "1 + -2i")
        self.assertEqual(str(self.c3), "0 + 0i")
        self.assertEqual(str(self.c4), "-1 + 1i")

# testele ruleaza doar la comanda directa sau main, nu si daca sunt importate si in alte module
if __name__ == '__main__':
    unittest.main()

