import unittest
from Points import Punct
from Triunghiuri import Triunghi
import math

class TestTriunghi(unittest.TestCase):

    def test_lungime_laturi(self):
        p1 = Punct(0, 0)
        p2 = Punct(3, 0)
        p3 = Punct(0, 4)
        
        triunghi = Triunghi(p1, p2, p3)
        expected_lengths = (3.0, 4.0, 5.0)  # 3-4-5 triangle
        actual_lengths = triunghi.lungime_laturi()
        
        self.assertAlmostEqual(actual_lengths[0], expected_lengths[0], places=2)
        self.assertAlmostEqual(actual_lengths[1], expected_lengths[1], places=2)
        self.assertAlmostEqual(actual_lengths[2], expected_lengths[2], places=2)

    def test_perimetru(self):
        p1 = Punct(0, 0)
        p2 = Punct(3, 0)
        p3 = Punct(0, 4)
        
        triunghi = Triunghi(p1, p2, p3)
        expected_perimeter = 12.0  # Perimeter of 3-4-5 triangle
        actual_perimeter = triunghi.perimetru()
        
        self.assertAlmostEqual(actual_perimeter, expected_perimeter, places=2)

    def test_invalid_puncts(self):
        with self.assertRaises(TypeError):
            triunghi = Triunghi(1, 2, 3)  # This should raise a TypeError
    
    def test_arie(self):
        p1 = Punct(0, 0)
        p2 = Punct(3, 0)
        p3 = Punct(0, 4)
        
        triunghi = Triunghi(p1, p2, p3)
        expected_area = 6.0  # Area of 3-4-5 triangle using Heron's formula
        actual_area = triunghi.arie()
        
        self.assertAlmostEqual(actual_area, expected_area, places=2)

    def test_este_valid(self):
        # Test for a valid triangle
        p1 = Punct(0, 0)
        p2 = Punct(3, 0)
        p3 = Punct(0, 4)
        triunghi = Triunghi(p1, p2, p3)
        self.assertTrue(triunghi.este_valid())  # Valid triangle
        
        # Test for an invalid triangle (collinear points)
        p4 = Punct(0, 0)
        p5 = Punct(2, 0)
        p6 = Punct(4, 0)  # Collinear points, not a triangle
        triunghi_invalid = Triunghi(p4, p5, p6)
        self.assertFalse(triunghi_invalid.este_valid())  # Invalid triangle

    def test_este_dreptunghic(self):
        # Test for a right-angled triangle
        p1 = Punct(0, 0)
        p2 = Punct(3, 0)
        p3 = Punct(0, 4)
        triunghi = Triunghi(p1, p2, p3)
        self.assertTrue(triunghi.este_dreptunghic())  # Right-angled triangle
        
        # Test for a non-right-angled triangle
        p4 = Punct(0, 0)
        p5 = Punct(2, 0)
        p6 = Punct(1, 1)
        triunghi_non_dreptunghic = Triunghi(p4, p5, p6)
        self.assertTrue(triunghi_non_dreptunghic.este_dreptunghic())  # Non-right triangle

    def test_tip_triunghi(self):
        # Test for equilateral triangle
        p1 = Punct(0, 0)
        p2 = Punct(1, 0)
        p3 = Punct(0.5, math.sqrt(3)/2)  # Equilateral triangle
        triunghi_echilateral = Triunghi(p1, p2, p3)
        self.assertEqual(triunghi_echilateral.tip_triunghi(), "echilateral")

        # Test for isoscel triangle
        p4 = Punct(0, 0)
        p5 = Punct(2, 0)
        p6 = Punct(1, math.sqrt(3))  # Isosceles triangle
        triunghi_isoscel = Triunghi(p4, p5, p6)
        self.assertEqual(triunghi_isoscel.tip_triunghi(), "isoscel")
        
        # Test for right-angled triangle
        p7 = Punct(0, 0)
        p8 = Punct(3, 0)
        p9 = Punct(0, 4)  # Right-angled triangle (3-4-5)
        triunghi_dreptunghic = Triunghi(p7, p8, p9)
        self.assertEqual(triunghi_dreptunghic.tip_triunghi(), "dreptunghic")
        
        # Test for scalene triangle
        p10 = Punct(0, 0)
        p11 = Punct(2, 0)
        p12 = Punct(1, 2)  # Scalene triangle
        triunghi_scalen = Triunghi(p10, p11, p12)
        self.assertEqual(triunghi_scalen.tip_triunghi(), "isoscel")
    
    def test_individual_angles(self):
        A = Punct(0, 0)
        B = Punct(4, 0)
        C = Punct(0, 3)
        angles = Triunghi(A,B,C).get_angles()
        #delta e marja de eroare acceptata de test case
        self.assertAlmostEqual(angles[0], 90, delta=0.01)
        self.assertAlmostEqual(angles[1], 36.87, delta=0.01)
        self.assertAlmostEqual(angles[2], 53.13, delta=0.01)
    
    def test_arii_egale_true(self):
        t1 = Triunghi(Punct(0, 0), Punct(4, 0), Punct(0, 3))  # Area = 6
        t2 = Triunghi(Punct(1, 1), Punct(5, 1), Punct(1, 4))  # Area = 6
        
        self.assertTrue(t1.arii_egale(t2))

    def test_arii_egale_false(self):
        t1 = Triunghi(Punct(0, 0), Punct(4, 0), Punct(0, 3))
        t2 = Triunghi(Punct(0, 0), Punct(2, 0), Punct(0, 1))
        
        self.assertFalse(t1.arii_egale(t2))

    def test_arii_egale_invalid_type(self):
        t1 = Triunghi(Punct(0, 0), Punct(4, 0), Punct(0, 3))
        non_triangle = "Not a triangle"
        
        with self.assertRaises(TypeError):
            t1.arii_egale(non_triangle)
        
    def test_collinear_points(self):
        p1 = Punct(0, 0)
        p2 = Punct(2, 2)
        p3 = Punct(4, 4) 
        with self.assertRaises(ValueError):
            triangle = Triunghi(p1, p2, p3)

if __name__ == '__main__':
    unittest.main()
