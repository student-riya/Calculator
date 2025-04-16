class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"

if __name__ == "__main__":
    real1 = float(input("Enter real part of first complex number: "))
    imag1 = float(input("Enter imaginary part of first complex number: "))
    num1 = ComplexNumber(real1, imag1)
    
    real2 = float(input("Enter real part of second complex number: "))
    imag2 = float(input("Enter imaginary part of second complex number: "))
    num2 = ComplexNumber(real2, imag2)
    
    print(f"Sum: {num1 + num2}")
    print(f"Product: {num1 * num2}")