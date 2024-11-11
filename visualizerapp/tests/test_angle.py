import unittest
import math
from Angles import Angle

class TestAngleClass(unittest.TestCase):
    
    def test_initialization_degrees(self):
        """Test angle initialization with degrees"""
        angle = Angle(90)
        self.assertEqual(angle.to_degrees(), 90)
        self.assertAlmostEqual(angle.to_radians(), math.pi / 2, places=5)

    def test_initialization_radians(self):
        """Test angle initialization with radians"""
        angle = Angle(math.pi, unit="radians")
        self.assertEqual(angle.to_degrees(), 180)
        self.assertAlmostEqual(angle.to_radians(), math.pi, places=5)

    def test_invalid_unit(self):
        """Test invalid unit handling"""
        with self.assertRaises(ValueError):
            Angle(45, unit="gradians")  # Invalid unit

    def test_addition_of_angles(self):
        """Test addition of two Angle objects"""
        angle1 = Angle(45)
        angle2 = Angle(30)
        result = angle1.add(angle2)
        self.assertEqual(result.to_degrees(), 75)
        self.assertAlmostEqual(result.to_radians(), math.radians(75), places=5)

    def test_subtraction_of_angles(self):
        """Test subtraction of two Angle objects"""
        angle1 = Angle(90)
        angle2 = Angle(30)
        result = angle1.subtract(angle2)
        self.assertEqual(result.to_degrees(), 60)
        self.assertAlmostEqual(result.to_radians(), math.radians(60), places=5)

    def test_addition_with_invalid_type(self):
        """Test addition with invalid type"""
        angle1 = Angle(45)
        with self.assertRaises(TypeError):
            angle1.add(30)  # Adding an int instead of an Angle object

    def test_subtraction_with_invalid_type(self):
        """Test subtraction with invalid type"""
        angle1 = Angle(45)
        with self.assertRaises(TypeError):
            angle1.subtract(30)  # Subtracting an int instead of an Angle object

    def test_repr_output(self):
        """Test the string representation (__repr__) of the Angle object"""
        angle = Angle(45)
        self.assertEqual(repr(angle), "Angle(45 degrees / 0.7854 radians)")


# Run the tests
if __name__ == "__main__":
    unittest.main()
