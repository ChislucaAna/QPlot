import unittest
from domain import Complex

#teste pentru operatii din instante diferite

class TestComplexOperationsWithReals(unittest.TestCase):

    def setUp(self):
        self.real_num = 5
        self.complex_num = Complex(3, 4)

    def test_add_real_and_complex(self):
        result = self.real_num + self.complex_num
        expected = Complex(8, 4)
        self.assertEqual(result, expected)

    def test_add_complex_and_real(self):
        result = self.complex_num + self.real_num
        expected = Complex(8, 4)
        self.assertEqual(result, expected)

    def test_subtract_real_and_complex(self):
        result = self.real_num - self.complex_num
        expected = Complex(2, -4)
        self.assertEqual(result, expected)

    def test_subtract_complex_and_real(self):
        result = self.complex_num - self.real_num
        expected = Complex(-2, 4)
        self.assertEqual(result, expected)

    def test_multiply_real_and_complex(self):
        result = self.real_num * self.complex_num
        expected = Complex(15, 20)
        self.assertEqual(result, expected)

    def test_multiply_complex_and_real(self):
        result = self.complex_num * self.real_num
        expected = Complex(15, 20)
        self.assertEqual(result, expected)

    def test_divide_real_and_complex(self):
        result = self.real_num / self.complex_num
        expected_real = (self.real_num * self.complex_num.real) / (self.complex_num.real**2 + self.complex_num.imag**2)
        expected_imag = (-self.real_num * self.complex_num.imag) / (self.complex_num.real**2 + self.complex_num.imag**2)
        expected = Complex(expected_real, expected_imag)
        self.assertEqual(result, expected)

    def test_divide_complex_and_real(self):
        result = self.complex_num / self.real_num
        expected = Complex(3 / 5, 4 / 5)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
