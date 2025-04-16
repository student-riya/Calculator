import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sine_series(x, terms):
    x = math.radians(x)  # Convert degrees to radians
    sine_value = 0
    
    for i in range(terms):
        sign = (-1) ** i
        term = sign * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sine_value += term
    
    return sine_value

# Taking input from the user
angle = float(input("Enter the angle in degrees: "))
terms = int(input("Enter the number of terms: "))

# Calculate sine using series
result = sine_series(angle, terms)

# Display result
print(f"sin({angle}) ≈ {result}")
