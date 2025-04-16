# Initial dictionary
d1 = {1: 'a', 2: 'a', 4: [1, 2]}

# Invert the dictionary
d2 = {}
for key, value in d1.items():
    # If the value is mutable (like a list), convert it to a frozenset
    if isinstance(value, list):
        value = frozenset(value)
    # If the value already exists as a key in the inverted dictionary, append the new key to the list
    if value in d2:
        if isinstance(d2[value], list):
            d2[value].append(key)
        else:
            d2[value] = [d2[value], key]  # Convert to list if not already
    else:
        d2[value] = key

# Print results
print("Original Dictionary:", d1)
print("Inverted Dictionary:", d2)
