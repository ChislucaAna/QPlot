import unittest
from Points import Punct
from Lines  import Line
import math

class TestLine(unittest.TestCase):

    def test_lungime_real(self):
        p1 = Punct(0, 0)
        p2 = Punct(3, 4)
        line = Line(p1, p2)
        self.assertAlmostEqual(line.lungime(), 5.0)  # Distance between (0,0) and (3,4) is 5

    def test_lungime_complex(self):
        p1 = Punct(1 + 1j, 0)
        p2 = Punct(4 + 4j, 0)
        line = Line(p1, p2)
        self.assertAlmostEqual(line.lungime(), abs(4 + 4j - 1 - 1j))

    def test_mijloc_real(self):
        p1 = Punct(0, 0)
        p2 = Punct(4, 4)
        line = Line(p1, p2)
        mid = line.mijloc()
        self.assertAlmostEqual(mid.x, 2.0)  # Midpoint x should be (0 + 4) / 2
        self.assertAlmostEqual(mid.y, 2.0)  # Midpoint y should be (0 + 4) / 2

    def test_mijloc_complex(self):
        p1 = Punct(1 + 2j, 0)
        p2 = Punct(5 + 6j, 0)
        line = Line(p1, p2)
        mid = line.mijloc()
        self.assertEqual(mid.x, 3 + 4j)  # Midpoint of complex numbers

    def test_panta_real(self):
        p1 = Punct(0, 0)
        p2 = Punct(4, 2)
        line = Line(p1, p2)
        self.assertAlmostEqual(line.panta(), 0.5)  # Slope (y2 - y1) / (x2 - x1)

    def test_panta_vertical_line(self):
        p1 = Punct(2, 1)
        p2 = Punct(2, 4)
        line = Line(p1, p2)
        self.assertEqual(line.panta(), float('inf'))  # Infinite slope for vertical line

    def test_unghiul_cu_axa_ox(self):
        p1 = Punct(0, 0)
        p2 = Punct(1, 1)
        line = Line(p1, p2)
        self.assertAlmostEqual(line.unghiul_cu_axa_ox(), math.pi / 4)  # 45 degrees

    def test_intersectie_non_parallel(self):
        line1 = Line(Punct(0, 0), Punct(2, 2))
        line2 = Line(Punct(0, 2), Punct(2, 0))
        intersection = line1.intersectie(line2)
        self.assertAlmostEqual(intersection.x, 1.0)
        self.assertAlmostEqual(intersection.y, 1.0)  # Intersection at (1, 1)

    def test_intersectie_parallel(self):
        line1 = Line(Punct(0, 0), Punct(1, 1))
        line2 = Line(Punct(0, 1), Punct(1, 2))
        self.assertIsNone(line1.intersectie(line2))  # Parallel lines should return None

    def test_perpendiculara_din_origine(self):
        line = Line(Punct(0, 0), Punct(1, 1))
        perp = line.perpendiculara_din_origine()
        self.assertAlmostEqual(perp.panta(), -1.0)  # Perpendicular to slope 1 is -1

    def test_perpendiculara_vertical_line(self):
        line = Line(Punct(0, 0), Punct(0, 1))
        perp = line.perpendiculara_din_origine()
        self.assertEqual(perp.panta(), 0.0)  # Perpendicular to a vertical line is horizontal

if __name__ == '__main__':
    unittest.main()

