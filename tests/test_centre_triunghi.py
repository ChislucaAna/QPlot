#modul de teste pentru punctele importante din interiorul
#triunghiurilor

import unittest
from Points import Punct
from Triunghiuri import Triunghi
from Lines import Line
import math

class TestTriunghiCircumcenter(unittest.TestCase):

    def test_equilateral_triangle(self):
        """Test circumcenter of an equilateral triangle."""
        p1 = Punct(0, 0)
        p2 = Punct(2, 0)
        p3 = Punct(1, 1.732)  # Equilateral triangle with side length 2
        
        triangle = Triunghi(p1, p2, p3)
        circumcenter = triangle.get_centru_circumscris()

        # For an equilateral triangle, the circumcenter should be at (1, sqrt(3)/3)
        self.assertAlmostEqual(circumcenter.x, 1, places=3)
        self.assertAlmostEqual(circumcenter.y, 0.577, places=3)

    def test_right_angle_triangle(self):
        """Test circumcenter of a right-angled triangle."""
        p1 = Punct(0, 0)
        p2 = Punct(3, 0)
        p3 = Punct(0, 4)  # Right-angled triangle

        triangle = Triunghi(p1, p2, p3)
        circumcenter = triangle.get_centru_circumscris()

        # For a right-angled triangle, the circumcenter is the midpoint of the hypotenuse
        self.assertAlmostEqual(circumcenter.x, 1.5, places=3)
        self.assertAlmostEqual(circumcenter.y, 2, places=3)

    def test_scalene_triangle(self):
        """Test circumcenter of a scalene triangle."""
        p1 = Punct(1, 1)
        p2 = Punct(6, 1)
        p3 = Punct(4, 5) 

        triangle = Triunghi(p1, p2, p3)
        circumcenter = triangle.get_centru_circumscris()

        self.assertAlmostEqual(circumcenter.x, 3.5, places=3)
        self.assertAlmostEqual(circumcenter.y, 2.25, places=3)




class TestTriangleCentruInscris(unittest.TestCase):
    def test_echilateral(self):
        # Triunghi echilateral cu laturile egale, de exemplu: (0, 0), (1, sqrt(3)), (2, 0)
        p1 = Punct(0, 0)
        p2 = Punct(1, 1.732)  # Aproximativ sqrt(3)
        p3 = Punct(2, 0)
        triangle = Triunghi(p1, p2, p3)
        x, y = triangle.get_centru_inscris()
        # Pentru un triunghi echilateral, incentrul este pe mediane, aprox. (1, 0.577)
        self.assertAlmostEqual(x, 1, places=1)
        self.assertAlmostEqual(y, 0.577, places=1)

    def test_isoscel(self):
        # Triunghi isoscel cu baza pe axa x, de exemplu: (0, 0), (2, 0), (1, 2)
        p1 = Punct(0, 0)
        p2 = Punct(2, 0)
        p3 = Punct(1, 2)
        triangle = Triunghi(p1, p2, p3)
        x, y = triangle.get_centru_inscris()
        self.assertAlmostEqual(x, 1, places=1)
        self.assertAlmostEqual(y, 0.618, places=1)

    def test_dreptunghic(self):
        # Triunghi dreptunghic, de exemplu: (0, 0), (3, 0), (0, 4)
        p1 = Punct(0, 0)
        p2 = Punct(3, 0)
        p3 = Punct(0, 4)
        triangle = Triunghi(p1, p2, p3)
        x, y = triangle.get_centru_inscris()
        self.assertAlmostEqual(x, 1, places=1)
        self.assertAlmostEqual(y, 1, places=1)

    def test_scalene(self):
        # Triunghi oarecare (scalen), de exemplu: (0, 0), (4, 0), (2, 3)
        p1 = Punct(0, 0)
        p2 = Punct(4, 0)
        p3 = Punct(2, 3)
        triangle = Triunghi(p1, p2, p3)
        x, y = triangle.get_centru_inscris()
        # Verificare cu valori calculate pentru acest triunghi
        self.assertAlmostEqual(x, 2, places=1)
        self.assertAlmostEqual(y, 1.070,places=1)

if __name__ == '__main__':
    unittest.main()



