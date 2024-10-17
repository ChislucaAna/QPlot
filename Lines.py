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
        # Calculăm panta pentru fiecare dreaptă
        a1 = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        a2 = (other.p2.y - other.p1.y) / (other.p2.x - other.p1.x)
        
        # Verificăm dacă dreptele sunt paralele (au aceeași pantă)
        if a1 == a2:
            return None  # Dreptele paralele nu se intersectează
        
        # ax+b=y -ecuatia generala
        #in particular :a*x_dat+b=y_dat
        #=>b=y_dat-a*x_dat
        b1 = self.p1.y - a1 * self.p1.x
        b2 = other.p1.y - a2 * other.p1.x
        
        #obtinem sist
        #1. a1*x_intersect+b1=y_intersect
        #2. a2*x_intersect+b2=y_intersect
        #scadem cele doua ecuatii si scoatem x
        x_intersect = (b2 - b1) / (a1 - a2)
        
        # Calculăm coordonata y a punctului de intersecție
        #incluind in prima ecuatie
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