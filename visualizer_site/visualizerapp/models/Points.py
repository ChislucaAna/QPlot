import math
from .domain import Complex

class Punct:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __add__(self,other):
        if isinstance(other, Punct):
            return Punct(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Punct(self.x * other, self.y * other)
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Punct(self.x * other, self.y * other)
        return NotImplemented
            
    def __str__(self):
        return f'Punct({self.x}, {self.y})'

    def __abs__(self):
        return(math.sqrt(self.x*self.x+self.y*self.y))

    def get_angle(self):
        return((math.atan(self.y/self.x)*180.0)/math.pi)