import math

class Angle:
    def __init__(self, value, unit="degrees"):
        if unit == "degrees":
            self.degrees = value
            self.radians = math.radians(value)
        elif unit == "radians":
            self.radians = value
            self.degrees = math.degrees(value)
        else:
            raise ValueError("Unit must be 'degrees' or 'radians'")
    
    def to_degrees(self):
        return self.degrees

    def to_radians(self):
        return self.radians

    def add(self, other_angle):
        if isinstance(other_angle, Angle):
            return Angle(self.degrees + other_angle.degrees)
        else:
            raise TypeError("Can only add another Angle object")

    def subtract(self, other_angle):
        if isinstance(other_angle, Angle):
            return Angle(self.degrees - other_angle.degrees)
        else:
            raise TypeError("Can only subtract another Angle object")
    
    def __repr__(self):
        return f"Angle({self.degrees} degrees / {self.radians:.4f} radians)"

