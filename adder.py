class Adder:
    def __init__(self):
        self.sum = 0
        self.carry = 0

class HalfAdder(Adder):
    def __init__(self):
        super().__init__()

    def calculate(self, a, b):
        # XOR for sum, AND for carry
        self.sum = a ^ b
        self.carry = a & b
        return self.sum, self.carry

class FullAdder(Adder):
    def __init__(self):
        super().__init__()

    def calculate(self, a, b, cin):
        # Sum = XOR of inputs and carry-in
        self.sum = a ^ b ^ cin
        # Carry = (a AND b) OR (cin AND (a XOR b))
        self.carry = (a & b) | (cin & (a ^ b))
        return self.sum, self.carry

def main():
    print("Choose the adder type:")
    print("1. Half Adder")
    print("2. Full Adder")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        a = int(input("Enter first binary digit (0 or 1): "))
        b = int(input("Enter second binary digit (0 or 1): "))
        if a not in [0, 1] or b not in [0, 1]:
            print("Invalid input. Please enter 0 or 1.")
            return

        half_adder = HalfAdder()
        result_sum, result_carry = half_adder.calculate(a, b)
        print(f"Half Adder Result:\nSum: {result_sum}, Carry: {result_carry}")

    elif choice == 2:
        a = int(input("Enter first binary digit (0 or 1): "))
        b = int(input("Enter second binary digit (0 or 1): "))
        cin = int(input("Enter carry-in (0 or 1): "))
        if a not in [0, 1] or b not in [0, 1] or cin not in [0, 1]:
            print("Invalid input. Please enter 0 or 1.")
            return

        full_adder = FullAdder()
        result_sum, result_carry = full_adder.calculate(a, b, cin)
        print(f"Full Adder Result:\nSum: {result_sum}, Carry: {result_carry}")

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
