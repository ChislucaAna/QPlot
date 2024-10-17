import math

class Complex:
    def __init__(self, real=0, imag=0):
        if isinstance(real, str):
            self.real, self.imag = self.from_string(real)
        else:
            self.real = real
            self.imag = imag
    
    @staticmethod
    def from_string(s):
        s = s.replace(" ", "").rstrip('ij')
        last_plus = s.rfind('+')
        last_minus = s.rfind('-')

        if last_plus == -1 and last_minus == -1:
            return real(s), 0

        split_pos = max(last_plus, last_minus)
        real_part = s[:split_pos]
        imag_part = s[split_pos:]
        return int(real_part), int(imag_part)

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real + other, self.imag)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other + self.real, self.imag)
        return NotImplemented
       
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real - other, self.imag)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other - self.real, -self.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imag * other.imag,
                           self.real * other.imag + self.imag * other.real)
        elif isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            numitor = other.real ** 2 + other.imag ** 2
            if numitor != 0:
                return Complex((self.real * other.real + self.imag * other.imag) / numitor,
                               (self.imag * other.real - self.real * other.imag) / numitor)
            else:
                raise(ZeroDivisionError)
        elif isinstance(other, (int, float)) and other != 0:
            return Complex(self.real / other, self.imag / other)

        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return Complex(other * self.real / (self.real ** 2 + self.imag ** 2),
                           -other * self.imag / (self.real ** 2 + self.imag ** 2))
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def pow(self, n): #nr complexe sub forma trigonometrica
        #formula lui Moivre
        #z^n=r^n(cos nt + i sin nt)
        #r e modulul numarului
        #iar t este unghiul pe care il face numarul cu axa Ox
        r = abs(self)

        #functia asta returneaza unghiul in cadranul bun
        #chiar si pt puncte care nu is in -pi/2,pi/2
        #spre deosebire de atan are quadrant awareness
        theta = math.atan2(self.imag, self.real)

        r_pow_n = r ** n
        n_theta = n * theta
        
        real_part = r_pow_n * math.cos(n_theta)
        imag_part = r_pow_n * math.sin(n_theta)

        return Complex(real_part, imag_part)
