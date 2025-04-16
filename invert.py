# Initial dictionary
d1 = {1: 'a', 2: 'b', 3: 120}

# Invert the dictionary
d2 = {value: key for key, value in d1.items()}

# Print the result
print("Original Dictionary:", d1)
print("Inverted Dictionary:", d2)
