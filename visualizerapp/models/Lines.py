from .Points import Punct
from .domain import Complex
import math

class Line:

    def __init__(self, p1, p2):
        if isinstance(p1, Punct) and isinstance(p2, Punct):
            self.p1 = p1
            self.p2 = p2
        else:
            raise TypeError("P1 si P2 TREBUIE SA FIE PUNCTE")
    
    def lungime(self):
        ###cum se calculeaza asta cu nr complexe
        diff_x = self.p2.x - self.p1.x
        diff_y = self.p2.y - self.p1.y
        return (abs(diff_x)**2 + abs(diff_y)**2)**0.5

    def mijloc(self): #xm=(xa+xb)/2 ym=(xa+xb)/2
        return Punct((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)

    def panta(self):
        if self.p2.x == self.p1.x:  # Vertical line
            return None
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
    

    def intercept(self): #il gaseste pe n unde y=mx+n
        if self.panta() is None:  # Vertical line
            return None
        return self.p1.y - self.panta() * self.p1.x

    def unghiul_cu_axa_ox(self):#unghiul cu aza ox e arcangenta pantei
        return math.atan(self.panta())

    def mediatoare(self):
        M = self.mijloc()
        slope = self.panta()
        if slope is None:  # Vertical line becomes horizontal
            return Line(M, Punct(M.x + 1, M.y))  # Horizontal line through M
        # Perpendicular slope
        perpendicular_slope = -1 / slope
        intercept = M.y - perpendicular_slope * M.x
        return Line(M, Punct(M.x + 1, perpendicular_slope * (M.x + 1) + intercept))

    def intersectie(self, other):
        m1, b1 = self.panta(), self.intercept()
        m2, b2 = other.panta(), other.intercept()

        if m1 == m2:  # Parallel lines
            return None
        
        if m1 is None:  # self is a vertical line
            x = self.p1.x
            y = m2 * x + b2
        elif m2 is None:  # other is a vertical line
            x = other.p1.x
            y = m1 * x + b1
        else:  # Standard intersection
            x = (b2 - b1) / (m1 - m2)
            y = m1 * x + b1

        return Punct(x, y)
    
    def perpendiculara_din_origine(self):
        panta = self.panta()
        if panta == 0:
            p1 = Punct(0, 0)
            p2 = Punct(0, 1) 
        elif panta == float('inf'):
            p1 = Punct(0, 0)
            p2 = Punct(1, 0)  
        else:
            panta_perp = -1 / panta
            p1 = Punct(0, 0)
            p2 = Punct(1, panta_perp)
        
        return Line(p1, p2)

    def __str__(self): 
        return f'Dreapta de la {self.p1} la {self.p2}'