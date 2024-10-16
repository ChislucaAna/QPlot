import math

class Complex:
    def __init__(self, real=0, imaginar=0):
        if isinstance(real, str):
            self.real, self.imaginar = self.from_string(real)
        else:
            self.real = real
            self.imaginar = imaginar
    
    @staticmethod
    def from_string(s): #metodele statice nu au referinta self si nu lucreaza cu obiecte din acea clasa
        #scoatem spatiile extra din string pt parsare mai usoara
        s = s.replace(" ", "").rstrip('i')
        #gaseste minus sau plus
        last_plus = s.rfind('+')
        last_minus = s.rfind('-')
        #determina pozitia de split
        split_pos = max(last_plus, last_minus)
        #totul inainte de pozitia de split e partea reala, totul dupa e imaginar
        real_part = s[:split_pos]
        imag_part = s[split_pos:]
        #converteste in int cele doua parti pt a creea instanta
        return int(real_part), int(imag_part)

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imaginar + other.imaginar)
        elif isinstance(other, (int, float)):
            return Complex(self.real + other, self.imaginar)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other + self.real, self.imaginar)
        return NotImplemented
       
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imaginar - other.imaginar)
        elif isinstance(other, (int, float)):
            return Complex(self.real - other, self.imaginar)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other - self.real, -self.imaginar)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imaginar * other.imaginar,
                           self.real * other.imaginar + self.imaginar * other.real)
        elif isinstance(other, (int, float)):
            return Complex(self.real * other, self.imaginar * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real * other, self.imaginar * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            numitor = other.real ** 2 + other.imaginar ** 2
            if numitor != 0:
                return Complex((self.real * other.real + self.imaginar * other.imaginar) / numitor,
                               (self.imaginar * other.real - self.real * other.imaginar) / numitor)
        elif isinstance(other, (int, float)) and other != 0:
            return Complex(self.real / other, self.imaginar / other)

        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return Complex(other * self.real / (self.real ** 2 + self.imaginar ** 2),
                           -other * self.imaginar / (self.real ** 2 + self.imaginar ** 2))
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imaginar}i"

    def __eq__(self, other):
        return self.real == other.real and self.imaginar == other.imaginar

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginar ** 2)