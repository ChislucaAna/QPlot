from Points import Punct
from domain import Complex
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

    def panta(self):#mAB=(yA-yB)/(xA-xB) ecuatia dreptei prin doua pct
        try:
            return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        except ZeroDivisionError:
            return float('inf')

    def unghiul_cu_axa_ox(self):#unghiul cu aza ox e arcangenta pantei
        return math.atan(self.panta())

    def intersectie(self, other):
        # Verificăm dacă prima linie este verticală
        if self.p1.x == self.p2.x:  # Line 1 is vertical
            x_intersect = self.p1.x
            if other.p1.x == other.p2.x:  # Line 2 is also vertical
                return None  # Both lines are vertical and parallel
            else:
                # Calculate slope of the second line
                a2 = (other.p2.y - other.p1.y) / (other.p2.x - other.p1.x)
                b2 = other.p1.y - a2 * other.p1.x
                # Calculate intersection y-coordinate
                y_intersect = a2 * x_intersect + b2
                return Punct(x_intersect, y_intersect)

        # Verificăm dacă a doua linie este verticală
        if other.p1.x == other.p2.x:  # Line 2 is vertical
            x_intersect = other.p1.x
            a1 = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
            b1 = self.p1.y - a1 * self.p1.x
            # Calculate intersection y-coordinate
            y_intersect = a1 * x_intersect + b1
            return Punct(x_intersect, y_intersect)

        # Calculăm panta pentru fiecare dreaptă
        delta_x1 = self.p2.x - self.p1.x
        delta_y1 = self.p2.y - self.p1.y
        delta_x2 = other.p2.x - other.p1.x
        delta_y2 = other.p2.y - other.p1.y

        # Check for potential division by zero in slope calculation
        if delta_x1 == 0 or delta_x2 == 0:
            return None  # One of the lines is vertical, already handled above

        a1 = delta_y1 / delta_x1
        a2 = delta_y2 / delta_x2

        # Verificăm dacă dreptele sunt paralele (au aceeași pantă)
        if math.isclose(a1, a2, abs_tol=1e-9):
            return None  # Dreptele paralele nu se intersectează

        # ax+b=y -ecuatia generala
        b1 = self.p1.y - a1 * self.p1.x
        b2 = other.p1.y - a2 * other.p1.x

        # Obtinem sist
        # 1. a1*x_intersect+b1=y_intersect
        # 2. a2*x_intersect+b2=y_intersect
        # Scadem cele doua ecuatii si scoatem x
        x_intersect = (b2 - b1) / (a1 - a2)

        # Calculăm coordonata y a punctului de intersecție
        # Incluind in prima ecuatie
        y_intersect = a1 * x_intersect + b1

        # Returnăm punctul de intersecție sub forma unui obiect Punct
        return Punct(x_intersect, y_intersect)

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