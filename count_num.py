import re

# Input a paragraph
paragraph = input("Enter a paragraph: ")

# Count the number of sentences
# Sentences end with '.', '!', or '?'
sentences = re.split(r'[.!?]', paragraph)
sentence_count = len([s for s in sentences if s.strip()])  # Ignore empty strings

# Count the number of words
words = paragraph.split()
word_count = len(words)

# Capitalize all words starting with 'm'
updated_paragraph = ' '.join([word.capitalize() if word.lower().startswith('m') else word for word in words])

# Replace the word "students" with "CMSA-Sem V Students"
final_paragraph = updated_paragraph.replace("students", "CMSA-Sem V Students")

# Output results
print("\nProcessed Results:")
print(f"Number of sentences: {sentence_count}")
print(f"Number of words: {word_count}")
print("\nUpdated Paragraph:")
print(final_paragraph)
