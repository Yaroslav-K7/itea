class Complex:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real}+{self.imag}j"
        else:
            return f"{self.real}-{abs(self.imag)}j"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        return Complex(((self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2)),
                       ((self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)))
