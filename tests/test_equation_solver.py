import unittest
from domain import Complex
from equation_solver import QuadraticSolver

class TestQuadraticSolverWithComplex(unittest.TestCase):

    def setUp(self):
        self.solver = QuadraticSolver()

    def test_real_roots_with_complex_coefficients(self):
        x1, x2 = self.solver.solve_quadratic(Complex(1, 0), Complex(-3, 0), Complex(2, 0))  # x^2 - 3x + 2 = 0
        self.assertEqual(x1, Complex(2, 0))  # Root is 2
        self.assertEqual(x2, Complex(1, 0))  # Root is 1

    def test_repeated_root_with_complex_coefficients(self):
        x1, x2 = self.solver.solve_quadratic(Complex(1, 0), Complex(-2, 0), Complex(1, 0))  # x^2 - 2x + 1 = 0
        self.assertEqual(x1, Complex(1, 0))  # Root is 1
        self.assertEqual(x2, Complex(1, 0))  # Root is 1

    def test_complex_roots_with_real_coefficients(self):
        x1, x2 = self.solver.solve_quadratic(Complex(1, 0), Complex(2, 0), Complex(5, 0))  # x^2 + 2x + 5 = 0
        self.assertEqual(x1, Complex(-1, 2))  # Root is -1 + 2i
        self.assertEqual(x2, Complex(-1, -2))  # Root is -1 - 2i

    def test_complex_coefficients(self):
        x1, x2 = self.solver.solve_quadratic(Complex(1, 1), Complex(2, 2), Complex(1, 1))
        expected_root1 = Complex(-1, 0)
        expected_root2 = Complex(-1, 0)
        self.assertEqual(x1, expected_root1)
        self.assertEqual(x2, expected_root2)

    def test_invalid_a_coefficient(self):
        with self.assertRaises(ValueError):
            self.solver.solve_quadratic(Complex(0, 0), Complex(2, 1), Complex(1, 1))  # Should raise an error

if __name__ == '__main__':
    unittest.main()
