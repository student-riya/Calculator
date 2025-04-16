#Iterative approach:
# Input two integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Ensure a >= b
if b > a:
    a, b = b, a

# Iterative GCD computation
while b != 0:
    remainder = a % b
    a = b
    b = remainder

# Output the result
print("GCD (iterative):", a)

#Recursive approach:
# Input two integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Recursive function to compute GCD
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

# Output the result
print("GCD (recursive):", gcd_recursive(a, b))
