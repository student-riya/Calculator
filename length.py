def find_smallest_and_longest(words):
    if not words:
        return "N/A", "N/A", 0, 0  # Handle empty input case

    smallest = min(words, key=len)
    longest = max(words, key=len)

    return smallest, longest, len(smallest), len(longest)

# Take input from the user
words_list = input("Enter words separated by space: ").split()

# Process words
smallest, longest, small_len, long_len = find_smallest_and_longest(words_list)

# Display results
print(f"Smallest Word: '{smallest}' (Length: {small_len})")
print(f"Longest Word: '{longest}' (Length: {long_len})")