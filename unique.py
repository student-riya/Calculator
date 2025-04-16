#For a list of numbers
numbers = [1,2,2,3,4,4,5]
unique_numbers = list(set(numbers)) #convert back to list if needed
print("Unique numbers:", unique_numbers)

#For a string
text = "helloworld"
unique_characters = ''.join(set(text)) #join unique characters back into a string
print("Unique characters in string:", unique_characters)