import unittest
from Points import Punct
from Lines import Line

class TestIntersectie(unittest.TestCase):
    
    def setUp(self):
        self.p1 = Punct(0, 0)
        self.p2 = Punct(2, 2)
        self.p3 = Punct(0, 2)
        self.p4 = Punct(2, 0)
        self.vertical_line = Punct(1, 0)
        self.vertical_line_2 = Punct(1, 3)
        self.horizontal_line = Punct(0, 1)
        self.horizontal_line_2 = Punct(2, 1)

    def test_intersecting_lines(self):
        line1 = Line(self.p1, self.p2)  # y = x
        line2 = Line(self.p3, self.p4)  # y = -x + 2
        intersection = line1.intersectie(line2)
        self.assertEqual(intersection.x, 1)
        self.assertEqual(intersection.y, 1)

    def test_parallel_lines(self):
        # Define two parallel lines, for example:
        line1 = Line(Punct(0, 1), Punct(2, 1))  # This line is horizontal at y = 1
        line2 = Line(Punct(0, 2), Punct(2, 2))  # This line is also horizontal at y = 2
        intersection = line1.intersectie(line2)
        self.assertIsNone(intersection)  # Should return None for parallel lines


    def test_vertical_and_non_vertical_lines(self):
        line1 = Line(self.p1, self.p2)  # y = x
        line2 = Line(self.vertical_line, self.vertical_line_2)  # x = 1
        intersection = line1.intersectie(line2)
        self.assertEqual(intersection.x, 1)
        self.assertEqual(intersection.y, 1)

    def test_vertical_lines(self):
        line1 = Line(self.vertical_line, self.vertical_line_2)  # x = 1
        line2 = Line(self.vertical_line, Punct(1, 4))  # x = 1
        intersection = line1.intersectie(line2)
        self.assertIsNone(intersection)  # Should return None for parallel vertical lines

    def test_horizontal_and_vertical_lines(self):
        line1 = Line(self.horizontal_line, self.horizontal_line_2)  # y = 1
        line2 = Line(self.vertical_line, self.vertical_line_2)  # x = 1
        intersection = line1.intersectie(line2)
        self.assertEqual(intersection.x, 1)
        self.assertEqual(intersection.y, 1)

if __name__ == '__main__':
    unittest.main()
